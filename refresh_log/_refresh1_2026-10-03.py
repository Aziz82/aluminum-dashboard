# Daily data refresh - 2026-10-03 (SATURDAY, no LME ring). Board ROLLED to FRIDAY 02-Oct LME official (the weekly close).
# EN+DE cache-busted overviews agree exactly; per-metal Al and Cu tables show 02-Oct newest (no later row), 01-Oct prior unchanged.
import json, re
P='market_data.json'
d=json.load(open(P,encoding='utf-8'))
RD='2026-10-03'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_SMMQ="https://news.metal.com/newscontent/104142880-smm-analysis-overseas-primary-aluminum-market-quiet-as-market-awaits-q4-mjp-settlement"
S_ALCQ="https://www.alcircle.com/news/ex-china-aluminium-market-runs-steadily-as-market-awaits-q4-mjp-settlement-121397"
S_TED="https://tradingeconomics.com/united-states/currency"
S_TEY="https://tradingeconomics.com/united-states/government-bond-yield"
S_TEB="https://tradingeconomics.com/commodity/brent-crude-oil"
S_RIO="https://www.riotimesonline.com/copper-markets-latam-friday-october-2-2026/"
S_BBG="https://www.bloomberg.com/news/articles/2026-10-02/copper-heads-for-weekly-loss-as-high-energy-costs-limit-demand"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
ZN_SEP=3986.0; PB_SEP=None

cash,prev_c,m3,prev_m,stk,prev_s=3109.5,3120.0,3122.0,3131.0,240375,240625
spr=cash-m3
pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100

VER=("COMPILED SATURDAY 03-OCTOBER-2026 - NO LME RING TODAY (WEEKEND). THE BOARD ROLLED THIS RUN TO THE FRIDAY 02-OCTOBER-2026 LONDON METAL EXCHANGE OFFICIAL, THE LAST TRADING SESSION AND THE WEEKLY CLOSE; IT IS CARRIED BECAUSE THE MARKET IS SHUT UNTIL MONDAY 05-OCTOBER. "
 "COMPLETENESS CHECKS: (1) the cache-busted English and German Westmetall overviews AGREE EXACTLY on 02-October across all six metals, all six stock lines and the foreign-exchange fixings; (2) the per-metal daily tables for aluminium and copper show 02-October as the newest row - NO ROW AFTER IT - with 01-October reproduced unchanged as the prior row; "
 "(3) ALL FIVE STOCK LINES RECONCILE against the levels carried for 01-October: aluminium 240,625 less 250 to 240,375; copper 248,075 PLUS 575 to 248,650; nickel 284,682 PLUS 486 to 285,168; zinc 123,975 less 225 to 123,750; lead 356,600 less 2,425 to 354,175. "
 "The whole board sits on ONE UNIFORM SESSION (02-October) and no intraday, closing, reference or contract-for-difference mark is used anywhere in it. Prior-month averages remain the completed SEPTEMBER-2026 official means. NEXT OFFICIAL: MONDAY 05-OCTOBER, 13:20 LONDON.")

AL=(f" CASH SETTLED $3,109.50 ON THE 02-OCTOBER OFFICIAL, DOWN $10.50 OR {abs(pc):.2f}% FROM $3,120.00. THREE-MONTH SETTLED $3,122.00, DOWN $9.00 OR {abs(pm):.2f}% FROM $3,131.00 - A SECOND LOWER SETTLEMENT AND A NEW LOW FOR THE MOVE, THOUGH THE PACE SLOWED SHARPLY AFTER THURSDAY'S 2.5% FALL. "
 "SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION: cash fell $1.50 more than three-month, so the CONTANGO WIDENED TO $12.50 from $11.00 as the price eased. "
 "VISIBLE LME STOCK DREW 250 TONNES TO 240,375, a second consecutive small draw. "
 "THIS WAS THE WEEKLY CLOSE: three-month at $3,122.00 is $139.00 BENEATH THE 3,261 WEEKLY RETRACEMENT, so the pre-registered weekly test FAILED and the weekly alternate is formally re-opened. Over the week three-month fell $145.00 or 4.4% from the $3,267.00 close of 25-September. Friday's macro backdrop eased slightly: US September payrolls rose only 29,000 against about 90,000 expected and the dollar index slipped 0.17% (Trading Economics), but metal did not bounce.")

d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,109.5","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,122.0","pos":False,"delta":VER+AL+" THREE-MONTH CLOSED THE WEEK $139.00 BELOW 3,261, $61.00 BELOW THE BROKEN 3,183 DAILY LEVEL, $167.00 BELOW THE 3,289 DAILY INVALIDATION and $60.50 above the 3,061.5 July low."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-12.5","pos":False,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,109.50 against three-month $3,122.00 is a $12.50 CONTANGO, WIDENED $1.50 from $11.00. Spread and flat price moved in the SAME direction for a second session (price down, contango wider). The published reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"240,375","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK DREW 250 TONNES TO 240,375, a second consecutive draw and a fresh low for the series on this page. September's mean stock was {sep_s:,} tonnes. Stock still falling while price falls says the decline is macro- and supply-outlook-driven, not a visible physical glut."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,122.00, DOWN $9.00 OR {abs(pm):.2f}% FROM $3,131.00, THE WEEKLY CLOSE. AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DREW 250 TONNES TO 240,375, A SECOND CONSECUTIVE DRAW. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-11.0,"avg":sep_sp,"note":VER+f" A $12.50 CONTANGO, WIDENED $1.50 FROM $11.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in the SAME direction on this ring. PUBLISHED REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1233,"prev":1.1305,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.12330 FROM 1.13050 at the Friday ring; the ECB fixing printed 1.12250 and BFIX 1.12332, so all three agree on a firmer dollar at midday. Later on Friday the dollar index slipped 0.17% to about 101.92 after weak US payrolls (Trading Economics). AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]

