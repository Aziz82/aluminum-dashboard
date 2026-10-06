# Daily data refresh - 2026-10-01 (THURSDAY, compiled ~03:40 London, BEFORE the ring). MONTH ROLL: September closed.
# Board ROLLED to WEDNESDAY 30-Sep LME official (month-end). EN+DE cache-busted agree; per-metal tables show 30-Sep newest row.
import json
P='market_data.json'
d=json.load(open(P,encoding='utf-8'))
RD='2026-10-01'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TEA="https://tradingeconomics.com/commodity/aluminum"
S_DA="https://discoveryalert.com/news/metals-market-snapshot-q3-september-2026/"
S_MJP="https://news.metal.com/newscontent/104142880-smm-analysis-overseas-primary-aluminum-market-quiet-as-market-awaits-q4-mjp-settlement"
S_ALW="https://news.metal.com/newscontent/104142604-30000-mt-alumina-traded-at-369mt-fob-western-australia-for-november-2026-shipment"
S_KED="https://in.investing.com/news/commodities-news/aluminium-falls-as-smelter-restarts-improve-global-supply-outlook-further-today-5609985"
S_TEB="https://tradingeconomics.com/commodity/brent-crude-oil"
S_TEC="https://tradingeconomics.com/commodity/crude-oil"
S_TEY="https://tradingeconomics.com/united-states/government-bond-yield"
S_TED="https://tradingeconomics.com/united-states/currency"
S_ALC="https://www.alcircle.com/news/changes-in-aluminium-ingot-and-billet-inventory-before-and-after-national-day-2020-2026-121328"

# ---- September 2026 full-month official tables (Westmetall per-metal tables, 22 sessions, 01-30 Sep) ----
AL_C=[3261.0,3255.5,3303.0,3292.5,3310.0,3325.0,3352.0,3343.0,3274.0,3311.0,3260.0,3310.0,3303.5,3285.0,3262.5,3242.0,3240.0,3228.0,3254.0,3248.5,3225.5,3204.0]
AL_M=[3261.0,3253.5,3303.5,3293.0,3308.0,3319.0,3338.0,3318.0,3250.0,3257.0,3236.0,3289.0,3285.0,3282.0,3273.0,3264.0,3260.0,3252.5,3267.0,3252.0,3232.0,3210.0]
AL_S=[246725,246225,245975,244525,244525,244525,244525,244350,244100,243850,243600,243600,242600,242600,242200,242125,241375,241375,241375,241375,241375,241375]
CU_C=[14395.5,14355.0,14359.0,14371.0,14540.0,14737.0,14672.0,14390.0,14238.5,14044.0,14045.0,14227.0,14400.5,14529.0,14788.0,14797.0,14735.0,14765.0,14740.0,14544.5,14474.5,14487.0]
NI_C=[16350,16530,16615,16690,16600,16675,16675,16630,16270,16205,16135,16090,16170,16055,16125,16410,16430,16320,16050,16050,15860,15860]
ZN_C=[4115.0,4000.0,3995.5,4087.0,4157.0,4110.0,4186.0,4105.0,4015.0,3951.0,3922.0,3937.0,3941.0,4010.0,4018.0,4006.0,3949.0,3981.0,4060.0,3957.0,3977.0,3954.0]
PB_C=[1874,1873,1870,1871,1875,1859,1871,1870.5,1854,1834,1829,1848,1862,1868,1890,1909,1885.5,1900,1902.5,1886,1876,1856]
for L in (AL_C,AL_M,AL_S,CU_C,NI_C,ZN_C,PB_C): assert len(L)==22
mean=lambda L: sum(L)/len(L)
sep_c=round(mean(AL_C),2); sep_m=round(mean(AL_M),2); sep_s=round(mean(AL_S)); sep_sp=round(mean([c-m for c,m in zip(AL_C,AL_M)]),2)
sep_cu=round(mean(CU_C),2); sep_ni=round(mean(NI_C),2); sep_zn=round(mean(ZN_C),2); sep_pb=round(mean(PB_C),2)

cash,prev_c,m3,prev_m,stk=3204.0,3225.5,3210.0,3232.0,241375
spr=cash-m3

VER=("COMPILED THURSDAY 01-OCTOBER-2026 AT ABOUT 03:40 LONDON, BEFORE THURSDAY'S RING. THE BOARD ROLLED THIS RUN TO THE WEDNESDAY 30-SEPTEMBER-2026 (MONTH-END) LONDON METAL EXCHANGE OFFICIAL, WHICH IS THE LATEST PUBLISHED SESSION; THURSDAY'S OFFICIAL PRINTS AT 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted English and German Westmetall overviews AGREE EXACTLY on 30-September across all six metals, all six stock lines and the foreign-exchange fixings; (2) the per-metal daily tables for aluminium, copper, nickel, zinc and lead all show 30-September as the newest row with 29-September reproduced unchanged as the prior row; "
 "(3) ALL FIVE STOCK LINES RECONCILE against the levels carried for 29-September: aluminium 241,375 unchanged; copper 250,475 less 1,075 to 249,400; nickel 284,898 unchanged; zinc 123,550 less 1,950 to 121,600; lead 357,550 less 200 to 357,350 - FIVE FOR FIVE. "
 "The whole board sits on ONE UNIFORM SESSION (30-September) and no intraday, closing, reference or contract-for-difference mark is used anywhere in it. THE MONTH HAS ROLLED: every prior-month average on this page now uses the COMPLETED SEPTEMBER-2026 official means (22 sessions), recomputed from the per-metal tables. NEXT OFFICIAL: THURSDAY 01-OCTOBER, 13:20 LONDON.")

AL=(f" CASH SETTLED $3,204.00 ON THE 30-SEPTEMBER OFFICIAL, DOWN $21.50 OR 0.67% FROM $3,225.50. THREE-MONTH SETTLED $3,210.00, DOWN $22.00 OR 0.68% FROM $3,232.00. "
 "SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS, MARGINALLY: three-month fell $0.50 more than cash, so the CONTANGO NARROWED $0.50 TO $6.00 from $6.50 while the price fell - the curve is effectively unchanged and close to flat. "
 "VISIBLE LME STOCK WAS UNCHANGED AT 241,375 TONNES FOR A FIFTH CONSECUTIVE SESSION (the per-metal table shows the level unchanged since 23-September). "
 f"THE MONTH CLOSED WEAK: September's official cash mean was ${sep_c:,.2f} and three-month ${sep_m:,.2f}; the month-end cash settlement is ${sep_c-cash:,.2f} below the September mean and the lowest official cash of the month. Public commentary (Trading Economics, 30-September) cites improving supply from smelter restarts, rising Chinese exports and a firmer dollar. "
 "THREE-MONTH SETTLED $51.00 BELOW THE 3,261 LEVEL on a DAILY official and $27.00 ABOVE the 3,183 daily invalidation; the weekly test of 3,261 is set on Friday 02-October's close.")

