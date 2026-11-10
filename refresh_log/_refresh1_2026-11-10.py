# Daily data refresh - 2026-11-10 (TUESDAY, ~02:35 UTC). Board ROLLED ONE SESSION to the MONDAY 09-Nov LME official.
# Westmetall cache-busted EN + DE overviews agree on 09-Nov (Al cash 3,147 / 3M 3,059.50 / stock 226,975; MTLE 1.11920);
# aluminium per-metal table newest row 09-Nov and its 03-06 Nov rows match the stored series.
# 3M 3,059.50: not above 3,077 and not below 3,024.50 -> weights unchanged 15/45/40.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-10'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-10"; L_ST="Straits Daily Brief - Strait of Hormuz, 10-Nov-2026 (ticker AI-assisted)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum 3,073.65 (+0.26%) on 09-Nov-2026 (CFD reference)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$92, fell almost 6% on 09-Nov to lowest since late August (10-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~101.7, -0.4% on 09-Nov; December-hike odds ~80% (10-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 81.6/MWh, lowest since 09-Oct; EU storage 72.65% (10-Nov-2026)"
S_HN="https://www.arthneeti.com/announcements/hindalco-industries-ltd-announcement-under-regulation-30-lodr-press-release-media-release-06-nov-2026"; L_HN="Hindalco Q2 FY27 media release (Reg-30 filing, 06-Nov-2026) via Arthneeti: revenue RS 91,708cr (+39%), PAT RS 7,533cr (+59%), Aluminium Upstream EBITDA RS 7,009cr (+55%)"
S_HN2="https://www.kotakneo.com/news/stocks/hindalco-q2-fy-27-results-shares-in-focus/"; L_HN2="Kotak Neo - Hindalco Q2 FY27: PAT RS 7,533cr vs RS 4,741cr; revenue RS 91,708cr vs RS 66,058cr"
S_WS="https://www.alcircle.com/news/alcoas-8b-south32-deal-puts-worsley-alumina-workers-pay-and-conditions-to-the-fore-121893"; L_WS="AL Circle - Alcoa-South32 deal puts Worsley alumina workers' pay in focus (09-Nov-2026)"
S_MM="https://www.alcircle.com/news/metro-mining-ships-752-000-tonnes-of-bauxite-in-october-as-operations-recover-121892"; L_MM="AL Circle - Metro Mining ships 752,000 t of bauxite in October (09-Nov-2026)"
S_GU="https://www.alcircle.com/news/china-aluminum-international-proposes-988m-epc-contract-for-guinea-alumina-project-121890"; L_GU="AL Circle - China Aluminum International proposes $988m EPC contract for Guinea alumina project (09-Nov-2026)"
S_MC="https://www.alcircle.com/news/molson-coors-faces-30m-midwest-premium-hit-as-q3-results-disappoint-121899"; L_MC="AL Circle - Molson Coors faces $30m Midwest premium hit (Nov-2026)"
S_CA="https://www.metal.com/en/newscontent/IQ36NQA72ALH7DMFD24JYVGJL4ADLM3GO2XLDMY-us-midterm-results-spark-hope-for-canadian-aluminum-tariff-relief-amid-persistent-trade-costs"; L_CA="SMM - US midterm results spark hope for Canadian aluminium tariff relief; 50% Section 232 still in place (Nov-2026)"

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3117.0 and B['LME 3-month']['cur']==3050.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3117.0,3050.0,227600
cash,m3,stk=3147.0,3059.5,226975
spr=cash-m3; psp=pc-pm; assert spr==87.5 and psp==67.0 and ps-625==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED TUESDAY 10-NOVEMBER-2026 ABOUT 02:35 LONDON, BEFORE TUESDAY'S RING, SO THE BOARD IS THE MONDAY 09-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION (TUESDAY'S PRINTS 13:20 LONDON). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 09-November official for all metals with stocks and FX (EUR/USD MTLE 1.11920; 06-November 1.11690); (2) the aluminium per-metal daily table shows 09-November as its newest row and its 03 to 06-November rows match the stored series exactly. "
 "The whole board sits on ONE UNIFORM SESSION (09-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" MONDAY 09-NOVEMBER (the board): CASH SETTLED $3,147.00, UP $30.00 OR 0.96% FROM $3,117.00. THREE-MONTH SETTLED $3,059.50, UP $9.50 OR 0.31% FROM $3,050.00 - $17.50 below 3,077, $2.00 below the 3,061.5 July low, $17.50 above the 3,042.00 low of 03-November and $35.00 above the 3,024.50 bear-trigger level; $49.00 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION WIDENED TO $87.50 FROM $67.00 - cash rose more than three times as much as three-month, so spread and flat price moved in the SAME direction (both firmer) - an eighteenth straight backwardation, the seventh above $15.00 and the widest since at least mid-September. "
 "VISIBLE LME STOCK FELL 625 t TO 226,975 t, another new series low and a fourteenth straight draw. The Trading Economics aluminium reference showed $3,073.65 (+0.26%) for 09-November - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,147.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,059.5","pos":True,"delta":VER+AL+" THREE-MONTH IS $17.50 BELOW THE 3,077 WEEKLY 50% RETRACEMENT and $2.00 below the 3,061.5 July low, $89.00 beneath the 3,148.5 wave (iv) high and $229.50 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a seventeenth session."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+87.5","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,147.00 against three-month $3,059.50 is an $87.50 BACKWARDATION, WIDER than 06-November's $67.00 as cash rose $30.00 and three-month only $9.50 - spread and price moved in the SAME direction. It stays above the published $15.00 reversal condition for a seventh session, an eighteenth straight backwardation and the widest print in the stored series; a contango beyond $24.50 would reverse the structural signal. The October mean spread was $"+f"{oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"226,975","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 625 t TO 226,975 t (06-November: -875 t to 227,600 t), another new series low and a fourteenth straight draw. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 06-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $3,059.50, UP $9.50 FROM THE 06-NOVEMBER $3,050.00 - $17.50 below 3,077, $2.00 below 3,061.5 and $35.00 above 3,024.50; $49.00 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 625 t TO 226,975 t, another new series low (06-November 227,600 t). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" AN $87.50 BACKWARDATION, WIDER THAN 06-NOVEMBER'S $67.00 (05-November $62.50). CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On Monday cash rose $30.00 and three-month $9.50, so structure and price FIRMED TOGETHER. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00 and $87.50."},
 {"name":"EUR/USD LME fixing","cur":1.1192,"prev":1.1169,"avg":1.1465,"note":VER+" THE LME EURO FIXING ROSE TO 1.11920 ON 09-NOVEMBER FROM 1.11690 ON 06-NOVEMBER as the dollar gave back part of Friday's payrolls rally. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (09-Nov official)","price":"3,147.0","basis":"THE MONDAY 09-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,147.00, UP $30.00 OR 0.96% (06-November $3,117.00). Next official Tuesday 10-November 13:20 London."},
 {"tenor":"3-month (09-Nov official)","price":"3,059.5","basis":"THE 09-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $3,059.50, UP $9.50 - $17.50 below 3,077, $2.00 below 3,061.5, $35.00 above 3,024.50 and $65.00 above the 2,994.50 October low."},
 {"tenor":"Cash-to-3M structure","price":"+87.5 (BACKWARDATION)","basis":"An $87.50 BACKWARDATION, wider than $67.00 with price firmer (same direction) - above the $15.00 reversal condition for a seventh session."},
 {"tenor":"Visible LME stock","price":"226,975 t","basis":f"DOWN 625 t to a new series low on 09-November (fourteenth straight draw); October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PROMPT TIGHTNESS STEPS UP AGAIN. On the 09-November official cash $3,147.00 sits $87.50 ABOVE three-month $3,059.50, a BACKWARDATION, wider than $67.00 on 06-November as cash rose $30.00 and three-month only $9.50 - spread and flat price moved in the SAME direction on Monday, after moving in opposite directions on Friday. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00 and now $87.50. "
 f"READ: an eighteenth straight backwardation, the seventh above $15.00, with visible stock at another low (226,975 t) - nearby LME metal is clearly tight while the outright three-month price holds in a $3,040-3,100 range, capped by falling energy and a firm dollar. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2900,3450] and d['chart_stock_axis']==[200000,255000]

ls=d['lme_series']; assert ls[-1][0]=='06-Nov'
d['lme_series']=ls[1:]+[["09-Nov",cash,m3,stk]]
assert len(d['lme_series'])==15 and all(200000<r[3]<255000 and 2900<r[2]<3450 and 2900<r[1]<3450 for r in d['lme_series'])
# (cash, m3, stock) 09-Nov and 06-Nov
CU=(14030.0,13855.0,317400); NI=(16190.0,16400.0,271662); ZN=(3754.0,3724.0,146375); PB=(1854.0,1889.0,300300)
CU6=(13955.0,13780.0,316675); NI6=(16095.0,16280.0,271968); ZN6=(3759.0,3735.0,146875); PB6=(1857.0,1887.0,304000)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU6[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI6[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN6[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB6[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU6[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI6[1],1)
zn5=[3935.0,3869.0,3875.0,3877.0,3759.0]; pb5=[1869.5,1862.0,1858.0,1866.5,1857.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zn5)+ZN[0])/6)/(sum(zn5)/5),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(pb5)+PB[0])/6)/(sum(pb5)/5),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU6[0]),('NI',NI[0],NI6[0]),('ZN',ZN[0],ZN6[0]),('PB',PB[0],PB6[0])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-11-09'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending MONDAY 09-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 19-October dropped, 09-November appended, so the window is 20-October to 09-November. Every point is an official cash settlement from the Westmetall per-metal tables and English/German overviews (09-November read from both overviews, which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (09-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,CU6,f" COPPER 09-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU6[0])}; three-month ${CU[1]:,.2f}, {chg(CU[1],CU6[1])}. BACKWARDATION unchanged at $175.00. Stock rose 725 t to 317,400 t."),
 ("Nickel",NI,NI6,f" NICKEL 09-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI6[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI6[1])} - the strongest metal on Monday's board. CONTANGO widened to $210.00 from $185.00, still the widest carry on the board. Stock fell 306 t to 271,662 t."),
 ("Zinc",ZN,ZN6,f" ZINC 09-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN6[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN6[1])}. BACKWARDATION widened to $30.00 from $24.00 while price eased (opposite directions). Stock fell 500 t to 146,375 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,PB6,f" LEAD 09-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB6[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB6[1])}. CONTANGO $35.00 from $30.00. Stock fell 3,700 t to 300,300 t."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Monday 09-November official three-month nickel rose 0.74%, copper 0.54%, aluminium 0.31% and lead 0.11%; zinc eased 0.29%. Copper alone built stock. Trading Economics reports the dollar index fell about 0.4% to near 101.8 on Monday, giving back part of Friday's payrolls rally, while Brent fell almost 6% to its lowest since late August on diplomatic efforts to end the Middle East conflict. The LME euro fixing rose to 1.1192.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,c6,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='06-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["09-Nov",CU[0]]]; assert len(i['hist'])==15
        i['val']="~13,855.00 (3M); 14,030.00 (cash) $/t"; i['ratio']="~14,030.00 $/t cash vs LME 3M 13,855.00 $/t"; i['trend']='up'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the MONDAY 09-NOVEMBER-2026 session at $14,030.00 (06-November $13,955.00). THE WINDOW ROLLED THIS RUN: 19-October dropped and 09-November appended, so the series is the last fifteen published official cash sessions, 20-October to 09-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall copper table and English/German overviews. "
                  "Copper structure for context: backwardation $175.00 on 09-November; stock 317,400 t (+725 t).")
