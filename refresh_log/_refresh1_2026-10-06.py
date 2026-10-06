# Daily data refresh - 2026-10-06 (TUESDAY, compiled ~05:35 London BEFORE the ring). Board ROLLED to MONDAY 05-Oct LME official.
# EN+DE cache-busted overviews agree exactly on 05-Oct; Al per-metal table shows 05-Oct newest (no later row), 02-Oct prior unchanged; 5/5 stock lines reconcile.
import json, re
P='market_data.json'
d=json.load(open(P,encoding='utf-8'))
RD='2026-10-06'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TEA="https://tradingeconomics.com/commodity/aluminum"
S_TED="https://tradingeconomics.com/united-states/currency"
S_TEY="https://tradingeconomics.com/united-states/government-bond-yield"
S_TEB="https://tradingeconomics.com/commodity/brent-crude-oil"
S_ALCI="https://www.alcircle.com/news/andhra-pradesh-backs-srikakulam-aluminium-smelter-plan-with-odisha-alumina-link-121414"
S_SMMQ="https://news.metal.com/newscontent/104143393-smm-flash-news-south32-revised-q4-26-cif-mjp-premium-offer-at-us265mt"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']

cash,prev_c,m3,prev_m,stk,prev_s=3107.0,3109.5,3118.0,3122.0,240375,240375
spr=cash-m3
pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100

VER=("COMPILED TUESDAY 06-OCTOBER-2026 BEFORE THE LONDON RING (~05:35 LONDON). THE BOARD ROLLED THIS RUN TO THE MONDAY 05-OCTOBER-2026 LONDON METAL EXCHANGE OFFICIAL, THE LATEST PUBLISHED SESSION; TODAY'S OFFICIAL DOES NOT PRINT UNTIL 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted English and German Westmetall overviews AGREE EXACTLY on 05-October across all six metals, all six stock lines and the foreign-exchange fixings; (2) the aluminium per-metal daily table shows 05-October as the newest row - NO ROW AFTER IT - with 02-October reproduced unchanged as the prior row; "
 "(3) ALL FIVE STOCK LINES RECONCILE against the levels carried for 02-October: aluminium 240,375 UNCHANGED; copper 248,650 less 3,750 to 244,900; nickel 285,168 less 198 to 284,970; zinc 123,750 PLUS 3,225 to 126,975; lead 354,175 less 2,700 to 351,475. "
 "The whole board sits on ONE UNIFORM SESSION (05-October) and no intraday, closing, reference or contract-for-difference mark is used anywhere in it. Prior-month averages remain the completed SEPTEMBER-2026 official means. NEXT OFFICIAL: TUESDAY 06-OCTOBER, 13:20 LONDON.")

AL=(f" CASH SETTLED $3,107.00 ON THE 05-OCTOBER OFFICIAL, DOWN $2.50 OR {abs(pc):.2f}% FROM $3,109.50. THREE-MONTH SETTLED $3,118.00, DOWN $4.00 OR {abs(pm):.2f}% FROM $3,122.00 - A THIRD LOWER SETTLEMENT AND ANOTHER MARGINAL LOW FOR THE MOVE, BUT THE SMALLEST DAILY DECLINE OF THE THREE. "
 "SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS: three-month fell $1.50 more than cash, so the CONTANGO NARROWED TO $11.00 from $12.50 even as the price eased - a small sign that prompt metal is not being pushed onto the market. "
 "VISIBLE LME STOCK WAS UNCHANGED AT 240,375 TONNES. Three-month now sits $56.50 above the 3,061.5 July low and $171.00 beneath the 3,289 daily invalidation. "
 "Macro stayed a headwind: the dollar index held near 102, close to its strongest since April 2025, and the US ten-year yield held near 5.32%, the highest since 2002 (Trading Economics, 06-October); Trading Economics attributes aluminium's slide to the firm dollar, expected smelter restarts and Chinese exports up about 17% year on year in August.")

d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,107.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,118.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $143.00 BELOW 3,261, $65.00 BELOW THE BROKEN 3,183 DAILY LEVEL, $171.00 BELOW THE 3,289 DAILY INVALIDATION, $41.00 above the 3,077 weekly 50% retracement and $56.50 above the 3,061.5 July low."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-11.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,107.00 against three-month $3,118.00 is an $11.00 CONTANGO, NARROWED $1.50 from $12.50. Spread and flat price moved in OPPOSITE directions on this ring (price down, contango narrower). The published reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"240,375","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK WAS UNCHANGED AT 240,375 TONNES after two consecutive small draws; it remains the low for the series on this page. September's mean stock was {sep_s:,} tonnes. Flat stock while price falls says the decline is macro- and supply-outlook-driven, not a visible physical glut."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,118.00, DOWN $4.00 OR {abs(pm):.2f}% FROM $3,122.00. AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK UNCHANGED AT 240,375 TONNES. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-12.5,"avg":sep_sp,"note":VER+f" AN $11.00 CONTANGO, NARROWED $1.50 FROM $12.50. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in OPPOSITE directions on this ring (price lower, contango narrower). PUBLISHED REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1206,"prev":1.1233,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.12060 FROM 1.12330 at the Monday ring; the ECB fixing printed 1.12040 and BFIX 1.12044, so all three agree on a slightly firmer dollar. Trading Economics (06-October) links euro weakness to political and fiscal uncertainty in Europe. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]

