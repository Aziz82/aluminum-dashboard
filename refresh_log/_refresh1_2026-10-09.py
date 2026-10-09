# Daily data refresh - 2026-10-09 (FRIDAY, compiled ~03:35 London BEFORE the ring). Board ROLLED to THURSDAY 08-Oct LME official.
# EN+DE cache-busted overviews agree exactly on 08-Oct; Al per-metal table shows 08-Oct newest (no later row), 07-Oct prior unchanged; 5/5 stock lines reconcile.
import json, re
P='market_data.json'
d=json.load(open(P,encoding='utf-8'))
RD='2026-10-09'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TEA="https://tradingeconomics.com/commodity/aluminum"
S_TED="https://tradingeconomics.com/united-states/currency"
S_TEB="https://tradingeconomics.com/commodity/brent-crude-oil"
S_CRU="https://www.alcircle.com/news/asian-aluminium-premium-slips-to-202-t-as-mjp-q4-offers-fall-to-245-260-121444"
S_SMM="https://news.metal.com/newscontent/104146955-rate-hike-expectations-disrupt-coupled-with-post-holiday-inventory-buildup-aluminum-prices-consolidate-on-a-subdued-note-in-the-short-term-smm-aluminum-morning-meeting-summary"
S_ALC="https://alcircle.com/news/lme-aluminium-price-pulls-back-rapidly-before-the-holiday-then-recovers-from-lows-why-did-it-fall-below-usd-3-150-per-tonne-121479"
S_NHY="https://www.engineeringnews.co.za/article/norways-norsk-hydro-sees-up-to-210m-hit-from-gas-supply-disruption-at-alunorte-2026-10-06"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']

cash,prev_c,m3,prev_m,stk,prev_s=3060.5,3102.5,3069.0,3114.0,238875,238875
spr=cash-m3
pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100

VER=("COMPILED FRIDAY 09-OCTOBER-2026 BEFORE THE LONDON RING (~03:35 LONDON). THE BOARD ROLLED THIS RUN TO THE THURSDAY 08-OCTOBER-2026 LONDON METAL EXCHANGE OFFICIAL, THE LATEST PUBLISHED SESSION; TODAY'S OFFICIAL DOES NOT PRINT UNTIL 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted English and German Westmetall overviews AGREE EXACTLY on 08-October across all six metals, all six stock lines and the foreign-exchange fixings; (2) the aluminium per-metal daily table shows 08-October as the newest row - NO ROW AFTER IT - with 07-October reproduced unchanged as the prior row; "
 "(3) ALL FIVE STOCK LINES RECONCILE against the levels carried for 07-October: aluminium 238,875 unchanged; copper 239,875 less 4,650 to 235,225; nickel 284,178 unchanged; zinc 127,750 less 325 to 127,425; lead 349,400 less 1,525 to 347,875. "
 "The whole board sits on ONE UNIFORM SESSION (08-October) and no intraday, closing, reference or contract-for-difference mark is used anywhere in it. Prior-month averages remain the completed SEPTEMBER-2026 official means. NEXT OFFICIAL: FRIDAY 09-OCTOBER, 13:20 LONDON.")

AL=(f" CASH SETTLED $3,060.50 ON THE 08-OCTOBER OFFICIAL, DOWN $42.00 OR {pc:.2f}% FROM $3,102.50. THREE-MONTH SETTLED $3,069.00, DOWN $45.00 OR {pm:.2f}% FROM $3,114.00 - A THIRD NEW LOW FOR THE MOVE, NOW ONLY $7.50 ABOVE THE 3,061.5 JULY LOW AND $8.00 BENEATH THE 3,077 WEEKLY 50% RETRACEMENT. "
 "SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS FOR A SECOND SESSION: three-month fell $3.00 more than cash, so the CONTANGO NARROWED TO $8.50 from $11.50 even as the price fell - the structure again did not confirm the drop. "
 "VISIBLE LME STOCK WAS UNCHANGED AT 238,875 TONNES. AFTER THE OFFICIAL, SMM (09-October) reports the LME three-month closing the electronic day at $3,042.0, low $3,041.5, down $83.0 or 2.66% - i.e. BENEATH the July low; that is a closing mark, not an official, and is NOT used on this board. "
 "The LME euro fixing eased to 1.1177 from 1.1183; Trading Economics (09-October) has the dollar index slipping to about 102.0 after a well-received 30-year auction pulled yields lower, with the ten-year near 5.23%.")

d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,060.5","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,069.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $192.00 BELOW 3,261, $114.00 BELOW THE BROKEN 3,183 DAILY LEVEL, $220.00 BELOW THE 3,289 DAILY INVALIDATION, $8.00 BENEATH the 3,077 weekly 50% retracement and $7.50 above the 3,061.5 July low."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-8.5","pos":False,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,060.50 against three-month $3,069.00 is an $8.50 CONTANGO, NARROWED $3.00 from $11.50. Spread and flat price moved in OPPOSITE directions for a second ring (price down, contango narrower). The published reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"238,875","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK WAS UNCHANGED AT 238,875 TONNES for a third session, holding the series low on this page. September's mean stock was {sep_s:,} tonnes. Flat stock alongside a narrowing contango says the visible stock is not the driver of the price drop."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,069.00, DOWN $45.00 OR {pm:.2f}% FROM $3,114.00, a new low for the move, $7.50 above the 3,061.5 July low. AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK UNCHANGED AT 238,875 TONNES. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-11.5,"avg":sep_sp,"note":VER+f" AN $8.50 CONTANGO, NARROWED $3.00 FROM $11.50. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in OPPOSITE directions for a second ring (price lower, contango narrower). PUBLISHED REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1177,"prev":1.1183,"avg":1.1465,"note":VER+" THE LME EURO FIXING EASED TO 1.11770 FROM 1.11830 at the Thursday ring; the ECB fixing printed 1.11860 and BFIX 1.11785 - a broadly flat dollar at that session. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]