d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,204.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,210.0","pos":False,"delta":VER+AL+" THREE-MONTH FELL A THIRD SESSION AND IS NOW $51.00 BELOW THE 3,261 RETRACEMENT on a daily settlement - the fifth daily close beneath it in six sessions - and only $27.00 above the 3,183 daily invalidation. A third-party report (Discovery Alert) records a post-official 30-September close near $3,160, beneath 3,183; this is NOT an official settlement and Trading Economics' reference quote showed about $3,209 on the same day, so the sources disagree and no Elliott label is changed on it."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-6.0","pos":False,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,204.00 against three-month $3,210.00 is a $6.00 CONTANGO, NARROWED $0.50 from $6.50. Spread and flat price moved in OPPOSITE directions on this ring (price down, contango marginally tighter), but the change is negligible. The published reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"241,375","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK UNCHANGED AT 241,375 TONNES FOR A FIFTH CONSECUTIVE SESSION. September's mean stock was {sep_s:,} tonnes and the level fell 5,350 tonnes across the month (246,725 on 01-September). Public commentary describes LME stock as near a 36-year low (Kedia Advisory via Investing.com), but there has been no fresh draw since 23-September."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN ROLLED from the August mean ($3,249.63) to the completed SEPTEMBER-2026 official cash mean."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,210.00, DOWN $22.00 OR 0.68% FROM $3,232.00. AVERAGE COLUMN ROLLED to the completed September-2026 official three-month mean of ${sep_m:,.2f} (22 sessions; August was $3,251.23); three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":241375,"avg":sep_s,"note":VER+f" STOCK UNCHANGED AT 241,375 TONNES FOR A FIFTH CONSECUTIVE SESSION. AVERAGE COLUMN ROLLED to the September-2026 mean of {sep_s:,} tonnes (August 251,215). Level about {sep_s-stk:,} tonnes below the September mean."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-6.5,"avg":sep_sp,"note":VER+f" A $6.00 CONTANGO, NARROWED $0.50 FROM $6.50. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN ROLLED to the September-2026 mean spread of ${sep_sp:,.2f} (August -$1.60). Flat price and spread moved in OPPOSITE directions on this ring, negligibly. PUBLISHED REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1351,"prev":1.1352,"avg":1.1465,"note":VER+" THE LME EURO FIXING EASED TO 1.13510 FROM 1.13520; the ECB fixing printed 1.13550 and BFIX 1.13506, so all three agree. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source this run; it is labelled rather than estimated. Public commentary (Trading Economics, 01-October) ties dollar strength to Treasury yields at their highest since 2002."},
]

d['outlook']['forward_path']=[
 {"tenor":"Cash (30-Sep official - latest published)","price":"3,204.0","basis":"THE 30-SEPTEMBER-2026 (MONTH-END) OFFICIAL CASH SETTLEMENT OF $3,204.00, DOWN $21.50 OR 0.67%. The lowest official cash of September. Thursday's official prints at 13:20 London."},
 {"tenor":"3-month (30-Sep official - latest published)","price":"3,210.0","basis":"THE 30-SEPTEMBER-2026 OFFICIAL THREE-MONTH OF $3,210.00, DOWN $22.00 OR 0.68%, $51.00 below 3,261 and $27.00 above 3,183 on daily settlements; the weekly test is Friday 02-October's close."},
 {"tenor":"Cash-to-3M structure","price":"-6.0 (CONTANGO)","basis":"A $6.00 CONTANGO, narrowed $0.50 from $6.50. Flat price and spread moved in OPPOSITE directions, negligibly; the curve is near flat."},
 {"tenor":"Visible LME stock","price":"241,375 t","basis":f"UNCHANGED for a fifth consecutive session; September mean {sep_s:,} t; down 5,350 t across September."},
]
d['outlook']['curve_note']=("THE CURVE IS FLAT AND STILL. On the 30-September official cash $3,204.00 sits $6.00 BELOW three-month $3,210.00, a CONTANGO narrowed $0.50 from $6.50. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50 and now $6.00. "
 f"READ: both legs fell almost one-for-one, so the price weakness is not coming from the prompt date - there is no sign of either a spot squeeze or a glut at the front. The September mean spread was ${sep_sp:,.2f}. The published reversal condition (a backwardation beyond $15.00) remains far away and visible stock has not drawn for five sessions.")

