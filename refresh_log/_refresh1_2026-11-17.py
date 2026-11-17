# Daily data refresh - 2026-11-17 (TUESDAY, ~02:35 UTC, before today's ring). Board ROLLED ONE SESSION to the MONDAY 16-Nov LME official.
# Westmetall cache-busted EN + DE overviews agree on 16-Nov (Al cash 3,332.00 / 3M 3,020.00 / stock 221,900; MTLE 1.10140);
# Al per-metal table newest row 16-Nov and its 09-13 Nov rows match the stored series. Cash +181.50 -> backwardation $312.00 (from $132.50).
# 3M 3,020 still below 3,024.50 and above 2,994.50: weights unchanged 10/45/45, EW no re-label.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-17'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-17"; L_ST="Straits Daily Brief - Strait of Hormuz, 17-Nov-2026 (Brent figure AI-assisted)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,995 (-0.48%) on 16-Nov-2026, a year-to-date low (CFD reference)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$91.3 (-1.2%) on supply-glut expectations (17-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.6, highest in nearly 20 months; ~92% odds of a 25bp December Fed hike (17-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 84.6/MWh, below EUR 90; EU storage 70.6% vs 89% five-year average (17-Nov-2026)"
S_BRC="https://www.brecorder.com/news/40448599/lme-aluminium-backwardation-hits-36-year-high-as-stocks-shrink"; L_BRC="Business Recorder (Reuters) - LME aluminium backwardation hits 36-year high ($176.80/t traded, 12-Nov-2026); one entity holds 30-39% of warrants"
S_NA="https://www.alcircle.com/news/nalco-evaluates-sites-for-500kt-aluminium-smelter-in-india-121976"; L_NA="AL Circle - NALCO evaluates sites for a 500 kt greenfield smelter; Angul +500 kt expansion targeted Dec-2030 (16-Nov-2026)"
S_HU="https://www.alcircle.com/news/pakistan-explores-300-000-tonne-aluminium-smelter-through-hubco-subsidiary-121975"; L_HU="AL Circle - HUBCO commissions feasibility study for a 300 kt/yr smelter in Pakistan (16-Nov-2026)"
S_EG="https://alcircle.com/news/ega-allocates-400-million-to-restore-al-taweelah-smelter-production-121967"; L_EG="AL Circle - EGA allocates $400m to restore Al Taweelah; restoration 61% complete, full production Q1-2027 (16-Nov-2026)"

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3150.5 and B['LME 3-month']['cur']==3018.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3150.5,3018.0,224150
cash,m3,stk=3332.0,3020.0,221900
spr=cash-m3; psp=pc-pm; assert spr==312.0 and psp==132.5 and ps-2250==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED TUESDAY 17-NOVEMBER-2026 ABOUT 02:35 LONDON, BEFORE TODAY'S RING. THE BOARD IS THE MONDAY 16-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION AND THE CORRECT FIGURE UNTIL TODAY'S OFFICIAL PRINTS AT 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 16-November official for all metals with stocks and FX (EUR/USD MTLE 1.10140; 13-November 1.10510); (2) the aluminium per-metal daily table shows 16-November as its newest row and its 09-13 November rows match the stored series exactly. "
 "The whole board sits on ONE UNIFORM SESSION (16-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" MONDAY 16-NOVEMBER (the board): CASH SETTLED $3,332.00, UP $181.50 OR 5.76% FROM $3,150.50 - by far the largest one-session cash move in this series. THREE-MONTH SETTLED $3,020.00, UP ONLY $2.00 OR 0.07% FROM $3,018.00 - still $4.50 BELOW the 3,024.50 bear trigger, $25.50 above the 2,994.50 October low and $9.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION MORE THAN DOUBLED TO $312.00 FROM $132.50 - the widest in this dashboard's series and far beyond the $176.80 traded spread that Reuters (12-November) called the steepest since November 1990. The move is almost entirely in CASH: nearby metal is being bid for immediate delivery while forward pricing barely moved. A twenty-third straight backwardation and the twelfth above $15.00. "
 "VISIBLE LME STOCK FELL 2,250 t TO 221,900 t, another new series low and a nineteenth straight draw - a second consecutive draw above 2,000 t. Reuters reports one entity holds 30-39% of LME aluminium warrants and that available stock is almost exclusively Russian metal. The Trading Economics aluminium reference showed about $2,995 (-0.48%) for 16-November, a year-to-date low - a CFD reference cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,332.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,020.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $57.00 BELOW THE 3,077 WEEKLY 50% RETRACEMENT and $41.50 below the 3,061.5 July low, $128.50 beneath the 3,148.5 wave (iv) high and $269.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a twenty-second session, $25.50 below."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+312.0","pos":True,"delta":VER+f" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,332.00 against three-month $3,020.00 is a $312.00 BACKWARDATION, MORE THAN DOUBLE 13-November's $132.50, as cash rose $181.50 and three-month only $2.00 - spread and flat price moved in the SAME direction on Monday (both up), but the spread move dwarfs the price move. It stays far above the published $15.00 reversal condition for a twelfth session and is a twenty-third straight backwardation; a contango beyond $24.50 would reverse the structural signal. Reuters (12-November) described a $176.80 traded spread as the steepest since November 1990. The October mean spread was ${oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"221,900","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 2,250 t TO 221,900 t (13-November: -2,200 t to 224,150 t), another new series low, a nineteenth straight draw and the second consecutive draw above 2,000 t. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 13-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $3,020.00, UP $2.00 FROM THE 13-NOVEMBER $3,018.00 - a second settled close below the 3,024.50 bear trigger (by $4.50) and $57.00 below 3,077; $25.50 above the 2,994.50 October low; $9.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 2,250 t TO 221,900 t, another new series low (13-November 224,150 t). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $312.00 BACKWARDATION, MORE THAN DOUBLE 13-NOVEMBER'S $132.50 and the widest in this series (previous series high $159.50 on 11-November). CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On Monday cash rose $181.50 and three-month $2.00, so the tightening is concentrated at the prompt. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50 and $312.00."},
 {"name":"EUR/USD LME fixing","cur":1.1014,"prev":1.1051,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.10140 ON 16-NOVEMBER FROM 1.10510 ON 13-NOVEMBER as the dollar index held near its highest in nearly 20 months. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (16-Nov official)","price":"3,332.0","basis":"THE MONDAY 16-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,332.00, UP $181.50 OR 5.76% (13-November $3,150.50). Next official Tuesday 17-November 13:20 London."},
 {"tenor":"3-month (16-Nov official)","price":"3,020.0","basis":"THE 16-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $3,020.00, UP $2.00 - $4.50 BELOW the 3,024.50 bear trigger, $57.00 below 3,077 and $25.50 above the 2,994.50 October low."},
 {"tenor":"Cash-to-3M structure","price":"+312.0 (BACKWARDATION)","basis":"A $312.00 BACKWARDATION, more than double $132.50 - the widest in this series; the whole move is in cash."},
 {"tenor":"Visible LME stock","price":"221,900 t","basis":f"DOWN 2,250 t to a new series low on 16-November (nineteenth straight draw); October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("A PROMPT SQUEEZE, NOT A FORWARD RALLY. On the 16-November official cash $3,332.00 sits $312.00 ABOVE three-month $3,020.00, a BACKWARDATION more than double the $132.50 of 13-November, as cash jumped $181.50 and three-month rose only $2.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50 and now $312.00. "
 f"READ: a twenty-third straight backwardation with visible stock down to another low (221,900 t), warrant concentration reported at 30-39% in one holder and available stock almost exclusively Russian (Reuters, 12-November) - nearby deliverable metal is scarce for many buyers. The forward price is unmoved and the Trading Economics reference hit a year-to-date low, so the market is pricing acute prompt scarcity alongside a looser 2027. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2900,3450] and d['chart_stock_axis']==[200000,255000]
d['chart_stock_axis']=[190000,255000]   # re-bracketed ahead of the floor: stock 221,900 and drawing ~2,200 t/session

ls=d['lme_series']; assert ls[-1][0]=='13-Nov'
d['lme_series']=ls[1:]+[["16-Nov",cash,m3,stk]]
assert len(d['lme_series'])==15 and all(190000<r[3]<255000 and 2900<r[2]<3450 and 2900<r[1]<3450 for r in d['lme_series'])
CU=(13375.0,13305.0,327475); NI=(15805.0,16000.0,272682); ZN=(3848.0,3715.0,141275); PB=(1856.0,1886.0,279325)
CU6=(13610.0,13545.0,329100); NI6=(16025.0,16230.0,272724); ZN6=(3745.0,3705.0,142625); PB6=(1853.0,1886.0,283350)
assert CU6[2]-1625==CU[2] and NI6[2]-42==NI[2] and ZN6[2]-1350==ZN[2] and PB6[2]-4025==PB[2]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU6[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI6[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN6[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB6[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU6[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI6[1],1)
zn10=[3935.0,3869.0,3875.0,3877.0,3759.0,3754.0,3768.0,3794.0,3760.5,3745.0]; pb10=[1869.5,1862.0,1858.0,1866.5,1857.0,1854.0,1846.0,1845.0,1843.0,1853.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zn10)+ZN[0])/11)/(sum(zn10)/10),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(pb10)+PB[0])/11)/(sum(pb10)/10),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU6[0]),('NI',NI[0],NI6[0]),('ZN',ZN[0],ZN6[0]),('PB',PB[0],PB6[0])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-11-16'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending MONDAY 16-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 26-October dropped, 16-November appended, so the window is 27-October to 16-November. Every point is an official cash settlement from the Westmetall per-metal tables and English/German overviews (16-November read from both overviews, which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (16-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return "unchanged" if a==b else f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,f" COPPER 16-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU6[0])}; three-month ${CU[1]:,.2f}, {chg(CU[1],CU6[1])}. BACKWARDATION $70.00 from $65.00. Stock fell 1,625 t to 327,475 t."),
 ("Nickel",NI,f" NICKEL 16-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI6[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI6[1])}. CONTANGO $195.00 from $205.00, still the widest carry on the board. Stock fell 42 t to 272,682 t."),
 ("Zinc",ZN,f" ZINC 16-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN6[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN6[1])}. BACKWARDATION jumped to $133.00 from $40.00 - a prompt squeeze similar in shape to aluminium's. Stock fell 1,350 t to 141,275 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,f" LEAD 16-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB6[0])}; three-month ${PB[1]:,.2f}, unchanged. CONTANGO $30.00 from $33.00. Stock fell 4,025 t to 279,325 t, the largest draw on the board."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Monday 16-November official three-month nickel fell 1.42%, copper 1.77%, while zinc rose 0.27%, aluminium 0.07% and lead was unchanged; aluminium and zinc both saw cash jump far more than three-month. Trading Economics reports the dollar index near 103.6, its highest in nearly 20 months, with about 92% odds of a 25bp Fed hike in December; Brent about $91.3. The LME euro fixing fell to 1.1014.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='13-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["16-Nov",CU[0]]]; assert len(i['hist'])==15
        i['val']="~13,305.00 (3M); 13,375.00 (cash) $/t"; i['ratio']="~13,375.00 $/t cash vs LME 3M 13,305.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the MONDAY 16-NOVEMBER-2026 session at $13,375.00 (13-November $13,610.00). THE WINDOW ROLLED THIS RUN: 26-October dropped and 16-November appended, so the series is the last fifteen published official cash sessions, 27-October to 16-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English/German overviews. "
                  "Copper structure for context: backwardation $70.00 on 16-November; stock 327,475 t (-1,625 t).")
