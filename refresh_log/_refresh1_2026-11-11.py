# Daily data refresh - 2026-11-11 (WEDNESDAY, ~02:40 UTC). Board ROLLED ONE SESSION to the TUESDAY 10-Nov LME official.
# Westmetall cache-busted EN + DE overviews agree on 10-Nov (Al cash 3,137 / 3M 3,027 / stock 226,850; MTLE 1.12150);
# aluminium per-metal table newest row 10-Nov and its 02-09 Nov rows match the stored series.
# 3M 3,027.00: not above 3,077 and not below 3,024.50 -> weights unchanged 15/45/40. Below 3,042 -> EW daily alternate favoured (no re-label).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-11'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-11"; L_ST="Straits Daily Brief - Strait of Hormuz, 11-Nov-2026 (ticker AI-assisted)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum 3,006.50 (-2.18%) on 10-Nov-2026 (CFD reference); EGA expects full Al Taweelah recovery by Q1-2027"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$92.3 near ten-week lows; Bahri sending tankers through Hormuz with US coordination (11-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~102.25; October CPI +0.4% m/m vs 0.3% expected; next-meeting hike odds ~88% (11-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 85.2/MWh, rebounding from a one-month low of ~82.5 on 09-Nov; EU storage below 73% (11-Nov-2026)"
S_WR="https://www.alcircle.com/news/alcoa-takeover-puts-south32-s-worsley-workforce-on-a-collision-course-over-pay-121918"; L_WR="AL Circle - Worsley Alumina workers begin 48-hour stoppage over pay ahead of Alcoa takeover; South32 expects no production impact (10-Nov-2026)"
S_SM="https://www.alcircle.com/news/inventory-drawdown-supports-aluminium-prices-weakening-demand-at-end-of-peak-season-limits-rebound-space-121902"; L_SM="AL Circle (SMM republication) - Inventory drawdown supports aluminium prices; SHFE RMB 23,170/t, A00 RMB 23,540/t (10-Nov-2026)"
S_CF="https://www.alcircle.com/news/from-scrap-to-billets-clearflow-plans-major-secondary-aluminum-investment-in-kentucky-121916"; L_CF="AL Circle - ClearFlow plans secondary aluminium billet investment in Kentucky (10-Nov-2026)"
S_JP="https://www.spglobal.com/energy/en/news-research/latest-news/metals/101326-japanese-q4-aluminum-premium-falls-35-to-255mt-cif-japan"; L_JP="S&P Global - Japanese Q4 premium $255/mt; participants expected Q1-2027 talks around $190-200/mt (Oct-2026)"

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3147.0 and B['LME 3-month']['cur']==3059.5
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3147.0,3059.5,226975
cash,m3,stk=3137.0,3027.0,226850
spr=cash-m3; psp=pc-pm; assert spr==110.0 and psp==87.5 and ps-125==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED WEDNESDAY 11-NOVEMBER-2026 ABOUT 02:40 LONDON, BEFORE WEDNESDAY'S RING, SO THE BOARD IS THE TUESDAY 10-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION (WEDNESDAY'S PRINTS 13:20 LONDON). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 10-November official for all metals with stocks and FX (EUR/USD MTLE 1.12150; 09-November 1.11920); (2) the aluminium per-metal daily table shows 10-November as its newest row and its 02 to 09-November rows match the stored series exactly. "
 "The whole board sits on ONE UNIFORM SESSION (10-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" TUESDAY 10-NOVEMBER (the board): CASH SETTLED $3,137.00, DOWN $10.00 OR 0.32% FROM $3,147.00. THREE-MONTH SETTLED $3,027.00, DOWN $32.50 OR 1.06% FROM $3,059.50 - the lowest three-month official since 26-October (also $3,027.00), $15.00 BELOW the 3,042.00 low of 03-November, $50.00 below 3,077 and only $2.50 above the 3,024.50 bear-trigger level; $16.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION WIDENED TO $110.00 FROM $87.50 WHILE FLAT PRICE FELL - SPREAD AND PRICE MOVED IN OPPOSITE DIRECTIONS: three-month fell more than three times as much as cash. A nineteenth straight backwardation, the eighth above $15.00 and the widest in the stored series. "
 "VISIBLE LME STOCK FELL 125 t TO 226,850 t, another new series low and a fifteenth straight draw. The Trading Economics aluminium reference showed $3,006.50 (-2.18%) for 10-November - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,137.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,027.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $50.00 BELOW THE 3,077 WEEKLY 50% RETRACEMENT and $34.50 below the 3,061.5 July low, $121.50 beneath the 3,148.5 wave (iv) high and $262.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for an eighteenth session, $32.50 below."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+110.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,137.00 against three-month $3,027.00 is a $110.00 BACKWARDATION, WIDER than 09-November's $87.50 even though cash fell $10.00 and three-month $32.50 - SPREAD AND PRICE MOVED IN OPPOSITE DIRECTIONS (structure tighter, price lower). It stays above the published $15.00 reversal condition for an eighth session, a nineteenth straight backwardation and the widest print in the stored series; a contango beyond $24.50 would reverse the structural signal. The October mean spread was $"+f"{oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"226,850","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 125 t TO 226,850 t (09-November: -625 t to 226,975 t), another new series low and a fifteenth straight draw, though the smallest of the recent draws. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 09-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $3,027.00, DOWN $32.50 FROM THE 09-NOVEMBER $3,059.50 - $50.00 below 3,077, $15.00 below the 3,042.00 low of 03-November and only $2.50 above 3,024.50; $16.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 125 t TO 226,850 t, another new series low (09-November 226,975 t). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $110.00 BACKWARDATION, WIDER THAN 09-NOVEMBER'S $87.50 (06-November $67.00). CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On Tuesday cash fell $10.00 and three-month $32.50, so STRUCTURE TIGHTENED WHILE PRICE FELL (opposite directions). REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50 and $110.00."},
 {"name":"EUR/USD LME fixing","cur":1.1215,"prev":1.1192,"avg":1.1465,"note":VER+" THE LME EURO FIXING ROSE TO 1.12150 ON 10-NOVEMBER FROM 1.11920 ON 09-NOVEMBER. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (10-Nov official)","price":"3,137.0","basis":"THE TUESDAY 10-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,137.00, DOWN $10.00 OR 0.32% (09-November $3,147.00). Next official Wednesday 11-November 13:20 London."},
 {"tenor":"3-month (10-Nov official)","price":"3,027.0","basis":"THE 10-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $3,027.00, DOWN $32.50 - $50.00 below 3,077, $15.00 below 3,042.00, only $2.50 above 3,024.50 and $32.50 above the 2,994.50 October low."},
 {"tenor":"Cash-to-3M structure","price":"+110.0 (BACKWARDATION)","basis":"A $110.00 BACKWARDATION, wider than $87.50 with price LOWER (opposite directions) - above the $15.00 reversal condition for an eighth session."},
 {"tenor":"Visible LME stock","price":"226,850 t","basis":f"DOWN 125 t to a new series low on 10-November (fifteenth straight draw); October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PROMPT TIGHTNESS UP, OUTRIGHT PRICE DOWN. On the 10-November official cash $3,137.00 sits $110.00 ABOVE three-month $3,027.00, a BACKWARDATION, wider than $87.50 on 09-November even though both legs fell (cash -$10.00, three-month -$32.50) - SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS on Tuesday, after moving together on Monday. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50 and now $110.00. "
 f"READ: a nineteenth straight backwardation, the eighth above $15.00, with visible stock at another low (226,850 t) - nearby LME metal is tight, but the forward price is being pulled down by improving ex-Middle-East supply, cheaper energy and a hawkish Fed repricing. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2900,3450] and d['chart_stock_axis']==[200000,255000]

ls=d['lme_series']; assert ls[-1][0]=='09-Nov'
d['lme_series']=ls[1:]+[["10-Nov",cash,m3,stk]]
assert len(d['lme_series'])==15 and all(200000<r[3]<255000 and 2900<r[2]<3450 and 2900<r[1]<3450 for r in d['lme_series'])
CU=(13992.0,13830.0,316625); NI=(15875.0,16075.0,271662); ZN=(3768.0,3734.0,144975); PB=(1846.0,1882.0,300300)
CU6=(14030.0,13855.0,317400); NI6=(16190.0,16400.0,271662); ZN6=(3754.0,3724.0,146375); PB6=(1854.0,1889.0,300300)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU6[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI6[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN6[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB6[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU6[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI6[1],1)
zn6=[3935.0,3869.0,3875.0,3877.0,3759.0,3754.0]; pb6=[1869.5,1862.0,1858.0,1866.5,1857.0,1854.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zn6)+ZN[0])/7)/(sum(zn6)/6),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(pb6)+PB[0])/7)/(sum(pb6)/6),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU6[0]),('NI',NI[0],NI6[0]),('ZN',ZN[0],ZN6[0]),('PB',PB[0],PB6[0])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-11-10'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending TUESDAY 10-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 20-October dropped, 10-November appended, so the window is 21-October to 10-November. Every point is an official cash settlement from the Westmetall per-metal tables and English/German overviews (10-November read from both overviews, which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (10-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,CU6,f" COPPER 10-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU6[0])}; three-month ${CU[1]:,.2f}, {chg(CU[1],CU6[1])}. BACKWARDATION narrowed to $162.00 from $175.00. Stock fell 775 t to 316,625 t."),
 ("Nickel",NI,NI6,f" NICKEL 10-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI6[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI6[1])} - the weakest metal on Tuesday's board after Monday's lead. CONTANGO narrowed to $200.00 from $210.00, still the widest carry on the board. Stock unchanged at 271,662 t."),
 ("Zinc",ZN,ZN6,f" ZINC 10-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN6[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN6[1])} - the only metal to rise on Tuesday. BACKWARDATION widened to $34.00 from $30.00. Stock fell 1,400 t to 144,975 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,PB6,f" LEAD 10-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB6[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB6[1])}. CONTANGO $36.00 from $35.00. Stock unchanged at 300,300 t."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Tuesday 10-November official three-month nickel fell 1.98%, aluminium 1.06%, lead 0.37% and copper 0.18%; zinc rose 0.27%. Zinc and copper drew stock. Trading Economics reports US October CPI rose 0.4% m/m against 0.3% expected, lifting market-implied odds of a 25bp Fed hike at the next meeting to about 88%, with the dollar index near 102.25; Brent held near ten-week lows around $92. The LME euro fixing rose to 1.1215.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,c6,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='09-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["10-Nov",CU[0]]]; assert len(i['hist'])==15
        i['val']="~13,830.00 (3M); 13,992.00 (cash) $/t"; i['ratio']="~13,992.00 $/t cash vs LME 3M 13,830.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the TUESDAY 10-NOVEMBER-2026 session at $13,992.00 (09-November $14,030.00). THE WINDOW ROLLED THIS RUN: 20-October dropped and 10-November appended, so the series is the last fifteen published official cash sessions, 21-October to 10-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall copper table and English/German overviews. "
                  "Copper structure for context: backwardation $162.00 on 10-November; stock 316,625 t (-775 t).")