d['outlook']['forward_path']=[
 {"tenor":"Cash (08-Oct official)","price":"3,060.5","basis":f"THE 08-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,060.50, DOWN $42.00 OR {pc:.2f}%. Next official Friday 09-October 13:20 London."},
 {"tenor":"3-month (08-Oct official)","price":"3,069.0","basis":f"THE 08-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,069.00, DOWN $45.00 OR {pm:.2f}%, a new low for the move: $7.50 above the 3,061.5 July low, $8.00 beneath the 3,077 weekly 50% retracement, $114.00 beneath the broken 3,183."},
 {"tenor":"Cash-to-3M structure","price":"-8.5 (CONTANGO)","basis":"An $8.50 CONTANGO, narrowed $3.00 from $11.50. Flat price and spread moved in OPPOSITE directions for a second ring."},
 {"tenor":"Visible LME stock","price":"238,875 t","basis":f"UNCHANGED on the session; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE CURVE FIRMED AGAIN EVEN AS THE PRICE FELL. On the 08-October official cash $3,060.50 sits $8.50 BELOW three-month $3,069.00, a CONTANGO narrowed $3.00 from $11.50. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50 and now $8.50. "
 f"READ: a narrow, narrowing contango with visible stock flat at 238,875 t - the slide is a flat-price (macro, premium and supply-recovery) repricing, not a prompt glut. The September mean spread was ${sep_sp:,.2f}. The published reversal condition (a backwardation beyond $15.00) is closer but unmet; a contango beyond $24.50 would be the bearish structural confirmation.")

ls=d['lme_series']; assert ls[-1][0]=='07-Oct', ls[-1]
d['lme_series']=ls[1:]+[["08-Oct",cash,m3,stk]]
d['chart_price_axis']=[2950,3450]
d['chart_stock_axis']=[225000,255000]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2950<r[1]<3450 and 2950<r[2]<3450 for r in d['lme_series'])
# (cash, 3M, prev cash, prev 3M)
CU=(14526.0,14417.0,14510.0,14422.0); NI=(15415.0,15600.0,15645.0,15840.0); ZN=(3781.0,3737.0,3799.0,3756.0); PB=(1833.0,1874.0,1844.5,1884.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
zn_old=(3834.0+3798.0+3774.0+3803.0+3799.0)/5; pb_old=(1837.0+1827.0+1829.5+1837.5+1844.5)/5
zn_avg=(3834.0+3798.0+3774.0+3803.0+3799.0+3781.0)/6; pb_avg=(1837.0+1827.0+1829.5+1837.5+1844.5+1833.0)/6
mh['zn'][-1]=round(mh['zn'][-1]*zn_avg/zn_old,1); mh['pb'][-1]=round(mh['pb'][-1]*pb_avg/pb_old,1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])): R[k]=R[k][1:]+[v]
ms['asof']='2026-10-08'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending THURSDAY 08-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 17-September dropped and 08-October appended, so the window is 18-September to 08-October. Every point is an official cash settlement, verified against the cache-busted Westmetall English and German overviews, which agree to the cent, the aluminium per-metal daily table (no row after 08-October), and five-for-five stock-line reconciliation. Next official Friday 09-October.")
ms['src']=["Westmetall - LME official cash settlements, EN and DE overviews cache-busted and in exact agreement (08-October-2026 session)",W]

AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,526.00, up $16.00 or 0.11%; three-month $14,417.00, down $5.00 or 0.03%. The BACKWARDATION WIDENED to $109.00 from $88.00 while stock DREW 4,650 tonnes to 235,225 - prompt tightness firming for a third session; copper cash was the only gain on the board."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,415.00, down $230.00 or 1.47%; three-month $15,600.00, down $240.00 or 1.52% - the weakest three-month move on the board, reversing Wednesday's gain. CONTANGO $185.00 from $195.00, still the widest carry on the board. Stock unchanged at 284,178."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,781.00, down $18.00 or 0.47%; three-month $3,737.00, down $19.00 or 0.51%. The BACKWARDATION was steady at $44.00 (from $43.00) while stock drew 325 tonnes to 127,425. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,833.00, down $11.50 or 0.62%; three-month $1,874.00, down $10.00 or 0.53%. CONTANGO widened to $41.00 from $39.50. Stock drew 1,525 tonnes to 347,875, a fourteenth consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL, REPORTED AS DATA NOT AS A REGIME SIGNAL: on the Thursday 08-October official the board fell almost across the line in three-month terms - nickel -1.52%, aluminium -1.45%, lead -0.53%, zinc -0.51%, copper -0.03% - while the LME euro fixing was near flat at 1.1177. A broader base-metal pullback on China's first day back from holiday, with aluminium and nickel leading lower.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

OLDH="COMPILED THURSDAY 08-OCTOBER-2026, BEFORE THE LME RING (REVIEWED; NO NEW MARK FOR THIS ROW SINCE THE PRIOR RUN - CHINA IS ON ITS 01-08 OCTOBER HOLIDAY, REOPENING 09-OCTOBER)."
NEWH="COMPILED FRIDAY 09-OCTOBER-2026, BEFORE THE LME RING (REVIEWED; NO NEW MARK FOR THIS ROW LOCATED SINCE THE PRIOR RUN - CHINESE MARKETS REOPENED 08-OCTOBER AFTER THE NATIONAL DAY HOLIDAY AND NO POST-HOLIDAY WEEKLY ASSESSMENT FOR THIS ROW HAD BEEN LOCATED)."
n_rep=0
for i in d['inputs']:
    if isinstance(i.get('src'),str) and OLDH in i['src']: i['src']=i['src'].replace(OLDH,NEWH); n_rep+=1
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='07-Oct'
        i['hist']=i['hist'][1:]+[["08-Oct",CU[0]]]
        assert len(i['hist'])==15
        i['val']="~14,417.00 (3M); 14,526.00 (cash) $/t"
        i['ratio']="~14,526.00 $/t cash vs LME 3M 14,417.00 $/t"
        i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the THURSDAY 08-OCTOBER-2026 session at $14,526.00, UP $16.00 or 0.11% against $14,510.00. THE WINDOW ROLLED THIS RUN: 17-September dropped and 08-October appended, so the series is the last fifteen published official cash sessions, 18-September to 08-October - the same window as the LME Board sparklines. Official settlement only, verified on the cache-busted Westmetall English and German overviews, which agree to the cent. "
                  "Copper structure for context: backwardation $109.00 (from $88.00), stock drew 4,650 t to 235,225 t.")
