# Daily data refresh - 2026-10-08 (THURSDAY, compiled ~03:40 London BEFORE the ring). Board ROLLED to WEDNESDAY 07-Oct LME official.
# EN+DE cache-busted overviews agree exactly on 07-Oct; Al per-metal table shows 07-Oct newest (no later row), 06-Oct prior unchanged; 5/5 stock lines reconcile.
import json, re
P='market_data.json'
d=json.load(open(P,encoding='utf-8'))
RD='2026-10-08'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TEA="https://tradingeconomics.com/commodity/aluminum"
S_TED="https://tradingeconomics.com/united-states/currency"
S_TEB="https://tradingeconomics.com/commodity/brent-crude-oil"
S_CRU="https://www.alcircle.com/news/asian-aluminium-premium-slips-to-202-t-as-mjp-q4-offers-fall-to-245-260-121444"
S_ALCM="https://www.alcircle.com/news/ex-china-aluminium-market-runs-steadily-as-market-awaits-q4-mjp-settlement-121397"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']

cash,prev_c,m3,prev_m,stk,prev_s=3102.5,3134.5,3114.0,3148.5,238875,238875
spr=cash-m3
pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100

VER=("COMPILED THURSDAY 08-OCTOBER-2026 BEFORE THE LONDON RING (~03:40 LONDON). THE BOARD ROLLED THIS RUN TO THE WEDNESDAY 07-OCTOBER-2026 LONDON METAL EXCHANGE OFFICIAL, THE LATEST PUBLISHED SESSION; TODAY'S OFFICIAL DOES NOT PRINT UNTIL 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted English and German Westmetall overviews AGREE EXACTLY on 07-October across all six metals, all six stock lines and the foreign-exchange fixings; (2) the aluminium per-metal daily table shows 07-October as the newest row - NO ROW AFTER IT - with 06-October reproduced unchanged as the prior row; "
 "(3) ALL FIVE STOCK LINES RECONCILE against the levels carried for 06-October: aluminium 238,875 unchanged; copper 242,975 less 3,100 to 239,875; nickel 284,178 unchanged; zinc 127,275 PLUS 475 to 127,750; lead 349,625 less 225 to 349,400. "
 "The whole board sits on ONE UNIFORM SESSION (07-October) and no intraday, closing, reference or contract-for-difference mark is used anywhere in it. Prior-month averages remain the completed SEPTEMBER-2026 official means. NEXT OFFICIAL: THURSDAY 08-OCTOBER, 13:20 LONDON.")

AL=(f" CASH SETTLED $3,102.50 ON THE 07-OCTOBER OFFICIAL, DOWN $32.00 OR {pc:.2f}% FROM $3,134.50. THREE-MONTH SETTLED $3,114.00, DOWN $34.50 OR {pm:.2f}% FROM $3,148.50 - A NEW LOW FOR THE MOVE, BENEATH THE 3,118.00 SETTLEMENT OF 05-OCTOBER; Trading Economics (07-October) describes UK aluminium futures at their lowest since early July. "
 "SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS AGAIN: three-month fell $2.50 more than cash, so the CONTANGO NARROWED TO $11.50 from $14.00 even as the price fell - the structure did not confirm the drop. "
 "VISIBLE LME STOCK WAS UNCHANGED AT 238,875 TONNES. Three-month now sits $52.50 above the 3,061.5 July low, $69.00 beneath the broken 3,183 level and $175.00 beneath the 3,289 daily invalidation. "
 "The LME euro fixing fell to 1.1183 from 1.1268, a firmer dollar at that ring; Trading Economics (08-October) has the dollar index near 102.2 after Fed minutes showed most policymakers favour another hike by year-end, and the US ten-year near 5.31%.")

d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,102.5","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,114.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $147.00 BELOW 3,261, $69.00 BELOW THE BROKEN 3,183 DAILY LEVEL, $175.00 BELOW THE 3,289 DAILY INVALIDATION, $37.00 above the 3,077 weekly 50% retracement and $52.50 above the 3,061.5 July low."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-11.5","pos":False,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,102.50 against three-month $3,114.00 is an $11.50 CONTANGO, NARROWED $2.50 from $14.00. Spread and flat price moved in OPPOSITE directions on this ring (price down, contango narrower). The published reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"238,875","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK WAS UNCHANGED AT 238,875 TONNES, holding the new low for the series on this page set on 06-October. September's mean stock was {sep_s:,} tonnes. Flat stock alongside a narrow contango says the visible stock is not the driver of the price drop."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,114.00, DOWN $34.50 OR {pm:.2f}% FROM $3,148.50, a new low for the move. AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK UNCHANGED AT 238,875 TONNES. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-14.0,"avg":sep_sp,"note":VER+f" AN $11.50 CONTANGO, NARROWED $2.50 FROM $14.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in OPPOSITE directions on this ring (price lower, contango narrower). PUBLISHED REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1183,"prev":1.1268,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.11830 FROM 1.12680 at the Wednesday ring; the ECB fixing printed 1.11770 and BFIX 1.11798, so all three agree on a firmer dollar at that session. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]