ls=d['lme_series']; assert ls[-1][0]=='29-Sep', ls[-1]
d['lme_series']=ls[1:]+[["30-Sep",cash,m3,stk]]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":14455.0,"day":round((14455/14448-1)*100,2),"ytd":round((14455/12511-1)*100,2)},
 {"name":"Nickel","price":16060.0,"day":round((16060/16085-1)*100,2),"ytd":round((16060/16915-1)*100,2)},
 {"name":"Zinc","price":3842.0,"day":round((3842/3871-1)*100,2),"ytd":round((3842/3130.5-1)*100,2)},
 {"name":"Lead","price":1890.0,"day":round((1890/1907-1)*100,2),"ytd":round((1890/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*3210/3232,1); mh['cu'][-1]=round(mh['cu'][-1]*14455/14448,1); mh['ni'][-1]=round(mh['ni'][-1]*16060/16085,1)
zn21=mean(ZN_C[:21]); pb21=mean(PB_C[:21])
mh['zn'][-1]=round(mh['zn'][-1]*sep_zn/zn21,1); mh['pb'][-1]=round(mh['pb'][-1]*sep_pb/pb21,1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',14487.0),('NI',15860.0),('ZN',3954.0),('PB',1856.0)): R[k]=R[k][1:]+[v]
ms['asof']='2026-09-30'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending WEDNESDAY 30-SEPTEMBER-2026 (month-end). THE WINDOW ROLLED THIS RUN: 09-September dropped and 30-September appended, so the window is 10-September to 30-September. Every point is an official cash settlement, verified against the cache-busted Westmetall English and German overviews, which agree to the cent, the per-metal daily tables, and five-for-five stock-line reconciliation. Thursday's official prints at 13:20 London, after this page compiles.")
ms['src']=["Westmetall - LME official cash settlements, EN and DE overviews cache-busted and in exact agreement (30-September-2026 session)",W]

AVGNOTE=" AVERAGE COLUMN ROLLED THIS RUN: it is now the completed SEPTEMBER-2026 mean of official cash (22 sessions, recomputed from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",14487.0,14455.0,sep_cu," COPPER WAS THE ONLY METAL TO RISE ON CASH: cash $14,487.00, up $12.50 or 0.09%; three-month $14,455.00, up $7.00. The BACKWARDATION edged out to $32.00 from $26.50. Stock drew 1,075 tonnes to 249,400. "+f"September cash mean ${sep_cu:,.2f} (August $14,353.40)."),
 ("Nickel",15860.0,16060.0,sep_ni," NICKEL: cash $15,860.00, UNCHANGED (the per-metal table confirms the identical print on 29 and 30 September); three-month $16,060.00, down $25.00. The CONTANGO NARROWED from $225.00 to $200.00, still the widest carry on the board. Stock unchanged at 284,898 tonnes. "+f"September cash mean ${sep_ni:,.2f} (August $16,765.75)."),
 ("Zinc",3954.0,3842.0,sep_zn," ZINC: cash $3,954.00, down $23.00 or 0.58%; three-month $3,842.00, down $29.00. The BACKWARDATION widened to $112.00 from $106.00, the tightest front on the board, on a 1,950-tonne draw to 121,600. Zinc remains the strongest metal on this board year to date. "+f"September cash mean ${sep_zn:,.2f} (August $3,875.13)."),
 ("Lead",1856.0,1890.0,sep_pb," LEAD: cash $1,856.00, down $20.00 or 1.07%; three-month $1,890.00, down $17.00. CONTANGO widened $3.00 to $34.00. Stock drew 200 tonnes to 357,350 - an eighth consecutive draw, still without the front paying for immediacy. Lead remains the weakest metal on this board year to date. "+f"September cash mean ${sep_pb:,.2f} (August $1,855.05)."),
]
CROSS=(" CROSS-METAL, REPORTED AS DATA NOT AS A REGIME SIGNAL: at month-end three-month prices fell in four of five metals (copper the exception, +$7.00), with the dollar steady (LME euro fixing 1.1351 from 1.1352). Fronts were mixed: aluminium contango -$0.50, nickel contango -$25.00, lead contango +$3.00, copper backwardation +$5.50, zinc backwardation +$6.00.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":a,"src":VER+AVGNOTE+txt+CROSS,"src_url":W} for (n,c,m,a,txt) in MD]

OLDH="COMPILED WEDNESDAY 30-SEPTEMBER-2026 AT ABOUT 03:45 LONDON, BEFORE WEDNESDAY'S RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN)."
NEWH="COMPILED THURSDAY 01-OCTOBER-2026 AT ABOUT 03:40 LONDON, BEFORE THURSDAY'S RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY)."
for i in d['inputs']:
    if isinstance(i.get('src'),str): i['src']=i['src'].replace(OLDH,NEWH)
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='29-Sep'
        i['hist']=i['hist'][1:]+[["30-Sep",14487.0]]
        i['val']="~14,455.00 (3M); 14,487.00 (cash) $/t"
        i['ratio']="~14,487.00 $/t cash vs LME 3M 14,455.00 $/t"
        i['trend']='flat'
        i['src']=("LME official cash settlement, rolled to the 30-SEPTEMBER-2026 (month-end) session at $14,487.00, UP $12.50 or 0.09% against $14,474.50. THE WINDOW ROLLED THIS RUN: 09-September dropped and 30-September appended, so the series is the last fifteen published official cash sessions, 10-September to 30-September - the same window as the LME Board sparklines. Official settlement only, verified on the cache-busted Westmetall English and German overviews, which agree to the cent, and the per-metal daily table. "
                  f"September cash mean ${sep_cu:,.2f}. Copper structure for context: backwardation $32.00 (from $26.50), stock drew 1,075 t to 249,400 t.")
d['inputs_summary']=("UPDATE 01-OCTOBER: copper rolled to the 30-September (month-end) LME official cash of $14,487.00, up $12.50, with its fifteen-session window moved to 10-September to 30-September. No other input mark printed in this window - China entered its 01-08 October National Day holiday, so the SMM fluoride, silicon and magnesium weeklies are not expected until after 08-October, and the carbon settlement cycle (anodes, pitch, green coke) is mid-October - so every other row is carried at its own dated public mark and no value was interpolated. PRIOR RUN: "+d['inputs_summary'])

for r in d['raw_materials']:
    if isinstance(r.get('src'),str): r['src']=r['src'].replace(OLDH,NEWH)
ratio=363.6/m3*100
ALNOTE=("COMPILED THURSDAY 01-OCTOBER-2026 AT ABOUT 03:40 LONDON. ONE NEW DATED PUBLIC ALUMINA TRADE PRINTED INTO THIS WINDOW: SMM reports that on 30-September 30,000 tonnes of alumina traded at $369/t FOB Western Australia for November shipment - above the $355/t FOB Western Australia level SMM cited a day earlier. It is a single reported transaction on a different basis from the FOB East Australia trade row, which stays carried at its 18-September mark rather than being overwritten. "
 "The SMM alumina index is carried at its 30-September print of 2,669.99 yuan/tonne; SHFE is closed 01-08 October, so no domestic index update is expected until after the holiday. "
 f"THE RATIO: LME Alumina (Platts-settled) at $363.60/t (carried at its own date) against the 30-September aluminium three-month of $3,210.00 is {ratio:.2f}%, against a decade norm of 15-17%; it rose slightly because the metal fell. Alumina remains historically CHEAP relative to metal.")