print('inputs header replaced', n_rep)
d['inputs_summary']=("UPDATE 09-OCTOBER (FRIDAY, PRE-RING): copper rolled to the Thursday 08-October LME official cash of $14,526.00, up $16.00, with its fifteen-session window moved to 18-September to 08-October. Chinese markets reopened on 08-October, but no post-holiday SMM fluoride, silicon or magnesium weekly mark had been located when this page compiled, and the carbon settlement cycle (anodes, pitch, green coke) is mid-October - so every other row is carried at its own dated public mark and no value was interpolated.")
nr=0
for r in d['raw_materials']:
    if isinstance(r.get('src'),str) and OLDH in r['src']: r['src']=r['src'].replace(OLDH,NEWH); nr+=1
print('raw header replaced', nr)

ratio=360.4/m3*100
ALNOTE=("COMPILED FRIDAY 09-OCTOBER-2026 (PRE-RING). NO NEW DATED PUBLIC ALUMINA PRICE MARK WAS LOCATED FOR THIS WINDOW: the LME Alumina (Platts) row stays at AL Circle's $360.40/t print of 30-September; the FOB East Australia trade row stays at its 18-September mark; SMM separately reported 30,000 t traded at $369/t FOB Western Australia on 30-September for November shipment (a different basis, reported in news only). The SMM alumina index is carried at its 30-September print of 2,669.99 yuan/tonne pending a confirmed post-holiday print. SUPPLY CONTEXT: Norsk Hydro (05-October, via Reuters/Engineering News) guided a further $90-110m fourth-quarter cost at its Alunorte refinery from gas bought above contract, after losing 100,000-120,000 t of alumina in the August disruption. "
 f"THE RATIO: LME Alumina at $360.40/t against the 08-October aluminium three-month of $3,069.00 is {ratio:.2f}%, against a decade norm of 15-17%. Alumina remains historically CHEAP relative to metal.")
for a in d['alumina']: a['src']=ALNOTE

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
PREM=("COMPILED FRIDAY 09-OCTOBER-2026 (PRE-RING). PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND THIS PANEL CARRIES EACH ROW AT ITS OWN LAST PUBLIC ASSESSMENT DATE. NO NEW ASSESSMENT ON ANY ROW'S OWN BASIS WAS LOCATED FOR THIS WINDOW, so every row is CARRIED UNCHANGED. CONTEXT FROM A DIFFERENT ASSESSOR, NOT MIXED INTO ANY ROW: AL Circle (06-October) reports CRU's Asia CIF premium at $202/t and Q4 MJP offers down to $245-260/t from $325/t in early September, against the $395/t Q3 benchmark; earlier SMM reporting (30-September) had Rio Tinto at $280/t and South32 at $265/t. No Q4 settlement had been publicly reported when this page compiled. These are offers, not a settlement. "
 f"THE TARIFF DECOMPOSITION IS REFRESHED DAILY BY DESIGN: on a re-verified Section 232 rate of 50% on aluminium articles applied to full customs value, the tariff leg of the US duty-paid premium is 0.50 times the 08-October official cash of $3,060.50, or ${tl:,.2f}, DOWN $21.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}% of the US duty-paid premium is policy arithmetic rather than market. "
 "This page does NOT fabricate freight, financing or tightness splits for any premium row.")
for p in d['premiums']:
    s=p['src']; j=s.find("for any premium row.")
    if s.startswith("COMPILED") and j>0: p['src']=PREM+s[j+len("for any premium row."):]
    else: p['src']=PREM+" "+s
pq=d['premium_quarters']; assert pq[-1]['q']=='Q4-26' and pq[-1]['v'] is None
pq[-1]['range']=[245,280]

d['lme_commentary']=(f"ALUMINIUM EXTENDED ITS SLIDE TO A THIRD NEW LOW FOR THE MOVE. On the Thursday 08-October official cash settled $3,060.50, down $42.00 or {pc:.2f}%, and three-month $3,069.00, down $45.00 or {pm:.2f}% - $7.50 above the 3,061.5 July low and $8.00 beneath the 3,077 weekly 50% retracement. After the official the electronic market kept falling: SMM reports LME three-month closing at $3,042.0 (low $3,041.5), down 2.66% on the day, beneath the July low - a closing mark, not an official. "
 "The contango NARROWED $3.00 to $8.50 while the price fell (spread and price in OPPOSITE directions for a second ring) and visible stock was unchanged at 238,875 t, so the drop is still not structural. "
 "China reopened from its holiday on 08-October with SHFE weaker (SMM: most-traded contract night session 23,220 yuan/t, down 0.71%; A00 spot 23,760, down 270) and a post-holiday build in billet stocks (+38,000 t to 187,500 t since 30-September). SMM and AL Circle (08-October) frame the move as the market shifting from 'supply disruption' to 'supply recovery' trading, alongside a strong dollar and high long-term yields. "
 f"The whole board fell bar copper cash; nickel (-1.52%) and aluminium (-1.45%) led. September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND IN CONTROL; THE JULY LOW IS THE LINE. Against: three-month made a third successive new low at 3,069 and the post-official close was already beneath 3,061.5; China came back from holiday with weaker SHFE prices and a billet-stock build; the narrative has turned to supply recovery (Gulf restarts, Indonesian and Chinese exports); the Fed is still guided towards another hike and US yields remain above 5.2%; Asian premium offers sit at $245-260/t versus $395/t in Q3. "
 "Constructive: the contango narrowed for a second ring on the drop; visible LME stock is holding at a series low (238,875 t); the dollar and yields eased on 09-October; Brent still near $103 keeps the energy cost floor high; alumina supply costs are rising at the margin (Hydro's Alunorte gas bill).")
