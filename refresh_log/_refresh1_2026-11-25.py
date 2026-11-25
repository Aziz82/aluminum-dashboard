# Daily data refresh - 2026-11-25 (WEDNESDAY, ~02:40 UTC, BEFORE the Wednesday ring). Board ROLLED ONE SESSION to the TUESDAY 24-Nov LME official.
# Cache-busted EN + DE overviews agree on 24-Nov (Al cash 3,120.50 / 3M 2,789.00 / stock 220,350; MTLE 1.09600); Al per-metal table newest row 24-Nov.
# All five metals' stock changes reconcile with 23-Nov. Cash AND 3M both DOWN (same direction); backwardation narrowed to $331.50.
# PRE-REGISTERED TRIGGER FIRED: three-month settled BELOW ~2,803 -> wave (v) now longer than (iii): EW re-label to extended (v); scenario weights 10/35/55 -> 10/30/60.
import json, subprocess
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-25'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-25"; L_ST="Straits Daily Brief - Strait of Hormuz, 25-Nov-2026 (closed; 1 transit on 22-Nov per IMF PortWatch; further tanker attacks reported; Brent $91.09)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$90.28 (-1.22%) on 25-Nov-2026; IEA: Gulf crude exports rebounded to 74% of pre-war levels"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.81 (25-Nov-2026); ~97% probability priced for a 25bp December Fed hike, ~59% for January; PCE report due"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,775.20 (-3.19%) on 24-Nov-2026, 'lowest level this year' (CFD reference); 830 kt 2027 surplus forecast"
S_BW="https://www.alcircle.com/news/lme-aluminium-backwardation-hits-38yr-high-at-405-t-oddo-calls-for-urgent-action-122085"; L_BW="AL Circle - LME aluminium backwardation traded at $405/t, a 38-year high; Oddo BHF calls for LME action; one entity held 50-79% of warrants (24-Nov-2026)"
S_HU="https://www.alcircle.com/news/hubco-explores-300-000-tonne-aluminium-smelter-as-pakistan-looks-to-turn-surplus-electricity-into-industrial-opportunity-122089"; L_HU="AL Circle - HUBCO commissions feasibility study for a 300 ktpa smelter in Pakistan (24-Nov-2026)"
S_CM="https://www.alcircle.com/news/cameroons-minim-martap-bauxite-project-misses-q4-export-target-as-canyon-explores-new-funding-122087"; L_CM="AL Circle - Canyon's Minim-Martap bauxite project (Cameroon) misses Q4-2026 export target (24-Nov-2026)"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3201.5 and B['LME 3-month']['cur']==2834.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3201.5,2834.0,221400            # 23-Nov (previous column)
cash,m3,stk=3120.5,2789.0,220350          # 24-Nov (board)
spr=cash-m3; psp=pc-pm; assert spr==331.5 and psp==367.5 and ps-1050==stk
ytd=(m3/3010.5-1)*100; dc=cash-pc; dm=m3-pm
assert dc==-81.0 and dm==-45.0

