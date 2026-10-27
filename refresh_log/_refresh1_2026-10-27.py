# Daily data refresh - 2026-10-27 (TUESDAY, ~02:45 UTC, BEFORE the ring). Board ROLLED to MONDAY 26-Oct LME official (latest published session).
# Westmetall cache-busted EN and DE overviews both fetched and agree on the full 26-Oct session; Al per-metal table top row = 26-Oct (no later row).
# Completeness: 5/5 stock lines reconcile vs 23-Oct board (DE page change column agrees); prior FX column (MTLE 1.11910) matches 23-Oct board.
# Key: Al cash 3,047.50 (+4.50), 3M 3,027.00 (+9.00) -> BACKWARDATION narrowed to $20.50 from $25.00 while price rose (opposite directions); stock -1,750 to 234,050 (new low).
# TE 26/27-Oct: Brent 114.61 (-1.04%), TTF EUR94.92 (-1.82%), DXY 102.04, UST10Y 4.98%; Fed hold ~90%, Dec hike ~82%.
# SMM 27-Oct: three-region ingot 419,500 t (+7,500), ending a ten-day destocking run; SHFE 23,525 (+0.32%); LME 3M e-close 3,038 (-0.08%).
# SMM 26-Oct: Sept China prebaked-anode exports 288,300 t (+39.75% y/y), avg ~$968.63/t; Alba lines 4-6 running, ~1.3 Mt operating.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-27'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (26/27-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (27-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (26/27-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (27-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (27-Oct-2026)"
S_MM="https://news.metal.com/newscontent/104179681-aluminum-morning-meeting-summary-aluminum-prices-consolidate-as-expectations-for-us-fed-interest-rate-hikes-disrupt-and-limited-destocking-support"
L_MM="SMM - Aluminum prices consolidate as Fed rate-hike expectations disrupt and destocking support is limited [Aluminum Morning Meeting Summary] (27-Oct-2026)"
S_IN="https://news.metal.com/newscontent/104179744-chinas-aluminum-ingot-inventory-in-three-regions-rises-on-october-27"
L_IN="SMM - China's aluminum ingot inventory in three regions rises on October 27 (27-Oct-2026)"
S_AN="https://news.metal.com/newscontent/104179333-september-prebaked-anode-exports-surge-as-overseas-aluminum-smelter-restarts-underpin-demand-smm-analysis"
L_AN="SMM - September prebaked anode exports surge as overseas aluminum smelter restarts underpin demand (26-Oct-2026)"
S_ST="https://straits.live/briefs/2026-10-27"; L_ST="Straits Daily Brief - Strait of Hormuz, 27-Oct-2026"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
assert B['LME Cash settlement']['cur']==3043.0 and B['LME 3-month']['cur']==3018.0
cash,prev_c,m3,prev_m,stk,prev_s=3047.5,3043.0,3027.0,3018.0,234050,235800
spr=cash-m3; assert spr==20.5 and prev_s-1750==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED TUESDAY 27-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING). THE BOARD IS THE MONDAY 26-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION; Tuesday's official has not printed yet. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 26-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.11910); their prior-day FX column (MTLE 1.11910) matches the verified 23-October board, and the per-metal aluminium table's newest row is 26-October with NO later row; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 23-October (and match the German page's change column): aluminium 235,800 less 1,750 to 234,050; copper 273,750 less 775 to 272,975; nickel 280,674 less 732 to 279,942; zinc 167,025 less 75 to 166,950; lead 322,175 less 3,525 to 318,650. "
 "The whole board sits on ONE UNIFORM SESSION (26-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(" CASH SETTLED $3,047.50 ON THE 26-OCTOBER OFFICIAL, UP $4.50 OR 0.15% FROM $3,043.00. THREE-MONTH SETTLED $3,027.00, UP $9.00 OR 0.30% FROM $3,018.00 - the highest settled three-month since 13-October, $16.50 ABOVE the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%), $32.50 above the 2,994.50 settled low of 15-October and an ELEVENTH settled close beneath the 3,061.5 July low (by $34.50). "
 "THE BACKWARDATION NARROWED TO $20.50 FROM $25.00 because three-month rose more than cash - SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS (price up, structure softer) - but it is still a THIRD consecutive settled official beyond the published $15.00 reversal condition. "
 "VISIBLE LME STOCK FELL 1,750 t TO 234,050 t, another new series low and the largest one-day draw since 19-October.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,047.5","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,027.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $34.50 BENEATH THE 3,061.5 JULY LOW, $50.00 beneath the 3,077 weekly 50% retracement and $262.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a seventh session; the rule-based cap on daily wave (v) near 2,977.5 was never touched."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+20.5","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,047.50 against three-month $3,027.00 is a $20.50 BACKWARDATION, NARROWER than 23-October's $25.00 as three-month rose $9.00 and cash only $4.50 - THE SPREAD SOFTENED WHILE THE PRICE ROSE, the two moving in opposite directions. It remains the THIRD consecutive settled official beyond the published $15.00 reversal condition (confirmed on 23-October); a return below $15.00 would weaken, and a contango beyond $24.50 would reverse, that signal. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"234,050","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 1,750 t TO 234,050 t, another new series low and a fourth straight draw. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,027.00, UP $9.00 - the highest settled three-month since 13-October, $34.50 beneath the 3,061.5 July low (an eleventh settled close below it) and $16.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 1,750 t TO 234,050 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":25.0,"avg":sep_sp,"note":VER+f" A $20.50 BACKWARDATION, NARROWER THAN 23-OCTOBER'S $25.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Three-month rose $9.00 and cash $4.50, so the structure softened while the flat price rose - opposite directions. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): CONFIRMED on 23-October and still met on 26-October (third consecutive print)."},
 {"name":"EUR/USD LME fixing","cur":1.1191,"prev":1.1191,"avg":1.1465,"note":VER+" THE LME EURO FIXING WAS UNCHANGED AT 1.11910 at the Monday ring; the ECB fixing printed 1.11880 and BFIX 1.11890. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (26-Oct official)","price":"3,047.5","basis":"THE 26-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,047.50, UP $4.50 OR 0.15%. Next official Tuesday 27-October 13:20 London."},
 {"tenor":"3-month (26-Oct official)","price":"3,027.0","basis":"THE 26-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,027.00, UP $9.00 - the highest since 13-October, $34.50 beneath the 3,061.5 July low (eleventh settled close below it), $32.50 above the 2,994.50 October low and $16.50 above the 02-January official."},
 {"tenor":"Cash-to-3M structure","price":"+20.5 (BACKWARDATION)","basis":"A $20.50 BACKWARDATION, narrowed from $25.00 while price rose - still the third consecutive settled print beyond the $15.00 reversal condition."},
 {"tenor":"Visible LME stock","price":"234,050 t","basis":f"DOWN 1,750 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE BACKWARDATION EASED BUT HELD ABOVE THE TRIGGER. On the 26-October official cash $3,047.50 sits $20.50 ABOVE three-month $3,027.00, a BACKWARDATION, narrower than $25.00 on 23-October because three-month rose $9.00 and cash $4.50 - SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00 and now $20.50. "
 f"READ: an eighth straight backwardation and a third consecutive print beyond the published $15.00 reversal condition, while visible stock set another low (234,050 t). The narrowing is worth watching: a slip back below $15.00 would weaken the signal. The September mean spread was ${sep_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]
d['chart_stock_axis']=[220000,255000]

ls=d['lme_series']; assert ls[-1][0]=='23-Oct', ls[-1]
d['lme_series']=ls[1:]+[["26-Oct",cash,m3,stk]]
assert all(220000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14500.0,14332.0,14415.0,14270.0); NI=(15535.0,15750.0,15695.0,15900.0); ZN=(3900.0,3797.0,3790.0,3726.0); PB=(1900.0,1921.0,1886.0,1908.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average-to-date: 17 sessions to 23-Oct (16 listed in 24-Oct script + 23-Oct) + 26-Oct
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0,3736.0,3771.0,3727.0,3790.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0,1851.0,1880.0,1872.0,1886.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/18)/(sum(zs)/17),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/18)/(sum(ps)/17),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-26'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending MONDAY 26-OCTOBER-2026 (Tuesday's official prints 13:20 London, after this run). THE WINDOW ROLLED THIS RUN: 05-October dropped and 26-October appended, so the window is 06-October to 26-October. Every point is an official cash settlement; the 26-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 23-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (26-October-2026 session; stock lines reconciled against 23-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,500.00, up $85.00 or 0.59%; three-month $14,332.00, up $62.00 or 0.43%. The BACKWARDATION WIDENED to $168.00 from $145.00. Stock fell 775 tonnes to 272,975 t, ending a run of five straight rises."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,535.00, down $160.00 or 1.02%; three-month $15,750.00, down $150.00 or 0.94% - the only metal down on the board for a second session. CONTANGO $215.00 from $205.00, still the widest carry on the board. Stock fell 732 tonnes to 279,942 t."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,900.00, up $110.00 or 2.90%; three-month $3,797.00, up $71.00 or 1.91% - the strongest metal on the board. BACKWARDATION widened to $103.00 from $64.00. Stock fell 75 tonnes to 166,950 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,900.00, up $14.00 or 0.74%; three-month $1,921.00, up $13.00 or 0.68%. CONTANGO $21.00 from $22.00. Stock drew 3,525 tonnes to 318,650, a twenty-sixth consecutive draw."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Monday 26-October official the board rose for a second session except nickel - zinc three-month +1.91%, lead +0.68%, copper +0.43% and aluminium +0.30%, with nickel -0.94%. Stocks fell for all five metals. Trading Economics shows the US ten-year just below 5% and the dollar index near 102 ahead of the 27-28 October Fed meeting. The LME euro fixing was unchanged at 1.1191.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='23-Oct'
        i['hist']=i['hist'][1:]+[["26-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,332.00 (3M); 14,500.00 (cash) $/t"
        i['ratio']="~14,500.00 $/t cash vs LME 3M 14,332.00 $/t"
        i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the MONDAY 26-OCTOBER-2026 session at $14,500.00, UP $85.00 or 0.59% against $14,415.00. THE WINDOW ROLLED THIS RUN: 05-October dropped and 26-October appended, so the series is the last fifteen published official cash sessions, 06-October to 26-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 23-October). "
                  "Copper structure for context: backwardation $168.00 (from $145.00), stock fell 775 t to 272,975 t.")
s=d['inputs_summary']; j=s.find("UPDATE 24-OCTOBER"); s=s[j:] if j>0 else s
d['inputs_summary']=("UPDATE 27-OCTOBER: Copper rolled to the Monday 26-October LME official cash of $14,500.00, up $85.00, with its fifteen-session window moved to 06-October to 26-October. No new monthly carbon settlement is due until mid-November, and no new dated SMM fluoride, silicon or magnesium mark was located, so no other hist mark was appended. "
 "CARBON CONTEXT (SMM, 26-October, customs data): China's September prebaked-anode exports reached 288,300 t, a 2026 monthly high, up 39.75% year on year and 21.03% month on month, at an average export price of about $968.63/t (+25.40% y/y), with Indonesia, Norway, Canada, Malaysia and the UAE the main destinations - SMM ties this to ex-China smelter restarts. This is an export-value basis, not the Shandong benchmark charted in the anode row, so it is NOT appended to that series. "
 "Energy eased slightly: Brent $114.61 (-1.04%) and European gas EUR 94.92/MWh (-1.82%) on 27-October, with EU storage about 75% full, the lowest seasonal level since 2009 (Trading Economics). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT="the tariff leg of the US duty-paid premium is 0.50 times the 23-October official cash of $3,043.00, or $1,521.50, UP $5.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of $881.50, so 63.3%"
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 26-October official cash of $3,047.50, or ${tl:,.2f}, UP $2.25 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED MONDAY 26-OCTOBER-2026 (BEFORE THE RING; LATEST PUBLISHED OFFICIAL) (LME BOARD ON THE FRIDAY 23-OCTOBER OFFICIAL)."; NEWC="COMPILED TUESDAY 27-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE MONDAY 26-OCTOBER OFFICIAL)."
n=0; nc=0
for p in d['premiums']:
    n+=p['src'].count(OLDT); nc+=p['src'].count(OLDC); p['src']=p['src'].replace(OLDT,NEWT).replace(OLDC,NEWC)
print('premium tariff replaced',n,nc); assert n==len(d['premiums'])
ra=360.40/m3*100; na=0
o="THE RATIO: LME Alumina at $360.40/t against the 23-October aluminium three-month of $3,018.00 is 11.94%"
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    if o in s: na+=1
    a['src']=s.replace(o,f"THE RATIO: LME Alumina at $360.40/t against the 26-October aluminium three-month of $3,027.00 is {ra:.2f}%")
print('alumina',na,len(d['alumina'])); assert na==len(d['alumina'])

d['lme_commentary']=("A FIRMER PRICE, A SOFTER CURVE. On the Monday 26-October official cash settled $3,047.50 (+$4.50) and three-month $3,027.00 (+$9.00) - the highest three-month settlement since 13-October, $16.50 above the 02-January official, $32.50 above the 15-October settled low of 2,994.50 and $34.50 beneath the 3,061.5 July low. "
 "Because three-month outpaced cash, the backwardation narrowed to $20.50 from $25.00 - spread and flat price moved in opposite directions - though it is a third straight settled print beyond the $15.00 reversal condition; visible stock fell 1,750 t to a new low of 234,050 t. Every base metal except nickel rose and all five stock lines fell; zinc led (+1.9%). "
 "After the official, SMM reports LME three-month closing electronic trade at $3,038 (-0.08%) and Shanghai at RMB 23,525 (+0.32%), with Chinese three-region ingot stocks up 7,500 t to 419,500 t on 27-October, ending a ten-day draw. Energy eased (Brent $114.61, -1.04%) on Gulf diplomacy, and the Fed meets 27-28 October with a hold priced at about 90% and a December hike at about 82% (Trading Economics). "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND STILL IN CONTROL ON PRICE, STRUCTURE STILL SUPPORTIVE BUT LESS EMPHATIC. Against: three-month has settled beneath 3,061.5 eleven times; Gulf supply keeps returning - EGA has half of Al Taweelah's 1,262 cells restarted (21-October) and Alba's lines 4-6 are running, with operating capacity near 1.3 Mt (SMM, 26-October); China's anode exports surged in September to feed ex-China restarts; Chinese ingot stocks rose on 27-October for the first time in eleven working days (SMM); markets price about 82% odds of a December Fed hike (Trading Economics). "
 "Constructive: the backwardation printed beyond $15.00 for a third session ($20.50), visible LME stock fell to another low of 234,050 t, the 2,994.50 October low has held for seven sessions and three-month settled at its highest since 13-October; energy costs remain elevated (Brent near $115, TTF near EUR 95) with Hormuz still effectively closed.")
d['bottom_line']=("BOTTOM LINE: on the Monday 26-October LME official aluminium three-month rose $9.00 to $3,027.00 and cash $4.50 to $3,047.50, so the backwardation narrowed to $20.50 - price up, structure softer - while still a third close beyond the $15.00 tightness trigger, with visible stock at another low of 234,050 t. "
 "The structure has turned but price has not confirmed: three-month is still beneath 3,061.5 for an eleventh session. Scenario weights hold at 15% bull / 45% base / 40% bear; a settled close above 3,061.5-3,077 would add to the base/bull side, while a backwardation back below $15.00 or a break of 2,994.50 then 2,977.5 would reverse the shift. The daily Elliott count (wave (v) of a C-wave decline from 3,374) still leans to wave (v) complete at 2,994.50 - a settled close above 3,077 would confirm it, below about 2,977.5 would force a re-count; invalidation 3,289; the weekly corrective count towards 2,894 stays preferred. Next catalyst: the Fed decision on 28-October.")
c2=d['commercial']
for a,b in [("FIRST, THE PROMPT PREMIUM IS CONFIRMED: a $25.00 backwardation on 23-October for a second consecutive official, as cash and three-month both rose $10.00 - two prints beyond the $15.00 reversal condition, so nearby metal is clearly valued over forward metal and there is no carry reward for deferring purchases, though it is still far from a squeeze.",
             "FIRST, THE PROMPT PREMIUM HOLDS BUT EASED: a $20.50 backwardation on 26-October, narrower than $25.00 as three-month rose $9.00 and cash $4.50 - a third consecutive print beyond the $15.00 reversal condition, so nearby metal is still valued over forward metal and there is no carry reward for deferring purchases, though the narrowing shows the tightness is not building."),
 ("is $1,521.50 on 23-October cash, 63.3% of the $2,403/t premium",f"is ${tl:,.2f} on 26-October cash, {share:.1f}% of the $2,403/t premium"),
 ("the 23-October official took three-month to $3,018.00, $23.50 above the 2,994.50 settled low inside the 2,980-3,000 zone and $43.50 beneath 3,061.5; energy rose again (Brent $116.91, the highest since June 2022; European gas EUR 93.19/MWh);",
  "the 26-October official took three-month to $3,027.00, $32.50 above the 2,994.50 settled low inside the 2,980-3,000 zone and $34.50 beneath 3,061.5; energy eased slightly but stays high (Brent $114.61; European gas EUR 94.92/MWh, 27-October); the Fed decides on 28-October;")]:
    assert a in c2,a; c2=c2.replace(a,b)
d['commercial']=c2

O_SC="HELD 26-OCTOBER at 15/45/40: no new official before Monday's ring; continued Chinese destocking and Hormuz closure are supportive, ex-China restarts cap the upside. "
for s in d['outlook']['scenarios']:
    assert s['drivers'].startswith(O_SC)
    s['drivers']=("HELD 27-OCTOBER at 15/45/40: the 26-October official lifted three-month $9.00 to $3,027.00 with stock at another low, but the backwardation narrowed to $20.50 and price is still beneath 3,061.5, so no weight moves; Chinese ingot stocks rose on 27-October for the first time in eleven working days. ")+s['drivers'][len(O_SC):]
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium three-month rose $9 to $3,027 on Monday's LME official - its highest since 13 October - and stocks hit another low, but the backwardation narrowed to $20.50: price is firming while the tightness signal softens, with the Fed decision on 28 October next.",
 "points":[
 "WHAT MOVED: Monday's LME official settled cash at $3,047.50 (+$4.50) and three-month at $3,027.00 (+$9.00), $34.50 below the $3,061.5 July low. Cash still trades $20.50 above three-month (backwardation), down from $25.00 - the spread narrowed while price rose. LME stock fell 1,750 t to a new low of 234,050 t.",
 "WHY: LME sheds keep emptying and most of the metals board rose (zinc +1.9%, copper +0.4%). But Chinese three-region ingot stocks rose 7,500 t to 419,500 t on 27-October, ending a ten-day draw, and SMM expects consolidation as ex-China restarts weigh (SMM).",
 "SUPPLY AND COST: Gulf restarts continue - Alba's lines 4-6 are running at about 1.3 Mt and China's September anode exports jumped 40% y/y to supply restarting smelters (SMM). Energy eased on Gulf diplomacy (Brent $114.61, -1.0%) but Hormuz is still described as effectively closed.",
 "WHAT TO WATCH: the Fed decision on 28-October (hold about 90% priced; December hike about 82%); a settled close above $3,061.5-3,077 or a backwardation back below $15.00; whether Chinese ingot stocks resume falling."]}

