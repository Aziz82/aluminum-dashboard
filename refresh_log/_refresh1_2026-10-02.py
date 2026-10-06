# Daily data refresh - 2026-10-02 (FRIDAY, compiled ~03:40 London, BEFORE the ring).
# Board ROLLED to THURSDAY 01-Oct LME official. EN+DE cache-busted overviews agree; per-metal Al and Cu tables show 01-Oct newest, 30-Sep prior unchanged.
import json
P='market_data.json'
d=json.load(open(P,encoding='utf-8'))
RD='2026-10-02'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_BR="https://www.brecorder.com/news/40442141/aluminium-falls-to-2-month-low-on-iran-peace-hopes-stronger-dollar"
S_DAO="https://discoveryalert.com/analysis/aluminum-market-outlook-october-2026/"
S_ALC="https://www.alcircle.com/news/lme-aluminium-cash-bid-drops-22-to-3-203-as-asian-reference-price-falls-1-38-121384"
S_SMMX="https://news.metal.com/newscontent/104140398-restoration-for-one-smelter-in-middle-east-initially-completed-yoy-decline-in-aluminium-output-narrows-to-24"
S_BB="https://www.mining-technology.com/news/bell-bay-aluminium-continue-operations-2031/"
S_TEB="https://tradingeconomics.com/commodity/brent-crude-oil"
S_TEY="https://tradingeconomics.com/united-states/government-bond-yield"
S_TED="https://tradingeconomics.com/united-states/currency"

# September per-metal official cash tables (carried from the 01-Oct run, 22 sessions) for the prior-month means
ZN_C=[4115.0,4000.0,3995.5,4087.0,4157.0,4110.0,4186.0,4105.0,4015.0,3951.0,3922.0,3937.0,3941.0,4010.0,4018.0,4006.0,3949.0,3981.0,4060.0,3957.0,3977.0,3954.0]
PB_C=[1874,1873,1870,1871,1875,1859,1871,1870.5,1854,1834,1829,1848,1862,1868,1890,1909,1885.5,1900,1902.5,1886,1876,1856]
mean=lambda L: sum(L)/len(L)
sep_zn=mean(ZN_C); sep_pb=mean(PB_C)
B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']

cash,prev_c,m3,prev_m,stk,prev_s=3120.0,3204.0,3131.0,3210.0,240625,241375
spr=cash-m3
pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100

VER=("COMPILED FRIDAY 02-OCTOBER-2026 AT ABOUT 03:40 LONDON, BEFORE FRIDAY'S RING. THE BOARD ROLLED THIS RUN TO THE THURSDAY 01-OCTOBER-2026 LONDON METAL EXCHANGE OFFICIAL, THE LATEST PUBLISHED SESSION AND THE FIRST OF OCTOBER; FRIDAY'S OFFICIAL PRINTS AT 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted English and German Westmetall overviews AGREE EXACTLY on 01-October across all six metals, all six stock lines and the foreign-exchange fixings; (2) the per-metal daily tables for aluminium and copper show 01-October as the newest row with 30-September reproduced unchanged as the prior row; "
 "(3) ALL FIVE STOCK LINES RECONCILE against the levels carried for 30-September: aluminium 241,375 less 750 to 240,625; copper 249,400 less 1,325 to 248,075; nickel 284,898 less 216 to 284,682; zinc 121,600 PLUS 2,375 to 123,975; lead 357,350 less 750 to 356,600. "
 "The whole board sits on ONE UNIFORM SESSION (01-October) and no intraday, closing, reference or contract-for-difference mark is used anywhere in it. Prior-month averages remain the completed SEPTEMBER-2026 official means. NEXT OFFICIAL: FRIDAY 02-OCTOBER, 13:20 LONDON - also the weekly close.")

AL=(f" CASH SETTLED $3,120.00 ON THE 01-OCTOBER OFFICIAL, DOWN $84.00 OR {abs(pc):.2f}% FROM $3,204.00. THREE-MONTH SETTLED $3,131.00, DOWN $79.00 OR {abs(pm):.2f}% FROM $3,210.00 - THE LARGEST SINGLE-SESSION FALL ON THIS BOARD IN WEEKS AND THE LOWEST THREE-MONTH OFFICIAL SINCE EARLY JULY. "
 "SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION: cash fell $5.00 more than three-month, so the CONTANGO WIDENED TO $11.00 from $6.00 while the price fell - a mildly weaker front, consistent with the move. "
 "VISIBLE LME STOCK DREW 750 TONNES TO 240,625, the first change after five unchanged sessions. "
 "THE 3,183 DAILY ELLIOTT INVALIDATION BROKE ON AN OFFICIAL SETTLEMENT: three-month at $3,131.00 is $52.00 beneath it, so the constructive daily count is re-labelled this run. Public reporting attributes the slide to a stronger dollar (index at its highest since March 2025 per Trading Economics), multi-decade-high US yields, Iran-related peace hopes improving prospective Gulf flows (Reuters via Business Recorder, 01-October) and faster Gulf smelter restarts.")

d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,120.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,131.0","pos":False,"delta":VER+AL+" THREE-MONTH IS NOW $130.00 BELOW THE 3,261 WEEKLY RETRACEMENT LEVEL into Friday's weekly close, $52.00 BELOW THE BROKEN 3,183 DAILY LEVEL and $69.50 above the 3,061.5 July low. Third-party reports put post-official trade near $3,146 (Business Recorder, -0.74%, low $3,141, lowest since 28-July) and an intraday low near $3,112 (Discovery Alert); neither is an official settlement and neither is used on the board."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-11.0","pos":False,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,120.00 against three-month $3,131.00 is an $11.00 CONTANGO, WIDENED $5.00 from $6.00. Spread and flat price moved in the SAME direction (price down, contango wider) - the front softened with the price. The published reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"240,625","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK DREW 750 TONNES TO 240,625, the first move after five unchanged sessions and a fresh low for the series on this page. AL Circle reports 14,700 t of cancelled warrants and 226,675 t live on 30-September. September's mean stock was {sep_s:,} tonnes. Lower stock alongside a falling price says the decline is macro- and supply-outlook-driven, not a visible physical glut."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,131.00, DOWN $79.00 OR {abs(pm):.2f}% FROM $3,210.00. AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DREW 750 TONNES TO 240,625 AFTER FIVE UNCHANGED SESSIONS. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-6.0,"avg":sep_sp,"note":VER+f" AN $11.00 CONTANGO, WIDENED $5.00 FROM $6.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in the SAME direction on this ring. PUBLISHED REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1305,"prev":1.1351,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.13050 FROM 1.13510; the ECB fixing printed 1.12980 and BFIX 1.13080, so all three agree on a firmer dollar. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated. Trading Economics (02-October) has the dollar index at its highest since March 2025."},
]