for a in d['alumina']:
    a['src']=ALNOTE

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
PREM=("COMPILED THURSDAY 01-OCTOBER-2026 AT ABOUT 03:40 LONDON. PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND THIS PANEL CARRIES EACH ROW AT ITS OWN LAST PUBLIC ASSESSMENT DATE. NO NEW PUBLIC PREMIUM ASSESSMENT WAS LOCATED FOR THIS WINDOW, so every row is CARRIED UNCHANGED. ONE NEGOTIATION DATA POINT: SMM (30-September) reports a major producer's Q4 MJP offer lowered to $280/t from $310/t, with the market expecting the final Q4 settlement BELOW $280/t; this is an offer, not a settlement, and no row is changed on it. "
 f"THE TARIFF DECOMPOSITION IS REFRESHED DAILY BY DESIGN: on a re-verified Section 232 rate of 50% on aluminium articles applied to full customs value, the tariff leg of the US duty-paid premium is 0.50 times the 30-September official cash of $3,204.00, or ${tl:,.2f}, DOWN $10.75 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}% of the US duty-paid premium is policy arithmetic rather than market. "
 "This page does NOT fabricate freight, financing or tightness splits for any premium row.")
for p in d['premiums']:
    s=p['src']; j=s.find("for any premium row.")
    if s.startswith("COMPILED WEDNESDAY") and j>0: p['src']=PREM+s[j+len("for any premium row."):]
    else: p['src']=PREM+" "+s

d['premium_settlement_src']=["Japanese quarterly P1020A premium settlements - Q4-2026 pending; SMM 30-Sep-2026: Q4 offer lowered to $280/t from $310/t, settlement expected below $280/t",S_MJP]
po=d['premium_outlook']
if isinstance(po,str):
    d['premium_outlook']=("UPDATE 01-OCTOBER: THE Q4-2026 JAPANESE QUARTERLY SETTLEMENT IS STILL PENDING AT THE START OF THE QUARTER IT PRICES. SMM reports (30-September) that a major producer cut its Q4 MJP offer to $280/t from $310/t and that the market expects the final settlement BELOW $280/t, with Korean and Thai spot demand described as subdued to very weak. The pending band carried on the chart remains the publicly reported OFFER range of $280-310/t with v set to null; on the SMM read the eventual settlement may print beneath that band, which would be a fall of more than 29% from the Q3 record of $395/t. PRIOR: "+po)

pdv=d['premium_drivers'][0]
pdv['t']="The Q4 Japanese negotiation has moved further in the buyer's favour"
pdv['d']=("SMM reports on 30-September that a major producer lowered its Q4 MJP offer to $280/t from $310/t and that the market now expects the final Q4 settlement below $280/t, against a Q3 settlement of $395/t. Regional spot demand was described as very subdued in South Korea and very weak in Thailand. WHY IT LANDS ON PREMIUMS: the quarterly MJP is the reference for much Asian physical business, so a settlement below $280 would reset the regional premium level downward for the quarter. Meanwhile the LME curve is flat (a $6.00 contango on 30-September), offering no exchange-side signal of scarcity.")
pdv['src']=["SMM - overseas primary aluminium market quiet as market awaits Q4 MJP settlement (30-September-2026)",S_MJP]

d['lme_commentary']=("ALUMINIUM CLOSED SEPTEMBER AT THE MONTH'S LOWEST OFFICIAL. On the 30-September official cash settled $3,204.00, down $21.50 or 0.67%, and three-month $3,210.00, down $22.00 or 0.68%. Both legs fell almost equally, so the contango narrowed only $0.50 to $6.00 - spread and flat price nominally in OPPOSITE directions, but the curve is in practice unchanged and flat. "
 f"Visible stock was unchanged at 241,375 tonnes for a fifth session. September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}; the month-end print is ${sep_c-cash:,.2f} beneath the cash mean. Public commentary (Trading Economics) continues to cite smelter restarts, Chinese aluminium exports up 17.2% year on year in August, and a firmer dollar. "
 "A third-party report (Discovery Alert) puts the post-official 30-September close near $3,160, the lowest since 29-July and beneath the 55-day moving average, and cites Marex support at $3,100-3,125; Trading Economics' reference quote was about $3,209, so the sources disagree and the board uses only the official. "
 "Across the complex three-month fell in four of five metals; copper alone edged up. China's markets are shut 01-08 October.")
d['net_read']=("NET: BEARISH ON PRICE, NEUTRAL ON STRUCTURE. Against: September closed at its lowest official, three-month is $51.00 beneath 3,261 and only $27.00 above the 3,183 daily invalidation, visible LME stock has not drawn for five sessions, and the US ten-year is near 5.31% - its highest since 2002 per Trading Economics - with the dollar index near 101.6. Public commentary keeps pointing to restarts and Chinese exports. "
 "Constructive: the curve is flat rather than in a widening contango, LME stock is still described as near a 36-year low, and alumina remains cheap relative to metal. Energy is firm rather than falling (Brent about $98 on 01-October per Trading Economics) as Hormuz flows recover only partially and US-Iran talks remain at an impasse, with Tehran saying it received a US proposal on reopening the strait.")
d['commercial']=("COMMERCIAL READ - GENERIC AND PUBLIC. FIRST, THE CURVE STILL PAYS BUYERS LITTLE TO WAIT: a $6.00 contango is close to flat, so the carry argument for deferring purchases is weak while the flat price drifts lower. SECOND, ASIAN PREMIUMS ARE RESETTING LOWER: public reporting (SMM, 30-September) has the Q4 MJP offer cut to $280/t and the market expecting a settlement below that, against $395/t in Q3. THIRD, THE TARIFF ARITHMETIC MOVED WITH THE METAL: "
 f"on a verified 50% Section 232 rate, the tariff leg of the US Midwest duty-paid premium is ${tl:,.2f} on 30-September cash, {share:.1f}% of the $2,403/t premium. FOURTH, WATCH THE CALENDAR: Friday 02-October sets the weekly close against 3,261; China is on holiday 01-08 October, when public records (AL Circle) show ingot stock has built in every year since 2020. This is generic public market context, not advice.")
d['bottom_line']=("BOTTOM LINE: aluminium closed September at the month's lowest LME official - cash $3,204.00 (-0.67%), three-month $3,210.00 (-0.68%) - with the curve flat (a $6.00 contango) and visible stock unchanged for a fifth session. "
 f"The September official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}, now the reference averages on this page. Macro remains a headwind (US ten-year near 5.31%, a 2002 high; DXY near 101.6), and Asian premiums are softening into an unsettled Q4 MJP. Scenario weights are held at 18% bull / 52% base / 30% bear pending Friday's weekly close against 3,261, with three-month now $51.00 beneath it and $27.00 above the 3,183 daily invalidation.")