s=d['inputs_summary']; assert s.startswith("UPDATE 07-NOVEMBER")
d['inputs_summary']=("UPDATE 10-NOVEMBER: Copper rolled one session to the Monday 09-November LME official cash of $14,030.00, its fifteen-session window now 20-October to 09-November. No new monthly carbon settlement (due mid-November) or dated SMM fluoride, silicon or magnesium mark was located, so no other hist mark was appended. Energy fell again: Brent near $92 after an almost 6% drop on Monday to its lowest since late August; European gas near EUR 81.6/MWh, its lowest since 09-October, with EU storage 72.65% against a 90% five-year norm (Trading Economics, 10-November). Upstream: Metro Mining shipped 752,000 t of bauxite in October (AL Circle, 09-November). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OT="the tariff leg of the US duty-paid premium is 0.50 times the 06-November official cash of $3,117.00, or $1,558.50, DOWN $9.00 against the 04-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of $844.50, so 64.9%"
NT=f"the tariff leg of the US duty-paid premium is 0.50 times the 09-November official cash of $3,147.00, or ${tl:,.2f}, UP $15.00 against the 06-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OC1="COMPILED MONDAY 09-NOVEMBER-2026 BEFORE THE RING (LME BOARD CARRIED ON THE FRIDAY 06-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; MONDAY'S OFFICIAL PRINTS 13:20 LONDON)."
NC1="COMPILED TUESDAY 10-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE MONDAY 09-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; TUESDAY'S OFFICIAL PRINTS 13:20 LONDON)."
n=0
for p in d['premiums']:
    assert OT in p['src'] and OC1 in p['src'],p['name']
    p['src']=p['src'].replace(OT,NT).replace(OC1,NC1); n+=1
ra=398.24/m3*100
OR="THE RATIO: LME Alumina at $398.24/t against the 06-November aluminium three-month of $3,050.00 is 13.06%"
for a in d['alumina']:
    assert OR in a['src'],a['name']
    a['src']=a['src'].replace(OR,f"THE RATIO: LME Alumina at $398.24/t against the 09-November aluminium three-month of $3,059.50 is {ra:.2f}%").replace(OC1,NC1)
OC0="COMPILED MONDAY 09-NOVEMBER-2026 ABOUT 02:40 LONDON, BEFORE MONDAY'S RING (THE OFFICIAL PRINTS 13:20 LONDON), SO THE LATEST PUBLISHED LME OFFICIAL IS STILL FRIDAY 06-NOVEMBER-2026 AND THE BOARD IS CARRIED ON IT."
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace(OC1,NC1).replace(OC0,"COMPILED TUESDAY 10-NOVEMBER-2026 ABOUT 02:35 LONDON; THE BOARD IS THE MONDAY 09-NOVEMBER-2026 LME OFFICIAL.")
        o=o.replace("REVIEWED 09-NOVEMBER: no newer public disclosure","REVIEWED 10-NOVEMBER: no newer public disclosure").replace("REVIEWED 09-NOVEMBER. NO NEW DATED","REVIEWED 10-NOVEMBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status','inputs','logistics','raw_materials'):
    if k in d: d[k]=walk(d[k])

d['lme_commentary']=("CASH LEADS, THREE-MONTH LAGS. The Monday 09-November official lifted cash $30.00 to $3,147.00 but three-month only $9.50 to $3,059.50, so the backwardation widened to $87.50 - the widest in the stored series and an eighteenth straight backwardation - while visible stock fell another 625 t to a new low of 226,975 t. Spread and price moved in the SAME direction on Monday. "
 "Three-month remains inside the $3,042-3,097.50 range of the past week: $2.00 below 3,061.5, $17.50 below 3,077 and $35.00 above the 3,024.50 bear trigger, so no pre-registered rule fired and weights stay 15/45/40. "
 "The rest of the board firmed modestly (nickel +0.74%, copper +0.54%, lead +0.11%, zinc -0.29%) as the dollar index slipped about 0.4% to near 101.8, but Brent fell almost 6% to its lowest since late August on Middle East diplomacy (Trading Economics), which keeps lowering the smelter energy-cost floor. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" its October mean.")
d['net_read']=("NET: NEUTRAL - PRICE RANGE-BOUND, STRUCTURE TIGHTENING. Supportive: an $87.50 backwardation (eighteenth straight, seventh above $15.00, widest in the series), visible LME stock at a new low of 226,975 t, Chinese ingot social inventory still falling (372,500 t on 09-November, SMM) and record integrated-producer margins (Hindalco upstream EBITDA +55%). "
 "Against: three-month still below both 3,061.5 and 3,077; energy collapsing again (Brent near $92, European gas at a one-month low), which lowers the cost floor; December Fed-hike odds near 80%; ex-China restarts adding supply.")
d['bottom_line']=("BOTTOM LINE: LME aluminium three-month settled $3,059.50 on the Monday 09-November official, up $9.50, still inside the past week's $3,042-3,097.50 range, while cash rose $30.00 to $3,147.00 and the backwardation widened to $87.50 with visible stock at a new low of 226,975 t - prompt tightness keeps building ahead of outright price. "
 "Weights stay 15% bull / 45% base / 40% bear: no pre-registered rule fired. Re-crediting the bull needs a settled close above 3,077 with the backwardation beyond $15.00; a close below 3,024.50, or a contango beyond $24.50, adds bear weight. Daily Elliott invalidation 3,289. Next official Tuesday 10-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, PROMPT PREMIUM UP, PRICE DOWN:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, PROMPT PREMIUM UP AGAIN: an $87.50 backwardation on 09-November, wider than $67.00 as cash rose $30.00 and three-month $9.50 - a seventh print above the $15.00 reversal condition, so nearby metal is valued clearly over forward metal and there is no carry reward for deferring purchases; the outright three-month price sits $17.50 below 3,077. "+c2[a1:]
o="is $1,558.50 on 06-November cash, 64.9% of the $2,403/t premium"; assert o in c2; c2=c2.replace(o,f"is ${tl:,.2f} on 09-November cash, {share:.1f}% of the $2,403/t premium")
o="the 06-November official took three-month to $3,050.00 for the weekly close, below 3,061.5 and 3,077, $55.50 above the 2,994.50 settled low; energy fell further (Brent near $98 and down more than 12.5% on the week, European gas near EUR 85.6/MWh, Trading Economics 06-November); the dollar index rose to 102.28 after October payrolls of 165,000 beat forecasts; December-hike odds roughly 68-71%;"
assert o in c2
c2=c2.replace(o,"the 09-November official took three-month to $3,059.50, below 3,061.5 and 3,077, $65.00 above the 2,994.50 settled low; energy fell further (Brent near $92 after an almost 6% Monday drop to its lowest since late August, European gas near EUR 81.6/MWh, Trading Economics 10-November); the dollar index eased to about 101.7; December-hike odds about 80%; Hindalco's Q2 FY27 aluminium upstream EBITDA rose 55% to RS 7,009cr (06-November release);")
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 10-NOVEMBER at 15/45/40: the Monday 09-November official settled three-month at $3,059.50 - not above 3,077 (the bull trigger, with the backwardation beyond $15.00 now $87.50) and not below 3,024.50 (the bear trigger) - so no pre-registered rule fired. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 10-NOVEMBER: the 09-November official printed an $87.50 BACKWARDATION, a seventh session above $15.00 and the widest in the stored series. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 10-NOVEMBER: LME stock fell 625 t on 09-November to a new low of 226,975 t, a fourteenth straight draw. Trend held at FLAT: the pace remains modest."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 10-NOVEMBER: Brent fell almost 6% on 09-November to its lowest since late August, near $92 on 10-November; TTF near EUR 81.6/MWh, lowest since 09-October; EU storage 72.65% (Trading Economics). Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 10-NOVEMBER: Straits Daily Brief - strait still listed CLOSED; latest lagged transit count 1 vessel on 01-November vs 85/day; 99 AIS-visible vessels holding (down from 115). Reported, not verified: Washington has proposed a phased reopening and Secretary Rubio called Iran's demands 'outrageous' (Firstpost, AOL); US CENTCOM struck the stern of a blockade-runner (Hellenic Shipping News, single source); an Iranian state-media claim of a tanker mine fire remains UNCONFIRMED. Trading Economics reports US strikes on Qeshm Island and continued tanker targeting. Trend held at UP: no reopening has occurred."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 10-NOVEMBER: Trading Economics cites market-implied odds of a December 25bp hike around 80%; CPI and PPI due this week. Trend held at UP."; r['trend']='up'; hit+=1
assert hit==5,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Mon 09-Nov':
        hc+=1; cat['date']='Daily, from Tue 10-Nov'
        cat['event']=("MONDAY 09-NOVEMBER OFFICIAL: three-month $3,059.50 (+$9.50), cash $3,147.00, backwardation $87.50 - no rule fired; weights 15/45/40. NEXT: a settled close above 3,077 with the backwardation beyond $15.00 returns five points to bull; resistance 3,097.5 then 3,110 and the 3,148.5 wave (iv) high. A settled close below 3,042.00 weakens the daily base count; below 3,024.50 adds bear weight; below about 2,977.5 forces a re-count toward 2,894. Invalidation 3,289. US CPI and PPI this week.")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"TUESDAY 10-NOVEMBER ON THE MONDAY 09-NOVEMBER OFFICIAL: cash rose $30.00 to $3,147.00 and three-month $9.50 to $3,059.50, widening the backwardation to $87.50 - the widest in the stored series - as visible stock fell to a new low of 226,975 t. Three-month stays inside last week's $3,042-3,097.50 range, so weights are unchanged at 15/45/40. Energy is the main drag on the cost floor: Brent fell almost 6% on Monday to about $92, its lowest since late August, on Middle East diplomacy, and European gas is at a one-month low. Hindalco's Q2 FY27 (aluminium upstream EBITDA +55% y/y) confirms integrated producers are converting the price structure into record margins. Watch 3,077 above and 3,042 / 3,024.50 below, plus US CPI.")

EWP=("REVIEWED 10-NOVEMBER ON THE 09-NOVEMBER OFFICIAL: three-month settled 3,059.50 (+9.50), holding $17.50 above the 3,042.00 B/2 low and below the 3,097.50 high of 05-November; no pivot is added or re-labelled and no invalidation level is touched. The overlapping 3,042-3,097.50 range still fits either a developing (i)-(ii) of C/3 (base, about 50%) or a completed corrective bounce (alternate, about 50%); a settled close above 3,097.50 favours the base toward 3,110 then 3,148.5, a settled close below 3,042.00 the alternate. Invalidation 3,289; confidence low. ")
EWL=("REVIEWED 10-NOVEMBER: the week has opened at 3,059.50, just below the 3,061.5 July low and the 3,077 50% retracement; the weekly base case (corrective count toward the 61.8% retracement at 2,894) is unchanged and loses preference only on a weekly close above 3,110; the alternate (2,994.50 completed the correction, about 35%) is supported by the $87.50 backwardation and record-low stock. Confidence moderate. ")
pre="REVIEWED 09-NOVEMBER (PRE-RING, NO NEW SESSION SINCE FRIDAY): the count is unchanged because there has been no official since Friday's 3,050.00; no pivot is added or re-labelled and no invalidation level is touched; Monday's 13:20 official is the next input. "
for k,new in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith(pre); d['ew'][k]['writeup']=new+w[len(pre):]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="92.0",day="about $92.0 on 10-November (Trading Economics; quote 91.96 -0.65%, stats 92.12 -0.48%); fell almost 6% on 09-November to its lowest since late August",
 note="REFRESHED TUESDAY 10-NOVEMBER-2026 (Trading Economics): Brent extended losses as diplomatic efforts to end the Middle East conflict gained attention - President Trump cited 'momentum toward an end' after meeting Qatar's prime minister, while Secretary Rubio tempered expectations; US forces reportedly struck Iran's Qeshm Island again and tankers were still targeted in Hormuz. EIA, OPEC and IEA monthly reports due. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="81.6",day="about EUR 81.0-81.7/MWh on 10-November (Trading Economics; sections differ), about -1.0% to -1.8%, lowest since 09-October; down 17.7% the prior week",
 note="REFRESHED TUESDAY 10-NOVEMBER-2026 (Trading Economics): TTF fell on hopes of a diplomatic resolution; EU storage 72.65% (08-November) against a 90% five-year seasonal average, Germany below 60%; disrupted Middle East LNG keeps prices far above pre-war levels. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.69",day="about 101.69 on 10-November (Trading Economics, about flat); fell nearly 0.4% to about 101.8 on 09-November",
 note="REFRESHED TUESDAY 10-NOVEMBER-2026 (Trading Economics): the dollar gave back part of Friday's 0.7% payrolls rally as oil fell; markets await CPI and PPI; December 25bp-hike odds around 80%. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.11920',day="LME fixing on 09-November, up from 1.11690 on 06-November",note="REFRESHED TUESDAY 10-NOVEMBER-2026 to the 09-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE MONDAY 09-NOVEMBER-2026 LME OFFICIAL, the latest published session: this Tuesday 10-November run (about 02:35 London) precedes Tuesday's ring, whose official prints at 13:20 London and will be picked up by the next run. The board rolled ONE session this run (from Friday 06-November). The Trading Economics aluminium reference ($3,073.65, +0.26% for 09-November) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (10-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 09-November session (aluminium cash 3,147.00, three-month 3,059.50, stock 226,975; EUR/USD MTLE 1.11920); the aluminium per-metal daily table shows 09-November as its newest row.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 03 to 06-November rows match the stored series exactly; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 09-November values come from both overviews, which agree.")
C[3]=("STOCK CHANGES 09-November against the stored 06-November values: aluminium -625 to 226,975; copper +725 to 317,400; nickel -306 to 271,662; zinc -500 to 146,375; lead -3,700 to 300,300 (computed against the prior run's verified figures, not read from the pages' change column).")
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (09-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (six sessions, 02-09 November) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,059.50; the stock chart axis floor of 200,000 t leaves about 27,000 t headroom below visible stock of 226,975 t; it is re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,147.00 against three-month $3,059.50 is therefore an $87.50 BACKWARDATION, wider than $67.00 on 06-November - on Monday the spread and the flat price moved in the SAME direction (both firmer)."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        o="the tariff leg is 0.50 times the 06-November official cash of $3,117.00, or $1,558.50, leaving a $844.50 residual market leg out of the $2,403/t US duty-paid premium (64.9% policy arithmetic)"
        assert o in cv
        C[i]=cv.replace(o,f"the tariff leg is 0.50 times the 09-November official cash of $3,147.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic)").replace("(no change located this run;","(no change located this run - SMM reports the 50% Section 232 rate on Canadian metal remains in place after the US midterms;"); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $92.0), the dollar index (about 101.69) and TTF (about EUR 81.6/MWh) are Trading Economics readings for 10-November (Asian hours); Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages again showed different levels in different sections (Brent 91.96 vs 92.12; TTF 81.65 vs 80.99), so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (10-November) shows Brent about $92.48 (-5.30% over 24h); the brief labels its ticker as AI-assisted. EUR/USD is the 09-November LME fixing, the same session as the board."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 10-NOVEMBER: no authorised fetch was blocked (Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/TTF/dollar, AL Circle, news.metal.com and the Straits Daily Brief all fetched). One metal.com article link (Hindalco) returned HTTP 404, so Hindalco's figures were taken via web search from a summary of the company's Reg-30 media release (Arthneeti) cross-checked against Kotak Neo. news.metal.com showed no new SMM social-inventory print for 10-November, so the 09-November figure is carried. mining.com was not fetched. A search for Q1-2027 Japanese premium offers again found none - Q1 stays unpriced. Hormuz diplomacy and strike reports are cited as reported/UNCONFIRMED per the brief."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        C[i]=("PEER EARNINGS: ONE NEW PEER RESULT ADDED THIS RUN (10-NOVEMBER) - HINDALCO Q2 FY27 (company media release filed 06-November; revenue RS 91,708cr +39%, PAT RS 7,533cr +59%, Aluminium Upstream EBITDA RS 7,009cr +55%) - and its earnings_history strip was REFRESHED with the Q2 FY27 upstream EBITDA point, dropping Q2 FY26; consolidated EBITDA and margin were not in the public summary read, so they are not published. "+cv.split("PEER EARNINGS:",1)[1].replace("NO NEW PEER RESULT AND NO earnings_history BACK-FILL THIS RUN (09-NOVEMBER).","").strip()); hit+=1
assert hit==4,hit

d['so_what']={"line":"LME aluminium's cash premium over three-month jumped to $87.50 on Monday - the widest in the series - as cash rose $30 to $3,147 and LME stock hit another low, but three-month ($3,059.50) stays stuck below $3,077 while collapsing oil drags the cost floor lower.",
 "points":[
 "WHAT MOVED: the Monday 09-November official lifted cash $30.00 to $3,147.00 and three-month $9.50 to $3,059.50; the backwardation widened to $87.50 (from $67.00) and visible LME stock fell 625 t to 226,975 t, a fourteenth straight draw.",
 "WHY IT MATTERS: prompt metal keeps tightening (China's ingot social inventory was also down to 372,500 t on 09-November, SMM), yet the outright price is range-bound at $3,042-3,097.50 because energy is falling fast - Brent dropped almost 6% on Monday to about $92, its lowest since late August, on Middle East diplomacy, and European gas is at a one-month low (Trading Economics).",
 "PEERS: Hindalco's Q2 FY27 aluminium upstream EBITDA rose 55% to RS 7,009cr with PAT up 59% to RS 7,533cr - integrated producers are earning record margins at current prices.",
 "WHAT TO WATCH: a settled close above $3,077 (bull trigger) or below $3,024.50 (bear trigger); US CPI/PPI this week with December Fed-hike odds near 80%; Hormuz still closed despite reports of a US phased-reopening proposal (unverified); first Q1-2027 Japanese premium offers (none public yet)."]}

d['feed']=([
 {"when":"Mon 09-Nov","impact":"Bullish","text":"09-NOVEMBER OFFICIAL: cash $3,147.00 (+$30.00), three-month $3,059.50 (+$9.50); backwardation $87.50, widest in series; stock -625 t to 226,975 t."},
 {"when":"Mon 09-Nov","impact":"Bearish (cost)","text":"ENERGY: Brent -~6% to ~$92, lowest since late August; TTF ~EUR 81.6/MWh, lowest since 09-Oct (Trading Economics)."},
 {"when":"Fri 06-Nov","impact":"Bullish (margin)","text":"HINDALCO Q2 FY27: PAT RS 7,533cr (+59%), revenue RS 91,708cr (+39%), aluminium upstream EBITDA RS 7,009cr (+55%)."},
 {"when":"Tue 10-Nov","impact":"Mixed","text":"HORMUZ: still closed; 99 vessels holding; reports of a US phased-reopening proposal and a US strike on a blockade-runner (unverified)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM BACKWARDATION WIDENS TO $87.50. The Monday 09-November official settled cash at $3,147.00 (+0.96%) and three-month at $3,059.50 (+0.31%), widening the cash premium to the widest in the stored series; visible stock fell 625 t to a new low of 226,975 t. Board: nickel three-month +0.74%, copper +0.54%, aluminium +0.31%, lead +0.11%, zinc -0.29%. READ: prompt tightness builds while three-month stays below 3,077."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bearish (cost)","url":S_BR,
  "headline":"BRENT SLIDES TO A TEN-WEEK LOW (Trading Economics, 10-November): Brent fell almost 6% on Monday to its lowest since late August and traded near $92 on Tuesday as diplomatic efforts to end the Middle East conflict gained attention, though Secretary Rubio tempered expectations and tankers were still targeted in Hormuz. European gas fell to about EUR 81.6/MWh, its lowest since 09-October; EU storage 72.65%. READ: the smelter energy-cost floor keeps falling."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Bullish (margin)","url":S_HN,
  "headline":"HINDALCO Q2 FY27 RECORD (company media release, 06-November): revenue from operations RS 91,708cr (+39% y/y from RS 66,058cr), PAT RS 7,533cr (+59% from RS 4,741cr), Aluminium Upstream EBITDA RS 7,009cr (+55%), copper EBITDA RS 1,673cr (+164%). READ: integrated producers with captive alumina and power are converting 2026 prices into record margins."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Mixed","url":S_ST,
  "headline":"HORMUZ STILL CLOSED AS DIPLOMACY TALK BUILDS (Straits Daily Brief, 10-November): latest lagged transit count 1 vessel on 01-November vs 85/day; 99 AIS-visible vessels holding (from 115). Reported, not verified: Washington proposed a phased reopening and Secretary Rubio called Iran's demands 'outrageous' (Firstpost, AOL); US CENTCOM struck the stern of a blockade-runner (Hellenic Shipping News); an Iranian claim of a tanker mine fire is UNCONFIRMED."},
 {"theme":"Tariffs","horizon":"0-6 months","impact":"Mixed","url":S_CA,
  "headline":"US MIDTERMS RAISE HOPES OF CANADIAN TARIFF RELIEF (SMM): the 50% Section 232 tariff on Canadian aluminium remains in place; SMM cites a US Midwest premium of about US$1.12/lb on 04-November, down from a May-2026 record of US$1.19/lb. AL Circle reports Molson Coors took a $30m Midwest-premium hit in Q3."},
 {"theme":"Supply","horizon":"0-12 months","impact":"Mixed","url":S_MM,
  "headline":"BAUXITE AND ALUMINA PIPELINE (AL Circle, 09-November): Metro Mining shipped 752,000 t of bauxite in October as operations recovered; China Aluminum International proposed a $988m EPC contract for a Guinea alumina project; Alcoa's South32 deal puts Worsley alumina workers' pay and conditions in focus."},
]+d['news']
d['news']=d['news'][:20]

for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('Alcoa'):
        p['update']="UPDATED 10-NOVEMBER: AL Circle (09-November) reports the Alcoa-South32 deal has put Worsley alumina workers' pay and conditions in focus ("+S_WS+"); no CADE decision on Trimet's challenge located. "+p['update'].replace("REVIEWED 09-NOVEMBER: no CADE decision or Alcoa response to Trimet's filing located. ","")
    elif p['name'].startswith('EGA'):
        p['update']=p['update'].replace("REVIEWED 09-NOVEMBER: no newer EGA release located;","REVIEWED 10-NOVEMBER: no newer EGA operational release located (AL Circle 09-November covers only EGA's Dubai Future Week partnership);")
    elif p['name'].startswith('China operators'):
        p['update']="REVIEWED 10-NOVEMBER: no newer SMM social-inventory print located; last 372,500 t (09-November). China Aluminum International proposed a $988m EPC contract for a Guinea alumina project (AL Circle, 09-November). "+p['update']
    elif p['name'].startswith('US / Canada'):
        p['update']="UPDATED 10-NOVEMBER (SMM): the 50% Section 232 tariff on Canadian aluminium remains in place after the US midterms, which raised hopes of relief ("+S_CA+"). "+p['update']

d['earnings']=[
 {"company":"Hindalco Industries (HNDL)","group":"Aluminum producer (India)","period":"Q2 FY27 (Jul-Sep 2026)","reported":"06 Nov 2026","reported_iso":"2026-11-06","sentiment":"Positive",
  "headline":"Q2 FY27 RECORD: consolidated revenue from operations RS 91,708cr, up 39% y/y from RS 66,058cr and about 8% q/q; PAT RS 7,533cr, up 59% from RS 4,741cr and about 7% q/q (includes about RS 284cr one-time income per one report); Aluminium Upstream EBITDA RS 7,009cr, up 55% y/y (Q1 FY27 RS 7,390cr); copper EBITDA RS 1,673cr, up 164%.",
  "readthrough":"INTEGRATION KEEPS PAYING: upstream aluminium EBITDA rose 55% y/y on captive bauxite, alumina and power, though it eased about 5% from Q1's record as LME and premiums came off the summer peak. Consolidated EBITDA and margins were not in the public summary read, so they are not shown. Source: company media release (Reg-30 filing, 06-November) via Arthneeti; PAT and revenue cross-checked with Kotak Neo.",
  "eps":"-","revenue_bn":"RS 91,708cr","yoy_pct":"+39% revenue, +59% PAT, +55% upstream EBITDA","url":S_HN},
]+d['earnings']
d['earnings_note']=("HINDALCO REPORTED (added 10-November): Q2 FY27 revenue RS 91,708cr (+39%), PAT RS 7,533cr (+59%), Aluminium Upstream EBITDA RS 7,009cr (+55%) (media release, 06-November). ")+d['earnings_note']
EH=d['earnings_history']['HNDL']; assert EH['points'][-1]==['Q1 FY27',7390] and EH['points'][0]==['Q2 FY26',4524]
EH['points']=EH['points'][1:]+[['Q2 FY27',7009]]
EH['src']=["Hindalco / Aditya Birla Group quarterly results releases - India Aluminium Upstream segment EBITDA: Q3 FY26 RS 4,832cr, Q4 FY26 RS 5,448cr, Q1 FY27 RS 7,390cr (record), Q2 FY27 RS 7,009cr (+55% y/y on Q2 FY26's RS 4,524cr; media release 06-Nov-2026). REFRESHED 10-Nov-2026 with the Q2 FY27 print; the Q2 FY26 point was dropped to hold four quarters. Exact publicly reported figures only - no interpolation, no estimates.",S_HN]

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 09-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 09-Nov)",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_HN,S_HN],[L_HN2,S_HN2],[L_WS,S_WS],[L_MM,S_MM],[L_GU,S_GU],[L_MC,S_MC],[L_CA,S_CA]): d['sources'].append(x)
for x in ([L_BR,S_BR],[L_TD,S_TD],[L_ST,S_ST],[L_HN,S_HN]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-11-06'
ph['rows'].append(['2026-11-09',cash,m3,stk]); ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2),d['metals_board'])
