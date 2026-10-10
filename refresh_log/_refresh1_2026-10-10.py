# Daily data refresh - 2026-10-10 (SATURDAY - NO LME RING). Board ROLLED to FRIDAY 09-Oct LME official, carried through the weekend.
# EN+DE cache-busted overviews agree exactly on 09-Oct; Al per-metal table shows 09-Oct newest (no later row), 08-Oct prior unchanged; 5/5 stock lines reconcile.
import json, re
P='market_data.json'
d=json.load(open(P,encoding='utf-8'))
RD='2026-10-10'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TEA="https://tradingeconomics.com/commodity/aluminum"
S_TED="https://tradingeconomics.com/united-states/currency"
S_TEB="https://tradingeconomics.com/commodity/brent-crude-oil"
S_MID="https://news.metal.com/newscontent/104148344-dollar-crude-oil-weakens-base-metals-overseas-market-outperforms-domestic-market-shfe-tin-plunges-lme-copper-aluminum-tin-and-gold-futures-lead-gains-smm-midday-review"
S_BBG="https://www.bloomberg.com/news/articles/2026-10-09/copper-set-for-weekly-gain-on-china-s-return-and-supply-concerns"
S_DA="https://discoveryalert.com/analysis/lme-aluminium-price-curve-october-2026/"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']

cash,prev_c,m3,prev_m,stk,prev_s=3055.5,3060.5,3070.0,3069.0,238875,238875
spr=cash-m3
pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100
wk=(m3-3122.0)/3122.0*100

VER=("COMPILED SATURDAY 10-OCTOBER-2026. THERE IS NO LONDON METAL EXCHANGE RING ON SATURDAY OR SUNDAY, SO THE FRIDAY 09-OCTOBER-2026 OFFICIAL IS THE CORRECT, LATEST PUBLISHED SESSION AND IS CARRIED THROUGH THE WEEKEND; THE NEXT OFFICIAL PRINTS MONDAY 12-OCTOBER AT 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted English and German Westmetall overviews AGREE EXACTLY on 09-October across all six metals, all six stock lines and the foreign-exchange fixings; (2) the aluminium per-metal daily table shows 09-October as the newest row - NO ROW AFTER IT - with 08-October reproduced unchanged as the prior row; "
 "(3) ALL FIVE STOCK LINES RECONCILE against the levels carried for 08-October: aluminium 238,875 unchanged; copper 235,225 less 2,200 to 233,025; nickel 284,178 less 1,314 to 282,864; zinc 127,425 less 575 to 126,850; lead 347,875 less 750 to 347,125. "
 "The whole board sits on ONE UNIFORM SESSION (09-October) and no intraday, closing, reference or contract-for-difference mark is used anywhere in it. Prior-month averages remain the completed SEPTEMBER-2026 official means.")

AL=(f" CASH SETTLED $3,055.50 ON THE 09-OCTOBER OFFICIAL, DOWN $5.00 OR {pc:.2f}% FROM $3,060.50. THREE-MONTH SETTLED $3,070.00, UP $1.00 OR {pm:.2f}% FROM $3,069.00 - the first non-negative three-month settlement in four sessions, $8.50 ABOVE THE 3,061.5 JULY LOW (which therefore HELD on a settled basis) but $7.00 BENEATH THE 3,077 WEEKLY 50% RETRACEMENT, and this was the WEEKLY CLOSE. "
 "SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS: three-month edged up while cash fell, so the CONTANGO WIDENED $6.00 TO $14.50 from $8.50 - the structure softened, reversing two sessions of narrowing. "
 f"VISIBLE LME STOCK WAS UNCHANGED AT 238,875 TONNES for a fourth session. On the week three-month fell $52.00 or {wk:.2f}% from the 02-October weekly close of $3,122.00. "
 "The LME euro fixing firmed to 1.1209 from 1.1177; Trading Economics (09-October) has the dollar index near 102.2, on track for a fourth straight weekly gain and at its highest since April 2025.")

d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,055.5","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,070.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $191.00 BELOW 3,261, $113.00 BELOW THE BROKEN 3,183 DAILY LEVEL, $219.00 BELOW THE 3,289 DAILY INVALIDATION, $7.00 BENEATH the 3,077 weekly 50% retracement and $8.50 above the 3,061.5 July low."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-14.5","pos":False,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,055.50 against three-month $3,070.00 is a $14.50 CONTANGO, WIDENED $6.00 from $8.50. Spread and flat price moved in OPPOSITE directions (three-month up $1.00, contango wider). The published reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET; the bearish structural confirmation, a contango beyond $24.50, is also unmet. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"238,875","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK WAS UNCHANGED AT 238,875 TONNES for a fourth session, holding the series low on this page. September's mean stock was {sep_s:,} tonnes. Flat stock alongside a modestly wider contango says visible stock is still not the driver of price."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,070.00, UP $1.00 OR {pm:.2f}% FROM $3,069.00, $8.50 above the 3,061.5 July low and $7.00 beneath the 3,077 weekly 50% retracement on the weekly close. AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK UNCHANGED AT 238,875 TONNES. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-8.5,"avg":sep_sp,"note":VER+f" A $14.50 CONTANGO, WIDENED $6.00 FROM $8.50. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in OPPOSITE directions (three-month up, contango wider). PUBLISHED REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1209,"prev":1.1177,"avg":1.1465,"note":VER+" THE LME EURO FIXING FIRMED TO 1.12090 FROM 1.11770 at the Friday ring; the ECB fixing printed 1.12060 and BFIX 1.12084. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]