d['so_what']={"line":"Aluminium ended September at its lowest LME official of the month as supply-restart headlines, a firm dollar and 2002-high US yields weighed; the curve is flat, so this is a price move rather than a physical squeeze or glut - Friday's weekly close against 3,261 and the 3,183 floor are the tests.",
 "points":[
 "WHAT MOVED: the 30-September LME official settled cash at $3,204.00 (-$21.50, -0.67%) and three-month at $3,210.00 (-$22.00, -0.68%). The contango barely changed ($6.00 from $6.50) and LME stock was unchanged at 241,375 t for a fifth session.",
 f"THE MONTH: September averaged ${sep_c:,.0f} cash and ${sep_m:,.0f} three-month on the LME official; month-end is about ${sep_c-cash:,.0f} below the cash average. These are now the reference averages on the dashboard.",
 "WHY: public commentary cites smelter restarts, Chinese exports up 17.2% year on year in August, and a firm dollar as US ten-year yields reached about 5.3%, the highest since 2002. In Asia, the Q4 Japanese premium offer was cut to $280/t from $310/t and the market expects settlement below that (SMM).",
 "WHAT TO WATCH: Friday 02-October's weekly close against 3,261 (three-month is $51 below); whether the 3,183 daily level holds ($27 away); the unsettled Q4 MJP; and Chinese inventory after the 01-08 October holiday."]}

new_feed=[
 {"when":"Thu 01-Oct 03:40 London","impact":"Bearish","text":"BOARD ROLLED TO THE WEDNESDAY 30-SEPTEMBER (MONTH-END) LME OFFICIAL. Cash $3,204.00 (-$21.50), three-month $3,210.00 (-$22.00), contango $6.00 from $6.50, stock 241,375 t unchanged for a fifth session. Verified on cache-busted English and German overviews in exact agreement, per-metal tables and five-for-five stock reconciliation. Monthly averages rolled to September."},
 {"when":"Wed 30-Sep","impact":"Bearish (premium)","text":"SMM: Q4 MJP OFFER LOWERED TO $280/T FROM $310/T; the market expects the final Q4 settlement below $280/t. Korean trade very subdued, Thai demand very weak."},
 {"when":"Wed 30-Sep","impact":"Mixed","text":"SMM: 30,000 T OF ALUMINA TRADED AT $369/T FOB WESTERN AUSTRALIA FOR NOVEMBER SHIPMENT."},
 {"when":"Wed 30-Sep / Thu 01-Oct","impact":"Mixed","text":"ENERGY AND RATES: Brent steadied near $98 on 01-October as Hormuz flows climbed to 13.2 million b/d and Tehran said it received a US proposal on reopening the strait (Trading Economics). US ten-year near 5.31%, highest since 2002; softer August PCE (+0.3%) cut October Fed-hike odds to about 38% from 51%."},
]
d['feed']=(new_feed+d['feed'])[:12]

new_news=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":S_TEA,
  "headline":f"LME ALUMINIUM ENDED SEPTEMBER AT THE MONTH'S LOWEST OFFICIAL. The 30-September official settled cash at $3,204.00 (-0.67%) and three-month at $3,210.00 (-0.68%); the contango was near-flat at $6.00. September averaged ${sep_c:,.2f} cash. Trading Economics cites smelter restarts, Chinese exports up 17.2% year on year in August and a firmer dollar on hawkish Fed comments; it shows the price down about 2.1% over the month."},
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":S_DA,
  "headline":"THIRD-PARTY REPORT: ALUMINIUM SLID TO A TWO-MONTH LOW TO END Q3. Discovery Alert reports a 30-September close near $3,160 (-1.7%), the lowest since 29-July and beneath the 55-day moving average, and cites Marex support at $3,100-3,125 where systematic selling could accelerate. This is a post-official close and differs from Trading Economics' reference quote (about $3,209); the official settlement was $3,210.00 three-month."},
 {"theme":"Premiums","horizon":"1-3 months","impact":"Bearish (premium)","url":S_MJP,
  "headline":"Q4 JAPANESE PREMIUM: A MAJOR PRODUCER CUT ITS OFFER TO $280/T FROM $310/T, AND THE MARKET EXPECTS SETTLEMENT BELOW $280/T (SMM, 30-SEPTEMBER). The Q3 settlement was $395/t. Korean trade was very subdued and Thai demand very weak; participants are waiting for the Q4 outcome to guide further negotiations."},
 {"theme":"Alumina","horizon":"1-3 months","impact":"Mixed","url":S_ALW,
  "headline":"ALUMINA SPOT TRADE AT $369/T FOB WESTERN AUSTRALIA: SMM reports 30,000 tonnes traded on 30-September for November shipment, above the $355/t level SMM cited a day earlier. Alumina remains cheap relative to metal at about 11.3% of LME three-month."},
 {"theme":"Supply","horizon":"1-3 months","impact":"Bearish","url":S_KED,
  "headline":"SUPPLY NARRATIVE: public commentary (Kedia Advisory via Investing.com, 29-September) cites several smelters restarting and ramping curtailed capacity; China's August output reached a record 3.98 million tonnes (+4.7% year on year) while global primary output fell 1.7% to 6.172 million tonnes and Gulf output fell 44% year on year in July. LME stock is described as near a 36-year low."},
 {"theme":"Macro","horizon":"1-3 months","impact":"Bearish","url":S_TEY,
  "headline":"US YIELDS AT A 2002 HIGH: the ten-year traded near 5.31% and the thirty-year near 5.64% on 01-October (Trading Economics), on energy-driven inflation and fiscal concerns. Softer August PCE (+0.3% vs 0.4% expected) cut October Fed-hike odds to about 38% from 51%. The dollar index rose to about 101.6 - a headwind for dollar-priced metals."},
 {"theme":"Geopolitics / energy","horizon":"1-3 months","impact":"Mixed","url":S_TEC,
  "headline":"HORMUZ: TEHRAN SAYS IT RECEIVED A US PROPOSAL ON REOPENING THE STRAIT (Trading Economics, 30-September), while flows through the strait climbed to 13.2 million b/d. Brent steadied near $98 on 01-October; OPEC+ is expected to hold November quotas. The impasse in US-Iran talks persists, so Gulf aluminium export logistics remain constrained."},
]
d['news']=new_news+d['news'][:13]

