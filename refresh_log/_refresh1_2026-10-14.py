# Daily data refresh - 2026-10-14 (WEDNESDAY, compiled ~03:30 London). Board ROLLED to TUESDAY 13-Oct LME official.
# Westmetall cache-busted EN/DE URLs returned PROVENANCE_REQUIRED; per owner fallback the plain EN overview URL surfaced by WebSearch was
# fetched and shows 13-Oct. DE overview could not be fetched; the Al per-metal table returned a LAGGING cached snapshot (newest 12-Oct).
# Completeness: 5/5 stock-change lines reconcile vs the verified 12-Oct board; prior-day FX fixings (MTLE 1.11770) match the 12-Oct board;
# Reuters (via Mining.com.au) 13-Oct 0915 GMT three-month marks (Al 3,035.50, Cu 14,636.50, Zn 3,741.50, Ni 15,620, Pb 1,894.50) corroborate.
# Trading Economics pages not granted this run -> macro from search-found sources (investingLive, BabyPips, SMM, GuruFocus).
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-14'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_MC="https://mining.com.au/copper-price-rises-amid-disruptions-zinc-and-aluminium-fall/"; L_MC="Mining.com.au (Reuters) - Copper price rises amid disruptions; zinc and aluminium fall (13-Oct-2026)"
S_SM="https://news.metal.com/newscontent/104155320-dollar-slips-metals-mostly-decline-lme-and-shfe-tin-lead-losses-lme-zinc-and-shfe-silver-among-top-decliners-lead-futures-buck-trend-to-rise-overnight-market"; L_SM="SMM - Dollar slips, metals mostly decline [Overnight market] (14-Oct-2026)"
S_HS="https://www.hellenicshippingnews.com/aluminum-falls-to-lowest-since-february/"; L_HS="Hellenic Shipping News (Trading Economics) - Aluminum falls to lowest since February (13-Oct-2026)"
S_KD="https://in.investing.com/news/commodities-news/aluminium-slips-as-concerns-over-gulf-region-supply-disruptions-continue-to-ease-5629522"; L_KD="Investing.com India (Kedia Advisory) - Aluminium slips as Gulf supply concerns ease (13-Oct-2026)"
S_TN="https://www.thenationalnews.com/news/gulf/2026/10/13/strait-of-hormuz-attacks-surge-as-iran-steps-up-campaign-against-us-backed-oil-shipping/"; L_TN="The National - Strait of Hormuz attacks surge as Iran steps up campaign against oil shipping (13-Oct-2026)"
S_IL="https://investinglive.com/commodities/catch-up-time-oil-settles-mixed-brent-near-106-booms-reported-near-aramco-hq-in-dhahran/"; L_IL="investingLive - Oil settles mixed, Brent near $106 (13-Oct-2026)"
S_GF="https://www.gurufocus.com/news/9121205/european-natural-gas-prices-surge-amid-middle-east-tensions-ttf-etf-reacts"; L_GF="GuruFocus - European natural gas prices surge, TTF EUR85.85/MWh (13-Oct-2026)"
S_BP="https://www.babypips.com/news/financial-forex-market-recap-2026-10-13"; L_BP="BabyPips - Financial and forex market recap (13-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
cash,prev_c,m3,prev_m,stk,prev_s=3036.0,3055.0,3037.0,3060.0,238625,238625
spr=cash-m3; pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100