d['outlook']['forward_path']=[
 {"tenor":"Cash (09-Oct official)","price":"3,055.5","basis":f"THE 09-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,055.50, DOWN $5.00 OR {pc:.2f}%. Carried through the weekend; next official Monday 12-October 13:20 London."},
 {"tenor":"3-month (09-Oct official)","price":"3,070.0","basis":f"THE 09-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,070.00, UP $1.00 OR {pm:.2f}% - the weekly close: $8.50 above the 3,061.5 July low, $7.00 beneath the 3,077 weekly 50% retracement, $113.00 beneath the broken 3,183."},
 {"tenor":"Cash-to-3M structure","price":"-14.5 (CONTANGO)","basis":"A $14.50 CONTANGO, widened $6.00 from $8.50. Flat price and spread moved in OPPOSITE directions."},
 {"tenor":"Visible LME stock","price":"238,875 t","basis":f"UNCHANGED on the session for a fourth day; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE CURVE SOFTENED AGAIN ON THE WEEKLY CLOSE. On the 09-October official cash $3,055.50 sits $14.50 BELOW three-month $3,070.00, a CONTANGO widened $6.00 from $8.50. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50 and now $14.50. "
 f"READ: still a modest contango with visible stock flat at 238,875 t - the slide remains a flat-price (macro, premium and supply-recovery) repricing rather than a prompt glut, but Friday's widening removes the 'structure firming' signal of the prior two sessions. The September mean spread was ${sep_sp:,.2f}. The published reversal condition (a backwardation beyond $15.00) is unmet; a contango beyond $24.50 would be the bearish structural confirmation.")

ls=d['lme_series']; assert ls[-1][0]=='08-Oct', ls[-1]
d['lme_series']=ls[1:]+[["09-Oct",cash,m3,stk]]
d['chart_price_axis']=[2950,3450]
d['chart_stock_axis']=[225000,255000]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2950<r[1]<3450 and 2950<r[2]<3450 for r in d['lme_series'])
# (cash, 3M, prev cash, prev 3M)
CU=(14689.0,14570.0,14526.0,14417.0); NI=(15545.0,15720.0,15415.0,15600.0); ZN=(3840.0,3781.5,3781.0,3737.0); PB=(1847.0,1883.5,1833.0,1874.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0]
zn_old=sum(zs)/6; pb_old=sum(ps)/6
zn_avg=(sum(zs)+3840.0)/7; pb_avg=(sum(ps)+1847.0)/7
mh['zn'][-1]=round(mh['zn'][-1]*zn_avg/zn_old,1); mh['pb'][-1]=round(mh['pb'][-1]*pb_avg/pb_old,1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])): R[k]=R[k][1:]+[v]
ms['asof']='2026-10-09'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending FRIDAY 09-OCTOBER-2026 (carried through the weekend; no ring Saturday or Sunday). THE WINDOW ROLLED THIS RUN: 18-September dropped and 09-October appended, so the window is 21-September to 09-October. Every point is an official cash settlement, verified against the cache-busted Westmetall English and German overviews, which agree to the cent, the aluminium per-metal daily table (no row after 09-October), and five-for-five stock-line reconciliation. Next official Monday 12-October.")
ms['src']=["Westmetall - LME official cash settlements, EN and DE overviews cache-busted and in exact agreement (09-October-2026 session)",W]

AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,689.00, up $163.00 or 1.12%; three-month $14,570.00, up $153.00 or 1.06%. The BACKWARDATION WIDENED to $119.00 from $109.00 while stock DREW 2,200 tonnes to 233,025 - prompt tightness firming for a fourth session. Bloomberg (09-October) headlined copper set for a weekly gain on China's return and supply concerns."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,545.00, up $130.00 or 0.84%; three-month $15,720.00, up $120.00 or 0.77%, recovering part of Thursday's loss. CONTANGO $175.00 from $185.00, still the widest carry on the board. Stock drew 1,314 tonnes to 282,864."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,840.00, up $59.00 or 1.56%; three-month $3,781.50, up $44.50 or 1.19%. The BACKWARDATION WIDENED to $58.50 from $44.00 while stock drew 575 tonnes to 126,850. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,847.00, up $14.00 or 0.76%; three-month $1,883.50, up $9.50 or 0.51%. CONTANGO narrowed to $36.50 from $41.00. Stock drew 750 tonnes to 347,125, a fifteenth consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL, REPORTED AS DATA NOT AS A REGIME SIGNAL: on the Friday 09-October official the rest of the board rebounded in three-month terms - zinc +1.19%, copper +1.06%, nickel +0.77%, lead +0.51% - while aluminium three-month was flat (+0.03%) and aluminium cash fell. The LME euro fixing firmed to 1.1209. Aluminium LAGGED a broad base-metal rebound.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