d['outlook']['forward_path']=[
 {"tenor":"Cash (01-Oct official - latest published)","price":"3,120.0","basis":f"THE 01-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,120.00, DOWN $84.00 OR {abs(pc):.2f}%. Friday's official prints at 13:20 London."},
 {"tenor":"3-month (01-Oct official - latest published)","price":"3,131.0","basis":f"THE 01-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,131.00, DOWN $79.00 OR {abs(pm):.2f}%: $52.00 beneath the broken 3,183 daily level, $130.00 beneath 3,261 into Friday's weekly close, $69.50 above the 3,061.5 July low."},
 {"tenor":"Cash-to-3M structure","price":"-11.0 (CONTANGO)","basis":"An $11.00 CONTANGO, widened $5.00 from $6.00. Flat price and spread moved in the SAME direction; the front softened with the price."},
 {"tenor":"Visible LME stock","price":"240,625 t","basis":f"DREW 750 t after five unchanged sessions; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE CURVE SOFTENED WITH THE PRICE. On the 01-October official cash $3,120.00 sits $11.00 BELOW three-month $3,131.00, a CONTANGO widened $5.00 from $6.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00 and now $11.00. "
 f"READ: the front gave up slightly more than three-month, so this session the spread and flat price moved together - mild, not a glut signal, especially with visible stock still drawing (240,625 t). The September mean spread was ${sep_sp:,.2f}. The published reversal condition (a backwardation beyond $15.00) remains far away.")

ls=d['lme_series']; assert ls[-1][0]=='30-Sep', ls[-1]
d['lme_series']=ls[1:]+[["01-Oct",cash,m3,stk]]
d['chart_price_axis']=[3000,3450]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":14290.0,"day":round((14290/14455-1)*100,2),"ytd":round((14290/12511-1)*100,2)},
 {"name":"Nickel","price":15760.0,"day":round((15760/16060-1)*100,2),"ytd":round((15760/16915-1)*100,2)},
 {"name":"Zinc","price":3766.0,"day":round((3766/3842-1)*100,2),"ytd":round((3766/3130.5-1)*100,2)},
 {"name":"Lead","price":1869.0,"day":round((1869/1890-1)*100,2),"ytd":round((1869/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*14290/14455,1); mh['ni'][-1]=round(mh['ni'][-1]*15760/16060,1)
# zn/pb 'now' = current-month (October) cash average-to-date = the single 01-Oct session, rebased from the September monthly-average point
mh['zn'][-1]=round(mh['zn'][-1]*3834.0/sep_zn,1); mh['pb'][-1]=round(mh['pb'][-1]*1837.0/sep_pb,1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',14335.0),('NI',15570.0),('ZN',3834.0),('PB',1837.0)): R[k]=R[k][1:]+[v]
ms['asof']='2026-10-01'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending THURSDAY 01-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 10-September dropped and 01-October appended, so the window is 11-September to 01-October. Every point is an official cash settlement, verified against the cache-busted Westmetall English and German overviews, which agree to the cent, the per-metal daily tables, and five-for-five stock-line reconciliation. Friday's official prints at 13:20 London, after this page compiles.")
ms['src']=["Westmetall - LME official cash settlements, EN and DE overviews cache-busted and in exact agreement (01-October-2026 session)",W]

AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",14335.0,14290.0," COPPER: cash $14,335.00, down $152.00 or 1.05%; three-month $14,290.00, down $165.00 or 1.14%. The BACKWARDATION widened to $45.00 from $32.00 - the front held up better than the curve. Stock drew 1,325 tonnes to 248,075."),
 ("Nickel",15570.0,15760.0," NICKEL: cash $15,570.00, down $290.00 or 1.83%; three-month $15,760.00, down $300.00 or 1.87%. CONTANGO narrowed to $190.00 from $200.00, still the widest carry on the board. Stock drew 216 tonnes to 284,682."),
 ("Zinc",3834.0,3766.0," ZINC: cash $3,834.00, down $120.00 or 3.03%; three-month $3,766.00, down $76.00 or 1.98%. The BACKWARDATION NARROWED SHARPLY to $68.00 from $112.00 as stock ROSE 2,375 tonnes to 123,975 - the only metal to add stock, and the clearest easing of nearby tightness on the board. Zinc remains the strongest metal on this board year to date."),
 ("Lead",1837.0,1869.0," LEAD: cash $1,837.00, down $19.00 or 1.02%; three-month $1,869.00, down $21.00 or 1.11%. CONTANGO narrowed $2.00 to $32.00. Stock drew 750 tonnes to 356,600, a ninth consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL, REPORTED AS DATA NOT AS A REGIME SIGNAL: on the first October session three-month prices fell in ALL FIVE metals (aluminium -2.46%, copper -1.14%, nickel -1.87%, zinc -1.98%, lead -1.11%) as the LME euro fixing fell to 1.1305 from 1.1351 - a broad, dollar-led risk-off session rather than an aluminium-specific shock, although aluminium fell most.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

OLDH="COMPILED THURSDAY 01-OCTOBER-2026 AT ABOUT 03:40 LONDON, BEFORE THURSDAY'S RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY)."
NEWH="COMPILED FRIDAY 02-OCTOBER-2026 AT ABOUT 03:40 LONDON, BEFORE FRIDAY'S RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY)."
for i in d['inputs']:
    if isinstance(i.get('src'),str): i['src']=i['src'].replace(OLDH,NEWH)
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='30-Sep'
        i['hist']=i['hist'][1:]+[["01-Oct",14335.0]]
        i['val']="~14,290.00 (3M); 14,335.00 (cash) $/t"
        i['ratio']="~14,335.00 $/t cash vs LME 3M 14,290.00 $/t"
        i['trend']='down'
        i['src']=("LME official cash settlement, rolled to the 01-OCTOBER-2026 session at $14,335.00, DOWN $152.00 or 1.05% against $14,487.00. THE WINDOW ROLLED THIS RUN: 10-September dropped and 01-October appended, so the series is the last fifteen published official cash sessions, 11-September to 01-October - the same window as the LME Board sparklines. Official settlement only, verified on the cache-busted Westmetall English and German overviews, which agree to the cent, and the per-metal daily table. "
                  "Copper structure for context: backwardation $45.00 (from $32.00), stock drew 1,325 t to 248,075 t.")
d['inputs_summary']=("UPDATE 02-OCTOBER: copper rolled to the 01-October LME official cash of $14,335.00, down $152.00, with its fifteen-session window moved to 11-September to 01-October. No other input mark printed in this window - China is on its 01-08 October National Day holiday, so the SMM fluoride, silicon and magnesium weeklies are not expected until after 08-October, and the carbon settlement cycle (anodes, pitch, green coke) is mid-October - so every other row is carried at its own dated public mark and no value was interpolated.")

for r in d['raw_materials']:
    if isinstance(r.get('src'),str): r['src']=r['src'].replace(OLDH,NEWH)

for a in d['alumina']:
    if a['name'].startswith('LME Alumina'):
        a['val']=360.4; a['asof']='30-Sep-26'; a['trend']='up'
ratio=360.4/m3*100
ALNOTE=("COMPILED FRIDAY 02-OCTOBER-2026 AT ABOUT 03:40 LONDON. ONE ROW UPDATED TO A NEW DATED PUBLIC MARK: AL Circle reports the LME Alumina (Platts) price at $360.40/t on 30-September, up 1.50% on the day; the row previously carried an older $363.60 mark from 21-August and is now refreshed to the newer date. "
 "The FOB East Australia trade row stays at its 18-September mark; SMM separately reported 30,000 t traded at $369/t FOB Western Australia on 30-September for November shipment, a different basis that is reported in news rather than overwriting the row. The SMM alumina index is carried at its 30-September print of 2,669.99 yuan/tonne; SHFE is closed 01-08 October. "
 f"THE RATIO: LME Alumina at $360.40/t against the 01-October aluminium three-month of $3,131.00 is {ratio:.2f}%, against a decade norm of 15-17%. Alumina rose while metal fell, but it remains historically CHEAP relative to metal.")
for a in d['alumina']:
    a['src']=ALNOTE

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
PREM=("COMPILED FRIDAY 02-OCTOBER-2026 AT ABOUT 03:40 LONDON. PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND THIS PANEL CARRIES EACH ROW AT ITS OWN LAST PUBLIC ASSESSMENT DATE. NO NEW PUBLIC PREMIUM ASSESSMENT WAS LOCATED FOR THIS WINDOW, so every row is CARRIED UNCHANGED. The Q4 MJP remains unsettled: the latest public data point is SMM (30-September), reporting a major producer's offer lowered to $280/t from $310/t and the market expecting settlement BELOW $280/t; that is an offer, not a settlement. "
 f"THE TARIFF DECOMPOSITION IS REFRESHED DAILY BY DESIGN: on a re-verified Section 232 rate of 50% on aluminium articles applied to full customs value, the tariff leg of the US duty-paid premium is 0.50 times the 01-October official cash of $3,120.00, or ${tl:,.2f}, DOWN $42.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}% of the US duty-paid premium is policy arithmetic rather than market. "
 "This page does NOT fabricate freight, financing or tightness splits for any premium row.")
for p in d['premiums']:
    s=p['src']; j=s.find("for any premium row.")
    if s.startswith("COMPILED THURSDAY") and j>0: p['src']=PREM+s[j+len("for any premium row."):]
    else: p['src']=PREM+" "+s

pdv=d['premium_drivers'][0]
pdv['d']=("SMM reports on 30-September that a major producer lowered its Q4 MJP offer to $280/t from $310/t and that the market now expects the final Q4 settlement below $280/t, against a Q3 settlement of $395/t. No settlement had been publicly reported by 02-October. WHY IT LANDS ON PREMIUMS: the quarterly MJP is the reference for much Asian physical business, so a settlement below $280 would reset the regional premium level downward for the quarter. The LME curve offers no exchange-side scarcity signal either: an $11.00 contango on 01-October.")

d['lme_commentary']=(f"ALUMINIUM OPENED OCTOBER WITH ITS SHARPEST FALL IN WEEKS AND BROKE A KEY LEVEL. On the 01-October official cash settled $3,120.00, down $84.00 or {abs(pc):.2f}%, and three-month $3,131.00, down $79.00 or {abs(pm):.2f}% - the lowest three-month official since early July and $52.00 beneath the 3,183 August swing low. "
 "The contango widened $5.00 to $11.00, so spread and price moved in the SAME direction, mildly; visible stock nonetheless drew 750 tonnes to 240,625. "
 "Public reporting (Reuters via Business Recorder, 01-October) attributes the fall to US-Iran ceasefire hopes improving prospective Gulf flows ('There's some sensitivity for aluminium there, in terms of flows of material through the Gulf' - BNP Paribas), a dollar near multi-month highs and rising Treasury yields. Discovery Alert cites Macquarie cutting its 2026 deficit estimate to 820,000 t from 940,000 t on a faster-than-expected EGA Al Taweelah restart and forecasting a 410,000 t surplus in 2027. "
 f"The whole complex fell on the session (three-month down in all five metals), so the move is broad and dollar-led, with aluminium the weakest. China's markets are shut 01-08 October. September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH ON PRICE, MILDLY BEARISH ON STRUCTURE. Against: three-month broke the 3,183 swing low on an official settlement and sits $69.50 above the 3,061.5 July low; the contango widened to $11.00; the dollar index is at its highest since March 2025 and the US ten-year near 5.26-5.3%, the highest since 2002 (Trading Economics); supply restarts are accelerating (Alba lines 4-6 back, overseas operating capacity back near 29.65 Mt per SMM) and Macquarie projects a 2027 surplus. "
 "Constructive: visible LME stock is still drawing (240,625 t) and described in public commentary as near a 36-year low, Macquarie still sees a 2026 deficit of 820,000 t, and energy costs are rising rather than falling (Brent about $102.7, up about 7.5% over the month, on reported Hormuz tanker attacks and US carrier deployments per Trading Economics) - which supports the smelter cost floor. The peace-hope narrative and the escalation narrative are both in public reporting at once; they point in opposite directions for Gulf supply.")
d['commercial']=("COMMERCIAL READ - GENERIC AND PUBLIC. FIRST, THE CURVE NOW PAYS BUYERS A LITTLE TO WAIT: an $11.00 contango is still small, but it widened as the price fell, so the carry argument for deferring purchases has strengthened slightly. SECOND, ASIAN PREMIUMS ARE RESETTING LOWER: public reporting (SMM, 30-September) has the Q4 MJP offer at $280/t with settlement expected below that, against $395/t in Q3. THIRD, THE TARIFF ARITHMETIC MOVED WITH THE METAL: "
 f"on a verified 50% Section 232 rate, the tariff leg of the US Midwest duty-paid premium is ${tl:,.2f} on 01-October cash, {share:.1f}% of the $2,403/t premium. FOURTH, WATCH THE CALENDAR: Friday 02-October sets the weekly close against 3,261 (three-month is $130 beneath it); the 3,061.5 July low is the next technical reference; China returns from holiday on 09-October. This is generic public market context, not advice.")
d['bottom_line']=(f"BOTTOM LINE: aluminium opened October with a {abs(pm):.1f}% fall on the LME official - cash $3,120.00, three-month $3,131.00 - breaking the 3,183 August low that had held for twenty-seven sessions, on a firm dollar, 2002-high US yields, Gulf peace hopes and faster smelter restarts. "
 "The curve softened (an $11.00 contango) but visible stock still drew. Scenario weights move to 15% bull / 48% base / 37% bear and the base range is lowered to $3,050-3,300; the daily Elliott count is re-labelled bearish (a C-wave decline from 3,374), with 3,061.5 the next reference and 3,289 the new invalidation.")

d['so_what']={"line":"Aluminium fell about 2.5% on the first October LME official and broke its August low, as a stronger dollar, the highest US yields since 2002, Gulf peace hopes and faster smelter restarts outweighed still-falling LME stock - the July low near $3,060 is now the level to watch.",
 "points":[
 f"WHAT MOVED: the 01-October LME official settled cash at $3,120.00 (-$84.00, -{abs(pc):.2f}%) and three-month at $3,131.00 (-$79.00, -{abs(pm):.2f}%), the lowest since early July. The contango widened to $11.00 from $6.00 and LME stock still drew 750 t to 240,625 t.",
 "WHY: public reporting cites US-Iran ceasefire hopes that could free Gulf metal flows, a dollar at its highest since March 2025, and US ten-year yields above 5.3% intraday. Supply is recovering: Alba has restarted lines 4-6 (about 1.3 Mt operating, SMM) and Macquarie cut its 2026 deficit view to 820,000 t and sees a 2027 surplus.",
 "THE OTHER SIDE: Brent rose to about $102.7 on reported tanker attacks in Hormuz and US carrier deployments, which raises smelter power costs and keeps Gulf logistics fragile; Asian premiums are still falling (Q4 Japanese offer $280/t, settlement expected lower).",
 "WHAT TO WATCH: Friday's weekly close against 3,261 (three-month is $130 below), the 3,061.5 July low ($69.50 away), a daily settlement back above 3,289 (which would negate the new bearish count), the Q4 MJP settlement, and Chinese inventory when markets reopen on 09-October."]}

new_feed=[
 {"when":"Fri 02-Oct 03:40 London","impact":"Bearish","text":f"BOARD ROLLED TO THE THURSDAY 01-OCTOBER LME OFFICIAL. Cash $3,120.00 (-$84.00), three-month $3,131.00 (-$79.00, -{abs(pm):.2f}%), contango $11.00 from $6.00, stock 240,625 t (-750). Three-month broke the 3,183 August low on an official settlement. Verified on cache-busted English and German overviews in exact agreement, per-metal tables and five-for-five stock reconciliation."},
 {"when":"Thu 01-Oct","impact":"Bearish","text":"REUTERS VIA BUSINESS RECORDER: ALUMINIUM AT A TWO-MONTH LOW ON IRAN PEACE HOPES AND A STRONGER DOLLAR; LME three-month near $3,146 after the official, low $3,141, lowest since 28-July."},
 {"when":"Thu 01-Oct","impact":"Bearish","text":"MACQUARIE (VIA DISCOVERY ALERT): 2026 ALUMINIUM DEFICIT CUT TO 820,000 T FROM 940,000 T ON A FASTER EGA AL TAWEELAH RESTART; 410,000 T SURPLUS FORECAST FOR 2027; price averages $3,325 (2026) and $3,050 (2027)."},
 {"when":"Wed 30-Sep","impact":"Bearish","text":"SMM: ALBA LINES 4-6 RESUMED, OPERATING CAPACITY ABOUT 1.3 MT; Middle East operating capacity back to about 4.5-5.0 Mt and global operating capacity ex-China about 29.65 Mt."},
 {"when":"Thu 01-Oct","impact":"Mixed","text":"RIO TINTO BELL BAY (TASMANIA, ~190,000 T/Y) SECURED TO 31-DECEMBER-2031 under new power and government-support agreements - removes a closure risk to existing supply rather than adding new supply."},
 {"when":"Fri 02-Oct","impact":"Mixed","text":"ENERGY AND RATES: Brent above $102 after two sessions of gains on reported tanker attacks in Hormuz and a possible third US carrier deployment; dollar index about 102.0, highest since March 2025; US ten-year 5.26% after topping 5.3% (Trading Economics)."},
]
d['feed']=(new_feed+d['feed'])[:12]

new_news=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":f"LME ALUMINIUM BREAKS ITS AUGUST LOW ON THE FIRST OCTOBER OFFICIAL. The 01-October official settled cash at $3,120.00 (-{abs(pc):.2f}%) and three-month at $3,131.00 (-{abs(pm):.2f}%), beneath the 3,183 swing low of 20-August and the lowest three-month official since early July. The contango widened to $11.00 while visible stock drew 750 t to 240,625 t. All five base metals fell on the session."},
 {"theme":"Macro / geopolitics","horizon":"Immediate","impact":"Bearish","url":S_BR,
  "headline":"ALUMINIUM AT A TWO-MONTH LOW ON IRAN PEACE HOPES AND A STRONGER DOLLAR (Reuters via Business Recorder, 01-October). LME three-month traded near $3,146 after touching $3,141, the lowest since 28-July; BNP Paribas' David Wilson: 'There's some sensitivity for aluminium there, in terms of flows of material through the Gulf.' Inflation, debt concerns and weaker sentiment also weighed."},
 {"theme":"Balance","horizon":"3-12 months","impact":"Bearish","url":S_DAO,
  "headline":"MACQUARIE CUTS ITS 2026 ALUMINIUM DEFICIT TO 820,000 T FROM 940,000 T AND FORECASTS A 410,000 T SURPLUS IN 2027 (via Discovery Alert, 01/02-October), citing a faster-than-expected EGA Al Taweelah restart (315 of 1,262 cells restored by late August, full production targeted Q1-2027). Price forecasts: $3,325/t average for 2026 and $3,050/t for 2027."},
 {"theme":"Supply","horizon":"1-3 months","impact":"Bearish","url":S_SMMX,
  "headline":"ALBA RESTARTS LINES 4-6 (SMM, 30-September): operating capacity about 1.3 Mt; Middle East operating capacity back to about 4.5-5.0 Mt and global operating capacity ex-China about 29.65 Mt. Overseas September output was still down 2.4% year on year, but average daily output rose 2.2% month on month; several Q4 projects are delayed, so growth should moderate."},
 {"theme":"Supply","horizon":"3-12 months","impact":"Mixed","url":S_BB,
  "headline":"RIO TINTO'S BELL BAY SMELTER SECURED TO 2031 (01-October): Rio Tinto, the Australian federal government and Tasmania agreed continued Hydro Tasmania power and government support, keeping about 190,000 t/y of output running to 31-December-2031. It removes a closure risk rather than adding supply."},
 {"theme":"Energy / geopolitics","horizon":"1-3 months","impact":"Mixed","url":S_TEB,
  "headline":"BRENT ABOVE $102 (Trading Economics, 02-October) after two sessions of gains as the US weighs a third carrier group for the Gulf; at least three tankers were reported attacked transiting Hormuz this week, though crude flows have largely recovered. Higher energy lifts smelter costs; it sits awkwardly against the peace-hope narrative in metals."},
 {"theme":"Macro","horizon":"1-3 months","impact":"Bearish","url":S_TED,
  "headline":"DOLLAR AT ITS HIGHEST SINCE MARCH 2025: the index rose a fourth session to about 102.0 (Trading Economics, 02-October), with markets fully pricing another 25bp Fed hike this year; the US ten-year topped 5.3% on Thursday before easing to about 5.26%. A firmer dollar raises the cost of dollar-priced metal for non-dollar buyers."},
 {"theme":"Alumina","horizon":"1-3 months","impact":"Mixed","url":S_ALC,
  "headline":"LME ALUMINA (PLATTS) ROSE 1.50% TO $360.40/T ON 30-SEPTEMBER (AL Circle) even as aluminium fell; the Asian reference price fell 1.38% to $3,169.50. Live LME aluminium warrants were 226,675 t and cancelled warrants 14,700 t."},
]
d['news']=new_news+d['news'][:12]

cats=d['outlook']['catalysts']
for c in cats:
    if c['date']=='Daily, from Thu 01-Oct':
        c['date']='Resolved Thu 01-Oct'; c['impact']='High'
        c['event']="THE 3,183 DAILY INVALIDATION BROKE ON AN OFFICIAL SETTLEMENT: three-month settled $3,131.00 on 01-October, $52.00 beneath the 20-August swing low that had held for twenty-seven sessions. The constructive daily Elliott count is invalidated and re-labelled bearish (a C-wave decline from 3,374)."
    if c['date']=='Fri 02-Oct':
        c['event']="THE WEEKLY CLOSE TEST AT 3,261 ON THREE-MONTH. Three-month settled $3,131.00 on 01-October, $130.00 below the level. A WEEKLY close beneath 3,261 - the likely outcome barring a $130 recovery in one session - shifts weight materially towards the weekly alternate (the move off 3,061.5 was corrective) and the bear scenario."
cats.insert(0,{"date":"Daily, from Fri 02-Oct","impact":"High","event":"THE 3,061.5 JULY LOW AND THE 3,289 NEW INVALIDATION. Three-month settled $3,131.00, $69.50 above the 02-July low at 3,061.5 (and the 50% weekly retracement at 3,077). A daily official settlement beneath 3,061.5 opens the 2,950-3,000 area; a daily settlement back above 3,289 negates the new bearish daily count."})
d['outlook']['catalysts']=cats

RK=d['outlook']['risks']
RK[0]['risk']=RK[0]['risk']+" UPDATE 02-OCTOBER: the contango widened $5.00 to $11.00 on 01-October as the price fell. Still small; trend held at FLAT."
RK[1]['risk']=RK[1]['risk']+" UPDATE 02-OCTOBER: the dollar index reached its highest since March 2025 and the ten-year topped 5.3% intraday; markets fully price another 25bp hike this year (Trading Economics). Trend held at UP."
RK[4]['risk']=RK[4]['risk']+" UPDATE 02-OCTOBER: LME stock drew 750 t to 240,625 t after five unchanged sessions. Trend held at FLAT."
RK[7]['trend']='up'
RK[7]['risk']=RK[7]['risk']+" UPDATE 02-OCTOBER: Brent rose above $102, up about 7.5% over the month, on reported Hormuz tanker attacks and US carrier deployments (Trading Economics). Trend moved from FLAT to UP."
RK[8]['risk']=RK[8]['risk']+" UPDATE 02-OCTOBER: no Q4 settlement publicly reported yet; offer $280/t, settlement expected lower (SMM, 30-September). Trend held at DOWN."
RK[9]['risk']=RK[9]['risk']+" UPDATE 02-OCTOBER: at least three tankers reported attacked in Hormuz this week and a third US carrier group under consideration, while metals markets priced Iran peace hopes the same day - the signals conflict. Arrow stays UP."
RK[10]['risk']=RK[10]['risk']+" UPDATE 02-OCTOBER: Alba lines 4-6 back (about 1.3 Mt operating, SMM) and Macquarie cites a faster EGA restart in cutting its 2026 deficit to 820,000 t. Trend held at UP."

SC={'Bull':('15%','$3,350-3,700'),'Base':('48%','$3,050-3,300'),'Bear':('37%','$2,880-3,050')}
for s in d['outlook']['scenarios']:
    p,t=SC[s['case']]; s['prob']=p; s['target']=t
    s['drivers']=("MOVED 02-OCTOBER (from 18/52/30): three-month broke the pre-registered 3,183 daily invalidation on an official settlement ($3,131.00), the dollar is at a 2025 high, Gulf restarts are accelerating and Macquarie now forecasts a 2027 surplus; weight shifts toward the bear case and the base range is lowered. Still constructive: LME stock drawing and energy costs rising. PRIOR: "+s['drivers'].split(' PRIOR: ',1)[-1])
sp=d['outlook']['scenario_paths']
sp['labels']=['Now','Nov-26','Dec-26','Mar-27','Jun-27']
sp['bull']=[3131.0,3300,3450,3600,3700]; sp['base']=[3131.0,3150,3200,3250,3280]; sp['bear']=[3131.0,3020,2960,2910,2880]

d['outlook']['ai_analysis'].insert(0,f"THE CENTRAL FACT OF THIS RUN IS THAT THE 3,183 FLOOR BROKE. The 01-October official settled three-month at $3,131.00 (-{abs(pm):.2f}%) and cash at $3,120.00, beneath the 20-August swing low that had held for twenty-seven sessions. All five base metals fell and the dollar firmed, so the trigger was broad and macro-led; aluminium fell most as public reporting points to an unwinding Gulf-supply premium on peace hopes and faster restarts (Alba lines 4-6, EGA).")
d['outlook']['ai_analysis'].insert(1,"THE BALANCE OF PUBLIC EVIDENCE HAS TILTED BEARISH BUT NOT ONE-WAY: Macquarie trims its 2026 deficit to 820,000 t and sees a 2027 surplus, premiums keep resetting lower, and the contango is widening; against that, visible LME stock is still drawing and Brent above $102 lifts smelter costs. The 3,061.5 July low is the next objective test; a daily settlement back above 3,289 would negate the new bearish count.")

for b in d['outlook']['balance']:
    if b['year']=='2026':
        b['label']="UPDATE 02-OCTOBER: Macquarie revised its 2026 deficit to 820,000 t from 940,000 t and forecasts a 410,000 t surplus in 2027, citing the faster EGA Al Taweelah restart (via Discovery Alert). "+b['label']
found=False
for c in d['outlook']['consensus']:
    if c['source'].startswith('Macquarie'):
        c['source']='Macquarie (Oct-26)'; c['y2026']='$3,325'; c['y2027']='$3,050'; c['note']="Via Discovery Alert, 01/02-October-2026: 2026 deficit cut to 820 kt (from 940 kt); 2027 surplus of 410 kt; faster EGA Al Taweelah restart"; found=True
if not found:
    d['outlook']['consensus'].append({'source':'Macquarie (Oct-26)','y2026':'$3,325','y2027':'$3,050','note':"Via Discovery Alert, 01/02-October-2026: 2026 deficit cut to 820 kt (from 940 kt); 2027 surplus of 410 kt; faster EGA Al Taweelah restart"})

for l in d['logistics']:
    if l['name']=='Strait of Hormuz transit':
        l['val']="CONSTRAINED AND CONTESTED. At least three tankers reported attacked transiting the strait this week; US weighing a third carrier group; crude flows largely recovered; no US-Iran agreement"
        rest=l['note'].split(' PRIOR: ',1)[-1]
        l['note']=("REVIEWED FRIDAY 02-OCTOBER-2026. Trading Economics (02-October) reports at least three tankers attacked while transiting the Strait of Hormuz this week, Iran and Houthi allies targeting regional refineries, and the US weighing a third aircraft-carrier strike group and up to 10,000 troops, while crude flows have largely recovered to pre-conflict levels. The same day metals reporting (Reuters via Business Recorder) cited US-Iran ceasefire hopes. No container or bulk transit count is published because tracker figures remain disputed. Arrow stays UP. PRIOR: "+rest)
        l['src']="REVIEWED FRIDAY 02-OCTOBER-2026: Trading Economics Brent 02-Oct-2026 ("+S_TEB+"); Business Recorder 01-Oct-2026 ("+S_BR+"). PRIOR: "+l['src'].split(' PRIOR: ',1)[-1]

for m in d['macro']:
    if m['name'].startswith('Brent'):
        m['value']='102.66'; m['day']="+0.34% early 02-October after two sessions of gains (Trading Economics front-month); +7.47% over the month"
        m['note']="REFRESHED FRIDAY 02-OCTOBER-2026 AT ABOUT 03:40 LONDON on a public reference board (Trading Economics), which cites reported tanker attacks in Hormuz and possible additional US carrier deployment. Energy is a major smelter cash-cost line. Used nowhere in the LME board, premium panel or input basket."
    elif m['name'].startswith('US dollar index'):
        m['value']='102.037'; m['day']="+0.01% early 02-October after a fourth straight gain; +3.16% over the month; highest since March 2025 (Trading Economics)"
        m['note']="REFRESHED FRIDAY 02-OCTOBER-2026 on a public reference board (Trading Economics). A firmer dollar raises the cost of dollar-priced metal for non-dollar buyers."
    elif m['name'].startswith('US 10-year'):
        m['value']='5.26'; m['day']="+2bp early 02-October; topped 5.3% on 01-October, highest since early 2002, before easing (Trading Economics)"
        m['note']="REFRESHED FRIDAY 02-OCTOBER-2026 on a public reference board (Trading Economics). Higher yields raise the cost of carrying metal and financing inventory."
    elif m['name']=='EUR/USD':
        m['value']='1.13050'; m['day']="LME fixing on 01-October, -0.41% from 1.13510; ECB fixing 1.12980, BFIX 1.13080"
        m['note']="REFRESHED FRIDAY 02-OCTOBER-2026 to the 01-October LME fixing via Westmetall, the same session as the LME board."

OLD="REVIEWED 01-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE FOR THIS SPECIFIC ASSET IN THIS WINDOW - none was located in Wednesday trading or early Thursday Asian hours - so"
NEW="REVIEWED 02-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE FOR THIS SPECIFIC ASSET IN THIS WINDOW - none was located in Thursday trading or early Friday Asian hours - so"
newps=[]
for r in d['producer_status']:
    r['asof']=RD
    r['update']=r['update'].replace(OLD,NEW)
    if r['name'].startswith('Aluminium Bahrain'):
        r['update']="UPDATED 02-OCTOBER: SMM (30-September) reports Alba lines 4-6 have resumed production, bringing operating capacity to about 1.3 million tonnes, and Middle East operating capacity back to about 4.5-5.0 Mt. "+r['update'].replace(NEW,"PRIOR STATUS:")
        r['src']=["SMM - Restoration for one smelter in Middle East initially completed (30-Sep-2026)",S_SMMX]
    if r['name'].startswith('EGA'):
        r['update']="UPDATED 02-OCTOBER: Macquarie (via Discovery Alert, 01/02-October) cut its 2026 global deficit estimate to 820,000 t citing a faster-than-expected Al Taweelah restart - 315 of 1,262 cells restored by late August, about 18% of capacity by mid-August, full production targeted Q1-2027 per the company. "+r['update'].replace(NEW,"PRIOR STATUS:")
        r['src']=["Discovery Alert - aluminium market outlook October 2026 (Macquarie, EGA restart progress)",S_DAO]
    if r['name'].startswith('Century Aluminum'):
        r={"name":"Rio Tinto (RIO) - Bell Bay, Tasmania","status":"SECURED TO 31-DECEMBER-2031 - new agreements with the Australian federal and Tasmanian governments provide continued Hydro Tasmania power and government support; about 190,000 t/y, ~550 direct jobs","impact":"Medium - removes a closure risk to existing Australian supply; adds no new capacity","update":"NEW ROW 02-OCTOBER (replaces the Century Aluminum row, whose last public update dated from Q1-2026): agreements announced 01-October-2026.","src":["Mining Technology - Bell Bay Aluminium to continue operations until 2031 (01-Oct-2026)",S_BB],"asof":RD}
    newps.append(r)
d['producer_status']=newps

for s in [["Westmetall - LME official prices and stocks, 01-Oct-2026 session (EN+DE)",W],
          ["Business Recorder (Reuters) - aluminium falls to 2-month low on Iran peace hopes, stronger dollar (01-Oct-2026)",S_BR],
          ["Discovery Alert - aluminum market outlook October 2026 (Macquarie balance revision)",S_DAO],
          ["AL Circle - LME aluminium cash bid, LME alumina Platts $360.40 (01-Oct-2026)",S_ALC],
          ["SMM - Middle East smelter restoration, Alba lines 4-6 (30-Sep-2026)",S_SMMX],
          ["Mining Technology - Bell Bay Aluminium to continue to 2031 (01-Oct-2026)",S_BB],
          ["Trading Economics - Brent crude (02-Oct-2026)",S_TEB],
          ["Trading Economics - US 10-year yield (02-Oct-2026)",S_TEY],["Trading Economics - US dollar index (02-Oct-2026)",S_TED]]:
    d['sources'].append(s)
d['outlook']['sources'].append(["Discovery Alert - Macquarie 2026 deficit 820 kt, 2027 surplus 410 kt (Oct-2026)",S_DAO])
d['outlook']['sources'].append(["Business Recorder (Reuters) - aluminium 2-month low (01-Oct-2026)",S_BR])

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE 01-OCTOBER-2026 LME OFFICIAL. This page compiled at about 03:40 London on FRIDAY 02-October, before the 13:20 official, so Thursday 01-October is the latest published session and the correct current figure.")
C[1]=("THE COMPLETENESS TEST PASSES: the per-metal daily tables for aluminium and copper show 01-October as the newest row with 30-September unchanged as the prior row; the other three metals reconcile through the cache-busted overviews and stock arithmetic.")
C[2]=("THE ENGLISH AND GERMAN OVERVIEWS WERE BOTH RE-REQUESTED CACHE-BUSTED AND AGREE EXACTLY on 01-October across all six metals, stocks and FX fixings.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against the levels carried for 30-September: aluminium -750 to 240,625; copper -1,325 to 248,075; nickel -216 to 284,682; zinc +2,375 to 123,975; lead -750 to 356,600.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (01-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart now use the October cash average-to-date (a single session, 01-October) as their latest point. Post-official third-party marks (Business Recorder about $3,146; Discovery Alert intraday low about $3,112; Trading Economics reference about $3,148) are reported in text only and never used on the board.")
C[6]=("PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND NO NEW PUBLIC ASSESSMENT WAS LOCATED FOR THIS WINDOW; every premium row is carried at its own assessment date. No Q4-2026 Japanese quarterly settlement has been publicly reported; SMM (30-September) reports the offer cut to $280/t and the market expecting a settlement below that. The chart's pending band remains the reported offer range ($280-310/t).")
for i,c in enumerate(C):
    if c.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent, the dollar index and the US ten-year are early-Friday 02-October reference marks (Trading Economics); EUR/USD is the 01-October LME fixing; European gas TTF is carried at its last reference session. Hormuz transit counts remain disputed, so none is published; tanker-attack reports are as published by Trading Economics and are not independently verified here.")
    if c.startswith("PEER EARNINGS ARE IN A LULL"):
        C[i]=("PEER EARNINGS ARE IN A LULL AND NO COMPANY WAS BACK-FILLED THIS RUN (02-October). The Q3-2026 reporting season opens in mid-October; existing earnings_history entries are unchanged and carry only exact publicly verified figures.")
    if c.startswith("THE ELLIOTT WAVE PANELS"):
        C[i]=c.split(' UPDATE 02-OCTOBER:')[0]+" UPDATE 02-OCTOBER: the daily count was RE-LABELLED this run on its stated invalidation (a daily official settlement beneath 3,183); the weekly count is unchanged pending Friday's weekly close."

ew=d['ew']; ew['updated']=RD
st=ew['short_term']
assert st['line'][-1]==[0.99206,3210.0], st['line'][-1]
st['line'].append([0.9978,3131.0])
st['now_x']=0.9985
st['ymin']=2900
st['yticks']=[3000,3200,3400,3600,3800]
st['proj']={"bull":[[0.9985,3131.0],[0.9992,3220],[1.0,3290]],
            "base":[[0.9985,3131.0],[0.9992,3100],[1.0,3150]],
            "bear":[[0.9985,3131.0],[0.9992,3060],[1.0,2980]]}
for w in st['waves']:
    if w['p']==3374.0: w['w']="B - corrective rally COMPLETE (re-labelled 02-Oct; formerly (1))"
    if w['p']==3183.0: w['w']="(i) of C - broken 01-Oct (formerly (2))"
st['waves'].append({"t":0.9337,"p":3289.0,"w":"(ii) of C - new invalidation"})
st['waves'].sort(key=lambda w:w['t'])
st['fib']=[
 {"l":"3,289 - the 12-September (ii) high and the NEW INVALIDATION of the bearish daily count. A daily official settlement above it negates the C-wave count. It is $158.00 above the 01-October three-month.","p":3289.0,"k":"res"},
 {"l":"3,261 - the shared 38.2% weekly retracement, held at the SAME price as the weekly panel. Three-month is $130.00 beneath it into Friday 02-October's weekly close.","p":3261.0,"k":"res"},
 {"l":"3,183 - the 20-August low, BROKEN on the 01-October official ($3,131.00). Now first resistance on any rebound.","p":3183.0,"k":"key"},
 {"l":"3,061.5 - the 02-July C low and the next objective support, shared with the weekly panel (50% weekly retracement at 3,077). $69.50 beneath three-month.","p":3061.5,"k":"deep"}]
st['fwd_pivots']=[
 {"t":0.9992,"p":3061.5,"w":"FIRST TEST BELOW: the 3,061.5 July low (and 3,077, the weekly 50% retracement), $69.50 beneath the 01-October three-month. A daily official settlement beneath it extends wave (iii) of C towards the 2,980 area (1.618 x wave (i) projected from 3,289)."},
 {"t":0.9996,"p":3289.0,"w":"THE NEW INVALIDATION: 3,289, the 12-September (ii) high. A DAILY OFFICIAL SETTLEMENT ABOVE IT negates the bearish C-wave count and restores the possibility that the 3,061.5-3,374 advance was the first leg of a new uptrend."}]
for a in st['annos']:
    if a['text'].startswith('(2) 3,183'): a['text']='(i) 3,183 - broken 01-Oct'
    if a['text'].startswith('(1)/v 3,374'): a['text']='B 3,374 - corrective high'
st['annos'].append({"t":0.9337,"p":3289.0,"dy":-9,"text":"(ii) 3,289 - invalidation","anchor":"end"})
st['writeup']=("DAILY (SWING DEGREE) - THE CONSTRUCTIVE COUNT IS INVALIDATED AND RE-LABELLED ON THE STATED RULE. The pre-registered invalidation was a daily official settlement beneath the 3,183 low of 20-August; on 01-October three-month settled $3,131.00, so the advance from 3,061.5 to 3,374 can no longer be wave (1) of an impulse with (2) at 3,183. "
 "NEW BASE CASE, ABOUT 60%: the 3,061.5-3,374 rally was a corrective B wave and a C-wave decline is underway from 3,374, with (i) at 3,183, (ii) at 3,289 on 12-September and (iii) now in progress; the cardinal rules hold - (ii) did not exceed the 3,374 origin and (iii) is already extending beyond (i). Targets: the 3,061.5 July low first, then about 2,980 where (iii) equals 1.618 times (i). "
 "ALTERNATE, ABOUT 40%: a deep expanded flat or double-three in which price holds above 3,061.5 and the uptrend resumes later; it needs a quick recovery above 3,183. "
 "INVALIDATION OF THE NEW COUNT: a daily official settlement above 3,289, $158.00 above the 01-October three-month. CONFIDENCE IS MODERATE; the break came on a broad, dollar-led session rather than aluminium-specific news. This is technical context, not advice.")
lt=ew['long_term']
lt['fwd_pivots'][0]['w']=("THE 3,261 LEVEL - THE 38.2% RETRACEMENT OF THE 3,855-TO-3,061.5 DECLINE - IS THE WEEKLY TEST, AND IT IS TESTED ON THE WEEKLY CLOSE. Friday 25-September's weekly close held it at $3,267.00. On Thursday 01-October three-month settled $3,131.00, $130.00 beneath it, and the daily count broke the 3,183 low. FRIDAY 02-OCTOBER'S WEEKLY CLOSE: a close beneath 3,261, now likely, shifts weight materially to the weekly alternate in which the move off 3,061.5 was corrective.")
lt['fwd_pivots'][1]['w']=("THE NEXT OVERHEAD POSITION-DEGREE OBJECTIVE IS THE 23.6% RETRACEMENT AT 3,488, $357.00 above the 01-October three-month official of $3,131.00. The downside references are unchanged and shared with the daily panel: the 50% retracement at 3,077 (held on the 3,061.5 low of 02-July), now $54.00 beneath three-month, and the 61.8% at 2,894, where the bear path terminates. The 2,950-3,110 support zone is unchanged and price is approaching its upper edge.")
lt['writeup']=("WEEKLY (POSITION DEGREE) - THE COUNT IS UNCHANGED PENDING FRIDAY'S WEEKLY CLOSE, BUT WEIGHT HAS SHIFTED. The 3,855 high of 02-June terminates the position-degree advance; the decline into 3,061.5 on 02-July is a completed A-B-C, and the 50% retracement at 3,077 held. "
 "THE CONSTRUCTIVE CASE, CUT TO ABOUT 55% (from about 70%): price is building a new position-degree advance off 3,061.5, which requires 3,061.5 to hold; targets 3,488, then 3,680 and 3,840 into mid-2027. "
 "THE ALTERNATE, RAISED TO ABOUT 45%: the move off 3,061.5 was corrective - a B wave or the opening leg of a larger fourth wave - and the decline now under way breaks the 2,950-3,110 zone towards the 61.8% retracement at 2,894. The daily break of 3,183 on 01-October (three-month $3,131.00) is consistent with it. "
 "INVALIDATION: a WEEKLY close beneath 3,261 (Friday 02-October, likely) re-opens the alternate formally, and a weekly close beneath 3,077 invalidates the constructive count outright. CONFIDENCE IS LOW-TO-MODERATE. This is technical context, not advice.")
lt['proj']={"bull":[[0.66,3131.0],[0.76,3400],[0.88,3600],[1.0,3800]],"base":[[0.66,3131.0],[0.78,3150],[0.9,3250],[1.0,3300]],"bear":[[0.66,3131.0],[0.8,2980],[1.0,2890]]}

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-09-30', ph['rows'][-1]
ph['rows'][-1]=['2026-10-01',cash,m3,stk]
ph['updated']=RD
ph['basis']=("London Metal Exchange official settlements via Westmetall. LME Aluminium official cash settlement, official 3-month, and LME warehouse stock. Weekly sampling (last published official session of each week). AT THE 02-OCTOBER-2026 UPDATE the row for the week of 28-September is replaced with the 01-October session (cash 3,120.00, 3-month 3,131.00, stock 240,625 t); it will be replaced by Friday's session when it publishes. Compiled at about 03:40 London on Friday 02-October, before that day's 13:20 official. Verified against both cache-busted Westmetall language overviews and the per-metal aluminium daily table.")
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok', d['metals_board'], mh['al'][-1], mh['zn'][-1], mh['pb'][-1], round(tl,2), round(share,1), round(ratio,2))