cats=d['outlook']['catalysts']
for c in cats:
    if c['date']=='Wed 30-Sep 13:20':
        c['date']='Resolved Wed 30-Sep'; c['impact']='Medium'
        c['event']=(f"THE MONTH-END OFFICIAL CLOSED SEPTEMBER WEAK: cash $3,204.00 and three-month $3,210.00, both the month's lowest; the contango narrowed only $0.50 to $6.00 and visible stock was unchanged for a fifth session. September means: cash ${sep_c:,.2f}, three-month ${sep_m:,.2f}; these rolled into the average column on 01-October.")
    if c['date']=='Fri 02-Oct':
        c['event']="THE WEEKLY CLOSE TEST AT 3,261 ON THREE-MONTH. Three-month settled $3,210.00 on 30-September, $51.00 below the level on a daily official. A WEEKLY close beneath 3,261 shifts weight materially towards the weekly alternate Elliott count and the bear scenario; a close above keeps the constructive count."
cats.insert(0,{"date":"Daily, from Thu 01-Oct","impact":"High","event":"THE 3,183 DAILY INVALIDATION. Three-month settled $3,210.00, only $27.00 above the 20-August swing low. A DAILY OFFICIAL SETTLEMENT beneath 3,183 invalidates the constructive daily Elliott count. A third-party post-official close near $3,160 on 30-September (Discovery Alert) is not an official settlement and is not used to resolve this test."})
cats.insert(1,{"date":"October (pending)","impact":"High","event":"Q4-2026 JAPANESE QUARTERLY PREMIUM SETTLEMENT. Offer cut to $280/t from $310/t; market expects settlement below $280/t (SMM, 30-September), against $395/t for Q3."})
d['outlook']['catalysts']=cats

RK=d['outlook']['risks']
RK[0]['risk']=RK[0]['risk']+" UPDATE 01-OCTOBER: the contango narrowed $0.50 to $6.00 on 30-September; curve effectively flat. Trend held at FLAT."
RK[1]['risk']=RK[1]['risk']+" UPDATE 01-OCTOBER: US ten-year near 5.31%, highest since 2002 (Trading Economics); October hike odds eased to about 38% after softer PCE. Trend held at UP."
RK[4]['risk']=RK[4]['risk']+" UPDATE 01-OCTOBER: LME stock unchanged at 241,375 t for a fifth session. Trend held at FLAT."
RK[7]['trend']='flat'
RK[7]['risk']=RK[7]['risk']+" UPDATE 01-OCTOBER: Brent steadied near $98 (Trading Economics), so the prior session's energy easing did not extend. Trend moved from DOWN to FLAT."
RK[8]['risk']=RK[8]['risk']+" UPDATE 01-OCTOBER: the Q4 offer was cut to $280/t and the market expects settlement below it (SMM, 30-September) - the downside premium reset is materialising. Trend held at DOWN (premium level falling)."
RK[9]['risk']=RK[9]['risk']+" UPDATE 01-OCTOBER: Tehran says it received a US proposal on reopening the strait and flows climbed to 13.2 million b/d, but no agreement exists. Arrow stays UP."
RK[10]['risk']=RK[10]['risk']+" UPDATE 01-OCTOBER: public commentary continues to cite restarts and ramp-ups as a driver of September's decline. Trend held at UP."

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 01-OCTOBER: September closed at its lowest official and three-month is $51.00 below 3,261 and $27.00 above 3,183, which leans further towards the bear case; but the pre-registered weekly test is Friday's close and the curve is flat, so no weight is moved before then. PRIOR: "+s['drivers'])
d['outlook']['ai_analysis'].insert(0,f"THE CENTRAL FACT OF THIS RUN IS THAT SEPTEMBER CLOSED AT ITS LOW. The 30-September official settled cash $3,204.00 and three-month $3,210.00, both the month's lowest, against September means of ${sep_c:,.2f} and ${sep_m:,.2f}. The curve stayed flat (a $6.00 contango) and visible stock was unchanged for a fifth session, so the decline is a flat-price move driven by macro and supply narrative rather than by the prompt date.")
d['outlook']['ai_analysis'].insert(1,"PREMIUMS ARE NOW FOLLOWING THE PRICE LOWER IN ASIA: the Q4 MJP offer has been cut to $280/t and SMM reports the market expects a settlement below that, against $395/t in Q3. Combined with 2002-high US yields and a firm dollar, the near-term balance of public evidence has tilted bearish; the 3,183 daily level is $27 away and is the next objective test.")

for l in d['logistics']:
    if l['name']=='Strait of Hormuz transit':
        l['val']="CONSTRAINED; NO AGREEMENT. Tehran says it received a US proposal on reopening (30-Sep); flows reported at 13.2 million b/d; US-Iran talks at an impasse"
        l['note']=("REVIEWED THURSDAY 01-OCTOBER-2026. Trading Economics reports on 30-September that Iran's government spokesperson said Tehran had received a US proposal regarding reopening the strait, and that flows through the Strait of Hormuz climbed to 13.2 million barrels per day; on 01-October it describes an ongoing impasse in US-Iran negotiations and uncertainty over whether the recovery is durable. Public reporting on 29-September recorded the US rejecting Iran's seven-day reopening plan. No container or bulk transit count is published because tracker figures remain disputed. Arrow stays UP. PRIOR: "+l['note'])
        l['src']="REVIEWED THURSDAY 01-OCTOBER-2026: Trading Economics crude oil 30-Sep-2026 ("+S_TEC+"); Trading Economics Brent 01-Oct-2026 ("+S_TEB+"). PRIOR: "+l['src']

for m in d['macro']:
    if m['name'].startswith('Brent'):
        m['value']='98.12'; m['day']="+0.02% early 01-October after rising in the previous session (Trading Economics front-month); +2.61% over the month. Trading Economics showed about $96.3 early on 30-September, so the reference rose about $1.8 across the session."
        m['note']="REFRESHED THURSDAY 01-OCTOBER-2026 AT ABOUT 03:40 LONDON on a public reference board (Trading Economics), which cites Hormuz flows at 13.2 million b/d against an ongoing US-Iran impasse, and OPEC+ expected to hold November quotas. Energy is a major smelter cash-cost line. Used nowhere in the LME board, premium panel or input basket."
    elif m['name'].startswith('US dollar index'):
        m['value']='101.575'; m['day']="+0.11% on 01-October, +1.99% over the month, as Treasury yields reached their highest since 2002 (Trading Economics)"
        m['note']="REFRESHED THURSDAY 01-OCTOBER-2026 on a public reference board (Trading Economics). A firmer dollar raises the cost of dollar-priced metal for non-dollar buyers."
    elif m['name'].startswith('US 10-year'):
        m['value']='5.31'; m['day']="+2bp on 01-October; highest since 2002, thirty-year near 5.64%; October Fed-hike odds about 38% (from 51%) after softer August PCE (Trading Economics)"
        m['note']="REFRESHED THURSDAY 01-OCTOBER-2026 on a public reference board (Trading Economics). Higher yields raise the cost of carrying metal and financing inventory."
    elif m['name']=='EUR/USD':
        m['value']='1.13510'; m['day']="LME fixing on 30-September, -0.01% from 1.13520; ECB fixing 1.13550, BFIX 1.13506"
        m['note']="REFRESHED THURSDAY 01-OCTOBER-2026 to the 30-September LME fixing via Westmetall, the same session as the LME board."

