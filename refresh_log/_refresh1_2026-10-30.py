# Daily data refresh - 2026-10-30 (FRIDAY, ~02:45 UTC, BEFORE the ring). Board ROLLED to THURSDAY 29-Oct LME official (latest published session).
# Westmetall cache-busted EN and DE overviews both fetched and agree on the full 29-Oct session; Al per-metal table top row = 29-Oct (no later row).
# Completeness: 5/5 stock lines reconcile vs 28-Oct board; prior FX column (MTLE 1.11350) matches 28-Oct board.
# Key: Al cash 3,071.00 (-30.00), 3M 3,064.00 (-20.00) -> back BELOW 3,077 one session after clearing it, still above 3,061.5; BACKWARDATION NARROWED to $7.00 (below the $15 trigger) - spread and price moved in the SAME direction (both weaker).
# TE 30-Oct: Brent ~112.36-112.89 (page inconsistent), TTF 99.85 (+1.97%), DXY 101.74, UST10Y 4.916%; US Q3 GDP 3.4%, Sept PCE 3.6%/core 3.1%, ~83% Dec hike odds.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-30'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (29/30-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (30-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield, Dec hike pricing (30-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index, Q3 GDP and September PCE (30-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (30-Oct-2026)"
S_ST="https://straits.live/briefs/2026-10-30"; L_ST="Straits Daily Brief - Strait of Hormuz, 30-Oct-2026"
S_SMM="https://news.metal.com/"; L_SMM="SMM news feed - China three-region aluminium ingot inventory flat at 409,000 t; morning minutes on resurfacing rate-hike expectations (30-Oct-2026)"
S_VD="https://www.alcircle.com/news/vedanta-q2-fy27-profit-jumps-to-62-02b-aluminium-ebitda-soars-83-with-record-649kt-output-121749"; L_VD="AL Circle - Vedanta Q2 FY27 profit jumps to INR 62.02bn; aluminium EBITDA +83% with record 649kt output (29-Oct-2026)"
S_CS="https://www.alcircle.com/news/constellium-raises-2026-guidance-as-q3-adjusted-ebitda-hits-276m-revenue-jumps-22-121751"; L_CS="AL Circle - Constellium raises 2026 guidance as Q3 adjusted EBITDA hits $276m (29-Oct-2026)"
S_NS="https://www.alcircle.com/news/alumina-prices-fall-22-to-321-t-nanshan-flags-a-volatile-2026-market-121757"; L_NS="AL Circle - Alumina prices fall 22% to $321/t (9M-2026 average): Nanshan flags a volatile market (29-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
assert B['LME Cash settlement']['cur']==3101.0 and B['LME 3-month']['cur']==3084.0
cash,prev_c,m3,prev_m,stk,prev_s=3071.0,3101.0,3064.0,3084.0,231675,231900
spr=cash-m3; assert spr==7.0 and prev_s-225==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED FRIDAY 30-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING). THE BOARD IS THE THURSDAY 29-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION; Friday's official has not printed yet. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 29-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.11280); their prior-day FX column (MTLE 1.11350) matches the verified 28-October board, and the per-metal aluminium table's newest row is 29-October with NO later row; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 28-October (and match the pages' change column): aluminium 231,900 less 225 to 231,675; copper 271,450 plus 750 to 272,200; nickel 278,814 less 24 to 278,790; zinc 164,625 less 1,950 to 162,675; lead 312,675 less 1,150 to 311,525. "
 "The whole board sits on ONE UNIFORM SESSION (29-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(" CASH SETTLED $3,071.00 ON THE 29-OCTOBER OFFICIAL, DOWN $30.00 OR 0.97% FROM $3,101.00. THREE-MONTH SETTLED $3,064.00, DOWN $20.00 OR 0.65% FROM $3,084.00 - ending a three-session rise and falling BACK BELOW 3,077 one session after the first settled close above it, though still $2.50 ABOVE 3,061.5; $53.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%) and $69.50 above the 2,994.50 settled low of 15-October. "
 "THE BACKWARDATION NARROWED TO $7.00 FROM $17.00 because cash fell more than three-month - SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION (both weaker) - and it is BACK BELOW the published $15.00 reversal condition. "
 "VISIBLE LME STOCK FELL 225 t TO 231,675 t, another new series low and a seventh straight draw. The Trading Economics aluminium CFD reference was about $3,071.25 (-0.24%) on 29-October, in line with the official - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,071.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,064.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $13.00 BELOW THE 3,077 WEEKLY 50% RETRACEMENT (lost one session after clearing it), $2.50 above the 3,061.5 July low, $84.50 beneath the 3,148.5 wave (iv) high and $225.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a tenth session."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+7.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,071.00 against three-month $3,064.00 is a $7.00 BACKWARDATION, NARROWER than 28-October's $17.00 as cash fell $30.00 and three-month $20.00 - SPREAD AND PRICE MOVED TOGETHER (both weaker). It is BACK BELOW the published $15.00 reversal condition, one session after regaining it, though still an eleventh straight backwardation; a contango beyond $24.50 would reverse the structural signal. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"231,675","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 225 t TO 231,675 t, another new series low and a seventh straight draw. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,064.00, DOWN $20.00 - ending a three-session rise and back below 3,077 after one close above it, still $2.50 above 3,061.5 and $53.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 225 t TO 231,675 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":17.0,"avg":sep_sp,"note":VER+f" A $7.00 BACKWARDATION, NARROWER THAN 28-OCTOBER'S $17.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Cash fell $30.00 and three-month $20.00, so the structure softened WITH the flat price this session. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October at $14.00, regained 28-October at $17.00, LOST AGAIN 29-October at $7.00."},
 {"name":"EUR/USD LME fixing","cur":1.1128,"prev":1.1135,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.11280 FROM 1.11350 at the Thursday ring; the ECB fixing printed 1.11300 and BFIX 1.11312. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (29-Oct official)","price":"3,071.0","basis":"THE 29-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,071.00, DOWN $30.00 OR 0.97%. Next official Friday 30-October 13:20 London (also the weekly close)."},
 {"tenor":"3-month (29-Oct official)","price":"3,064.0","basis":"THE 29-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,064.00, DOWN $20.00 - back below 3,077 after one close above it, $2.50 above 3,061.5, $69.50 above the 2,994.50 October low and $53.50 above the 02-January official."},
 {"tenor":"Cash-to-3M structure","price":"+7.0 (BACKWARDATION)","basis":"A $7.00 BACKWARDATION, narrowed from $17.00 with price - back below the $15.00 reversal condition."},
 {"tenor":"Visible LME stock","price":"231,675 t","basis":f"DOWN 225 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE ONE-SESSION CONFIRMATION DID NOT HOLD. On the 29-October official cash $3,071.00 sits $7.00 ABOVE three-month $3,064.00, a BACKWARDATION, narrower than $17.00 on 28-October because cash fell $30.00 and three-month $20.00 - SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION (both weaker). "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00 and now $7.00. "
 f"READ: an eleventh straight backwardation with visible stock at another low (231,675 t), so prompt metal is still valued over forward metal, but the spread is back below the $15.00 trigger and the rally's confirmation lasted one session. The September mean spread was ${sep_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]
d['chart_stock_axis']=[220000,255000]

ls=d['lme_series']; assert ls[-1][0]=='28-Oct', ls[-1]
d['lme_series']=ls[1:]+[["29-Oct",cash,m3,stk]]
assert all(220000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14560.0,14350.0,14675.5,14484.0); NI=(15360.0,15550.0,15580.0,15750.0); ZN=(3980.0,3880.0,3960.0,3870.0); PB=(1878.0,1909.0,1910.0,1926.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average-to-date: 20 sessions to 28-Oct + 29-Oct = 21
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0,3736.0,3771.0,3727.0,3790.0,3900.0,3927.0,3960.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0,1851.0,1880.0,1872.0,1886.0,1900.0,1900.0,1910.0]
assert len(zs)==20 and len(ps)==20
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/21)/(sum(zs)/20),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/21)/(sum(ps)/20),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-29'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending THURSDAY 29-OCTOBER-2026 (Friday's official prints 13:20 London, after this run). THE WINDOW ROLLED THIS RUN: 08-October dropped and 29-October appended, so the window is 09-October to 29-October. Every point is an official cash settlement; the 29-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 28-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (29-October-2026 session; stock lines reconciled against 28-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,560.00, down $115.50 or 0.79%; three-month $14,350.00, down $134.00 or 0.93%. BACKWARDATION $210.00 from $191.50 - widening while price fell (spread and price in OPPOSITE directions), still the tightest prompt structure on the board. Stock ROSE 750 tonnes to 272,200 t, the only build on the board."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,360.00, down $220.00 or 1.41%; three-month $15,550.00, down $200.00 or 1.27%. CONTANGO widened to $190.00 from $170.00, still the widest carry on the board. Stock fell 24 tonnes to 278,790 t."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,980.00, up $20.00 or 0.51%; three-month $3,880.00, up $10.00 or 0.26% - the only riser on the board. BACKWARDATION widened to $100.00 from $90.00. Stock fell 1,950 tonnes to 162,675 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,878.00, down $32.00 or 1.68%; three-month $1,909.00, down $17.00 or 0.88%. CONTANGO widened to $31.00 from $16.00. Stock drew 1,150 tonnes to 311,525, a twenty-ninth consecutive draw."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Thursday 29-October official every metal except zinc fell: nickel three-month -1.27%, copper -0.93%, lead -0.88%, aluminium -0.65%, zinc +0.26%. Stocks fell for four metals; copper built 750 t. Trading Economics (30-October) reports US Q3 GDP at 3.4% annualised, September PCE inflation at 3.6% (core 3.1%) and roughly 83% odds of a December Fed hike priced, with the US ten-year near 4.92% and the dollar index near 101.7. The LME euro fixing fell to 1.1128.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='28-Oct'
        i['hist']=i['hist'][1:]+[["29-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,350.00 (3M); 14,560.00 (cash) $/t"
        i['ratio']="~14,560.00 $/t cash vs LME 3M 14,350.00 $/t"
        i['trend']='down'
        i['src']=("LME official cash settlement, rolled to the THURSDAY 29-OCTOBER-2026 session at $14,560.00, DOWN $115.50 or 0.79% against $14,675.50. THE WINDOW ROLLED THIS RUN: 08-October dropped and 29-October appended, so the series is the last fifteen published official cash sessions, 09-October to 29-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 28-October). "
                  "Copper structure for context: backwardation $210.00 (from $191.50), stock rose 750 t to 272,200 t.")
s=d['inputs_summary']; j=s.find("UPDATE 29-OCTOBER"); s=s[j:] if j>=0 else s
d['inputs_summary']=("UPDATE 30-OCTOBER: Copper rolled to the Thursday 29-October LME official cash of $14,560.00, down $115.50, with its fifteen-session window moved to 09-October to 29-October. No new monthly carbon settlement is due until mid-November, and no new dated SMM fluoride, silicon or magnesium mark was located, so no other hist mark was appended. "
 "Energy re-firmed: European gas EUR 99.85/MWh (+1.97%, up about 35% on the month) on 30-October with EU storage below 75% against a five-year average near 86%; Brent about $112.4-112.9 on Trading Economics (page internally inconsistent) and $115.50 on the Straits Daily Brief at 00:04 UTC. "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
otl=0.5*3101.0; ores=2403-otl; osh=otl/2403*100
OLDT=f"the tariff leg of the US duty-paid premium is 0.50 times the 28-October official cash of $3,101.00, or ${otl:,.2f}, UP $11.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${ores:,.2f}, so {osh:.1f}%"
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 29-October official cash of $3,071.00, or ${tl:,.2f}, DOWN $15.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED THURSDAY 29-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE WEDNESDAY 28-OCTOBER OFFICIAL)."; NEWC="COMPILED FRIDAY 30-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE THURSDAY 29-OCTOBER OFFICIAL)."
n=0; nc=0
for p in d['premiums']:
    n+=p['src'].count(OLDT); nc+=p['src'].count(OLDC); p['src']=p['src'].replace(OLDT,NEWT).replace(OLDC,NEWC)
print('premium tariff replaced',n,nc); assert n==len(d['premiums'])
ra=360.40/m3*100; na=0
o="THE RATIO: LME Alumina at $360.40/t against the 28-October aluminium three-month of $3,084.00 is 11.69%"
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    if o in s: na+=1
    a['src']=s.replace(o,f"THE RATIO: LME Alumina at $360.40/t against the 29-October aluminium three-month of $3,064.00 is {ra:.2f}%")
print('alumina',na,len(d['alumina'])); assert na==len(d['alumina'])

d['lme_commentary']=("3,077 LOST AFTER ONE SESSION. On the Thursday 29-October official cash settled $3,071.00 (-$30.00) and three-month $3,064.00 (-$20.00), ending a three-session rise and slipping back below 3,077 one session after the first settled close above it, though three-month held $2.50 above 3,061.5. "
 "Cash led the fall, so the backwardation narrowed to $7.00 from $17.00 - back below the $15.00 reversal condition, with spread and price both weaker; visible stock still fell 225 t to a new low of 231,675 t. The board turned lower outside zinc (nickel -1.3%, copper -0.9%, lead -0.9%, aluminium -0.65%, zinc +0.3%), and copper posted the only stock build. "
 "Macro turned less friendly for metals: Trading Economics (30-October) reports US Q3 GDP at 3.4% annualised against 3.1% expected and September PCE at 3.6% (core 3.1%), with markets pricing about 83% odds of a December hike; SMM's morning minutes say resurfacing rate-hike expectations are weighing on the rebound while destocking slows. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}. Friday's official is also the weekly close test against 3,077.")
d['net_read']=("NET: THE ONE-SESSION CONFIRMATION FADED. Against: three-month slipped back below 3,077 to $3,064.00, the backwardation narrowed below $15.00 to $7.00, strong US growth and sticky inflation revived December-hike pricing (about 83%, Trading Economics), China's three-region ingot inventory was flat at 409,000 t as destocking slowed (SMM), and ex-Middle East supply keeps improving (Chinese output near record, European restarts). "
 "Constructive: three-month held above 3,061.5 and the 2,994.50 low, the curve is still in backwardation for an eleventh session, visible LME stock fell to another low of 231,675 t, energy costs stay elevated (TTF near EUR 100) and Hormuz remains effectively closed, and producer results (Vedanta, Constellium) show demand and margins holding.")
d['bottom_line']=("BOTTOM LINE: on the Thursday 29-October LME official aluminium three-month fell $20.00 to $3,064.00 and cash $30.00 to $3,071.00 - back below 3,077 one session after clearing it - while the backwardation narrowed to $7.00, below the $15.00 tightness trigger, and visible stock still fell to a new low of 231,675 t. "
 "The pre-registered reversal condition (a settled close below 3,061.5 with the spread heading to contango) was NOT met, so scenario weights are held at 20% bull / 45% base / 35% bear, with the bull case on watch. The daily Elliott count keeps wave (v) of the C-wave decline complete at 2,994.50 (base case trimmed to about 60%); a settled close below 3,061.5 would weaken it and below about 2,977.5 would force a re-count; invalidation 3,289. The weekly corrective count toward 2,894 stays preferred; Friday's weekly close versus 3,077 is the next test.")
c2=d['commercial']
for a,b in [("FIRST, PRICE AND PROMPT PREMIUM FIRMED TOGETHER: a $17.00 backwardation on 28-October, wider than $14.00 as cash rose $23.00 and three-month $20.00 - back above the $15.00 reversal condition, so nearby metal is again valued more clearly over forward metal and there is no carry reward for deferring purchases; one session does not make a trend.",
             "FIRST, PRICE AND PROMPT PREMIUM EASED TOGETHER: a $7.00 backwardation on 29-October, narrower than $17.00 as cash fell $30.00 and three-month $20.00 - back below the $15.00 reversal condition one session after regaining it, so nearby metal is still valued over forward metal and there is still no carry reward for deferring purchases, but the prompt tightness signal has softened again."),
 (f"is ${otl:,.2f} on 28-October cash, {osh:.1f}% of the $2,403/t premium",f"is ${tl:,.2f} on 29-October cash, {share:.1f}% of the $2,403/t premium"),
 ("the 28-October official took three-month to $3,084.00, $89.50 above the 2,994.50 settled low and $7.00 above 3,077 (first close above it); energy eased from highs but stays elevated (Brent about $114.30; European gas EUR 98.22/MWh, 29-October); the Fed held at 3.75-4.00% on 28-October with two dissents for a hike;",
  "the 29-October official took three-month back to $3,064.00, $13.00 below 3,077 after one close above it and $2.50 above 3,061.5; energy stays elevated (European gas EUR 99.85/MWh, Brent about $112-116 depending on source, 30-October); after the Fed's 28-October hold, strong Q3 GDP (3.4%) and September PCE (3.6%) put December-hike odds near 83% (Trading Economics);")]:
    assert a in c2,a; c2=c2.replace(a,b)
d['commercial']=c2

pre_end="would reverse the shift. "
for s in d['outlook']['scenarios']:
    assert s['drivers'].startswith("MOVED 29-OCTOBER"); k=s['drivers'].find(pre_end); assert k>0
    s['drivers']=("HELD 30-OCTOBER at 20/45/35: the 29-October official gave back the 3,077 break (three-month $3,064.00, -$20.00) and the backwardation narrowed below the $15.00 trigger to $7.00, but the pre-registered reversal - a settled close below 3,061.5 with the spread heading to contango - was NOT met (three-month $2.50 above 3,061.5, still backwardated, stock at another low), so no weight moves; the bull case is on watch and a close below 3,061.5 would return five points to bear. ")+s['drivers'][k+len(pre_end):]
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium gave back its breakout: three-month fell $20 to $3,064 on Thursday's LME official, back below $3,077 one session after clearing it, and the backwardation narrowed to $7, below the $15 tightness trigger, as strong US data revived December-hike bets - though LME stock still fell to a new low.",
 "points":[
 "WHAT MOVED: Thursday's LME official settled cash at $3,071.00 (-$30.00) and three-month at $3,064.00 (-$20.00, -0.65%), ending a three-session rise. Cash now trades $7.00 above three-month (backwardation), down from $17.00, while LME stock fell 225 t to a new low of 231,675 t. Every LME base metal except zinc fell.",
 "WHY: US Q3 GDP grew 3.4% annualised and September PCE inflation was 3.6% (core 3.1%), so markets now price about 83% odds of a December Fed hike (Trading Economics); SMM says resurfacing hike expectations and slower Chinese destocking (three-region ingot inventory flat at 409,000 t) are capping the rebound.",
 "SUPPORT: three-month held above $3,061.5 and the curve stayed in backwardation; European gas rose back toward EUR 100/MWh and Hormuz remains effectively closed (Straits Daily Brief), keeping smelter energy costs high. Vedanta (record 649 kt quarterly output) and Constellium (guidance raised) reported solid quarters.",
 "WHAT TO WATCH: Friday's official, which is also the weekly close versus $3,077; whether three-month holds $3,061.5 (a close below it with the spread heading to contango would reverse this week's bullish shift); Chalco's Q3 report, not yet located."]}

d['feed']=([
 {"when":"Fri 30-Oct","impact":"Bearish","text":"BOARD ROLLED TO THE THURSDAY 29-OCTOBER LME OFFICIAL: cash $3,071.00 (-$30.00), three-month $3,064.00 (-$20.00), back below 3,077 after one close above it; stock -225 t to a new low of 231,675 t."},
 {"when":"Fri 30-Oct","impact":"Bearish","text":"STRUCTURE SOFTER: the cash-to-three-month backwardation narrowed to $7.00 from $17.00, back below the $15.00 reversal condition - spread and price both weaker."},
 {"when":"Fri 30-Oct","impact":"Bearish","text":"US DATA REVIVE HIKE BETS: Q3 GDP 3.4% annualised, September PCE 3.6% (core 3.1%); about 83% odds of a December hike priced; US ten-year about 4.92%, dollar index about 101.7 (Trading Economics)."},
 {"when":"Fri 30-Oct","impact":"Mixed","text":"SMM: China three-region aluminium ingot inventory flat at 409,000 t on 30-October; destocking slowed mid-week."},
 {"when":"Thu 29-Oct","impact":"Bullish","text":"PEER EARNINGS: Vedanta Q2 FY27 aluminium EBITDA INR 101.92bn (+83% y/y) on record 649 kt output; Constellium Q3 adjusted EBITDA $276m (+17%), 2026 guidance raised (AL Circle)."},
 {"when":"Fri 30-Oct","impact":"Mixed","text":"ENERGY / HORMUZ: TTF EUR 99.85/MWh (+1.97%) (Trading Economics); Straits Daily Brief - strait still effectively closed; IRGC claim of tankers striking mines unconfirmed by any maritime authority; Brent $115.50 at 00:04 UTC."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM GIVES BACK 3,077. The Thursday 29-October official settled cash at $3,071.00 (-0.97%) and three-month at $3,064.00 (-0.65%), ending a three-session rise one session after the first settled close above 3,077; three-month held $2.50 above 3,061.5. Visible stock still fell 225 t to a new low of 231,675 t. The board fell outside zinc: nickel three-month -1.27%, copper -0.93%, lead -0.88%, zinc +0.26%; copper posted the only stock build (+750 t)."},
 {"theme":"LME","horizon":"0-1 month","impact":"Bearish","url":W,
  "headline":"THE CURVE SOFTENED WITH PRICE: the cash-to-three-month backwardation narrowed to $7.00 from $17.00 on 29-October, back below the $15.00 reversal condition one session after regaining it, because cash fell more than three-month. READ: still an eleventh straight backwardation, but the joint price-and-structure confirmation of 28-October lasted one session."},
 {"theme":"Macro","horizon":"0-2 months","impact":"Bearish","url":S_TY,
  "headline":"US DATA REVIVE DECEMBER-HIKE PRICING (Trading Economics, 30-October): Q3 GDP grew at a 3.4% annualised rate against 3.1% expected; September PCE inflation rose to 3.6% with core at 3.1%; initial jobless claims fell to 194,000. Traders price nearly 83% odds of a 25bp December hike after the Fed's 28-October hold. The US ten-year eased to about 4.92% and the dollar index to about 101.7. SMM's morning minutes (30-October) say resurfacing rate-hike expectations are pressuring the aluminium rebound."},
 {"theme":"China","horizon":"Immediate","impact":"Mixed","url":S_SMM,
  "headline":"CHINA INGOT INVENTORY FLAT (SMM, 30-October): three-region social aluminium ingot inventory was 409,000 t, unchanged day on day, with Gongyi down to 118,000 t and Guangdong (116,500 t) and Wuxi (174,500 t) up; SMM says inventories are still falling overall but destocking slowed mid-week and expects prices to consolidate short term."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Bullish","url":S_VD,
  "headline":"VEDANTA Q2 FY27 (AL Circle, 29-October): group revenue INR 258.12bn (+57% y/y), EBITDA INR 99.38bn (+106%), PAT INR 62.02bn (+151%); Vedanta Aluminium EBITDA INR 101.92bn (+83% from INR 55.82bn) at a 46% margin, on record quarterly aluminium output of 649 kt (+5% y/y, +3% q/q) and alumina 895 kt (+37%)."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Bullish","url":S_CS,
  "headline":"CONSTELLIUM RAISES 2026 GUIDANCE (AL Circle, 29-October; reported 28-October): Q3-2026 revenue $2.64bn (from $2.17bn), adjusted EBITDA $276m (from $235m), net income $119m (from $88m) on shipments of 368 kt, slightly lower y/y; 2026 adjusted EBITDA guidance now $1.03-1.06bn excluding metal price lag, free cash flow above $300m."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Mixed","url":S_ST,
  "headline":"ENERGY RE-FIRMS (Trading Economics / Straits Daily Brief, 30-October): TTF rose to about EUR 99.85/MWh (+1.97%, up about 35% on the month) on colder forecasts and EU storage below 75%; Brent near four-year highs on concern US strikes on Iran could resume ($115.50 at 00:04 UTC per the Straits brief). Hormuz is still effectively closed (IMF PortWatch: 2 transits on 25-October vs an 85/day baseline); an IRGC claim that tankers struck mines is unconfirmed by any maritime authority. READ: smelter energy costs stay elevated."},
 {"theme":"Alumina","horizon":"0-6 months","impact":"Bearish","url":S_NS,
  "headline":"ALUMINA PRICES DOWN 22% Y/Y (AL Circle, 29-October, citing Nanshan's unaudited nine-month disclosure): overseas alumina prices averaged around $321/t in January-September 2026, about 22% below a year earlier, low in H1 and recovering in Q3 on new overseas smelting capacity and some refinery constraints."},
]+d['news']
d['news']=d['news'][:20]

hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Thu 29-Oct':
        hitc+=1
        cat['date']='Daily, from Fri 30-Oct'
        cat['event']="3,077 CLEARED ON 28-OCTOBER ($3,084.00) AND LOST ON 29-OCTOBER ($3,064.00); THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE, RETESTED IT ON 20-OCTOBER ($2,997.00), AND HAS SINCE SETTLED $3,024.50, $3,008.00, $3,018.00, $3,027.00, $3,064.00, $3,084.00 AND $3,064.00. A renewed settled close above 3,077 would restore the confirmation that wave (v) is complete; next resistance 3,110 then the 3,148.5 wave (iv) high - above 3,148.5 the C wave is complete and above 3,183 the impulsive labelling void. A settled close beneath 3,061.5 would weaken the rebound and return five scenario points to bear, and beneath about 2,977.5 would force a re-count toward the 2,894 weekly 61.8%. Invalidation 3,289. STRUCTURE: the $15.00 backwardation reversal condition was lost again on 29-October at $7.00. WEEKLY TEST: Friday 30-October close versus 3,077 (week opened from a 3,018.00 weekly close)."
assert hitc==1,hitc
d['outlook']['catalysts'].insert(0,{"date":"Fri 30-Oct (pending)","event":"CHALCO Q3-2026 RESULTS - PENDING: Chalco normally publishes its third-quarter report in late October; a search this run did not locate a Q3-2026 release (results found were Q3-2025). Hydro and Alcoa Q3 prints both showed smelting margin intact and alumina margin compressed; Chalco, the world's largest alumina producer, is the next test of that split. Broker estimates are not published as results.","impact":"Medium"})
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 30-OCTOBER: the 29-October official printed a $7.00 BACKWARDATION, back BELOW the $15.00 reversal condition one session after regaining it, as cash fell more than three-month; stock still fell to a new low. Trend moved from DOWN to FLAT: contango is still $7.00 away, but the prompt-tightness cushion thinned."
RK[0]['trend']='flat'
RK[4]['risk']+=" UPDATE 30-OCTOBER: LME stock fell 225 t to a new series low of 231,675 t on 29-October, a seventh straight draw; SMM's three-region Chinese ingot inventory was flat at 409,000 t on 30-October with destocking slowing mid-week. Trend held at FLAT."
RK[4]['trend']='flat'
hit=0
for r in RK:
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 30-OCTOBER: TTF rose back to EUR 99.85/MWh (+1.97%) on colder forecasts with EU storage below 75%; Brent near four-year highs on US-Iran strike concern (Trading Economics; Straits brief $115.50). Trend held at UP."; hit+=1
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 30-OCTOBER: Straits Daily Brief - strait still effectively closed (IMF PortWatch: 2 transits on 25-October vs an 85/day baseline; 265 dry-bulk vessels waiting in the Gulf and Gulf of Oman on 28-October per Hellenic Shipping News); an IRGC claim that tankers struck mines and a single-source tanker-explosion report are UNCONFIRMED by any maritime authority. Trend held at UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 30-OCTOBER: RE-RAISED - US Q3 GDP 3.4% annualised (3.1% expected), September PCE 3.6% with core 3.1%, and jobless claims at 194,000 lifted December-hike odds to about 83% (Trading Economics, 30-October); SMM cites resurfacing hike expectations as a drag on aluminium. Trend moved from FLAT back to UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('THE EX-CHINA RESTART PIPELINE'):
        r['risk']+=" UPDATE 30-OCTOBER: Vedanta reported record quarterly aluminium output of 649 kt in Q2 FY27 (AL Circle, 29-October); Trading Economics still notes Chinese output near record and Gulf smelters gradually recovering. Trend held at UP."; hit+=1; r['trend']='up'
assert hit==4,hit
d['outlook']['ai_analysis'].insert(0,"FRIDAY 30-OCTOBER ON THE THURSDAY 29-OCTOBER OFFICIAL: three-month fell $20.00 to $3,064.00 and cash $30.00 to $3,071.00 - back below 3,077 one session after clearing it - and the backwardation narrowed to $7.00, below the $15.00 reversal condition, though visible stock fell to another low (231,675 t). The pre-registered reversal (a close below 3,061.5 with the spread heading to contango) was not met, so weights are held at 20/45/35 with the bull case on watch. Strong US Q3 GDP and sticky PCE revived December-hike pricing (about 83%), the most direct headwind this week; Friday's official is also the weekly close test against 3,077.")

EWS=("REVIEWED 30-OCTOBER ON THE THURSDAY 29-OCTOBER OFFICIAL: three-month settled $3,064.00, down $20.00 - a tenth settled close above the 2,994.50 low of 15-October but BACK BELOW 3,077 one session after the first close above it, and still $2.50 above 3,061.5. The sequence 2,994.50 / 3,024.50 / 3,008.00 / 3,018.00 / 3,027.00 / 3,064.00 / 3,084.00 / 3,064.00 reads as the first leg of a corrective rebound from a completed wave (v) of C now pulling back; 3,084.00 is NOT yet a confirmed pivot. Wave (v) ($154.00 from the 3,148.5 wave (iv) high to 2,994.50) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged, NOT re-labelled; base case trimmed to about 60%: wave (v) ended at 2,994.50 and, after this pullback holds above 3,061.5-3,024.5, the rebound extends toward 3,110 then the 3,148.5 wave (iv) area; alternate about 40%: the failure at 3,084 is the end of a minor corrective bounce, a settled close beneath 3,061.5 reopens the low, and a close beneath 2,977.5 forces a re-count toward 2,894. Invalidation 3,289; confidence moderate-to-low. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED 24-OCTOBER"); assert st.startswith("REVIEWED 29-OCTOBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED 24-OCTOBER"); assert lt.startswith("REVIEWED 29-OCTOBER") and k>0
d['ew']['long_term']['writeup']="REVIEWED 30-OCTOBER (THURSDAY 29-OCTOBER OFFICIAL, WEEK IN PROGRESS): three-month at 3,064.00, up $46.00 from the 3,018.00 weekly close but $13.00 BELOW the 3,077 50% retracement after one session above it, in the middle of the 2,950-3,110 zone; Friday 30-October's official is the weekly close - a close above 3,077 would be the first sign the larger correction is ending early, a close below it keeps the corrective count towards the 61.8% retracement at 2,894 preferred - no re-label. "+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="112.4",day="about $112.36-112.89 on 30-October, +1.4-1.9% on the day (Trading Economics, page internally inconsistent; likely a contract roll versus 29-October's 114.30); Straits Daily Brief $115.50 at 00:04 UTC",
 note="REFRESHED FRIDAY 30-OCTOBER-2026 (Trading Economics): Brent is approaching four-year highs on concern that US strikes on Iran could resume (Trump has warned strikes could restart after the midterms), intensified Saudi-Houthi clashes and continued threats to Hormuz shipping, partly offset by a US diplomatic letter on restarting talks and regional crude exports near pre-war levels. The quoted level differs between the page's table (112.36) and stats (112.89), so it is approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="99.9",day="EUR 99.85/MWh on 30-October, +1.97% (Trading Economics); up about 35% on the month",
 note="REFRESHED FRIDAY 30-OCTOBER-2026 (Trading Economics): TTF rose back toward EUR 100/MWh on rising heating demand and colder forecasts for north-west Europe; EU storage was below 75% on 28-October against a five-year average near 86% (Germany 61.65%, Netherlands 65.53%); Hormuz disruption has halted several LNG sources, mainly Qatar. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.74",day="about 101.74 on 30-October, -0.13% (Trading Economics)",
 note="REFRESHED FRIDAY 30-OCTOBER-2026 (Trading Economics): the dollar eased despite US Q3 GDP of 3.4% annualised (3.1% expected) and September PCE inflation of 3.6% (core 3.1%); jobless claims fell to 194,000; markets watch for a December Fed move. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="4.92",day="about 4.92% on 30-October, -2bp (Trading Economics)",
 note="REFRESHED FRIDAY 30-OCTOBER-2026 (Trading Economics): the yield held just under 5%; traders price nearly 83% odds of a 25bp December hike after strong Q3 GDP and core PCE at 3.1%. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.11280',day="LME fixing on 29-October, down from 1.11350; ECB fixing 1.11300, BFIX 1.11312",
 note="REFRESHED FRIDAY 30-OCTOBER-2026 to the 29-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE THURSDAY 29-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION. This Friday 30-October run is compiled about 02:45 London, BEFORE the ring, so Friday's official (13:20 London) - which is also the weekly close - has not printed. The Trading Economics aluminium CFD reference (about $3,071.25, -0.24% on 29-October) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (30-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 29-October session, and the per-metal aluminium daily table's newest row is 29-October (cash 3,071.00, three-month 3,064.00, stock 231,675) with NO later row, so the board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.11350) matches the 28-October board verified on 29-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 28-October, and match the pages' change column: aluminium -225 to 231,675; copper +750 to 272,200; nickel -24 to 278,790; zinc -1,950 to 162,675; lead -1,150 to 311,525.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (29-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (twenty-one sessions, 01- to 29-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,064.00; the stock chart axis floor of 220,000 t leaves about 11,675 t of headroom below visible stock at 231,675 t and will be re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,071.00 against three-month $3,064.00 is therefore a $7.00 BACKWARDATION, narrower than $17.00 on 28-October - the spread and the flat price moved in the same direction (both weaker) this session. In copper the backwardation WIDENED to $210.00 while price fell - spread and price in opposite directions."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 29-October official cash of $3,071.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $112.4), the dollar index (about 101.74), TTF (EUR 99.85/MWh) and the US ten-year (about 4.92%) are Trading Economics readings shown on 30-October; Trading Economics prices are contract-for-difference references, not official benchmarks. Its Brent page was internally inconsistent this run (table 112.36 vs stats 112.89, and a level below 29-October's 114.30 despite a quoted daily gain - likely a front-month roll), and the Straits Daily Brief shows $115.50 at 00:04 UTC, so the Brent level is approximate and the day-on-day change is not comparable. EUR/USD is the 29-October LME fixing, the same session as the board."; hit+=1
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 30-OCTOBER: no authorised fetch was blocked (Westmetall EN, DE and per-metal pages, Trading Economics, AL Circle, news.metal.com and the Straits Daily Brief all fetched). Two individual SMM article pages returned HTTP 404, so the 409,000 t Chinese ingot inventory figure and the morning-minutes read are cited from the news.metal.com feed summaries (30-October). Hormuz items flagged by the Straits brief as unconfirmed or single-source are cited as such, not as fact. No Q1-2027 Japanese premium offer has been reported yet (negotiations normally start late November)."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: TWO NEW RESULTS ADDED THIS RUN - Vedanta Q2 FY27 and Constellium Q3-2026 (both via AL Circle, 29-October). Constellium's per-company history was rolled to Q3-26 ($276m adjusted EBITDA; Q3-25 $235m confirms the same basis). Vedanta's history was NOT extended: the INR 101.92bn aluminium EBITDA is reported on a Vedanta Aluminium basis that could not be confirmed as identical to the series' existing basis (public sources disagree on the Q1 FY27 segment figure), so the gap is left rather than mixing bases. NO NEW COMPANY WAS BACK-FILLED THIS RUN. Chalco's Q3-2026 report was searched for again and not located. Other entries are carried at their last publicly verified figures."; hit+=1
assert hit==4,hit
en=d['earnings_note']; j=en.find("NORSK HYDRO REPORTED Q3-2026"); assert j>=0
d['earnings_note']=("VEDANTA AND CONSTELLIUM REPORTED THIS WEEK (added 30-October): Vedanta's Q2 FY27 aluminium EBITDA rose 83% y/y to INR 101.92bn at a 46% margin on record 649 kt output; Constellium's Q3-2026 adjusted EBITDA rose to $276m from $235m and it raised 2026 guidance to $1.03-1.06bn. Constellium's history was rolled to Q3-26; Vedanta's was not extended because the reporting basis could not be matched. Chalco's Q3 is still pending. "+en[j:].replace("(added 24-October; no newer peer result to 29-October):","(added 24-October):",1))
eh=d['earnings_history']['CSTM']; assert eh['points'][-1][0]=='Q2-26' and eh['points'][0]==['Q3-25',235]
eh['points']=eh['points'][1:]+[['Q3-26',276]]
eh['src']=["Constellium releases (Q4-25 to Q2-26); AL Circle - Constellium Q3-2026 adjusted EBITDA $276m (29-Oct-2026)",S_CS]
d['earnings'].insert(0,{"company":"Constellium (CSTM)","group":"Downstream / rolled and extruded products","period":"Q3 2026","reported":"28 Oct 2026","reported_iso":"2026-10-28","sentiment":"Positive",
 "headline":"Q3-2026: revenue $2.64bn (from $2.17bn, about +22%); adjusted EBITDA $276m (from $235m, about +17%); net income $119m (from $88m); shipments 368 kt, slightly lower y/y. 2026 guidance RAISED to adjusted EBITDA of $1.03-1.06bn excluding non-cash metal price lag and free cash flow above $300m. Metal price lag was unfavourable in Q3 (amount not disclosed in the source).",
 "readthrough":"CONVERSION MARGIN IS HOLDING ON LOWER VOLUME: revenue rose faster than EBITDA because metal prices pass through, while shipments edged lower - so the guidance raise reflects pricing and cost rather than volume. The fall from Q2's $439m to $276m is largely the reversal of metal-price-lag gains, which is why guidance is stated excluding lag. Generic read for primary metal: downstream demand is stable, not accelerating.",
 "eps":None,"revenue_bn":2.64,"yoy_pct":17.0,"url":S_CS})
d['earnings'].insert(0,{"company":"Vedanta Aluminium (VEDL)","group":"Aluminum producer (India)","period":"Q2 FY27 (Jul-Sep 2026)","reported":"29 Oct 2026","reported_iso":"2026-10-29","sentiment":"Positive",
 "headline":"Q2 FY27: Vedanta group revenue INR 258.12bn (+57% y/y), EBITDA INR 99.38bn (+106%), PAT INR 62.02bn (+151%), net debt/EBITDA 0.1x. Vedanta Aluminium: revenue INR 220.66bn (+41%), EBITDA INR 101.92bn (+83% from INR 55.82bn) at a 46% margin (36% a year earlier), adjusted PAT INR 51.67bn (+118%); record quarterly aluminium output 649 kt (+5% y/y, +3% q/q), value-added 432 kt (+31%), alumina 895 kt (+37%).",
 "readthrough":"AN INTEGRATED, LOW-COST PRODUCER IS STILL CONVERTING THE 2026 PRICE STRUCTURE INTO RECORD MARGIN: a 46% aluminium EBITDA margin on record volume, with alumina self-supply rising 37%. Read-through: unlike Hydro's and Alcoa's alumina legs, integrated producers that consume their own alumina capture the low alumina price as a cost benefit. (The source's group-margin figure appears internally inconsistent and is not used.)",
 "eps":None,"revenue_bn":None,"yoy_pct":83.0,"url":S_VD})

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 29-OCTOBER: no newer public disclosure","REVIEWED 30-OCTOBER: no newer public disclosure").replace("REVIEWED 29-OCTOBER. NO NEW DATED","REVIEWED 30-OCTOBER. NO NEW DATED")
    return o
PS={p['name']:p for p in d['producer_status']}
c=PS['China operators (aggregate, incl. Chalco and Hongqiao)']
c['update']="UPDATED 30-OCTOBER (SMM feed, 30-October): three-region social aluminium ingot inventory flat at 409,000 t, destocking slowing mid-week; Trading Economics still describes Chinese output near record despite the capacity cap; Chalco's Q3-2026 report not yet located. "+c['update']
c['src']=[L_SMM,S_SMM]
c=PS['EGA (Al Taweelah)']
c['update']="REVIEWED 30-OCTOBER: no newer EGA release than 21-October (half of Al Taweelah's cells restarted); Trading Economics' summary still cites a quarter of cells online with full recovery expected by Q1-2027 - the older figure, so the company release is kept. "+c['update']
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD
for s_ in [[L_TE,S_TE],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG],[L_ST,S_ST],[L_SMM,S_SMM],[L_VD,S_VD],[L_CS,S_CS],[L_NS,S_NS]]:
    d['sources'].append(s_)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 29-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 28-Oct)",W])
for x in ([L_TY,S_TY],[L_ST,S_ST],[L_SMM,S_SMM],[L_VD,S_VD]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-28'
ph['rows'][-1]=['2026-10-29',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