OLDH="COMPILED FRIDAY 09-OCTOBER-2026, BEFORE THE LME RING (REVIEWED; NO NEW MARK FOR THIS ROW LOCATED SINCE THE PRIOR RUN - CHINESE MARKETS REOPENED 08-OCTOBER AFTER THE NATIONAL DAY HOLIDAY AND NO POST-HOLIDAY WEEKLY ASSESSMENT FOR THIS ROW HAD BEEN LOCATED)."
NEWH="COMPILED SATURDAY 10-OCTOBER-2026, NO LME RING (REVIEWED; NO NEW MARK FOR THIS ROW LOCATED SINCE THE PRIOR RUN - NO POST-HOLIDAY SMM WEEKLY ASSESSMENT FOR THIS ROW WAS LOCATED, AND THE MID-MONTH CARBON SETTLEMENT CYCLE HAS NOT YET PRINTED)."
n_rep=0
for i in d['inputs']:
    if isinstance(i.get('src'),str) and OLDH in i['src']: i['src']=i['src'].replace(OLDH,NEWH); n_rep+=1
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='08-Oct'
        i['hist']=i['hist'][1:]+[["09-Oct",CU[0]]]
        assert len(i['hist'])==15
        i['val']="~14,570.00 (3M); 14,689.00 (cash) $/t"
        i['ratio']="~14,689.00 $/t cash vs LME 3M 14,570.00 $/t"
        i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the FRIDAY 09-OCTOBER-2026 session at $14,689.00, UP $163.00 or 1.12% against $14,526.00 (carried through the weekend; no ring Saturday or Sunday). THE WINDOW ROLLED THIS RUN: 18-September dropped and 09-October appended, so the series is the last fifteen published official cash sessions, 21-September to 09-October - the same window as the LME Board sparklines. Official settlement only, verified on the cache-busted Westmetall English and German overviews, which agree to the cent. "
                  "Copper structure for context: backwardation $119.00 (from $109.00), stock drew 2,200 t to 233,025 t.")
print('inputs header replaced', n_rep); assert n_rep>=9
d['inputs_summary']=("UPDATE 10-OCTOBER (SATURDAY, NO RING): copper rolled to the Friday 09-October LME official cash of $14,689.00, up $163.00, with its fifteen-session window moved to 21-September to 09-October. No post-holiday SMM fluoride, silicon or magnesium weekly mark was located, and the carbon settlement cycle (anodes, pitch, green coke) is due mid-October - so every other row is carried at its own dated public mark and no value was interpolated.")
nr=0
for r in d['raw_materials']:
    if isinstance(r.get('src'),str) and OLDH in r['src']: r['src']=r['src'].replace(OLDH,NEWH); nr+=1
print('raw header replaced', nr); assert nr==3

ratio=360.4/m3*100
ALNOTE=("COMPILED SATURDAY 10-OCTOBER-2026. NO NEW DATED PUBLIC ALUMINA PRICE MARK ON THIS PANEL'S OWN SOURCES WAS LOCATED: the LME Alumina (Platts) row stays at AL Circle's $360.40/t print of 30-September; the FOB East Australia trade row stays at its 18-September mark; the SMM alumina index is carried at its 30-September print of 2,669.99 yuan/tonne. THIRD-PARTY CONTEXT, NOT SUBSTITUTED INTO ANY ROW: a Discovery Alert analysis (05-October) reports Platts alumina at $372.84/t on 02-October, up about 5% from $355.34/t on 30-September; that secondary report has not been matched to a primary print and is labelled rather than used. SUPPLY CONTEXT: Norsk Hydro (05-October, via Reuters/Engineering News) guided a further $90-110m fourth-quarter cost at its Alunorte refinery from gas bought above contract. "
 f"THE RATIO: LME Alumina at $360.40/t against the 09-October aluminium three-month of $3,070.00 is {ratio:.2f}%, against a decade norm of 15-17%. Alumina remains historically CHEAP relative to metal.")
for a in d['alumina']: a['src']=ALNOTE

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
PREM=("COMPILED SATURDAY 10-OCTOBER-2026 (NO LME RING). PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND THIS PANEL CARRIES EACH ROW AT ITS OWN LAST PUBLIC ASSESSMENT DATE. NO NEW ASSESSMENT ON ANY ROW'S OWN BASIS WAS LOCATED FOR THIS WINDOW, so every row is CARRIED UNCHANGED. CONTEXT FROM A DIFFERENT ASSESSOR, NOT MIXED INTO ANY ROW: AL Circle (06-October) reports CRU's Asia CIF premium at $202/t and Q4 MJP offers down to $245-260/t from $325/t in early September, against the $395/t Q3 benchmark; earlier SMM reporting (30-September) had Rio Tinto at $280/t and South32 at $265/t. No Q4 settlement had been publicly reported when this page compiled. These are offers, not a settlement. "
 f"THE TARIFF DECOMPOSITION IS REFRESHED DAILY BY DESIGN: on a re-verified Section 232 rate of 50% on aluminium articles applied to full customs value, the tariff leg of the US duty-paid premium is 0.50 times the 09-October official cash of $3,055.50, or ${tl:,.2f}, DOWN $2.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}% of the US duty-paid premium is policy arithmetic rather than market. "
 "This page does NOT fabricate freight, financing or tightness splits for any premium row.")
for p in d['premiums']:
    s=p['src']; j=s.find("for any premium row.")
    if s.startswith("COMPILED") and j>0: p['src']=PREM+s[j+len("for any premium row."):]
    else: p['src']=PREM+" "+s
pq=d['premium_quarters']; assert pq[-1]['q']=='Q4-26' and pq[-1]['v'] is None
pq[-1]['range']=[245,280]

