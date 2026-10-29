# Daily data refresh - 2026-10-29 (THURSDAY, ~02:40 UTC, BEFORE the ring). Board ROLLED to WEDNESDAY 28-Oct LME official (latest published session).
# Westmetall cache-busted EN and DE overviews both fetched and agree on the full 28-Oct session; Al per-metal table top row = 28-Oct (no later row).
# Completeness: 5/5 stock lines reconcile vs 27-Oct board; prior FX column (MTLE 1.11520) matches 27-Oct board.
# Key: Al cash 3,101.00 (+23.00), 3M 3,084.00 (+20.00) -> FIRST settled 3M close above 3,077 (weekly 50% retracement) = stated confirmation of daily wave (v) complete; BACKWARDATION WIDENED to $17.00 (back above the $15 trigger) - spread and price moved in the SAME direction.
# Fed 28-Oct: HOLD at 3.75-4.00%, 10-2 vote (Cook, Hammack dissent for a hike), no clear December signal (TE). TE 29-Oct: Brent ~114.30 (-0.89%), TTF 98.22 (-2.11%), DXY 102.09, UST10Y ~4.99%. TE aluminium CFD 3,078.50 (-0.69%) on 28-Oct after the official.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-29'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (28/29-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (29-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (29-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index, Fed decision (29-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (29-Oct-2026)"
S_ST="https://straits.live/briefs/2026-10-29"; L_ST="Straits Daily Brief - Strait of Hormuz, 29-Oct-2026"
S_EU="https://www.alcircle.com/news/europes-9m-2026-aluminium-production-jumps-to-5-56mt-as-smelter-restarts-gain-ground-121723"; L_EU="AL Circle - Europe's 9M-2026 aluminium production jumps to 5.56Mt as smelter restarts gain ground (28-Oct-2026)"
S_HY="https://www.alcircle.com/news/hydro-invests-53-5m-in-5-900mt-aluminum-extrusion-press-in-pennsylvania-121737"; L_HY="AL Circle - Hydro invests $53.5m in 5,900t extrusion press in Pennsylvania (28-Oct-2026)"
S_CE="https://www.alcircle.com/news/chalieco-wins-833m-bid-for-2-4-million-tonne-vietnam-alumina-project-121734"; L_CE="AL Circle - CHALIECO wins $833m bid for 2.4Mt Vietnam alumina project (28-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
assert B['LME Cash settlement']['cur']==3078.0 and B['LME 3-month']['cur']==3064.0
cash,prev_c,m3,prev_m,stk,prev_s=3101.0,3078.0,3084.0,3064.0,231900,232100
spr=cash-m3; assert spr==17.0 and prev_s-200==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED THURSDAY 29-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING). THE BOARD IS THE WEDNESDAY 28-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION; Thursday's official has not printed yet. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 28-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.11350); their prior-day FX column (MTLE 1.11520) matches the verified 27-October board, and the per-metal aluminium table's newest row is 28-October with NO later row; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 27-October (and match the pages' change column): aluminium 232,100 less 200 to 231,900; copper 272,725 less 1,275 to 271,450; nickel 280,218 less 1,404 to 278,814; zinc 165,650 less 1,025 to 164,625; lead 314,675 less 2,000 to 312,675. "
 "The whole board sits on ONE UNIFORM SESSION (28-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(" CASH SETTLED $3,101.00 ON THE 28-OCTOBER OFFICIAL, UP $23.00 OR 0.75% FROM $3,078.00. THREE-MONTH SETTLED $3,084.00, UP $20.00 OR 0.65% FROM $3,064.00 - a third straight rise, the highest settled three-month since 09-October, $73.50 ABOVE the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%), $89.50 above the 2,994.50 settled low of 15-October and THE FIRST SETTLED CLOSE ABOVE 3,077 (by $7.00), the level this page set as confirmation of the rebound. "
 "THE BACKWARDATION WIDENED TO $17.00 FROM $14.00 because cash rose more than three-month - SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION this session, ending two sessions of divergence - and it is BACK ABOVE the published $15.00 reversal condition. "
 "VISIBLE LME STOCK FELL 200 t TO 231,900 t, another new series low and a sixth straight draw. AFTER THE OFFICIAL the Trading Economics aluminium CFD reference slipped to about $3,078.50 (-0.69% on 28-October) - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,101.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,084.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $7.00 ABOVE THE 3,077 WEEKLY 50% RETRACEMENT (first settled close above it), $22.50 above the 3,061.5 July low, $64.50 beneath the 3,148.5 wave (iv) high and $205.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a ninth session."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+17.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,101.00 against three-month $3,084.00 is a $17.00 BACKWARDATION, WIDER than 27-October's $14.00 as cash rose $23.00 and three-month $20.00 - SPREAD AND PRICE MOVED TOGETHER this session after two sessions in opposite directions. It is BACK ABOVE the published $15.00 reversal condition, one session after slipping below it; a contango beyond $24.50 would reverse the structural signal. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"231,900","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 200 t TO 231,900 t, another new series low and a sixth straight draw, though the smallest of the run. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,084.00, UP $20.00 - a third straight rise, the highest settled three-month since 09-October and the FIRST settled close above 3,077, $73.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 200 t TO 231,900 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":14.0,"avg":sep_sp,"note":VER+f" A $17.00 BACKWARDATION, WIDER THAN 27-OCTOBER'S $14.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Cash rose $23.00 and three-month $20.00, so the structure firmed WITH the flat price this session. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost on 27-October at $14.00, REGAINED on 28-October at $17.00."},
 {"name":"EUR/USD LME fixing","cur":1.1135,"prev":1.1152,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.11350 FROM 1.11520 at the Wednesday ring; the ECB fixing printed 1.11330 and BFIX 1.11349. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (28-Oct official)","price":"3,101.0","basis":"THE 28-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,101.00, UP $23.00 OR 0.75%. Next official Thursday 29-October 13:20 London."},
 {"tenor":"3-month (28-Oct official)","price":"3,084.0","basis":"THE 28-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,084.00, UP $20.00 - the highest since 09-October and the first settled close above 3,077 (by $7.00), $89.50 above the 2,994.50 October low and $73.50 above the 02-January official."},
 {"tenor":"Cash-to-3M structure","price":"+17.0 (BACKWARDATION)","basis":"A $17.00 BACKWARDATION, widened from $14.00 with price - back above the $15.00 reversal condition."},
 {"tenor":"Visible LME stock","price":"231,900 t","basis":f"DOWN 200 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("PRICE AND CURVE CONFIRMED TOGETHER. On the 28-October official cash $3,101.00 sits $17.00 ABOVE three-month $3,084.00, a BACKWARDATION, wider than $14.00 on 27-October because cash rose $23.00 and three-month $20.00 - SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION, ending two sessions of divergence. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00 and now $17.00. "
 f"READ: a tenth straight backwardation, back above the published $15.00 reversal condition, with visible stock at another low (231,900 t) - the prompt-led firming the rally lacked on 26- and 27-October. One session is not a trend; the September mean spread was ${sep_sp:,.2f} and a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]
d['chart_stock_axis']=[220000,255000]

ls=d['lme_series']; assert ls[-1][0]=='27-Oct', ls[-1]
d['lme_series']=ls[1:]+[["28-Oct",cash,m3,stk]]
assert all(220000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
# (cash, 3M, prev cash, prev 3M)
CU=(14675.5,14484.0,14625.0,14435.0); NI=(15580.0,15750.0,15440.0,15650.0); ZN=(3960.0,3870.0,3927.0,3830.0); PB=(1910.0,1926.0,1900.0,1920.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average-to-date: 19 sessions to 27-Oct + 28-Oct = 20
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0,3736.0,3771.0,3727.0,3790.0,3900.0,3927.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0,1851.0,1880.0,1872.0,1886.0,1900.0,1900.0]
assert len(zs)==19 and len(ps)==19
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/20)/(sum(zs)/19),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/20)/(sum(ps)/19),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-28'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending WEDNESDAY 28-OCTOBER-2026 (Thursday's official prints 13:20 London, after this run). THE WINDOW ROLLED THIS RUN: 07-October dropped and 28-October appended, so the window is 08-October to 28-October. Every point is an official cash settlement; the 28-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 27-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (28-October-2026 session; stock lines reconciled against 27-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,675.50, up $50.50 or 0.35%; three-month $14,484.00, up $49.00 or 0.34%. BACKWARDATION $191.50 from $190.00 - still the tightest prompt structure on the board. Stock fell 1,275 tonnes to 271,450 t."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,580.00, up $140.00 or 0.91%; three-month $15,750.00, up $100.00 or 0.64% - snapping a three-session fall. CONTANGO narrowed to $170.00 from $210.00, still the widest carry on the board. Stock fell 1,404 tonnes to 278,814 t."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,960.00, up $33.00 or 0.84%; three-month $3,870.00, up $40.00 or 1.04%. BACKWARDATION narrowed to $90.00 from $97.00. Stock fell 1,025 tonnes to 164,625 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,910.00, up $10.00 or 0.53%; three-month $1,926.00, up $6.00 or 0.31%. CONTANGO $16.00 from $20.00. Stock drew 2,000 tonnes to 312,675, a twenty-eighth consecutive draw."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Wednesday 28-October official every metal on the board rose: zinc three-month +1.04% led, aluminium +0.65%, nickel +0.64%, copper +0.34% and lead +0.31%. Stocks fell for all five metals. The Fed held rates at 3.75-4.00% that evening (10-2, two dissents for a hike) and Trading Economics shows the US ten-year just under 5% and the dollar index near 102.1 on 29-October. The LME euro fixing fell to 1.1135.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='27-Oct'
        i['hist']=i['hist'][1:]+[["28-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,484.00 (3M); 14,675.50 (cash) $/t"
        i['ratio']="~14,675.50 $/t cash vs LME 3M 14,484.00 $/t"
        i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the WEDNESDAY 28-OCTOBER-2026 session at $14,675.50, UP $50.50 or 0.35% against $14,625.00. THE WINDOW ROLLED THIS RUN: 07-October dropped and 28-October appended, so the series is the last fifteen published official cash sessions, 08-October to 28-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 27-October). "
                  "Copper structure for context: backwardation $191.50 (from $190.00), stock fell 1,275 t to 271,450 t.")
s=d['inputs_summary']; j=s.find("UPDATE 28-OCTOBER"); s=s[j:] if j>=0 else s
d['inputs_summary']=("UPDATE 29-OCTOBER: Copper rolled to the Wednesday 28-October LME official cash of $14,675.50, up $50.50, with its fifteen-session window moved to 08-October to 28-October. No new monthly carbon settlement is due until mid-November, and no new dated SMM fluoride, silicon or magnesium mark was located, so no other hist mark was appended. "
 "Energy eased from highs but stays elevated: Brent about $114.30 (-0.89%) and European gas EUR 98.22/MWh (-2.11%, still up about 36% on the month) on 29-October, with EU storage below 75% against a five-year average near 86% (Trading Economics). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
otl=0.5*3078.0; ores=2403-otl; osh=otl/2403*100
OLDT=f"the tariff leg of the US duty-paid premium is 0.50 times the 27-October official cash of $3,078.00, or ${otl:,.2f}, UP $15.25 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${ores:,.2f}, so {osh:.1f}%"
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 28-October official cash of $3,101.00, or ${tl:,.2f}, UP $11.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED WEDNESDAY 28-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE TUESDAY 27-OCTOBER OFFICIAL)."; NEWC="COMPILED THURSDAY 29-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE WEDNESDAY 28-OCTOBER OFFICIAL)."
n=0; nc=0
for p in d['premiums']:
    n+=p['src'].count(OLDT); nc+=p['src'].count(OLDC); p['src']=p['src'].replace(OLDT,NEWT).replace(OLDC,NEWC)
