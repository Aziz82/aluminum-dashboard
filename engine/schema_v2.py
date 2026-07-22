#!/usr/bin/env python3
"""schema_v2.py — Map the enriched engine dict (snake_case market_data.json) into the Web_v3
dashboard data.json contract. Faithful: real values only, no fabrication.
Exposes to_dashboard(e) -> dict. Standalone run maps /home/claude/market_data.json."""
import json, re, datetime

_MON = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def pnum(s):
    if s is None: return None
    if isinstance(s,(int,float)): return float(s)
    m = re.search(r'[-+]?\d+(?:\.\d+)?', str(s).replace(',',''))
    return float(m.group()) if m else None

def trim(s, n=320):
    return s if not isinstance(s,str) else (s if len(s)<=n else s[:n].rstrip()+'…')

def iso(d):
    if not isinstance(d,str): return d
    m = re.match(r'(\d{1,2})[- ]([A-Za-z]{3})[- ](\d{2,4})', d.strip())
    if not m: return d
    day=int(m.group(1)); mon=_MON.get(m.group(2).lower()); yr=int(m.group(3))
    if not mon: return d
    yr = 2000+yr if yr<100 else yr
    return f"{yr:04d}-{mon:02d}-{day:02d}"

def _asof_date(e):
    rd = e.get('report_date')
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', str(rd) or '')
    if m: return datetime.date(int(m.group(1)),int(m.group(2)),int(m.group(3)))
    return datetime.date(2026,7,22)

def _dates_back(end, n, step_days):
    return [(end - datetime.timedelta(days=step_days*(n-1-i))).isoformat() for i in range(n)]

def _dates_fwd(start, n, step_days):
    return [(start + datetime.timedelta(days=step_days*i)).isoformat() for i in range(n)]

def _rag_from_risk(r):
    r = (r or '').lower()
    if 'high' in r: return 'red'
    if 'med' in r: return 'amber'
    if 'low' in r: return 'green'
    return None

def _nearest(ts, t):
    return min(range(len(ts)), key=lambda i: abs(ts[i]-t)) if ts else 0

def _peer_eps(t):
    """Adjusted/reported EPS in $ only (skips non-$ subunits like fils)."""
    if not t: return None
    m = re.search(r'EPS\s*\$\s*([0-9]+\.?[0-9]*)', t, re.I)
    return float(m.group(1)) if m else None

def _peer_rev_bn(t):
    """Revenue in $bn ($m converted). Ignores non-$ (SAR/₹/RMB/¥) figures."""
    if not t: return None
    m = re.search(r'[Rr]evenue[^.]{0,18}?\$([0-9]+\.?[0-9]*)\s*bn', t)
    if m: return round(float(m.group(1)), 3)
    m = re.search(r'[Rr]evenue[^.]{0,18}?\$([0-9]+\.?[0-9]*)\s*m', t)
    if m: return round(float(m.group(1))/1000, 3)
    return None

def _peer_yoy(t):
    """Headline YoY %: explicit YoY/y-y first; else first '+X%' that is NOT q/q.
    Ranges → midpoint. Real sourced figures only."""
    if not t: return None
    m = re.search(r'\+?\s*([0-9]+\.?[0-9]*)\s*(?:[–-]\s*([0-9]+\.?[0-9]*)\s*)?%\s*(?:YoY|y/y)', t, re.I)
    if m:
        lo=float(m.group(1)); hi=float(m.group(2)) if m.group(2) else None
        return round((lo+hi)/2,1) if hi else lo
    for mm in re.finditer(r'\+\s*>?\s*([0-9]+\.?[0-9]*)\s*(?:[–-]\s*([0-9]+\.?[0-9]*)\s*)?%(\s*q/q)?', t):
        if mm.group(3): continue  # exclude quarter-on-quarter
        lo=float(mm.group(1)); hi=float(mm.group(2)) if mm.group(2) else None
        return round((lo+hi)/2,1) if hi else lo
    return None


