# Daily data refresh - 2026-10-15 (THURSDAY, compiled ~03:35 London). Board ROLLED to WEDNESDAY 14-Oct LME official.
# Westmetall cache-busted EN AND DE overviews BOTH fetched this run and agree on the full 14-Oct session (all six metals, stocks, FX).
# Completeness: 5/5 stock-change lines reconcile vs the verified 13-Oct board; prior-day FX column (MTLE 1.11880) matches 13-Oct board.
# Trading Economics aluminium / TTF / DXY / 10Y pages fetched; CPI, Brent, metals colour from fetched public reports.
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-15'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (14/15-Oct-2026)"
S_RA="https://rallies.ai/news/copper-falls-after-us-inflation-data-aluminium-hits-lowest-this-year-8c3d8c57f2526cfc"; L_RA="Rallies (XLB News) - Copper falls after US inflation data; aluminium hits lowest this year (14-Oct-2026)"
S_CX="https://www.cruxinvestor.com/posts/aluminum-prices-erase-war-premium-as-lme-stocks-hit-century-low"; L_CX="Crux Investor - Aluminum prices erase war premium as LME stocks hit century low (14-Oct-2026)"
S_SM="https://news.metal.com/newscontent/104157455-shfe-aluminum-falls-on-shrinking-volume-with-weakness-unchanged-alumina-inventory-buildup-worsens-supply-demand-looseness-smm-aluminum-brief"; L_SM="SMM - SHFE aluminum falls on shrinking volume; alumina inventory build-up [SMM aluminum brief] (14-Oct-2026)"
S_NT="https://nationthailand.com/news/world/40072291"; L_NT="Nation Thailand (Reuters) - Brent rises 0.35% on October 14 after Saudi Aramco attack (14-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (14/15-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (14/15-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (15-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
cash,prev_c,m3,prev_m,stk,prev_s=3010.0,3036.0,3013.5,3037.0,238375,238625
spr=cash-m3; pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100