d['commercial']=("COMMERCIAL READ - GENERIC AND PUBLIC. FIRST, THE CURVE PAYS BUYERS ONLY A LITTLE TO WAIT: an $8.50 contango on 08-October, narrowing. SECOND, ASIAN PREMIUMS ARE RESETTING LOWER: public reporting has Q4 MJP offers at $245-260/t (AL Circle, 06-October) and CRU's Asia CIF at $202/t, against $395/t in Q3; no settlement is yet reported. THIRD, THE TARIFF ARITHMETIC MOVED WITH THE METAL: "
 f"on a verified 50% Section 232 rate, the tariff leg of the US Midwest duty-paid premium is ${tl:,.2f} on 08-October cash, {share:.1f}% of the $2,403/t premium. FOURTH, WATCH THE CALENDAR: today's official decides whether the 3,061.5 July low breaks on a settled basis and sets the weekly close against 3,077; a Q4 Japanese premium settlement could come any day; China's post-holiday stock prints next week. This is generic public market context, not advice.")

for s in d['outlook']['scenarios']:
    dr=s['drivers']
    dr=re.sub(r"^MOVED 08-OCTOBER \(from 14/47/39 to 13/45/42\):.*?bigger shift\. ","PREVIOUSLY MOVED 08-OCTOBER (to 13/45/42 after the 07-October new low). ",dr,flags=re.S)
    s['prob']={'Bull':'12%','Base':'45%','Bear':'43%'}[s['case']]
    s['drivers']=("MOVED 09-OCTOBER (from 13/45/42 to 12/45/43): the 08-October official set a third new low (three-month 3,069, -1.45%), the post-official close slipped beneath the 3,061.5 July low, and China reopened weaker with a billet-stock build; one point moves from bull to bear. The second successive narrowing of the contango (to $8.50) and flat stock argue against a bigger shift until a settled break of 3,061.5. ")+dr
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['bottom_line']=(f"BOTTOM LINE: aluminium settled on the 08-October LME official at cash $3,060.50 and three-month $3,069.00, down {abs(pm):.2f}% - a third new low for the move, $7.50 above the 3,061.5 July low, with the post-official close already beneath it. "
 "The contango narrowed to $8.50 and visible stock held at 238,875 t, so the structure still did not confirm the drop. Scenario weights move to 12% bull / 45% base / 43% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) targets 3,061.5 then 2,980-3,000 with a rule-based floor near 2,977, invalidation 3,289; the weekly alternate is preferred at about 60% and today's weekly close against 3,077 is the test.")

d['so_what']={"line":"Aluminium fell to a third straight low for the move and is testing its early-July floor near $3,060 as China returned from holiday weaker and the market trades supply recovery - today's weekly close decides whether that support holds.",
 "points":[
 f"WHAT MOVED: Thursday's LME official settled cash at $3,060.50 (-$42.00) and three-month at $3,069.00 (-$45.00, {pm:.2f}%), just $7.50 above the July low; after the official, three-month closed near $3,042 (SMM), beneath it. Nearly all base metals fell; the contango narrowed to $8.50 and LME stock was unchanged at 238,875 t.",
 "WHY: China reopened after its holiday with Shanghai prices lower and billet stocks up 38,000 t since 30-September (SMM); analysts describe a shift from pricing supply disruption to pricing supply recovery, on top of a strong dollar and US ten-year yields above 5.2% (Trading Economics).",
 "PREMIUMS AND COSTS: Q4 Japanese premium offers are $245-260/t versus $395/t in Q3 (AL Circle), with no settlement yet; on the cost side, Norsk Hydro guided a further $90-110m Q4 gas cost at its Alunorte alumina refinery.",
 "WHAT TO WATCH: today's LME official and weekly close against $3,061.5 and $3,077 - a settled break opens the $2,980-3,000 area; a Q4 Japanese premium settlement; China's first post-holiday inventory prints next week."]}

new_feed=[
 {"when":"Fri 09-Oct","impact":"Bearish","text":f"BOARD ROLLED TO THE THURSDAY 08-OCTOBER LME OFFICIAL. Cash $3,060.50 (-$42.00), three-month $3,069.00 (-$45.00, {pm:.2f}%) - a third new low, $7.50 above the 3,061.5 July low - contango NARROWED to $8.50 from $11.50 (opposite to price), stock unchanged at 238,875 t. Verified on cache-busted English and German overviews in exact agreement, the aluminium per-metal table with no later row, and five-for-five stock reconciliation."},
 {"when":"Fri 09-Oct","impact":"Bearish","text":"POST-OFFICIAL SLIDE (SMM, 09-October): LME three-month closed the 08-October electronic day at $3,042.0, low $3,041.5, down 2.66% - beneath the July low on a closing basis (not an official)."},
 {"when":"Fri 09-Oct","impact":"Bearish","text":"CHINA BACK FROM HOLIDAY WEAKER (SMM): SHFE most-traded aluminium night session 23,220 yuan/t (-0.71%); A00 spot 23,760 (-270); 6063 billet stocks 187,500 t, +38,000 t since 30-September; bonded-zone stocks 114,600 t, -3,500 t."},
 {"when":"Fri 09-Oct","impact":"Mixed","text":"DOLLAR AND YIELDS EASE (Trading Economics, 09-October): dollar index about 102.0 after a well-received 30-year auction; US ten-year near 5.23%; markets still price about 81% odds of a December Fed hike, and Governor Waller said further increases will likely be needed."},
 {"when":"Mon 05-Oct","impact":"Mixed","text":"HYDRO GUIDES FURTHER ALUNORTE GAS COST (Reuters via Engineering News, 06-October): $90-110m in Q4 from gas bought above contract, up to about $210m including Q3; 100,000-120,000 t of alumina lost in the August disruption; legal remedies being sought."},
]
d['feed']=(new_feed+d['feed'])[:12]