OLD="REVIEWED 30-SEPTEMBER. NO NEW DATED PUBLIC DISCLOSURE FOR THIS SPECIFIC ASSET IN THIS WINDOW - none was located in Tuesday trading or early Wednesday Asian hours - so"
NEW="REVIEWED 01-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE FOR THIS SPECIFIC ASSET IN THIS WINDOW - none was located in Wednesday trading or early Thursday Asian hours - so"
for r in d['producer_status']:
    r['asof']=RD
    r['update']=r['update'].replace(OLD,NEW)
    if r['name'].startswith('China operators'):
        r['update']="UPDATED 01-OCTOBER: China entered its 01-08 October National Day holiday and SHFE is closed; public seasonal records (AL Circle) show ingot stock builds during the holiday week every year. Public commentary (Kedia Advisory, 29-September) cites China's August output at a record 3.98 million tonnes. "+r['update']
        r['src']=["Kedia Advisory via Investing.com - aluminium falls as smelter restarts improve supply outlook (29-Sep-2026)",S_KED]
for s in [["Westmetall - LME official prices and stocks, 30-Sep-2026 session; per-metal September tables",W],
          ["Trading Economics - aluminium (30-Sep-2026)",S_TEA],
          ["Discovery Alert - metals market snapshot, Q3 end (30-Sep-2026)",S_DA],
          ["SMM - overseas primary aluminium market awaits Q4 MJP settlement (30-Sep-2026)",S_MJP],
          ["SMM - 30,000 mt alumina traded at $369/mt FOB WA (30-Sep-2026)",S_ALW],
          ["Kedia Advisory via Investing.com - smelter restarts and supply (29-Sep-2026)",S_KED],
          ["Trading Economics - Brent crude (01-Oct-2026)",S_TEB],
          ["Trading Economics - crude oil, Hormuz flows (30-Sep-2026)",S_TEC],
          ["Trading Economics - US 10-year yield (01-Oct-2026)",S_TEY],["Trading Economics - US dollar index (01-Oct-2026)",S_TED]]:
    d['sources'].append(s)
d['outlook']['sources'].append(["SMM - Q4 MJP offer cut to $280/t (30-Sep-2026)",S_MJP])
d['outlook']['sources'].append(["Discovery Alert - aluminium two-month low to end Q3 (30-Sep-2026)",S_DA])

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE 30-SEPTEMBER-2026 (MONTH-END) LME OFFICIAL. This page compiled at about 03:40 London on THURSDAY 01-October, before the 13:20 official, so Wednesday 30-September is the latest published session and the correct current figure.")
C[1]=("THE COMPLETENESS TEST PASSES: the per-metal daily tables for all five metals show 30-September as the newest row with 29-September unchanged as the prior row. Aluminium stock (241,375 t) and nickel cash ($15,860.00) and stock (284,898 t) are genuinely unchanged on the tables and are not carried values.")
C[2]=("THE ENGLISH AND GERMAN OVERVIEWS WERE BOTH RE-REQUESTED CACHE-BUSTED AND AGREE EXACTLY on 30-September across all six metals, stocks and FX fixings.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against the levels carried for 29-September: aluminium unchanged at 241,375; copper -1,075 to 249,400; nickel unchanged at 284,898; zinc -1,950 to 121,600; lead -200 to 357,350.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (30-September) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. The MONTH ROLLED this run: LME averages are the completed September-2026 official means recomputed from the 22-session per-metal tables; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the completed September monthly cash average as their latest point because no October session has printed yet. A third-party post-official close (Discovery Alert, about $3,160) and Trading Economics' reference quote (about $3,209) disagree and neither is used on the board.")
C[6]=("PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND NO NEW PUBLIC ASSESSMENT WAS LOCATED FOR THIS WINDOW; every premium row is carried at its own assessment date. No Q4-2026 Japanese quarterly settlement has been publicly reported; SMM reports the offer cut to $280/t and the market expecting a settlement below that. The chart's pending band remains the reported offer range ($280-310/t).")
for i,c in enumerate(C):
    if c.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent, the dollar index and the US ten-year are early-Thursday 01-October reference marks (Trading Economics); EUR/USD is the 30-September LME fixing; European gas TTF is carried at its last reference session. Hormuz transit counts remain disputed, so none is published; the 13.2 million b/d flow figure is Trading Economics' reported crude flow, not a vessel count.")
    if c.startswith("PEER EARNINGS ARE IN A LULL"):
        C[i]=("PEER EARNINGS ARE IN A LULL AND NO COMPANY WAS BACK-FILLED THIS RUN (01-October). The Q3-2026 reporting season opens in mid-October; existing earnings_history entries are unchanged and carry only exact publicly verified figures.")

ew=d['ew']; ew['updated']=RD
st=ew['short_term']
assert st['line'][-1]==[0.98632,3232.0], st['line'][-1]
st['line'].append([0.99206,3210.0])
st['now_x']=0.9978
st['proj']={"bull":[[0.9978,3210.0],[0.9985,3290],[0.9993,3370],[1.0,3440]],
            "base":[[0.9978,3210.0],[0.999,3245],[1.0,3290]],
            "bear":[[0.9978,3210.0],[0.999,3150],[1.0,3090]]}