d['outlook']['forward_path']=[
 {"tenor":"Cash (05-Oct official)","price":"3,107.0","basis":f"THE 05-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,107.00, DOWN $2.50 OR {abs(pc):.2f}%. Next official Tuesday 06-October 13:20 London."},
 {"tenor":"3-month (05-Oct official)","price":"3,118.0","basis":f"THE 05-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,118.00, DOWN $4.00 OR {abs(pm):.2f}%: $143.00 beneath 3,261, $65.00 beneath the broken 3,183, $56.50 above the 3,061.5 July low."},
 {"tenor":"Cash-to-3M structure","price":"-11.0 (CONTANGO)","basis":"An $11.00 CONTANGO, narrowed $1.50 from $12.50. Flat price and spread moved in OPPOSITE directions."},
 {"tenor":"Visible LME stock","price":"240,375 t","basis":f"UNCHANGED on the session; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE CURVE FIRMED SLIGHTLY EVEN AS THE PRICE EDGED LOWER. On the 05-October official cash $3,107.00 sits $11.00 BELOW three-month $3,118.00, a CONTANGO narrowed $1.50 from $12.50. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50 and now $11.00. "
 f"READ: an orderly, narrow contango - not a glut signal, with visible stock flat at 240,375 t. The September mean spread was ${sep_sp:,.2f}. The published reversal condition (a backwardation beyond $15.00) remains far away; a contango beyond $24.50 would be the bearish structural confirmation.")

ls=d['lme_series']; assert ls[-1][0]=='02-Oct', ls[-1]
d['lme_series']=ls[1:]+[["05-Oct",cash,m3,stk]]
d['chart_price_axis']=[3000,3450]
d['chart_stock_axis']=[230000,255000]
CU=(14430.0,14366.0,14355.0,14320.0); NI=(15470.0,15690.0,15435.0,15625.0); ZN=(3774.0,3714.0,3798.0,3733.0); PB=(1829.5,1872.0,1827.0,1865.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# zn/pb 'now' = October cash average-to-date: 01-, 02- and 05-Oct sessions. Prior point was the two-session average.
zn_old=(3834.0+3798.0)/2; pb_old=(1837.0+1827.0)/2
zn_avg=(3834.0+3798.0+3774.0)/3; pb_avg=(1837.0+1827.0+1829.5)/3
mh['zn'][-1]=round(mh['zn'][-1]*zn_avg/zn_old,1); mh['pb'][-1]=round(mh['pb'][-1]*pb_avg/pb_old,1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])): R[k]=R[k][1:]+[v]
ms['asof']='2026-10-05'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending MONDAY 05-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 14-September dropped and 05-October appended, so the window is 15-September to 05-October. Every point is an official cash settlement, verified against the cache-busted Westmetall English and German overviews, which agree to the cent, the aluminium per-metal daily table (no row after 05-October), and five-for-five stock-line reconciliation. Next official Tuesday 06-October.")
ms['src']=["Westmetall - LME official cash settlements, EN and DE overviews cache-busted and in exact agreement (05-October-2026 session)",W]

AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,430.00, UP $75.00 or 0.52%; three-month $14,366.00, UP $46.00 or 0.32% - higher for a second session. The BACKWARDATION WIDENED to $64.00 from $35.00 while stock DREW 3,750 tonnes to 244,900, the largest draw on the board - prompt tightness firming. Public reporting continues to flag Chilean labour risk at Centinela and Escondida (mining.com via IMA, 29-30 September)."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,470.00, up $35.00 or 0.23%; three-month $15,690.00, up $65.00 or 0.42%. CONTANGO widened to $220.00 from $190.00, still the widest carry on the board. Stock drew 198 tonnes to 284,970."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,774.00, down $24.00 or 0.63%; three-month $3,714.00, down $19.00 or 0.51% - the only metal besides aluminium lower on the session. The BACKWARDATION narrowed to $60.00 from $65.00 and stock ROSE 3,225 tonnes to 126,975, the largest inflow on the board. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,829.50, up $2.50 or 0.14%; three-month $1,872.00, up $7.00 or 0.38%. CONTANGO widened $4.50 to $42.50. Stock drew 2,700 tonnes to 351,475, an eleventh consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL, REPORTED AS DATA NOT AS A REGIME SIGNAL: on the Monday 05-October official three-month prices rose in copper (+0.32%), nickel (+0.42%) and lead (+0.38%) and fell in aluminium (-0.13%) and zinc (-0.51%); the LME euro fixing eased to 1.1206 from 1.1233. A mixed, low-volatility session with China still on holiday.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