new_news=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":f"LME ALUMINIUM SETS A THIRD NEW LOW AND TESTS THE JULY FLOOR. The Thursday 08-October official settled cash at $3,060.50 ({pc:.2f}%) and three-month at $3,069.00 ({pm:.2f}%), $7.50 above the 3,061.5 July low; SMM reports three-month closing the electronic day at $3,042.0 (-2.66%), beneath it. The contango narrowed to $8.50 from $11.50 and visible stock was unchanged at 238,875 t."},
 {"theme":"China","horizon":"Days-weeks","impact":"Bearish","url":S_SMM,
  "headline":"CHINA REOPENS WEAKER WITH A POST-HOLIDAY STOCK BUILD (SMM, 09-October): the most-traded SHFE aluminium contract closed the 08-October night session at 23,220 yuan/t, down 165 (-0.71%); SMM A00 spot fell 270 to 23,760; 6063 billet stocks in major consumption areas rose 38,000 t to 187,500 t since 30-September while bonded-zone ingot stocks fell 3,500 t to 114,600 t. SMM expects prices to consolidate on a weak note, citing high US yields, a strong dollar and softer liquid-aluminium demand."},
 {"theme":"Market","horizon":"Weeks","impact":"Bearish","url":S_ALC,
  "headline":"FROM 'SUPPLY DISRUPTION' TO 'SUPPLY RECOVERY' TRADING (SMM via AL Circle, 08-October): the LME pullback of more than 7% from about 3,350 reflects macro pressure (strong dollar, high long-dated yields, fund profit-taking), an unwinding Middle East risk premium as production and logistics recover, and China peak-season demand that fell short; low visible ex-China inventory could support prices again only if demand improves while supply recovery lags."},
 {"theme":"Supply","horizon":"Months","impact":"Mixed","url":S_NHY,
  "headline":"HYDRO SEES UP TO $210M HIT FROM ALUNORTE GAS DISRUPTION (Reuters via Engineering News, 06-October): Norsk Hydro guided a further $90-110m fourth-quarter cost from buying gas above contract at the Brazilian alumina refinery, on top of a $75-100m third-quarter impact; the refinery is back at full rate under a temporary access deal but still not receiving contracted volumes. A cost-side support for alumina rather than a volume loss."},
 {"theme":"Macro","horizon":"Days-weeks","impact":"Mixed","url":S_TED,
  "headline":"DOLLAR AND YIELDS EASE BUT THE FED IS STILL HAWKISH (Trading Economics, 09-October): the dollar index slipped to about 102.0 and the US ten-year to about 5.23% after a well-received 30-year auction; markets price about 81% odds of a December hike and Governor Waller said further increases will likely be needed. Oil eased after President Trump cited 'productive discussions' with Iran (Brent about $103.4)."},
]
d['news']=new_news+d['news'][:15]

cats=d['outlook']['catalysts']
for c in cats:
    if c['date']=='Daily, from Thu 08-Oct':
        c['date']='Daily, from Fri 09-Oct'
        c['event']="3,061.5 AND 3,077 UNDER TEST, 3,183 OVERHEAD, 3,289 INVALIDATION. Three-month settled $3,069.00 on 08-October, $7.50 above the 02-July low at 3,061.5 and $8.00 beneath the 3,077 weekly 50% retracement; the post-official close (SMM) was $3,042.0. A settled official beneath 3,061.5 opens the 2,980 area (wave (v) of C, rule cap near 2,977); TODAY'S FRIDAY 09-OCTOBER OFFICIAL IS ALSO THE WEEKLY CLOSE - a weekly close beneath 3,077 invalidates the constructive weekly alternate outright; a daily settlement above 3,183 would void the impulsive C-wave labelling."
    if c['date']=='Any day (pending)':
        c['event']="Q4-2026 JAPANESE QUARTERLY PREMIUM (MJP) SETTLEMENT. Latest public offers $245-260/t (AL Circle, 06-October), after $265-280/t from South32 and Rio Tinto (SMM, 30-September); CRU's Asia CIF premium is $202/t; versus $395/t in Q3. Not yet reported as settled at 09-October."
    if c['date']=='Thu 01-Oct to Thu 08-Oct':
        c['date']='Resolved Thu 08-Oct'
        c['event']=c['event'].split(' UPDATE 08-OCTOBER')[0]+" RESOLVED 08-OCTOBER, BEARISH-LEANING: Chinese markets reopened on Thursday 08-October; the most-traded SHFE contract closed the night session at 23,220 yuan/t (-0.71%), A00 spot fell 270 to 23,760, and 6063 billet stocks rose 38,000 t to 187,500 t since 30-September (SMM, 09-October). The first post-holiday ingot social-inventory print is the next read."
d['outlook']['catalysts']=cats

RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 09-OCTOBER: the contango NARROWED again, $3.00 to $8.50, on 08-October as the price fell. Well inside the $24.50 bearish-confirmation threshold. Trend held at FLAT."
RK[1]['risk']+=" UPDATE 09-OCTOBER: markets price about 81% odds of a December hike and Governor Waller said further increases will likely be needed, though the ten-year eased to about 5.23% after a strong 30-year auction (Trading Economics). Trend held at UP."
RK[4]['risk']+=" UPDATE 09-OCTOBER: LME stock unchanged at 238,875 t on 08-October for a third session, holding the series low. Trend held at FLAT."
RK[6]['risk']+=" UPDATE 09-OCTOBER: China reopened with 6063 billet stocks up 38,000 t to 187,500 t since 30-September and SHFE lower (SMM, 09-October). Trend held at UP."
RK[7]['risk']+=" UPDATE 09-OCTOBER: Brent eased to about $103.4 after President Trump cited 'productive discussions' with Iran (Trading Economics); Hydro guided a further $90-110m Q4 gas cost at Alunorte. Trend held at FLAT."
RK[8]['risk']+=" UPDATE 09-OCTOBER: no Q4 settlement reported; latest offers $245-260/t. Trend held at DOWN."
RK[10]['risk']+=" UPDATE 09-OCTOBER: SMM and AL Circle (08-October) describe the market as shifting to 'supply recovery' trading - idled restarts, Middle East recovery and new Indonesian, Middle East and Central Asian capacity. Trend held at UP."