d['lme_commentary']=(f"ALUMINIUM HELD THE JULY LOW ON A SETTLED BASIS BUT CLOSED THE WEEK BENEATH 3,077. On the Friday 09-October official cash settled $3,055.50, down $5.00 or {pc:.2f}%, and three-month $3,070.00, up $1.00 or {pm:.2f}% - $8.50 above the 3,061.5 July low but $7.00 beneath the 3,077 weekly 50% retracement on the weekly close. On the week three-month fell $52.00 or {abs(wk):.2f}%. "
 "Cash fell while three-month edged up, so the contango WIDENED $6.00 to $14.50 (spread and price in OPPOSITE directions) and visible stock was unchanged at 238,875 t for a fourth session. "
 "Aluminium lagged a broad base-metal rebound: zinc +1.19%, copper +1.06%, nickel +0.77% and lead +0.51% in three-month terms. SMM's Friday midday review had LME aluminium up 1.07% in Asian trade while the SHFE contract slipped 0.36%; Trading Economics' reference price ended Friday near $3,055.65, up about 0.47% from the post-official Thursday close, but down 6.83% over the month. "
 f"The dollar index held near 102.2, set for a fourth straight weekly gain and its highest since April 2025 (Trading Economics). September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND IN CONTROL; THE JULY LOW HELD BUT THE WEEKLY TEST FAILED. Against: the weekly close at 3,070 settled beneath the 3,077 retracement, invalidating the constructive weekly count; aluminium lagged a base-metal rebound; the contango widened again to $14.50; the dollar posted a fourth weekly gain to its highest since April 2025 and markets still lean towards a December Fed hike; Asian premium offers sit at $245-260/t versus $395/t in Q3; the narrative is supply recovery. "
 "Constructive: 3,061.5 held on a settled basis for a second session; visible LME stock is holding at a series low (238,875 t); Brent near $104 and record tanker freight keep the energy cost floor high; Chinese ingot-plus-billet stock builds have so far been described as moderate.")
d['commercial']=("COMMERCIAL READ - GENERIC AND PUBLIC. FIRST, THE CURVE PAYS BUYERS A LITTLE MORE TO WAIT: a $14.50 contango on 09-October, widened from $8.50. SECOND, ASIAN PREMIUMS ARE RESETTING LOWER: public reporting has Q4 MJP offers at $245-260/t (AL Circle, 06-October) and CRU's Asia CIF at $202/t, against $395/t in Q3; no settlement is yet reported. THIRD, THE TARIFF ARITHMETIC MOVED WITH THE METAL: "
 f"on a verified 50% Section 232 rate, the tariff leg of the US Midwest duty-paid premium is ${tl:,.2f} on 09-October cash, {share:.1f}% of the $2,403/t premium. FOURTH, WATCH THE CALENDAR: Monday's official decides whether 3,061.5 keeps holding; a Q4 Japanese premium settlement could come any day; China's post-holiday inventory prints and the mid-October carbon settlements are due next week, and the Q3 producer reporting season opens mid-month. This is generic public market context, not advice.")

for s in d['outlook']['scenarios']:
    dr=s['drivers']
    dr=re.sub(r"^MOVED 09-OCTOBER \(from 13/45/42 to 12/45/43\):.*?settled break of 3,061\.5\. ","PREVIOUSLY MOVED 09-OCTOBER (to 12/45/43 after the 08-October new low). ",dr,flags=re.S)
    s['prob']={'Bull':'11%','Base':'45%','Bear':'44%'}[s['case']]
    s['drivers']=("MOVED 10-OCTOBER (from 12/45/43 to 11/45/44): the Friday 09-October official was the weekly close and three-month settled at 3,070, beneath the 3,077 weekly retracement, invalidating the constructive weekly count; the contango widened to $14.50 and aluminium lagged a broad base-metal rebound. One point moves from bull to bear. The settled hold of the 3,061.5 July low for a second session and flat stock argue against a bigger shift. ")+dr
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['bottom_line']=(f"BOTTOM LINE: aluminium settled on the Friday 09-October LME official at cash $3,055.50 and three-month $3,070.00 - the July low at 3,061.5 held on a settled basis, but the weekly close sat $7.00 beneath the 3,077 retracement, and three-month fell {abs(wk):.2f}% on the week. "
 "The contango widened to $14.50 and visible stock held at 238,875 t, while aluminium lagged a broad base-metal rebound. Scenario weights move to 11% bull / 45% base / 44% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) still targets a settled break of 3,061.5 then 2,980-3,000 with a rule-based floor near 2,977, invalidation 3,289; on the weekly panel the constructive alternate is now invalidated and the corrective count towards 2,894 is preferred at about 70%.")

d['so_what']={"line":"Aluminium held its early-July floor near $3,060 on Friday's official but closed the week beneath a key $3,077 retracement and lagged a broad base-metal rebound - the bias stays lower into next week unless that floor turns into a base.",
 "points":[
 f"WHAT MOVED: Friday's LME official settled cash at $3,055.50 (-$5.00) and three-month at $3,070.00 (+$1.00), down {abs(wk):.2f}% on the week; copper, zinc, nickel and lead all rose 0.5-1.2% while aluminium was flat. The contango widened to $14.50 and LME stock was unchanged at 238,875 t.",
 "WHY: a strong dollar (fourth straight weekly gain, highest since April 2025) and expectations of another Fed hike, plus a market now pricing supply recovery rather than disruption, are weighing on aluminium more than on other base metals (Trading Economics, SMM).",
 "PREMIUMS AND COSTS: Q4 Japanese premium offers remain $245-260/t versus $395/t in Q3 (AL Circle), with no settlement yet; energy stays expensive, with Brent near $104 and tanker freight at records amid Hormuz disruption (Trading Economics).",
 "WHAT TO WATCH: Monday's LME official against $3,061.5 - a settled break opens $2,980-3,000; a Q4 Japanese premium settlement; China's post-holiday inventory prints and mid-October carbon settlements; the Q3 producer earnings season starting mid-month."]}