d['outlook']['forward_path']=[
 {"tenor":"Cash (07-Oct official)","price":"3,102.5","basis":f"THE 07-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,102.50, DOWN $32.00 OR {pc:.2f}%. Next official Thursday 08-October 13:20 London."},
 {"tenor":"3-month (07-Oct official)","price":"3,114.0","basis":f"THE 07-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,114.00, DOWN $34.50 OR {pm:.2f}%, a new low for the move: $147.00 beneath 3,261, $69.00 beneath the broken 3,183, $52.50 above the 3,061.5 July low."},
 {"tenor":"Cash-to-3M structure","price":"-11.5 (CONTANGO)","basis":"An $11.50 CONTANGO, narrowed $2.50 from $14.00. Flat price and spread moved in OPPOSITE directions."},
 {"tenor":"Visible LME stock","price":"238,875 t","basis":f"UNCHANGED on the session; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE CURVE FIRMED SLIGHTLY EVEN AS THE PRICE FELL. On the 07-October official cash $3,102.50 sits $11.50 BELOW three-month $3,114.00, a CONTANGO narrowed $2.50 from $14.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00 and now $11.50. "
 f"READ: an orderly, narrow contango - not a glut signal, with visible stock flat at 238,875 t; the drop was a flat-price (macro and premium) move, not a structural one. The September mean spread was ${sep_sp:,.2f}. The published reversal condition (a backwardation beyond $15.00) remains far away; a contango beyond $24.50 would be the bearish structural confirmation.")

ls=d['lme_series']; assert ls[-1][0]=='06-Oct', ls[-1]
d['lme_series']=ls[1:]+[["07-Oct",cash,m3,stk]]
d['chart_price_axis']=[3000,3450]
d['chart_stock_axis']=[225000,255000]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(3000<r[1]<3450 and 3000<r[2]<3450 for r in d['lme_series'])
# (cash, 3M, prev cash, prev 3M)
CU=(14510.0,14422.0,14505.0,14434.0); NI=(15645.0,15840.0,15530.0,15720.0); ZN=(3799.0,3756.0,3803.0,3766.0); PB=(1844.5,1884.0,1837.5,1880.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# zn/pb 'now' = October cash average-to-date: 01-, 02-, 05-, 06- and 07-Oct sessions. Prior point was the four-session average.
zn_old=(3834.0+3798.0+3774.0+3803.0)/4; pb_old=(1837.0+1827.0+1829.5+1837.5)/4
zn_avg=(3834.0+3798.0+3774.0+3803.0+3799.0)/5; pb_avg=(1837.0+1827.0+1829.5+1837.5+1844.5)/5
mh['zn'][-1]=round(mh['zn'][-1]*zn_avg/zn_old,1); mh['pb'][-1]=round(mh['pb'][-1]*pb_avg/pb_old,1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])): R[k]=R[k][1:]+[v]
ms['asof']='2026-10-07'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending WEDNESDAY 07-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 16-September dropped and 07-October appended, so the window is 17-September to 07-October. Every point is an official cash settlement, verified against the cache-busted Westmetall English and German overviews, which agree to the cent, the aluminium per-metal daily table (no row after 07-October), and five-for-five stock-line reconciliation. Next official Thursday 08-October.")
ms['src']=["Westmetall - LME official cash settlements, EN and DE overviews cache-busted and in exact agreement (07-October-2026 session)",W]

AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,510.00, up $5.00 or 0.03%; three-month $14,422.00, DOWN $12.00 or 0.08%. The BACKWARDATION WIDENED to $88.00 from $71.00 while stock DREW 3,100 tonnes to 239,875 - prompt tightness firming for another session even as the forward eased."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,645.00, up $115.00 or 0.74%; three-month $15,840.00, up $120.00 or 0.76% - the strongest gain on the board. CONTANGO $195.00 from $190.00, still the widest carry on the board. Stock unchanged at 284,178."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,799.00, down $4.00 or 0.11%; three-month $3,756.00, down $10.00 or 0.27%. The BACKWARDATION widened to $43.00 from $37.00 while stock rose 475 tonnes to 127,750. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,844.50, up $7.00 or 0.38%; three-month $1,884.00, up $4.00 or 0.21%. CONTANGO narrowed to $39.50 from $42.50. Stock drew 225 tonnes to 349,400, a thirteenth consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL, REPORTED AS DATA NOT AS A REGIME SIGNAL: on the Wednesday 07-October official aluminium was the clear laggard in three-month terms - aluminium -1.10%, zinc -0.27%, copper -0.08%, lead +0.21%, nickel +0.76% - while the LME euro fixing fell to 1.1183 from 1.1268. An aluminium-specific drop (Asian premium weakness, supply-recovery narrative) on a firmer-dollar day, rather than a complex-wide sell-off.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

OLDH="COMPILED WEDNESDAY 07-OCTOBER-2026, BEFORE THE LME RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY)."
NEWH="COMPILED THURSDAY 08-OCTOBER-2026, BEFORE THE LME RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY, REOPENING 09-OCTOBER)."
n_rep=0
for i in d['inputs']:
    if isinstance(i.get('src'),str) and OLDH in i['src']: i['src']=i['src'].replace(OLDH,NEWH); n_rep+=1
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='06-Oct'
        i['hist']=i['hist'][1:]+[["07-Oct",CU[0]]]
        assert len(i['hist'])==15
        i['val']="~14,422.00 (3M); 14,510.00 (cash) $/t"
        i['ratio']="~14,510.00 $/t cash vs LME 3M 14,422.00 $/t"
        i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the WEDNESDAY 07-OCTOBER-2026 session at $14,510.00, UP $5.00 or 0.03% against $14,505.00. THE WINDOW ROLLED THIS RUN: 16-September dropped and 07-October appended, so the series is the last fifteen published official cash sessions, 17-September to 07-October - the same window as the LME Board sparklines. Official settlement only, verified on the cache-busted Westmetall English and German overviews, which agree to the cent. "
                  "Copper structure for context: backwardation $88.00 (from $71.00), stock drew 3,100 t to 239,875 t.")