d['outlook']['ai_analysis'][0]=(f"FRIDAY PRE-RING REVIEW, 09-OCTOBER: Thursday's official set a third successive low (three-month $3,069.00, {pm:.2f}%), $7.50 above the 3,061.5 July low, and the electronic close (SMM: $3,042) was already beneath it. China's return from holiday added to the pressure - SHFE lower and billet stocks up 38,000 t - as the market reprices from supply disruption to supply recovery. The structure still does not confirm (contango narrowed to $8.50, stock flat), so the bear case is raised only to 43%; today's official is also the weekly close against 3,077, the decisive test for the weekly count.")

for l in d['logistics']:
    if l['name']=='Strait of Hormuz transit':
        rest=l['note'].split(' PRIOR: ',1)[-1]
        l['note']=("REVIEWED FRIDAY 09-OCTOBER-2026. Trading Economics' Brent coverage (08-October) says attacks on tankers in the Strait of Hormuz keep supply concerns in play, while President Trump said the US was in 'productive discussions' with Iran and would hold off on attacks before the midterm elections. No container or bulk transit count is published because tracker figures remain disputed. Arrow stays UP pending a public, verifiable normalisation signal for dry-bulk and container traffic. PRIOR: "+rest)
        l['src']="REVIEWED FRIDAY 09-OCTOBER-2026: Trading Economics Brent ("+S_TEB+"). PRIOR: "+l['src'].split(' PRIOR: ',1)[-1]
    if l['name'].startswith('Red Sea'):
        l['note']=re.sub(r"^REVIEWED THURSDAY 08-OCTOBER-2026 \(.*?\):","REVIEWED FRIDAY 09-OCTOBER-2026 (no newer public transit count located; earlier note carried):",l['note'],count=1)

for m in d['macro']:
    if m['name'].startswith('Brent'):
        m['value']='103.42'; m['day']="-0.83% in Friday 09-October trade; -3.92% over the month (Trading Economics)"
        m['note']="REFRESHED FRIDAY 09-OCTOBER-2026 on a public reference board (Trading Economics): Brent eased below $104 after President Trump said the US was in 'productive discussions' with Iran, having risen on 08-October on strike-option reports, tanker attacks near Hormuz and storm threats to Gulf of Mexico output. Energy is a major smelter cash-cost line."
    elif m['name'].startswith('US dollar index'):
        m['value']='102.04'; m['day']="-0.08% in Friday 09-October trade; +3.02% over the month (Trading Economics)"
        m['note']="REFRESHED FRIDAY 09-OCTOBER-2026 on a public reference board (Trading Economics): the dollar slipped to about 102 as Treasury yields fell after a well-received 30-year auction; markets price about 81% odds of a December Fed hike and Governor Waller said further increases will likely be needed. A firm dollar weighs on dollar-priced metals."
    elif m['name'].startswith('US 10-year'):
        m['value']='5.23'; m['day']="about 5.231% in Friday 09-October trade, eased from about 5.31% a day earlier (Trading Economics)"
        m['note']="REFRESHED FRIDAY 09-OCTOBER-2026 on a public reference board (Trading Economics). Higher yields raise the cost of carrying metal and financing inventory."
    elif m['name']=='EUR/USD':
        m['value']='1.11770'; m['day']="LME fixing on 08-October, -0.05% from 1.11830; ECB fixing 1.11860, BFIX 1.11785"
        m['note']="REFRESHED FRIDAY 09-OCTOBER-2026 to the 08-October LME fixing via Westmetall, the same session as the LME board."

for r in d['producer_status']:
    r['asof']=RD
    u=r['update']
    if r['name'].startswith('Norsk Hydro (NHY) - Alunorte'):
        r['status']="AT FULL RATE ON A TEMPORARY TERMINAL-ACCESS AGREEMENT, BUT STILL NOT RECEIVING CONTRACTED GAS - HYDRO GUIDES A FURTHER $90-110M Q4 COST (UP TO ~$210M INCLUDING Q3) AND IS SEEKING LEGAL REMEDIES"
        r['impact']="Mixed"
        r['update']=("UPDATED 09-OCTOBER: Norsk Hydro said on 05-October (Reuters via Engineering News, 06-October) that Alunorte has not received contracted gas volumes from its supplier since the August disruption and has been buying gas at spot-based prices; it expects a $90-110m fourth-quarter impact on top of a $75-100m third-quarter impact, after losing an estimated 100,000-120,000 t of alumina. The final impact depends on gas prices, contractual developments and a long-term solution. READ: a cost and margin issue for the refinery rather than a fresh volume loss. PRIOR: "+u)
        r['src']=["Engineering News / Reuters - Norsk Hydro sees up to $210m hit from gas supply disruption at Alunorte (06-Oct-2026)",S_NHY]
        continue
    for a,b in (("REVIEWED 08-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE","REVIEWED 09-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE"),
                ("REVIEWED 08-OCTOBER: no newer public disclosure located; status below carried. ","REVIEWED 09-OCTOBER: no newer public disclosure located; status below carried. ")):
        if u.startswith(a): u=b+u[len(a):]; break
    else:
        u="REVIEWED 09-OCTOBER: no newer public disclosure located; status below carried. "+u
    if r['name'].startswith('China operators'):
        u=u.replace("REVIEWED 09-OCTOBER: no newer public disclosure located; status below carried. ","UPDATED 09-OCTOBER: Chinese markets reopened 08-October; SMM (09-October) reports 6063 billet stocks up 38,000 t to 187,500 t since 30-September and bonded-zone ingot stocks down 3,500 t to 114,600 t; no new output disclosure. ",1)
    r['update']=u

for s in [["Westmetall - LME official prices and stocks, 08-Oct-2026 session (EN+DE)",W],
          ["SMM - Aluminium morning meeting summary: post-holiday inventory build (09-Oct-2026)",S_SMM],
          ["AL Circle / SMM - LME aluminium pulls back before the holiday: why below $3,150 (08-Oct-2026)",S_ALC],
          ["Engineering News / Reuters - Norsk Hydro sees up to $210m hit from Alunorte gas disruption (06-Oct-2026)",S_NHY],
          ["Trading Economics - US dollar index and yields (09-Oct-2026)",S_TED],
          ["Trading Economics - Brent crude (08/09-Oct-2026)",S_TEB]]:
    d['sources'].append(s)