d['feed']=([
 {"when":"Tue 27-Oct","impact":"Bearish","text":"SMM: China three-region aluminium ingot inventory rose 7,500 t to 419,500 t on 27-October (Guangdong +2,500, Wuxi +500, Gongyi +4,500), ending a ten-working-day destocking run; billet stocks flat at about 89,500 t."},
 {"when":"Tue 27-Oct","impact":"Mixed","text":"BOARD ROLLED TO THE MONDAY 26-OCTOBER LME OFFICIAL: cash $3,047.50 (+$4.50), three-month $3,027.00 (+$9.00), highest since 13-October; backwardation narrowed to $20.50 from $25.00 (third print beyond $15.00); stock -1,750 t to a new low of 234,050 t."},
 {"when":"Mon 26-Oct","impact":"Bearish","text":"SMM: China's September prebaked-anode exports hit a 2026 high of 288,300 t (+39.75% y/y) on ex-China smelter restarts; Alba lines 4-6 running with operating capacity near 1.3 Mt."},
 {"when":"Tue 27-Oct","impact":"Mixed","text":"ENERGY / HORMUZ: Brent $114.61 (-1.04%) as Saudi, Pakistani and Turkish officials met Iranian leaders (Trading Economics); Straits Daily Brief still describes the strait as effectively closed, with 125 vessels holding position."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Mixed","url":W,
  "headline":"LME ALUMINIUM: PRICE UP, CURVE SOFTER. The Monday 26-October official settled cash at $3,047.50 (+0.15%) and three-month at $3,027.00 (+0.30%), the highest three-month settlement since 13-October. The backwardation narrowed to $20.50 from $25.00 - still a third consecutive print beyond the $15.00 reversal condition - and visible stock fell 1,750 t to a new low of 234,050 t. Zinc three-month +1.91%, copper +0.43%, lead +0.68%, nickel -0.94%; stocks fell for all five metals."},
 {"theme":"China","horizon":"0-1 month","impact":"Bearish","url":S_IN,
  "headline":"CHINESE DESTOCKING PAUSES (SMM, 27-October): three-region aluminium ingot social inventory rose 7,500 t (+1.8%) to 419,500 t - Guangdong 120,500 t (+2,500), Wuxi 171,500 t (+500), Gongyi 127,500 t (+4,500) - ending ten straight working days of destocking. SMM's morning summary had the most-traded SHFE contract at RMB 23,525/t (+0.32%) and LME three-month at $3,038 (-0.08%) at Monday's close, with East China spot premiums at RMB 220-240/t, and expects consolidation as Fed-hike expectations and ex-China restarts weigh. READ: one day's build is not a trend, but it removes a support the market leaned on last week."},
 {"theme":"Supply","horizon":"0-6 months","impact":"Bearish","url":S_AN,
  "headline":"ANODE EXPORTS TRACK EX-CHINA RESTARTS (SMM, 26-October, customs data): China's September prebaked-anode exports reached 288,300 t, a 2026 monthly high, up 39.75% year on year and 21.03% month on month, at about $968.63/t; Indonesia (about 64,000 t), Norway, Canada, Malaysia and the UAE led. SMM says Alba's lines 4-6 have resumed, with operating capacity recovering to about 1.3 Mt, and EGA's Al Taweelah restart is advancing. READ: the input trade confirms ex-China smelting capacity is coming back."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Mixed","url":S_BR,
  "headline":"ENERGY EASES ON DIPLOMACY, RISK STAYS (Trading Economics, 27-October): Brent fell 1.04% to about $114.61, a second daily loss, as officials from Saudi Arabia, Pakistan and Turkey met Iranian leaders; markets remain wary of renewed US-Israeli strikes after the US midterms. TTF fell 1.82% to EUR 94.92/MWh but is up about a third on the month, with EU storage about 75% full, the lowest seasonal level since 2009. The Straits Daily Brief (27-October) still describes Hormuz as effectively closed, with 125 vessels holding position; Iranian claims of a four-to-five-day reopening are unverified. READ: smelter energy costs remain elevated."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Bearish","url":S_TD,
  "headline":"FED WEEK (Trading Economics, 27-October): the dollar index held near 102.04 after two sessions of gains and the US ten-year eased just below 5% to about 4.98%; markets price about 90% odds of a hold at the 27-28 October meeting and about 82% odds of a December hike, with GDP and PCE data due. READ: hawkish guidance would add to dollar and financing pressure on metals."},
]+d['news']
d['news']=d['news'][:20]

hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Mon 26-Oct':
        hitc+=1
        cat['date']='Daily, from Tue 27-Oct'
        cat['event']="3,061.5 BROKEN ON ELEVEN SETTLED OFFICIALS; THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE AND $17.00 ABOVE THE RULE-BASED CAP, RETESTED IT ON 20-OCTOBER ($2,997.00), AND HAS SINCE SETTLED $3,024.50, $3,008.00, $3,018.00 AND $3,027.00 (26-OCTOBER). A settled close beneath about 2,977.5 would break the cap on daily wave (v) and force a re-count (extended fifth or larger correction toward the 2,894 weekly 61.8%); a settled recovery above 3,077 would signal wave (v) is complete; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289. STRUCTURE: the $15.00 backwardation reversal condition was CONFIRMED on 23-October and still holds at $20.50 (26-October); a slip back below $15.00 would weaken it and a return to contango would undo it."
    elif cat['date']=='Tue 27 - Wed 28-Oct':
        hitc+=1
        cat['event']="FOMC MEETING (decision 28-October): markets price about a 90% chance of a hold and about 82% odds of a 25bp hike in December (Trading Economics, 27-October), after the hot September CPI and PPI; the US ten-year is just below 5% and the dollar index near 102. Hawkish guidance would extend the dollar and rate pressure on metals; a softer tone would ease it."
assert hitc==2,hitc
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 27-OCTOBER: the 26-October official printed a $20.50 BACKWARDATION, narrower than $25.00 but a third consecutive print beyond $15.00. Trend held at DOWN: contango remains distant ($24.50 the other way), though the narrowing is noted."
RK[0]['trend']='down'
RK[4]['risk']+=" UPDATE 27-OCTOBER: LME stock fell 1,750 t to a new series low of 234,050 t on 26-October; SMM's Chinese three-region ingot inventory ROSE 7,500 t to 419,500 t on 27-October, ending a ten-day draw. Mixed evidence: trend held at FLAT."
RK[4]['trend']='flat'
hit=0
for r in RK:
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 27-OCTOBER: Brent eased to $114.61 (-1.04%) and TTF to EUR 94.92/MWh (-1.82%) on Gulf diplomacy, but both remain near multi-year highs (Trading Economics). Trend held at UP."; hit+=1
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 27-OCTOBER: Straits Daily Brief - strait still effectively closed (4 transits on 18-October vs an 85/day baseline), 125 vessels holding position, a tanker reported disabled and a vessel fire reported on 26-October; Iranian claims of a four-to-five-day reopening are unverified. Trend held at UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 27-OCTOBER: decision due 28-October; markets price about 90% odds of a hold and about 82% odds of a December hike (Trading Economics); US ten-year about 4.98%. Trend held at UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('THE EX-CHINA RESTART PIPELINE'):
        r['risk']+=" UPDATE 27-OCTOBER: SMM (26-October) reports Alba lines 4-6 running with operating capacity near 1.3 Mt and China's September anode exports up 39.75% y/y on ex-China restarts. Trend held at UP."; hit+=1; r['trend']='up'
assert hit==4,hit
d['outlook']['ai_analysis'].insert(0,"TUESDAY 27-OCTOBER ON THE MONDAY 26-OCTOBER OFFICIAL: three-month rose $9.00 to $3,027.00 and cash $4.50 to $3,047.50, so the backwardation narrowed to $20.50 from $25.00 - price and spread moved in opposite directions - while staying beyond the $15.00 reversal condition for a third session; visible stock set another low (234,050 t). Scenario weights hold at 15/45/40. The supportive China signal weakened as SMM's three-region ingot stocks rose 7,500 t on 27-October, ending a ten-day draw, and SMM's anode-export data (September +39.75% y/y) and Alba's ~1.3 Mt operating rate confirm the ex-China restart that caps upside. Energy eased on Gulf diplomacy but Hormuz remains effectively closed. The Fed decision on 28-October (hold ~90%, December hike ~82%) is the next test; a settled close above 3,061.5-3,077 would add to base/bull, a backwardation below $15.00 or a break of 2,994.50 would reverse the shift.")

EWS=("REVIEWED 27-OCTOBER ON THE MONDAY 26-OCTOBER OFFICIAL: three-month settled $3,027.00, up $9.00 - a seventh settled close above the 2,994.50 low of 15-October and the highest since 13-October, well clear of the rule-based cap near 2,977.5; the sequence 2,994.50 / 3,024.50 / 3,008.00 / 3,018.00 / 3,027.00 reads as a small first leg up, a shallow pullback and a new marginal high, consistent with a completed wave (v) and an early corrective rebound. Wave (v) of C ($154.00 from the 3,148.5 wave (iv) high to 2,994.50) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged, NOT re-labelled. Base case about 55%: wave (v) ended at 2,994.50 and a corrective rebound toward 3,061.5-3,077 is under way (confirmed by a settled close above 3,077); alternate about 45%: a settled close beneath 2,977.5 forces a re-count toward 2,894. The narrower $20.50 backwardation is context, not an Elliott signal. Invalidation 3,289; confidence moderate. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED 24-OCTOBER"); assert st.startswith("REVIEWED 26-OCTOBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED 24-OCTOBER"); assert lt.startswith("REVIEWED 26-OCTOBER") and k>0
d['ew']['long_term']['writeup']="REVIEWED 27-OCTOBER (MONDAY 26-OCTOBER OFFICIAL, WEEK IN PROGRESS): three-month at 3,027.00, up $9.00 from the 3,018.00 weekly close, still in the lower part of the 2,950-3,110 zone and beneath the 3,061.5 July low; the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label. "+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="114.61",day="about $114.61 on 27-October, -1.04% (Trading Economics); second straight daily loss",
 note="REFRESHED TUESDAY 27-OCTOBER-2026 (Trading Economics): Brent fell below $115 for a second straight session as officials from Saudi Arabia, Pakistan and Turkey met Iranian leaders to ease tensions; markets remain wary of renewed US-Israeli strikes on Iran, which Washington has hinted could resume after the US midterms, and of the Saudi-Houthi fighting. Trading Economics says crude flows have recovered to roughly pre-war levels. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="94.9",day="EUR 94.92/MWh on 27-October, -1.82% (Trading Economics); up about 33% on the month",
 note="REFRESHED TUESDAY 27-OCTOBER-2026 (Trading Economics): TTF eased to EUR 94.92/MWh but stays near multi-year highs, up about 33% on the month; EU storage is about 75% full, the lowest seasonal level since 2009 (Germany just over 61%). Drivers cited: continued attacks on Hormuz shipping and Persian Gulf LNG flows far below year-ago, colder weather, unplanned Norwegian outages and Europe-Asia competition for LNG. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="102.04",day="102.04 on 27-October, about +0.02% (Trading Economics); up 0.83% on the month",
 note="REFRESHED TUESDAY 27-OCTOBER-2026 (Trading Economics): the dollar index held near 102 after two sessions of gains ahead of the Fed decision; markets price about 90% odds of a hold this week and about 82% odds of a December hike, with GDP and PCE data due; safe-haven demand on fears of renewed US strikes on Iran is also cited. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="4.98",day="about 4.98% on 27-October, -1bp; just below 5% at one-month lows (Trading Economics)",
 note="REFRESHED TUESDAY 27-OCTOBER-2026 (Trading Economics): the yield edged below 5% on 26-October, extending a three-week decline to one-month lows; the Fed is expected to hold, with attention on whether guidance points to a December hike; lower oil eased inflation worries. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.11910',day="LME fixing on 26-October, unchanged from 1.11910; ECB fixing 1.11880, BFIX 1.11890",
 note="REFRESHED TUESDAY 27-OCTOBER-2026 to the 26-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE MONDAY 26-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION. This Tuesday 27-October run is compiled about 02:45 London, BEFORE the ring, so Tuesday's official (13:20 London) has not printed. Reference and electronic-close prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (27-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 26-October session, and the per-metal aluminium daily table's newest row is 26-October (cash 3,047.50, three-month 3,027.00, stock 234,050) with NO later row, so the board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.11910) matches the 23-October board verified on 24-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 23-October, and match the German page's change column: aluminium -1,750 to 234,050; copper -775 to 272,975; nickel -732 to 279,942; zinc -75 to 166,950; lead -3,525 to 318,650.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (26-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (eighteen sessions, 01- to 26-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,027.00; THE STOCK CHART AXIS FLOOR WAS LOWERED THIS RUN FROM 225,000 t TO 220,000 t, pre-emptively, because visible stock at 234,050 t had only about 9,000 t of headroom.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,047.50 against three-month $3,027.00 is therefore a $20.50 BACKWARDATION, narrower than $25.00 on 23-October - the spread softened while the flat price rose, the two moving in opposite directions."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 26-October official cash of $3,047.50, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $114.61), the dollar index (102.04), TTF (EUR 94.92/MWh) and the US ten-year (about 4.98%) are Trading Economics readings shown on 27-October; Trading Economics prices are contract-for-difference references, not official benchmarks, so they are approximate; EUR/USD is the 26-October LME fixing, the same session as the board. The Straits Daily Brief (27-October) shows Brent at $115.15 at 00:12 UTC - a different time stamp, cited in text only."; hit+=1
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 27-OCTOBER: no authorised fetch was blocked for the board (Westmetall EN, DE and per-metal pages all fetched). AL Circle's news index and mining.com search returned HTTP 403 and metal.com's English mirror returned HTTP 500; per the fallback, a web search was used and the same SMM articles were read on news.metal.com. A Trading Economics remark linking dollar strength to a specific company's IPO filing was not verified and is not used. Hormuz items from Iranian, Houthi-run or single-source outlets in the Straits Daily Brief are cited as reported, not as fact. The SMM-reported LME three-month electronic close of $3,038 on Monday is a post-official price and is NOT used on the board. No Q1-2027 Japanese premium offer has been reported yet (negotiations normally start late November); a search this run found none."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: NO NEW PEER RESULT WAS REPORTED IN THIS WINDOW. Norsk Hydro's Q3-2026 (23-October) remains the latest addition; Chalco's Q3-2026 report was searched for and not yet located (a BOC International forecast of about RMB 6.03bn net profit is a broker estimate and is NOT published as a result). NO NEW COMPANY WAS BACK-FILLED THIS RUN. Century Aluminum has not yet announced its Q3 date. Other entries are carried at their last publicly verified figures, and gaps stay gaps."; hit+=1
assert hit==4,hit
en=d['earnings_note']
d['earnings_note']=en.replace("NORSK HYDRO REPORTED Q3-2026 ON 23-OCTOBER (added this run):","NORSK HYDRO REPORTED Q3-2026 ON 23-OCTOBER (added 24-October; no newer peer result to 27-October):",1)

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 26-OCTOBER: no newer public disclosure","REVIEWED 27-OCTOBER: no newer public disclosure").replace("REVIEWED 26-OCTOBER. NO NEW DATED","REVIEWED 27-OCTOBER. NO NEW DATED")
    return o