print('premium tariff replaced',n,nc); assert n==len(d['premiums'])
ra=360.40/m3*100; na=0
o="THE RATIO: LME Alumina at $360.40/t against the 27-October aluminium three-month of $3,064.00 is 11.76%"
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    if o in s: na+=1
    a['src']=s.replace(o,f"THE RATIO: LME Alumina at $360.40/t against the 28-October aluminium three-month of $3,084.00 is {ra:.2f}%")
print('alumina',na,len(d['alumina'])); assert na==len(d['alumina'])

d['lme_commentary']=("3,077 CLEARED AND THE CURVE FOLLOWED. On the Wednesday 28-October official cash settled $3,101.00 (+$23.00) and three-month $3,084.00 (+$20.00) - a third straight rise, the highest three-month settlement since 09-October and the first settled close above 3,077, the level this page set as confirmation of the rebound. "
 "This time cash led, so the backwardation widened to $17.00 from $14.00 - back above the $15.00 reversal condition, with spread and price moving together after two sessions of divergence; visible stock fell 200 t to a new low of 231,900 t. The whole base-metals board rose (zinc +1.0%, aluminium +0.65%, nickel +0.6%, copper +0.3%, lead +0.3%) and stocks fell for all five metals. "
 "After the official the Fed held rates at 3.75-4.00% by 10-2, with two dissents for a hike and no clear December signal; Trading Economics read the statement as slightly dovish (dollar index about 102.1, US ten-year just under 5% on 29-October). The Trading Economics aluminium CFD reference nonetheless slipped about 0.7% to roughly $3,078.50 later on 28-October, so the first test is whether Thursday's official holds above 3,077. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: PRICE AND STRUCTURE CONFIRMED TOGETHER FOR ONE SESSION. Constructive: three-month settled above 3,077 for the first time ($3,084.00) on a third straight rise, the backwardation widened back above $15.00 to $17.00, visible LME stock fell to another low of 231,900 t, every LME base metal rose with stocks down across the board, the Fed hold was read as slightly dovish, and energy costs stay elevated (Brent near $114, TTF near EUR 98) with Hormuz still effectively closed. "
 "Against: the post-official CFD reference slipped back to about $3,078.50, so the break is marginal; Trading Economics notes Chinese output near record levels and September exports up 25.9% y/y; Gulf supply keeps returning and European nine-month output rose to 5.56 Mt on restarts (AL Circle); two FOMC members voted for a hike and December remains open.")