print('inputs header replaced', n_rep)
d['inputs_summary']=("UPDATE 08-OCTOBER (THURSDAY, PRE-RING): copper rolled to the Wednesday 07-October LME official cash of $14,510.00, up $5.00, with its fifteen-session window moved to 17-September to 07-October. No other input mark printed in this window - China is on the last day of its 01-08 October National Day holiday, so the SMM fluoride, silicon and magnesium weeklies are expected from 09-October onward, and the carbon settlement cycle (anodes, pitch, green coke) is mid-October - so every other row is carried at its own dated public mark and no value was interpolated.")
nr=0
for r in d['raw_materials']:
    if isinstance(r.get('src'),str) and OLDH in r['src']: r['src']=r['src'].replace(OLDH,NEWH); nr+=1
print('raw header replaced', nr)

ratio=360.4/m3*100
ALNOTE=("COMPILED THURSDAY 08-OCTOBER-2026 (PRE-RING). NO NEW DATED PUBLIC ALUMINA MARK WAS LOCATED FOR THIS WINDOW: the LME Alumina (Platts) row stays at AL Circle's $360.40/t print of 30-September; the FOB East Australia trade row stays at its 18-September mark; SMM separately reported 30,000 t traded at $369/t FOB Western Australia on 30-September for November shipment (a different basis, reported in news only). The SMM alumina index is carried at its 30-September print of 2,669.99 yuan/tonne; SHFE is closed 01-08 October and reopens 09-October. "
 f"THE RATIO: LME Alumina at $360.40/t against the 07-October aluminium three-month of $3,114.00 is {ratio:.2f}%, against a decade norm of 15-17%. Alumina remains historically CHEAP relative to metal.")
for a in d['alumina']: a['src']=ALNOTE

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
PREM=("COMPILED THURSDAY 08-OCTOBER-2026 (PRE-RING). PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND THIS PANEL CARRIES EACH ROW AT ITS OWN LAST PUBLIC ASSESSMENT DATE. NO NEW ASSESSMENT ON ANY ROW'S OWN BASIS WAS LOCATED FOR THIS WINDOW, so every row is CARRIED UNCHANGED. CONTEXT FROM A DIFFERENT ASSESSOR, NOT MIXED INTO ANY ROW: AL Circle (06-October) reports CRU's Asia CIF premium at $202/t and Q4 MJP offers down to $245-260/t from $325/t in early September, against the $395/t Q3 benchmark; earlier SMM reporting (30-September) had Rio Tinto at $280/t and South32 at $265/t. No Q4 settlement had been publicly reported when this page compiled. These are offers, not a settlement. "
 f"THE TARIFF DECOMPOSITION IS REFRESHED DAILY BY DESIGN: on a re-verified Section 232 rate of 50% on aluminium articles applied to full customs value, the tariff leg of the US duty-paid premium is 0.50 times the 07-October official cash of $3,102.50, or ${tl:,.2f}, DOWN $16.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}% of the US duty-paid premium is policy arithmetic rather than market. "
 "This page does NOT fabricate freight, financing or tightness splits for any premium row.")
for p in d['premiums']:
    s=p['src']; j=s.find("for any premium row.")
    if s.startswith("COMPILED") and j>0: p['src']=PREM+s[j+len("for any premium row."):]
    else: p['src']=PREM+" "+s
pq=d['premium_quarters']; assert pq[-1]['q']=='Q4-26' and pq[-1]['v'] is None
pq[-1]['range']=[245,280]
pdv=d['premium_drivers'][0]
pdv['d']=("Q4 MJP OFFERS HAVE FALLEN AGAIN AND NO SETTLEMENT IS YET REPORTED: AL Circle (06-October) reports Q4 offers at $245-260/t, down from $325/t in early September, and CRU's Asia CIF premium at $202/t, against a Q3 settlement of $395/t; it cites weak demand, cautious buyers, rising regional inventories and reluctance to hold metal on long routes. Earlier SMM reporting (30-September) had Rio Tinto at $280/t and South32 at $265/t. WHY IT LANDS ON PREMIUMS: the quarterly MJP is the reference for much Asian physical business, so a settlement in the $245-280 band would reset the regional premium level down by roughly 30-38% for the quarter. The LME curve offers no exchange-side scarcity signal either: an $11.50 contango on 07-October.")
pdv['src']=["AL Circle - Asian aluminium premium slips to $202/t as MJP Q4 offers fall to $245-260 (06-Oct-2026)",S_CRU]

d['lme_commentary']=(f"ALUMINIUM GAVE BACK TUESDAY'S BOUNCE AND SET A NEW LOW FOR THE MOVE. On the Wednesday 07-October official cash settled $3,102.50, down $32.00 or {pc:.2f}%, and three-month $3,114.00, down $34.50 or {pm:.2f}% - beneath the 3,118.00 settlement of 05-October; Trading Economics puts UK futures at their lowest since early July, citing a stronger dollar and a more ample supply outlook (smelter restarts, Chinese exports up 17.2% year on year in August). "
 "The contango NARROWED $2.50 to $11.50 while the price fell (spread and price in OPPOSITE directions) and visible stock was unchanged at 238,875 t, so the drop was not structural. "
 "Aluminium was the clear laggard on a mixed board - nickel and lead rose, copper and zinc were near flat - and the LME euro fixing fell to 1.1183; Fed minutes released Wednesday showed most policymakers favour another hike by year-end (Trading Economics), with the dollar index near 102.2 and the US ten-year near 5.31%. "
 f"China's markets reopen on 09-October. September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND REASSERTED, STRUCTURE STILL NOT CONFIRMING. Against: three-month made a new low for the move at 3,114 and remains $69.00 under the broken 3,183; the Fed minutes leaned hawkish and the dollar and US yields remain near multi-year highs; Asian premium offers have slipped again to $245-260/t (CRU Asia CIF $202/t) versus $395/t in Q3; Gulf restarts are progressing and Chinese exports are elevated. "
 "Constructive: the contango narrowed rather than widened on the drop; visible LME stock is holding at a series low (238,875 t); the 3,061.5 July low is still $52.50 below; Brent back near $102 props the energy cost floor.")