VER=("COMPILED WEDNESDAY 25-NOVEMBER-2026 ABOUT 02:40 LONDON - BEFORE TODAY'S LME RING (13:20 LONDON). THE BOARD IS THE TUESDAY 24-NOVEMBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION; it ROLLED ONE SESSION this run (the previous run carried Monday 23-November). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 24-November official for all metals with stocks and FX (EUR/USD MTLE 1.09600; 23-November 1.09460); (2) the aluminium per-metal daily table shows 24-November as its newest row and its 17- to 23-November rows match the stored series; (3) every metal's 24-November stock change reconciles exactly with the stored 23-November stock. "
 "The whole board sits on ONE UNIFORM SESSION (24-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" TUESDAY 24-NOVEMBER (the board): CASH SETTLED $3,120.50, DOWN $81.00 OR 2.53% FROM MONDAY'S $3,201.50. THREE-MONTH SETTLED $2,789.00, DOWN $45.00 OR 1.59% FROM $2,834.00 - BELOW THE 2,830-2,850 ELLIOTT COMPLETION ZONE AND BELOW THE PRE-REGISTERED ~2,803 RE-LABEL LEVEL, the lowest three-month official in this dashboard's 2026 record, and $221.50 BELOW the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION NARROWED TO $331.50 (23-November $367.50, the series widest) - still a twenty-ninth straight backwardation and the eighteenth above $15.00. Cash and three-month fell in the SAME direction, cash faster, so the spread narrowed. "
 "VISIBLE LME STOCK FELL 1,050 t TO 220,350 t - a fourth straight draw, EQUAL to the 17-November series low. The Trading Economics aluminium reference shows about $2,775.20 (-3.19%) for 24-November and describes it as the lowest level this year - a CFD reference cited in text only.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,120.5","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"2,789.0","pos":False,"delta":VER+AL+" THE PRE-REGISTERED ~2,803 LEVEL BROKE ON A SETTLED BASIS: wave (v) from 3,097.50 now measures $308.50, longer than wave (iii) ($294.50) - not a rule break because wave (iii) still exceeds wave (i) ($191), but the count is re-labelled to an EXTENDED wave (v); 1.618 x wave (i) near 2,788 is now met. A settled close back above 2,994.50 would signal a failed break; above 3,097.50 negates the wave (v) count; daily invalidation of the bearish count remains 3,289."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+331.5","pos":True,"delta":VER+f" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,120.50 against three-month $2,789.00 is a $331.50 BACKWARDATION, DOWN from $367.50 on 23-November (the widest in this series). On 24-November cash (-$81.00) and three-month (-$45.00) both fell (same direction), cash faster. It stays above the published $15.00 reversal condition for an eighteenth session and is a twenty-ninth straight backwardation; a contango beyond $24.50 would reverse the structural signal. AL Circle (24-November) reports the cash-to-three-month spread TRADED at $405/t intraday, a 38-year high - a traded figure, not a settled official. The October mean spread was ${oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"220,350","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 1,050 t TO 220,350 t ON 24-NOVEMBER, a fourth straight draw (23-November -2,125 t; 20-November -900 t), now EQUAL to the 17-November series low of 220,350 t. AL Circle reports available stock near its lowest since 1990 and Russian-origin metal at 99.98% of available LME stock at end-October. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 23-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $2,789.00, DOWN $45.00 FROM THE 23-NOVEMBER $2,834.00 - below the 2,830-2,850 zone and the ~2,803 re-label level, $105.00 BELOW the 2,894 weekly 61.8%; $221.50 BELOW the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 1,050 t TO 220,350 t on 24-November - a fourth straight draw, equal to the 17-November series low. AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $331.50 BACKWARDATION, DOWN FROM $367.50 ON 23-NOVEMBER (the widest in this series). CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On 24-November cash (-$81.00) and three-month (-$45.00) moved in the SAME direction. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00, $353.00, $367.50 and $331.50."},
 {"name":"EUR/USD LME fixing","cur":1.096,"prev":1.0946,"avg":1.1465,"note":VER+" THE LME EURO FIXING WAS 1.09600 ON 24-NOVEMBER, UP FROM 1.09460 ON 23-NOVEMBER, with the dollar index near 103.8 (Trading Economics, 25-November). AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (24-Nov official)","price":"3,120.5","basis":"THE TUESDAY 24-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,120.50, DOWN $81.00 OR 2.53% (23-November $3,201.50). Next print Wednesday 25-November 13:20 London."},
 {"tenor":"3-month (24-Nov official)","price":"2,789.0","basis":"THE 24-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $2,789.00, DOWN $45.00 - below the 2,830-2,850 zone and the ~2,803 re-label level; 1.618 x wave (i) near 2,788 met."},
 {"tenor":"Cash-to-3M structure","price":"+331.5 (BACKWARDATION)","basis":"A $331.50 BACKWARDATION, down from the series-wide $367.50; cash and three-month both fell, cash faster."},
 {"tenor":"Visible LME stock","price":"220,350 t","basis":f"DOWN 1,050 t on 24-November, a fourth straight draw, equal to the 17-November series low; October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PROMPT STILL TIGHT, FORWARD BREAKS LOWER. On the 24-November official cash $3,120.50 sits $331.50 ABOVE three-month $2,789.00, a BACKWARDATION down from the series-wide $367.50 (23-November). Cash and three-month both fell (same direction), cash faster, so the spread narrowed; AL Circle reports the spread traded at $405/t intraday, a 38-year high, with Oddo BHF calling for LME intervention. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00, $353.00, $367.50 and now $331.50. "
 f"READ: a twenty-ninth straight backwardation with visible stock at the series low (220,350 t) and warrant holdings concentrated (one entity 50-79% per AL Circle) - nearby metal is scarce while the forward prices a looser 2027 (Trading Economics cites an 830 kt 2027 surplus; Emkay Global, via AL Circle, a ~400 kt deficit). The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
# CHART AXES: three-month 2,789 is only $89 above the 2,700 floor -> re-bracket BEFORE it gets close
assert d['chart_price_axis']==[2700,3450] and d['chart_stock_axis']==[190000,255000]
d['chart_price_axis']=[2600,3450]

ls=d['lme_series']; assert ls[-1][0]=='23-Nov' and len(ls)==15
d['lme_series']=ls[1:]+[["24-Nov",cash,m3,stk]]
assert [tuple(r[1:]) for r in d['lme_series'][-6:]]==[(3060.5,2940.0,220350),(3095.0,2865.0,226150),(3105.0,2845.0,224425),(3184.5,2831.5,223525),(3201.5,2834.0,221400),(cash,m3,stk)]
CU=(12035.0,12055.0,337825); NI=(15060.0,15295.0,275604); ZN=(3665.0,3508.0,143425); PB=(1786.0,1828.0,256950)
CU0=(12165.0,12170.0,330975); NI0=(15215.0,15380.0,274098); ZN0=(3630.5,3488.0,144650); PB0=(1788.0,1832.0,259675)
assert CU0[2]+6850==CU[2] and NI0[2]+1506==NI[2] and ZN0[2]-1225==ZN[2] and PB0[2]-2725==PB[2]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU0[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI0[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN0[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB0[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU0[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI0[1],1)
ms=d['metals_series']; R=ms['rows']; assert ms['asof']=='2026-11-23'
# November MTD (02..23 Nov = 16 sessions) = 02-Nov point (from the 23-Nov engine state, asserted vs per-metal tables 21-Nov) + current 03..23 window
old=json.loads(subprocess.check_output(['git','show','d5d523d:market_data.json']))
z02=old['metals_series']['rows']['ZN'][0]; p02=old['metals_series']['rows']['PB'][0]; assert (z02,p02)==(3935.0,1869.5)
zs=z02+sum(R['ZN']); psum=p02+sum(R['PB'])
mh['zn'][-1]=round(mh['zn'][-1]*((zs+ZN[0])/17)/(zs/16),1); mh['pb'][-1]=round(mh['pb'][-1]*((psum+PB[0])/17)/(psum/16),1)
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])):
    assert len(R[k])==15; R[k]=R[k][1:]+[v]
ms['asof']='2026-11-24'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending TUESDAY 24-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 03-November dropped, 24-November appended, so the window is 04-November to 24-November. Earlier points were asserted against the Westmetall per-metal tables on 21-November; the 23- and 24-November points are the official cash from the English and German overviews (which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (24-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return "unchanged" if a==b else f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,f" COPPER 24-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU0[0])} from 23-November; three-month ${CU[1]:,.2f}, {chg(CU[1],CU0[1])} - a new low for this window. STRUCTURE: a $20.00 CONTANGO (23-November $5.00). Stock ROSE 6,850 t to 337,825 t."),
 ("Nickel",NI,f" NICKEL 24-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI0[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI0[1])}. CONTANGO widened to $235.00 (23-November $165.00), still the widest carry on the board. Stock rose 1,506 t to 275,604 t."),
 ("Zinc",ZN,f" ZINC 24-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN0[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN0[1])}. BACKWARDATION widened to $157.00 (23-November $142.50). Stock fell 1,225 t to 143,425 t. Zinc remains the strongest metal on this board year to date and the only one whose three-month rose."),
 ("Lead",PB,f" LEAD 24-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB0[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB0[1])}. CONTANGO $42.00 (23-November $44.00). Stock fell 2,725 t to 256,950 t."),
]
oldm={m['name']:m for m in d['metals_detail']}
CROSS=(f" CROSS-METAL 24-NOVEMBER: aluminium three-month fell the most on the board (-1.59%); copper fell {abs(CU[1]/CU0[1]-1)*100:.2f}%, nickel {abs(NI[1]/NI0[1]-1)*100:.2f}% and lead {abs(PB[1]/PB0[1]-1)*100:.2f}%, while zinc rose {abs(ZN[1]/ZN0[1]-1)*100:.2f}%. Copper and nickel stocks rose; aluminium, zinc and lead stocks fell. The dollar index was about 103.8 with a 25bp December Fed hike about 97% priced (Trading Economics). The LME euro fixing was 1.0960.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":oldm[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${oldm[n]['avg']:,.2f}; cash sits ${abs(c[0]-oldm[n]['avg']):,.2f} "+("above" if c[0]>oldm[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='23-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["24-Nov",CU[0]]]; assert i['hist'][0][0]=='04-Nov'
        assert [v for _,v in i['hist']]==R['CU']
        i['val']="~12,055.00 (3M); 12,035.00 (cash) $/t"; i['ratio']="~12,035.00 $/t cash vs LME 3M 12,055.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the TUESDAY 24-NOVEMBER-2026 session at $12,035.00 (23-November $12,165.00). 03-November dropped and 24-November appended, so the series is the last fifteen published official cash sessions, 04-November to 24-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English/German overviews and per-metal table. "
                  "Copper structure for context: a $20.00 contango on 24-November; stock 337,825 t (+6,850 t).")
d['inputs_summary']=("UPDATE 25-NOVEMBER: Copper rolled one session to the Tuesday 24-November LME official cash of $12,035.00 (window 04-November to 24-November). No new carbon, fluoride, silicon or magnesium mark was located this run, so those series are unchanged (gaps stay gaps); AL Circle (24-November) reports renewed alumina price increases weighing on a refractories maker's margins but gives no price. Energy: Brent about $90.3 on 25-November (Trading Economics); the IEA reports Gulf crude exports back at 74% of pre-war levels. "+d['inputs_summary'])

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
NC1="COMPILED TUESDAY 24-NOVEMBER-2026 BEFORE THE RING (LME BOARD ROLLED TO THE MONDAY 23-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION)."
NC2="COMPILED WEDNESDAY 25-NOVEMBER-2026 BEFORE THE RING (LME BOARD ROLLED TO THE TUESDAY 24-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION)."
REPL=[
 ("0.50 times the 23-November official cash of $3,201.50, or $1,600.75, UP $8.50 against the 20-November figure used previously",f"0.50 times the 24-November official cash of $3,120.50, or ${tl:,.2f}, DOWN ${1600.75-tl:,.2f} against the 23-November figure used previously"),
 ("residual market leg of $802.25, so 66.6%",f"residual market leg of ${resid:,.2f}, so {share:.1f}%"),
 ("0.50 times the 23-November official cash of $3,201.50, or $1,600.75, leaving a $802.25 residual market leg out of the $2,403/t US duty-paid premium (66.6%",f"0.50 times the 24-November official cash of $3,120.50, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}%"),
 ("$1,600.75 on 23-November cash, 66.6%",f"${tl:,.2f} on 24-November cash, {share:.1f}%"),
 ("THE RATIO: LME Alumina at $398.24/t against the 23-November aluminium three-month of $2,834.00 is 14.05%",f"THE RATIO: LME Alumina at $398.24/t against the 24-November aluminium three-month of $2,789.00 is {398.24/m3*100:.2f}%"),
 ("REVIEWED 24-NOVEMBER: no newer public disclosure","REVIEWED 25-NOVEMBER: no newer public disclosure"),
 ("REVIEWED 24-NOVEMBER. NO NEW DATED","REVIEWED 25-NOVEMBER. NO NEW DATED"),
 (NC1,NC2)]
cnt={}
def f(s):
    for a,b in REPL:
        if a in s: cnt[a[:25]]=cnt.get(a[:25],0)+s.count(a); s=s.replace(a,b)
    return s
for k in list(d.keys()):
    if k in ('report_date','ew','sources','kpi_cards','benchmark','metals_detail'): continue
    d[k]=walk(d[k],f)
print(cnt)
blob=json.dumps(d,ensure_ascii=False)
assert "$1,600.75" not in blob and "TUESDAY 24-NOVEMBER-2026 BEFORE THE RING" not in blob, [blob.count("$1,600.75")]

d['lme_commentary']=("THE FORWARD BREAKS LOWER WHILE THE PROMPT STAYS SCARCE. On Tuesday 24-November cash fell $81.00 to $3,120.50 and three-month $45.00 to $2,789.00 - below the 2,830-2,850 Elliott zone and the ~2,803 re-label level, the lowest three-month official in this dashboard's 2026 record and the largest fall on the base-metals board. The backwardation narrowed to $331.50 from the series-wide $367.50 (AL Circle reports it traded at $405/t intraday, a 38-year high). Visible stock fell 1,050 t to 220,350 t, a fourth straight draw, equal to the series low. "
 "Trading Economics ties the slide to better expected supply - Chinese output on track for a record above 46 Mt and a recovering Middle East - and cites an 830 kt 2027 surplus; Emkay Global (via AL Circle) sees a ~400 kt deficit in 2027 and 2028 - the forecasts disagree. Macro stays a headwind (December hike ~97% priced) while Brent eased to about $90.3. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} below its October mean.")
d['net_read']=("NET: BEARISH ON THE FORWARD, TIGHT ON THE PROMPT. Against: three-month at $2,789.00 broke below the 2,830-2,850 zone and the ~2,803 re-label level, $105.00 under the 2,894 weekly 61.8%; a hawkish Fed (December hike ~97% priced); forecasts of a 2027 surplus as Chinese output tops 46 Mt and Gulf metal returns; copper and nickel stocks rising. "
 "Supportive: a $331.50 backwardation (twenty-ninth straight; traded $405/t intraday per AL Circle), stock at the 220,350 t series low with concentrated warrant holdings, Hormuz still closed with further tanker attacks reported, and Emkay Global's view of a ~400 kt deficit through 2028.")
d['bottom_line']=("BOTTOM LINE: Tuesday's official broke the forward out of the completion zone - three-month $2,789.00 (-$45.00), cash $3,120.50 (-$81.00), backwardation $331.50 - while visible stock drew for a fourth session to the 220,350 t series low. "
 "The pre-registered ~2,803 trigger fired: weights move to 10% bull / 30% base / 60% bear and the Elliott count is re-labelled to an extended wave (v). A settled close back above 2,994.50 would signal a failed break; above 3,097.50 negates the count; daily invalidation 3,289. Next print Wednesday 25-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, THE CURVE STEEPENS AGAIN - PROMPT TIGHT, FORWARD WEAK:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, THE CURVE STEEPENS AGAIN - PROMPT TIGHT, FORWARD WEAK: the forward broke lower on 24-November - three-month $2,789.00, below the 2,830-2,850 zone - while cash fell to $3,120.50, leaving a $331.50 backwardation (series high $367.50 on 23-November; $405/t traded intraday per AL Circle); nearby metal still commands a very large premium over forward metal, so there is no carry reward for holding stock - and visible LME stock drew for a fourth session to the 220,350 t series low. "+c2[a1:]
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find("; the dollar index near",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 24-November official took three-month to $2,789.00, below the ~2,803 re-label level, while cash fell to $3,120.50; a 25bp December Fed hike is about 97% priced and the US PCE report is due (Trading Economics 25-November); first Q1-2027 Japanese premium offers, which typically emerge from late November (none located yet)"+c2[b1:]
d['commercial']=c2

NEWP={'Bull':'10%','Base':'30%','Bear':'60%'}
for s in d['outlook']['scenarios']:
    assert s['prob']=={'Bull':'10%','Base':'35%','Bear':'55%'}[s['case']]
    s['prob']=NEWP[s['case']]
    s['drivers']=("SHIFTED 25-NOVEMBER TO 10/30/60: the 24-November official settled three-month at $2,789.00, BELOW about 2,803 - the pre-registered level that adds bear weight - so five points move from base to bear. The $331.50 backwardation and series-low stock are why the move is held to the minimum five points. REVERSAL: a settled close back above 2,994.50 returns the five points to base. ")+s['drivers']
d['outlook']['scenario_paths']['bull'][0]=m3; d['outlook']['scenario_paths']['base'][0]=m3; d['outlook']['scenario_paths']['bear'][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 25-NOVEMBER: the 24-November official printed a $331.50 backwardation (down from the $367.50 series high) - an eighteenth session above $15.00; AL Circle reports $405/t traded intraday. Contango risk remains remote near term. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 25-NOVEMBER: a fourth straight draw - LME stock fell 1,050 t to 220,350 t on 24-November, EQUAL to the 17-November series low; AL Circle reports one entity held 50-79% of warrants and Russian-origin metal 99.98% of available stock. Trend held at FLAT; a settled break below 220,350 t would move it to UP."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 25-NOVEMBER: Brent about $90.3 on 25-November (Trading Economics), down about 22% over the month; the IEA reports Gulf crude exports rebounded to 74% of pre-war levels. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 25-NOVEMBER: Straits Daily Brief - still CLOSED; IMF PortWatch 1 transit on 22-November (pre-crisis 85/day). Further attacks reported: a projectile strike on a tanker attributed to UKMTO (secondary report), Lloyd's List reporting three tankers attacked exiting the strait on 24-November, and gCaptain counting ten tanker strikes; Iranian claims of four tankers hitting mines remain UNCONFIRMED by any maritime authority. No reopening agreement. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 25-NOVEMBER: markets assign about 97% probability to a 25bp December hike and about 59% to another in January; dollar index about 103.81; PCE report due (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
assert hit==5,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Tue 24-Nov':
        hc+=1; cat['date']='Daily, from Wed 25-Nov'
        cat['event']=("TUESDAY 24-NOVEMBER OFFICIAL: three-month $2,789.00 (-$45.00), BELOW the ~2,803 re-label level (trigger fired: weights to 10/30/60, count re-labelled to an extended wave (v)); cash $3,120.50; backwardation $331.50; stock 220,350 t (equal to series low). NEXT: Wednesday 25-November official (13:20 London) - 2,750 and 2,700 are the extended-(v) objectives; a settled close back above 2,994.50 signals a failed break; above 3,097.50 negates the count; invalidation 3,289. Friday 27-November weekly close against the 2,894 weekly 61.8%. US PCE report; the December Fed meeting (25bp ~97% priced); first Q1-2027 Japanese premium offers (none located yet; S&P Global reported participant expectations of $190-200/t).")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"WEDNESDAY 25-NOVEMBER ON THE TUESDAY 24-NOVEMBER OFFICIAL: cash fell $81.00 to $3,120.50 and three-month $45.00 to $2,789.00 - out of the 2,830-2,850 Elliott zone and below the ~2,803 re-label level, the lowest three-month official in this dashboard's 2026 record. The backwardation narrowed to $331.50 from the series-high $367.50, though AL Circle reports $405/t traded intraday (a 38-year high) and calls from Oddo BHF for LME action over concentrated warrant holdings. Visible stock drew for a fourth session to the 220,350 t series low. The pre-registered trigger fired: weights move to 10/30/60 and the count is re-labelled to an extended wave (v).")

# ---- ELLIOTT WAVE: pre-registered re-label (extended wave (v)) ----
st=d['ew']['short_term']; nx=st['now_x']
st['ymin']=2600; st['yticks']=[2600,2800,3000,3200,3400,3600]
st['proj']={'bull':[[nx,m3],[0.99997,2900],[1.0,3000]],'base':[[nx,m3],[0.99997,2740],[1.0,2900]],'bear':[[nx,m3],[0.99997,2700],[1.0,2633]]}
assert st['fwd_pivots'][0]['t']==0.99996
st['fwd_pivots'][0]={'t':0.99996,'p':2750.0,'w':"RE-LABELLED 25-NOVEMBER ON A PRE-REGISTERED BREAK: three-month settled 2,789.00 on 24-November, below about 2,803, so wave (v) from 3,097.50 ($308.50) is now longer than wave (iii) ($294.50). No cardinal rule is broken - wave (iii) still exceeds wave (i) ($191), wave (ii) at 3,289 holds below the 3,374 origin, wave (iv) at 3,097.50 stays clear of the 3,183 wave (i) low - but wave (v) is now the EXTENDED wave. Count: (i) 3,374-3,183, (ii) 3,289, (iii) to 2,994.50, (iv) 3,097.50, extended (v) under way; 1.618 x (i) near 2,788 is met; objectives 2,750-2,700 (2,633 = the weekly 78.6%). The wave (v) low is NOT confirmed until a reversal settles; a settled close above 3,097.50 negates this count."}
lt=d['ew']['long_term']
lt['proj']={'bull':[[lt['now_x'],m3],[0.78,3200],[0.9,3400],[1.0,3550]],'base':[[lt['now_x'],m3],[0.78,2750],[0.9,2950],[1.0,3080]],'bear':[[lt['now_x'],m3],[0.8,2633],[1.0,2550]]}
EWP=("REVIEWED 25-NOVEMBER ON THE 24-NOVEMBER OFFICIAL - RE-LABEL ON A PRE-REGISTERED BREAK: three-month settled 2,789.00 (-45.00), below the 2,830-2,850 completion zone and below about 2,803, so wave (v) from 3,097.50 ($308.50) is now longer than wave (iii) ($294.50). All three cardinal rules still hold - wave (ii) at 3,289 stays below the 3,374 origin, wave (iii) is not the shortest because it exceeds wave (i) ($191), and wave (iv) at 3,097.50 stays clear of the 3,183 wave (i) low - so the count is kept but wave (v) is re-labelled as the EXTENDED wave of the C decline from 3,374. The 2,789 settlement is not added as a pivot because no reversal has confirmed a low. "
 "BASE CASE (about 55%): the extended wave (v) completes in 2,700-2,790 (1.618 x wave (i) near 2,788 is met; 2,750 and 2,700 are the next objectives), ending the C wave, followed by a corrective rebound toward 2,994.50-3,097.50 - the series-low stock and $331.50 backwardation argue for a sharp rebound once a low confirms. ALTERNATE (about 45%): the decline is a larger-degree leg toward 2,633 (the weekly 78.6% retracement) or lower. INVALIDATION of the count: a settled close above 3,097.50; of the bearish C-wave count, 3,289; a settled close back above 2,994.50 would signal a failed break. Confidence low. ")
EWL=("REVIEWED 25-NOVEMBER (MID-WEEK, DAILY BREAK LOWER): the Tuesday official at 2,789.00 settled $105.00 below the 2,894 weekly 61.8% retracement and below the 2,800-2,850 base-case zone. The base case (about 65%) is held but its completion zone widens to 2,700-2,850: a correction of the 2,300-3,855 advance completing before a rebound. The alternate toward the 78.6% retracement near 2,633 stays at about 35% and is raised to about 45% on a WEEKLY close below 2,750 (Friday 27-November). A weekly close back above 2,994.50 would favour a completed correction; loses preference only on a weekly close above 3,110. Confidence moderate. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 24-NOVEMBER'),k
    d['ew'][k]['writeup']=pfx+w
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="90.3",day="about $90.28 on 25-November (-1.22%, Trading Economics); Straits Daily Brief $91.09 on 25-November",
 note="REFRESHED WEDNESDAY 25-NOVEMBER-2026 (Trading Economics): about 22% lower over the month; attacks on vessels near Hormuz and new US sanctions keep supply risk in focus, while the IEA reports Gulf crude exports rebounded to 74% of pre-war levels and expects a market surplus this quarter. Levels approximate. SOURCE: "+S_BR)
M['US dollar index (DXY)'].update(value="103.81",day="about 103.81 on 25-November (-0.04%, Trading Economics), after touching 104.3 on 23-November",
 note="REFRESHED WEDNESDAY 25-NOVEMBER-2026 (Trading Economics): markets assign about 97% probability to a 25bp December hike and about 59% to another in January; the PCE report is awaited. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.09600',day="LME fixing on 24-November, up from 1.09460 on 23-November",note="REFRESHED WEDNESDAY 25-NOVEMBER-2026 to the 24-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE TUESDAY 24-NOVEMBER-2026 LME OFFICIAL, the latest published session. THIS WEDNESDAY 25-NOVEMBER RUN IS COMPILED AT ABOUT 02:40 LONDON, BEFORE TODAY'S RING; Wednesday's official prints at 13:20 London, so Tuesday's official is the correct latest figure. The board rolled ONE session this run. Nothing was estimated or taken intraday. The Trading Economics aluminium reference (about $2,775.20, -3.19% for 24-November) is a CFD reference cited in text only; AL Circle's $405/t backwardation is a traded intraday figure, cited in text only.")
C[1]=("SOURCE CHECK THIS RUN (25-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 24-November session (aluminium cash 3,120.50, three-month 2,789.00, stock 220,350; copper 12,035.00/12,055.00; nickel 15,060.00/15,295.00; zinc 3,665.00/3,508.00; lead 1,786.00/1,828.00; EUR/USD MTLE 1.09600); the aluminium per-metal daily table shows 24-November as its newest row.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 17- to 23-November rows match the stored series; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 04- to 20-November points were asserted against those tables on 21-November and the 23- and 24-November points come from agreeing overviews; each metal's 24-November stock change reconciles exactly with the stored 23-November stock.")
C[3]=("STOCK CHANGES 24-November: aluminium -1,050 to 220,350 (fourth straight draw, equal to the series low); copper +6,850 to 337,825; nickel +1,506 to 275,604; zinc -1,225 to 143,425; lead -2,725 to 256,950; tin +55 to 3,725.")
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (24-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (seventeen sessions, 02-24 November) as their latest point. "
 "The price chart axis was RE-BRACKETED this run to floor 2,600 / ceiling 3,450 (previously 2,700) because three-month 2,789.00 had come within $89 of the old floor; it brackets cash 3,120.50 and three-month 2,789.00. The stock chart axis floor of 190,000 t leaves 30,350 t headroom below visible stock of 220,350 t; both are re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,120.50 against three-month $2,789.00 is therefore a $331.50 BACKWARDATION, down from $367.50 on 23-November. On 24-November cash and three-month moved in the SAME direction (both down), cash faster. Press figures for the spread differ by measure and time (AL Circle: $405/t traded intraday); the dashboard uses the settled officials only."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $90.3) and the dollar index (about 103.81) are Trading Economics readings for 25-November; TTF (about EUR 88.45/MWh) and the US ten-year row are CARRIED from earlier sessions (not re-fetched). Trading Economics prices are contract-for-difference references, not official benchmarks, so levels are approximate. The Straits Daily Brief (25-November) shows Brent $91.09 and flags degraded feeds (oil data 7 hours stale, transit data 12 hours); its incident items include secondary or single-outlet reports and Iranian claims - none of the mine-strike claims is maritime-authority-confirmed."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 25-NOVEMBER (WEDNESDAY, PRE-RING): no authorised fetch was blocked. Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/dollar, AL Circle news (and three AL Circle articles) and the Straits Daily Brief (25-November) were fetched. A WebSearch for Q1-2027 Japanese premium offers located none; the latest public reference remains S&P Global's report of participant expectations of $190-200/t for Q1 talks - an expectation, not an offer. No earnings_history company was back-filled this run."); hit+=1
assert hit==2,hit

d['so_what']={"line":"LME aluminium's forward broke lower on Tuesday - three-month fell $45 to $2,789, its lowest official this year on this record and below the $2,800-2,850 support zone - even as the prompt stays extremely tight, with a $331.50 backwardation and LME stocks back at the 220,350 t series low.",
 "points":[
 "WHAT MOVED: on the 24-November official cash fell $81.00 to $3,120.50 and three-month $45.00 to $2,789.00 - the largest fall on the base-metals board. The backwardation (cash above three-month) narrowed to $331.50 from a series-high $367.50, and visible LME stock fell 1,050 t to 220,350 t, a fourth straight draw.",
 "WHY IT MATTERS: the market is pricing two different stories - scarce nearby metal (AL Circle reports the spread traded at $405/t, a 38-year high, with one holder controlling 50-79% of warrants) against a looser 2027 as Chinese output tops 46 Mt and Gulf supply recovers. The break below about $2,803 was a pre-stated bearish trigger, so scenario weights shift to 10/30/60.",
 "48H DEVELOPMENTS: further tanker attacks were reported around a still-closed Strait of Hormuz (one transit on 22-November), though Brent eased to about $90 as the IEA reported Gulf crude exports back at 74% of pre-war levels. Pakistan's HUBCO commissioned a feasibility study for a 300 ktpa smelter; Cameroon's Minim-Martap bauxite project missed its Q4 export target.",
 "WHAT TO WATCH: Wednesday's official against $2,750-2,700 (a settle back above $2,994.50 would mark a failed break), whether stocks break below 220,350 t, Friday's weekly close, the US PCE report ahead of a near-certain December Fed hike, and first Q1-2027 Japanese premium offers (none reported; earlier talk $190-200/t)."]}

d['feed']=([
 {"when":"Tue 24-Nov","impact":"Bearish","text":"24-NOVEMBER OFFICIAL: three-month $2,789.00 (-$45.00), below the ~2,803 trigger; cash $3,120.50 (-$81.00); backwardation $331.50; stock -1,050 t to 220,350 t (equal to series low)."},
 {"when":"Tue 24-Nov","impact":"Bullish","text":"STRUCTURE: AL Circle - backwardation traded at $405/t, a 38-year high; Oddo BHF urges LME action; one entity held 50-79% of warrants."},
 {"when":"Wed 25-Nov","impact":"Bullish","text":"HORMUZ: still closed (1 transit on 22-Nov); further tanker attacks reported (Lloyd's List, gCaptain, UKMTO via secondary report); Iranian mine claims unconfirmed (Straits brief 25-Nov)."},
 {"when":"Wed 25-Nov","impact":"Bearish (cost)","text":"ENERGY: Brent ~$90.3 (-1.2%, Trading Economics); IEA says Gulf crude exports back at 74% of pre-war levels."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM THREE-MONTH BREAKS BELOW $2,800. The Tuesday 24-November official put three-month at $2,789.00 (-$45.00, -1.59%) and cash at $3,120.50 (-$81.00) - the largest fall on the base-metals board (copper -0.94%, nickel -0.55%, lead -0.22%, zinc +0.57%) and the lowest three-month official in this dashboard's 2026 record. The backwardation narrowed to $331.50 and visible stock fell 1,050 t to 220,350 t, equal to the series low. Trading Economics describes UK aluminium futures at their lowest level this year."},
 {"theme":"Market structure","horizon":"Immediate","impact":"Bullish","url":S_BW,
  "headline":"BACKWARDATION AT A 38-YEAR HIGH; CALLS FOR LME ACTION (AL Circle, 24-November): the cash-to-three-month spread traded at $405/t, levels unseen since 1988 per Oddo BHF, which urged the LME to intervene and limit extreme backwardation. One entity held 50-79% of LME aluminium warrants; Russian-origin metal was 99.98% of available stock at end-October. The LME said existing safeguards include front-month lending rules and position reporting."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ: MORE TANKER ATTACKS REPORTED (Straits Daily Brief, 25-November): the Strait is listed as closed, with 1 transit on 22-November (IMF PortWatch) vs 85/day pre-crisis. Lloyd's List reported three tankers attacked exiting the strait on 24-November; a projectile strike on a tanker is attributed to UKMTO via a secondary report; gCaptain counts ten tanker strikes. Iranian claims that four tankers hit mines are unconfirmed by any maritime authority."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bearish (cost)","url":S_BR,
  "headline":"BRENT EASES TO ABOUT $90 (Trading Economics, 25-November): Brent was about $90.28 (-1.22%), roughly 22% lower over the month, as the IEA reported Persian Gulf crude exports rebounded to 74% of pre-war levels and a market surplus this quarter - lower oil eases smelter energy and freight cost pressure."},
 {"theme":"Supply","horizon":"12+ months","impact":"Bearish","url":S_HU,
  "headline":"PAKISTAN'S HUBCO STUDIES A 300 KTPA SMELTER (AL Circle, 24-November): Hub Power appointed a Chinese design institute for a bankable feasibility study on a smelter using Pakistan's surplus power; no investment figure or timeline is disclosed - another signal of planned capacity outside China."},
 {"theme":"Bauxite","horizon":"6-12 months","impact":"Mixed","url":S_CM,
  "headline":"CAMEROON BAUXITE PROJECT MISSES Q4 EXPORT TARGET (AL Circle, 24-November): Canyon's Minim-Martap project missed its Q4-2026 export target amid funding uncertainty and is exploring new funding."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"FED DECEMBER HIKE ~97% PRICED; PCE AWAITED (Trading Economics, 25-November): the dollar index eased to about 103.81 after touching 104.3; markets assign about 97% to a 25bp December hike and about 59% to another in January."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])
for p in d['producer_status']: p['asof']=RD

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 24-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 24-Nov)",W])
for x in ([L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_TE,S_TE],[L_BW,S_BW],[L_HU,S_HU],[L_CM,S_CM]): d['sources'].append(x)
for x in ([L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_TE,S_TE],[L_BW,S_BW],[L_HU,S_HU]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-23',3201.5,2834.0,221400]
ph['rows'][-1]=['2026-11-24',cash,m3,stk]; ph['updated']=RD   # same week (w/c 23-Nov): replace
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],d['metals_board'])