d['bottom_line']=("BOTTOM LINE: on the Wednesday 28-October LME official aluminium three-month rose $20.00 to $3,084.00 and cash $23.00 to $3,101.00 - the first settled close above 3,077 - while the backwardation widened back to $17.00, above the $15.00 tightness trigger, and visible stock fell to another low of 231,900 t. "
 "Both pre-registered tests passed on the same session, so scenario weight shifts from bear to bull: 20% bull / 45% base / 35% bear. The daily Elliott count now treats wave (v) of the C-wave decline from 3,374 as complete at 2,994.50 (about 65%), with a corrective rebound toward the 3,110-3,148.5 area; a settled close back below 3,061.5 would weaken it and below about 2,977.5 would force a re-count; invalidation 3,289. The weekly corrective count toward 2,894 stays the larger-degree preference until a weekly close above 3,077. Next tests: Thursday's official holding 3,077 and Friday's weekly close.")
c2=d['commercial']
for a,b in [("FIRST, THE PRICE ROSE BUT THE PROMPT PREMIUM KEPT EASING: a $14.00 backwardation on 27-October, narrower than $20.50 as three-month rose $37.00 and cash $30.50 - back below the $15.00 reversal condition after three prints beyond it, so nearby metal is still valued over forward metal but by less, and the rally is being carried by forward buying and short-covering rather than prompt physical demand.",
             "FIRST, PRICE AND PROMPT PREMIUM FIRMED TOGETHER: a $17.00 backwardation on 28-October, wider than $14.00 as cash rose $23.00 and three-month $20.00 - back above the $15.00 reversal condition, so nearby metal is again valued more clearly over forward metal and there is no carry reward for deferring purchases; one session does not make a trend."),
 (f"is ${otl:,.2f} on 27-October cash, {osh:.1f}% of the $2,403/t premium",f"is ${tl:,.2f} on 28-October cash, {share:.1f}% of the $2,403/t premium"),
 ("the 27-October official took three-month to $3,064.00, $69.50 above the 2,994.50 settled low and $2.50 above 3,061.5 (first close above it), $13.00 short of 3,077; energy firmed again (Brent about $115.64; European gas EUR 97.07/MWh, 28-October); the Fed decides on 28-October;",
  "the 28-October official took three-month to $3,084.00, $89.50 above the 2,994.50 settled low and $7.00 above 3,077 (first close above it); energy eased from highs but stays elevated (Brent about $114.30; European gas EUR 98.22/MWh, 29-October); the Fed held at 3.75-4.00% on 28-October with two dissents for a hike;")]:
    assert a in c2,a; c2=c2.replace(a,b)