d['commercial']=("COMMERCIAL READ - GENERIC AND PUBLIC. FIRST, THE CURVE STILL PAYS BUYERS A LITTLE TO WAIT: an $11.50 contango on 07-October, slightly narrower. SECOND, ASIAN PREMIUMS ARE RESETTING LOWER: public reporting has Q4 MJP offers at $245-260/t (AL Circle, 06-October) and CRU's Asia CIF at $202/t, against $395/t in Q3; no settlement is yet reported. THIRD, THE TARIFF ARITHMETIC MOVED WITH THE METAL: "
 f"on a verified 50% Section 232 rate, the tariff leg of the US Midwest duty-paid premium is ${tl:,.2f} on 07-October cash, {share:.1f}% of the $2,403/t premium. FOURTH, WATCH THE CALENDAR: a Q4 Japanese premium settlement could come any day; 3,061.5 is the next downside reference and 3,183 the resistance; China returns from holiday on 09-October. This is generic public market context, not advice.")

# scenario weights moved
for s in d['outlook']['scenarios']:
    dr=s['drivers']
    dr=re.sub(r"^HELD 07-OCTOBER: .*?move the weights\. ","",dr)
    dr=dr.replace("LAST MOVED 03-OCTOBER","PREVIOUSLY MOVED 03-OCTOBER",1)
    s['prob']={'Bull':'13%','Base':'45%','Bear':'42%'}[s['case']]
    s['drivers']=("MOVED 08-OCTOBER (from 14/47/39 to 13/45/42): the 07-October official reversed the whole of Tuesday's bounce and settled three-month at a new low for the move (3,114, beneath 3,118), on hawkish Fed minutes and a further slide in Asian premium offers to $245-260/t; the bear case gains three points. The contango narrowing to $11.50 and flat stock argue against a bigger shift. ")+dr
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['bottom_line']=(f"BOTTOM LINE: aluminium settled on the 07-October LME official at cash $3,102.50 and three-month $3,114.00, down {abs(pm):.2f}% - a new low for the move and the weakest metal on the board. "
 "The contango narrowed to $11.50 and visible stock held at 238,875 t, so the structure did not confirm the drop. Scenario weights move to 13% bull / 45% base / 42% bear; the daily Elliott count (a C-wave decline from 3,374) now reads wave (iv) complete at 3,148.5 and wave (v) under way towards 3,061.5, with 3,183 and 3,289 the invalidation levels; the weekly alternate remains preferred at about 55%.")

d['so_what']={"line":"Aluminium erased Tuesday's bounce and hit its lowest level since early July as hawkish Fed minutes lifted the dollar and Asian premium offers slid again - the downtrend is back in charge, with $3,061.5 the next support.",
 "points":[
 f"WHAT MOVED: Wednesday's LME official settled cash at $3,102.50 (-$32.00) and three-month at $3,114.00 (-$34.50, {pm:.2f}%), a new low for the move; aluminium was the weakest metal on a mixed board. The contango narrowed to $11.50 and LME stock was unchanged at 238,875 t.",
 "WHY: Fed minutes showed most policymakers favour another hike by year-end, keeping the dollar index near 102.2 and the US ten-year near 5.31% (Trading Economics); the supply outlook keeps improving as smelters restart and Chinese exports run high (+17.2% year on year in August).",
 "PREMIUMS: Q4 Japanese premium offers have slipped to $245-260/t and CRU's Asia CIF premium to $202/t (AL Circle, 06-October), against $395/t in Q3 - Asian physical demand is soft and regional stocks are building. No settlement yet.",
 "WHAT TO WATCH: today's LME official against the 3,061.5 July low (and 3,183 above); a Q4 Japanese premium settlement; Chinese markets reopening on 09-October and whether SHFE follows London lower."]}

new_feed=[
 {"when":"Thu 08-Oct","impact":"Bearish","text":f"BOARD ROLLED TO THE WEDNESDAY 07-OCTOBER LME OFFICIAL. Cash $3,102.50 (-$32.00), three-month $3,114.00 (-$34.50, {pm:.2f}%) - a new low for the move - contango NARROWED to $11.50 from $14.00 (opposite to price), stock unchanged at 238,875 t. Verified on cache-busted English and German overviews in exact agreement, the aluminium per-metal table with no later row, and five-for-five stock reconciliation."},
 {"when":"Thu 08-Oct","impact":"Bearish","text":"FED MINUTES LEAN HAWKISH (Trading Economics): all 19 policymakers backed the September hike and most see another increase as appropriate by year-end; markets price about 78% odds of a December hike. Dollar index near 102.2; US ten-year near 5.31%."},
 {"when":"Thu 08-Oct","impact":"Mixed","text":"BRENT BACK NEAR $102 (Trading Economics): reports of US strike options against Iran and over 510,000 b/d of Gulf of Mexico output shut in by Tropical Storm Isaias outweighed slowly recovering Middle East exports."},
 {"when":"Tue 06-Oct","impact":"Bearish (premium)","text":"ASIAN PREMIUMS SLIDE (AL Circle, 06-October): CRU's Asia CIF premium at $202/t; Q4 MJP offers fall to $245-260/t from $325/t in early September, versus the $395/t Q3 benchmark; regional inventories rising, buyers cautious."},
 {"when":"Wed 07-Oct","impact":"Mixed","text":"BASE METALS MIXED AT THE WEDNESDAY OFFICIAL: aluminium -1.10% three-month, zinc -0.27%, copper -0.08% with backwardation widening to $88, lead +0.21%, nickel +0.76%."},
]
d['feed']=(new_feed+d['feed'])[:12]