OLDH="COMPILED MONDAY 05-OCTOBER-2026, BEFORE THE LME RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY)."
NEWH="COMPILED TUESDAY 06-OCTOBER-2026, BEFORE THE LME RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY)."
n_rep=0
for i in d['inputs']:
    if isinstance(i.get('src'),str) and OLDH in i['src']: i['src']=i['src'].replace(OLDH,NEWH); n_rep+=1
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='02-Oct'
        i['hist']=i['hist'][1:]+[["05-Oct",CU[0]]]
        i['val']="~14,366.00 (3M); 14,430.00 (cash) $/t"
        i['ratio']="~14,430.00 $/t cash vs LME 3M 14,366.00 $/t"
        i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the MONDAY 05-OCTOBER-2026 session at $14,430.00, UP $75.00 or 0.52% against $14,355.00. THE WINDOW ROLLED THIS RUN: 14-September dropped and 05-October appended, so the series is the last fifteen published official cash sessions, 15-September to 05-October - the same window as the LME Board sparklines. Official settlement only, verified on the cache-busted Westmetall English and German overviews, which agree to the cent. "
                  "Copper structure for context: backwardation $64.00 (from $35.00), stock drew 3,750 t to 244,900 t.")
print('inputs header replaced', n_rep)
d['inputs_summary']=("UPDATE 06-OCTOBER (TUESDAY, PRE-RING): copper rolled to the Monday 05-October LME official cash of $14,430.00, up $75.00, with its fifteen-session window moved to 15-September to 05-October. No other input mark printed in this window - China remains on its 01-08 October National Day holiday, so the SMM fluoride, silicon and magnesium weeklies are not expected until after 08-October, and the carbon settlement cycle (anodes, pitch, green coke) is mid-October - so every other row is carried at its own dated public mark and no value was interpolated.")
nr=0
for r in d['raw_materials']:
    if isinstance(r.get('src'),str) and OLDH in r['src']: r['src']=r['src'].replace(OLDH,NEWH); nr+=1
print('raw header replaced', nr)

ratio=360.4/m3*100
ALNOTE=("COMPILED TUESDAY 06-OCTOBER-2026 (PRE-RING). NO NEW DATED PUBLIC ALUMINA MARK WAS LOCATED FOR THIS WINDOW: the LME Alumina (Platts) row stays at AL Circle's $360.40/t print of 30-September; the FOB East Australia trade row stays at its 18-September mark; SMM separately reported 30,000 t traded at $369/t FOB Western Australia on 30-September for November shipment (a different basis, reported in news only). The SMM alumina index is carried at its 30-September print of 2,669.99 yuan/tonne; SHFE is closed 01-08 October. "
 f"THE RATIO: LME Alumina at $360.40/t against the 05-October aluminium three-month of $3,118.00 is {ratio:.2f}%, against a decade norm of 15-17%. Alumina remains historically CHEAP relative to metal.")
for a in d['alumina']: a['src']=ALNOTE

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
PREM=("COMPILED TUESDAY 06-OCTOBER-2026 (PRE-RING). PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND THIS PANEL CARRIES EACH ROW AT ITS OWN LAST PUBLIC ASSESSMENT DATE. NO NEW PUBLIC PREMIUM ASSESSMENT WAS LOCATED FOR THIS WINDOW, so every row is CARRIED UNCHANGED. The Q4 MJP remains unsettled as of this run: SMM (30-September) and AL Circle (02-October) report Rio Tinto's offer cut to $280/t from $310/t and South32's offer at $265/t (revised down from $325/t, stated as valid to 05-October), with the market expecting a settlement below $280/t; no settlement had been publicly reported when this page compiled. These are offers, not a settlement. "
 f"THE TARIFF DECOMPOSITION IS REFRESHED DAILY BY DESIGN: on a re-verified Section 232 rate of 50% on aluminium articles applied to full customs value, the tariff leg of the US duty-paid premium is 0.50 times the 05-October official cash of $3,107.00, or ${tl:,.2f}, DOWN $1.25 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}% of the US duty-paid premium is policy arithmetic rather than market. "
 "This page does NOT fabricate freight, financing or tightness splits for any premium row.")
for p in d['premiums']:
    s=p['src']; j=s.find("for any premium row.")
    if s.startswith("COMPILED") and j>0: p['src']=PREM+s[j+len("for any premium row."):]
    else: p['src']=PREM+" "+s
pdv=d['premium_drivers'][0]
pdv['d']=("Q4 MJP OFFERS KEEP FALLING AND NO SETTLEMENT IS YET REPORTED: SMM (30-September) reports Rio Tinto's offer cut to $280/t from $310/t and South32's to $265/t from $325/t (stated as valid to 05-October); AL Circle (02-October) says the market expects settlement below $280/t, against a Q3 settlement of $395/t. No settlement had been publicly reported by 06-October. WHY IT LANDS ON PREMIUMS: the quarterly MJP is the reference for much Asian physical business, so a settlement in the $260s-270s would reset the regional premium level down by roughly 30% for the quarter. The LME curve offers no exchange-side scarcity signal either: an $11.00 contango on 05-October.")
pdv['src']=["SMM - South32 revised Q4-26 CIF MJP premium offer at US$265/mt",S_SMMQ]

