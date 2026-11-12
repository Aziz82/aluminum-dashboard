# Daily data refresh - 2026-11-12 (THURSDAY, ~02:40 UTC). Board ROLLED ONE SESSION to the WEDNESDAY 11-Nov LME official.
# Westmetall cache-busted EN + DE overviews agree on 11-Nov (Al cash 3,223.50 / 3M 3,064.00 / stock 226,725; MTLE 1.11320);
# aluminium per-metal table newest row 11-Nov and its 02-10 Nov rows match the stored series.
# 3M 3,064.00: not above 3,077 and not below 3,024.50 -> weights unchanged 15/45/40. Back above 3,042 -> EW daily alternate preference neutralised (no re-label).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-12'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-12"; L_ST="Straits Daily Brief - Strait of Hormuz, 12-Nov-2026 (ticker AI-assisted)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum 3,063.25 (+1.89%) on 11-Nov-2026 (CFD reference); prompt spread at five-month high, Chinese overseas capacity build (12-Nov-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$92.0; US-Iran talks deadlocked; Saudi October output +26% to 10.56 mb/d (12-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~102.94, highest since April 2025; ~91% odds of a hike next month (12-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 87.1/MWh; EU storage below 73% (12-Nov-2026)"
S_LA="https://www.alcircle.com/news/lme-aluminium-stocks-fall-52-6-in-nine-months-with-q3-average-down-43-6-year-on-year-121917"; L_LA="AL Circle - LME aluminium stocks fall 52.6% in nine months; Q3 average down 43.6% y/y (11-Nov-2026)"
S_CA="https://www.alcircle.com/news/the-us-canada-aluminum-deal-could-put-european-buyers-under-pressure-as-imports-shift-121915"; L_CA="AL Circle - possible US-Canada deal could cut the US tariff on Canadian aluminium to 25% from 50% (reported/proposed, 11-Nov-2026)"
S_CY="https://www.alcircle.com/news/century-aluminum-prepares-for-next-phase-of-4b-oklahoma-smelter-targets-2030-production-121908"; L_CY="AL Circle - Century Aluminum prepares next phase of $4bn, 750 kt/yr Oklahoma smelter, 2030 target (Nov-2026)"
S_VB="https://www.alcircle.com/news/vedanta-bets-on-captive-bauxite-as-omcl-pricing-dispute-threatens-cost-advantage-121919"; L_VB="AL Circle - Vedanta bets on captive Sijimali bauxite amid OMCL pricing dispute (11-Nov-2026)"
S_MA="https://www.arabnews.pk/business/knowledge-economic-city-maaden-report-higher-q3-revenues-as-profit-growth-diverges-3006548"; L_MA="Arab News - Maaden (1211) Q3-2026: revenue $3.0bn (+11%), EBITDA $0.9bn (-24%), aluminium EBITDA $419m (09-Nov-2026)"

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3137.0 and B['LME 3-month']['cur']==3027.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3137.0,3027.0,226850
cash,m3,stk=3223.5,3064.0,226725
spr=cash-m3; psp=pc-pm; assert spr==159.5 and psp==110.0 and ps-125==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED THURSDAY 12-NOVEMBER-2026 ABOUT 02:40 LONDON, BEFORE THURSDAY'S RING, SO THE BOARD IS THE WEDNESDAY 11-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION (THURSDAY'S PRINTS 13:20 LONDON). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 11-November official for all metals with stocks and FX (EUR/USD MTLE 1.11320; 10-November 1.12150); (2) the aluminium per-metal daily table shows 11-November as its newest row and its 02 to 10-November rows match the stored series exactly. "
 "The whole board sits on ONE UNIFORM SESSION (11-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" WEDNESDAY 11-NOVEMBER (the board): CASH SETTLED $3,223.50, UP $86.50 OR 2.76% FROM $3,137.00. THREE-MONTH SETTLED $3,064.00, UP $37.00 OR 1.22% FROM $3,027.00 - back above the 3,042.00 low of 03-November but $13.00 below 3,077 and $33.50 below the 3,097.50 high of 05-November; $39.50 above the 3,024.50 bear-trigger level and $53.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION WIDENED AGAIN, TO $159.50 FROM $110.00, AS FLAT PRICE ROSE - SPREAD AND PRICE MOVED IN THE SAME DIRECTION (tighter and higher) after moving in opposite directions on Tuesday: cash rose more than twice as much as three-month. A twentieth straight backwardation, the ninth above $15.00 and the widest in the stored series. "
 "VISIBLE LME STOCK FELL 125 t TO 226,725 t, another new series low and a sixteenth straight draw. The Trading Economics aluminium reference showed $3,063.25 (+1.89%) for 11-November - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,223.5","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,064.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $13.00 BELOW THE 3,077 WEEKLY 50% RETRACEMENT and $2.50 above the 3,061.5 July low, $84.50 beneath the 3,148.5 wave (iv) high and $225.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a nineteenth session, $69.50 below."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+159.5","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,223.50 against three-month $3,064.00 is a $159.50 BACKWARDATION, WIDER than 10-November's $110.00 as cash rose $86.50 and three-month $37.00 - SPREAD AND PRICE MOVED IN THE SAME DIRECTION (structure tighter, price higher), reversing Tuesday's divergence. It stays above the published $15.00 reversal condition for a ninth session, a twentieth straight backwardation and the widest print in the stored series; a contango beyond $24.50 would reverse the structural signal. Trading Economics separately describes the LME prompt spread at a five-month high. The October mean spread was $"+f"{oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"226,725","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 125 t TO 226,725 t (10-November: -125 t to 226,850 t), another new series low and a sixteenth straight draw. AL Circle (11-November) notes LME aluminium stocks fell 52.6% in the nine months to 30-September. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 10-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $3,064.00, UP $37.00 FROM THE 10-NOVEMBER $3,027.00 - back above 3,042.00 but $13.00 below 3,077; $39.50 above 3,024.50; $53.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 125 t TO 226,725 t, another new series low (10-November 226,850 t). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $159.50 BACKWARDATION, WIDER THAN 10-NOVEMBER'S $110.00 (09-November $87.50). CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On Wednesday cash rose $86.50 and three-month $37.00, so STRUCTURE TIGHTENED AND PRICE ROSE (same direction). REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00 and $159.50."},
 {"name":"EUR/USD LME fixing","cur":1.1132,"prev":1.1215,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.11320 ON 11-NOVEMBER FROM 1.12150 ON 10-NOVEMBER as the dollar strengthened. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (11-Nov official)","price":"3,223.5","basis":"THE WEDNESDAY 11-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,223.50, UP $86.50 OR 2.76% (10-November $3,137.00). Next official Thursday 12-November 13:20 London."},
 {"tenor":"3-month (11-Nov official)","price":"3,064.0","basis":"THE 11-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $3,064.00, UP $37.00 - $13.00 below 3,077, $22.00 above 3,042.00, $39.50 above 3,024.50 and $69.50 above the 2,994.50 October low."},
 {"tenor":"Cash-to-3M structure","price":"+159.5 (BACKWARDATION)","basis":"A $159.50 BACKWARDATION, wider than $110.00 with price HIGHER (same direction) - above the $15.00 reversal condition for a ninth session."},
 {"tenor":"Visible LME stock","price":"226,725 t","basis":f"DOWN 125 t to a new series low on 11-November (sixteenth straight draw); October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PROMPT TIGHTNESS UP AGAIN, OUTRIGHT PRICE REBOUNDS. On the 11-November official cash $3,223.50 sits $159.50 ABOVE three-month $3,064.00, a BACKWARDATION, wider than $110.00 on 10-November as both legs rose (cash +$86.50, three-month +$37.00) - SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION on Wednesday, after diverging on Tuesday. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00 and now $159.50. "
 f"READ: a twentieth straight backwardation, the ninth above $15.00, with visible stock at another low (226,725 t) - nearby LME metal is scarce and the squeeze is leading the outright price, which Trading Economics attributes to brief supply tightness outweighing ample Chinese production. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2900,3450] and d['chart_stock_axis']==[200000,255000]

ls=d['lme_series']; assert ls[-1][0]=='10-Nov'
d['lme_series']=ls[1:]+[["11-Nov",cash,m3,stk]]
assert len(d['lme_series'])==15 and all(200000<r[3]<255000 and 2900<r[2]<3450 and 2900<r[1]<3450 for r in d['lme_series'])
CU=(13875.5,13795.0,319675); NI=(15930.0,16140.0,271632); ZN=(3794.0,3746.0,143575); PB=(1845.0,1880.0,292125)
CU6=(13992.0,13830.0,316625); NI6=(15875.0,16075.0,271662); ZN6=(3768.0,3734.0,144975); PB6=(1846.0,1882.0,300300)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU6[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI6[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN6[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB6[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU6[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI6[1],1)
zn7=[3935.0,3869.0,3875.0,3877.0,3759.0,3754.0,3768.0]; pb7=[1869.5,1862.0,1858.0,1866.5,1857.0,1854.0,1846.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zn7)+ZN[0])/8)/(sum(zn7)/7),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(pb7)+PB[0])/8)/(sum(pb7)/7),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU6[0]),('NI',NI[0],NI6[0]),('ZN',ZN[0],ZN6[0]),('PB',PB[0],PB6[0])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-11-11'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending WEDNESDAY 11-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 21-October dropped, 11-November appended, so the window is 22-October to 11-November. Every point is an official cash settlement from the Westmetall per-metal tables and English/German overviews (11-November read from both overviews, which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (11-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,CU6,f" COPPER 11-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU6[0])}; three-month ${CU[1]:,.2f}, {chg(CU[1],CU6[1])}. BACKWARDATION narrowed to $80.50 from $162.00. Stock ROSE 3,050 t to 319,675 t."),
 ("Nickel",NI,NI6,f" NICKEL 11-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI6[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI6[1])}. CONTANGO widened to $210.00 from $200.00, still the widest carry on the board. Stock fell 30 t to 271,632 t."),
 ("Zinc",ZN,ZN6,f" ZINC 11-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN6[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN6[1])}. BACKWARDATION widened to $48.00 from $34.00. Stock fell 1,400 t to 143,575 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,PB6,f" LEAD 11-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB6[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB6[1])}. CONTANGO $35.00 from $36.00. Stock fell 8,175 t to 292,125 t, the largest draw on the board."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Wednesday 11-November official three-month aluminium rose 1.22%, zinc 0.32% and nickel 0.40%, while copper fell 0.25% and lead 0.11%. Lead and zinc drew stock; copper stock rose. Trading Economics reports the dollar index near 102.94, its highest since April 2025, with markets pricing about 91% odds of a Fed hike next month; Brent held near $92. The LME euro fixing fell to 1.1132.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,c6,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='10-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["11-Nov",CU[0]]]; assert len(i['hist'])==15
        i['val']="~13,795.00 (3M); 13,875.50 (cash) $/t"; i['ratio']="~13,875.50 $/t cash vs LME 3M 13,795.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the WEDNESDAY 11-NOVEMBER-2026 session at $13,875.50 (10-November $13,992.00). THE WINDOW ROLLED THIS RUN: 21-October dropped and 11-November appended, so the series is the last fifteen published official cash sessions, 22-October to 11-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English/German overviews. "
                  "Copper structure for context: backwardation $80.50 on 11-November; stock 319,675 t (+3,050 t).")