def _map_panel(panel, pid, asof, weekly):
    if not isinstance(panel, dict): return None
    step = 7 if weekly else 1
    # price path: 'line' [[t,p]] preferred, else 'waves' [{t,p,w}]
    if panel.get('line'):
        path = [(x[0], x[1]) for x in panel['line'] if isinstance(x,(list,tuple)) and len(x)>=2]
    elif panel.get('waves'):
        path = [(w['t'], w['p']) for w in panel['waves'] if isinstance(w,dict) and 't' in w and 'p' in w]
    else:
        path = []
    ts = [t for t,_ in path]
    price = [p for _,p in path]
    n = len(price)
    hist_dates = _dates_back(asof, n, step) if n else []
    # wave labels → index into history price
    wave_labels = []
    for w in panel.get('waves', []):
        if not isinstance(w, dict): continue
        idx = _nearest(ts, w.get('t', 0)) if ts else 0
        wave_labels.append({'index': idx, 'label': str(w.get('w','')), 'position': 'top'})
    fib = [{'label': f.get('l'), 'value': f.get('p')} for f in panel.get('fib', [])
           if isinstance(f, dict) and f.get('p') is not None]
    proj = panel.get('proj', {}) or {}
    last_price = price[-1] if price else None
    scenarios, zones = [], []
    order = [k for k in ('base','bull','bear') if k in proj] + [k for k in proj if k not in ('base','bull','bear')]
    max_len = 0
    for sc in order:
        pts = [pt[1] for pt in proj[sc] if isinstance(pt,(list,tuple)) and len(pt)>=2]
        if not pts: continue
        if last_price is not None:
            pts = [last_price] + pts[1:] if len(pts) > 1 else [last_price]
        max_len = max(max_len, len(pts))
        scenarios.append({'id': sc, 'label': sc.capitalize(),
                          'summary': None, 'points': pts})
        if len(pts) >= 2:
            lo, hi = sorted([pts[-1], pts[-2]])
            zones.append({'low': lo, 'high': hi, 'label': f'{sc.capitalize()} target', 'scenario': sc})
    # long-term 'zone' as base target if base absent
    if 'base' not in [z['scenario'] for z in zones] and isinstance(panel.get('zone'), list) and len(panel['zone'])==2:
        z = sorted(panel['zone']); zones.append({'low': z[0], 'high': z[1], 'label': 'Base zone', 'scenario': 'base'})
    proj_dates = _dates_fwd(asof, max_len, step) if max_len else []
    return {
        'id': pid, 'title': panel.get('label') or pid, 'timeframe': panel.get('fwd_label') or ('Weekly' if weekly else 'Daily'),
        'history': {'dates': hist_dates, 'price': price},
        'projection_dates': proj_dates,
        'wave_labels': wave_labels, 'fib_levels': fib,
        'target_zones': zones, 'scenarios': scenarios,
    }