d['lme_commentary']=(f"ALUMINIUM EDGED TO ANOTHER MARGINAL LOW AS SELLING FADED. On the Monday 05-October official cash settled $3,107.00, down $2.50 or {abs(pc):.2f}%, and three-month $3,118.00, down $4.00 or {abs(pm):.2f}% - a third lower settlement but the smallest of the three, after Thursday's 2.5% fall and Friday's $9. "
 "The contango NARROWED $1.50 to $11.00 while the price fell (spread and price in OPPOSITE directions) and visible stock was unchanged at 240,375 t. "
 "Macro remained a headwind: the dollar index held near 102, close to its strongest since April 2025, and the US ten-year yield held near 5.32%, the highest since 2002, while markets put about 78% odds on the Fed holding at its next meeting (Trading Economics, 06-October). Brent slipped toward $100 as Middle East crude exports recovered to about 98% of pre-war levels. "
 f"Copper, nickel and lead rose on the session; zinc fell with aluminium. China's markets are shut until 09-October. September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH ON PRICE, NEUTRAL-TO-SOFTER ON STRUCTURE, MOMENTUM FADING. Against: three-month made a third lower settlement and sits $143 under the 3,261 weekly level; the dollar and US yields remain near multi-year highs; Asian premium offers are down about 30% quarter on quarter; Gulf restarts are progressing and Chinese exports are elevated. "
 "Constructive: daily declines have shrunk from $80 to $9 to $4; the contango narrowed to $11.00 rather than widening; visible LME stock is flat at the low of the series (240,375 t); and the 3,061.5 July low ($56.50 away) has not yet been tested. Lower Brent (near $100) trims the energy cost floor at the margin.")
d['commercial']=("COMMERCIAL READ - GENERIC AND PUBLIC. FIRST, THE CURVE STILL PAYS BUYERS A LITTLE TO WAIT: an $11.00 contango, narrowed slightly on 05-October. SECOND, ASIAN PREMIUMS ARE RESETTING LOWER: public reporting has Q4 MJP offers at $265-280/t with settlement expected below $280/t, against $395/t in Q3; no settlement is yet reported. THIRD, THE TARIFF ARITHMETIC MOVED WITH THE METAL: "
 f"on a verified 50% Section 232 rate, the tariff leg of the US Midwest duty-paid premium is ${tl:,.2f} on 05-October cash, {share:.1f}% of the $2,403/t premium. FOURTH, WATCH THE CALENDAR: a Q4 Japanese premium settlement could come any day; the 3,061.5 July low is the next technical reference; China returns from holiday on 09-October. This is generic public market context, not advice.")
d['bottom_line']=(f"BOTTOM LINE: aluminium settled on the 05-October LME official at cash $3,107.00 and three-month $3,118.00, down {abs(pm):.2f}% - a third lower settlement but with the decline fading. "
 "The contango narrowed to $11.00 and visible stock held at 240,375 t. Scenario weights are held at 14% bull / 47% base / 39% bear; the daily Elliott count (a C-wave decline from 3,374) is unchanged, with 3,061.5 the next reference and 3,289 the invalidation; the weekly alternate remains preferred at about 55%.")

d['so_what']={"line":"Aluminium slipped to another marginal low for the move on Monday, but the selling is fading and the curve firmed slightly - the strong dollar and near-record US yields keep pressure on, with the July low near $3,060 still the key test.",
 "points":[
 f"WHAT MOVED: Monday's LME official settled cash at $3,107.00 (-$2.50) and three-month at $3,118.00 (-$4.00, -{abs(pm):.2f}%), the smallest of three straight declines; the contango narrowed to $11.00 from $12.50 and LME stock was unchanged at 240,375 t.",
 "WHY: the dollar index is holding near 102, close to its strongest since April 2025, and the US ten-year yield is near 5.32%, the highest since 2002; expected smelter restarts and Chinese exports up about 17% year on year in August add supply-side pressure (Trading Economics).",
 "PREMIUMS: no Q4 Japanese premium settlement has been reported yet; offers stand at $265-280/t against $395/t in Q3, and the market expects a settlement below $280/t.",
 "WHAT TO WATCH: today's LME official against the 3,061.5 July low ($56.50 below three-month) and the 3,289 level that would negate the bearish count; a Q4 Japanese premium settlement; Chinese markets reopening on 09-October."]}

new_feed=[
 {"when":"Tue 06-Oct","impact":"Bearish","text":f"BOARD ROLLED TO THE MONDAY 05-OCTOBER LME OFFICIAL. Cash $3,107.00 (-$2.50), three-month $3,118.00 (-$4.00, -{abs(pm):.2f}%), contango NARROWED to $11.00 from $12.50 (opposite to price), stock unchanged at 240,375 t. Verified on cache-busted English and German overviews in exact agreement, the aluminium per-metal table with no later row, and five-for-five stock reconciliation."},
 {"when":"Tue 06-Oct","impact":"Bearish","text":"DOLLAR NEAR 18-MONTH HIGH, US 10-YEAR NEAR 5.32% (Trading Economics): the dollar index held around 102 as the euro weakened on European political and fiscal uncertainty; the ten-year yield is near its highest since 2002; markets price about 78% odds of a Fed hold at the next meeting."},
 {"when":"Tue 06-Oct","impact":"Mixed","text":"BRENT NEAR $100 (Trading Economics): crude slipped after Monday's decline as Middle East exports recovered to about 17.5 million barrels a day, roughly 98% of pre-war levels; Saudi Arabia cut its flagship crude price for Asian buyers."},
 {"when":"Mon 05-Oct","impact":"Mixed","text":"BASE METALS MIXED AT THE MONDAY OFFICIAL: copper +0.32% three-month with backwardation widening to $64 and stock down 3,750 t; nickel +0.42%, lead +0.38%; zinc -0.51% with a 3,225 t stock inflow; aluminium -0.13%."},
]
d['feed']=(new_feed+d['feed'])[:12]