VER=("COMPILED WEDNESDAY 14-OCTOBER-2026. THE BOARD IS THE TUESDAY 13-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION (Wednesday's official prints at 13:20 London). "
 "COMPLETENESS CHECKS: (1) the Westmetall English overview shows the full 13-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.11880), and its prior-day FX column (MTLE 1.11770) matches the verified 12-October board; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 12-October: aluminium unchanged at 238,625; copper 231,275 less 1,625 to 229,650; nickel 282,228 plus 276 to 282,504; zinc 132,850 plus 5,550 to 138,400; lead 345,550 less 3,725 to 341,825; "
 "(3) Reuters' 13-October mid-morning three-month marks (aluminium $3,035.50, copper $14,636.50, zinc $3,741.50, nickel $15,620, lead $1,894.50) are consistent with the settled figures. "
 "CAVEAT: the German overview could not be fetched this run and the aluminium per-metal table served a lagging cached snapshot (newest row 12-October), so the English overview is the newer and governing source. "
 "The whole board sits on ONE UNIFORM SESSION (13-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(f" CASH SETTLED $3,036.00 ON THE 13-OCTOBER OFFICIAL, DOWN $19.00 OR {pc:.2f}% FROM $3,055.00. THREE-MONTH SETTLED $3,037.00, DOWN $23.00 OR {pm:.2f}% FROM $3,060.00 - A SECOND SETTLED CLOSE BENEATH THE 3,061.5 JULY LOW, NOW BY $24.50, and the lowest settled three-month since February. "
 "SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS AGAIN: three-month fell faster than cash, so the CONTANGO NARROWED $4.00 TO JUST $1.00 from $5.00 - the curve is now essentially flat. "
 "VISIBLE LME STOCK WAS UNCHANGED AT 238,625 t, the series low. Reuters (13-October) cited easing Hormuz passage restrictions reconnecting Gulf smelters and rising Indonesian supply; the dollar index eased about 0.35% to near 102.2 ahead of US CPI.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,036.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,037.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $24.50 BENEATH THE 3,061.5 JULY LOW, $40.00 beneath the 3,077 weekly 50% retracement, $146.00 below the broken 3,183 daily level and $252.00 below the 3,289 daily invalidation; the rule-based cap on daily wave (v) sits near 2,977.5."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-1.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,036.00 against three-month $3,037.00 is a $1.00 CONTANGO, NARROWED $4.00 from $5.00 and $13.50 over two sessions. Spread and flat price moved in OPPOSITE directions (three-month down $23.00, contango narrower). The reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET; the bearish structural confirmation, a contango beyond $24.50, is also unmet. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"238,625","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK WAS UNCHANGED AT 238,625 t, the series low on this page. September's mean stock was {sep_s:,} tonnes. A flat stock line with a near-flat curve says the prompt end is not loosening even as the flat price breaks lower."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,037.00, DOWN $23.00 OR {pm:.2f}% FROM $3,060.00 - $24.50 beneath the 3,061.5 July low, a second settled close below it. AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK UNCHANGED AT 238,625 t. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-5.0,"avg":sep_sp,"note":VER+f" A $1.00 CONTANGO, NARROWED $4.00 FROM $5.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in OPPOSITE directions (three-month down, contango narrower). REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1188,"prev":1.1177,"avg":1.1465,"note":VER+" THE LME EURO FIXING FIRMED TO 1.11880 FROM 1.11770 at the Tuesday ring; the ECB fixing printed 1.11880 and BFIX 1.11885. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (13-Oct official)","price":"3,036.0","basis":f"THE 13-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,036.00, DOWN $19.00 OR {pc:.2f}%. Next official Wednesday 14-October 13:20 London."},
 {"tenor":"3-month (13-Oct official)","price":"3,037.0","basis":f"THE 13-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,037.00, DOWN $23.00 OR {pm:.2f}% - $24.50 beneath the 3,061.5 July low (second settled close below it), $40.00 beneath the 3,077 weekly retracement."},
 {"tenor":"Cash-to-3M structure","price":"-1.0 (CONTANGO)","basis":"A $1.00 CONTANGO, narrowed $4.00 from $5.00 - essentially flat. Flat price and spread moved in OPPOSITE directions."},
 {"tenor":"Visible LME stock","price":"238,625 t","basis":f"UNCHANGED on the session at the series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE CURVE IS NOW ESSENTIALLY FLAT WHILE THE FLAT PRICE BREAKS LOWER. On the 13-October official cash $3,036.00 sits $1.00 BELOW three-month $3,037.00, a CONTANGO narrowed $4.00 from $5.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00 and now $1.00. "
 f"READ: the forward is leading the fall while the prompt holds and visible stock sits at a series low of 238,625 t - the break below the July low is a macro and supply-recovery repricing, not a prompt glut. A flip into backwardation would sharpen that divergence. The September mean spread was ${sep_sp:,.2f}. The reversal condition (a backwardation beyond $15.00) is unmet; a contango beyond $24.50 would be the bearish structural confirmation.")

ls=d['lme_series']; assert ls[-1][0]=='12-Oct', ls[-1]
d['lme_series']=ls[1:]+[["13-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2950<r[1]<3450 and 2950<r[2]<3450 for r in d['lme_series'])
CU=(14741.0,14625.5,14822.0,14657.5); NI=(15445.0,15630.0,15515.0,15720.0); ZN=(3821.0,3756.0,3811.0,3760.0); PB=(1860.0,1895.5,1842.0,1885.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/9)/(sum(zs)/8),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/9)/(sum(ps)/8),1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])): R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-13'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending TUESDAY 13-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 22-September dropped and 13-October appended, so the window is 23-September to 13-October. Every point is an official cash settlement; the 13-October points come from the Westmetall English overview, checked by five-for-five stock-line reconciliation against 12-October and matching prior-day FX fixings (the German overview could not be fetched this run). Next official Wednesday 14-October.")
ms['src']=["Westmetall - LME official cash settlements, English overview (13-October-2026 session; stock lines reconciled against 12-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,741.00, down $81.00 or 0.55%; three-month $14,625.50, down $32.00 or 0.22%. The BACKWARDATION NARROWED to $115.50 from $164.50 while stock DREW 1,625 tonnes to 229,650 - a sixth straight draw. Reuters (13-October) said concerns over a supply shortage kept copper within striking distance of its all-time peak, citing Codelco's partial suspension at El Teniente after a landslide and the strike at Centinela."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,445.00, down $70.00 or 0.45%; three-month $15,630.00, down $90.00 or 0.57%. CONTANGO narrowed to $185.00 from $205.00, still the widest carry on the board. Stock rose 276 tonnes to 282,504."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,821.00, up $10.00 or 0.26%; three-month $3,756.00, down $4.00 or 0.11%. BACKWARDATION WIDENED to $65.00 from $51.00 even as another 5,550 tonnes were delivered in, lifting stock to 138,400 t - SMM (14-October) notes LME zinc inventory continuing to grow. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,860.00, up $18.00 or 0.98%; three-month $1,895.50, up $10.50 or 0.56%. CONTANGO narrowed to $35.50 from $43.00. Stock drew 3,725 tonnes to 341,825, a seventeenth consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Tuesday 13-October official lead three-month rose 0.56%, zinc slipped 0.11%, copper 0.22%, nickel 0.57% and aluminium fell most, 0.75%, to a second settled close beneath its July low. The LME euro fixing firmed to 1.1188.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='12-Oct'
        i['hist']=i['hist'][1:]+[["13-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,625.50 (3M); 14,741.00 (cash) $/t"
        i['ratio']="~14,741.00 $/t cash vs LME 3M 14,625.50 $/t"
        i['trend']='flat'
        i['src']=("LME official cash settlement, rolled to the TUESDAY 13-OCTOBER-2026 session at $14,741.00, DOWN $81.00 or 0.55% against $14,822.00. THE WINDOW ROLLED THIS RUN: 22-September dropped and 13-October appended, so the series is the last fifteen published official cash sessions, 23-September to 13-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English overview (stock lines reconciled against 12-October). "
                  "Copper structure for context: backwardation $115.50 (from $164.50), stock drew 1,625 t to 229,650 t.")
d['inputs_summary']=("UPDATE 14-OCTOBER: copper rolled to the Tuesday 13-October LME official cash of $14,741.00, down $81.00, with its fifteen-session window moved to 23-September to 13-October; Reuters still describes copper as within striking distance of its record on Chilean supply disruption. No new SMM fluoride, silicon or magnesium weekly mark was located, and the carbon settlement cycle (anodes, pitch, green coke) is due around 17-18 October - so every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 12-October official cash of \$3,055\.00, or \$1,527\.50, DOWN \$0\.25 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$875\.50, so 63\.6%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 13-October official cash of $3,036.00, or ${tl:,.2f}, DOWN $9.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
n=0
for p in d['premiums']:
    p['src'],k=OLDT.subn(NEWT,p['src']); n+=k
    p['src']=p['src'].replace("COMPILED TUESDAY 13-OCTOBER-2026 (LME BOARD ON THE 12-OCTOBER OFFICIAL).","COMPILED WEDNESDAY 14-OCTOBER-2026 (LME BOARD ON THE 13-OCTOBER OFFICIAL).")
print('premium tariff replaced',n); assert n==len(d['premiums'])
for a in d['alumina']:
    s=a['src'].replace("COMPILED TUESDAY 13-OCTOBER-2026 (LME BOARD ON THE 12-OCTOBER OFFICIAL).","COMPILED WEDNESDAY 14-OCTOBER-2026 (LME BOARD ON THE 13-OCTOBER OFFICIAL).")
    m=re.search(r"THE RATIO: LME Alumina at \$360\.40/t against the 12-October aluminium three-month of \$3,060\.00 is [0-9.]+%",s)
    if m: s=s.replace(m.group(0),f"THE RATIO: LME Alumina at $360.40/t against the 13-October aluminium three-month of $3,037.00 is {360.4/3037*100:.2f}%")
    a['src']=s

d['lme_commentary']=(f"ALUMINIUM EXTENDED BENEATH ITS JULY LOW. On the Tuesday 13-October official cash settled $3,036.00, down $19.00, and three-month $3,037.00, down $23.00 or {abs(pm):.2f}% - $24.50 beneath the 3,061.5 July low and the lowest settled three-month since February. "
 "Three-month again fell faster than cash, so the contango NARROWED $4.00 to just $1.00 (spread and price in OPPOSITE directions), and visible stock held at the series low of 238,625 t. "
 "Reuters (13-October) quoted Panmure Liberum that some easing in Hormuz passage restrictions has 'reconnected Gulf smelters to the world', alongside rising Indonesian supply; Macquarie has cut its 2026 deficit estimate to 820,000 t on faster Middle East restarts, and Citi sees a 1.8 Mt 2027 surplus. Aluminium was the weakest base metal on the session while lead rose. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND IN CONTROL; THE JULY-LOW BREAK HAS FOLLOWED THROUGH. Against: three-month settled $3,037.00, a second close beneath 3,061.5 and now $24.50 below it; the supply narrative is Gulf reconnection plus Indonesian growth (Reuters, Macquarie); Citi forecasts a 2027 surplus; spot Japanese premiums sit below the $255/t Q4 benchmark. "
 "Constructive: the curve has gone almost flat ($1.00 contango) and visible stock sits at a series low of 238,625 t, so the prompt is tight; the dollar eased from its 18-month high; European gas is at its highest since 2022 and Hormuz attacks continue, keeping smelter energy and freight costs high.")
d['bottom_line']=("BOTTOM LINE: aluminium settled on the Tuesday 13-October LME official at cash $3,036.00 and three-month $3,037.00 - a second settled close beneath the 3,061.5 July low, now by $24.50. "
 "The contango narrowed to $1.00 and visible stock held at 238,625 t, so the prompt is not loosening even as the forward falls. Scenario weights are held at 10% bull / 45% base / 45% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) targets 2,980-3,000 with a rule-based floor near 2,977, invalidation 3,289; the weekly corrective count towards 2,894 stays preferred.")
c=d['commercial']
c=c.replace("FIRST, THE CURVE IS NEAR FLAT: a $5.00 contango on 12-October, narrowed from $14.50, so there is little carry reward for waiting.","FIRST, THE CURVE IS FLAT: a $1.00 contango on 13-October, narrowed from $5.00, so there is effectively no carry reward for waiting.")
c=c.replace("is $1,527.50 on 12-October cash, 63.6% of the $2,403/t premium",f"is ${tl:,.2f} on 13-October cash, {share:.1f}% of the $2,403/t premium")
c=c.replace("the 12-October official settled $1.50 beneath 3,061.5 - follow-through below $3,023 would open 2,980-3,000;","the 13-October official settled $24.50 beneath 3,061.5, so the 2,980-3,000 zone is now in play; US CPI on 14-October and Alcoa's results on 15-October;")
assert c!=d['commercial']; d['commercial']=c

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 14-OCTOBER at 10/45/45: the 13-October official extended the break to $3,037.00 three-month, $24.50 beneath the July low, on Gulf reconnection and Indonesian supply (Reuters); the flat $1.00 contango and series-low stock argue against moving further to the bear case before US CPI and Alcoa's results. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium's break below the July floor followed through on Tuesday - three-month settled $3,037, the lowest since February - as Gulf smelters reconnect to world markets and Indonesian supply grows, yet a flat curve and series-low LME stock show the prompt market is still tight.",
 "points":[
 "WHAT MOVED: Tuesday's LME official settled cash at $3,036.00 (-$19.00) and three-month at $3,037.00 (-$23.00, -0.75%), $24.50 beneath the $3,061.5 July low; the contango narrowed to $1.00 from $5.00 (spread and price moved in opposite directions) and LME stock held at 238,625 t. Aluminium was the weakest base metal on the day.",
 "WHY: Reuters cites easing Hormuz passage restrictions that have reconnected Gulf smelters, plus rising Indonesian supply; Macquarie cut its 2026 deficit view to 820,000 t on faster Middle East restarts and Citi sees a 1.8 Mt surplus in 2027. The dollar eased about 0.35% to near 102.2.",
 "ENERGY AND LOGISTICS: at least 12 tankers were attacked in and around Hormuz in the past week (The National); Brent settled near $106 and Dutch TTF gas rose to about EUR 85.9/MWh, the highest since late 2022 - keeping smelter energy and freight costs elevated.",
 "WHAT TO WATCH: US September CPI today (14-October); Alcoa's Q3 results on Thursday 15-October after the New York close; whether the curve flips into backwardation; the 2,980-3,000 target zone; the mid-October carbon settlements around 17-18 October."]}

d['feed']=([
 {"when":"Wed 14-Oct","impact":"Bearish","text":f"BOARD ROLLED TO THE TUESDAY 13-OCTOBER LME OFFICIAL: cash $3,036.00 (-$19.00), three-month $3,037.00 (-$23.00, {pm:.2f}%) - a second settled close beneath the 3,061.5 July low - contango NARROWED to $1.00 from $5.00, stock unchanged at 238,625 t."},
 {"when":"Tue 13-Oct","impact":"Bearish","text":"Aluminium fell 0.6% to $3,035.50 by mid-morning, near an eight-month low; Panmure Liberum said easing Hormuz passage restrictions have reconnected Gulf smelters to the world, with Indonesian supply rising (Reuters via Mining.com.au)."},
 {"when":"Tue 13-Oct","impact":"Bullish","text":"At least 12 tankers attacked in and around the Strait of Hormuz in the past week; UKMTO confirmed six vessel strikes on Sunday alone (The National)."},
 {"when":"Tue 13-Oct","impact":"Bullish","text":"Dutch TTF gas rose 1.8% to EUR 85.85/MWh, a sixth straight gain and the highest since late 2022 (GuruFocus); Brent settled near $106 (investingLive)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":f"LME ALUMINIUM EXTENDS BENEATH THE JULY LOW. The Tuesday 13-October official settled cash at $3,036.00 ({pc:.2f}%) and three-month at $3,037.00 ({pm:.2f}%), $24.50 beneath the 3,061.5 July low. The contango narrowed to $1.00 from $5.00 and visible stock was unchanged at 238,625 t. Copper three-month eased to $14,625.50 with its backwardation narrowing to $115.50; zinc stock rose another 5,550 t to 138,400 t."},
 {"theme":"Supply","horizon":"0-3 months","impact":"Bearish","url":S_MC,
  "headline":"GULF SMELTERS 'RECONNECTED TO THE WORLD' (Reuters via Mining.com.au, 13-October): three-month aluminium fell 0.6% to $3,035.50 by 0915 GMT, near an eight-month low. Panmure Liberum: 'Some easing in passage restrictions in the Strait of Hormuz has reconnected Gulf smelters to the world', with new Indonesian supply also rising. Copper rose for a third session to $14,636.50 on supply-shortage concerns (El Teniente landslide, Centinela strike); zinc fell 0.4%, lead rose 0.6%."},
 {"theme":"Market","horizon":"3-12 months","impact":"Bearish","url":S_KD,
  "headline":"FORECASTERS TRIM THE DEFICIT (Investing.com India / Kedia Advisory, 13-October): Macquarie cut its 2026 global aluminium deficit forecast to 820,000 t, 120,000 t below its June estimate, on faster Middle East restarts, and sees prices averaging $3,050/t in 2027 against $3,325/t in 2026; Citi sees a shift from a 941,000 t deficit in 2026 to a 1.8 Mt surplus in 2027. IAI data for August: global output -1.5% year on year, China a record 3.87 Mt (+3%), GCC output down 43% to 299,000 t."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Bearish","url":S_HS,
  "headline":"ALUMINIUM AT ITS LOWEST SINCE FEBRUARY (Trading Economics via Hellenic Shipping News, 13-October): UK aluminium futures near $3,050/t on a dollar near an 18-month high, easing Gulf supply concerns (EGA restarting part of Al Taweelah; Macquarie's deficit cut), Rio Tinto's agreement to keep Bell Bay running through 2031, expanding Indonesian capacity and weaker Chinese demand expectations."},
 {"theme":"Logistics","horizon":"0-3 months","impact":"Bullish","url":S_TN,
  "headline":"HORMUZ ATTACKS SURGE (The National, 13-October): at least 12 tankers were attacked in and around the strait in the past week; UKMTO confirmed six strikes on Sunday alone, five in the strait and one near Oman's Sohar anchorage. Iran's IRGC warned that tankers ignoring its 'security and rules' would face a similar fate, while the US Secretary of State said nearly as much oil is flowing out as before the conflict. For aluminium, Gulf export freight and war-risk costs stay elevated even as flows partly resume."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish","url":S_GF,
  "headline":"EUROPEAN GAS EXTENDS ITS RALLY (GuruFocus, 13-October): Dutch TTF rose 1.8% to EUR 85.85/MWh, a sixth consecutive gain and the highest since late 2022, on Middle East tensions. Brent settled near $106, down about $1, as hopes of a US-Russia diesel deal offset Gulf risk; OPEC cut its 2026 demand-growth forecast for a sixth month (investingLive). Higher European energy costs pressure marginal European smelters."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Mixed","url":S_SM,
  "headline":"DOLLAR SLIPS BEFORE US CPI; METALS MOSTLY LOWER (SMM, 14-October): LME aluminium fell 0.59% overnight and SHFE aluminium 0.45%; LME zinc -1.08%, tin -3.4%, lead +1.04%. The dollar index fell 0.37% to 102.2 ahead of Wednesday's September CPI; China's September CPI rose 0.9% and PPI 5.0% year on year."},
]+d['news'][:13]
d['news']=d['news'][:20]

for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Tue 13-Oct':
        cat['date']='Daily, from Wed 14-Oct'
        cat['event']="3,061.5 BROKEN ON TWO SETTLED OFFICIALS (NOW BY $24.50), 3,023 INTRADAY LOW, 3,077 / 3,148.5 / 3,183 OVERHEAD, 3,289 INVALIDATION. Three-month settled $3,037.00 on Tuesday 13-October. A settled close beneath 3,023 opens the 2,980-3,000 area (wave (v) of C, rule cap near 2,977.5); a settled recovery above 3,077 would weaken the break; above 3,148.5 would warn the C wave is complete and above 3,183 would void the impulsive C-wave labelling."
d['outlook']['catalysts'].insert(1,{"date":"Wed 14-Oct","impact":"High","event":"US SEPTEMBER CPI. Markets are focused on the release (SMM, 14-October); the dollar index slipped to about 102.2 from an 18-month high and the US ten-year eased to about 5.22% beforehand (BabyPips). A hot print that lifts the dollar and yields would add to the macro pressure on aluminium; a soft one would ease it."})
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 14-OCTOBER: the contango NARROWED $4.00 to $1.00 on 13-October as three-month fell $23.00 - spread and price in opposite directions again; far inside the $24.50 bearish-confirmation threshold. Trend held at FLAT."
RK[1]['risk']+=" UPDATE 14-OCTOBER: the dollar index eased about 0.35% to near 102.2 and the US ten-year about 3bp to near 5.22% on 13-October ahead of US CPI (BabyPips). Trend held at UP pending the CPI print."
RK[4]['risk']+=" UPDATE 14-OCTOBER: LME stock unchanged at the 238,625 t series low on 13-October. Trend held at FLAT."
d['outlook']['ai_analysis'].insert(0,"WEDNESDAY REVIEW, 14-OCTOBER: the July-low break followed through. Tuesday's official settled three-month at $3,037.00, $24.50 beneath 3,061.5 and the lowest since February, with aluminium the weakest base metal on the day. The driver is supply: Reuters quotes Panmure Liberum that easing Hormuz passage restrictions have reconnected Gulf smelters, Indonesian supply is rising, and Macquarie has cut its 2026 deficit to 820,000 t. Against that, the curve is flat ($1.00 contango) and visible stock is at a series low, while European gas at a near three-year high and continuing Hormuz attacks keep cost and freight risk elevated. Weights held at 10/45/45 into US CPI and Alcoa's 15-October results.")

EWS=("REVIEWED 14-OCTOBER ON THE TUESDAY 13-OCTOBER OFFICIAL: three-month settled $3,037.00, down $23.00, a second settled close beneath the 3,061.5 July low (now by $24.50). The base case is unchanged and progressing: wave (v) of C extending toward 2,980-3,000, with the rule-based cap on (v) near 2,977.5 (it must stay shorter than (iii)'s $171). Base case about 70%; the double-bottom alternate (about 30%) still needs a settled recovery above 3,077. Invalidation unchanged at 3,289; confidence moderate. ")
EWL=("REVIEWED 14-OCTOBER ON THE TUESDAY 13-OCTOBER OFFICIAL: three-month settled $3,037.00, a second close beneath the 3,061.5 July low, extending the weekly decline from 3,855; the corrective count towards 2,894 stays preferred and no re-label is needed. ")
d['ew']['short_term']['writeup']=EWS+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=EWL+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="106.0",day="settled near $106 on 13-October, down nearly $1 (about -1%) from Monday's highest close since mid-September (investingLive); approximate settle",
 note="REFRESHED WEDNESDAY 14-OCTOBER-2026 from search-found public reporting (investingLive, 13-October; value approximate as reported 'near $106'): Brent eased as hopes of a US-Russia diesel export deal offset Saudi-Houthi escalation and reported booms near Aramco's Dhahran headquarters; OPEC cut its 2026 demand-growth forecast for a sixth month. Energy is a major smelter cash-cost line. SOURCE: "+S_IL)
M['European gas TTF (EUR/MWh)'].update(value="85.85",day="+1.8% on 13-October, a sixth straight gain; highest since late 2022 (GuruFocus)",
 note="REFRESHED WEDNESDAY 14-OCTOBER-2026 (GuruFocus, 13-October): Dutch TTF futures rose to EUR 85.85/MWh on Middle East tensions. European power and gas costs bear on marginal European smelter economics. SOURCE: "+S_GF)
M['US dollar index (DXY)'].update(value="102.2",day="-0.35% to -0.37% on 13-October, slipping from an 18-month high ahead of US CPI (BabyPips; SMM)",
 note="REFRESHED WEDNESDAY 14-OCTOBER-2026 (BabyPips recap and SMM overnight report, 13-14 October): the dollar index fell to about 102.2 ahead of the US September CPI release. SOURCE: "+S_BP)
M['US 10-year Treasury yield (%)'].update(value="5.22",day="down about 3bp on 13-October (BabyPips, approximate)",
 note="REFRESHED WEDNESDAY 14-OCTOBER-2026 (BabyPips recap, approximate level). Higher yields raise the cost of carrying metal and financing inventory. SOURCE: "+S_BP)
M['EUR/USD'].update(value='1.11880',day="LME fixing on 13-October, +0.10% from 1.11770; ECB fixing 1.11880, BFIX 1.11885",
 note="REFRESHED WEDNESDAY 14-OCTOBER-2026 to the 13-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE TUESDAY 13-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION; Wednesday's official prints at 13:20 London. Reference prices (Reuters, SMM, Trading Economics) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN: the cache-busted Westmetall URLs were not granted; the plain Westmetall English overview (found via web search) was fetched and shows the full 13-October official. The German overview could NOT be fetched and the aluminium per-metal table served a lagging cached snapshot (newest row 12-October), so the usual EN/DE agreement test could not be run; the English overview, being the newer session, governs.")
C[2]=("COMPENSATING CHECKS: the overview's prior-day FX column (MTLE 1.11770, ECB 1.11810, BFIX 1.11756) matches the 12-October board verified on 13-October, and Reuters' 13-October 0915 GMT three-month marks (aluminium $3,035.50, copper $14,636.50, zinc $3,741.50, nickel $15,620, lead $1,894.50) are consistent with the settled officials.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 12-October: aluminium unchanged at 238,625; copper -1,625 to 229,650; nickel +276 to 282,504; zinc +5,550 to 138,400; lead -3,725 to 341,825.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (13-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (nine sessions, 01- to 13-October) as their latest point. The price chart axis floor (2,950) brackets three-month at 3,037; the stock chart axis floor (225,000 t) brackets visible stock at 238,625 t.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,036.00 against three-month $3,037.00 is therefore a $1.00 CONTANGO, narrowed $4.00 from $5.00 on 12-October - and it narrowed while three-month fell, i.e. spread and price moved in OPPOSITE directions."
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a re-verified 50% Section 232 rate on full customs value, the tariff leg is 0.50 times the 13-October official cash of $3,036.00, or ${tl:,.2f}, leaving an ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (near $106, approximate as reported), the dollar index (about 102.2) and the US ten-year (about 5.22%) are 13-October levels from search-found public reports because Trading Economics was not reachable this run; TTF (EUR 85.85/MWh) is the 13-October reported level; EUR/USD is the 13-October LME fixing, the same session as the board."

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 13-OCTOBER: no newer public disclosure","REVIEWED 14-OCTOBER: no newer public disclosure").replace("REVIEWED 13-OCTOBER. NO NEW DATED","REVIEWED 14-OCTOBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD

for s in [[L_MC,S_MC],[L_SM,S_SM],[L_HS,S_HS],[L_KD,S_KD],[L_TN,S_TN],[L_IL,S_IL],[L_GF,S_GF],[L_BP,S_BP]]:
    d['sources'].append(s)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 13-Oct-2026 session (English overview; stock lines reconciled vs 12-Oct)",W])
d['outlook']['sources'].append([L_MC,S_MC]); d['outlook']['sources'].append([L_KD,S_KD])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-12'
ph['rows'][-1]=['2026-10-13',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
