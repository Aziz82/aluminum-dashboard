#!/usr/bin/env python3
"""schema_v2.py — transform the enriched engine dict (snake_case market_data) into
the new React dashboard data.json contract (camelCase). Faithful, values-only.
Kept as a module so build_data_json.py can call to_dashboard(D)."""
import re

def pnum(s):
    """First finite number in a string; commas/tilde/spaces stripped. None if absent."""
    if s is None: return None
    if isinstance(s,(int,float)): return float(s)
    t = str(s).replace(',','')
    m = re.search(r'[-+]?\d+(?:\.\d+)?', t)
    return float(m.group()) if m else None

def trim(s, n=600):
    return s if not isinstance(s,str) else (s if len(s)<=n else s[:n].rstrip()+'…')

_MON={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
def iso(d):
    """'21-Jul-26' -> '2026-07-21' so the frontend's Date() parses cleanly. Pass-through otherwise."""
    if not isinstance(d,str): return d
    m=re.match(r'(\d{1,2})[- ]([A-Za-z]{3})[- ](\d{2,4})', d.strip())
    if not m: return d
    day=int(m.group(1)); mon=_MON.get(m.group(2).lower()); yr=int(m.group(3))
    if not mon: return d
    yr = 2000+yr if yr<100 else yr
    return f"{yr:04d}-{mon:02d}-{day:02d}"


def to_dashboard(e):
    # ---- meta / soWhat ----
    out = {}
    out['meta'] = {
        'generatedAt': e.get('report_date'),
        'version': 'daily',
        'source': 'Aluminium Market Intelligence Engine — public sources',
        'timezone': 'Asia/Riyadh (UTC+3)',
    }
    sw = e.get('so_what',{})
    out['soWhat'] = {'headline': sw.get('line'), 'bullets': sw.get('points',[])}

    # ---- kpis (from benchmark: numeric cur/prev/avg) ----
    kpis=[]
    for b in e.get('benchmark',[]):
        cur=b.get('cur'); prev=b.get('prev')
        name=b.get('name','')
        unit='t' if 'stock' in name.lower() else '$/t'
        delta = (cur-prev) if (isinstance(cur,(int,float)) and isinstance(prev,(int,float))) else None
        dpct = (delta/prev*100) if (delta is not None and prev) else None
        direction = 'flat'
        if delta is not None:
            direction = 'up' if delta>0 else ('down' if delta<0 else 'flat')
        kpis.append({
            'id': re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-'),
            'label': name, 'value': cur, 'unit': unit,
            'delta': round(delta,2) if delta is not None else None,
            'deltaPct': round(dpct,2) if dpct is not None else None,
            'direction': direction, 'note': trim(b.get('note'),400),
        })
    out['kpis']=kpis

    # ---- lme ----
    bm = {b.get('name'):b for b in e.get('benchmark',[])}
    cash = next((b for n,b in bm.items() if 'cash' in (n or '').lower()), {})
    threeM = next((b for n,b in bm.items() if '3-month' in (n or '').lower() or '3m' in (n or '').lower()), {})
    series=[]
    for row in e.get('lme_series',[]):
        # [date, cash, 3m, stock]
        if len(row)>=4:
            series.append({'date':iso(row[0]), 'price':row[1], 'stock':row[3]})
    series = list(reversed(series))  # chronological
    out['lme'] = {
        'benchmark': {
            'cash': cash.get('cur'), 'threeMonth': threeM.get('cur'),
            'average': cash.get('avg'), 'unit':'$/t',
            'commentary': trim(e.get('lme_commentary'),500),
        },
        'series': series,
    }

    # ---- baseMetals ----
    SYM={'aluminium':'AL','aluminum':'AL','copper':'CU','nickel':'NI','zinc':'ZN','lead':'PB'}
    mh=e.get('metals_history',{})
    labels=mh.get('labels',[])
    histmap={'AL':mh.get('al',[]),'CU':mh.get('cu',[]),'NI':mh.get('ni',[])}
    bmetals=[]
    for m in e.get('metals_board',[]):
        nm=m.get('name',''); sym=SYM.get(nm.lower(),nm[:2].upper())
        hist=[]
        arr=histmap.get(sym)
        if arr and labels and len(arr)==len(labels):
            hist=[{'date':labels[i],'value':arr[i]} for i in range(len(arr))]
        bmetals.append({'symbol':sym,'name':nm,'price':m.get('price'),
                        'dayPct':m.get('day'),'ytdPct':m.get('ytd'),'history':hist})
    out['baseMetals']=bmetals

    # ---- premiums ----
    reg=[]
    for p in e.get('premiums',[]):
        cur=p.get('cur'); prev=p.get('prev')
        chg=(cur-prev) if isinstance(cur,(int,float)) and isinstance(prev,(int,float)) else None
        reg.append({'region':p.get('name'),'premium':cur,'unit':'$/t',
                    'change':round(chg,1) if chg is not None else None,
                    'status':('up' if (chg or 0)>0 else 'down' if (chg or 0)<0 else 'flat')})
    quarterly=[]
    for q in e.get('premium_quarters',[]):
        note=None
        if q.get('v') is None and q.get('range'):
            note=f"Range ${q['range'][0]}–${q['range'][1]}/t"
        quarterly.append({'quarter':q.get('q'),'value':q.get('v'),'note':note})
    pt=e.get('premium_tariff',{})
    tariffs=[]
    if pt:
        if pt.get('us_rate') is not None:
            tariffs.append({'label':'US Section 232 (aluminium)','rate':f"{pt['us_rate']*100:.0f}%",
                            'note':'Full customs value; eff. 08-Jun-2026 → 31-Dec-2027'})
        if pt.get('eu_duty') is not None:
            tariffs.append({'label':'EU import duty (P1020A)','rate':f"{pt['eu_duty']*100:.0f}%",
                            'note':'Structural floor plus CBAM'})
        if pt.get('us_dp_match'):
            tariffs.append({'label':pt['us_dp_match'],'rate':'ref','note':'US duty-paid benchmark'})
    drivers=[]
    for d in e.get('premium_drivers',[]):
        src=d.get('src'); srctxt = src[0] if isinstance(src,list) and src else (src if isinstance(src,str) else None)
        drivers.append({'title':d.get('t'),'detail':trim(d.get('d'),500),'source':srctxt})
    out['premiums']={'regional':reg,'quarterly':quarterly,'tariffs':tariffs,'drivers':drivers}

    # ---- alumina (alumina board + raw_materials feedstock) ----
    al_items=[]
    for a in e.get('alumina',[]):
        al_items.append({'name':a.get('name'),'price':pnum(a.get('val')),'unit':a.get('unit'),
                         'changePct':None,'note':trim(a.get('src'),400)})
    for a in e.get('raw_materials',[]):
        al_items.append({'name':a.get('name'),'price':pnum(a.get('val')),'unit':a.get('unit'),
                         'changePct':None,'note':trim(a.get('src'),400)})
    ah=e.get('alumina_history',{})
    al_hist=[]
    if ah.get('labels') and ah.get('fob') and len(ah['labels'])==len(ah['fob']):
        al_hist=[{'date':ah['labels'][i],'value':ah['fob'][i]} for i in range(len(ah['fob']))]
    out['alumina']={'items':al_items,'history':al_hist}

    # ---- inputs ----
    in_items=[]
    for it in e.get('inputs',[]):
        in_items.append({'name':it.get('name'),'value':pnum(it.get('val')),'unit':it.get('unit'),
                         'changePct':None,'status':it.get('risk')})
    log=e.get('logistics',[])
    hormuz=next((l for l in log if 'hormuz' in (l.get('name','').lower())), log[0] if log else {})
    out['inputs']={'items':in_items,'hormuz':{'status':hormuz.get('val'),'detail':trim(hormuz.get('note'),400)}}

    # ---- macro ----
    mrow=[]
    for m in e.get('macro',[]):
        nm=m.get('name',''); unit=None
        um=re.search(r'\(([^)]+)\)',nm)
        if um: unit=um.group(1)
        mrow.append({'label':re.sub(r'\s*\([^)]*\)','',nm).strip(),'value':pnum(m.get('value')),
                     'unit':unit,'changePct':m.get('day')})
    mevents=[]
    for f in e.get('feed',[]):
        txt=f.get('text',''); title=txt.split(':')[0] if ':' in txt[:80] else txt[:60]
        mevents.append({'date':f.get('when'),'title':title,'detail':trim(txt,400),'impact':f.get('impact')})
    out['macro']={'row':mrow,'events':mevents}

    # ---- elliottWave ----
    def nearest_idx(pts_t, t):
        return min(range(len(pts_t)), key=lambda i: abs(pts_t[i]-t)) if pts_t else 0

    def map_panel(panel):
        if not panel: return None
        # price path: prefer 'line', else 'waves'
        if panel.get('line'):
            pts=[{'t':x[0],'date':f"{x[0]:.3f}",'price':x[1]} for x in panel['line']]
        elif panel.get('waves'):
            pts=[{'t':w['t'],'date':f"{w['t']:.3f}",'price':w['p']} for w in panel['waves']]
        else:
            pts=[]
        pts_t=[p['t'] for p in pts]
        points=[{'date':p['date'],'price':p['price']} for p in pts]
        waves=[]
        for w in panel.get('waves',[]):
            idx=nearest_idx(pts_t, w['t'])
            waves.append({'label':w['w'],'index':idx})
        fib=[{'label':f['l'],'value':f['p']} for f in panel.get('fib',[])]
        proj=panel.get('proj',{}) or {}
        projections={}
        for sc in ('bull','base','bear'):
            if proj.get(sc):
                projections[sc]=[{'date':f"{x[0]:.3f}",'price':x[1]} for x in proj[sc]]
        targets={}
        for sc in ('bull','base','bear'):
            p=proj.get(sc)
            if p and len(p)>=2:
                vals=sorted([p[-1][1],p[-2][1]])
                targets[sc]={'low':vals[0],'high':vals[1]}
        # long-term base target can also use 'zone'
        if 'base' not in targets and panel.get('zone') and len(panel['zone'])==2:
            z=sorted(panel['zone']); targets['base']={'low':z[0],'high':z[1],'note':'projection zone'}
        return {'title':panel.get('label'),'unit':'$/t','points':points,'waves':waves,
                'fibLevels':fib,'projections':projections,'targets':targets}

    ew=e.get('ew',{})
    out['elliottWave']={'longTerm':map_panel(ew.get('long_term')),'shortTerm':map_panel(ew.get('short_term'))}

    # ---- news ----
    SENT={'bullish':'bullish','bearish':'bearish','positive':'bullish','negative':'bearish'}
    news=[]
    for n in e.get('news',[]):
        imp=(n.get('impact') or '').lower()
        news.append({'time':n.get('horizon'),'title':n.get('headline'),'source':n.get('source'),
                     'sentiment':SENT.get(imp,'neutral')})
    out['news']=news

    # ---- peers (from earnings; financial numerics not in engine → null) ----
    peers=[]
    for p in e.get('earnings',[]):
        comp=p.get('company',''); tk=None
        tm=re.search(r'\(([^)]+)\)',comp)
        if tm: tk=tm.group(1)
        peers.append({'company':re.sub(r'\s*\([^)]*\)','',comp).strip(),'ticker':tk,
                      'group':p.get('group'),'period':p.get('period'),
                      'headline':trim(p.get('headline'),320),'readthrough':trim(p.get('readthrough'),320),
                      'sentiment':p.get('sentiment'),
                      'eps':None,'revenue':None,'margin':None,'ytdPct':None})
    out['peers']=peers

    # ---- outlook ----
    o=e.get('outlook',{})
    catalysts=[]
    for c in o.get('catalysts',[]):
        catalysts.append(f"{c.get('date','')}: {c.get('event','')}".strip(': ').strip())
    risks=[]
    TREND={'up':'rising','down':'falling','flat':'stable'}
    for r in o.get('risks',[]):
        risks.append({'title':trim(r.get('risk'),260),'likelihood':(r.get('likelihood') or '').lower(),
                      'impact':(r.get('impact') or '').lower(),'trend':TREND.get((r.get('trend') or '').lower(),r.get('trend')),
                      'detail':''})
    out['outlook']={'consensus':trim(e.get('net_read'),500),'catalysts':catalysts,'risks':risks}

    # ---- sources / caveats ----
    srcs=[]
    for s in e.get('sources',[]):
        if isinstance(s,list) and len(s)>=2:
            srcs.append({'label':s[0],'note':s[1]})
        elif isinstance(s,list) and s:
            srcs.append({'label':s[0],'note':None})
    out['sources']=srcs
    cav=e.get('caveats',[])
    out['caveats']=' · '.join(cav) if isinstance(cav,list) else cav
    return out