d['commercial']=c2

O_SC=("HELD 28-OCTOBER at 15/45/40: the 27-October official lifted three-month $37.00 to $3,064.00, a first settled close above 3,061.5, but the backwardation narrowed to $14.00 - back below the $15.00 trigger - and Chinese ingot stocks rose a second session, so the price and structure signals offset and no weight moves until a close above 3,077 or a slip back below 3,061.5. ")
NEWP={'15%':'20%','45%':'45%','40%':'35%'}
for s in d['outlook']['scenarios']:
    assert s['drivers'].startswith(O_SC)
    s['prob']=NEWP[s['prob']]
    s['drivers']=("MOVED 29-OCTOBER from 15/45/40 to 20/45/35: the 28-October official took three-month $20.00 higher to $3,084.00, a first settled close above 3,077, AND the backwardation widened back above the $15.00 trigger to $17.00 with stock at another low - both pre-registered tests passed on one session, so five points move from bear to bull. A settled close back below 3,061.5 with the spread heading to contango would reverse the shift. ")+s['drivers'][len(O_SC):]
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium three-month rose $20 to $3,084 on Wednesday's LME official - its first settled close above $3,077 - and the backwardation widened back above the $15 tightness trigger to $17: price and physical structure confirmed together for the first time in this rebound, though the post-official price already slipped back toward $3,078.",
 "points":[
 "WHAT MOVED: Wednesday's LME official settled cash at $3,101.00 (+$23.00) and three-month at $3,084.00 (+$20.00, +0.65%), a third straight rise and the highest since 9 October. Cash now trades $17.00 above three-month (backwardation), up from $14.00, and LME stock fell 200 t to a new low of 231,900 t. Every LME base metal rose and all five stocks fell.",
 "WHY: Fed-hike expectations had cooled into the meeting; the Fed then held rates at 3.75-4.00% by 10-2 with two dissents for a hike and no clear December signal, which markets read as slightly dovish (dollar index about 102.1, US ten-year just under 5%).",
 "AGAINST: Trading Economics notes Chinese output near record levels and September exports up 25.9% y/y; Europe's nine-month output rose to 5.56 Mt on restarts (AL Circle) and Gulf restarts continue. The Trading Economics price reference slipped about 0.7% after the official, so the break above $3,077 is marginal.",
 "WHAT TO WATCH: whether Thursday's official holds above $3,077 and Friday's weekly close; whether the backwardation stays above $15; Hormuz, still effectively closed, with Tehran reportedly pressing a seven-day reopening plan that Washington disputes (Straits Daily Brief)."]}