def to_dashboard(e):
    asof = _asof_date(e)
    out = {}
    # meta / brief
    out['meta'] = {'generated_at': e.get('generated') or (e.get('report_date')),
                   'as_of': e.get('report_date'), 'engine_version': 'daily',
                   'timezone': 'Asia/Riyadh (UTC+3)'}
    sw = e.get('so_what', {}) or {}
    out['brief'] = {'headline': sw.get('line'), 'bullets': sw.get('points', [])}

    # kpis from benchmark (numeric)
    kpis = []
    for b in e.get('benchmark', []):
        cur, prev = b.get('cur'), b.get('prev')
        name = b.get('name', '')
        is_stock = 'stock' in name.lower(); is_spread = 'spread' in name.lower() or 'cash-3m' in name.lower()
        chg = ((cur-prev)/prev*100) if isinstance(cur,(int,float)) and isinstance(prev,(int,float)) and prev else None
        trend = 'flat'
        if isinstance(cur,(int,float)) and isinstance(prev,(int,float)):
            trend = 'up' if cur>prev else ('down' if cur<prev else 'flat')
        kpis.append({'id': re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-'), 'label': name,
                     'value': cur, 'unit': 't' if is_stock else '$/t',
                     'change_pct': round(chg,2) if chg is not None else None,
                     'trend': trend, 'note': trim(b.get('note'), 160),
                     'decimals': 0 if is_stock else (1 if is_spread else 1)})
    out['kpis'] = kpis

    # lme
    bench_rows = []
    bm = {b.get('name'): b for b in e.get('benchmark', [])}
    cash = next((b for n,b in bm.items() if 'cash' in (n or '').lower()), {})
    thr  = next((b for n,b in bm.items() if '3-month' in (n or '').lower() or '3m' in (n or '').lower()), {})
    spr  = next((b for n,b in bm.items() if 'spread' in (n or '').lower()), {})
    al_spread = spr.get('cur')
    bench_rows.append({'metal':'Aluminium','cash':cash.get('cur'),'three_month':thr.get('cur'),
                       'average':cash.get('avg'),'spread':al_spread,
                       'structure':('Backwardation' if (al_spread or 0)>0 else 'Contango') if al_spread is not None else None})
    for m in e.get('metals_board', []):
        nm = m.get('name','')
        if nm.lower().startswith('alum'): continue
        bench_rows.append({'metal':nm,'three_month':m.get('price')})
    series = e.get('lme_series', []) or []
    ser = list(reversed(series))
    out['lme'] = {'commentary': trim(e.get('lme_commentary'), 400),
                  'benchmarks': bench_rows,
                  'series': {'dates':[iso(r[0]) for r in ser if len(r)>=4],
                             'price':[r[1] for r in ser if len(r)>=4],
                             'stocks':[r[3] for r in ser if len(r)>=4]}}

    # base_metals
    SYM = {'aluminium':'AL','aluminum':'AL','copper':'CU','nickel':'NI','zinc':'ZN','lead':'PB'}
    board = [{'symbol':SYM.get(m.get('name','').lower(), m.get('name','')[:2].upper()),
              'name':m.get('name'),'price':m.get('price'),'day_pct':m.get('day'),'ytd_pct':m.get('ytd')}
             for m in e.get('metals_board', [])]
    mh = e.get('metals_history', {}) or {}
    hseries = {}
    for sym,key in (('AL','al'),('CU','cu'),('NI','ni')):
        if mh.get(key): hseries[sym] = mh[key]
    out['base_metals'] = {'board': board,
                          'history': {'dates': mh.get('labels', []), 'rebased_base': 100, 'series': hseries}}

    # premiums
    reg = []
    for p in e.get('premiums', []):
        cur, prev = p.get('cur'), p.get('prev')
        chg = (cur-prev) if isinstance(cur,(int,float)) and isinstance(prev,(int,float)) else None
        reg.append({'region':p.get('name'),'premium':cur,'unit':'$/t',
                    'change':round(chg,1) if chg is not None else None,
                    'basis':trim(p.get('src'),60),
                    'status':('amber' if (chg or 0)>0 else 'green')})
    ph = e.get('premium_history', {}) or {}
    settlements = []
    labels = ph.get('labels_reg', [])
    for i,q in enumerate(labels):
        row = {'quarter': q}
        if i < len(ph.get('mjp',[])): row['MJP'] = ph['mjp'][i]
        if i < len(ph.get('cif',[])): row['CIF Japan'] = ph['cif'][i]
        if i < len(ph.get('edu',[])): row['EU duty-unpaid'] = ph['edu'][i]
        settlements.append(row)
    pt = e.get('premium_tariff', {}) or {}
    tariffs = []
    if pt.get('us_rate') is not None:
        tariffs.append({'region':'United States','rate':f"{pt['us_rate']*100:.0f}%",'instrument':'Section 232',
                        'status':'amber','note':'Full customs value; eff. 08-Jun-2026 → 31-Dec-2027'})
    if pt.get('eu_duty') is not None:
        tariffs.append({'region':'European Union','rate':f"{pt['eu_duty']*100:.0f}% + CBAM",'instrument':'Import duty',
                        'status':'amber','note':'Structural floor plus carbon border adjustment'})
    drivers = []
    for d in e.get('premium_drivers', []):
        src = d.get('src'); srctxt = src[0] if isinstance(src,list) and src else (src if isinstance(src,str) else None)
        drivers.append({'text': trim((d.get('t','') + ' — ' + (d.get('d') or '')).strip(' —'), 300), 'source': srctxt})
    out['premiums'] = {'regional':reg,'settlements':settlements,'tariffs':tariffs,'drivers':drivers}

    # alumina (+ raw_materials feedstock)
    prices = []
    for a in e.get('alumina', []):
        prices.append({'label':a.get('name'),'value':pnum(a.get('val')),'unit':a.get('unit'),
                       'note':trim(a.get('src'),160),'status':None})
    for a in e.get('raw_materials', []):
        prices.append({'label':a.get('name'),'value':pnum(a.get('val')),'unit':a.get('unit'),
                       'note':trim(a.get('src'),160),'status':None})
    ah = e.get('alumina_history', {}) or {}
    ahser = {}
    if ah.get('fob'): ahser['FOB Australia ($/t)'] = ah['fob']
    if ah.get('api'): ahser['API ex-China ($/t)'] = ah['api']
    out['alumina'] = {'prices':prices,'notes':e.get('alumina_notes', []),
                      'history':{'dates':ah.get('labels', []),'series':ahser}}

    # inputs
    items = []
    for it in e.get('inputs', []):
        items.append({'label':it.get('name'),'value':pnum(it.get('val')),'unit':it.get('unit'),
                      'note':trim(it.get('src'),160),'status':_rag_from_risk(it.get('risk'))})
    logistics = []
    for l in e.get('logistics', []):
        tr = (l.get('trend') or '').lower()
        logistics.append({'label':l.get('name'),'status':('red' if tr=='up' else 'green' if tr=='down' else 'amber'),
                          'note':trim(l.get('note'),200)})
    out['inputs'] = {'items':items,'logistics':logistics}

    # macro
    row = []
    for m in e.get('macro', []):
        nm = m.get('name',''); um = re.search(r'\(([^)]+)\)', nm)
        row.append({'label':re.sub(r'\s*\([^)]*\)','',nm).strip(),'value':pnum(m.get('value')),
                    'unit':um.group(1) if um else None,'day_pct':m.get('day'),
                    'status':None})
    IMP = {'positive':'medium','negative':'medium','high':'high'}
    events = []
    for f in e.get('feed', []):
        txt = f.get('text',''); title = txt.split(':')[0] if ':' in txt[:80] else txt[:60]
        events.append({'date':f.get('when'),'event':title,'importance':IMP.get((f.get('impact') or '').lower(),'medium'),
                       'note':trim(txt,200)})
    out['macro'] = {'row':row,'events':events}

    # elliott_wave
    ew = e.get('ew', {}) or {}
    panels = []
    lt = _map_panel(ew.get('long_term'), 'al_weekly', asof, True)
    st = _map_panel(ew.get('short_term'), 'al_daily', asof, False)
    for p in (lt, st):
        if p: panels.append(p)
    out['elliott_wave'] = {'panels':panels}

    # news
    heads = []
    for n in e.get('news', []):
        heads.append({'ts':None,'title':n.get('headline'),'source':n.get('source'),'tag':n.get('theme')})
    out['news'] = {'headlines':heads}

    # peers (qualitative note; engine lacks numeric peer financials)
    earnings = []
    for p in e.get('earnings', []):
        comp = p.get('company',''); tm = re.search(r'\(([^)]+)\)', comp)
        note = ' '.join(x for x in [p.get('headline'), p.get('readthrough')] if x)
        earnings.append({'company':re.sub(r'\s*\([^)]*\)','',comp).strip(),
                         'ticker':tm.group(1) if tm else None,'period':p.get('period'),
                         'eps':_peer_eps(note),'revenue_bn':_peer_rev_bn(note),'yoy_pct':_peer_yoy(note),
                         'note':trim(note, 300)})
    out['peers'] = {'earnings':earnings}

    # outlook
    o = e.get('outlook', {}) or {}
    consensus = []
    for c in o.get('consensus', []):
        consensus.append({'bank':c.get('source'),'target':pnum(c.get('y2026')),'horizon':'2026',
                          'stance':'neutral'})
    DIR = {'positive':'up','negative':'down','high':'up'}
    catalysts = []
    for c in o.get('catalysts', []):
        catalysts.append({'text':c.get('event'),'date':c.get('date'),
                          'direction':DIR.get((c.get('impact') or '').lower(),'flat')})
    TREND = {'up':'rising','down':'fading','flat':'stable'}
    risks = []
    for r in o.get('risks', []):
        risks.append({'text':trim(r.get('risk'),260),'likelihood':(r.get('likelihood') or '').lower() or None,
                      'impact':(r.get('impact') or '').lower() or None,
                      'trend':TREND.get((r.get('trend') or '').lower())})
    out['outlook'] = {'consensus':consensus,'catalysts':catalysts,'risks':risks}

    # sources
    refs = []
    for s in e.get('sources', []):
        if isinstance(s,list) and len(s)>=2: refs.append({'name':s[0],'url':s[1]})
        elif isinstance(s,list) and s: refs.append({'name':s[0]})
    out['sources'] = {'caveats':e.get('caveats', []),'references':refs}
    return out