new_news=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":f"LME ALUMINIUM MAKES A THIRD LOWER SETTLEMENT AS SELLING FADES. The Monday 05-October official settled cash at $3,107.00 (-{abs(pc):.2f}%) and three-month at $3,118.00 (-{abs(pm):.2f}%), another marginal low for the move and $56.50 above the 3,061.5 July low. The contango narrowed to $11.00 from $12.50 while the price fell, and visible stock was unchanged at 240,375 t."},
 {"theme":"Macro","horizon":"Days-weeks","impact":"Bearish","url":S_TEA,
  "headline":"ALUMINIUM AT LOWEST SINCE EARLY JULY ON DOLLAR AND SUPPLY OUTLOOK (Trading Economics, 05-October): Trading Economics attributes the fall below $3,130/t to a robust dollar and expectations of improving supply as smelters prepare restarts and expansions, adding that Chinese exports rose about 17% year on year in August as weak domestic demand and high inventories pushed metal overseas."},
 {"theme":"Macro","horizon":"Days-weeks","impact":"Bearish","url":S_TEY,
  "headline":"US 10-YEAR YIELD NEAR 5.32%, HIGHEST SINCE 2002 (Trading Economics, 06-October): a persistent global bond sell-off, fiscal concerns and sticky services inflation keep long yields elevated; the dollar index held near 102 as the euro weakened on European political uncertainty. Higher carrying and financing costs weigh on metal inventory demand."},
 {"theme":"Energy","horizon":"Days-weeks","impact":"Mixed","url":S_TEB,
  "headline":"BRENT SLIPS TOWARD $100 AS GULF EXPORTS RECOVER (Trading Economics, 06-October): Middle East crude shipments rebounded to about 17.5 million barrels a day, roughly 98% of pre-war levels, and Saudi Arabia cut its official selling price for Asia. Lower energy trims the smelter cost floor at the margin; recovering Gulf flows also point to normalising regional logistics."},
 {"theme":"Supply","horizon":"Multi-year","impact":"Bearish (long-term)","url":S_ALCI,
  "headline":"INDIA IDENTIFIES 6,800 ACRES FOR A NEW SMELTER SITE IN ANDHRA PRADESH (AL Circle, 03-October): land in Srikakulam district has been earmarked for a proposed aluminium smelter, with alumina potentially sourced from Angul, Odisha; a Ministry of Mines inspection team is due to assess feasibility. Capacity and investment were not specified - an early-stage, long-dated supply signal only."},
]
d['news']=new_news+d['news'][:15]

cats=d['outlook']['catalysts']
for c in cats:
    if c['date']=='Mon 05-Oct':
        c['date']='Passed Mon 05-Oct'
        c['event']="SOUTH32'S Q4 MJP OFFER OF $265/T REACHED ITS STATED VALIDITY DATE (SMM) WITHOUT A PUBLICLY REPORTED SETTLEMENT by the time this page compiled on 06-October. A settlement at or below that level would confirm a roughly 30% quarter-on-quarter reset in the Japanese premium from $395/t."
    if c['date']=='Daily, from Mon 05-Oct':
        c['date']='Daily, from Tue 06-Oct'
        c['event']="THE 3,061.5 JULY LOW AND THE 3,289 INVALIDATION. Three-month settled $3,118.00 on 05-October, $56.50 above the 02-July low at 3,061.5 (and $41.00 above the 50% weekly retracement at 3,077). A daily official settlement beneath 3,061.5 opens the 2,950-3,000 area; a daily settlement back above 3,289 negates the bearish daily count."
cats.insert(1,{"date":"Any day (pending)","impact":"High","event":"Q4-2026 JAPANESE QUARTERLY PREMIUM (MJP) SETTLEMENT. Latest public offers $265-280/t (South32, Rio Tinto per SMM); market expects below $280/t versus $395/t in Q3. Not yet reported as settled at 06-October."})
d['outlook']['catalysts']=cats

RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 06-OCTOBER: the contango NARROWED $1.50 to $11.00 on 05-October even as the price fell. Trend held at FLAT."
RK[1]['risk']+=" UPDATE 06-OCTOBER: the US ten-year yield is near 5.32%, the highest since 2002, and the dollar index near 102; markets price about 78% odds of a Fed hold at the next meeting (Trading Economics). Financing costs remain elevated. Trend held at UP."
RK[4]['risk']+=" UPDATE 06-OCTOBER: LME stock unchanged at 240,375 t on 05-October. Trend held at FLAT."
RK[8]['risk']+=" UPDATE 06-OCTOBER: South32's $265/t offer passed its stated 05-October validity with no settlement publicly reported. Trend held at DOWN."