PS={p['name']:p for p in d['producer_status']}
a=PS['Aluminium Bahrain (ALBH)']; pre="REVIEWED 26-OCTOBER: no newer public disclosure located; status below carried. "; assert a['update'].startswith(pre)
a['update']=("UPDATED 27-OCTOBER (SMM, 26-October): SMM's anode-export analysis again states Alba has resumed production at lines 4-6 with operating capacity recovering to about 1.3 million tonnes, that lines 1-3 are expected to stay shut, and that total capacity is expected to reach 1.6 million tonnes once the Aluminium Dunkerque acquisition completes (as reported by SMM; not an Alba disclosure). ")+a['update'][len(pre):]
a['src']=[L_AN,S_AN]
c=PS['China operators (aggregate, incl. Chalco and Hongqiao)']
c['update']="UPDATED 27-OCTOBER (SMM, 27-October): three-region aluminium ingot social inventory rose 7,500 t to 419,500 t, ending a ten-working-day destocking run; billet inventory flat at about 89,500 t. "+c['update']
c['src']=[L_IN,S_IN]
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD
for s_ in [[L_TE,S_TE],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG],[L_MM,S_MM],[L_IN,S_IN],[L_AN,S_AN],[L_ST,S_ST]]:
    d['sources'].append(s_)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 26-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 23-Oct)",W])
for x in ([L_IN,S_IN],[L_AN,S_AN],[L_TD,S_TD],[L_ST,S_ST]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-23'
ph['rows'].append(['2026-10-26',cash,m3,stk]); ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