VER=("COMPILED THURSDAY 15-OCTOBER-2026. THE BOARD IS THE WEDNESDAY 14-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION (Thursday's official prints at 13:20 London). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 14-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.11930); their prior-day FX column (MTLE 1.11880) matches the verified 13-October board; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 13-October: aluminium 238,625 less 250 to 238,375; copper 229,650 less 1,650 to 228,000; nickel 282,504 plus 150 to 282,654; zinc 138,400 plus 5,725 to 144,125; lead 341,825 less 1,750 to 340,075. "
 "The whole board sits on ONE UNIFORM SESSION (14-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(f" CASH SETTLED $3,010.00 ON THE 14-OCTOBER OFFICIAL, DOWN $26.00 OR {pc:.2f}% FROM $3,036.00. THREE-MONTH SETTLED $3,013.50, DOWN $23.50 OR {pm:.2f}% FROM $3,037.00 - a THIRD settled close beneath the 3,061.5 July low, now by $48.00, and only $3.00 above the first-published 2026 three-month official of $3,010.50, so aluminium has given back almost the entire year's gain. "
 "The contango WIDENED $2.50 to $3.50 from $1.00 as the flat price fell - spread and price moved in the SAME (bearish) direction this session. "
 "VISIBLE LME STOCK FELL 250 t TO 238,375 t, a new series low. Reported intraday, three-month touched about $2,978, the lowest since 31-December, after the hot US September CPI lifted the dollar (Rallies/XLB, Trading Economics).")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,010.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,013.5","pos":False,"delta":VER+AL+" THREE-MONTH IS $48.00 BENEATH THE 3,061.5 JULY LOW, $63.50 beneath the 3,077 weekly 50% retracement and $275.50 below the 3,289 daily invalidation. The rule-based cap on daily wave (v) near 2,977.5 was approached intraday (reported low about $2,978) but has NOT been broken on a settled basis."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-3.5","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,010.00 against three-month $3,013.50 is a $3.50 CONTANGO, WIDENED $2.50 from $1.00. Spread and flat price moved in the SAME direction this session (price down, contango wider). The reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET; the bearish structural confirmation, a contango beyond $24.50, is also unmet. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"238,375","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 250 t TO 238,375 t, a new series low; Crux Investor (14-October, citing LME data) describes registered stocks near 238,600 t as the lowest of the 21st century, with off-warrant stocks of 73,509 t the lowest since that category was first reported in 2020. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,013.50, DOWN $23.50 OR {pm:.2f}% FROM $3,037.00 - $48.00 beneath the 3,061.5 July low, a third settled close below it, and $3.00 above the 02-January three-month official. AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 250 t TO 238,375 t, a new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-1.0,"avg":sep_sp,"note":VER+f" A $3.50 CONTANGO, WIDENED $2.50 FROM $1.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in the SAME direction this session (three-month down, contango wider). REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1193,"prev":1.1188,"avg":1.1465,"note":VER+" THE LME EURO FIXING FIRMED TO 1.11930 FROM 1.11880 at the Wednesday ring; the ECB fixing printed 1.11950 and BFIX 1.11928. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (14-Oct official)","price":"3,010.0","basis":f"THE 14-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,010.00, DOWN $26.00 OR {pc:.2f}%. Next official Thursday 15-October 13:20 London."},
 {"tenor":"3-month (14-Oct official)","price":"3,013.5","basis":f"THE 14-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,013.50, DOWN $23.50 OR {pm:.2f}% - $48.00 beneath the 3,061.5 July low (third settled close below it), $3.00 above the 02-January official."},
 {"tenor":"Cash-to-3M structure","price":"-3.5 (CONTANGO)","basis":"A $3.50 CONTANGO, widened $2.50 from $1.00. Flat price and spread moved in the SAME direction."},
 {"tenor":"Visible LME stock","price":"238,375 t","basis":f"DOWN 250 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE CURVE STAYS NEAR FLAT WHILE THE FLAT PRICE BREAKS LOWER. On the 14-October official cash $3,010.00 sits $3.50 BELOW three-month $3,013.50, a CONTANGO widened $2.50 from $1.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and now $3.50. "
 f"READ: the forward is leading the fall while the prompt holds and visible stock sits at a new series low of 238,375 t - the slide is a macro (hot US CPI, firmer dollar) and supply-recovery repricing, not a prompt glut. The September mean spread was ${sep_sp:,.2f}. The reversal condition (a backwardation beyond $15.00) is unmet; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]

ls=d['lme_series']; assert ls[-1][0]=='13-Oct', ls[-1]
d['lme_series']=ls[1:]+[["14-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14751.0,14635.0,14741.0,14625.5); NI=(15475.0,15680.0,15445.0,15630.0); ZN=(3803.0,3749.0,3821.0,3756.0); PB=(1866.0,1906.0,1860.0,1895.5)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/10)/(sum(zs)/9),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/10)/(sum(ps)/9),1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])): R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-14'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending WEDNESDAY 14-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 23-September dropped and 14-October appended, so the window is 24-September to 14-October. Every point is an official cash settlement; the 14-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 13-October. Next official Thursday 15-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (14-October-2026 session; stock lines reconciled against 13-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,751.00, up $10.00 or 0.07%; three-month $14,635.00, up $9.50 or 0.06%. Backwardation $116.00 (from $115.50); stock DREW 1,650 tonnes to 228,000 - a seventh straight draw. Later in the day copper eased about 0.6% to $14,484.50 after touching $14,700, its highest since 23-September, as the hot US CPI lifted the dollar; a possible strike at BHP's Escondida was defused by a preliminary agreement and Codelco's El Teniente remains partly suspended after a fatal landslide (Rallies/XLB, 14-October)."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,475.00, up $30.00 or 0.19%; three-month $15,680.00, up $50.00 or 0.32%. CONTANGO widened to $205.00 from $185.00, still the widest carry on the board. Stock rose 150 tonnes to 282,654."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,803.00, down $18.00 or 0.47%; three-month $3,749.00, down $7.00 or 0.19%. BACKWARDATION NARROWED to $54.00 from $65.00 as another 5,725 tonnes were delivered in, lifting stock to 144,125 t - a third straight large inflow. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,866.00, up $6.00 or 0.32%; three-month $1,906.00, up $10.50 or 0.55%. CONTANGO widened to $40.00 from $35.50. Stock drew 1,750 tonnes to 340,075, an eighteenth consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Wednesday 14-October official lead three-month rose 0.55%, nickel 0.32% and copper 0.06%, zinc slipped 0.19% and aluminium fell most, 0.77%, to $3,013.50, a third settled close beneath its July low. The LME euro fixing firmed to 1.1193.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='13-Oct'
        i['hist']=i['hist'][1:]+[["14-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,635.00 (3M); 14,751.00 (cash) $/t"
        i['ratio']="~14,751.00 $/t cash vs LME 3M 14,635.00 $/t"
        i['trend']='flat'
        i['src']=("LME official cash settlement, rolled to the WEDNESDAY 14-OCTOBER-2026 session at $14,751.00, UP $10.00 or 0.07% against $14,741.00. THE WINDOW ROLLED THIS RUN: 23-September dropped and 14-October appended, so the series is the last fifteen published official cash sessions, 24-September to 14-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 13-October). "
                  "Copper structure for context: backwardation $116.00 (from $115.50), stock drew 1,650 t to 228,000 t.")
d['inputs_summary']=("UPDATE 15-OCTOBER: copper rolled to the Wednesday 14-October LME official cash of $14,751.00, up $10.00, with its fifteen-session window moved to 24-September to 14-October. No new SMM fluoride, silicon or magnesium weekly mark was located; India's NALCO extended its expression-of-interest deadline for aluminium fluoride, calcined petroleum coke and coal tar pitch supply to 30-October (SMM, context only, no price). The carbon settlement cycle (anodes, pitch, green coke) is due around 17-18 October - so every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 13-October official cash of \$3,036\.00, or \$1,518\.00, DOWN \$9\.50 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$885\.00, so 63\.2%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 14-October official cash of $3,010.00, or ${tl:,.2f}, DOWN $13.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
n=0
for p in d['premiums']:
    p['src'],k=OLDT.subn(NEWT,p['src']); n+=k
    p['src']=p['src'].replace("COMPILED WEDNESDAY 14-OCTOBER-2026 (LME BOARD ON THE 13-OCTOBER OFFICIAL).","COMPILED THURSDAY 15-OCTOBER-2026 (LME BOARD ON THE 14-OCTOBER OFFICIAL).")
print('premium tariff replaced',n); assert n==len(d['premiums'])
for a in d['alumina']:
    s=a['src'].replace("COMPILED WEDNESDAY 14-OCTOBER-2026 (LME BOARD ON THE 13-OCTOBER OFFICIAL).","COMPILED THURSDAY 15-OCTOBER-2026 (LME BOARD ON THE 14-OCTOBER OFFICIAL).")
    m=re.search(r"THE RATIO: LME Alumina at \$360\.40/t against the 13-October aluminium three-month of \$3,037\.00 is [0-9.]+%",s)
    if m: s=s.replace(m.group(0),f"THE RATIO: LME Alumina at $360.40/t against the 14-October aluminium three-month of $3,013.50 is {360.4/3013.5*100:.2f}%")
    a['src']=s

d['lme_commentary']=(f"ALUMINIUM SLID TO THE START-OF-YEAR LEVEL ON A HOT US CPI. On the Wednesday 14-October official cash settled $3,010.00, down $26.00, and three-month $3,013.50, down $23.50 or {abs(pm):.2f}% - $48.00 beneath the 3,061.5 July low and just $3.00 above the 02-January three-month official, erasing almost all of 2026's gain. "
 "Later in the session three-month was reported down 1.7% at $2,986.50 after touching about $2,978, the lowest since 31-December, on 'signs of emerging oversupply' (Rallies/XLB); Trading Economics cites a stronger dollar, faster-than-expected Gulf restarts (a quarter of EGA's Al Taweelah running again), Bell Bay secured to 2031 and surging Chinese alloy and semis exports. "
 "The contango widened $2.50 to $3.50 while visible stock slipped 250 t to a new series low of 238,375 t; off-warrant stock of 73,509 t is the lowest since 2020 (Crux Investor). SHFE aluminium fell 0.75% to RMB 23,285 and SMM reports a growing alumina surplus. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND IN CONTROL AND ACCELERATING ON MACRO. Against: three-month settled $3,013.50, a third close beneath 3,061.5 and now $48.00 below it, with intraday trade near $2,978; the hot US September CPI (3.7% headline) lifted the dollar to its strongest since April 2025 and revived Fed-hike odds; Gulf restarts, Indonesian growth and Chinese alloy/semis exports feed the supply-recovery narrative; Citi forecasts a 2027 surplus. "
 "Constructive: the curve is near flat ($3.50 contango) and visible and off-warrant LME stocks are at multi-year lows, so the prompt is tight; Hormuz attacks continue (two vessels struck, a container ship sunk by a mine) and European gas is near its highest since 2022, keeping smelter energy and freight costs high.")
d['bottom_line']=("BOTTOM LINE: aluminium settled on the Wednesday 14-October LME official at cash $3,010.00 and three-month $3,013.50 - a third settled close beneath the 3,061.5 July low (now by $48.00) and back at the level the year started. "
 "The contango widened to $3.50 and visible stock fell to a new low of 238,375 t, so the prompt is still not loosening. Scenario weights are held at 10% bull / 45% base / 45% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) has reached its 2,980-3,000 target zone intraday, with the rule-based cap near 2,977.5 and invalidation at 3,289; the weekly corrective count towards 2,894 stays preferred.")
c=d['commercial']
c=c.replace("FIRST, THE CURVE IS FLAT: a $1.00 contango on 13-October, narrowed from $5.00, so there is effectively no carry reward for waiting.","FIRST, THE CURVE IS NEAR FLAT: a $3.50 contango on 14-October, widened from $1.00, so there is little carry reward for waiting.")
c=c.replace("is $1,518.00 on 13-October cash, 63.2% of the $2,403/t premium",f"is ${tl:,.2f} on 14-October cash, {share:.1f}% of the $2,403/t premium")
c=c.replace("the 13-October official settled $24.50 beneath 3,061.5, so the 2,980-3,000 zone is now in play; US CPI on 14-October and Alcoa's results on 15-October;","the 14-October official settled $48.00 beneath 3,061.5 and intraday trade reached about 2,978, inside the 2,980-3,000 zone; the hot US CPI has put an October Fed hike in play; Alcoa's results on 15-October;")
assert c!=d['commercial']; d['commercial']=c

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 15-OCTOBER at 10/45/45: the 14-October official took three-month to $3,013.50, $48.00 beneath the July low, on a hot US CPI and supply-recovery headlines; the bear path's near-term 2,950-3,010 marks are being tested, but a flat curve and record-low visible stock argue against shifting further before Alcoa's results and the next Fed signals. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium has given back almost all of 2026's gain - three-month settled $3,013.50 on Wednesday after a hot US inflation print lifted the dollar and rate-hike bets - yet a near-flat curve and record-low LME stocks show physical metal is still tight even as the forward market prices in a supply recovery.",
 "points":[
 "WHAT MOVED: Wednesday's LME official settled cash at $3,010.00 (-$26.00) and three-month at $3,013.50 (-$23.50, -0.77%), $48 beneath the $3,061.5 July low and only $3 above where 2026 began; intraday it touched about $2,978, the lowest since 31-December. The contango widened to $3.50 and LME stock fell to a new low of 238,375 t.",
 "WHY: US September CPI came in hot (3.7% y/y headline, 2.6% core, both above forecasts), lifting the dollar to its strongest since April 2025, the US ten-year to about 5.3% and the odds of an October Fed hike to roughly 40-50%. The supply side adds pressure: faster Gulf restarts, Bell Bay secured to 2031, and Chinese alloy and semis exports surging.",
 "ENERGY AND LOGISTICS: two vessels were struck in the Strait of Hormuz and a container ship sank after hitting a mine; a Houthi strike hit an Aramco building in Dhahran. Brent settled $106.06 (+0.35%) and European gas holds near its highest since 2022 - keeping smelter cost floors and freight risk elevated.",
 "WHAT TO WATCH: Alcoa's Q3 results today (15-October, after the New York close); whether three-month settles beneath about $2,977.5, which would force a re-count of the daily wave structure; Fed commentary on an October hike; the mid-October carbon settlements around 17-18 October."]}

d['feed']=([
 {"when":"Thu 15-Oct","impact":"Bearish","text":f"BOARD ROLLED TO THE WEDNESDAY 14-OCTOBER LME OFFICIAL: cash $3,010.00 (-$26.00), three-month $3,013.50 (-$23.50, {pm:.2f}%) - a third settled close beneath the 3,061.5 July low - contango WIDENED to $3.50 from $1.00, stock down 250 t to 238,375 t."},
 {"when":"Wed 14-Oct","impact":"Bearish","text":"Aluminium fell 1.7% to $2,986.50 after touching $2,978, its lowest since 31-December, on 'signs of emerging oversupply'; copper eased 0.6% as the hot US CPI lifted the dollar (Rallies/XLB)."},
 {"when":"Wed 14-Oct","impact":"Bearish","text":"US September CPI rose 0.6% m/m and 3.7% y/y (core 2.6%), above forecasts; the US ten-year rose about 10bp to near 5.3% and October Fed-hike odds rose to about 50% (Trading Economics)."},
 {"when":"Wed 14-Oct","impact":"Bullish","text":"Brent settled $106.06 (+0.35%) after a Houthi strike on Aramco's Dhahran HQ and attacks on ships in Hormuz; a container ship sank south of the strait after hitting a mine (Reuters via Nation Thailand)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":f"LME ALUMINIUM BACK TO WHERE 2026 STARTED. The Wednesday 14-October official settled cash at $3,010.00 ({pc:.2f}%) and three-month at $3,013.50 ({pm:.2f}%), $48.00 beneath the 3,061.5 July low and $3.00 above the 02-January three-month official. The contango widened to $3.50 from $1.00 and visible stock fell 250 t to a new low of 238,375 t. Copper three-month edged up to $14,635.00 with stock drawing to 228,000 t; zinc stock rose another 5,725 t to 144,125 t."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Bearish","url":S_TY,
  "headline":"HOT US CPI REVIVES FED-HIKE BETS (Trading Economics, 14-October): US September CPI rose to 3.7% year on year (core 2.6%), both above forecasts, driven by energy. The ten-year yield rose about 10bp to roughly 5.3%, near its highest since 2002, and traders lifted the odds of another Fed hike this month to about 50% from roughly 22%; the dollar index rose as much as 0.7% to 102.88, its strongest since April 2025. A firmer dollar and higher carry costs weigh on dollar-priced metals."},
 {"theme":"Market","horizon":"Immediate","impact":"Bearish","url":S_RA,
  "headline":"ALUMINIUM HITS ITS LOWEST THIS YEAR (Rallies/XLB News, 14-October): three-month aluminium fell 1.7% to $2,986.50 after touching $2,978, its lowest since 31-December, on 'signs of emerging oversupply'. Copper fell 0.6% to $14,484.50 at 1600 GMT after reaching $14,700, its highest since 23-September, as the inflation data lifted the dollar; a possible strike at BHP's Escondida was defused by a preliminary agreement. Tin fell 3%."},
 {"theme":"Supply","horizon":"0-3 months","impact":"Bearish","url":S_TE,
  "headline":"WAR PREMIUM ERASED (Trading Economics, 14-October): aluminium's drop has erased the gains made since the Iran-US conflict began, on a stronger dollar and ample supply outside the Middle East. Gulf smelters restarted faster than expected - EGA reports a quarter of Al Taweelah running again - Rio Tinto agreed to keep Bell Bay operating through 2031, and Chinese alloy exports have doubled year on year despite the 30% duty on primary metal."},
 {"theme":"Inventory","horizon":"0-3 months","impact":"Bullish","url":S_CX,
  "headline":"RECORD-LOW STOCKS VS NO WAR PREMIUM (Crux Investor, 14-October): LME registered aluminium stocks of about 238,600 t are the lowest of the 21st century and off-warrant stocks of 73,509 t the lowest since that category began in 2020. Citing the IAI, Gulf output fell by an annualised 2.8 Mt between February and May and the August run-rate of 3.5 Mt/yr remains 2.6 Mt below pre-war; the article flags a rebuild of LME stocks above 300,000 t as the signal that the tightness has ended."},
 {"theme":"China","horizon":"0-1 month","impact":"Mixed","url":S_SM,
  "headline":"SHFE ALUMINIUM SLIPS, ALUMINA SURPLUS GROWS (SMM, 14-October): SHFE aluminium 2611 closed down 0.75% at RMB 23,285/t on shrinking volume, below all key moving averages; alumina 2701 fell 1.02% to RMB 2,626/t as national alumina inventory builds at an accelerating pace on new Guangxi capacity. Aluminium ingot stocks fell 50,000 t from the post-holiday peak to 636,000 t (15-October), offering some support; SMM expects range-bound trade."},
 {"theme":"Logistics","horizon":"0-3 months","impact":"Bullish","url":S_NT,
  "headline":"HORMUZ ATTACKS AND ARAMCO STRIKE LIFT OIL (Reuters via Nation Thailand, 14-October): Brent settled up 37 cents at $106.06 and WTI up 95 cents at $95.09, a three-week high. Two vessels were reported struck in the Strait of Hormuz, Iran's IRGC Navy said a container ship sank south of the strait after hitting a naval mine, and a Houthi attack hit an administrative building at Aramco's Dhahran headquarters. Gulf freight and war-risk costs stay elevated for metal flows."},
]+d['news'][:13]
d['news']=d['news'][:20]

cats=d['outlook']['catalysts']
for cat in cats:
    if cat['date']=='Daily, from Wed 14-Oct':
        cat['date']='Daily, from Thu 15-Oct'
        cat['event']="3,061.5 BROKEN ON THREE SETTLED OFFICIALS (NOW BY $48.00); 2,980-3,000 TARGET ZONE REACHED INTRADAY (reported low about 2,978). Three-month settled $3,013.50 on Wednesday 14-October. A settled close beneath about 2,977.5 would break the rule-based cap on daily wave (v) and force a re-count (extended fifth or larger correction toward the 2,894 weekly 61.8%); a settled recovery above 3,077 would signal wave (v) is complete; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289."
    elif cat['date']=='Wed 14-Oct':
        cat['date']='Resolved Wed 14-Oct'
        cat['event']="US SEPTEMBER CPI - RESOLVED HOT: headline 0.6% m/m and 3.7% y/y, core 2.6% y/y, both above forecasts (Trading Economics). The ten-year rose about 10bp to near 5.3%, the dollar index touched 102.88 (strongest since April 2025) and October Fed-hike odds rose to about 50%. Aluminium three-month settled $23.50 lower at $3,013.50 on the day."
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 15-OCTOBER: the contango WIDENED $2.50 to $3.50 on 14-October as three-month fell $23.50 - spread and price in the same direction; still far inside the $24.50 bearish-confirmation threshold. Trend held at FLAT."
RK[1]['risk']+=" UPDATE 15-OCTOBER: US September CPI printed hot (3.7% headline, 2.6% core); the ten-year rose about 10bp to near 5.3% and October Fed-hike odds rose to about 50% (Trading Economics). Trend held at UP, now confirmed by the data."
RK[4]['risk']+=" UPDATE 15-OCTOBER: LME stock fell 250 t to a new series low of 238,375 t on 14-October; off-warrant stock of 73,509 t is the lowest since 2020 (Crux Investor). Trend held at FLAT."
for r in RK:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 15-OCTOBER: two vessels reported struck in the strait on 14-October and a container ship sank south of it after hitting a naval mine (IRGC Navy statement, via Reuters/Nation Thailand). Trend held at UP."
d['outlook']['ai_analysis'].insert(0,"THURSDAY REVIEW, 15-OCTOBER: macro took over. The hot US September CPI (3.7% headline, 2.6% core) lifted the dollar to its strongest since April 2025 and Fed-hike odds to about 50%, and aluminium three-month settled $3,013.50 on Wednesday's official - $48.00 beneath the July low and back at the 02-January level - after trading near $2,978 intraday. Commentary now frames the year's war premium as fully erased, citing faster Gulf restarts, Bell Bay's extension and surging Chinese semis exports. The counterweight is physical: a near-flat curve ($3.50 contango) and visible and off-warrant LME stocks at multi-year lows. Weights held at 10/45/45 into Alcoa's results; a settled break below about 2,977.5 would be the next technical signal.")

EWS=("REVIEWED 15-OCTOBER ON THE WEDNESDAY 14-OCTOBER OFFICIAL: three-month settled $3,013.50, down $23.50, a third settled close beneath the 3,061.5 July low (now by $48.00); wave (v) of C has travelled $135.00 from the 3,148.5 wave (iv) high on a settled basis. Intraday trade reportedly touched about 2,978, inside the 2,980-3,000 target zone and within $0.50 of the rule-based cap near 2,977.5 (wave (v) must stay shorter than (iii)'s $171 so that (iii) is not the shortest) - so wave (v) is mature and may be completing. Base case about 70%: (v) terminates in 2,977.5-3,000, followed by a corrective rebound toward 3,061.5-3,077; alternate about 30%: a settled close beneath 2,977.5 forces a re-count toward the 2,894 weekly 61.8% level. Invalidation of the bearish count unchanged at 3,289; confidence moderate. ")
EWL=("REVIEWED 15-OCTOBER ON THE WEDNESDAY 14-OCTOBER OFFICIAL: three-month settled $3,013.50, a third close beneath the 3,061.5 July low and back inside the 2,950-3,110 zone's lower half; the weekly decline from 3,855 extends and the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label is needed. ")
d['ew']['short_term']['writeup']=EWS+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=EWL+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="106.06",day="+$0.37 (+0.35%) settle on 14-October; WTI +$0.95 to $95.09, a three-week high (Reuters via Nation Thailand)",
 note="REFRESHED THURSDAY 15-OCTOBER-2026: Brent settled $106.06 on 14-October after a Houthi attack on Aramco's Dhahran headquarters, ship attacks in the Strait of Hormuz and an API-reported 11.1m-barrel US crude draw. Energy is a major smelter cash-cost line. SOURCE: "+S_NT)
M['European gas TTF (EUR/MWh)'].update(value="86.8",day="about EUR 86.8/MWh quoted 15-October, -0.4%; page also cites a dip below EUR 86 on 14-October (Trading Economics; figures internally inconsistent, approximate)",
 note="REFRESHED THURSDAY 15-OCTOBER-2026 (Trading Economics): TTF near its highest since 2022 on Middle East LNG competition; EU storage about 74% full, below historical norms. Value approximate - the source page shows slightly different figures in different sections. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="102.0",day="rose as much as 0.7% to 102.88 on 14-October after hot CPI (strongest since April 2025); quoted about 102.0 early 15-October (Trading Economics)",
 note="REFRESHED THURSDAY 15-OCTOBER-2026 (Trading Economics): the dollar spiked on the hot US September CPI then retraced as Treasury yields gave back gains; the 15-October quote of about 102.0 is shown, with the 14-October intraday high of 102.88 in the day column. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="5.3",day="up about 10bp to roughly 5.3% on 14-October on hot CPI, near the highest since 2002; Trading Economics quotes 5.11% on 15-October (not reconciled by the source - treat as approximate)",
 note="REFRESHED THURSDAY 15-OCTOBER-2026 (Trading Economics). Higher yields raise the cost of carrying metal and financing inventory. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.11930',day="LME fixing on 14-October, +0.04% from 1.11880; ECB fixing 1.11950, BFIX 1.11928",
 note="REFRESHED THURSDAY 15-OCTOBER-2026 to the 14-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE WEDNESDAY 14-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION; Thursday's official prints at 13:20 London. Reference and intraday prices (Trading Economics, Rallies/XLB, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN: the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 14-October session, so the usual EN/DE agreement test passed.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.11880, ECB 1.11880, BFIX 1.11885) matches the 13-October board verified on 14-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 13-October: aluminium -250 to 238,375; copper -1,650 to 228,000; nickel +150 to 282,654; zinc +5,725 to 144,125; lead -1,750 to 340,075.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (14-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (ten sessions, 01- to 14-October) as their latest point. The price chart axis floor was LOWERED THIS RUN to 2,900 (from 2,950) so it brackets three-month at 3,013.50 with room below; the stock chart axis floor (225,000 t) brackets visible stock at 238,375 t.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,010.00 against three-month $3,013.50 is therefore a $3.50 CONTANGO, widened $2.50 from $1.00 on 13-October - spread and price moved in the SAME direction this session."
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (still described as 50% by Reuters-cited reporting on 14-October, Crux Investor), the tariff leg is 0.50 times the 14-October official cash of $3,010.00, or ${tl:,.2f}, leaving an ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). Note: Crux Investor (14-October) cites a Reuters US Midwest premium of $2,312/t from a different assessment; this page carries its own row at its own assessment date. This page does not fabricate freight, financing or tightness splits for any premium row."
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent ($106.06) is the 14-October settle; the dollar index (about 102.0) and TTF (about EUR 86.8/MWh) are early 15-October Trading Economics quotes, and the US ten-year (about 5.3%) is the 14-October level - Trading Economics' own pages show inconsistent figures for these rows, so they are approximate; EUR/USD is the 14-October LME fixing, the same session as the board."
    if cv.startswith("PEER EARNINGS ARE IN A LULL"):
        C[i]="PEER EARNINGS: NO COMPANY WAS BACK-FILLED THIS RUN (15-October). The Q3-2026 reporting season opens with Alcoa after the New York close on 15-October; existing earnings_history entries are carried unchanged at their last publicly verified figures, and gaps stay gaps."

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 14-OCTOBER: no newer public disclosure","REVIEWED 15-OCTOBER: no newer public disclosure").replace("REVIEWED 14-OCTOBER. NO NEW DATED","REVIEWED 15-OCTOBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD

for s in [[L_TE,S_TE],[L_RA,S_RA],[L_CX,S_CX],[L_SM,S_SM],[L_NT,S_NT],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG]]:
    d['sources'].append(s)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 14-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 13-Oct)",W])
d['outlook']['sources'].append([L_RA,S_RA]); d['outlook']['sources'].append([L_CX,S_CX])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-13'
ph['rows'][-1]=['2026-10-14',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