new_feed=[
 {"when":"Sat 10-Oct","impact":"Mixed","text":f"BOARD ROLLED TO THE FRIDAY 09-OCTOBER LME OFFICIAL (carried through the weekend - no ring). Cash $3,055.50 (-$5.00), three-month $3,070.00 (+$1.00, {pm:.2f}%) - July low 3,061.5 held, weekly close $7.00 beneath 3,077 - contango WIDENED to $14.50 from $8.50, stock unchanged at 238,875 t. Verified on cache-busted English and German overviews in exact agreement, the aluminium per-metal table with no later row, and five-for-five stock reconciliation."},
 {"when":"Fri 09-Oct","impact":"Bearish","text":"ALUMINIUM LAGS A BASE-METAL REBOUND: three-month zinc +1.19%, copper +1.06%, nickel +0.77%, lead +0.51% on the Friday official versus aluminium +0.03%; Bloomberg headlined copper set for a weekly gain on China's return and supply concerns."},
 {"when":"Fri 09-Oct","impact":"Bearish","text":"DOLLAR'S FOURTH WEEKLY GAIN (Trading Economics, 09-October): the dollar index held near 102.2, its highest since April 2025; the US ten-year about 5.24%; markets price roughly 69-81% odds of a December Fed hike."},
 {"when":"Fri 09-Oct","impact":"Mixed","text":"ENERGY AND SHIPPING (Trading Economics, 09-October): Brent near $104.4 after the US issued a temporary licence for about 22.5 million barrels of Russian diesel; tanker freight at record highs with ships tied up in transfers outside Hormuz and eleven tankers attacked in the Strait in the week to 04-October."},
]
d['feed']=(new_feed+d['feed'])[:12]

new_news=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":f"LME ALUMINIUM HOLDS THE JULY LOW BUT CLOSES THE WEEK BENEATH 3,077. The Friday 09-October official settled cash at $3,055.50 ({pc:.2f}%) and three-month at $3,070.00 (+{pm:.2f}%), $8.50 above the 3,061.5 July low and $7.00 beneath the 3,077 weekly retracement; three-month fell {abs(wk):.2f}% on the week. The contango widened to $14.50 from $8.50 and visible stock was unchanged at 238,875 t."},
 {"theme":"Base metals","horizon":"Days","impact":"Bearish (relative)","url":S_BBG,
  "headline":"ALUMINIUM LAGS AS BASE METALS REBOUND (LME official 09-October; Bloomberg, 09-October): copper three-month rose 1.06% to $14,570 with its backwardation widening to $119 and stock drawing to 233,025 t, zinc +1.19% and nickel +0.77%; Bloomberg headlined copper set for a weekly gain on China's return and supply concerns. Aluminium three-month was flat, underlining metal-specific supply-recovery pressure."},
 {"theme":"Macro","horizon":"Days-weeks","impact":"Bearish","url":S_TED,
  "headline":"DOLLAR HEADS FOR A FOURTH WEEKLY GAIN AT ITS HIGHEST SINCE APRIL 2025 (Trading Economics, 09-October): the dollar index held near 102.2; September FOMC minutes showed most policymakers expect another hike this year and Governor Waller said further increases will likely be needed; the US ten-year yield is about 5.24%."},
 {"theme":"Energy","horizon":"Weeks","impact":"Mixed","url":S_TEB,
  "headline":"BRENT HOLDS NEAR $104 AS HORMUZ STRAINS SHIPPING (Trading Economics, 09-October): the US Treasury issued a temporary licence allowing roughly 22.5 million barrels of Russian diesel to market; tankers are tied up in ship-to-ship transfers outside the Strait of Hormuz, freight rates are at record highs and eleven tankers were attacked in the Strait in the week ending 04-October. President Trump said the US would not strike Iran again before the midterm elections."},
 {"theme":"China","horizon":"Days","impact":"Mixed","url":S_MID,
  "headline":"OVERSEAS OUTPERFORMS SHANGHAI (SMM midday review, 09-October): LME aluminium was up 1.07% in Asian trade while the most-traded SHFE aluminium contract slipped 0.36% and foundry-alloy futures fell 0.64%, as the dollar and crude eased intraday."},
]
d['news']=new_news+d['news'][:15]

cats=d['outlook']['catalysts']
for c in cats:
    if c['date']=='Daily, from Fri 09-Oct':
        c['date']='Daily, from Mon 12-Oct'
        c['event']="3,061.5 HELD, 3,077 FAILED ON THE WEEKLY CLOSE, 3,183 OVERHEAD, 3,289 INVALIDATION. Three-month settled $3,070.00 on Friday 09-October, $8.50 above the 02-July low at 3,061.5 and $7.00 beneath the 3,077 weekly 50% retracement - the weekly close beneath 3,077 invalidated the constructive weekly alternate. A settled official beneath 3,061.5 opens the 2,980 area (wave (v) of C, rule cap near 2,977); a daily settlement above 3,148.5 would warn the C wave is complete and above 3,183 would void the impulsive C-wave labelling."
    if c['date']=='Any day (pending)':
        c['event']="Q4-2026 JAPANESE QUARTERLY PREMIUM (MJP) SETTLEMENT. Latest public offers $245-260/t (AL Circle, 06-October), after $265-280/t from South32 and Rio Tinto (SMM, 30-September); CRU's Asia CIF premium is $202/t; versus $395/t in Q3. Not yet reported as settled at 10-October."
d['outlook']['catalysts']=cats

RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 10-OCTOBER: the contango WIDENED $6.00 to $14.50 on 09-October as cash fell and three-month edged up - reversing two narrowing sessions but still well inside the $24.50 bearish-confirmation threshold. Trend held at FLAT."
RK[1]['risk']+=" UPDATE 10-OCTOBER: the dollar index posted a fourth straight weekly gain to its highest since April 2025; September FOMC minutes showed most policymakers expect another hike this year (Trading Economics). Trend held at UP."
RK[4]['risk']+=" UPDATE 10-OCTOBER: LME stock unchanged at 238,875 t on 09-October for a fourth session, holding the series low. Trend held at FLAT."
RK[7]['risk']+=" UPDATE 10-OCTOBER: Brent near $104.4 with tanker freight at record highs (Trading Economics, 09-October); the US licensed about 22.5 million barrels of Russian diesel to market. Trend held at FLAT."
RK[8]['risk']+=" UPDATE 10-OCTOBER: no Q4 settlement reported; latest offers $245-260/t. Trend held at DOWN."
RK[9]['risk']+=" UPDATE 10-OCTOBER: Trading Economics (09-October) reports eleven tankers attacked in the Strait of Hormuz in the week ending 04-October and tankers tied up in ship-to-ship transfers outside it. Trend held at UP."

d['outlook']['ai_analysis'][0]=(f"SATURDAY REVIEW, 10-OCTOBER (NO RING): Friday's official was the weekly close. Three-month settled $3,070.00 (+{pm:.2f}%), holding the 3,061.5 July low on a settled basis for a second session but $7.00 beneath the 3,077 weekly retracement, which invalidates the constructive weekly count. Aluminium lagged a broad base-metal rebound and the contango widened to $14.50, so the structure no longer leans against the decline; the bear case is raised to 44%. Monday's official against 3,061.5 is the next test.")

for l in d['logistics']:
    if l['name']=='Strait of Hormuz transit':
        rest=l['note'].split(' PRIOR: ',1)[-1]
        l['note']=("REVIEWED SATURDAY 10-OCTOBER-2026. Trading Economics' Brent coverage (09-October) says the US-Iran conflict continues to strain shipping: tankers are tied up in ship-to-ship transfers outside the Strait of Hormuz, freight rates are at record highs and eleven tankers were attacked in the Strait in the week ending 04-October; President Trump said the US would not strike Iran again before the midterm elections. No container or bulk transit count is published because tracker figures remain disputed. Arrow stays UP pending a public, verifiable normalisation signal. PRIOR: "+rest)
        l['src']="REVIEWED SATURDAY 10-OCTOBER-2026: Trading Economics Brent ("+S_TEB+"). PRIOR: "+l['src'].split(' PRIOR: ',1)[-1]
    if l['name'].startswith('Red Sea'):
        l['note']=re.sub(r"^REVIEWED FRIDAY 09-OCTOBER-2026 \(.*?\):","REVIEWED SATURDAY 10-OCTOBER-2026 (no newer public transit count located; earlier note carried):",l['note'],count=1)

for m in d['macro']:
    if m['name'].startswith('Brent'):
        m['value']='104.43'; m['day']="+0.14% on Friday 09-October; -2.97% over the month (Trading Economics)"
        m['note']="REFRESHED SATURDAY 10-OCTOBER-2026 on a public reference board (Trading Economics, Friday 09-October close): Brent hovered near $104 after the US issued a temporary licence for about 22.5 million barrels of Russian diesel, while Hormuz disruption kept tanker freight at record highs. Energy is a major smelter cash-cost line."
    elif m['name'].startswith('US dollar index'):
        m['value']='102.23'; m['day']="+0.09% on Friday 09-October; +3.21% over the month; fourth straight weekly gain (Trading Economics)"
        m['note']="REFRESHED SATURDAY 10-OCTOBER-2026 on a public reference board (Trading Economics): the dollar held near 102, its highest since April 2025, set for a fourth weekly gain; September FOMC minutes showed most policymakers expect another hike this year. A firm dollar weighs on dollar-priced metals."
    elif m['name'].startswith('US 10-year'):
        m['value']='5.24'; m['day']="about 5.237% at the Friday 09-October close, broadly flat on the day (Trading Economics)"
        m['note']="REFRESHED SATURDAY 10-OCTOBER-2026 on a public reference board (Trading Economics). Higher yields raise the cost of carrying metal and financing inventory."
    elif m['name']=='EUR/USD':
        m['value']='1.12090'; m['day']="LME fixing on 09-October, +0.29% from 1.11770; ECB fixing 1.12060, BFIX 1.12084"
        m['note']="REFRESHED SATURDAY 10-OCTOBER-2026 to the 09-October LME fixing via Westmetall, the same session as the LME board."

for r in d['producer_status']:
    r['asof']=RD
    u=r['update']
    for a,b in (("REVIEWED 09-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE","REVIEWED 10-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE"),
                ("REVIEWED 09-OCTOBER: no newer public disclosure located; status below carried. ","REVIEWED 10-OCTOBER: no newer public disclosure located; status below carried. ")):
        if u.startswith(a): u=b+u[len(a):]; break
    else:
        u="REVIEWED 10-OCTOBER: no newer public disclosure located; status below carried. "+u
    r['update']=u

for s in [["Westmetall - LME official prices and stocks, 09-Oct-2026 session (EN+DE)",W],
          ["SMM - Midday review: overseas base metals outperform, LME aluminium +1.07% (09-Oct-2026)",S_MID],
          ["Bloomberg - Copper set for weekly gain on China's return and supply concerns (09-Oct-2026, headline)",S_BBG],
          ["Trading Economics - US dollar index, fourth weekly gain (09-Oct-2026)",S_TED],
          ["Trading Economics - Brent crude and Hormuz shipping (09-Oct-2026)",S_TEB],
          ["Trading Economics - Aluminum reference price (09-Oct-2026)",S_TEA]]:
    d['sources'].append(s)