d['outlook']['forward_path']=[
 {"tenor":"Cash (02-Oct official - weekly close, carried over the weekend)","price":"3,109.5","basis":f"THE 02-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,109.50, DOWN $10.50 OR {abs(pc):.2f}%. No ring on Saturday or Sunday; next official Monday 05-October 13:20 London."},
 {"tenor":"3-month (02-Oct official - weekly close)","price":"3,122.0","basis":f"THE 02-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,122.00, DOWN $9.00 OR {abs(pm):.2f}%: weekly close $139.00 beneath 3,261, $61.00 beneath the broken 3,183, $60.50 above the 3,061.5 July low."},
 {"tenor":"Cash-to-3M structure","price":"-12.5 (CONTANGO)","basis":"A $12.50 CONTANGO, widened $1.50 from $11.00. Flat price and spread moved in the SAME direction for a second session."},
 {"tenor":"Visible LME stock","price":"240,375 t","basis":f"DREW 250 t, a second consecutive draw; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE CURVE SOFTENED A LITTLE FURTHER WITH THE PRICE. On the 02-October official cash $3,109.50 sits $12.50 BELOW three-month $3,122.00, a CONTANGO widened $1.50 from $11.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00 and now $12.50. "
 f"READ: a mild, orderly widening - not a glut signal, with visible stock still drawing (240,375 t). The September mean spread was ${sep_sp:,.2f}. The published reversal condition (a backwardation beyond $15.00) remains far away; a contango beyond $24.50 would be the bearish structural confirmation.")

ls=d['lme_series']; assert ls[-1][0]=='01-Oct', ls[-1]
d['lme_series']=ls[1:]+[["02-Oct",cash,m3,stk]]
d['chart_price_axis']=[3000,3450]
d['chart_stock_axis']=[230000,255000]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":14320.0,"day":round((14320/14290-1)*100,2),"ytd":round((14320/12511-1)*100,2)},
 {"name":"Nickel","price":15625.0,"day":round((15625/15760-1)*100,2),"ytd":round((15625/16915-1)*100,2)},
 {"name":"Zinc","price":3733.0,"day":round((3733/3766-1)*100,2),"ytd":round((3733/3130.5-1)*100,2)},
 {"name":"Lead","price":1865.0,"day":round((1865/1869-1)*100,2),"ytd":round((1865/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*14320/14290,1); mh['ni'][-1]=round(mh['ni'][-1]*15625/15760,1)
# zn/pb 'now' = October cash average-to-date: 01-Oct + 02-Oct sessions. Prior point was based on 01-Oct alone.
zn_avg=(3834.0+3798.0)/2; pb_avg=(1837.0+1827.0)/2
mh['zn'][-1]=round(mh['zn'][-1]*zn_avg/3834.0,1); mh['pb'][-1]=round(mh['pb'][-1]*pb_avg/1837.0,1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',14355.0),('NI',15435.0),('ZN',3798.0),('PB',1827.0)): R[k]=R[k][1:]+[v]
ms['asof']='2026-10-02'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending FRIDAY 02-OCTOBER-2026 (the last session before the weekend). THE WINDOW ROLLED THIS RUN: 11-September dropped and 02-October appended, so the window is 14-September to 02-October. Every point is an official cash settlement, verified against the cache-busted Westmetall English and German overviews, which agree to the cent, the per-metal daily tables (no row after 02-October), and five-for-five stock-line reconciliation. Next official Monday 05-October.")
ms['src']=["Westmetall - LME official cash settlements, EN and DE overviews cache-busted and in exact agreement (02-October-2026 session)",W]

AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",14355.0,14320.0," COPPER: cash $14,355.00, UP $20.00 or 0.14%; three-month $14,320.00, UP $30.00 or 0.21% - the only metal higher on the session. The BACKWARDATION narrowed to $35.00 from $45.00. Stock ROSE 575 tonnes to 248,650. Public reporting flags Chilean labour risk (strike authorisation by Escondida supervisors; Centinela workers rejecting a final offer - Rio Times, 02-October) and Bloomberg reports copper heading for a weekly loss as high energy costs limit demand."),
 ("Nickel",15435.0,15625.0," NICKEL: cash $15,435.00, down $135.00 or 0.87%; three-month $15,625.00, down $135.00 or 0.86%. CONTANGO unchanged at $190.00, still the widest carry on the board. Stock ROSE 486 tonnes to 285,168."),
 ("Zinc",3798.0,3733.0," ZINC: cash $3,798.00, down $36.00 or 0.94%; three-month $3,733.00, down $33.00 or 0.88%. The BACKWARDATION narrowed slightly to $65.00 from $68.00; stock drew 225 tonnes to 123,750. Zinc remains the strongest metal on this board year to date."),
 ("Lead",1827.0,1865.0," LEAD: cash $1,827.00, down $10.00 or 0.54%; three-month $1,865.00, down $4.00 or 0.21%. CONTANGO widened $6.00 to $38.00. Stock drew 2,425 tonnes to 354,175, a tenth consecutive draw and the largest on the board this session. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL, REPORTED AS DATA NOT AS A REGIME SIGNAL: on the Friday 02-October weekly close three-month prices fell in four of five metals (aluminium -0.29%, nickel -0.86%, zinc -0.88%, lead -0.21%) while copper rose 0.21%; the LME euro fixing fell to 1.1233 from 1.1305. The selling was far milder than Thursday's broad, dollar-led session.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

OLDH="COMPILED FRIDAY 02-OCTOBER-2026 AT ABOUT 03:40 LONDON, BEFORE FRIDAY'S RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY)."
NEWH="COMPILED SATURDAY 03-OCTOBER-2026, NO LME RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY)."
n_rep=0
for i in d['inputs']:
    if isinstance(i.get('src'),str) and OLDH in i['src']: i['src']=i['src'].replace(OLDH,NEWH); n_rep+=1
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='01-Oct'
        i['hist']=i['hist'][1:]+[["02-Oct",14355.0]]
        i['val']="~14,320.00 (3M); 14,355.00 (cash) $/t"
        i['ratio']="~14,355.00 $/t cash vs LME 3M 14,320.00 $/t"
        i['trend']='flat'
        i['src']=("LME official cash settlement, rolled to the FRIDAY 02-OCTOBER-2026 session (the last before the weekend) at $14,355.00, UP $20.00 or 0.14% against $14,335.00. THE WINDOW ROLLED THIS RUN: 11-September dropped and 02-October appended, so the series is the last fifteen published official cash sessions, 14-September to 02-October - the same window as the LME Board sparklines. Official settlement only, verified on the cache-busted Westmetall English and German overviews, which agree to the cent, and the per-metal daily table (no row after 02-October). "
                  "Copper structure for context: backwardation $35.00 (from $45.00), stock rose 575 t to 248,650 t.")
print('inputs header replaced', n_rep)
d['inputs_summary']=("UPDATE 03-OCTOBER (WEEKEND, NO RING): copper rolled to the Friday 02-October LME official cash of $14,355.00, up $20.00, with its fifteen-session window moved to 14-September to 02-October. No other input mark printed in this window - China is on its 01-08 October National Day holiday, so the SMM fluoride, silicon and magnesium weeklies are not expected until after 08-October, and the carbon settlement cycle (anodes, pitch, green coke) is mid-October - so every other row is carried at its own dated public mark and no value was interpolated.")
for r in d['raw_materials']:
    if isinstance(r.get('src'),str): r['src']=r['src'].replace(OLDH,NEWH)

ratio=360.4/m3*100
ALNOTE=("COMPILED SATURDAY 03-OCTOBER-2026 (NO RING). NO NEW DATED PUBLIC ALUMINA MARK WAS LOCATED FOR THIS WINDOW: the LME Alumina (Platts) row stays at AL Circle's $360.40/t print of 30-September; the FOB East Australia trade row stays at its 18-September mark; SMM separately reported 30,000 t traded at $369/t FOB Western Australia on 30-September for November shipment (a different basis, reported in news only). The SMM alumina index is carried at its 30-September print of 2,669.99 yuan/tonne; SHFE is closed 01-08 October. "
 f"THE RATIO: LME Alumina at $360.40/t against the 02-October aluminium three-month of $3,122.00 is {ratio:.2f}%, against a decade norm of 15-17%. Alumina remains historically CHEAP relative to metal.")
for a in d['alumina']: a['src']=ALNOTE

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
PREM=("COMPILED SATURDAY 03-OCTOBER-2026. PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND THIS PANEL CARRIES EACH ROW AT ITS OWN LAST PUBLIC ASSESSMENT DATE. NO NEW PUBLIC PREMIUM ASSESSMENT WAS LOCATED FOR THIS WINDOW, so every row is CARRIED UNCHANGED. The Q4 MJP remains unsettled: SMM (30-September) and AL Circle (02-October) report Rio Tinto's offer cut to $280/t from $310/t and South32's offer at $265/t (revised down from $325/t, valid to 05-October), with the market expecting a settlement below $280/t; these are offers, not a settlement. "
 f"THE TARIFF DECOMPOSITION IS REFRESHED DAILY BY DESIGN: on a re-verified Section 232 rate of 50% on aluminium articles applied to full customs value, the tariff leg of the US duty-paid premium is 0.50 times the 02-October official cash of $3,109.50, or ${tl:,.2f}, DOWN $5.25 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}% of the US duty-paid premium is policy arithmetic rather than market. "
 "This page does NOT fabricate freight, financing or tightness splits for any premium row.")
for p in d['premiums']:
    s=p['src']; j=s.find("for any premium row.")
    if s.startswith("COMPILED") and j>0: p['src']=PREM+s[j+len("for any premium row."):]
    else: p['src']=PREM+" "+s
for q in d['premium_quarters']:
    if q['q']=='Q4-26': q['range']=[265,280]
d['premium_settlement_src']=["SMM - Overseas primary aluminium market quiet as market awaits Q4 MJP settlement (30-Sep-2026: Rio Tinto $280, South32 $265 offers)",S_SMMQ]
pdv=d['premium_drivers'][0]
pdv['d']=("Q4 MJP OFFERS KEEP FALLING: SMM (30-September) reports Rio Tinto's offer cut to $280/t from $310/t and South32's to $265/t from $325/t (valid to 05-October); AL Circle (02-October) says the market expects settlement below $280/t, against a Q3 settlement of $395/t. No settlement had been publicly reported by 03-October. WHY IT LANDS ON PREMIUMS: the quarterly MJP is the reference for much Asian physical business, so a settlement in the $260s-270s would reset the regional premium level down by roughly 30% for the quarter. The LME curve offers no exchange-side scarcity signal either: a $12.50 contango on 02-October.")
pdv['src']=["SMM - Q4 MJP offers: Rio Tinto $280, South32 $265 (30-Sep-2026)",S_SMMQ]

d['lme_commentary']=(f"ALUMINIUM CLOSED THE WEEK AT ITS LOWEST SINCE EARLY JULY AND FAILED THE WEEKLY TEST. On the Friday 02-October official cash settled $3,109.50, down $10.50 or {abs(pc):.2f}%, and three-month $3,122.00, down $9.00 or {abs(pm):.2f}% - a second lower settlement after Thursday's 2.5% fall, and $139.00 beneath the 3,261 weekly level. Over the week three-month lost $145.00 or about 4.4%. "
 "The contango widened $1.50 to $12.50 (spread and price in the same direction again) and visible stock drew 250 tonnes to 240,375. "
 "Friday's macro was mixed for metals: US September payrolls rose only 29,000 against about 90,000 expected, unemployment rose to 4.2% and the dollar index slipped 0.17% to about 101.9 (Trading Economics), yet the ten-year yield held near 5.28% and markets still price a December Fed hike. Copper was the only base metal higher on the session. "
 f"In Asia the Q4 Japanese premium offers kept falling (South32 $265/t, Rio Tinto $280/t, per SMM). China's markets are shut until 09-October. September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH ON PRICE, MILDLY BEARISH ON STRUCTURE, BUT MOMENTUM SLOWED. Against: three-month closed the week $139 under the 3,261 weekly level, extending the break of 3,183; the contango widened to $12.50; Asian premium offers are down about 30% quarter on quarter; Gulf restarts (Alba lines 4-6, EGA) are progressing and Macquarie projects a 2027 surplus. "
 "Constructive: visible LME stock is still drawing (240,375 t); Friday's fall was small ($9) despite heavy pressure all week; weak US payrolls trimmed near-term Fed-hike odds and nudged the dollar lower; and Brent near $102 keeps the smelter cost floor firm. The 3,061.5 July low ($60.50 away) is the decisive next test.")
d['commercial']=("COMMERCIAL READ - GENERIC AND PUBLIC. FIRST, THE CURVE PAYS BUYERS A LITTLE TO WAIT: a $12.50 contango is small but has widened for two sessions as the price fell. SECOND, ASIAN PREMIUMS ARE RESETTING LOWER: public reporting has Q4 MJP offers at $265-280/t with settlement expected below $280/t, against $395/t in Q3. THIRD, THE TARIFF ARITHMETIC MOVED WITH THE METAL: "
 f"on a verified 50% Section 232 rate, the tariff leg of the US Midwest duty-paid premium is ${tl:,.2f} on 02-October cash, {share:.1f}% of the $2,403/t premium. FOURTH, WATCH THE CALENDAR: Monday 05-October is the South32 offer's validity date and the first ring of the week; the 3,061.5 July low is the next technical reference; China returns from holiday on 09-October. This is generic public market context, not advice.")
d['bottom_line']=(f"BOTTOM LINE: aluminium ended the week on the LME official at cash $3,109.50 and three-month $3,122.00, down {abs(pm):.2f}% on Friday and about 4.4% on the week, closing $139 beneath the 3,261 weekly level - the pre-registered weekly test failed. "
 "The curve softened slightly (a $12.50 contango) while visible stock still drew. Scenario weights move to 14% bull / 47% base / 39% bear on the failed weekly test; the daily Elliott count (a C-wave decline from 3,374) is unchanged, with 3,061.5 the next reference and 3,289 the invalidation; the weekly alternate is promoted to about 55%.")

d['so_what']={"line":"Aluminium closed the week at its lowest since early July, about 4.4% lower on the week and below a key weekly level, as falling Asian premiums and recovering Gulf supply outweighed still-shrinking LME stock - the July low near $3,060 is the next test when trading resumes Monday.",
 "points":[
 f"WHAT MOVED: Friday's LME official settled cash at $3,109.50 (-$10.50) and three-month at $3,122.00 (-$9.00, -{abs(pm):.2f}%), the weekly close; the contango widened to $12.50 and LME stock edged down 250 t to 240,375 t. Weekend: no trading until Monday.",
 "WHY: the week's slide was driven by a strong dollar, multi-decade-high US yields, Gulf peace hopes and faster smelter restarts. Friday's selling was much lighter, helped by weak US jobs data (payrolls +29,000 vs about 90,000 expected) that nudged the dollar lower.",
 "PREMIUMS: Japanese Q4 premium offers keep falling - South32 at $265/t and Rio Tinto at $280/t against $395/t in Q3 - and the market expects a settlement below $280/t.",
 "WHAT TO WATCH: the 3,061.5 July low ($60.50 below three-month), a daily settlement back above 3,289 (which would negate the bearish count), the Q4 Japanese premium settlement, and Chinese inventory when markets reopen on 09-October."]}

new_feed=[
 {"when":"Sat 03-Oct","impact":"Bearish","text":f"BOARD ROLLED TO THE FRIDAY 02-OCTOBER LME OFFICIAL (WEEKLY CLOSE; NO WEEKEND RING). Cash $3,109.50 (-$10.50), three-month $3,122.00 (-$9.00, -{abs(pm):.2f}%), contango $12.50 from $11.00, stock 240,375 t (-250). Weekly close $139 below 3,261. Verified on cache-busted English and German overviews in exact agreement, per-metal tables with no later row, and five-for-five stock reconciliation."},
 {"when":"Fri 02-Oct","impact":"Mixed","text":"US SEPTEMBER PAYROLLS +29,000 VS ABOUT 90,000 EXPECTED; UNEMPLOYMENT 4.2% (Trading Economics). Dollar index -0.17% to about 101.9, still set for a third weekly gain; ten-year about 5.28%; October Fed-hike bets trimmed, December hike still priced."},
 {"when":"Fri 02-Oct","impact":"Bearish","text":"AL CIRCLE / SMM: EX-CHINA PRIMARY MARKET QUIET AWAITING THE Q4 MJP. Rio Tinto offer $280/t (from $310), South32 $265/t (from $325, valid to 05-October); settlement expected below $280/t."},
 {"when":"Fri 02-Oct","impact":"Mixed","text":"COPPER THE ONLY BASE METAL HIGHER AT THE OFFICIAL (+0.21% three-month); Chilean labour risk at Escondida and Centinela (Rio Times); Bloomberg: copper heads for a weekly loss as high energy costs limit demand."},
]
d['feed']=(new_feed+d['feed'])[:12]

new_news=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":f"LME ALUMINIUM ENDS THE WEEK AT A NEW LOW FOR THE MOVE. The Friday 02-October official settled cash at $3,109.50 (-{abs(pc):.2f}%) and three-month at $3,122.00 (-{abs(pm):.2f}%), the weekly close, $139 beneath the 3,261 weekly retracement and about 4.4% lower on the week. The contango widened to $12.50 while visible stock drew 250 t to 240,375 t."},
 {"theme":"Premiums","horizon":"1-3 months","impact":"Bearish","url":S_SMMQ,
  "headline":"Q4 JAPANESE PREMIUM OFFERS FALL FURTHER (SMM, 30-September; AL Circle, 02-October): South32 offered $265/t, revised down from $325/t and valid to 05-October, while Rio Tinto's offer stands at $280/t after a cut from $310/t. Japanese buyers widely expect the final Q4 MJP below $280/t, against $395/t in Q3; Korean and Southeast Asian spot demand is described as very subdued."},
 {"theme":"Macro","horizon":"1-3 months","impact":"Mixed","url":S_TED,
  "headline":"WEAK US JOBS DATA TRIMS FED-HIKE BETS (Trading Economics, 02-October): September nonfarm payrolls rose only 29,000 against expectations near 90,000 and unemployment rose to 4.2%. The dollar index slipped 0.17% to about 101.9 but remained on track for a third weekly gain; the ten-year yield held near 5.28% and markets still price a December hike."},
 {"theme":"Base metals","horizon":"Immediate","impact":"Mixed","url":S_RIO,
  "headline":"BASE METALS SELL-OFF EASES; COPPER HOLDS UP ON CHILE RISK (Rio Times, 02-October): Thursday's broad sell-off left nickel at a ten-month low and zinc down 2.7% amid thin Golden Week trade; Escondida supervisors authorised strike action and Centinela workers rejected a final offer. On Friday's LME official copper was the only base metal higher."},
 {"theme":"Energy","horizon":"1-3 months","impact":"Mixed","url":S_TEB,
  "headline":"BRENT HOLDS NEAR $102 (Trading Economics): additional US military deployments to the Middle East and China's halt to fuel exports support prices, offset by Gulf crude flows approaching pre-war levels and a G7 plan to release up to 100 million barrels of diesel and crude over four months. High energy keeps the smelter cost floor firm."},
]
d['news']=new_news+d['news'][:15]

cats=d['outlook']['catalysts']
for c in cats:
    if c['date']=='Fri 02-Oct':
        c['date']='Resolved Fri 02-Oct'; c['impact']='High'
        c['event']="THE WEEKLY CLOSE TEST AT 3,261 FAILED: three-month settled $3,122.00 on Friday 02-October, $139.00 below the level. Per the pre-registered rule, weight shifts to the weekly alternate (the move off 3,061.5 was corrective) and to the bear scenario."
    if c['date']=='Daily, from Fri 02-Oct':
        c['date']='Daily, from Mon 05-Oct'
        c['event']="THE 3,061.5 JULY LOW AND THE 3,289 INVALIDATION. Three-month settled $3,122.00 at the weekly close, $60.50 above the 02-July low at 3,061.5 (and the 50% weekly retracement at 3,077). A daily official settlement beneath 3,061.5 opens the 2,950-3,000 area; a daily settlement back above 3,289 negates the bearish daily count."
cats.insert(1,{"date":"Mon 05-Oct","impact":"Medium","event":"SOUTH32'S Q4 MJP OFFER OF $265/T REACHES ITS STATED VALIDITY DATE (SMM). A settlement at or below that level would confirm a roughly 30% quarter-on-quarter reset in the Japanese premium from $395/t."})
d['outlook']['catalysts']=cats

RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 03-OCTOBER: the contango widened a further $1.50 to $12.50 on 02-October. Still small; trend held at FLAT."
RK[1]['risk']+=" UPDATE 03-OCTOBER: September payrolls +29,000 vs about 90,000 expected trimmed October hike bets and nudged the dollar down 0.17%, but the ten-year held near 5.28% and a December hike is still priced (Trading Economics). Trend held at UP."
RK[4]['risk']+=" UPDATE 03-OCTOBER: LME stock drew 250 t to 240,375 t, a second consecutive draw. Trend held at FLAT."
RK[8]['risk']+=" UPDATE 03-OCTOBER: South32 offered $265/t (from $325/t, valid to 05-October) alongside Rio Tinto's $280/t; settlement expected below $280/t (SMM, AL Circle). Trend held at DOWN."

SC={'Bull':('14%','$3,350-3,700'),'Base':('47%','$3,050-3,300'),'Bear':('39%','$2,880-3,050')}
for s in d['outlook']['scenarios']:
    p,t=SC[s['case']]; s['prob']=p; s['target']=t
    s['drivers']=("MOVED 03-OCTOBER (from 15/48/37): the pre-registered weekly test failed - three-month closed Friday 02-October at $3,122.00, $139.00 beneath 3,261 - so a further two points shift to the bear case. Kept modest because Friday's decline was only $9.00, visible stock is still drawing and weak US payrolls eased the dollar. PRIOR: "+s['drivers'])
sp=d['outlook']['scenario_paths']
sp['bull']=[3122.0,3290,3450,3600,3700]; sp['base']=[3122.0,3140,3200,3250,3280]; sp['bear']=[3122.0,3010,2950,2910,2880]

d['outlook']['ai_analysis'].insert(0,f"THE WEEKLY TEST FAILED AND THE MOVE IS NOW CONFIRMED ON BOTH TIMEFRAMES. Friday's official settled three-month at $3,122.00 (-{abs(pm):.2f}%), the weekly close, $139 beneath the 3,261 retracement and about 4.4% lower on the week. The pace slowed sharply after Thursday's 2.5% fall and visible stock is still drawing, so this is a repricing of the Gulf-supply premium and macro, not a physical glut.")
d['outlook']['ai_analysis'].insert(1,"PREMIUMS CONFIRM THE LOOSENING IN ASIA: Q4 Japanese offers have fallen to $265-280/t against a $395/t Q3 settlement. The 3,061.5 July low is the next objective test; a daily settlement back above 3,289 would negate the bearish count. Weak US payrolls are the one new macro input leaning the other way.")

for l in d['logistics']:
    if l['name']=='Strait of Hormuz transit':
        rest=l['note'].split(' PRIOR: ',1)[-1]
        l['note']=("REVIEWED SATURDAY 03-OCTOBER-2026. Trading Economics' Brent coverage cites additional US military deployments to the Middle East and continuing tanker-attack shipping risk, while Persian Gulf crude flows approach pre-war export levels; US-Iran negotiations remain uncertain. No container or bulk transit count is published because tracker figures remain disputed. Arrow stays UP. PRIOR: "+rest)
        l['src']="REVIEWED SATURDAY 03-OCTOBER-2026: Trading Economics Brent ("+S_TEB+"). PRIOR: "+l['src'].split(' PRIOR: ',1)[-1]

for m in d['macro']:
    if m['name'].startswith('Brent'):
        m['value']='102.25'; m['day']="-0.06% (Trading Economics front-month); +7.05% over the month"
        m['note']="REFRESHED SATURDAY 03-OCTOBER-2026 on a public reference board (Trading Economics), which cites US deployments, China's fuel-export halt, recovering Gulf crude flows and a G7 plan to release up to 100 million barrels. Trading Economics' dollar commentary notes Brent briefly below $100 on Friday; the board value is used. Energy is a major smelter cash-cost line."
    elif m['name'].startswith('US dollar index'):
        m['value']='101.924'; m['day']="-0.17% on Friday 02-October after weak US payrolls; +3.05% over the month; on track for a third weekly gain (Trading Economics)"
        m['note']="REFRESHED SATURDAY 03-OCTOBER-2026 on a public reference board (Trading Economics). September payrolls +29,000 vs about 90,000 expected; unemployment 4.2%."
    elif m['name'].startswith('US 10-year'):
        m['value']='5.28'; m['day']="+4bp on Friday 02-October despite weak payrolls; December Fed hike still priced (Trading Economics)"
        m['note']="REFRESHED SATURDAY 03-OCTOBER-2026 on a public reference board (Trading Economics). Higher yields raise the cost of carrying metal and financing inventory."
    elif m['name']=='EUR/USD':
        m['value']='1.12330'; m['day']="LME fixing on 02-October, -0.64% from 1.13050; ECB fixing 1.12250, BFIX 1.12332"
        m['note']="REFRESHED SATURDAY 03-OCTOBER-2026 to the 02-October LME fixing via Westmetall, the same session as the LME board."

for r in d['producer_status']:
    r['asof']=RD
    u=r['update']
    u=re.sub(r"^REVIEWED 02-OCTOBER\. NO NEW DATED PUBLIC DISCLOSURE FOR THIS SPECIFIC ASSET IN THIS WINDOW - none was located in Thursday trading or early Friday Asian hours - so",
             "REVIEWED 03-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE FOR THIS SPECIFIC ASSET IN THIS WINDOW - none was located in Friday trading or the weekend window - so",u)
    if not u.startswith("REVIEWED 03-OCTOBER"):
        u="REVIEWED 03-OCTOBER: no newer public disclosure located; status below carried. "+u
    r['update']=u

for s in [["Westmetall - LME official prices and stocks, 02-Oct-2026 session (EN+DE)",W],
          ["SMM - Q4 MJP offers Rio Tinto $280, South32 $265 (30-Sep-2026)",S_SMMQ],
          ["AL Circle - ex-China aluminium market awaits Q4 MJP settlement (02-Oct-2026)",S_ALCQ],
          ["Trading Economics - US dollar index, payrolls (02-Oct-2026)",S_TED],
          ["Trading Economics - US 10-year yield (02-Oct-2026)",S_TEY],
          ["Trading Economics - Brent crude (Oct-2026)",S_TEB],
          ["Rio Times - copper falls in base-metals selloff; Chile risks (02-Oct-2026)",S_RIO],
          ["Bloomberg - copper heads for weekly loss as high energy costs limit demand (02-Oct-2026)",S_BBG]]:
    d['sources'].append(s)
d['outlook']['sources'].append(["SMM - Q4 MJP offers (30-Sep-2026)",S_SMMQ])

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 02-OCTOBER-2026 LME OFFICIAL, CARRIED BECAUSE THE MARKET IS SHUT. This page compiled on SATURDAY 03-October; there is no LME ring on Saturday or Sunday, so Friday's official - also the weekly close - is the correct current figure until Monday 05-October 13:20 London.")
C[1]=("THE COMPLETENESS TEST PASSES: the per-metal daily tables for aluminium and copper show 02-October as the newest row with NO ROW AFTER IT and 01-October unchanged as the prior row; the other three metals reconcile through the cache-busted overviews and stock arithmetic.")
C[2]=("THE ENGLISH AND GERMAN OVERVIEWS WERE BOTH RE-REQUESTED CACHE-BUSTED AND AGREE EXACTLY on 02-October across all six metals, stocks and FX fixings.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against the levels carried for 01-October: aluminium -250 to 240,375; copper +575 to 248,650; nickel +486 to 285,168; zinc -225 to 123,750; lead -2,425 to 354,175.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (02-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (two sessions, 01- and 02-October) as their latest point. The stock chart axis floor was lowered to 230,000 t this run as visible stock approaches 235,000 t.")
C[6]=("PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND NO NEW PUBLIC ASSESSMENT WAS LOCATED FOR THIS WINDOW; every premium row is carried at its own assessment date. No Q4-2026 Japanese quarterly settlement has been publicly reported; the chart's pending band is now the latest reported OFFER range ($265-280/t: South32 and Rio Tinto per SMM, 30-September), replacing the earlier $280-310/t band. Offers are not settlements.")
for i,c in enumerate(C):
    if c.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent, the dollar index and the US ten-year are Trading Economics reference marks from the Friday 02-October session or its close; Trading Economics' own pages differ on whether Brent dipped below $100 intraday, so the board value ($102.25) is shown. EUR/USD is the 02-October LME fixing; European gas TTF is carried at its last reference session. Payroll figures are as published by Trading Economics. Hormuz transit counts remain disputed, so none is published.")
    if c.startswith("PEER EARNINGS ARE IN A LULL"):
        C[i]=("PEER EARNINGS ARE IN A LULL AND NO COMPANY WAS BACK-FILLED THIS RUN (03-October). The Q3-2026 reporting season opens in mid-October; existing earnings_history entries are unchanged and carry only exact publicly verified figures.")
    if c.startswith("THE ELLIOTT WAVE PANELS"):
        C[i]=c.split(' UPDATE 02-OCTOBER:')[0]+" UPDATE 03-OCTOBER: the daily count (C-wave from 3,374) is unchanged; the weekly alternate was promoted on its stated rule after the 02-October weekly close beneath 3,261."

ew=d['ew']; ew['updated']=RD
st=ew['short_term']
assert st['line'][-1]==[0.9978,3131.0], st['line'][-1]
st['line'].append([0.9989,3122.0])
st['now_x']=0.9994
st['proj']={"bull":[[0.9994,3122.0],[0.9997,3210],[1.0,3290]],
            "base":[[0.9994,3122.0],[0.9997,3090],[1.0,3140]],
            "bear":[[0.9994,3122.0],[0.9997,3050],[1.0,2980]]}
for f in st['fib']:
    if f['p']==3289.0: f['l']="3,289 - the 12-September (ii) high and the INVALIDATION of the bearish daily count. A daily official settlement above it negates the C-wave count. It is $167.00 above the 02-October three-month."
    if f['p']==3261.0: f['l']="3,261 - the shared 38.2% weekly retracement, held at the SAME price as the weekly panel. The 02-October weekly close settled $139.00 beneath it - the weekly test FAILED."
    if f['p']==3183.0: f['l']="3,183 - the 20-August low, BROKEN on 01-October and not regained (02-October three-month $3,122.00). First resistance on any rebound."
    if f['p']==3061.5: f['l']="3,061.5 - the 02-July C low and the next objective support, shared with the weekly panel (50% weekly retracement at 3,077). $60.50 beneath three-month."
st['fwd_pivots'][0]['w']="FIRST TEST BELOW: the 3,061.5 July low (and 3,077, the weekly 50% retracement), $60.50 beneath the 02-October three-month. A daily official settlement beneath it extends wave (iii) of C towards the 2,980 area (1.618 x wave (i) projected from 3,289)."
st['fwd_pivots'][1]['w']="THE INVALIDATION: 3,289, the 12-September (ii) high. A DAILY OFFICIAL SETTLEMENT ABOVE IT negates the bearish C-wave count and restores the possibility that the 3,061.5-3,374 advance was the first leg of a new uptrend."
st['writeup']=("DAILY (SWING DEGREE) - THE C-WAVE COUNT IS UNCHANGED AND CONFIRMED BY A SECOND LOWER SETTLEMENT. Three-month settled $3,122.00 on Friday 02-October, a new low for the decline from 3,374, after $3,131.00 on Thursday. "
 "BASE CASE, ABOUT 62%: the 3,061.5-3,374 rally was a corrective B wave and a C-wave decline is under way, with (i) at 3,183, (ii) at 3,289 on 12-September and (iii) in progress; the cardinal rules hold - (ii) did not exceed the 3,374 origin and (iii) already extends beyond (i). Friday's small $9 fall suggests a minor pause inside (iii) rather than its end. Targets: the 3,061.5 July low first, then about 2,980 where (iii) equals 1.618 times (i). "
 "ALTERNATE, ABOUT 38%: a deep expanded flat or double-three that holds above 3,061.5 and resumes higher; it needs a recovery above 3,183. "
 "INVALIDATION: a daily official settlement above 3,289, $167.00 above the 02-October three-month. CONFIDENCE IS MODERATE. This is technical context, not advice.")
lt=ew['long_term']
lt['fwd_pivots'][0]['w']=("THE 3,261 LEVEL - THE 38.2% RETRACEMENT OF THE 3,855-TO-3,061.5 DECLINE - WAS THE WEEKLY TEST AND IT FAILED: Friday 02-October's weekly close settled three-month at $3,122.00, $139.00 beneath it, after holding at $3,267.00 on 25-September. Per the pre-registered rule the weekly alternate (the move off 3,061.5 was corrective) is promoted. 3,261 is now overhead resistance.")
lt['fwd_pivots'][1]['w']=("THE DOWNSIDE REFERENCES ARE SHARED WITH THE DAILY PANEL: the 50% retracement at 3,077 (held on the 3,061.5 low of 02-July), now $45.00 beneath the 02-October three-month of $3,122.00, and the 61.8% at 2,894, where the bear path terminates. A WEEKLY close beneath 3,077 invalidates the constructive count outright. Overhead, the 23.6% retracement at 3,488 is $366.00 above.")
lt['writeup']=("WEEKLY (POSITION DEGREE) - THE WEEKLY CLOSE FAILED THE TEST AND THE ALTERNATE IS PROMOTED. The 3,855 high of 02-June terminates the position-degree advance; the decline into 3,061.5 on 02-July is a completed A-B-C and the 50% retracement at 3,077 held. Friday 02-October's weekly close at $3,122.00 sits $139.00 beneath the 3,261 retracement. "
 "PREFERRED COUNT NOW, ABOUT 55% (up from about 45%): the move off 3,061.5 was corrective - a B wave or the opening leg of a larger fourth wave - and the decline under way breaks the 2,950-3,110 zone towards the 61.8% retracement at 2,894. "
 "ALTERNATE, ABOUT 45%: a new position-degree advance is still building off 3,061.5 as long as that low holds on a weekly close; targets 3,488, then 3,680 and 3,840 into mid-2027. "
 "INVALIDATION: a weekly close beneath 3,077 invalidates the constructive alternate outright; a weekly close back above 3,261 would restore it as preferred. CONFIDENCE IS LOW-TO-MODERATE. This is technical context, not advice.")
lt['proj']={"bull":[[0.66,3122.0],[0.76,3380],[0.88,3600],[1.0,3800]],"base":[[0.66,3122.0],[0.78,3120],[0.9,3230],[1.0,3290]],"bear":[[0.66,3122.0],[0.8,2970],[1.0,2890]]}

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-01', ph['rows'][-1]
ph['rows'][-1]=['2026-10-02',cash,m3,stk]
ph['updated']=RD
ph['basis']=("London Metal Exchange official settlements via Westmetall. LME Aluminium official cash settlement, official 3-month, and LME warehouse stock. Weekly sampling (last published official session of each week). AT THE 03-OCTOBER-2026 UPDATE the row for the week of 28-September is FINAL: the Friday 02-October session (cash 3,109.50, 3-month 3,122.00, stock 240,375 t). Verified against both cache-busted Westmetall language overviews and the per-metal aluminium daily table.")
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok', d['metals_board'], mh['al'][-1], mh['zn'][-1], mh['pb'][-1], round(tl,2), round(share,1), round(ratio,2))