s=d['inputs_summary']; assert s.startswith("UPDATE 11-NOVEMBER")
d['inputs_summary']=("UPDATE 12-NOVEMBER: Copper rolled one session to the Wednesday 11-November LME official cash of $13,875.50, its fifteen-session window now 22-October to 11-November. No new monthly carbon settlement (due mid-November) or dated SMM fluoride, silicon or magnesium mark was located, so no other hist mark was appended. Energy: Brent near $92.0 with US-Iran talks deadlocked and Saudi October crude output up 26% to 10.56 mb/d; European gas firmer near EUR 87.1/MWh with EU storage below 73% (Trading Economics, 12-November). Upstream: Vedanta is leaning on its captive Sijimali bauxite mine as a pricing dispute with OMCL threatens its cost advantage (AL Circle, 11-November). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OT="the tariff leg of the US duty-paid premium is 0.50 times the 10-November official cash of $3,137.00, or $1,568.50, DOWN $5.00 against the 09-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of $834.50, so 65.3%"
NT=f"the tariff leg of the US duty-paid premium is 0.50 times the 11-November official cash of $3,223.50, or ${tl:,.2f}, UP $43.25 against the 10-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OC1="COMPILED WEDNESDAY 11-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE TUESDAY 10-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; WEDNESDAY'S OFFICIAL PRINTS 13:20 LONDON)."
NC1="COMPILED THURSDAY 12-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE WEDNESDAY 11-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; THURSDAY'S OFFICIAL PRINTS 13:20 LONDON)."
for p in d['premiums']:
    assert OT in p['src'] and OC1 in p['src'],p['name']
    p['src']=p['src'].replace(OT,NT).replace(OC1,NC1)
ra=398.24/m3*100
OR="THE RATIO: LME Alumina at $398.24/t against the 10-November aluminium three-month of $3,027.00 is 13.16%"
for a in d['alumina']:
    assert OR in a['src'],a['name']
    a['src']=a['src'].replace(OR,f"THE RATIO: LME Alumina at $398.24/t against the 11-November aluminium three-month of $3,064.00 is {ra:.2f}%").replace(OC1,NC1)
OC0="COMPILED WEDNESDAY 11-NOVEMBER-2026 ABOUT 02:40 LONDON; THE BOARD IS THE TUESDAY 10-NOVEMBER-2026 LME OFFICIAL."
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace(OC1,NC1).replace(OC0,"COMPILED THURSDAY 12-NOVEMBER-2026 ABOUT 02:40 LONDON; THE BOARD IS THE WEDNESDAY 11-NOVEMBER-2026 LME OFFICIAL.")
        o=o.replace("REVIEWED 11-NOVEMBER: no newer public disclosure","REVIEWED 12-NOVEMBER: no newer public disclosure").replace("REVIEWED 11-NOVEMBER. NO NEW DATED","REVIEWED 12-NOVEMBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status','inputs','logistics','raw_materials'):
    if k in d: d[k]=walk(d[k])

d['lme_commentary']=("SQUEEZE LEADS A REBOUND. The Wednesday 11-November official lifted cash $86.50 to $3,223.50 and three-month $37.00 to $3,064.00, so the backwardation widened to $159.50 - the widest in the stored series and a twentieth straight backwardation - with spread and price moving in the SAME direction after Tuesday's divergence. Visible stock fell another 125 t to a new low of 226,725 t. "
 "Three-month recovered above the 3,042 low of 03-November but stopped $13.00 short of the 3,077 bull trigger, so no pre-registered rule fired and weights stay 15/45/40; the daily Elliott alternate's preference is neutralised. "
 "Trading Economics attributes the bounce from Tuesday's sub-$3,000 CFD low to brief supply tightness outweighing ample Chinese production, with US-Iran tensions still restricting Gulf output and LME inventories about half pre-war levels; offsetting this, Chinese producers are building more than 15 Mt of smelting capacity abroad, led by Indonesia, and the dollar index rose to about 102.94, its highest since April 2025. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" its October mean.")
d['net_read']=("NET: NEUTRAL - PROMPT SQUEEZE INTENSIFYING, FORWARD PRICE STILL CAPPED. Supportive: a $159.50 backwardation (twentieth straight, ninth above $15.00, widest in the series), visible LME stock at a new low of 226,725 t, Gulf output still constrained by US-Iran tensions and new Hormuz incident reports (unconfirmed). "
 "Against: three-month at $3,064.00 remains below the 3,077 bull trigger; Chinese overseas smelter build-out (over 15 Mt planned, Indonesia leading); a dollar index near 102.94 and about 91% odds of a Fed hike next month; Brent near $92 keeping the energy cost floor lower.")
d['bottom_line']=("BOTTOM LINE: LME aluminium three-month rose $37.00 to $3,064.00 on the Wednesday 11-November official and cash jumped $86.50 to $3,223.50, widening the backwardation to a series-record $159.50 as visible stock fell to a new low of 226,725 t - nearby metal is getting scarcer and is pulling the curve up, but the forward price is still below the 3,077 bull trigger and faces a firm dollar and growing ex-China supply. "
 "Weights stay 15% bull / 45% base / 40% bear: no pre-registered rule fired. A settled close above 3,077 with the backwardation beyond $15.00 returns five points to bull; a settled close below 3,024.50, or a contango beyond $24.50, adds bear weight. Daily Elliott invalidation 3,289. Next official Thursday 12-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, PROMPT PREMIUM UP, FORWARD PRICE DOWN:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, PROMPT PREMIUM UP AGAIN: a $159.50 backwardation on 11-November, wider than $110.00 as cash rose $86.50 and three-month $37.00 - a ninth print above the $15.00 reversal condition, so nearby metal is valued well over forward metal and there is no carry reward for deferring purchases; the outright three-month price sits $13.00 below the 3,077 bull trigger. "+c2[a1:]
o="is $1,568.50 on 10-November cash, 65.3% of the $2,403/t premium"; assert o in c2; c2=c2.replace(o,f"is ${tl:,.2f} on 11-November cash, {share:.1f}% of the $2,403/t premium")
o="the 10-November official took three-month to $3,027.00, below 3,042, 3,061.5 and 3,077, $32.50 above the 2,994.50 settled low; Brent held near $92 at ten-week lows while European gas rebounded to about EUR 85.2/MWh (Trading Economics 11-November); US October CPI rose 0.4% m/m against 0.3% expected and next-meeting hike odds rose to about 88% with the dollar index near 102.25;"
assert o in c2
c2=c2.replace(o,"the 11-November official lifted three-month to $3,064.00, back above 3,042 but below 3,077, $69.50 above the 2,994.50 settled low; Brent near $92 and European gas near EUR 87.1/MWh (Trading Economics 12-November); the dollar index near 102.94, its highest since April 2025, with about 91% odds of a Fed hike next month; a possible US-Canada deal that would cut the US tariff on Canadian aluminium to 25% is reported but unconfirmed (AL Circle 11-November); Maaden (1211) reported Q3-2026 aluminium EBITDA of $419m (Arab News 09-November);")
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 12-NOVEMBER at 15/45/40: the Wednesday 11-November official settled three-month at $3,064.00 - $13.00 short of 3,077 (the bull trigger, which also needs a backwardation beyond $15.00; it is $159.50) and $39.50 above 3,024.50 (the bear trigger) - so no pre-registered rule fired. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 12-NOVEMBER: the 11-November official printed a $159.50 BACKWARDATION, a ninth session above $15.00 and the widest in the stored series, as flat price rose. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 12-NOVEMBER: LME stock fell 125 t on 11-November to a new low of 226,725 t, a sixteenth straight draw; AL Circle notes LME stocks fell 52.6% in the nine months to September. Trend held at FLAT: the daily pace remains modest."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 12-NOVEMBER: Brent near $92.0, more than 20% below its October peak, with Saudi October output up 26% to 10.56 mb/d; TTF firmer near EUR 87.1/MWh on low storage (Trading Economics). Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 12-NOVEMBER: Straits Daily Brief - strait still listed CLOSED; lagged count 3 transits on 08-November (vs 85/day pre-crisis); AIS-visible vessels holding rose to 42 from 38. New incident reports: TradeWinds reports a strike on a Sinokor VLCC injured four seafarers; Iran's army says a tanker caught fire after hitting a mine (unconfirmed by any maritime authority); an IRGC claim of an attack on navigation systems on Oman's Didamar island (Iranian state media, unverified). Trading Economics reports US-Iran talks deadlocked, with Iran demanding sanctions relief and an end to the naval blockade before reopening. Trend RAISED FROM FLAT TO UP: incident reports increased and no reopening path is visible."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 12-NOVEMBER: the dollar index rose to about 102.94, its highest since April 2025, with markets pricing about 91% odds of a hike next month (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('TARIFF POLICY'):
        r['risk']+=" UPDATE 12-NOVEMBER: AL Circle (11-November) discusses a POSSIBLE US-Canada agreement that would cut the US tariff on Canadian aluminium to 25% from 50% - reported/proposed, no official confirmation or effective date located; the 50% Section 232 rate is unchanged. Trend held at FLAT."; r['trend']='flat'; hit+=1
assert hit==6,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Wed 11-Nov':
        hc+=1; cat['date']='Daily, from Thu 12-Nov'
        cat['event']=("WEDNESDAY 11-NOVEMBER OFFICIAL: three-month $3,064.00 (+$37.00), cash $3,223.50 (+$86.50), backwardation $159.50 - no rule fired, $13.00 below the bull trigger; weights 15/45/40. NEXT: a settled close above 3,077 with the backwardation beyond $15.00 returns five points to bull; a settled close below 3,024.50 adds bear weight; below about 2,977.5 forces a re-count toward 2,894. Invalidation 3,289. US PPI this week; mid-November carbon (anode/CTP/petcoke) settlements; any official US-Canada tariff announcement; first Q1-2027 Japanese premium offers.")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"THURSDAY 12-NOVEMBER ON THE WEDNESDAY 11-NOVEMBER OFFICIAL: cash jumped $86.50 to $3,223.50 and three-month rose $37.00 to $3,064.00, widening the backwardation to a series-record $159.50 as stock fell to another low of 226,725 t. Spread and price moved together this time: the prompt squeeze is leading the curve higher, which Trading Economics attributes to brief supply tightness while US-Iran tensions keep restricting Gulf output. Against that, Chinese producers are building more than 15 Mt of overseas smelting capacity and the dollar index is at its highest since April 2025 with about 91% odds of a Fed hike next month. Three-month is $13.00 below the 3,077 bull trigger, so weights stay 15/45/40. Watch the Thursday official, US PPI, mid-November carbon settlements and any official US-Canada tariff move.")

EWP=("REVIEWED 12-NOVEMBER ON THE 11-NOVEMBER OFFICIAL: three-month settled 3,064.00 (+37.00), BACK ABOVE the 3,042.00 B/2 low, which neutralises Tuesday's trigger favouring the alternate. The count is NOT re-labelled; probabilities return to about 50/50 between the base (a deeper wave (ii) of C/3 holding above 2,994.50, now targeting 3,110 then 3,148.5) and the alternate (the rebound from 2,994.50 to 3,097.50 was a completed corrective bounce and 3,064 is a lower-high attempt). A settled close above 3,097.50 confirms the base; a settled close below 3,024.50 restores the alternate and below 2,994.50 ends the base count. Invalidation 3,289; confidence low. ")
EWL=("REVIEWED 12-NOVEMBER (MID-WEEK): the Wednesday official at 3,064.00 rebounded to just above the 3,061.5 July low but stays below the 3,077 50% retracement, so the weekly base case - the corrective count toward the 61.8% retracement at 2,894 - is unchanged and loses preference only on a weekly close above 3,110. Alternate (2,994.50 completed the correction) held at about 30%: the $159.50 backwardation and record-low stock support it, but the forward price has not yet cleared 3,077. Confidence moderate. ")
pre_s="REVIEWED 11-NOVEMBER ON THE 10-NOVEMBER OFFICIAL:"; pre_l="REVIEWED 11-NOVEMBER (MID-WEEK):"
assert d['ew']['short_term']['writeup'].startswith(pre_s) and d['ew']['long_term']['writeup'].startswith(pre_l)
d['ew']['short_term']['writeup']=EWP+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=EWL+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="92.0",day="about $92.0-92.1 on 12-November (Trading Economics; table 92.03 -0.79%, stats 92.14); after rebounding above $93 on Wednesday from a ten-week low",
 note="REFRESHED THURSDAY 12-NOVEMBER-2026 (Trading Economics): Brent held near $92 as US-Iran negotiations remain deadlocked but both sides avoid escalation; Iran wants sanctions lifted and the naval blockade ended before Hormuz reopens; Saudi October crude output rose 26% to 10.56 mb/d; API showed a 9 mb US crude build; Ukrainian drone strikes have disrupted about 30% of Russian refining capacity. Still more than 20% below its October peak. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="87.1",day="about EUR 87.05-87.21/MWh on 12-November (Trading Economics; sections differ), +0.45% to +0.64%, up from a one-month low near 82.5 on 09-November",
 note="REFRESHED THURSDAY 12-NOVEMBER-2026 (Trading Economics): EU storage below 73% against a five-year average of about 89-90%, Germany below 60%; disrupted Middle East LNG, Norwegian outages and Asian competition keep supply tight, partly offset by de-escalation hopes and higher Qatari loadings. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="102.94",day="about 102.94 on 12-November (Trading Economics, +0.09%), highest since April 2025 after gaining more than 1% over two sessions",
 note="REFRESHED THURSDAY 12-NOVEMBER-2026 (Trading Economics): stronger-than-expected October inflation and hawkish Fed commentary drove the rally; markets price about 91% odds of a hike next month, with further tightening possible in early 2027. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.11320',day="LME fixing on 11-November, down from 1.12150 on 10-November",note="REFRESHED THURSDAY 12-NOVEMBER-2026 to the 11-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE WEDNESDAY 11-NOVEMBER-2026 LME OFFICIAL, the latest published session: this Thursday 12-November run (about 02:40 London) precedes Thursday's ring, whose official prints at 13:20 London and will be picked up by the next run. The board rolled ONE session this run (from Tuesday 10-November). The Trading Economics aluminium reference ($3,063.25, +1.89% for 11-November) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (12-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 11-November session (aluminium cash 3,223.50, three-month 3,064.00, stock 226,725; EUR/USD MTLE 1.11320); the aluminium per-metal daily table shows 11-November as its newest row.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 02 to 10-November rows match the stored series exactly; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 11-November values come from both overviews, which agree, and each metal's stock change reconciles with its 10-November stock.")
C[3]=("STOCK CHANGES 11-November (also shown in the pages' change column): aluminium -125 to 226,725; copper +3,050 to 319,675; nickel -30 to 271,632; zinc -1,400 to 143,575; lead -8,175 to 292,125.")
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (11-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (eight sessions, 02-11 November) as their latest point. The price chart axis (floor 2,900, ceiling 3,450) brackets cash 3,223.50 and three-month 3,064.00; the stock chart axis floor of 200,000 t leaves about 26,725 t headroom below visible stock of 226,725 t; it is re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,223.50 against three-month $3,064.00 is therefore a $159.50 BACKWARDATION, wider than $110.00 on 10-November - on Wednesday the spread and the flat price moved in the SAME direction (structure tighter, price higher)."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        o="the tariff leg is 0.50 times the 10-November official cash of $3,137.00, or $1,568.50, leaving a $834.50 residual market leg out of the $2,403/t US duty-paid premium (65.3% policy arithmetic)"
        assert o in cv
        C[i]=cv.replace(o,f"the tariff leg is 0.50 times the 11-November official cash of $3,223.50, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). A possible US-Canada deal cutting the Canadian rate to 25% is REPORTED ONLY (AL Circle, 11-November) and is not applied"); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $92.0), the dollar index (about 102.94) and TTF (about EUR 87.1/MWh) are Trading Economics readings for 12-November (Asian hours); Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages again showed different levels in different sections (Brent 92.03 vs 92.14; TTF 87.05 vs 87.21), so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (12-November) shows Brent about $92.43 (+0.65% over 24h) and its header $92.19; the brief labels its ticker as AI-assisted. EUR/USD is the 11-November LME fixing, the same session as the board."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 12-NOVEMBER: no authorised fetch was blocked (Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/TTF/dollar, AL Circle, news.metal.com and the Straits Daily Brief all fetched). news.metal.com showed no dated aluminium price print and AL Circle carried no new SMM daily note, so SHFE/A00/social-inventory figures are not refreshed this run. mining.com was not fetched. A search for Q1-2027 Japanese premium offers found none (S&P Global says participants expect premiums to stay under pressure into Q1-2027), so Q1 stays unpriced and no range is published. Hormuz incident reports are cited as reported/UNCONFIRMED per the brief. Maaden Q3-2026 figures come from a single Arab News report of the Tadawul statement and were not cross-checked against the filing."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        C[i]=("PEER EARNINGS: ONE NEW PEER RESULT ADDED THIS RUN (12-NOVEMBER) - MAADEN (1211) Q3-2026 (Arab News, 09-November, citing the Tadawul statement): revenue $3.0bn (+11% y/y), EBITDA $0.9bn (-24%), net profit attributable $0.4bn (no y/y given), aluminium segment revenue $985m (+32%) and EBITDA $419m (more than doubled). The 1211 earnings_history strip is NOT extended: it is kept in SAR bn and the report gives only a rounded USD figure, so no converted or estimated point is published. "+cv.split("PEER EARNINGS:",1)[1].strip()); hit+=1
assert hit==4,hit

d['so_what']={"line":"LME aluminium cash jumped $86.50 to $3,223.50 and three-month $37 to $3,064 on Wednesday, widening the backwardation to a record $159.50 as LME stock hit another low - the prompt squeeze is now pulling the curve up, but three-month is still $13 below the $3,077 bull trigger against a dollar at its highest since April 2025.",
 "points":[
 "WHAT MOVED: the Wednesday 11-November official lifted cash 2.76% to $3,223.50 and three-month 1.22% to $3,064.00, so the backwardation widened to $159.50 from $110.00 - spread and price moved together this time; visible LME stock fell 125 t to 226,725 t, a sixteenth straight draw.",
 "WHY: Trading Economics attributes the rebound from Tuesday's sub-$3,000 reference low to brief supply tightness, with US-Iran tensions still restricting Gulf output and LME stocks about half pre-war levels; Hormuz remains listed closed with fresh, unconfirmed tanker-incident reports (Straits Daily Brief).",
 "HEADWINDS: the dollar index near 102.94 (highest since April 2025) with about 91% odds of a Fed hike next month, and Chinese producers building over 15 Mt of smelting capacity abroad, led by Indonesia.",
 "WHAT TO WATCH: a settled three-month close above $3,077 (bull trigger) or below $3,024.50 (bear trigger); US PPI; mid-November carbon-input settlements; whether a reported US-Canada deal cutting the Canadian tariff to 25% is confirmed."]}

d['feed']=([
 {"when":"Wed 11-Nov","impact":"Bullish","text":"11-NOVEMBER OFFICIAL: three-month $3,064.00 (+$37.00), cash $3,223.50 (+$86.50); backwardation $159.50, widest in series; stock -125 t to 226,725 t."},
 {"when":"Wed 11-Nov","impact":"Bearish","text":"DOLLAR: index ~102.94, highest since April 2025; ~91% odds of a Fed hike next month (Trading Economics)."},
 {"when":"Wed 11-Nov","impact":"Mixed","text":"US-CANADA: AL Circle discusses a possible deal cutting the US tariff on Canadian aluminium to 25% from 50% - reported, not confirmed."},
 {"when":"Thu 12-Nov","impact":"Bullish","text":"HORMUZ: still listed closed; vessels holding up to 42; VLCC strike and mine-strike reports (unconfirmed) (Straits Daily Brief)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM CASH JUMPS $86.50 AS BACKWARDATION HITS $159.50. The Wednesday 11-November official settled cash at $3,223.50 (+2.76%) and three-month at $3,064.00 (+1.22%), back above the 3,042 low of 03-November but $13.00 below 3,077; the cash premium widened to $159.50, the widest in the stored series, and visible stock fell 125 t to a new low of 226,725 t. Board: aluminium +1.22%, nickel +0.40%, zinc +0.32%, lead -0.11%, copper -0.25%. READ: spread and price moved together - the prompt squeeze is leading."},
 {"theme":"Supply","horizon":"0-12 months","impact":"Mixed","url":S_TE,
  "headline":"BRIEF TIGHTNESS VS CHINESE OVERSEAS BUILD (Trading Economics, 12-November): aluminium rebounded to about $3,050 after dipping below $3,000 on 10-November as brief supply tightness outweighed ample Chinese production; US-Iran tensions still restrict GCC output and LME inventories are about half pre-war levels. Offsetting: Chinese smelters, capped at 45 Mt/yr at home, are building over 15 Mt of capacity in Southeast Asia and Africa, with Indonesia leading."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"DOLLAR AT HIGHEST SINCE APRIL 2025 (Trading Economics, 12-November): the dollar index hovered near 102.94 after gaining more than 1% in two sessions on stronger October inflation and hawkish Fed commentary; markets price about 91% odds of a hike next month. READ: a firmer dollar weighs on dollar-priced metals and investor length."},
 {"theme":"Trade policy","horizon":"0-6 months","impact":"Mixed","url":S_CA,
  "headline":"POSSIBLE US-CANADA ALUMINIUM DEAL (AL Circle, 11-November): a possible agreement would cut the US tariff on Canadian aluminium to 25% from 50%, which could pull Canadian metal back to the US and leave European buyers competing harder; Canadian unwrought imports into six European markets rose from about 205 kt in 2024 to about 612 kt in 2025 (ITC Trade Map). Reported/proposed only - no official confirmation or effective date located."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL CLOSED, INCIDENT REPORTS RISE (Straits Daily Brief, 12-November): 3 transits on 08-November vs 85/day pre-crisis; AIS-visible vessels holding rose to 42. TradeWinds reports a strike on a Sinokor VLCC injured four seafarers; Iran's army says a tanker hit a mine (unconfirmed); an IRGC claim of an attack on navigation systems on Oman's Didamar island (Iranian state media, unverified). Trading Economics reports US-Iran talks deadlocked."},
 {"theme":"Inventory","horizon":"Structural","impact":"Bullish","url":S_LA,
  "headline":"LME STOCKS DOWN 52.6% IN NINE MONTHS (AL Circle, 11-November): LME aluminium stocks fell to 241,375 t by 30-September, with the Q3 monthly average down 43.6% year on year; the 11-November official shows 226,725 t."},
 {"theme":"Capacity","horizon":"Structural","impact":"Bearish","url":S_CY,
  "headline":"CENTURY'S OKLAHOMA SMELTER ADVANCES (AL Circle): Century Aluminum is preparing the next phase of its $4bn, 750,000 t/yr Inola, Oklahoma smelter, targeting production in 2030."},
 {"theme":"Bauxite","horizon":"0-12 months","impact":"Mixed","url":S_VB,
  "headline":"VEDANTA LEANS ON CAPTIVE BAUXITE (AL Circle, 11-November): Vedanta expects its Sijimali captive bauxite mine to start producing this fiscal year as a pricing dispute with OMCL threatens its cost advantage."},
]+d['news']
d['news']=d['news'][:20]

d['earnings'].insert(0,{"company":"Maaden (1211)","group":"Diversified miner incl. aluminium (Saudi Arabia)","period":"Q3-2026 (Jul-Sep 2026)","reported":"09 Nov 2026","reported_iso":"2026-11-09","sentiment":"Mixed",
 "headline":"Q3-2026: revenue $3.0bn, up 11% y/y; EBITDA $0.9bn, down 24%; net profit attributable $0.4bn (no y/y comparison given). Aluminium segment revenue $985m (+32%) and EBITDA $419m (more than doubled); phosphate EBITDA fell 83% to $135m on record sulfur costs; gold and growth metals EBITDA +71% to $403m.",
 "readthrough":"ALUMINIUM CARRIED THE QUARTER: the aluminium segment's EBITDA more than doubled on higher prices and premiums, while group EBITDA fell on phosphate cost pressure. Single public source (Arab News, citing the Tadawul statement); figures are rounded USD as reported and not converted.",
 "eps":"-","revenue_bn":"$3.0bn","yoy_pct":"+11% revenue, -24% EBITDA, aluminium EBITDA more than doubled","url":S_MA})

hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('EGA'):
        p['update']="REVIEWED 12-NOVEMBER: Trading Economics (12-November) still cites about a quarter of Al Taweelah's cells back online by late August and full recovery expected by Q1-2027, and says US-Iran tensions continue to restrict GCC output ("+S_TE+"); no newer EGA operational release located. "+p['update']; hit+=1
    elif p['name'].startswith('China operators'):
        p['update']="UPDATED 12-NOVEMBER (Trading Economics, 12-November): with domestic primary output capped at 45 Mt/yr, Chinese smelters are building over 15 Mt of capacity in Southeast Asia and Africa, Indonesia leading; China's exports remain strong despite a 30% export duty on primary metal ("+S_TE+"). No new dated SMM social-inventory print located this run. "+p['update']; hit+=1
    elif p['name'].startswith('US / Canada'):
        p['update']="UPDATED 12-NOVEMBER: AL Circle (11-November) discusses a POSSIBLE US-Canada agreement that would cut the US tariff on Canadian aluminium to 25% from 50% - reported/proposed, no official confirmation or effective date located; the 50% Section 232 rate is unchanged on this page ("+S_CA+"). "+p['update']; hit+=1
assert hit==3

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 11-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 11-Nov)",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_LA,S_LA],[L_CA,S_CA],[L_CY,S_CY],[L_VB,S_VB],[L_MA,S_MA]): d['sources'].append(x)
for x in ([L_TE,S_TE],[L_TD,S_TD],[L_ST,S_ST],[L_CA,S_CA]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-11-10'
ph['rows'][-1]=['2026-11-11',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2),d['metals_board'])