st['fib'][0]['l']="(1) 3,374 - the 11-August impulse high and the next upside objective. It is $164.00 overhead on three-month after the 30-September session. A daily settlement above it confirms wave (3) is underway."
st['fib'][1]['l']="(2) 3,183 - the 20-August swing low and the HARD INVALIDATION. It has held for TWENTY-SEVEN sessions on official settlements and sits only $27.00 below the three-month official. A daily settlement beneath it invalidates the constructive daily count outright."
st['fib'][2]['l']="3,261 - the shared 38.2% retracement, held at the SAME price as the weekly panel. Three-month settled $3,210.00 on 30-September, $51.00 beneath it on a DAILY official - the fifth daily close below in six sessions. The weekly test is Friday 02-October's close."
st['fwd_pivots']=[
 {"t":0.9985,"p":3374.0,"w":"FIRST TEST OVERHEAD: 3,374, the wave (1) terminus, now $164.00 away on three-month after the 30-September official. A DAILY SETTLEMENT ABOVE IT confirms wave (3). Momentum is running the other way."},
 {"t":0.9992,"p":3183.0,"w":"THE HARD INVALIDATION: 3,183, the 20-August wave (2) low, held for twenty-seven sessions on official settlements and now only $27.00 beneath three-month. A third-party report puts a post-official 30-September close near $3,160; that is NOT an official settlement, so the count is not re-labelled on it, but the level is under direct attack. A DAILY OFFICIAL SETTLEMENT BENEATH IT invalidates the constructive daily count and forces a re-label at swing degree."}]
for a in st['annos']:
    if a['text'].startswith('(2) 3,183'): a['text']='(2) 3,183 - held 27 sessions, $27 away'
    if a['text'].startswith('(1)/v 3,374'): a['text']='(1)/v 3,374 - trigger, $164 away'
st['writeup']=("DAILY (SWING DEGREE) - THE COUNT IS UNCHANGED ON OFFICIAL SETTLEMENTS BUT IS NOW AT RISK. From the C low of 3,061.5 on 02-July an impulse completed at 3,374 on 11-August, labelled (1); the pullback to 3,183 on 20-August is labelled (2), held for twenty-seven sessions on official settlements. The cardinal rules still hold: (2) has not retraced beyond the origin of (1), no fourth wave overlaps a first, and wave 3 is not the shortest. "
 "THE BASE CASE IS NARROWED TO ABOUT 55%: wave (3) is still possible but unconfirmed; the trigger is a daily settlement above 3,374, now $164.00 above the 30-September three-month of $3,210.00, with 3,462 the target on confirmation. "
 "THE ALTERNATE IS RAISED TO ABOUT 45% (from about 40%): the move off 3,183 was corrective and a deeper (2) or a flat is unfolding towards the 3,100-3,125 support area that third-party technical commentary (Marex, via Discovery Alert) identifies; a month-end at the September low and a fifth daily close beneath 3,261 fit it. "
 "INVALIDATION: a daily OFFICIAL settlement beneath 3,183, now only $27.00 away, invalidates the count; a reported post-official close near $3,160 is noted but not used. CONFIDENCE IS LOW. This is technical context, not advice.")
lt=ew['long_term']
lt['fwd_pivots'][0]['w']=("THE 3,261 LEVEL - THE 38.2% RETRACEMENT OF THE 3,855-TO-3,061.5 DECLINE - IS THE WEEKLY TEST, AND IT IS TESTED ON THE WEEKLY CLOSE, NOT THE DAILY. Friday 25-September's weekly close held it at $3,267.00. On Wednesday 30-September three-month settled $3,210.00, $51.00 beneath it on a DAILY official, which is recorded but does not by itself change the weekly count. THE NEXT WEEKLY TEST IS FRIDAY 02-OCTOBER: a weekly close beneath 3,261 shifts weight materially towards the weekly alternate in which the move off 3,061.5 is corrective.")
lt['fwd_pivots'][1]['w']=("THE NEXT OVERHEAD POSITION-DEGREE OBJECTIVE IS THE 23.6% RETRACEMENT AT 3,488, $278.00 above the 30-September three-month official of $3,210.00. The deep downside references are unchanged and shared with the daily panel: the 50% retracement at 3,077, which held on the 3,061.5 low of 02-July, and the 61.8% at 2,894, where the bear path terminates. The 2,950-3,110 support zone is unchanged.")
lt['writeup']=("WEEKLY (POSITION DEGREE) - THE COUNT IS UNCHANGED AND THE SHARED PIVOTS ARE HELD AT THE SAME PRICES AS THE DAILY PANEL. The 3,855 high of 02-June terminates the position-degree advance; the decline into 3,061.5 on 02-July is a completed A-B-C, and the 50% retracement at 3,077 held. "
 "THE BASE CASE IS THAT PRICE IS BUILDING THE FIRST IMPULSE OF A NEW POSITION-DEGREE ADVANCE OFF 3,061.5, with targets at the 23.6% retracement of 3,488, then 3,680 and 3,840 into mid-2027. The last weekly close (25-September, $3,267.00) held the 3,261 test, but this week's daily settlements have fallen to $3,210.00, $51.00 beneath it, so the weekly close on Friday is likely to test it hard. "
 "THE ALTERNATE, held at roughly 30% against roughly 70% for the constructive count pending the weekly close, is that the move off 3,061.5 is corrective - a B wave or the opening leg of a larger fourth wave - pointing to a break of the 2,950-3,110 zone and ultimately the 61.8% retracement at 2,894. "
 "INVALIDATION: a WEEKLY close beneath 3,261 (Friday 02-October) re-opens the alternate, and a weekly close beneath 3,077 invalidates the constructive count outright. CONFIDENCE IS MODERATE-TO-LOW AND FALLING: September closed at its lowest official. This is technical context, not advice.")

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-09-29', ph['rows'][-1]
ph['rows'][-1]=['2026-09-30',cash,m3,stk]
ph['updated']=RD
ph['basis']=("London Metal Exchange official settlements via Westmetall. LME Aluminium official cash settlement, official 3-month, and LME warehouse stock. Weekly sampling (last published official session of each week). AT THE 01-OCTOBER-2026 UPDATE the row for the week of 28-September is replaced with the 30-September session (cash 3,204.00, 3-month 3,210.00, stock 241,375 t); it will be replaced by later sessions of the same week. Compiled at about 03:40 London on Thursday 01-October, before that day's 13:20 official. Verified against both cache-busted Westmetall language overviews and the per-metal aluminium daily table.")
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok', d['metals_board'], sep_c, sep_m, sep_s, sep_sp, sep_cu, sep_ni, sep_zn, sep_pb, mh['al'][-1], mh['zn'][-1], mh['pb'][-1])