d['feed']=([
 {"when":"Thu 29-Oct","impact":"Bullish","text":"BOARD ROLLED TO THE WEDNESDAY 28-OCTOBER LME OFFICIAL: cash $3,101.00 (+$23.00), three-month $3,084.00 (+$20.00), first settled close above 3,077; stock -200 t to a new low of 231,900 t."},
 {"when":"Thu 29-Oct","impact":"Bullish","text":"STRUCTURE FIRMER: the cash-to-three-month backwardation widened to $17.00 from $14.00, back above the $15.00 reversal condition - spread and price moved together after two sessions of divergence."},
 {"when":"Thu 29-Oct","impact":"Mixed","text":"FED HOLDS at 3.75-4.00% (10-2; Cook and Hammack dissented for a hike); no clear December signal; dollar index about 102.1, US ten-year just under 5% (Trading Economics)."},
 {"when":"Thu 29-Oct","impact":"Mixed","text":"ENERGY / HORMUZ: Brent about $114.30 (-0.89%), TTF EUR 98.22/MWh (-2.11%) (Trading Economics); Straits Daily Brief - strait still effectively closed (2 transits on 25-October vs an 85/day baseline); Tehran reportedly pressing a seven-day reopening plan, disputed by Washington."},
 {"when":"Wed 28-Oct","impact":"Bearish","text":"AL CIRCLE: Europe's nine-month 2026 aluminium production rose to 5.56 Mt as smelter restarts gain ground."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM CLEARS 3,077. The Wednesday 28-October official settled cash at $3,101.00 (+0.75%) and three-month at $3,084.00 (+0.65%) - a third straight rise, the highest three-month settlement since 09-October and the first settled close above 3,077. Visible stock fell 200 t to a new low of 231,900 t. Every metal on the board rose: zinc three-month +1.04%, nickel +0.64%, copper +0.34%, lead +0.31%; stocks fell for all five."},
 {"theme":"LME","horizon":"0-1 month","impact":"Bullish","url":W,
  "headline":"THE CURVE FOLLOWED THIS TIME: the cash-to-three-month backwardation widened to $17.00 from $14.00 on 28-October, back above the $15.00 reversal condition one session after slipping below it, because cash rose more than three-month. READ: the first session in this rebound where prompt tightness and flat price confirmed together - one session, not yet a trend."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Mixed","url":S_TD,
  "headline":"FED HOLDS (Trading Economics, 29-October): the Federal Reserve held its benchmark rate at 3.75-4.00% by a 10-2 vote, with Governor Cook and Cleveland Fed President Hammack dissenting in favour of a 25bp hike; officials gave no clear signal on December and said data will guide decisions; traders read small statement changes as slightly dovish. The dollar index eased to about 102.1 and the US ten-year slipped just under 5%. Chair Warsh also said rate decisions will be cut to seven in 2027 and six in 2028."},
 {"theme":"Supply","horizon":"0-6 months","impact":"Bearish","url":S_EU,
  "headline":"EUROPEAN RESTARTS GAIN GROUND (AL Circle, 28-October): Europe's nine-month 2026 primary aluminium production rose to 5.56 Mt as smelter restarts gained ground. Separately, Trading Economics notes Chinese output running close to record levels despite the capacity cap, Chinese September exports up 25.9% y/y, Indonesian exports above 150,000 t in August, and Rio Tinto's agreement to run Bell Bay through 2031. READ: ex-Middle East supply keeps improving."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Mixed","url":S_TG,
  "headline":"ENERGY EASES FROM HIGHS (Trading Economics, 29-October): Brent slipped to about $114.30 (-0.89%) on renewed diplomacy, still up more than 17% on the month; TTF fell to about EUR 98.22/MWh (-2.11%) after approaching EUR 100, the highest since late 2022, with EU storage below 75% against a five-year average near 86%. The Straits Daily Brief (29-October) still describes Hormuz as effectively closed (2 transits on 25-October vs an 85/day baseline); Al Jazeera reports Tehran pressing a seven-day reopening plan, while President Trump denies peace talks are under way. READ: smelter energy costs stay elevated."},
 {"theme":"Alumina","horizon":"6-24 months","impact":"Bearish","url":S_CE,
  "headline":"CHALIECO WINS $833M EPC CONTRACT for a 2.4 Mt/y alumina project in Vietnam, due within 27 months (AL Circle, 28-October) - another addition to the ex-China alumina pipeline. Hydro is also investing $53.5m in a 5,900 t extrusion press at Cressona, Pennsylvania, operational in Q1-2028 (AL Circle, 28-October)."},
]+d['news']
d['news']=d['news'][:20]

hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Wed 28-Oct':
        hitc+=1
        cat['date']='Daily, from Thu 29-Oct'
        cat['event']="3,077 CLEARED ON THE 28-OCTOBER OFFICIAL ($3,084.00), ONE SESSION AFTER 3,061.5 WAS RECLAIMED ($3,064.00 on 27-October); THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE, RETESTED IT ON 20-OCTOBER ($2,997.00), AND HAS SINCE SETTLED $3,024.50, $3,008.00, $3,018.00, $3,027.00, $3,064.00 AND $3,084.00. The settled close above 3,077 is this page's stated confirmation that wave (v) is complete; next resistance 3,110 then the 3,148.5 wave (iv) high - above 3,148.5 the C wave is complete and above 3,183 the impulsive labelling void. A settled close back beneath 3,061.5 would weaken the rebound and beneath about 2,977.5 would force a re-count toward the 2,894 weekly 61.8%. Invalidation 3,289. STRUCTURE: the $15.00 backwardation reversal condition, lost on 27-October, was REGAINED on 28-October at $17.00. WEEKLY TEST: Friday 30-October close versus 3,077."
    elif cat['date']=='Tue 27 - Wed 28-Oct':
        hitc+=1
        cat['date']='Resolved Wed 28-Oct'
        cat['event']="FOMC - RESOLVED HOLD: the Fed held its benchmark rate at 3.75-4.00% by a 10-2 vote, with Cook and Hammack dissenting for a 25bp hike; no clear signal on December, decisions data-dependent; markets read the statement as slightly dovish (dollar index about 102.1, US ten-year just under 5%, Trading Economics 29-October). Into the meeting markets had priced about 90% odds of a hold and about 79-82% odds of a December hike. Chair Warsh also announced fewer rate decisions in 2027 (seven) and 2028 (six). The metals board rose on the day of the decision; the December meeting is the next policy test."
assert hitc==2,hitc
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 29-OCTOBER: the 28-October official printed a $17.00 BACKWARDATION, back ABOVE the $15.00 reversal condition one session after slipping below it, as cash outpaced three-month and stock fell to another low. Trend moved from FLAT back to DOWN: contango is $17.00 away and prompt tightness re-firmed."
RK[0]['trend']='down'
RK[4]['risk']+=" UPDATE 29-OCTOBER: LME stock fell 200 t to a new series low of 231,900 t on 28-October, a sixth straight draw but the smallest of the run; no new Chinese social-inventory print was located this run. Trend held at FLAT."
RK[4]['trend']='flat'
hit=0
for r in RK:
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 29-OCTOBER: Brent eased to about $114.30 (-0.89%) and TTF to EUR 98.22/MWh (-2.11%) after approaching EUR 100, still up about 36% on the month with EU storage below 75% (Trading Economics). Trend held at UP."; hit+=1
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 29-OCTOBER: Straits Daily Brief - strait still effectively closed to normal commercial traffic (IMF PortWatch: 2 transits on 25-October vs an 85/day baseline); Al Jazeera reports Tehran pressing a seven-day reopening plan via mediators, which President Trump disputes; no new independently sourced ship attack in the window. Trend held at UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 29-OCTOBER: RESOLVED FOR NOW - the Fed held at 3.75-4.00% on 28-October (10-2, two dissents for a hike) with no clear December signal, read as slightly dovish; the US ten-year slipped just under 5% and the dollar index to about 102.1 (Trading Economics). Trend moved from UP to FLAT: the hike risk is deferred to December, not removed."; hit+=1; r['trend']='flat'
    if r['risk'].startswith('THE EX-CHINA RESTART PIPELINE'):
        r['risk']+=" UPDATE 29-OCTOBER: AL Circle (28-October) reports Europe's nine-month 2026 output up to 5.56 Mt as restarts gain ground; Trading Economics notes Indonesian exports above 150,000 t in August and Rio Tinto extending Bell Bay through 2031. Trend held at UP."; hit+=1; r['trend']='up'
assert hit==4,hit
d['outlook']['ai_analysis'].insert(0,"THURSDAY 29-OCTOBER ON THE WEDNESDAY 28-OCTOBER OFFICIAL: three-month rose $20.00 to $3,084.00 and cash $23.00 to $3,101.00 - the first settled close above 3,077 - and the backwardation widened back to $17.00, above the $15.00 reversal condition, with visible stock at another low (231,900 t). Both pre-registered tests passed on one session, so scenario weights move to 20/45/35 from 15/45/40. The Fed held at 3.75-4.00% with two hawkish dissents and no December signal, read as slightly dovish. Caution: the post-official CFD reference slipped back to about $3,078.50, Chinese output is near record and European restarts are adding supply; a settled close back below 3,061.5 with the spread heading to contango would reverse the shift.")

EWS=("REVIEWED 29-OCTOBER ON THE WEDNESDAY 28-OCTOBER OFFICIAL: three-month settled $3,084.00, up $20.00 - a ninth settled close above the 2,994.50 low of 15-October and THE FIRST ABOVE 3,077, the level this count set as confirmation. The sequence 2,994.50 / 3,024.50 / 3,008.00 / 3,018.00 / 3,027.00 / 3,064.00 / 3,084.00 is the first leg of a corrective rebound from a completed wave (v) of C. Wave (v) ($154.00 from the 3,148.5 wave (iv) high to 2,994.50) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged, NOT re-labelled; base case raised to about 65%: wave (v) ended at 2,994.50 and the rebound extends toward 3,110 then the 3,148.5 wave (iv) area; alternate about 35%: the move above 3,077 fails (the post-official CFD reference already slipped toward 3,078) and a settled close back beneath 3,061.5 reopens the low, with a close beneath 2,977.5 forcing a re-count toward 2,894. Invalidation 3,289; confidence moderate. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED 24-OCTOBER"); assert st.startswith("REVIEWED 28-OCTOBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED 24-OCTOBER"); assert lt.startswith("REVIEWED 28-OCTOBER") and k>0
d['ew']['long_term']['writeup']="REVIEWED 29-OCTOBER (WEDNESDAY 28-OCTOBER OFFICIAL, WEEK IN PROGRESS): three-month at 3,084.00, up $66.00 from the 3,018.00 weekly close and $7.00 above the 3,077 50% retracement, in the upper half of the 2,950-3,110 zone; a WEEKLY close above 3,077 on Friday 30-October would be the first sign the larger correction is ending early, but until then the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label. "+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="114.30",day="about $114.30 on 29-October, -0.89% (Trading Economics); still up more than 17% on the month",
 note="REFRESHED THURSDAY 29-OCTOBER-2026 (Trading Economics): Brent eased from near four-year highs as investors weighed renewed diplomacy to contain the Middle East conflict, including reported US-Iran contacts; Saudi-Houthi clashes and threats to Hormuz shipping keep it supported, while regional energy flows are reported near pre-war levels. The Straits Daily Brief shows $114.34 at 00:11 UTC. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="98.2",day="EUR 98.22/MWh on 29-October, -2.11% (Trading Economics); up about 36% on the month",
 note="REFRESHED THURSDAY 29-OCTOBER-2026 (Trading Economics): TTF eased after approaching EUR 100/MWh, the highest since late 2022. EU storage was below 75% on 28-October against a five-year average near 86% and about 100 TWh below a year earlier; Germany and the Netherlands are lowest; colder forecasts and reports of possible US military action in the Gulf add risk. The stats section shows 98.36 (-1.98%). SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="102.09",day="about 102.09 on 29-October, -0.04% (Trading Economics); eased after the Fed hold",
 note="REFRESHED THURSDAY 29-OCTOBER-2026 (Trading Economics): the dollar slipped after the Fed held rates at 3.75-4.00% by 10-2 (Cook and Hammack dissenting for a hike); traders read the statement as slightly dovish and officials gave no clear December signal. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="4.99",day="about 4.99% on 29-October, -3bp (Trading Economics); just under 5% after the Fed hold",
 note="REFRESHED THURSDAY 29-OCTOBER-2026 (Trading Economics): the yield slipped just below 5% after the Fed left rates unchanged with little signal about December; decisions depend on incoming data and progress toward 2% inflation. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.11350',day="LME fixing on 28-October, down from 1.11520; ECB fixing 1.11330, BFIX 1.11349",
 note="REFRESHED THURSDAY 29-OCTOBER-2026 to the 28-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE WEDNESDAY 28-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION. This Thursday 29-October run is compiled about 02:40 London, BEFORE the ring, so Thursday's official (13:20 London) has not printed. The Trading Economics aluminium CFD reference (about $3,078.50, -0.69% on 28-October, after the official) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (29-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 28-October session, and the per-metal aluminium daily table's newest row is 28-October (cash 3,101.00, three-month 3,084.00, stock 231,900) with NO later row, so the board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.11520) matches the 27-October board verified on 28-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 27-October, and match the pages' change column: aluminium -200 to 231,900; copper -1,275 to 271,450; nickel -1,404 to 278,814; zinc -1,025 to 164,625; lead -2,000 to 312,675.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (28-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (twenty sessions, 01- to 28-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,084.00; the stock chart axis floor of 220,000 t leaves about 11,900 t of headroom below visible stock at 231,900 t and will be re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,101.00 against three-month $3,084.00 is therefore a $17.00 BACKWARDATION, wider than $14.00 on 27-October - the spread and the flat price moved in the same direction this session."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 28-October official cash of $3,101.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $114.30), the dollar index (about 102.09), TTF (EUR 98.22/MWh) and the US ten-year (about 4.99%) are Trading Economics readings shown on 29-October; Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages were internally inconsistent by a few cents or basis points this run (header vs stats section), so they are approximate; EUR/USD is the 28-October LME fixing, the same session as the board. The Straits Daily Brief (29-October) shows Brent at $114.34 at 00:11 UTC - a different time stamp, cited in text only."; hit+=1
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 29-OCTOBER: no authorised fetch was blocked (Westmetall EN, DE and per-metal pages, Trading Economics, AL Circle, news.metal.com and the Straits Daily Brief all fetched). The news.metal.com front page carried no dated SMM aluminium morning summary or inventory print for 28/29-October, and a search found none, so no Chinese inventory figure is updated this run. Hormuz items in the Straits Daily Brief flagged as single-source or unverified are cited as reported, not as fact. No Q1-2027 Japanese premium offer has been reported yet (negotiations normally start late November); a search this run found none. Trading Economics' EGA summary (a quarter of cells online) is older than EGA's own 21-October release (half restarted), so the company release is kept."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: NO NEW PEER RESULT WAS REPORTED IN THIS WINDOW. Norsk Hydro's Q3-2026 (23-October) remains the latest addition; Chalco's Q3-2026 report was searched for again and not yet located (it normally publishes in late October; broker estimates are NOT published as results). NO NEW COMPANY WAS BACK-FILLED THIS RUN. Century Aluminum has not yet announced its Q3 date. Other entries are carried at their last publicly verified figures, and gaps stay gaps."; hit+=1
assert hit==4,hit
en=d['earnings_note']
assert "no newer peer result to 28-October):" in en
d['earnings_note']=en.replace("(added 24-October; no newer peer result to 28-October):","(added 24-October; no newer peer result to 29-October):",1)

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 28-OCTOBER: no newer public disclosure","REVIEWED 29-OCTOBER: no newer public disclosure").replace("REVIEWED 28-OCTOBER. NO NEW DATED","REVIEWED 29-OCTOBER. NO NEW DATED")
    return o
PS={p['name']:p for p in d['producer_status']}
c=PS['Slovalco (Hydro / Penta JV, Slovakia)']
c['update']="UPDATED 29-OCTOBER (AL Circle, 28-October): Europe's nine-month 2026 primary aluminium output rose to 5.56 Mt as smelter restarts gained ground (regional, not asset-specific); Slovalco's first 75,000 t/y phase remains guided for end-February 2027. "+c['update']
c=PS['China operators (aggregate, incl. Chalco and Hongqiao)']
c['update']="UPDATED 29-OCTOBER (Trading Economics, 28/29-October): Chinese output is running close to record levels despite the capacity cap and September aluminium exports rose 25.9% y/y; no new SMM inventory print was located this run; Chalco's Q3-2026 report not yet located. "+c['update']
c['src']=[L_TE,S_TE]
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD
for s_ in [[L_TE,S_TE],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG],[L_ST,S_ST],[L_EU,S_EU],[L_CE,S_CE],[L_HY,S_HY]]:
    d['sources'].append(s_)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 28-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 27-Oct)",W])
for x in ([L_TD,S_TD],[L_ST,S_ST],[L_EU,S_EU]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-27'
ph['rows'][-1]=['2026-10-28',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