new_news=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":f"LME ALUMINIUM SETS A NEW LOW FOR THE MOVE. The Wednesday 07-October official settled cash at $3,102.50 ({pc:.2f}%) and three-month at $3,114.00 ({pm:.2f}%), erasing Tuesday's bounce and settling beneath the 3,118.00 of 05-October; Trading Economics describes UK futures at their lowest since early July. The contango narrowed to $11.50 from $14.00 and visible stock was unchanged at 238,875 t."},
 {"theme":"Premiums","horizon":"Weeks","impact":"Bearish (premium)","url":S_CRU,
  "headline":"ASIAN ALUMINIUM PREMIUM SLIPS TO $202/T AS Q4 MJP OFFERS FALL TO $245-260 (AL Circle, 06-October): CRU's Asia CIF premium is well below the $395/t Q3 MJP benchmark; Q4 offers have fallen from $325/t in early September. Korea, Malaysia and Taiwan premiums are under most pressure; demand is weak, buyers cautious and regional inventories rising, while Middle East tensions have reduced East-to-West flows."},
 {"theme":"Macro","horizon":"Days-weeks","impact":"Bearish","url":S_TED,
  "headline":"FED MINUTES POINT TO ANOTHER HIKE (Trading Economics, 08-October): all 19 policymakers backed the September increase and most judged a further rise appropriate by year-end; markets price about 78% odds of a December hike. The dollar index is near 102.2, up about 3.4% over the month, and the US ten-year yield near 5.31%. A firm dollar and high carrying costs weigh on dollar-priced metals."},
 {"theme":"Supply","horizon":"Months","impact":"Bearish (supply)","url":S_TEA,
  "headline":"SUPPLY OUTLOOK SEEN MORE AMPLE (Trading Economics, 07-October): several smelters are restarting idled capacity and others expanding, pointing to a gradual supply recovery, while Chinese aluminium exports rose 17.2% year on year in August on weak domestic demand and high inventories, cushioning Gulf production losses."},
 {"theme":"Energy","horizon":"Days-weeks","impact":"Mixed","url":S_TEB,
  "headline":"BRENT REBOUNDS ABOVE $101 (Trading Economics, 08-October): reports that the US administration requested strike options against Iran, and more than 510,000 b/d of Gulf of Mexico output shut in by Tropical Storm Isaias, outweighed Middle East exports slowly returning towards pre-war levels; tanker attacks in the Strait of Hormuz remain a supply risk. Higher energy supports the smelter cost floor at the margin."},
]
d['news']=new_news+d['news'][:15]

cats=d['outlook']['catalysts']
for c in cats:
    if c['date']=='Daily, from Wed 07-Oct':
        c['date']='Daily, from Thu 08-Oct'
        c['event']="3,061.5 BELOW, 3,183 OVERHEAD, 3,289 INVALIDATION. Three-month settled $3,114.00 on 07-October, a new low for the move, $52.50 above the 02-July low at 3,061.5 and $69.00 beneath the broken 3,183 level. Beneath 3,061.5 opens the 2,980 area (wave (v) of C); a daily official settlement above 3,183 would void the impulsive C-wave labelling; above 3,289 negates the bearish daily count."
    if c['date']=='Any day (pending)':
        c['event']="Q4-2026 JAPANESE QUARTERLY PREMIUM (MJP) SETTLEMENT. Latest public offers $245-260/t (AL Circle, 06-October), after $265-280/t from South32 and Rio Tinto (SMM, 30-September); CRU's Asia CIF premium is $202/t; versus $395/t in Q3. Not yet reported as settled at 08-October."
    if c['date']=='Thu 01-Oct to Thu 08-Oct':
        c['event']=c['event'].split(' UPDATE 08-OCTOBER')[0]+" UPDATE 08-OCTOBER: final holiday day; Chinese markets (SHFE, SMM assessments) reopen Friday 09-October - the first test of whether Shanghai follows London's slide to a three-month low."
d['outlook']['catalysts']=cats

RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 08-OCTOBER: the contango NARROWED $2.50 to $11.50 on 07-October even as the price fell. Well inside the $24.50 bearish-confirmation threshold. Trend held at FLAT."
RK[1]['risk']+=" UPDATE 08-OCTOBER: Fed minutes showed most policymakers favour another hike by year-end; markets price about 78% odds of a December hike; dollar index near 102.2, US ten-year near 5.31% (Trading Economics). Trend held at UP."
RK[4]['risk']+=" UPDATE 08-OCTOBER: LME stock unchanged at 238,875 t on 07-October, holding the series low. Trend held at FLAT."
RK[7]['risk']+=" UPDATE 08-OCTOBER: Brent rebounded towards $102 on Iran strike-option reports and storm shut-ins in the Gulf of Mexico (Trading Economics, 08-October). Trend held at FLAT."
RK[8]['risk']+=" UPDATE 08-OCTOBER: Q4 offers slipped further to $245-260/t and CRU's Asia CIF premium to $202/t (AL Circle, 06-October); no settlement reported. Trend held at DOWN."
RK[10]['risk']+=" UPDATE 08-OCTOBER: Trading Economics (07-October) cites several smelters restarting idled capacity and Chinese exports up 17.2% year on year in August. Trend held at UP."