for s in d['outlook']['scenarios']:
    dr=s['drivers']
    dr=re.sub(r"^HELD 05-OCTOBER \(pre-ring Monday, no new session since Friday\); ","",dr)
    s['drivers']="HELD 06-OCTOBER: the 05-October official was a further small decline ($4.00 on three-month) with a narrower contango and flat stock - not enough evidence to move the weights. "+dr
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['outlook']['ai_analysis'][0]=(f"TUESDAY PRE-RING REVIEW, 06-OCTOBER: Monday's official made a third lower settlement (three-month $3,118.00, -{abs(pm):.2f}%) but the smallest of the three, and the contango narrowed to $11.00 while stock held flat. That pattern - price drifting lower on fading momentum with a firmer prompt - looks like a market grinding toward the 3,061.5 July low rather than capitulating. The dollar near 102 and US ten-year yields near 5.32% remain the main headwinds.")

for l in d['logistics']:
    if l['name']=='Strait of Hormuz transit':
        rest=l['note'].split(' PRIOR: ',1)[-1]
        l['note']=("REVIEWED TUESDAY 06-OCTOBER-2026. Trading Economics' Brent coverage (06-October) reports Middle East crude shipments rebounding to about 17.5 million barrels a day, roughly 98% of pre-war levels. No container or bulk transit count is published because tracker figures remain disputed. Arrow stays UP pending a public, verifiable normalisation signal for dry-bulk and container traffic. PRIOR: "+rest)
        l['src']="REVIEWED TUESDAY 06-OCTOBER-2026: Trading Economics Brent ("+S_TEB+"). PRIOR: "+l['src'].split(' PRIOR: ',1)[-1]
    if l['name'].startswith('Red Sea'):
        l['note']=l['note'].replace("REVIEWED MONDAY 05-OCTOBER-2026:","REVIEWED TUESDAY 06-OCTOBER-2026 (no newer public transit count located; Monday's note carried):",1)

for m in d['macro']:
    if m['name'].startswith('Brent'):
        m['value']='100.41'; m['day']="+0.09% in Tuesday 06-October trade after declining on Monday; +3.34% over the month (Trading Economics)"
        m['note']="REFRESHED TUESDAY 06-OCTOBER-2026 on a public reference board (Trading Economics), which cites Middle East crude exports recovering to about 17.5 million barrels a day (about 98% of pre-war levels) and a Saudi price cut for Asian buyers; markets await the US EIA Short-Term Energy Outlook. Energy is a major smelter cash-cost line."
    elif m['name'].startswith('US dollar index'):
        m['value']='102.165'; m['day']="+0.06% in Tuesday 06-October trade; +3.01% over the month; near its strongest since April 2025 (Trading Economics)"
        m['note']="REFRESHED TUESDAY 06-OCTOBER-2026 on a public reference board (Trading Economics): the euro is under pressure from political and fiscal uncertainty in Europe; markets price about 78% odds of a Fed hold at the next meeting. A firm dollar weighs on dollar-priced metals."
    elif m['name'].startswith('US 10-year'):
        m['value']='5.32'; m['day']="+1bp in Tuesday 06-October trade; near the highest since 2002 (Trading Economics)"
        m['note']="REFRESHED TUESDAY 06-OCTOBER-2026 on a public reference board (Trading Economics), citing a persistent global bond sell-off, fiscal concerns and sticky services inflation. Higher yields raise the cost of carrying metal and financing inventory."
    elif m['name']=='EUR/USD':
        m['value']='1.12060'; m['day']="LME fixing on 05-October, -0.24% from 1.12330; ECB fixing 1.12040, BFIX 1.12044"
        m['note']="REFRESHED TUESDAY 06-OCTOBER-2026 to the 05-October LME fixing via Westmetall, the same session as the LME board."

for r in d['producer_status']:
    r['asof']=RD
    u=r['update']
    if u.startswith("REVIEWED 05-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE"):
        u="REVIEWED 06-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE"+u[len("REVIEWED 05-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE"):]
    elif u.startswith("REVIEWED 05-OCTOBER: no newer public disclosure located; status below carried. "):
        u="REVIEWED 06-OCTOBER: no newer public disclosure located; status below carried. "+u[len("REVIEWED 05-OCTOBER: no newer public disclosure located; status below carried. "):]
    else:
        u="REVIEWED 06-OCTOBER: no newer public disclosure located; status below carried. "+u
    r['update']=u

for s in [["Westmetall - LME official prices and stocks, 05-Oct-2026 session (EN+DE)",W],
          ["Trading Economics - aluminium commentary (05-Oct-2026)",S_TEA],
          ["Trading Economics - US dollar index (06-Oct-2026)",S_TED],
          ["Trading Economics - US 10-year yield (06-Oct-2026)",S_TEY],
          ["Trading Economics - Brent crude (06-Oct-2026)",S_TEB],
          ["AL Circle - Andhra Pradesh backs Srikakulam aluminium smelter plan (03-Oct-2026)",S_ALCI]]:
    d['sources'].append(s)