s=d['inputs_summary']; assert s.startswith("UPDATE 10-NOVEMBER")
d['inputs_summary']=("UPDATE 11-NOVEMBER: Copper rolled one session to the Tuesday 10-November LME official cash of $13,992.00, its fifteen-session window now 21-October to 10-November. No new monthly carbon settlement (due mid-November) or dated SMM fluoride, silicon or magnesium mark was located, so no other hist mark was appended. Energy steadied: Brent near $92.3, still near ten-week lows; European gas rebounded to about EUR 85.2/MWh from a one-month low near 82.5 on 09-November, with EU storage below 73% against an 89% five-year norm (Trading Economics, 11-November). Upstream: workers at the 4.4 Mt/yr Worsley alumina refinery began a 48-hour stoppage on 10-November; South32 expects no production impact (AL Circle). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OT="the tariff leg of the US duty-paid premium is 0.50 times the 09-November official cash of $3,147.00, or $1,573.50, UP $15.00 against the 06-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of $829.50, so 65.5%"
NT=f"the tariff leg of the US duty-paid premium is 0.50 times the 10-November official cash of $3,137.00, or ${tl:,.2f}, DOWN $5.00 against the 09-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OC1="COMPILED TUESDAY 10-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE MONDAY 09-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; TUESDAY'S OFFICIAL PRINTS 13:20 LONDON)."
NC1="COMPILED WEDNESDAY 11-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE TUESDAY 10-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; WEDNESDAY'S OFFICIAL PRINTS 13:20 LONDON)."
for p in d['premiums']:
    assert OT in p['src'] and OC1 in p['src'],p['name']
    p['src']=p['src'].replace(OT,NT).replace(OC1,NC1)
ra=398.24/m3*100
OR="THE RATIO: LME Alumina at $398.24/t against the 09-November aluminium three-month of $3,059.50 is 13.02%"
for a in d['alumina']:
    assert OR in a['src'],a['name']
    a['src']=a['src'].replace(OR,f"THE RATIO: LME Alumina at $398.24/t against the 10-November aluminium three-month of $3,027.00 is {ra:.2f}%").replace(OC1,NC1)
OC0="COMPILED TUESDAY 10-NOVEMBER-2026 ABOUT 02:35 LONDON; THE BOARD IS THE MONDAY 09-NOVEMBER-2026 LME OFFICIAL."
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace(OC1,NC1).replace(OC0,"COMPILED WEDNESDAY 11-NOVEMBER-2026 ABOUT 02:40 LONDON; THE BOARD IS THE TUESDAY 10-NOVEMBER-2026 LME OFFICIAL.")
        o=o.replace("REVIEWED 10-NOVEMBER: no newer public disclosure","REVIEWED 11-NOVEMBER: no newer public disclosure").replace("REVIEWED 10-NOVEMBER. NO NEW DATED","REVIEWED 11-NOVEMBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status','inputs','logistics','raw_materials'):
    if k in d: d[k]=walk(d[k])

d['lme_commentary']=("FORWARD PRICE BREAKS LOWER, PROMPT STAYS TIGHT. The Tuesday 10-November official cut three-month $32.50 to $3,027.00 - below the 3,042.00 low of 03-November and the lowest since 26-October - while cash eased only $10.00 to $3,137.00, so the backwardation widened to $110.00, the widest in the stored series and a nineteenth straight backwardation. Spread and price moved in OPPOSITE directions on Tuesday. Visible stock fell another 125 t to a new low of 226,850 t. "
 "Three-month closed only $2.50 above the 3,024.50 bear trigger, so no pre-registered rule fired and weights stay 15/45/40, but the daily Elliott alternate (rebound from 2,994.50 complete) is now favoured. "
 "Pressure came from supply and macro: Trading Economics notes improving supply outside the Middle East (near-record Chinese output and exports, gradual Gulf restarts, EGA targeting full Al Taweelah recovery by Q1-2027) and a hotter-than-expected US October CPI (+0.4% m/m) that lifted Fed-hike odds to about 88%. Nickel led the board lower (-1.98%); zinc alone rose. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" its October mean.")
d['net_read']=("NET: NEUTRAL WITH A BEARISH TILT - FORWARD PRICE WEAKENING, PROMPT STRUCTURE TIGHTENING. Supportive: a $110.00 backwardation (nineteenth straight, eighth above $15.00, widest in the series), visible LME stock at a new low of 226,850 t, and Chinese ingot social inventory still drawing (down 14,000 t from the prior Thursday and 40,000 t from the prior Monday, SMM via AL Circle 10-November). "
 "Against: three-month at $3,027.00 is $2.50 above the 3,024.50 bear trigger and below 3,042; improving ex-Middle-East supply and gradual Gulf restarts; Brent near ten-week lows lowering the cost floor; hotter US CPI lifting Fed-hike odds near 88% and the dollar near 102.25.")
d['bottom_line']=("BOTTOM LINE: LME aluminium three-month fell $32.50 to $3,027.00 on the Tuesday 10-November official, breaking below last week's $3,042 low and settling just $2.50 above the 3,024.50 bear trigger, while cash eased only $10.00 to $3,137.00 and the backwardation widened to $110.00 with visible stock at a new low of 226,850 t - nearby metal is tight but the forward curve is pricing more supply and a hawkish Fed. "
 "Weights stay 15% bull / 45% base / 40% bear: no pre-registered rule fired. A settled close below 3,024.50, or a contango beyond $24.50, adds bear weight; re-crediting the bull needs a settled close above 3,077 with the backwardation beyond $15.00. Daily Elliott invalidation 3,289. Next official Wednesday 11-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, PROMPT PREMIUM UP AGAIN:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, PROMPT PREMIUM UP, FORWARD PRICE DOWN: a $110.00 backwardation on 10-November, wider than $87.50 even as cash fell $10.00 and three-month $32.50 - an eighth print above the $15.00 reversal condition, so nearby metal is valued well over forward metal and there is no carry reward for deferring purchases, while the outright three-month price sits only $2.50 above the 3,024.50 bear trigger. "+c2[a1:]
o="is $1,573.50 on 09-November cash, 65.5% of the $2,403/t premium"; assert o in c2; c2=c2.replace(o,f"is ${tl:,.2f} on 10-November cash, {share:.1f}% of the $2,403/t premium")
o="the 09-November official took three-month to $3,059.50, below 3,061.5 and 3,077, $65.00 above the 2,994.50 settled low; energy fell further (Brent near $92 after an almost 6% Monday drop to its lowest since late August, European gas near EUR 81.6/MWh, Trading Economics 10-November); the dollar index eased to about 101.7; December-hike odds about 80%;"
assert o in c2
c2=c2.replace(o,"the 10-November official took three-month to $3,027.00, below 3,042, 3,061.5 and 3,077, $32.50 above the 2,994.50 settled low; Brent held near $92 at ten-week lows while European gas rebounded to about EUR 85.2/MWh (Trading Economics 11-November); US October CPI rose 0.4% m/m against 0.3% expected and next-meeting hike odds rose to about 88% with the dollar index near 102.25;")
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 11-NOVEMBER at 15/45/40: the Tuesday 10-November official settled three-month at $3,027.00 - not above 3,077 (the bull trigger) and $2.50 above 3,024.50 (the bear trigger) - so no pre-registered rule fired, although the close sits at the edge of the bear trigger with the backwardation at $110.00. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 11-NOVEMBER: the 10-November official printed a $110.00 BACKWARDATION, an eighth session above $15.00 and the widest in the stored series, even as flat price fell. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 11-NOVEMBER: LME stock fell 125 t on 10-November to a new low of 226,850 t, a fifteenth straight draw. Trend held at FLAT: the pace remains modest."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 11-NOVEMBER: Brent near $92.3, still near ten-week lows and more than 20% below its late-October peak; TTF rebounded to about EUR 85.2/MWh from ~82.5 on cold weather and storage below 73% (Trading Economics). Trend held at DOWN: oil, the larger driver, has not recovered."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 11-NOVEMBER: Straits Daily Brief - strait still listed CLOSED, but the latest lagged transit count rose to 3 vessels on 08-November (vs 85/day pre-crisis) and AIS-visible vessels holding fell to 38 from 99. Trading Economics reports Middle Eastern oil shipments nearly back to pre-war levels and Bahri sending tankers through with US coordination; President Trump suggested more strikes may not be needed. Counter-signals, reported and UNCONFIRMED: an IRGC claim that two tankers caught fire after explosions, and Iran's security chief saying the strait stays closed until seven US conditions are met (single sources). Trend CUT FROM UP TO FLAT: traffic indicators are improving but no formal reopening has occurred."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 11-NOVEMBER: US October CPI rose 0.4% m/m (0.3% expected), core 0.3% (0.2% expected); Trading Economics cites about 88% odds of a 25bp hike at the next meeting, with Governor Waller reportedly open to 50bp. Trend held at UP."; r['trend']='up'; hit+=1
assert hit==5,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Tue 10-Nov':
        hc+=1; cat['date']='Daily, from Wed 11-Nov'
        cat['event']=("TUESDAY 10-NOVEMBER OFFICIAL: three-month $3,027.00 (-$32.50), cash $3,137.00, backwardation $110.00 - no rule fired, $2.50 above the bear trigger; weights 15/45/40. NEXT: a settled close below 3,024.50 adds bear weight; below about 2,977.5 forces a re-count toward 2,894. A settled close above 3,077 with the backwardation beyond $15.00 returns five points to bull. Invalidation 3,289. US PPI this week; mid-November carbon (anode/CTP/petcoke) settlements; first Q1-2027 Japanese premium offers.")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"WEDNESDAY 11-NOVEMBER ON THE TUESDAY 10-NOVEMBER OFFICIAL: three-month fell $32.50 to $3,027.00 - below the 3,042 low of 03-November and just $2.50 above the 3,024.50 bear trigger - while cash fell only $10.00 to $3,137.00, so the backwardation widened to $110.00 (widest in the series) as stock edged to a new low of 226,850 t. Spread and price moved in opposite directions: the prompt is tight but the forward curve is discounting improving ex-Middle-East supply (Chinese output and exports, Gulf restarts, EGA targeting full Al Taweelah recovery by Q1-2027) and a hotter US CPI that lifted Fed-hike odds to about 88%. Weights unchanged at 15/45/40; a settled close below 3,024.50 would move weight to the bear case. Watch the Wednesday official, US PPI and mid-November carbon settlements.")

EWP=("REVIEWED 11-NOVEMBER ON THE 10-NOVEMBER OFFICIAL: three-month settled 3,027.00 (-32.50), a settled close BELOW the 3,042.00 B/2 low - the pre-registered trigger that FAVOURS THE ALTERNATE. The count is NOT re-labelled (no invalidation level broke) but probabilities shift: alternate (the rebound from 2,994.50 to 3,097.50 was a completed corrective bounce and a new decline is under way) raised to about 60%; base (a deeper wave (ii) of C/3 still holding above 2,994.50) cut to about 40%. A settled close below 2,994.50 would end the base count; below about 2,977.5 forces a re-count toward the 2,894 weekly 61.8%. A recovery above 3,097.50 would restore the base toward 3,110 and 3,148.5. Invalidation 3,289; confidence low. ")
EWL=("REVIEWED 11-NOVEMBER (MID-WEEK): the Tuesday official at 3,027.00 sits well below the 3,061.5 July low and the 3,077 50% retracement, REINFORCING the weekly base case - the corrective count toward the 61.8% retracement at 2,894 - which loses preference only on a weekly close above 3,110. Alternate (2,994.50 completed the correction) trimmed to about 30% (from 35%): the $110.00 backwardation and record-low stock still support it, but the forward price is not confirming. Confidence moderate. ")
pre_s="REVIEWED 10-NOVEMBER ON THE 09-NOVEMBER OFFICIAL:"; pre_l="REVIEWED 10-NOVEMBER: the week has opened"
assert d['ew']['short_term']['writeup'].startswith(pre_s) and d['ew']['long_term']['writeup'].startswith(pre_l)
d['ew']['short_term']['writeup']=EWP+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=EWL+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="92.3",day="about $92.1-92.3 on 11-November (Trading Economics; quote 92.28 +0.87%, stats 92.10 +0.67%); near ten-week lows after falling below $92 on 10-November",
 note="REFRESHED WEDNESDAY 11-NOVEMBER-2026 (Trading Economics): Brent hovered near ten-week lows as US-Iran tensions appeared to ease - President Trump suggested more strikes may not be needed; Iran wants sanctions and the naval blockade eased before talks; Middle Eastern oil shipments are nearly back to pre-war levels and Bahri is sending tankers through Hormuz with US military coordination. Down more than 20% from the late-October peak. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="85.2",day="about EUR 85.2-85.3/MWh on 11-November (Trading Economics; sections differ), +0.5% to +0.7%, recovering from a one-month low near 82.5 on 09-November",
 note="REFRESHED WEDNESDAY 11-NOVEMBER-2026 (Trading Economics): TTF recovered as cold weather, weak wind and heating demand pushed net storage withdrawals to nearly six times the prior week's; EU storage below 73% against an 89% five-year average, Germany below 60%; disrupted Middle East LNG and Norwegian outages keep supply tight, partly offset by higher Qatari loadings. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="102.25",day="about 102.25 on 11-November (Trading Economics, +0.03%)",
 note="REFRESHED WEDNESDAY 11-NOVEMBER-2026 (Trading Economics): US October CPI rose 0.4% m/m (0.3% expected), core 0.3% (0.2% expected); markets price about 88% odds of a 25bp hike at the next meeting, with further hikes priced for January and possibly April; Governor Waller reportedly said 50bp may be needed in December. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.12150',day="LME fixing on 10-November, up from 1.11920 on 09-November",note="REFRESHED WEDNESDAY 11-NOVEMBER-2026 to the 10-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE TUESDAY 10-NOVEMBER-2026 LME OFFICIAL, the latest published session: this Wednesday 11-November run (about 02:40 London) precedes Wednesday's ring, whose official prints at 13:20 London and will be picked up by the next run. The board rolled ONE session this run (from Monday 09-November). The Trading Economics aluminium reference ($3,006.50, -2.18% for 10-November) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (11-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 10-November session (aluminium cash 3,137.00, three-month 3,027.00, stock 226,850; EUR/USD MTLE 1.12150); the aluminium per-metal daily table shows 10-November as its newest row.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 02 to 09-November rows match the stored series exactly; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 10-November values come from both overviews, which agree.")
C[3]=("STOCK CHANGES 10-November (also shown in the pages' change column): aluminium -125 to 226,850; copper -775 to 316,625; nickel unchanged at 271,662; zinc -1,400 to 144,975; lead unchanged at 300,300.")
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (10-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (seven sessions, 02-10 November) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,027.00; the stock chart axis floor of 200,000 t leaves about 26,850 t headroom below visible stock of 226,850 t; it is re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,137.00 against three-month $3,027.00 is therefore a $110.00 BACKWARDATION, wider than $87.50 on 09-November - on Tuesday the spread and the flat price moved in OPPOSITE directions (structure tighter, price lower)."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        o="the tariff leg is 0.50 times the 09-November official cash of $3,147.00, or $1,573.50, leaving a $829.50 residual market leg out of the $2,403/t US duty-paid premium (65.5% policy arithmetic)"
        assert o in cv
        C[i]=cv.replace(o,f"the tariff leg is 0.50 times the 10-November official cash of $3,137.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic)"); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $92.3), the dollar index (about 102.25) and TTF (about EUR 85.2/MWh) are Trading Economics readings for 11-November (Asian hours); Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages again showed different levels in different sections (Brent 92.28 vs 92.10; TTF 85.20 vs 85.34), so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (11-November) shows Brent about $91.82 (-0.58% over 24h) and its header $92.15; the brief labels its ticker as AI-assisted. EUR/USD is the 10-November LME fixing, the same session as the board."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 11-NOVEMBER: no authorised fetch was blocked (Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/TTF/dollar, AL Circle, news.metal.com and the Straits Daily Brief all fetched). news.metal.com showed no dated aluminium print; the SMM daily market note (SHFE, A00, social inventory direction) was read via AL Circle's unchanged republication of 10-November. mining.com was not fetched. A search for Q1-2027 Japanese premium offers found none - only S&P Global's October report that participants expected Q1-2027 talks around $190-200/mt - so Q1 stays unpriced and no range is published. Hormuz incident reports are cited as reported/UNCONFIRMED per the brief."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        C[i]=("PEER EARNINGS: NO NEW PEER RESULT AND NO earnings_history BACK-FILL THIS RUN (11-NOVEMBER). "+cv.split("PEER EARNINGS:",1)[1].strip()); hit+=1
assert hit==4,hit

d['so_what']={"line":"LME aluminium three-month fell $32.50 to $3,027 on Tuesday - just $2.50 above the $3,024.50 bear trigger - even as the cash premium widened to a record $110 and LME stock hit another low: the prompt is tight, but the forward curve is pricing more ex-Middle-East supply and a hawkish Fed.",
 "points":[
 "WHAT MOVED: the Tuesday 10-November official cut three-month $32.50 to $3,027.00 (lowest since 26-October) and cash $10.00 to $3,137.00, so the backwardation widened to $110.00 from $87.50 - spread and price moved in opposite directions; visible LME stock fell 125 t to 226,850 t, a fifteenth straight draw.",
 "WHY: Trading Economics points to improving supply outside the Middle East (near-record Chinese output and exports, gradual Gulf smelter restarts, EGA targeting full Al Taweelah recovery by Q1-2027), while US October CPI (+0.4% m/m vs 0.3% expected) lifted Fed-hike odds to about 88%; nickel led the base-metals board lower (-1.98%).",
 "SUPPORT STILL THERE: China's aluminium ingot social inventory kept drawing (down 40,000 t week-on-week, SMM via AL Circle) and Hormuz traffic indicators are improving without a formal reopening (Straits Daily Brief; incident reports unconfirmed).",
 "WHAT TO WATCH: a settled close below $3,024.50 (bear trigger) or above $3,077 (bull trigger); US PPI; mid-November carbon-input settlements; first Q1-2027 Japanese premium offers (participants expected about $190-200/t, S&P Global)."]}

d['feed']=([
 {"when":"Tue 10-Nov","impact":"Bearish","text":"10-NOVEMBER OFFICIAL: three-month $3,027.00 (-$32.50), cash $3,137.00 (-$10.00); backwardation $110.00, widest in series; stock -125 t to 226,850 t."},
 {"when":"Tue 10-Nov","impact":"Bearish","text":"US CPI: October +0.4% m/m vs 0.3% expected; next-meeting Fed-hike odds ~88%; dollar index ~102.25 (Trading Economics)."},
 {"when":"Tue 10-Nov","impact":"Mixed","text":"WORSLEY: 48-hour union stoppage at the 4.4 Mt/yr alumina refinery over pay ahead of the Alcoa takeover; South32 expects no production impact (AL Circle)."},
 {"when":"Wed 11-Nov","impact":"Mixed","text":"HORMUZ: still listed closed; 3 transits on 08-Nov, vessels holding down to 38 from 99; IRGC tanker-fire claim unconfirmed (Straits Daily Brief)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM THREE-MONTH DROPS TO $3,027 AS BACKWARDATION HITS $110. The Tuesday 10-November official settled three-month at $3,027.00 (-1.06%), below the 3,042 low of 03-November and $2.50 above the 3,024.50 bear trigger, while cash eased only 0.32% to $3,137.00 - the cash premium widened to $110.00, the widest in the stored series, and visible stock fell 125 t to a new low of 226,850 t. Board: nickel -1.98%, aluminium -1.06%, lead -0.37%, copper -0.18%, zinc +0.27%. READ: spread and price moved in opposite directions - tight prompt, weaker forward."},
 {"theme":"Supply","horizon":"0-6 months","impact":"Bearish","url":S_TE,
  "headline":"EX-MIDDLE-EAST SUPPLY IMPROVING (Trading Economics, 11-November): aluminium stays near multi-month lows as China offsets reduced Gulf supply with near-record domestic output and rising exports, some Gulf smelters are gradually restarting, and EGA expects full recovery at Al Taweelah by the first quarter of 2027. READ: the forward curve is pricing the return of Gulf metal."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"HOT US CPI LIFTS FED-HIKE ODDS (Trading Economics, 11-November): October consumer prices rose 0.4% m/m against 0.3% expected and core 0.3% against 0.2%; markets price about 88% odds of a 25bp hike at the next meeting, with Governor Waller reportedly open to 50bp. Dollar index near 102.25. READ: tighter financial conditions weigh on metals demand and investor length."},
 {"theme":"China","horizon":"Immediate","impact":"Bullish","url":S_SM,
  "headline":"CHINA INVENTORY DRAWDOWN (SMM via AL Circle, 10-November): aluminium ingot social inventory fell 14,000 t from the prior Thursday and 40,000 t from the prior Monday; SHFE aluminium closed RMB 23,170/t (-0.22%), SMM A00 RMB 23,540/t (+200); SMM notes weakening demand at the end of the peak season limits rebound space."},
 {"theme":"Alumina","horizon":"Immediate","impact":"Mixed","url":S_WR,
  "headline":"WORSLEY ALUMINA STOPPAGE (AL Circle, 10-November): about 200 ETU and AMWU members at South32's 4.4 Mt/yr Worsley refinery began a 48-hour stoppage on 10-November, coinciding with a scheduled shutdown of the main processing plant, seeking pay and conditions secured before Alcoa's planned acquisition (completion targeted 29-June-2027). South32 said it does not expect production to be affected."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Mixed","url":S_ST,
  "headline":"HORMUZ TRAFFIC EDGES UP, STRAIT STILL LISTED CLOSED (Straits Daily Brief, 11-November): 3 transits on 08-November (IMF PortWatch) vs 85/day pre-crisis; AIS-visible vessels holding fell to 38. Trading Economics reports Middle Eastern oil shipments nearly back to pre-war levels and Bahri sending tankers with US coordination. Reported, UNCONFIRMED: an IRGC claim of two tankers on fire after explosions and an Iranian statement that the strait stays closed until seven US conditions are met."},
]+d['news']
d['news']=d['news'][:20]

hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('Alcoa'):
        p['update']="UPDATED 11-NOVEMBER: AL Circle (10-November) reports about 200 ETU and AMWU members at South32's 4.4 Mt/yr Worsley alumina refinery began a 48-hour stoppage on 10-November over pay and conditions ahead of Alcoa's planned acquisition (completion targeted 29-June-2027); South32 expects no production impact ("+S_WR+"). "+p['update']; hit+=1
    elif p['name'].startswith('EGA'):
        p['update']="REVIEWED 11-NOVEMBER: Trading Economics (11-November) again cites EGA's expectation of full recovery at Al Taweelah by Q1-2027 and gradual restarts at some Gulf smelters ("+S_TE+"); no newer EGA operational release located. "+p['update']; hit+=1
    elif p['name'].startswith('China operators'):
        p['update']="UPDATED 11-NOVEMBER (SMM via AL Circle, 10-November): aluminium ingot social inventory down 14,000 t from the prior Thursday and 40,000 t from the prior Monday; SHFE RMB 23,170/t, A00 RMB 23,540/t; Trading Economics describes Chinese output as near-record with exports rising ("+S_SM+"). "+p['update']; hit+=1
    elif p['name'].startswith('US / Canada'):
        p['update']="REVIEWED 11-NOVEMBER: no change to the 50% Section 232 rate located. "+p['update']; hit+=1
assert hit==4

d['earnings_note']=d['earnings_note']
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 10-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 10-Nov)",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_WR,S_WR],[L_SM,S_SM],[L_CF,S_CF],[L_JP,S_JP]): d['sources'].append(x)
for x in ([L_TE,S_TE],[L_TD,S_TD],[L_ST,S_ST],[L_JP,S_JP]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-11-09'
ph['rows'][-1]=['2026-11-10',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2),d['metals_board'])