d['outlook']['ai_analysis'][0]=(f"THURSDAY PRE-RING REVIEW, 08-OCTOBER: Wednesday's official erased Tuesday's bounce and set a new low for the move (three-month $3,114.00, {pm:.2f}%), with aluminium the weakest metal on a mixed board. The drivers were aluminium-specific and macro - Asian premium offers sliding to $245-260/t and hawkish Fed minutes lifting the dollar - rather than structural: the contango narrowed to $11.50 and stock was flat. The bear case is raised to 42%; the 3,061.5 July low is now the key support, and China's reopening on 09-October is the next test.")

for l in d['logistics']:
    if l['name']=='Strait of Hormuz transit':
        rest=l['note'].split(' PRIOR: ',1)[-1]
        l['note']=("REVIEWED THURSDAY 08-OCTOBER-2026. Trading Economics' Brent coverage (08-October) says Middle East exports are slowly returning towards pre-war levels but attacks on tankers in the Strait of Hormuz still pose a supply risk, and reports of US strike options against Iran revived escalation concerns. No container or bulk transit count is published because tracker figures remain disputed. Arrow stays UP pending a public, verifiable normalisation signal for dry-bulk and container traffic. PRIOR: "+rest)
        l['src']="REVIEWED THURSDAY 08-OCTOBER-2026: Trading Economics Brent ("+S_TEB+"). PRIOR: "+l['src'].split(' PRIOR: ',1)[-1]
    if l['name'].startswith('Red Sea'):
        l['note']=re.sub(r"^REVIEWED WEDNESDAY 07-OCTOBER-2026 \(.*?\):","REVIEWED THURSDAY 08-OCTOBER-2026 (no newer public transit count located; earlier note carried; Trading Economics, 08-October, reports Houthi attacks on Saudi targets prompting new coalition strikes in Yemen):",l['note'],count=1)

for m in d['macro']:
    if m['name'].startswith('Brent'):
        m['value']='101.97'; m['day']="+1.77% in Thursday 08-October trade; +0.75% over the month (Trading Economics)"
        m['note']="REFRESHED THURSDAY 08-OCTOBER-2026 on a public reference board (Trading Economics): Brent rose back above $101 on reports of US strike options against Iran and more than 510,000 b/d of Gulf of Mexico output shut in by Tropical Storm Isaias, while Middle East exports slowly recover. Energy is a major smelter cash-cost line."
    elif m['name'].startswith('US dollar index'):
        m['value']='102.16'; m['day']="-0.12% in Thursday 08-October trade; +3.38% over the month (Trading Economics)"
        m['note']="REFRESHED THURSDAY 08-OCTOBER-2026 on a public reference board (Trading Economics): Fed minutes showed all 19 policymakers backed the September hike and most see another rise by year-end; about 78% odds priced for a December hike. A firm dollar weighs on dollar-priced metals."
    elif m['name'].startswith('US 10-year'):
        m['value']='5.31'; m['day']="about 5.307% in Thursday 08-October trade, +1bp; eased from a 24-year high (Trading Economics)"
        m['note']="REFRESHED THURSDAY 08-OCTOBER-2026 on a public reference board (Trading Economics). Higher yields raise the cost of carrying metal and financing inventory."
    elif m['name']=='EUR/USD':
        m['value']='1.11830'; m['day']="LME fixing on 07-October, -0.75% from 1.12680; ECB fixing 1.11770, BFIX 1.11798"
        m['note']="REFRESHED THURSDAY 08-OCTOBER-2026 to the 07-October LME fixing via Westmetall, the same session as the LME board."

for r in d['producer_status']:
    r['asof']=RD
    u=r['update']
    for a,b in (("REVIEWED 07-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE","REVIEWED 08-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE"),
                ("REVIEWED 07-OCTOBER: no newer public disclosure located; status below carried. ","REVIEWED 08-OCTOBER: no newer public disclosure located; status below carried. ")):
        if u.startswith(a): u=b+u[len(a):]; break
    else:
        u="REVIEWED 08-OCTOBER: no newer public disclosure located; status below carried. "+u
    r['update']=u

for s in [["Westmetall - LME official prices and stocks, 07-Oct-2026 session (EN+DE)",W],
          ["Trading Economics - aluminium (07/08-Oct-2026)",S_TEA],
          ["Trading Economics - US dollar index, Fed minutes and US 10-year (08-Oct-2026)",S_TED],
          ["Trading Economics - Brent crude (08-Oct-2026)",S_TEB],
          ["AL Circle - Asian aluminium premium slips to $202/t as MJP Q4 offers fall to $245-260 (06-Oct-2026)",S_CRU]]:
    d['sources'].append(s)