d['outlook']['sources'].append(["SMM - post-holiday aluminium inventory build and weak consolidation outlook (09-Oct-2026)",S_SMM])

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE THURSDAY 08-OCTOBER-2026 LME OFFICIAL. This page compiled on FRIDAY 09-October at about 03:35 London, before the ring; today's official prints at 13:20 London, so Thursday's official is the latest published figure. The post-official electronic close reported by SMM ($3,042.0) is cited in text only and is NOT used on the board.")
C[1]=("THE COMPLETENESS TEST PASSES: the aluminium per-metal daily table shows 08-October as the newest row with NO ROW AFTER IT and 07-October unchanged as the prior row; the other metals reconcile through the cache-busted overviews and stock arithmetic.")
C[2]=("THE ENGLISH AND GERMAN OVERVIEWS WERE BOTH REQUESTED CACHE-BUSTED ON 09-OCTOBER AND AGREE EXACTLY on 08-October across all six metals, stocks and FX fixings.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against the levels carried for 07-October: aluminium unchanged at 238,875; copper -4,650 to 235,225; nickel unchanged at 284,178; zinc -325 to 127,425; lead -1,525 to 347,875.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (08-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (six sessions, 01- to 08-October) as their latest point. The price chart axis floor was lowered to 2,950 to bracket three-month at 3,069; the stock chart axis floor (225,000 t) brackets visible stock at 238,875 t.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,060.50 against three-month $3,069.00 is therefore an $8.50 CONTANGO, narrowed $3.00 from $11.50 on 07-October - and it narrowed while the flat price fell, i.e. spread and price moved in OPPOSITE directions for a second ring."
C[6]=("PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND NO NEW ASSESSMENT ON ANY ROW'S OWN BASIS WAS LOCATED FOR THIS WINDOW; every premium row is carried at its own assessment date. CRU's Asia CIF $202/t (AL Circle, 06-October) is a different assessor's basis and is reported in drivers and news only, not substituted into the CIF Japan row. No Q4-2026 Japanese quarterly settlement had been publicly reported when this page compiled on 09-October; the chart's pending band is the span of reported OFFERS ($245-280/t). Offers are not settlements.")
for i,c in enumerate(C):
    if c.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a re-verified 50% Section 232 rate on full customs value, the tariff leg is 0.50 times the 08-October official cash of $3,060.50, or ${tl:,.2f}, leaving an ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."
    if c.startswith("PEER EARNINGS ARE IN A LULL"):
        C[i]=("PEER EARNINGS ARE IN A LULL AND NO COMPANY WAS BACK-FILLED THIS RUN (09-October). The Q3-2026 reporting season opens in mid-October; Norsk Hydro's 05-October Alunorte cost guidance is a forward estimate, not a reported result, and is NOT entered in earnings_history; existing entries carry only exact publicly verified figures.")
    if c.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent ($103.42), the dollar index (102.04) and the US ten-year (5.23%) are Trading Economics reference marks from Friday 09-October Asian-morning trade; EUR/USD is the 08-October LME fixing; European gas TTF is carried at its Friday 02-October close (74.76 EUR/MWh) because no newer public reference value was captured this run. Hormuz and Bab el-Mandeb transit counts remain disputed, so none is published.")
    if c.startswith("THE ELLIOTT WAVE PANELS"):
        C[i]=c.split(' UPDATE 0')[0]+" UPDATE 09-OCTOBER: the daily count (C-wave from 3,374, wave (v) under way from 3,148.5) is unchanged; three-month at 3,069 sits $8.00 beneath the 3,077 weekly 50% retracement, but the weekly invalidation is a WEEKLY CLOSE, and the week closes on today's (09-October) official, which had not printed when this page compiled."

ew=d['ew']; ew['updated']=RD
st=ew['short_term']
assert st['line'][-1]==[0.99985,3114.0], st['line'][-1]
st['line']+= [[0.99992,3069.0]]
st['now_x']=0.99994
st['proj']={"bull":[[0.99994,3069.0],[0.99997,3150],[1.0,3250]],
            "base":[[0.99994,3069.0],[0.99997,3030],[1.0,2995]],
            "bear":[[0.99994,3069.0],[0.99997,3010],[1.0,2977]]}
for f in st['fib']:
    if f['p']==3289.0: f['l']="3,289 - the 12-September (ii) high and the INVALIDATION of the bearish daily count. A daily official settlement above it negates the C-wave count. It is $220.00 above the 08-October three-month."
    if f['p']==3261.0: f['l']="3,261 - the shared 38.2% weekly retracement, held at the SAME price as the weekly panel. The 02-October weekly close settled $139.00 beneath it (weekly test FAILED); three-month is $192.00 beneath it on 08-October."
    if f['p']==3183.0: f['l']="3,183 - the 20-August low and the wave (i) low, BROKEN on 01-October. Wave (iv) peaked beneath it at 3,148.5; a settlement above 3,183 would void the impulsive labelling. $114.00 above three-month on 08-October."
    if f['p']==3061.5: f['l']="3,061.5 - the 02-July C low and the first wave (v) objective, shared with the weekly panel (50% weekly retracement at 3,077). Three-month is $7.50 above it on the 08-October official; the post-official electronic close ($3,042.0, SMM) was beneath it."
st['fwd_pivots'][0]['t']=0.99996
st['fwd_pivots'][1]['t']=0.99998
st['fwd_pivots'][0]['w']="FIRST TEST NOW: the 3,061.5 July low (and 3,077, the weekly 50% retracement, already $8.00 above the 08-October three-month). Wave (v) of C is under way from the 3,148.5 wave (iv) high and has travelled $79.50 so far; a daily official settlement beneath 3,061.5 extends it towards the 2,980 area. Rule check: wave (iii) (3,289 to 3,118, $171) cannot be the shortest, so wave (v) should not exceed $171 from 3,148.5 - a cap near 2,977.5; a settlement beneath that would force a re-count (extension of a larger degree)."
st['fwd_pivots'][1]['w']="THE INVALIDATION: 3,289, the 12-September (ii) high. A DAILY OFFICIAL SETTLEMENT ABOVE IT negates the bearish C-wave count. NEARER TELLS: a settlement back above 3,148.5 would mean wave (v) truncated and the C wave is complete; above 3,183 (wave (i) low) would void the impulsive labelling and promote the corrective alternate."
st['writeup']=("DAILY (SWING DEGREE) - THE C-WAVE COUNT IS UNCHANGED AND WAVE (v) IS EXTENDING. Three-month settled $3,069.00 on Thursday 08-October, down $45.00, a third successive low beneath the 3,148.5 wave (iv) high, and the post-official electronic close (SMM, $3,042) was already beneath the 3,061.5 July low. "
 "BASE CASE, ABOUT 64%: the 3,061.5-3,374 rally was a corrective B wave and the C wave from 3,374 is in its fifth leg - (i) 3,183, (ii) 3,289, (iii) 3,118, (iv) 3,148.5, (v) in progress. The cardinal rules hold: (ii) did not exceed 3,374, (iv) at 3,148.5 did not overlap the (i) low at 3,183, and (iii) at $171 is shorter than (i) at $191, so (v) must stay shorter than $171 - capping it near 2,977.5. Targets: a settled break of 3,061.5, then 2,980-3,000. The second successive narrowing of the contango is a warning that (v) may end close to the cap rather than extend. "
 "ALTERNATE, ABOUT 36%: a deep expanded flat or double-three that holds the 3,040-3,060 area on a settled basis and turns higher; a daily settlement above 3,148.5 would be the first sign and above 3,183 would promote it. "
 "INVALIDATION: a daily official settlement above 3,289, $220.00 above the 08-October three-month. CONFIDENCE IS MODERATE. This is technical context, not advice.")
lt=ew['long_term']
lt['fwd_pivots'][0]['w']=("THE 3,261 LEVEL - THE 38.2% RETRACEMENT OF THE 3,855-TO-3,061.5 DECLINE - WAS THE WEEKLY TEST AND IT FAILED: the 02-October weekly close settled three-month at $3,122.00, $139.00 beneath it; on 08-October three-month is $3,069.00, $192.00 beneath. Per the pre-registered rule the weekly alternate (the move off 3,061.5 was corrective) is preferred. 3,261 is now overhead resistance.")
lt['fwd_pivots'][1]['w']=("THE DOWNSIDE REFERENCES ARE SHARED WITH THE DAILY PANEL: the 50% retracement at 3,077 is now $8.00 ABOVE the 08-October three-month of $3,069.00, with the 3,061.5 July low $7.50 beneath it; the 61.8% at 2,894 is where the bear path terminates. A WEEKLY close beneath 3,077 invalidates the constructive count outright - the week closes on today's 09-October official. Overhead, the 23.6% retracement at 3,488 is $419.00 above.")
lt['writeup']=("WEEKLY (POSITION DEGREE) - THE ALTERNATE PROMOTED AFTER THE FAILED WEEKLY TEST REMAINS PREFERRED AND THE DECISIVE WEEKLY CLOSE IS TODAY. The 3,855 high of 02-June terminates the position-degree advance; the decline into 3,061.5 on 02-July is a completed A-B-C and the 50% retracement at 3,077 held. The 02-October weekly close at $3,122.00 sat $139.00 beneath the 3,261 retracement; Thursday 08-October's settlement at $3,069.00 is $8.00 beneath 3,077 with one session of the week left. "
 "PREFERRED COUNT, ABOUT 60%: the move off 3,061.5 was corrective - a B wave or the opening leg of a larger fourth wave - and the decline under way breaks the 2,950-3,110 zone towards the 61.8% retracement at 2,894. "
 "ALTERNATE, ABOUT 40%: a new position-degree advance is still building off 3,061.5 as long as that low and 3,077 hold on a weekly close; targets 3,488, then 3,680 and 3,840 into mid-2027. "
 "INVALIDATION: a weekly close beneath 3,077 on today's official invalidates the constructive alternate outright; a weekly close back above 3,261 would restore it as preferred. CONFIDENCE IS LOW-TO-MODERATE. This is technical context, not advice.")
lt['proj']={"bull":[[0.66,3069.0],[0.76,3350],[0.88,3580],[1.0,3800]],"base":[[0.66,3069.0],[0.78,3020],[0.9,3150],[1.0,3240]],"bear":[[0.66,3069.0],[0.8,2950],[1.0,2890]]}

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-07', ph['rows'][-1]
ph['rows'][-1]=['2026-10-08',cash,m3,stk]
ph['updated']=RD
ph['basis']=("London Metal Exchange official settlements via Westmetall. LME Aluminium official cash settlement, official 3-month, and LME warehouse stock. Weekly sampling (last published official session of each week). AT THE 09-OCTOBER-2026 UPDATE the row for the week of 05-October is PROVISIONAL: the Thursday 08-October session (cash 3,060.50, 3-month 3,069.00, stock 238,875 t), replacing Wednesday's, to be replaced by the Friday 09-October session once it prints; the week of 28-September is FINAL at the Friday 02-October session. Verified against both cache-busted Westmetall language overviews and the per-metal aluminium daily table.")
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok', d['metals_board'], mh['al'][-1], mh['zn'][-1], mh['pb'][-1], round(tl,2), round(share,1), round(ratio,2))

# --- follow-up (same run): refresh the stale curve reference in premium_drivers[0]
d=json.load(open(P,encoding='utf-8'))
pdv=d['premium_drivers'][0]
pdv['d']=pdv['d'].replace("an $11.50 contango on 07-October.","an $8.50 contango on 08-October, narrowing.")
assert "$8.50 contango on 08-October" in pdv['d']
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('premium driver tail refreshed')