d['outlook']['sources'].append(["Trading Economics - aluminium: lowest since early July on dollar and supply outlook (05-Oct-2026)",S_TEA])

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE MONDAY 05-OCTOBER-2026 LME OFFICIAL. This page compiled on TUESDAY 06-October at about 05:35 London, before the ring; today's official prints at 13:20 London, so Monday's official is the latest published figure.")
C[1]=("THE COMPLETENESS TEST PASSES: the aluminium per-metal daily table shows 05-October as the newest row with NO ROW AFTER IT and 02-October unchanged as the prior row; the other metals reconcile through the cache-busted overviews and stock arithmetic.")
C[2]=("THE ENGLISH AND GERMAN OVERVIEWS WERE BOTH REQUESTED CACHE-BUSTED ON 06-OCTOBER AND AGREE EXACTLY on 05-October across all six metals, stocks and FX fixings.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against the levels carried for 02-October: aluminium unchanged at 240,375; copper -3,750 to 244,900; nickel -198 to 284,970; zinc +3,225 to 126,975; lead -2,700 to 351,475.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (05-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (three sessions, 01-, 02- and 05-October) as their latest point. The stock chart axis floor stays at 230,000 t with visible stock at 240,375 t.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,107.00 against three-month $3,118.00 is therefore an $11.00 CONTANGO, narrowed $1.50 from $12.50 on 02-October - and it narrowed while the flat price fell, i.e. spread and price moved in OPPOSITE directions."
C[6]=("PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND NO NEW PUBLIC ASSESSMENT WAS LOCATED FOR THIS WINDOW; every premium row is carried at its own assessment date. No Q4-2026 Japanese quarterly settlement had been publicly reported when this page compiled on 06-October; the chart's pending band is the latest reported OFFER range ($265-280/t: South32 and Rio Tinto per SMM, 30-September). Offers are not settlements.")
for i,c in enumerate(C):
    if c.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a re-verified 50% Section 232 rate on full customs value, the tariff leg is 0.50 times the 05-October official cash of $3,107.00, or ${tl:,.2f}, leaving an ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."
    if c.startswith("PEER EARNINGS ARE IN A LULL"):
        C[i]=("PEER EARNINGS ARE IN A LULL AND NO COMPANY WAS BACK-FILLED THIS RUN (06-October). The Q3-2026 reporting season opens in mid-October; existing earnings_history entries are unchanged and carry only exact publicly verified figures.")
    if c.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent ($100.41), the dollar index (102.165) and the US ten-year (5.32%) are Trading Economics reference marks from Tuesday 06-October Asian/European-morning trade; EUR/USD is the 05-October LME fixing; European gas TTF is carried at its Friday 02-October close (74.76 EUR/MWh) because no newer public reference value was captured this run. Hormuz and Bab el-Mandeb transit counts remain disputed, so none is published.")
    if c.startswith("THE ELLIOTT WAVE PANELS"):
        C[i]=c.split(' UPDATE 0')[0]+" UPDATE 06-OCTOBER: the daily count (C-wave from 3,374) is unchanged after a third, smaller lower settlement on 05-October (three-month $3,118.00); the weekly alternate remains preferred after the 02-October weekly close beneath 3,261."

ew=d['ew']; ew['updated']=RD
st=ew['short_term']
assert st['line'][-1]==[0.9989,3122.0], st['line'][-1]
st['line'].append([0.9994,3118.0])
st['now_x']=0.9997
st['proj']={"bull":[[0.9997,3118.0],[0.99985,3205],[1.0,3290]],
            "base":[[0.9997,3118.0],[0.99985,3085],[1.0,3135]],
            "bear":[[0.9997,3118.0],[0.99985,3045],[1.0,2980]]}
for f in st['fib']:
    if f['p']==3289.0: f['l']="3,289 - the 12-September (ii) high and the INVALIDATION of the bearish daily count. A daily official settlement above it negates the C-wave count. It is $171.00 above the 05-October three-month."
    if f['p']==3261.0: f['l']="3,261 - the shared 38.2% weekly retracement, held at the SAME price as the weekly panel. The 02-October weekly close settled $139.00 beneath it (weekly test FAILED); three-month is $143.00 beneath it on 05-October."
    if f['p']==3183.0: f['l']="3,183 - the 20-August low, BROKEN on 01-October and not regained (05-October three-month $3,118.00). First resistance on any rebound."
    if f['p']==3061.5: f['l']="3,061.5 - the 02-July C low and the next objective support, shared with the weekly panel (50% weekly retracement at 3,077). $56.50 beneath three-month."
st['fwd_pivots'][0]['w']="FIRST TEST BELOW: the 3,061.5 July low (and 3,077, the weekly 50% retracement), $56.50 beneath the 05-October three-month. A daily official settlement beneath it extends wave (iii) of C towards the 2,980 area (1.618 x wave (i) projected from 3,289)."
st['fwd_pivots'][1]['w']="THE INVALIDATION: 3,289, the 12-September (ii) high. A DAILY OFFICIAL SETTLEMENT ABOVE IT negates the bearish C-wave count and restores the possibility that the 3,061.5-3,374 advance was the first leg of a new uptrend."
st['writeup']=("DAILY (SWING DEGREE) - THE C-WAVE COUNT IS UNCHANGED; A THIRD LOWER SETTLEMENT, BUT MOMENTUM IS FADING. Three-month settled $3,118.00 on Monday 05-October, another marginal low for the decline from 3,374, after $3,122.00 on Friday and $3,131.00 on Thursday. "
 "BASE CASE, ABOUT 62%: the 3,061.5-3,374 rally was a corrective B wave and a C-wave decline is under way, with (i) at 3,183, (ii) at 3,289 on 12-September and (iii) in progress; the cardinal rules hold - (ii) did not exceed the 3,374 origin and (iii) already extends beyond (i). The shrinking daily declines ($80, $9, $4) fit a small fourth-wave pause inside (iii) or a slowing approach to the July low. Targets: the 3,061.5 July low first, then about 2,980 where (iii) equals 1.618 times (i). "
 "ALTERNATE, ABOUT 38%: a deep expanded flat or double-three that holds above 3,061.5 and resumes higher; it needs a recovery above 3,183. "
 "INVALIDATION: a daily official settlement above 3,289, $171.00 above the 05-October three-month. CONFIDENCE IS MODERATE. This is technical context, not advice.")
lt=ew['long_term']
lt['fwd_pivots'][0]['w']=("THE 3,261 LEVEL - THE 38.2% RETRACEMENT OF THE 3,855-TO-3,061.5 DECLINE - WAS THE WEEKLY TEST AND IT FAILED: the 02-October weekly close settled three-month at $3,122.00, $139.00 beneath it; on 05-October three-month is $3,118.00, $143.00 beneath. Per the pre-registered rule the weekly alternate (the move off 3,061.5 was corrective) is preferred. 3,261 is now overhead resistance.")
lt['fwd_pivots'][1]['w']=("THE DOWNSIDE REFERENCES ARE SHARED WITH THE DAILY PANEL: the 50% retracement at 3,077 (held on the 3,061.5 low of 02-July), now $41.00 beneath the 05-October three-month of $3,118.00, and the 61.8% at 2,894, where the bear path terminates. A WEEKLY close beneath 3,077 invalidates the constructive count outright. Overhead, the 23.6% retracement at 3,488 is $370.00 above.")
lt['writeup']=("WEEKLY (POSITION DEGREE) - THE ALTERNATE PROMOTED AFTER THE FAILED WEEKLY TEST REMAINS PREFERRED. The 3,855 high of 02-June terminates the position-degree advance; the decline into 3,061.5 on 02-July is a completed A-B-C and the 50% retracement at 3,077 held. The 02-October weekly close at $3,122.00 sat $139.00 beneath the 3,261 retracement, and Monday 05-October's $3,118.00 keeps the week opening below it. "
 "PREFERRED COUNT, ABOUT 55%: the move off 3,061.5 was corrective - a B wave or the opening leg of a larger fourth wave - and the decline under way breaks the 2,950-3,110 zone towards the 61.8% retracement at 2,894. "
 "ALTERNATE, ABOUT 45%: a new position-degree advance is still building off 3,061.5 as long as that low holds on a weekly close; targets 3,488, then 3,680 and 3,840 into mid-2027. "
 "INVALIDATION: a weekly close beneath 3,077 invalidates the constructive alternate outright; a weekly close back above 3,261 would restore it as preferred. CONFIDENCE IS LOW-TO-MODERATE. This is technical context, not advice.")
lt['proj']={"bull":[[0.66,3118.0],[0.76,3380],[0.88,3600],[1.0,3800]],"base":[[0.66,3118.0],[0.78,3120],[0.9,3230],[1.0,3290]],"bear":[[0.66,3118.0],[0.8,2970],[1.0,2890]]}

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-02', ph['rows'][-1]
ph['rows'].append(['2026-10-05',cash,m3,stk])
ph['updated']=RD
ph['basis']=("London Metal Exchange official settlements via Westmetall. LME Aluminium official cash settlement, official 3-month, and LME warehouse stock. Weekly sampling (last published official session of each week). AT THE 06-OCTOBER-2026 UPDATE the row for the week of 05-October is PROVISIONAL: the Monday 05-October session (cash 3,107.00, 3-month 3,118.00, stock 240,375 t), to be replaced as later sessions print; the week of 28-September is FINAL at the Friday 02-October session. Verified against both cache-busted Westmetall language overviews and the per-metal aluminium daily table.")
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok', d['metals_board'], mh['al'][-1], mh['zn'][-1], mh['pb'][-1], round(tl,2), round(share,1), round(ratio,2))

# --- addendum (same run): deliberate trend review of the cost-floor risk ---
d=json.load(open(P,encoding='utf-8'))
r=d['outlook']['risks'][7]; assert r['risk'].startswith('THE COST FLOOR')
r['risk']+=" UPDATE 06-OCTOBER: Brent eased back toward $100.4 after declining on Monday as Middle East crude exports recovered to about 98% of pre-war levels and Saudi Arabia cut its Asian selling price (Trading Economics, 06-October). The energy support for the cost floor has stopped rising. Trend moved from UP to FLAT."
r['trend']='flat'
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('addendum ok')