d['outlook']['sources'].append(["AL Circle - Asian aluminium premium slips to $202/t; MJP Q4 offers $245-260 (06-Oct-2026)",S_CRU])
d['premium_settlement_src']=["AL Circle - Asian aluminium premium slips to $202/t as MJP Q4 offers fall to $245-260 (06-Oct-2026)",S_CRU]

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE WEDNESDAY 07-OCTOBER-2026 LME OFFICIAL. This page compiled on THURSDAY 08-October at about 03:40 London, before the ring; today's official prints at 13:20 London, so Wednesday's official is the latest published figure.")
C[1]=("THE COMPLETENESS TEST PASSES: the aluminium per-metal daily table shows 07-October as the newest row with NO ROW AFTER IT and 06-October unchanged as the prior row; the other metals reconcile through the cache-busted overviews and stock arithmetic.")
C[2]=("THE ENGLISH AND GERMAN OVERVIEWS WERE BOTH REQUESTED CACHE-BUSTED ON 08-OCTOBER AND AGREE EXACTLY on 07-October across all six metals, stocks and FX fixings.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against the levels carried for 06-October: aluminium unchanged at 238,875; copper -3,100 to 239,875; nickel unchanged at 284,178; zinc +475 to 127,750; lead -225 to 349,400.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (07-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (five sessions, 01-, 02-, 05-, 06- and 07-October) as their latest point. The stock chart axis floor (225,000 t) brackets visible stock at 238,875 t.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,102.50 against three-month $3,114.00 is therefore an $11.50 CONTANGO, narrowed $2.50 from $14.00 on 06-October - and it narrowed while the flat price fell, i.e. spread and price moved in OPPOSITE directions."
C[6]=("PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND NO NEW ASSESSMENT ON ANY ROW'S OWN BASIS WAS LOCATED FOR THIS WINDOW; every premium row is carried at its own assessment date. CRU's Asia CIF $202/t (AL Circle, 06-October) is a different assessor's basis and is reported in drivers and news only, not substituted into the CIF Japan row. No Q4-2026 Japanese quarterly settlement had been publicly reported when this page compiled on 08-October; the chart's pending band is the span of reported OFFERS ($245-280/t: $245-260 per AL Circle 06-October; $265-280 South32 and Rio Tinto per SMM 30-September). Offers are not settlements.")
for i,c in enumerate(C):
    if c.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a re-verified 50% Section 232 rate on full customs value, the tariff leg is 0.50 times the 07-October official cash of $3,102.50, or ${tl:,.2f}, leaving an ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."
    if c.startswith("PEER EARNINGS ARE IN A LULL"):
        C[i]=("PEER EARNINGS ARE IN A LULL AND NO COMPANY WAS BACK-FILLED THIS RUN (08-October). The Q3-2026 reporting season opens in mid-October; existing earnings_history entries are unchanged and carry only exact publicly verified figures.")
    if c.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent ($101.97), the dollar index (102.16) and the US ten-year (5.31%) are Trading Economics reference marks from Thursday 08-October Asian-morning trade; EUR/USD is the 07-October LME fixing; European gas TTF is carried at its Friday 02-October close (74.76 EUR/MWh) because no newer public reference value was captured this run. Hormuz and Bab el-Mandeb transit counts remain disputed, so none is published.")
    if c.startswith("THE ELLIOTT WAVE PANELS"):
        C[i]=c.split(' UPDATE 0')[0]+" UPDATE 08-OCTOBER: the daily count (C-wave from 3,374) is unchanged in degree; the 06-October bounce to 3,148.5 is now confirmed as wave (iv) by the lower 07-October settlement (3,114), and wave (v) is under way; the weekly alternate remains preferred."

ew=d['ew']; ew['updated']=RD
st=ew['short_term']
assert st['line'][-1]==[0.9994,3118.0], st['line'][-1]
st['line']+= [[0.9997,3148.5],[0.99985,3114.0]]
st['now_x']=0.9999
st['waves']+=[{'t':0.9994,'p':3118.0,'w':'(iii) of C'},{'t':0.9997,'p':3148.5,'w':'(iv) of C - confirmed 07-Oct'}]
st['proj']={"bull":[[0.9999,3114.0],[0.99995,3190],[1.0,3290]],
            "base":[[0.9999,3114.0],[0.99995,3080],[1.0,3040]],
            "bear":[[0.9999,3114.0],[0.99995,3050],[1.0,2980]]}
for f in st['fib']:
    if f['p']==3289.0: f['l']="3,289 - the 12-September (ii) high and the INVALIDATION of the bearish daily count. A daily official settlement above it negates the C-wave count. It is $175.00 above the 07-October three-month."
    if f['p']==3261.0: f['l']="3,261 - the shared 38.2% weekly retracement, held at the SAME price as the weekly panel. The 02-October weekly close settled $139.00 beneath it (weekly test FAILED); three-month is $147.00 beneath it on 07-October."
    if f['p']==3183.0: f['l']="3,183 - the 20-August low and the wave (i) low, BROKEN on 01-October. Wave (iv) peaked beneath it at 3,148.5; a settlement above 3,183 would void the impulsive labelling. $69.00 above three-month on 07-October."
    if f['p']==3061.5: f['l']="3,061.5 - the 02-July C low and the first wave (v) objective, shared with the weekly panel (50% weekly retracement at 3,077). $52.50 beneath three-month."
st['fwd_pivots'][0]['t']=0.99993
st['fwd_pivots'][1]['t']=0.99997
st['fwd_pivots'][0]['w']="FIRST TEST BELOW: the 3,061.5 July low (and 3,077, the weekly 50% retracement), $52.50 beneath the 07-October three-month. Wave (v) of C is under way from the 3,148.5 wave (iv) high; a daily official settlement beneath 3,061.5 extends it towards the 2,980 area. Rule check: wave (iii) (3,289 to 3,118, $171) cannot be the shortest, so wave (v) should not exceed $171 from 3,148.5 - a cap near 2,977."
st['fwd_pivots'][1]['w']="THE INVALIDATION: 3,289, the 12-September (ii) high. A DAILY OFFICIAL SETTLEMENT ABOVE IT negates the bearish C-wave count. NEARER TELLS: a settlement above 3,148.5 would mean wave (iv) is still extending; above 3,183 (wave (i) low) would void the impulsive labelling and promote the corrective alternate."
st['writeup']=("DAILY (SWING DEGREE) - THE C-WAVE COUNT IS UNCHANGED AND WAVE (iv) IS NOW CONFIRMED AT 3,148.5. Three-month settled $3,114.00 on Wednesday 07-October, down $34.50, beneath the 3,118 wave (iii) low, so the 06-October bounce is confirmed as a shallow wave (iv) and wave (v) is under way. "
 "BASE CASE, ABOUT 62%: the 3,061.5-3,374 rally was a corrective B wave and the C wave from 3,374 is in its fifth leg - (i) 3,183, (ii) 3,289, (iii) 3,118, (iv) 3,148.5. The cardinal rules hold: (ii) did not exceed 3,374, (iv) at 3,148.5 did not overlap the (i) low at 3,183, and (iii) at $171 is shorter than (i) at $191, so (v) must stay shorter than $171 - capping it near 2,977. Targets: the 3,061.5 July low, then 2,980-3,000. A narrower contango on the drop is a mild warning that (v) may be short. "
 "ALTERNATE, ABOUT 38%: a deep expanded flat or double-three that holds above 3,061.5 and turns higher; a daily settlement above 3,183 would promote it. "
 "INVALIDATION: a daily official settlement above 3,289, $175.00 above the 07-October three-month. CONFIDENCE IS MODERATE. This is technical context, not advice.")
lt=ew['long_term']
lt['fwd_pivots'][0]['w']=("THE 3,261 LEVEL - THE 38.2% RETRACEMENT OF THE 3,855-TO-3,061.5 DECLINE - WAS THE WEEKLY TEST AND IT FAILED: the 02-October weekly close settled three-month at $3,122.00, $139.00 beneath it; on 07-October three-month is $3,114.00, $147.00 beneath. Per the pre-registered rule the weekly alternate (the move off 3,061.5 was corrective) is preferred. 3,261 is now overhead resistance.")
lt['fwd_pivots'][1]['w']=("THE DOWNSIDE REFERENCES ARE SHARED WITH THE DAILY PANEL: the 50% retracement at 3,077 (held on the 3,061.5 low of 02-July), now only $37.00 beneath the 07-October three-month of $3,114.00, and the 61.8% at 2,894, where the bear path terminates. A WEEKLY close beneath 3,077 invalidates the constructive count outright. Overhead, the 23.6% retracement at 3,488 is $374.00 above.")
lt['writeup']=("WEEKLY (POSITION DEGREE) - THE ALTERNATE PROMOTED AFTER THE FAILED WEEKLY TEST REMAINS PREFERRED AND IS GAINING. The 3,855 high of 02-June terminates the position-degree advance; the decline into 3,061.5 on 02-July is a completed A-B-C and the 50% retracement at 3,077 held. The 02-October weekly close at $3,122.00 sat $139.00 beneath the 3,261 retracement; Wednesday 07-October's settlement at $3,114.00 puts the week on course for a lower weekly close, just $37.00 above 3,077. "
 "PREFERRED COUNT, ABOUT 57%: the move off 3,061.5 was corrective - a B wave or the opening leg of a larger fourth wave - and the decline under way breaks the 2,950-3,110 zone towards the 61.8% retracement at 2,894. "
 "ALTERNATE, ABOUT 43%: a new position-degree advance is still building off 3,061.5 as long as that low holds on a weekly close; targets 3,488, then 3,680 and 3,840 into mid-2027. "
 "INVALIDATION: a weekly close beneath 3,077 invalidates the constructive alternate outright - the Friday 09-October close is now the test; a weekly close back above 3,261 would restore it as preferred. CONFIDENCE IS LOW-TO-MODERATE. This is technical context, not advice.")
lt['proj']={"bull":[[0.66,3114.0],[0.76,3380],[0.88,3600],[1.0,3800]],"base":[[0.66,3114.0],[0.78,3090],[0.9,3200],[1.0,3270]],"bear":[[0.66,3114.0],[0.8,2960],[1.0,2890]]}
d['bottom_line']=d['bottom_line'].replace("about 55%","about 57%")

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-06', ph['rows'][-1]
ph['rows'][-1]=['2026-10-07',cash,m3,stk]
ph['updated']=RD
ph['basis']=("London Metal Exchange official settlements via Westmetall. LME Aluminium official cash settlement, official 3-month, and LME warehouse stock. Weekly sampling (last published official session of each week). AT THE 08-OCTOBER-2026 UPDATE the row for the week of 05-October is PROVISIONAL: the Wednesday 07-October session (cash 3,102.50, 3-month 3,114.00, stock 238,875 t), replacing Tuesday's, to be replaced again as later sessions print; the week of 28-September is FINAL at the Friday 02-October session. Verified against both cache-busted Westmetall language overviews and the per-metal aluminium daily table.")
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok', d['metals_board'], mh['al'][-1], mh['zn'][-1], mh['pb'][-1], round(tl,2), round(share,1), round(ratio,2))