assert [r for r in d['inputs'] if r['name'].startswith('Copper')][0]['hist'][-1]==["16-Nov",13375.0]
s=d['inputs_summary']
d['inputs_summary']=("UPDATE 17-NOVEMBER: Copper rolled one session to the Monday 16-November LME official cash of $13,375.00 (window 27-October to 16-November). No new carbon, fluoride, silicon or magnesium mark was located this run, so those series are unchanged (gaps stay gaps). Energy eased: Brent about $91.3 on supply-glut expectations and European gas about EUR 84.6/MWh, back below EUR 90, though EU storage is 70.6% against an 89% five-year average (Trading Economics, 17-November). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
ptl=0.5*pc; presid=2403-ptl; pshare=ptl/2403*100
OT=f"the tariff leg of the US duty-paid premium is 0.50 times the 13-November official cash of $3,150.50, or ${ptl:,.2f}, DOWN $2.50 against the 12-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${presid:,.2f}, so {pshare:.1f}%"
NT=f"the tariff leg of the US duty-paid premium is 0.50 times the 16-November official cash of $3,332.00, or ${tl:,.2f}, UP ${tl-ptl:,.2f} against the 13-November figure used previously (the cash squeeze lifts the tariff leg). Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OC1="COMPILED MONDAY 16-NOVEMBER-2026 WITH THE MARKET SHUT (LME BOARD ON THE FRIDAY 13-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; NEXT OFFICIAL MONDAY 16-NOVEMBER 13:20 LONDON)."
NC1="COMPILED TUESDAY 17-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE MONDAY 16-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; TUESDAY'S OFFICIAL PRINTS 13:20 LONDON)."
for p in d['premiums']:
    assert OT in p['src'] and OC1 in p['src'],p['name']
    p['src']=p['src'].replace(OT,NT).replace(OC1,NC1)
ra=398.24/m3*100; pra=398.24/pm*100
OR=f"THE RATIO: LME Alumina at $398.24/t against the 13-November aluminium three-month of $3,018.00 is {pra:.2f}%"
for a in d['alumina']:
    assert OR in a['src'] and OC1 in a['src'],a['name']
    a['src']=a['src'].replace(OR,f"THE RATIO: LME Alumina at $398.24/t against the 16-November aluminium three-month of $3,020.00 is {ra:.2f}%").replace(OC1,NC1)
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 16-NOVEMBER: no newer public disclosure","REVIEWED 17-NOVEMBER: no newer public disclosure").replace("REVIEWED 16-NOVEMBER. NO NEW DATED","REVIEWED 17-NOVEMBER. NO NEW DATED")
    return o
for k in ('producer_status','inputs','logistics','raw_materials','premiums','alumina'):
    if k in d: d[k]=walk(d[k])
for k in ('premiums','alumina'): assert "13-November official cash of $3,150.50" not in json.dumps(d[k]), k

d['lme_commentary']=("CASH SQUEEZE: THE BACKWARDATION MORE THAN DOUBLES TO $312. The Monday 16-November official lifted cash $181.50 (+5.76%) to $3,332.00 while three-month rose only $2.00 to $3,020.00, so the cash-to-three-month backwardation jumped to $312.00 from $132.50 - the widest in this series and well beyond the $176.80 traded spread Reuters called the steepest since November 1990 (12-November). Visible stock fell 2,250 t to a new low of 221,900 t, a second consecutive draw above 2,000 t. "
 "Reuters reports one entity holds 30-39% of LME aluminium warrants and that available stock is almost exclusively Russian metal, so deliverable metal is scarce for many buyers; zinc's backwardation also jumped (to $133 from $40). "
 "The forward price did not follow: three-month stayed $4.50 below the 3,024.50 bear trigger and the Trading Economics reference fell to a year-to-date low near $2,995 on expectations of improving 2027 supply, with the dollar index near 103.6 and about 92% odds of a December Fed hike. Scenario weights hold at 10/45/45. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" its October mean.")
d['net_read']=("NET: NEUTRAL-TO-BEARISH ON THE FORWARD, ACUTELY TIGHT ON THE PROMPT. Against: three-month at $3,020.00 is below the 3,024.50 bear trigger and $57.00 under 3,077; a dollar near its highest in nearly 20 months with a December Fed hike about 92% priced; a growing 2027-31 ex-China capacity pipeline (Hindalco, NALCO, HUBCO study) and Gulf metal returning through Q1-2027 (EGA). "
 "Supportive: a $312.00 backwardation (twenty-third straight), visible LME stock at a new low of 221,900 t with concentrated warrant holdings, and Hormuz still closed with UKMTO logging two tanker attacks.")
d['bottom_line']=("BOTTOM LINE: the Monday 16-November official lifted LME aluminium cash $181.50 to $3,332.00 while three-month rose just $2.00 to $3,020.00, more than doubling the backwardation to $312.00 - the widest in this series - and taking visible stock down 2,250 t to a new low of 221,900 t. This is a prompt squeeze on scarce deliverable metal, not a forward rally. "
 "Weights stay 10% bull / 45% base / 45% bear. A settled close back above 3,042 returns five points to bull; a settled close below 2,994.50 ends the Elliott base count and adds bear weight; a contango beyond $24.50 would confirm the bear case structurally. Daily Elliott invalidation 3,289. Next official Tuesday 17-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, PROMPT PREMIUM WIDENS AS THE FORWARD BREAKS LOWER:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, PROMPT PREMIUM EXPLODES WHILE THE FORWARD STALLS: a $312.00 backwardation on 16-November, more than double $132.50, as cash rose $181.50 and three-month only $2.00 - nearby metal is valued far above forward metal, so there is a heavy cost to needing prompt LME metal and no carry reward for holding stock; the outright three-month price settled $4.50 BELOW the 3,024.50 bear trigger. "+c2[a1:]
o=f"is ${ptl:,.2f} on 13-November cash, {pshare:.1f}% of the $2,403/t premium"; assert o in c2; c2=c2.replace(o,f"is ${tl:,.2f} on 16-November cash, {share:.1f}% of the $2,403/t premium")
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find(" Hindalco's",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 16-November official held three-month at $3,020.00, below the 3,024.50 bear trigger and $25.50 above the 2,994.50 settled low, while cash jumped to $3,332.00; the dollar index near 103.6 with about 92% odds of a 25bp Fed hike in December (Trading Economics 17-November); Brent about $91.3 and European gas about EUR 84.6/MWh; EGA has allocated $400m to restore Al Taweelah, 61% complete, full production targeted Q1-2027 (AL Circle 16-November); NALCO is evaluating sites for a 500 kt greenfield smelter and HUBCO has commissioned a 300 kt Pakistan smelter feasibility study (AL Circle 16-November); a possible US-Canada deal cutting the US tariff on Canadian aluminium to 25% remains unconfirmed; Maaden (1211) reported Q3-2026 aluminium EBITDA of $419m (Arab News 09-November);"+c2[b1:]
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 17-NOVEMBER AT 10/45/45: the 16-November official settled three-month at $3,020.00, still $4.50 below 3,024.50, and neither 3,042 (returns five points to bull) nor 2,994.50 (adds bear weight) was touched. The $312.00 backwardation is a prompt-availability signal and does not by itself move the forward-price weights. ")+s['drivers']
    assert s['prob']=={'Bull':'10%','Base':'45%','Bear':'45%'}[s['case']]
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 17-NOVEMBER: the 16-November official printed a $312.00 BACKWARDATION, more than double $132.50, as cash jumped $181.50 - a twelfth session above $15.00 and the widest in this series. Contango risk is remote near term. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 17-NOVEMBER: LME stock fell 2,250 t on 16-November to a new low of 221,900 t, the second consecutive draw above 2,000 t (13-November -2,200 t) - the faster pace flagged last run is now confirmed, alongside reported 30-39% warrant concentration in one holder (Reuters, 12-November). Trend RAISED from FLAT to UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 17-NOVEMBER: Brent fell to about $91.3 (Straits brief $92.13, -3.5% over 24 hours) on IEA surplus projections and Saudi/UAE official selling price cuts; European gas slipped below EUR 90 to about EUR 84.6/MWh although EU storage is only 70.6% (Trading Economics). Energy support for the cost floor is easing. Trend CUT from FLAT to DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 17-NOVEMBER: Straits Daily Brief - strait listed CLOSED; latest lagged count still 3 transits on 08-November (vs 85/day pre-crisis); 38 AIS-visible vessels holding. UKMTO has logged two separate tanker attacks, one vessel disabled (per gCaptain and Anadolu); other mine/attack and drone-seizure reports remain unconfirmed claims. Iran's army says the strait reopens only on acceptance of Iran's conditions. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 17-NOVEMBER: the dollar index held near 103.6, its highest in nearly 20 months; markets price about 92% odds of a 25bp hike (8% for 50bp) at the December meeting and about four more hikes by September 2027 (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
assert hit==5,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Mon 16-Nov':
        hc+=1; cat['date']='Daily, from Tue 17-Nov'
        cat['event']=("MONDAY 16-NOVEMBER OFFICIAL: three-month $3,020.00 (+$2.00), cash $3,332.00 (+$181.50), backwardation $312.00 - widest in this series; weights held 10/45/45. NEXT (from Tuesday 17-November, official 13:20 London): whether the cash squeeze persists or unwinds into the November prompt date; a settled close back above 3,042 returns five points to bull; below 2,994.50 ends the Elliott base count and adds bear weight; below about 2,977.5 forces a re-count toward 2,894. Invalidation 3,289. Fed meeting in December (hike about 92% priced); any official US-Canada tariff announcement; first Q1-2027 Japanese premium offers.")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"TUESDAY 17-NOVEMBER ON THE MONDAY 16-NOVEMBER OFFICIAL: cash jumped $181.50 to $3,332.00 while three-month rose only $2.00 to $3,020.00, so the backwardation more than doubled to $312.00 - the widest in this series and well beyond the $176.80 traded spread Reuters called a 36-year extreme on 12-November - and visible stock fell 2,250 t to a new low of 221,900 t. Reuters reports one entity holds 30-39% of warrants and available stock is almost all Russian metal, so this is a squeeze on deliverable prompt metal. The forward is not following: three-month stays below the 3,024.50 bear trigger and the Trading Economics reference hit a year-to-date low near $2,995 on expectations of 2027 supply growth (NALCO 500 kt site search, HUBCO 300 kt study, EGA full Al Taweelah restart in Q1-2027). Weights unchanged at 10/45/45.")

pre16="REVIEWED 16-NOVEMBER (BEFORE MONDAY'S RING, NO NEW SESSION): the count is unchanged because there has been no official since Friday's 3,018.00. Trading Economics' Friday CFD reference traded down to 2,983 intraday - beneath the 2,994.50 October low - before closing about 3,009; that is NOT a settled official, so no pivot is added or re-labelled and no invalidation level is touched, but it raises the odds that today's official tests 2,994.50. "
EWP=("REVIEWED 17-NOVEMBER ON THE 16-NOVEMBER OFFICIAL: three-month settled 3,020.00 (+2.00), still BELOW 3,024.50, so the alternate (the rebound from 2,994.50 to 3,097.50 was a completed corrective bounce, 3,064 a lower high, and a new leg down toward and below 2,994.50 is under way) stays at about 65% against about 35% for the base (a deep wave (ii) of C/3 that must hold 2,994.50). No pivot is added and nothing is re-labelled: 2,994.50 held on a settled basis even though the Trading Economics CFD reference printed a year-to-date low near 2,980-2,995. The $312 cash backwardation is a prompt-structure signal outside the three-month wave count. A settled close below 2,994.50 ends the base count; below about 2,977.5 forces a re-count toward the 2,894 weekly 61.8%. A recovery above 3,042 restores the 60/40 balance and above 3,097.50 the base toward 3,110 and 3,148.5. Invalidation 3,289; confidence low. ")
EWL=("REVIEWED 17-NOVEMBER (NEW WEEK): the week opened on the Monday official at 3,020.00, barely changed from Friday's 3,018.00 and below the 3,061.5 July low and the 3,077 50% retracement - the weekly base case, the corrective count toward the 61.8% retracement at 2,894, stays preferred and loses preference only on a weekly close above 3,110. Alternate (2,994.50 completed the correction) held at about 25%: the record prompt squeeze and record-low stock argue for it, but three-month has not confirmed. Confidence moderate. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith(pre16),k
    d['ew'][k]['writeup']=pfx+w[len(pre16):]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="91.3",day="about $91.30 on 17-November (-1.23%, Trading Economics; the page's stats section shows 91.70); Straits Daily Brief $92.13 (-3.52% over 24 hours)",
 note="REFRESHED TUESDAY 17-NOVEMBER-2026 (Trading Economics): Brent fell on expectations of stronger global supply - the IEA projects a surplus of about 2 mb/d this quarter, Goldman Sachs warned of a possible glut next year, and Saudi Arabia and the UAE cut official selling prices - outweighing Middle East tensions. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="84.6",day="about EUR 84.6-84.75/MWh on 17-November (Trading Economics; sections differ), below EUR 90 after Monday's fall",
 note="REFRESHED TUESDAY 17-NOVEMBER-2026 (Trading Economics): prices fell below EUR 90/MWh on Monday, extending Friday's losses, as investors weighed colder forecasts against low inventories; EU storage 70.6% against a five-year seasonal average of 89%, Germany 57%; Norwegian outages persist. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="103.60",day="about 103.60 on 17-November (+0.01%, Trading Economics); 103.4 on 16-November was the highest in nearly 20 months",
 note="REFRESHED TUESDAY 17-NOVEMBER-2026 (Trading Economics): markets price about 92% odds of a 25bp Fed hike at the December meeting (8% for 50bp) and about four more hikes by September 2027 after firm core inflation; French fiscal concerns weigh on the euro. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.10140',day="LME fixing on 16-November, down from 1.10510 on 13-November",note="REFRESHED TUESDAY 17-NOVEMBER-2026 to the 16-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE MONDAY 16-NOVEMBER-2026 LME OFFICIAL, the latest published session. THIS TUESDAY 17-NOVEMBER RUN IS COMPILED AT ABOUT 02:35 LONDON, BEFORE TODAY'S RING (today's official prints at 13:20 London). The board rolled ONE session this run (from Friday 13-November). The Trading Economics aluminium reference (about $2,995, -0.48% for 16-November, a year-to-date low) is a CFD reference cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (17-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 16-November session (aluminium cash 3,332.00, three-month 3,020.00, stock 221,900; EUR/USD MTLE 1.10140); the aluminium per-metal daily table shows 16-November as its newest row. Because the cash move (+$181.50) is exceptional, it was checked in all three pages; all agree.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 09-13 November rows match the stored series exactly; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 16-November values come from both overviews, which agree, and each metal's stock change reconciles with its 13-November stock.")
C[3]=("STOCK CHANGES 16-November (also shown in the pages' change column): aluminium -2,250 to 221,900; copper -1,625 to 327,475; nickel -42 to 272,682; zinc -1,350 to 141,275; lead -4,025 to 279,325.")
c4=C[4]; k=c4.find("The price chart ax"); assert k>0
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (16-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (eleven sessions, 02-16 November) as their latest point. ")+c4[k:]
o4="brackets cash 3,150.50 and three-month 3,018.00; the stock chart axis floor of 200,000 t leaves about 24,150 t headroom below visible stock of 224,150 t"
assert o4 in C[4]
C[4]=C[4].replace(o4,"brackets cash 3,332.00 and three-month 3,020.00; the stock chart axis floor was LOWERED THIS RUN from 200,000 t to 190,000 t, ahead of need, because visible stock of 221,900 t is drawing about 2,200 t per session (31,900 t headroom now)")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,332.00 against three-month $3,020.00 is therefore a $312.00 BACKWARDATION, more than double $132.50 on 13-November. On Monday spread and flat price moved in the SAME direction (cash up sharply, three-month up $2.00). Press figures for the spread differ by measure and time (Reuters $176.80 traded on 12-November; a Reuters column cited about $275 on Monday); the dashboard uses the settled officials only."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        o=f"the tariff leg is 0.50 times the 13-November official cash of $3,150.50, or ${ptl:,.2f}, leaving a ${presid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({pshare:.1f}% policy arithmetic)"
        assert o in cv,cv[:600]
        C[i]=cv.replace(o,f"the tariff leg is 0.50 times the 16-November official cash of $3,332.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic; the cash squeeze inflates the tariff leg)"); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $91.3), the dollar index (about 103.6) and TTF (about EUR 84.6/MWh) are Trading Economics readings for 17-November (early, pre-European session); Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages again showed different levels in different sections (Brent 91.30 vs 91.70; TTF 84.60 vs 84.75; dollar 103.597 vs 103.612), so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (17-November) shows Brent $92.13 (AI-assisted); its incident items are flagged as claims or unconfirmed except the UKMTO-logged attacks."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 17-NOVEMBER (TUESDAY, PRE-RING): no authorised fetch was blocked. Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/TTF/dollar, AL Circle news, news.metal.com and the Straits Daily Brief were fetched. news.metal.com's front page carried no aluminium print this run, so no SMM input mark is appended. A mining.com copy of the Reuters backwardation story returned 403; the Business Recorder copy of the same Reuters story was fetched and is cited instead. A Reuters column (via mining.com.au) citing about $275/t cash premium on Monday returned no article text and is mentioned only as a press figure, not used as data. A search for Q1-2027 Japanese premium offers again found none (S&P Global's $190-200/t is participant expectation, not an offer), so Q1 stays unpriced."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        rest=cv.split("EARLIER:",1)[-1].strip()
        C[i]=("PEER EARNINGS: NO NEW LISTED-PEER RESULT AND NO earnings_history BACK-FILL THIS RUN (17-NOVEMBER); EGA's $400m restoration budget and $5bn debt (AL Circle 16-November) are reported in news only. EARLIER: "+rest); hit+=1
assert hit==4,hit

d['so_what']={"line":"LME aluminium cash jumped $181.50 to $3,332 on Monday's official while three-month barely moved at $3,020, more than doubling the backwardation to a series-wide $312 as LME stock fell to a new low of 221,900 t: a squeeze on scarce prompt metal, while the forward price stays below the bear trigger.",
 "points":[
 "WHAT MOVED: the Monday 16-November official lifted cash 5.76% to $3,332.00 and three-month only 0.07% to $3,020.00, so the backwardation (cash above three-month) widened to $312.00 from $132.50; visible LME stock fell 2,250 t to 221,900 t, the second straight draw above 2,000 t.",
 "WHY: deliverable LME metal is scarce - Reuters reports one entity holds 30-39% of warrants and available stock is almost all Russian-origin, which many buyers avoid. Zinc showed a similar, smaller squeeze (backwardation $133 from $40).",
 "WHY THE FORWARD IS WEAK: a dollar near a 20-month high with about 92% odds of a December Fed hike, and a growing 2027-31 supply pipeline (EGA full Al Taweelah restart in Q1-2027, NALCO 500 kt site search, HUBCO 300 kt study). Brent eased to about $91 and EU gas below EUR 90.",
 "WHAT TO WATCH: whether the cash squeeze persists into the November prompt date or unwinds; a settled three-month close below $2,994.50 (bearish break) or above $3,042 (reverses the bear shift); Hormuz - still closed, UKMTO logging two tanker attacks."]}

d['feed']=([
 {"when":"Mon 16-Nov","impact":"Bullish","text":"16-NOVEMBER OFFICIAL: cash $3,332.00 (+$181.50); three-month $3,020.00 (+$2.00); backwardation more than doubles to $312.00; stock -2,250 t to 221,900 t."},
 {"when":"Mon 16-Nov","impact":"Mixed","text":"EGA: $400m to restore Al Taweelah, 61% complete, full production Q1-2027; debt $5bn (AL Circle)."},
 {"when":"Mon 16-Nov","impact":"Bearish","text":"INDIA: NALCO evaluating sites for a 500 kt greenfield smelter; Angul +500 kt targeted December 2030 (AL Circle)."},
 {"when":"Mon 16-Nov","impact":"Bearish","text":"PAKISTAN: HUBCO commissions feasibility study for a 300 kt/yr smelter - not an investment decision (AL Circle)."},
 {"when":"Tue 17-Nov","impact":"Bullish","text":"HORMUZ: still closed; UKMTO logs two tanker attacks; Iran says reopening only on its conditions (Straits brief)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM CASH SQUEEZE: BACKWARDATION MORE THAN DOUBLES TO $312. The Monday 16-November official lifted cash $181.50 (+5.76%) to $3,332.00 while three-month rose only $2.00 to $3,020.00; visible stock fell 2,250 t to a new low of 221,900 t. Board three-month moves: zinc +0.27%, aluminium +0.07%, lead unchanged, nickel -1.42%, copper -1.77%; zinc's backwardation also jumped to $133."},
 {"theme":"LME","horizon":"0-1 month","impact":"Bullish","url":S_BRC,
  "headline":"WARRANT CONCENTRATION AND RUSSIAN-ONLY STOCK BEHIND THE SQUEEZE (Reuters via Business Recorder, 12-November): the cash-to-three-month spread traded at a $176.80 backwardation, the steepest since November 1990; one entity holds 30-39% of LME aluminium warrants and available stock is almost exclusively Russian metal - 'the LME aluminium price is effectively the price of the Russian metal now' (Wood Mackenzie)."},
 {"theme":"LME","horizon":"0-3 months","impact":"Bearish","url":S_TE,
  "headline":"FORWARD PRICE AT A YEAR-TO-DATE LOW (Trading Economics, 16-November): the aluminium reference fell to about $2,995 (-0.48%), with UK futures near $2,980, on expectations of improving global supply - record-track Chinese output and new overseas smelting capacity pointing to a 2027 surplus."},
 {"theme":"Supply","horizon":"0-6 months","impact":"Bearish","url":S_EG,
  "headline":"EGA BUDGETS $400M TO RESTORE AL TAWEELAH (AL Circle, 16-November): restoration of the smelter damaged on 28-March is 61% complete with full production expected in Q1-2027; EGA's debt rose to $5bn at end-September from $3.5bn a year earlier; the recycling plant fully restarts in H2-2027."},
 {"theme":"Supply","horizon":"36-60 months","impact":"Bearish","url":S_NA,
  "headline":"NALCO EVALUATES SITES FOR A 500 KT GREENFIELD SMELTER (AL Circle, 16-November): alongside the 500 kt Angul expansion (to about 960 kt, about INR 30,000 crore, EGA technology, mechanical completion targeted December 2030) and a Damanjodi fifth stream lifting alumina capacity to 3.1 Mt/yr."},
 {"theme":"Supply","horizon":"Structural","impact":"Mixed","url":S_HU,
  "headline":"PAKISTAN'S HUBCO STUDIES A 300 KT/YR SMELTER (AL Circle, 16-November): a wholly owned subsidiary commissioned a bankable feasibility study by an unnamed Chinese design institute; construction depends on the study, approvals and financing - an initial step, not an investment decision."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL CLOSED; UKMTO LOGS TWO TANKER ATTACKS (Straits Daily Brief, 17-November): latest lagged count 3 transits on 08-November vs 85/day pre-crisis; 38 AIS-visible vessels holding. UKMTO has logged two separate tanker attacks, one vessel disabled (per gCaptain and Anadolu); a mine-strike fire and an IRGC drone-seizure claim are unconfirmed. Iran's army says the strait reopens only on acceptance of Iran's conditions."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bearish (cost)","url":S_BR,
  "headline":"ENERGY EASES (Trading Economics, 17-November): Brent about $91.3 (-1.2%) on IEA surplus projections and Saudi/UAE price cuts; European gas fell below EUR 90 to about EUR 84.6/MWh despite EU storage of only 70.6% against an 89% five-year average."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])

hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('EGA'):
        p['update']=("UPDATED 17-NOVEMBER: AL Circle (16-November) reports EGA allocating $400m to restore Al Taweelah, damaged 28-March; restoration 61% complete and full production expected in Q1-2027; debt $5bn at end-September; recycling plant full restart H2-2027. ")+p['update']
        p['src']=[L_EG,S_EG]; hit+=1
    elif p['name'].startswith('US / Canada'):
        p['update']="REVIEWED 17-NOVEMBER: still no official confirmation of the reported US-Canada deal; 50% Section 232 rate unchanged. "+p['update']; hit+=1
assert hit==2,hit

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 16-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 16-Nov)",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_BRC,S_BRC],[L_NA,S_NA],[L_HU,S_HU],[L_EG,S_EG]): d['sources'].append(x)
for x in ([L_BRC,S_BRC],[L_TE,S_TE],[L_EG,S_EG],[L_ST,S_ST]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-13',3150.5,3018.0,224150]
ph['rows'].append(['2026-11-16',cash,m3,stk]); ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2),d['metals_board'])