d['outlook']['sources'].append(["Trading Economics - dollar index at highest since April 2025, Fed hike expectations (09-Oct-2026)",S_TED])

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 09-OCTOBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND BECAUSE THE MARKET IS SHUT: there is no ring on Saturday 10-October or Sunday 11-October, so Friday's official is the correct latest figure; the next official prints Monday 12-October at 13:20 London. Reference prices from Trading Economics and SMM intraday moves are cited in text only and are NOT used on the board.")
C[1]=("THE COMPLETENESS TEST PASSES: the aluminium per-metal daily table shows 09-October as the newest row with NO ROW AFTER IT and 08-October unchanged as the prior row; the other metals reconcile through the cache-busted overviews and stock arithmetic.")
C[2]=("THE ENGLISH AND GERMAN OVERVIEWS WERE BOTH REQUESTED CACHE-BUSTED ON 10-OCTOBER AND AGREE EXACTLY on 09-October across all six metals, stocks and FX fixings.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against the levels carried for 08-October: aluminium unchanged at 238,875; copper -2,200 to 233,025; nickel -1,314 to 282,864; zinc -575 to 126,850; lead -750 to 347,125.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (09-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (seven sessions, 01- to 09-October) as their latest point. The price chart axis floor (2,950) brackets three-month at 3,070; the stock chart axis floor (225,000 t) brackets visible stock at 238,875 t.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,055.50 against three-month $3,070.00 is therefore a $14.50 CONTANGO, widened $6.00 from $8.50 on 08-October - and it widened while three-month edged up, i.e. spread and price moved in OPPOSITE directions."
C[6]=("PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND NO NEW ASSESSMENT ON ANY ROW'S OWN BASIS WAS LOCATED FOR THIS WINDOW; every premium row is carried at its own assessment date. CRU's Asia CIF $202/t (AL Circle, 06-October) is a different assessor's basis and is reported in drivers and news only, not substituted into the CIF Japan row. No Q4-2026 Japanese quarterly settlement had been publicly reported when this page compiled on 10-October; the chart's pending band is the span of reported OFFERS ($245-280/t). Offers are not settlements.")
for i,c in enumerate(C):
    if c.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a re-verified 50% Section 232 rate on full customs value, the tariff leg is 0.50 times the 09-October official cash of $3,055.50, or ${tl:,.2f}, leaving an ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."
    if c.startswith("PEER EARNINGS ARE IN A LULL"):
        C[i]=("PEER EARNINGS ARE IN A LULL AND NO COMPANY WAS BACK-FILLED THIS RUN (10-October). The Q3-2026 reporting season opens in mid-October; no new quarterly result from a tracked producer was published this week; existing entries carry only exact publicly verified figures.")
    if c.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent ($104.43), the dollar index (102.23) and the US ten-year (about 5.24%) are Trading Economics reference marks for the Friday 09-October close; EUR/USD is the 09-October LME fixing; European gas TTF is carried at its Friday 02-October close (74.76 EUR/MWh) because no newer public reference value was captured this run. Hormuz and Bab el-Mandeb transit counts remain disputed, so none is published.")
    if c.startswith("THE ELLIOTT WAVE PANELS"):
        C[i]=c.split(' UPDATE 0')[0].split(' UPDATE 1')[0]+" UPDATE 10-OCTOBER: the WEEKLY CLOSE (09-October official, three-month 3,070) settled $7.00 beneath the 3,077 weekly 50% retracement, so per the pre-registered rule the constructive weekly alternate is INVALIDATED and the weekly panel is re-weighted; the daily C-wave count is unchanged and the 3,061.5 July low held on a settled basis."

ew=d['ew']; ew['updated']=RD
st=ew['short_term']
assert st['line'][-1]==[0.99992,3069.0], st['line'][-1]
st['proj']={"bull":[[0.99994,3070.0],[0.99997,3150],[1.0,3250]],
            "base":[[0.99994,3070.0],[0.99997,3030],[1.0,2995]],
            "bear":[[0.99994,3070.0],[0.99997,3010],[1.0,2977]]}
for f in st['fib']:
    if f['p']==3289.0: f['l']="3,289 - the 12-September (ii) high and the INVALIDATION of the bearish daily count. A daily official settlement above it negates the C-wave count. It is $219.00 above the 09-October three-month."
    if f['p']==3261.0: f['l']="3,261 - the shared 38.2% weekly retracement, held at the SAME price as the weekly panel. Two weekly closes have now settled beneath it (02-October $3,122, 09-October $3,070); three-month is $191.00 beneath it."
    if f['p']==3183.0: f['l']="3,183 - the 20-August low and the wave (i) low, BROKEN on 01-October. Wave (iv) peaked beneath it at 3,148.5; a settlement above 3,183 would void the impulsive labelling. $113.00 above three-month on 09-October."
    if f['p']==3061.5: f['l']="3,061.5 - the 02-July C low and the first wave (v) objective, shared with the weekly panel (50% weekly retracement at 3,077). Held on a settled basis for a second session: three-month $3,070.00 on 09-October, $8.50 above it, after an electronic low near $3,041.5 on 08-October (SMM)."
st['fwd_pivots'][0]['w']="FIRST TEST: the 3,061.5 July low, held on two settled officials (3,069 and 3,070) despite an electronic dip to about 3,041.5 on 08-October. Wave (v) of C is under way from the 3,148.5 wave (iv) high and has travelled $79.50 on a settled basis; a daily official settlement beneath 3,061.5 extends it towards the 2,980 area. Rule check: wave (iii) (3,289 to 3,118, $171) cannot be the shortest, so wave (v) should not exceed $171 from 3,148.5 - a cap near 2,977.5; a settlement beneath that would force a re-count."
st['fwd_pivots'][1]['w']="THE INVALIDATION: 3,289, the 12-September (ii) high. A DAILY OFFICIAL SETTLEMENT ABOVE IT negates the bearish C-wave count. NEARER TELLS: a settlement back above 3,148.5 would mean wave (v) truncated and the C wave is complete; above 3,183 (wave (i) low) would void the impulsive labelling and promote the corrective alternate."
st['writeup']=("DAILY (SWING DEGREE) - THE C-WAVE COUNT IS UNCHANGED; WAVE (v) IS STALLING AT THE JULY LOW. Three-month settled $3,070.00 on Friday 09-October, up $1.00, after Thursday's $3,069.00 low for the move; the 3,061.5 July low has held on two settled officials although the electronic market traded beneath it on 08-October. "
 "BASE CASE, ABOUT 62%: the 3,061.5-3,374 rally was a corrective B wave and the C wave from 3,374 is in its fifth leg - (i) 3,183, (ii) 3,289, (iii) 3,118, (iv) 3,148.5, (v) in progress. The cardinal rules hold: (ii) did not exceed 3,374, (iv) at 3,148.5 did not overlap the (i) low at 3,183, and (iii) at $171 is shorter than (i) at $191, so (v) must stay shorter than $171 - capping it near 2,977.5. Targets: a settled break of 3,061.5, then 2,980-3,000. Friday's wider contango and aluminium's lag against a base-metal rebound keep the extension case in front. "
 "ALTERNATE, ABOUT 38%: wave (v) is complete or nearly so at 3,069 (a short fifth at the July low, i.e. a double bottom) and an expanded flat or double-three turns higher; a daily settlement above 3,148.5 would be the first confirmation and above 3,183 would promote it. "
 "INVALIDATION: a daily official settlement above 3,289, $219.00 above the 09-October three-month. CONFIDENCE IS MODERATE. This is technical context, not advice.")
lt=ew['long_term']
lt['fwd_pivots'][0]['w']=("THE 3,261 LEVEL - THE 38.2% RETRACEMENT OF THE 3,855-TO-3,061.5 DECLINE - IS OVERHEAD RESISTANCE: two weekly closes have settled beneath it (02-October $3,122.00; 09-October $3,070.00, $191.00 beneath). A WEEKLY CLOSE BACK ABOVE 3,261 is the condition to restore a constructive position-degree count.")
lt['fwd_pivots'][1]['w']=("THE DOWNSIDE REFERENCES ARE SHARED WITH THE DAILY PANEL: the 09-October weekly close at $3,070.00 settled $7.00 BENEATH the 50% retracement at 3,077, which per the pre-registered rule INVALIDATES the constructive alternate; the 3,061.5 July low is $8.50 beneath the close; the 61.8% retracement at 2,894 is the preferred-count objective. Overhead, the 23.6% retracement at 3,488 is $418.00 above.")
lt['writeup']=("WEEKLY (POSITION DEGREE) - THE DECISIVE WEEKLY TEST FAILED AND THE CONSTRUCTIVE ALTERNATE IS INVALIDATED. The 3,855 high of 02-June terminates the position-degree advance and the decline into 3,061.5 on 02-July was an A-B-C. The 09-October weekly close settled three-month at $3,070.00, $7.00 beneath the 3,077 50% retracement - meeting the pre-registered invalidation of the 'new advance off 3,061.5' count - though the July low itself has not yet broken on a settled basis. "
 "PREFERRED COUNT, ABOUT 70%: the move off 3,061.5 to 3,374 was corrective (a B wave or the opening leg of a larger fourth wave) and the decline under way breaks the 2,950-3,110 zone towards the 61.8% retracement at 2,894. "
 "ALTERNATE, ABOUT 30% (RE-LABELLED THIS RUN): a larger irregular correction completes in the 2,977-3,061 area as a double bottom, after which a new advance targets 3,261 and 3,488; it is only promoted by a weekly close back above 3,261. "
 "INVALIDATION OF THE PREFERRED COUNT: a weekly close above 3,261. CONFIDENCE IS MODERATE. This is technical context, not advice.")
lt['proj']={"bull":[[0.66,3070.0],[0.78,3260],[0.9,3420],[1.0,3560]],"base":[[0.66,3070.0],[0.78,3000],[0.9,3060],[1.0,3140]],"bear":[[0.66,3070.0],[0.8,2940],[1.0,2890]]}

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-08', ph['rows'][-1]
ph['rows'][-1]=['2026-10-09',cash,m3,stk]
ph['updated']=RD
ph['basis']=("London Metal Exchange official settlements via Westmetall. LME Aluminium official cash settlement, official 3-month, and LME warehouse stock. Weekly sampling (last published official session of each week). AT THE 10-OCTOBER-2026 UPDATE the row for the week of 05-October is FINAL at the Friday 09-October session (cash 3,055.50, 3-month 3,070.00, stock 238,875 t); a new row for the week of 12-October will be appended once Monday's official prints. Verified against both cache-busted Westmetall language overviews and the per-metal aluminium daily table.")
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)

pdv=d['premium_drivers'][0]
pdv['d']=pdv['d'].replace("an $8.50 contango on 08-October, narrowing.","a $14.50 contango on 09-October, widened from $8.50.")
assert "$14.50 contango on 09-October" in pdv['d']

json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok', d['metals_board'], mh['al'][-1], mh['zn'][-1], mh['pb'][-1], round(tl,2), round(share,1), round(ratio,2))
