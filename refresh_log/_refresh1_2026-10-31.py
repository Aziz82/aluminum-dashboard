# Daily data refresh - 2026-10-31 (SATURDAY, ~02:40 UTC). No LME ring on Saturday: board ROLLED to FRIDAY 30-Oct LME official (last trading session; also the weekly close).
# Westmetall cache-busted EN and DE overviews both fetched and agree on the full 30-Oct session; Al per-metal table top row = 30-Oct with NO later row.
# Completeness: 5/5 stock lines reconcile vs 29-Oct board; prior FX column (MTLE 1.11280) matches 29-Oct board.
# Key: Al cash 3,114.00 (+43.00), 3M 3,080.00 (+16.00) -> WEEKLY CLOSE ABOVE 3,077; BACKWARDATION WIDENED to $34.00 (above the $15 trigger) - spread and price moved in the SAME direction (both stronger).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-31'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (30/31-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (30-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield, December hike pricing (30-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index, tech sell-off and FedWatch odds (30-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF above EUR 100/MWh (30-Oct-2026)"
S_ST="https://straits.live/briefs/2026-10-31"; L_ST="Straits Daily Brief - Strait of Hormuz, 31-Oct-2026"
S_SMM="https://news.metal.com/"; L_SMM="SMM news feed - ex-China October aluminium output -1.2% y/y, November expected positive; bonded-zone selling; Chinese cost inputs seen rising (30/31-Oct-2026)"
S_YA="https://www.alcircle.com/news/yunnan-aluminium-s-net-income-surges-164-to-1-74b-in-nine-months-121774"; L_YA="AL Circle - Yunnan Aluminium nine-month net income surges 164% (31-Oct-2026)"
S_AM="https://www.alcircle.com/news/amag-groups-revenue-climbs-16-4-to-1-4b-as-nine-month-ebitda-jumps-59-121760"; L_AM="AL Circle - AMAG Group nine-month EBITDA up 59% (30-Oct-2026)"
S_RG="https://www.alcircle.com/news/rusal-targets-ghana-s-massive-bauxite-reserves-with-a-5mt-mining-plan-121770"; L_RG="AL Circle - Rusal and GIADEC plan 5 Mt bauxite mine and 1.2 Mt alumina refinery in Ghana (30-Oct-2026)"
S_NA="https://www.alcircle.com/news/north-american-aluminum-demand-rises-3-5-in-h1-2026-as-imports-offset-domestic-supply-decline-121773"; L_NA="AL Circle - North American aluminium demand +3.5% in H1-2026 (30-Oct-2026)"
S_EG="https://www.alcircle.com/news/hindalco-vedanta-nalco-shares-fall-as-ega-restarts-al-taweelah-smelter-aluminium-prices-seen-at-2-800-t-in-cy27-121687"; L_EG="AL Circle - Indian aluminium shares fall as EGA restarts Al Taweelah (631 of 1,262 cells) (26-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
assert B['LME Cash settlement']['cur']==3071.0 and B['LME 3-month']['cur']==3064.0
cash,prev_c,m3,prev_m,stk,prev_s=3114.0,3071.0,3080.0,3064.0,231200,231675
spr=cash-m3; assert spr==34.0 and prev_s-475==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED SATURDAY 31-OCTOBER-2026. THERE IS NO LME RING ON SATURDAY, SO THE BOARD IS THE FRIDAY 30-OCTOBER-2026 LME OFFICIAL - THE LAST TRADING SESSION AND THE WEEKLY CLOSE; the next official prints Monday 02-November 13:20 London. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 30-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.11770); their prior-day FX column (MTLE 1.11280) matches the verified 29-October board, and the per-metal aluminium table's newest row is 30-October with NO later row, so the board is complete rather than lagging; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 29-October (and match the pages' change column): aluminium 231,675 less 475 to 231,200; copper 272,200 plus 1,800 to 274,000; nickel 278,790 less 552 to 278,238; zinc 162,675 less 1,400 to 161,275; lead 311,525 less 150 to 311,375. "
 "The whole board sits on ONE UNIFORM SESSION (30-October); prior-month averages remain the completed SEPTEMBER-2026 official means (October's means complete with this session and roll in on the first November run).")
AL=(" CASH SETTLED $3,114.00 ON THE 30-OCTOBER OFFICIAL, UP $43.00 OR 1.40% FROM $3,071.00. THREE-MONTH SETTLED $3,080.00, UP $16.00 OR 0.52% FROM $3,064.00 - BACK ABOVE 3,077 BY $3.00 and the FIRST WEEKLY CLOSE ABOVE THE 3,077 WEEKLY 50% RETRACEMENT, up $62.00 on the week from the 3,018.00 weekly close; $69.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%) and $85.50 above the 2,994.50 settled low of 15-October. "
 "THE BACKWARDATION WIDENED TO $34.00 FROM $7.00 because cash rose more than three-month - SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION (both stronger) - the widest backwardation since at least mid-September and back ABOVE the published $15.00 reversal condition. "
 "VISIBLE LME STOCK FELL 475 t TO 231,200 t, another new series low and an eighth straight draw. The Trading Economics aluminium CFD reference showed about $3,059.70 (-0.38%) on 30-October, a later-in-day reference BELOW the official - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,114.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,080.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $3.00 ABOVE THE 3,077 WEEKLY 50% RETRACEMENT on the weekly close, $18.50 above the 3,061.5 July low, $68.50 beneath the 3,148.5 wave (iv) high and $209.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for an eleventh session."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+34.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,114.00 against three-month $3,080.00 is a $34.00 BACKWARDATION, WIDER than 29-October's $7.00 as cash rose $43.00 and three-month $16.00 - SPREAD AND PRICE MOVED TOGETHER (both stronger). It is BACK ABOVE the published $15.00 reversal condition and the widest print in the series shown since 16-September, a twelfth straight backwardation; a contango beyond $24.50 would reverse the structural signal. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"231,200","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 475 t TO 231,200 t, another new series low and an eighth straight draw. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{abs(sep_c-cash):,.2f} "+("beneath" if cash<sep_c else "above")+" it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,080.00, UP $16.00 - back above 3,077 on the weekly close, $18.50 above 3,061.5 and $69.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${abs(sep_m-m3):,.2f} "+("below" if m3<sep_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 475 t TO 231,200 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":7.0,"avg":sep_sp,"note":VER+f" A $34.00 BACKWARDATION, WIDER THAN 29-OCTOBER'S $7.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Cash rose $43.00 and three-month $16.00, so the structure firmed WITH the flat price this session. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October at $14.00, regained 28-October at $17.00, lost 29-October at $7.00, REGAINED 30-October at $34.00."},
 {"name":"EUR/USD LME fixing","cur":1.1177,"prev":1.1128,"avg":1.1465,"note":VER+" THE LME EURO FIXING ROSE TO 1.11770 FROM 1.11280 at the Friday ring; the ECB fixing printed 1.11720 and BFIX 1.11756. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (30-Oct official)","price":"3,114.0","basis":"THE 30-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,114.00, UP $43.00 OR 1.40%. No ring on Saturday; next official Monday 02-November 13:20 London."},
 {"tenor":"3-month (30-Oct official)","price":"3,080.0","basis":"THE 30-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,080.00, UP $16.00 - the weekly close, $3.00 above 3,077, $85.50 above the 2,994.50 October low and $69.50 above the 02-January official."},
 {"tenor":"Cash-to-3M structure","price":"+34.0 (BACKWARDATION)","basis":"A $34.00 BACKWARDATION, widened from $7.00 with price - back above the $15.00 reversal condition."},
 {"tenor":"Visible LME stock","price":"231,200 t","basis":f"DOWN 475 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("PRICE AND STRUCTURE RE-FIRMED TOGETHER INTO THE WEEKLY CLOSE. On the 30-October official cash $3,114.00 sits $34.00 ABOVE three-month $3,080.00, a BACKWARDATION, wider than $7.00 on 29-October because cash rose $43.00 and three-month $16.00 - SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION (both stronger). "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00 and now $34.00. "
 f"READ: a twelfth straight backwardation, the widest in this sequence, with visible stock at another low (231,200 t), so prompt metal is valued clearly over forward metal into month-end; the signal has flipped above and below $15.00 four times in six sessions, so persistence on Monday matters. The September mean spread was ${sep_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]
d['chart_stock_axis']=[220000,255000]

ls=d['lme_series']; assert ls[-1][0]=='29-Oct', ls[-1]
d['lme_series']=ls[1:]+[["30-Oct",cash,m3,stk]]
assert all(220000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
# (cash, 3M, prev cash, prev 3M)
CU=(14449.0,14250.0,14560.0,14350.0); NI=(15240.0,15425.0,15360.0,15550.0); ZN=(3955.5,3890.0,3980.0,3880.0); PB=(1890.0,1920.0,1878.0,1909.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average: 21 sessions to 29-Oct + 30-Oct = 22 (October now complete)
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0,3736.0,3771.0,3727.0,3790.0,3900.0,3927.0,3960.0,3980.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0,1851.0,1880.0,1872.0,1886.0,1900.0,1900.0,1910.0,1878.0]
assert len(zs)==21 and len(ps)==21
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/22)/(sum(zs)/21),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/22)/(sum(ps)/21),1)
print('Oct zn avg',(sum(zs)+ZN[0])/22,'pb avg',(sum(ps)+PB[0])/22)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-30'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending FRIDAY 30-OCTOBER-2026 (no ring on Saturday; next official Monday 02-November). THE WINDOW ROLLED THIS RUN: 09-October dropped and 30-October appended, so the window is 12-October to 30-October. Every point is an official cash settlement; the 30-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 29-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (30-October-2026 session; stock lines reconciled against 29-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,449.00, down $111.00 or 0.76%; three-month $14,250.00, down $100.00 or 0.70%. BACKWARDATION $199.00 from $210.00 - narrowing with price (spread and price in the SAME direction), still the tightest prompt structure on the board. Stock ROSE 1,800 tonnes to 274,000 t, the only build on the board for a second session."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,240.00, down $120.00 or 0.78%; three-month $15,425.00, down $125.00 or 0.80%. CONTANGO narrowed slightly to $185.00 from $190.00, still the widest carry on the board. Stock fell 552 tonnes to 278,238 t."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,955.50, down $24.50 or 0.62%; three-month $3,890.00, up $10.00 or 0.26%. BACKWARDATION narrowed to $65.50 from $100.00 - three-month rose while the spread narrowed (spread and outright in OPPOSITE directions). Stock fell 1,400 tonnes to 161,275 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,890.00, up $12.00 or 0.64%; three-month $1,920.00, up $11.00 or 0.58%. CONTANGO $30.00, about unchanged from $31.00. Stock drew 150 tonnes to 311,375, a thirtieth consecutive draw."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Friday 30-October official (the weekly close) aluminium led: aluminium three-month +0.52%, lead +0.58%, zinc +0.26%, copper -0.70%, nickel -0.80%. Stocks fell for four metals; copper built 1,800 t. Trading Economics (30-October) reports the dollar index near 102 after a tech-led flight to safety, the US ten-year near 4.93% (near seven-week lows) and December-hike odds easing to about 72% (CME FedWatch) from about 83% a day earlier. The LME euro fixing rose to 1.1177.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='29-Oct'
        i['hist']=i['hist'][1:]+[["30-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,250.00 (3M); 14,449.00 (cash) $/t"
        i['ratio']="~14,449.00 $/t cash vs LME 3M 14,250.00 $/t"
        i['trend']='down'
        i['src']=("LME official cash settlement, rolled to the FRIDAY 30-OCTOBER-2026 session at $14,449.00, DOWN $111.00 or 0.76% against $14,560.00. THE WINDOW ROLLED THIS RUN: 09-October dropped and 30-October appended, so the series is the last fifteen published official cash sessions, 12-October to 30-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 29-October). "
                  "Copper structure for context: backwardation $199.00 (from $210.00), stock rose 1,800 t to 274,000 t.")
s=d['inputs_summary']; j=s.find("UPDATE 30-OCTOBER"); s=s[j:] if j>=0 else s
d['inputs_summary']=("UPDATE 31-OCTOBER: Copper rolled to the Friday 30-October LME official cash of $14,449.00, down $111.00, with its fifteen-session window moved to 12-October to 30-October. No new monthly carbon settlement is due until mid-November, and no new dated SMM fluoride, silicon or magnesium mark was located (an SMM item on 30/31-October says Chinese auxiliary-material and electricity prices are expected to rise, pushing domestic smelting costs higher, but its article page returned 404 and no figure is used), so no other hist mark was appended. "
 "Energy firmed further: European gas rose above EUR 100/MWh for the first time since late 2022 (about EUR 103.6-104.0, +5.8-6.2%, up about 40% on the month, Trading Economics 30-October) with EU storage 74.89% full on 29-October; Brent about $112.3-113.4 (+1.4-2.4%, page internally inconsistent). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
otl=0.5*3071.0; ores=2403-otl; osh=otl/2403*100
OLDT=f"the tariff leg of the US duty-paid premium is 0.50 times the 29-October official cash of $3,071.00, or ${otl:,.2f}, DOWN $15.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${ores:,.2f}, so {osh:.1f}%"
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 30-October official cash of $3,114.00, or ${tl:,.2f}, UP $21.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED FRIDAY 30-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE THURSDAY 29-OCTOBER OFFICIAL)."; NEWC="COMPILED SATURDAY 31-OCTOBER-2026 (NO RING ON SATURDAY) (LME BOARD ON THE FRIDAY 30-OCTOBER OFFICIAL)."
n=0; nc=0
for p in d['premiums']:
    n+=p['src'].count(OLDT); nc+=p['src'].count(OLDC); p['src']=p['src'].replace(OLDT,NEWT).replace(OLDC,NEWC)
print('premium tariff replaced',n,nc); assert n==len(d['premiums'])
ra=360.40/m3*100; na=0
o="THE RATIO: LME Alumina at $360.40/t against the 29-October aluminium three-month of $3,064.00 is 11.76%"
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    if o in s: na+=1
    a['src']=s.replace(o,f"THE RATIO: LME Alumina at $360.40/t against the 30-October aluminium three-month of $3,080.00 is {ra:.2f}%")
print('alumina',na,len(d['alumina'])); assert na==len(d['alumina'])

d['lme_commentary']=("WEEKLY CLOSE ABOVE 3,077. On the Friday 30-October official cash settled $3,114.00 (+$43.00) and three-month $3,080.00 (+$16.00), regaining 3,077 one session after losing it and closing the week $62.00 higher at the first weekly settlement above the 3,077 50% retracement. "
 "Cash led the rise, so the backwardation widened to $34.00 from $7.00 - the widest in the sequence since mid-September and back above the $15.00 reversal condition, with spread and price both stronger; visible stock fell 475 t to a new low of 231,200 t. Aluminium was among the firmer metals on the board (aluminium +0.52%, lead +0.58%, zinc +0.26%, copper -0.70%, nickel -0.80%). "
 "Macro was mixed: a tech-led sell-off pulled the US ten-year toward seven-week lows (about 4.93%) and eased December-hike odds to about 72% from about 83%, while European gas broke above EUR 100/MWh for the first time since late 2022 and Brent rose above $113 on renewed US-Iran strike concern (Trading Economics, 30-October). SMM reports ex-China October aluminium output 1.2% lower y/y but expects a return to growth in November as Middle East capacity restarts. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}. The structure has flipped across $15.00 four times in six sessions, so Monday's official is the persistence test.")
d['net_read']=("NET: THE WEEK CLOSED CONSTRUCTIVE. Supportive: three-month settled the week at $3,080.00, above the 3,077 weekly 50% retracement for the first time, the backwardation widened to $34.00 (twelfth straight session), visible LME stock fell to another low of 231,200 t, European gas broke above EUR 100/MWh and Brent neared four-year highs (keeping the smelter cost floor high), Hormuz stays an active maritime emergency, and December-hike odds eased to about 72%. "
 "Against: the breakout margin is only $3.00 and the structure has flipped across $15.00 four times in six sessions; ex-China supply is recovering (SMM expects November ex-China output to turn positive y/y; EGA has restarted half of Al Taweelah), Chinese output is near record, and the Trading Economics CFD reference traded below the official later on Friday.")
d['bottom_line']=("BOTTOM LINE: on the Friday 30-October LME official - the weekly close - aluminium three-month rose $16.00 to $3,080.00 and cash $43.00 to $3,114.00, regaining 3,077 one session after losing it, while the backwardation widened to $34.00, back above the $15.00 tightness trigger, and visible stock fell to a new low of 231,200 t. "
 "Scenario weights are held at 20% bull / 45% base / 35% bear: the bull trigger was already credited on the 28-October close and the margin above 3,077 is thin; a SECOND consecutive settled close above 3,077 with the backwardation still beyond $15.00 (Monday 02-November) would move five points from bear to bull, and a close below 3,061.5 would return five to bear. The daily Elliott count keeps wave (v) of the C-wave decline complete at 2,994.50 (base case restored to about 65%); invalidation 3,289. The weekly count gets its first sign that the larger correction may end early, but the corrective path toward 2,894 is not yet voided.")
c2=d['commercial']
for a,b in [("FIRST, PRICE AND PROMPT PREMIUM EASED TOGETHER: a $7.00 backwardation on 29-October, narrower than $17.00 as cash fell $30.00 and three-month $20.00 - back below the $15.00 reversal condition one session after regaining it, so nearby metal is still valued over forward metal and there is still no carry reward for deferring purchases, but the prompt tightness signal has softened again.",
             "FIRST, PRICE AND PROMPT PREMIUM FIRMED TOGETHER INTO THE WEEKLY CLOSE: a $34.00 backwardation on 30-October, wider than $7.00 as cash rose $43.00 and three-month $16.00 - back above the $15.00 reversal condition and the widest in the sequence since mid-September, so nearby metal is valued clearly over forward metal and there is no carry reward for deferring purchases; the signal has flipped four times in six sessions, so persistence matters."),
 (f"is ${otl:,.2f} on 29-October cash, {osh:.1f}% of the $2,403/t premium",f"is ${tl:,.2f} on 30-October cash, {share:.1f}% of the $2,403/t premium"),
 ("the 29-October official took three-month back to $3,064.00, $13.00 below 3,077 after one close above it and $2.50 above 3,061.5; energy stays elevated (European gas EUR 99.85/MWh, Brent about $112-116 depending on source, 30-October); after the Fed's 28-October hold, strong Q3 GDP (3.4%) and September PCE (3.6%) put December-hike odds near 83% (Trading Economics);",
  "the 30-October official took three-month to $3,080.00, the first weekly close above 3,077, $85.50 above the 2,994.50 settled low; energy firmed further (European gas above EUR 100/MWh for the first time since late 2022, Brent above $113, 30-October); December-hike odds eased to about 72% after a tech-led bond rally (Trading Economics, CME FedWatch);")]:
    assert a in c2,a; c2=c2.replace(a,b)
d['commercial']=c2

pre_end="would return five points to bear. "
for s in d['outlook']['scenarios']:
    assert s['drivers'].startswith("HELD 30-OCTOBER"); k=s['drivers'].find(pre_end); assert k>0
    s['drivers']=("HELD 31-OCTOBER at 20/45/35: the Friday 30-October official (weekly close) regained 3,077 (three-month $3,080.00, +$16.00) and the backwardation widened back above the $15.00 trigger to $34.00 with stock at another low - supportive, but the first close above 3,077 was already credited on 28-October and the margin is only $3.00, so no weight moves this run. PRE-REGISTERED: a SECOND consecutive settled close above 3,077 with the backwardation beyond $15.00 (Monday 02-November) moves five points from bear to bull (25/45/30); a settled close below 3,061.5 returns five points to bear. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium closed the week back above its $3,077 pivot: Friday's LME official lifted three-month $16 to $3,080 and cash $43 to $3,114, widening the backwardation to $34 - the tightest prompt signal since mid-September - as LME stock fell to another low and European gas broke above EUR 100/MWh.",
 "points":[
 "WHAT MOVED: Friday's LME official (the weekly close) settled cash at $3,114.00 (+$43.00) and three-month at $3,080.00 (+$16.00, +0.52%), up $62 on the week. Cash now trades $34.00 above three-month (backwardation), up from $7.00, and LME stock fell 475 t to a new low of 231,200 t. Aluminium outperformed copper and nickel, which fell.",
 "WHY: prompt metal is scarce on the LME (eight straight stock draws), and the smelter cost floor rose again - European gas topped EUR 100/MWh for the first time since late 2022 and Brent rose above $113 on renewed US-Iran strike concern (Trading Economics). December-hike odds eased to about 72% from about 83% as a tech sell-off pulled bond yields lower.",
 "AGAINST: the close is only $3 above $3,077 and the spread has crossed the $15 tightness line four times in six sessions; SMM expects ex-China output to return to year-on-year growth in November as Middle East capacity restarts, and Chinese output stays near record.",
 "WHAT TO WATCH: Monday's official - a second close above $3,077 with the backwardation above $15 would strengthen the bullish case, a close below $3,061.5 would weaken it; Chalco's Q3 report (still not located); Hormuz incidents (Iranian claims of tanker fires remain unconfirmed)."]}

d['feed']=([
 {"when":"Sat 31-Oct","impact":"Bullish","text":"BOARD ROLLED TO THE FRIDAY 30-OCTOBER LME OFFICIAL (WEEKLY CLOSE; NO RING ON SATURDAY): cash $3,114.00 (+$43.00), three-month $3,080.00 (+$16.00), back above 3,077 - the first weekly close above it; stock -475 t to a new low of 231,200 t."},
 {"when":"Sat 31-Oct","impact":"Bullish","text":"STRUCTURE FIRMER: the cash-to-three-month backwardation widened to $34.00 from $7.00, back above the $15.00 reversal condition - spread and price both stronger."},
 {"when":"Fri 30-Oct","impact":"Bullish (cost)","text":"ENERGY: European gas TTF above EUR 100/MWh for the first time since late 2022 (about EUR 103.6-104.0, +5.8-6.2%; EU storage 74.89%); Brent above $113 on US-Iran strike concern (Trading Economics)."},
 {"when":"Fri 30-Oct","impact":"Mixed","text":"MACRO: tech-led sell-off pulled the US ten-year toward seven-week lows (about 4.93%); December-hike odds eased to about 72% (CME FedWatch via Trading Economics); dollar index near 102."},
 {"when":"Fri 30-Oct","impact":"Bearish","text":"SMM: ex-China primary aluminium output fell 1.2% y/y in October but daily output rose 1.6% m/m; November expected to turn positive (+0.2% y/y) as new capacity and Middle East restarts ramp."},
 {"when":"Sat 31-Oct","impact":"Bullish (margin)","text":"PEER EARNINGS: Yunnan Aluminium nine-month net income CNY 11.6bn (+164% y/y); AMAG nine-month EBITDA EUR 181m (+59%), full-year guidance EUR 200-220m (AL Circle)."},
 {"when":"Sat 31-Oct","impact":"Mixed","text":"HORMUZ: Straits Daily Brief - an active maritime emergency; IMF PortWatch 2 transits on 25-October vs an 85/day baseline; Oman rescued 25 from a burning tanker (Al Jazeera); Iranian claims of four tanker fires are unconfirmed by any maritime authority."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM CLOSES THE WEEK ABOVE 3,077. The Friday 30-October official settled cash at $3,114.00 (+1.40%) and three-month at $3,080.00 (+0.52%), regaining 3,077 one session after losing it - the first weekly settlement above the 3,077 50% retracement, up $62.00 on the week. Visible stock fell 475 t to a new low of 231,200 t. Board: lead three-month +0.58%, aluminium +0.52%, zinc +0.26%, copper -0.70%, nickel -0.80%; copper built 1,800 t, the only stock build."},
 {"theme":"LME","horizon":"0-1 month","impact":"Bullish","url":W,
  "headline":"THE CURVE FIRMED WITH PRICE: the cash-to-three-month backwardation widened to $34.00 from $7.00 on 30-October, the widest in the sequence since mid-September and back above the $15.00 reversal condition, because cash rose more than three-month into month-end. READ: a twelfth straight backwardation, but the signal has crossed $15.00 four times in six sessions."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish (cost)","url":S_TG,
  "headline":"EUROPEAN GAS TOPS EUR 100/MWh (Trading Economics, 30-October): TTF rose about 6% to roughly EUR 103.6-104.0/MWh, the first time above EUR 100 since late 2022 and about 40% higher on the month; EU storage was 74.89% full on 29-October (Germany 61.65%, Netherlands 65.53%), about 100 TWh below last year, with Gulf LNG deliveries cut by Hormuz disruption and colder forecasts. Brent rose above $113, near the $116.72 four-year high of 23-October, on reports of US strike options against Iran and two tanker incidents in Hormuz. READ: the smelter energy-cost floor rose again."},
 {"theme":"Macro","horizon":"0-2 months","impact":"Mixed","url":S_TY,
  "headline":"HIKE ODDS EASE ON TECH SELL-OFF (Trading Economics, 30-October): weak results from major tech firms triggered a flight to safety that pulled the US ten-year toward seven-week lows (about 4.93%); CME FedWatch December-hike odds eased to about 72% from nearly 83% on 29-October; the dollar index held near 102, up about 0.5% in October."},
 {"theme":"Supply","horizon":"0-3 months","impact":"Bearish","url":S_SMM,
  "headline":"EX-CHINA OUTPUT TO TURN POSITIVE (SMM feed, 30/31-October): October primary aluminium output outside China fell 1.2% y/y while average daily output rose 1.6% m/m; SMM expects November to return to positive y/y growth (+0.2%) on new capacity and production resumptions. SMM separately notes active buying but weak demand in the ex-China ingot market and rising selling from China's bonded zones. (Article pages returned 404; figures are from the feed summaries.)"},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Bullish (margin)","url":S_YA,
  "headline":"YUNNAN ALUMINIUM NINE-MONTH PROFIT +164% (AL Circle, 31-October): revenue CNY 52.61bn (+19.4% y/y from CNY 44.07bn); net income CNY 11.6bn (+164% from CNY 4.39bn); basic EPS CNY 3.35 (from CNY 1.27). Q3 standalone figures and output were not given in the source."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Bullish","url":S_AM,
  "headline":"AMAG NINE-MONTH EBITDA +59% (AL Circle, 30-October): 9M-2026 revenue EUR 1.3bn (+16.4%), EBITDA EUR 181m (from EUR 114m), net income EUR 82m (from EUR 34m), shipments 342,900 t (+7%); Q3 revenue EUR 473m (+35%), EBITDA EUR 80m on shipments of 121,500 t (+21%, including about 9,000 t carried over from Q2). Free cash flow was an outflow of EUR 67m; full-year EBITDA guidance EUR 200-220m."},
 {"theme":"Demand","horizon":"0-6 months","impact":"Mixed","url":S_NA,
  "headline":"NORTH AMERICAN DEMAND +3.5% IN H1-2026 (AL Circle, 30-October): demand grew 3.5% while domestic supply declined, with imports filling the gap - consistent with a tariff-inflated US Midwest premium that still has to attract imported metal."},
 {"theme":"Bauxite/Alumina","horizon":"Long-term","impact":"Bearish","url":S_RG,
  "headline":"RUSAL AND GHANA'S GIADEC PLAN A 5 Mt/yr BAUXITE MINE AND 1.2 Mt/yr ALUMINA REFINERY (AL Circle, 30-October) - a long-dated addition to ex-China raw-material supply; no timeline or financing is confirmed in the source."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Mixed","url":S_ST,
  "headline":"HORMUZ REMAINS AN ACTIVE MARITIME EMERGENCY (Straits Daily Brief, 31-October): IMF PortWatch shows 2 transits on 25-October against an 85/day baseline; Al Jazeera reports Oman rescued 25 people from a burning tanker; Iranian claims of four tanker fires, a second captured US drone and a destroyed unmanned vessel are UNCONFIRMED. The brief's oil-price feed had no print, so no Brent level is taken from it."},
]+d['news']
d['news']=d['news'][:20]

hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Fri 30-Oct':
        hitc+=1
        cat['date']='Daily, from Mon 02-Nov'
        cat['event']="3,077 CLEARED 28-OCTOBER ($3,084.00), LOST 29-OCTOBER ($3,064.00) AND REGAINED ON THE 30-OCTOBER WEEKLY CLOSE ($3,080.00); THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE, RETESTED IT ON 20-OCTOBER ($2,997.00), AND HAS SINCE SETTLED $3,024.50, $3,008.00, $3,018.00, $3,027.00, $3,064.00, $3,084.00, $3,064.00 AND $3,080.00. A SECOND consecutive settled close above 3,077 (Monday 02-November) with the backwardation beyond $15.00 would confirm that wave (v) is complete and move five scenario points to bull; next resistance 3,110 then the 3,148.5 wave (iv) high - above 3,148.5 the C wave is complete and above 3,183 the impulsive labelling void. A settled close beneath 3,061.5 would weaken the rebound and return five scenario points to bear, and beneath about 2,977.5 would force a re-count toward the 2,894 weekly 61.8%. Invalidation 3,289. STRUCTURE: the $15.00 backwardation reversal condition was regained on 30-October at $34.00. MONTH ROLL: October's official means complete with the 30-October session and replace September's in the average columns on the first November run."
assert hitc==1,hitc
for cat in d['outlook']['catalysts']:
    if cat['date']=='Fri 30-Oct (pending)':
        cat['date']='Late Oct / early Nov (pending)'
        cat['event']="CHALCO Q3-2026 RESULTS - STILL PENDING: searches on 31-October (English and Chinese) again did not locate a Q3-2026 release; only a broker estimate (BOC International, 26-October) was found, which is NOT published as a result. Yunnan Aluminium's nine-month report (net income +164%) is the first large Chinese smelter print located. Hydro and Alcoa Q3 prints both showed smelting margin intact and alumina margin compressed; Chalco, the world's largest alumina producer, is the next test of that split."
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 31-OCTOBER: the 30-October official printed a $34.00 BACKWARDATION, back ABOVE the $15.00 reversal condition and the widest in the sequence since mid-September, as cash outpaced three-month and stock fell to another low. Trend moved from FLAT to DOWN: contango is $34.00 away, though the spread has crossed $15.00 four times in six sessions."
RK[0]['trend']='down'
RK[4]['risk']+=" UPDATE 31-OCTOBER: LME stock fell 475 t to a new series low of 231,200 t on 30-October, an eighth straight draw. Trend held at FLAT (the draw pace is slow, about 4,600 t over eight sessions)."
RK[4]['trend']='flat'
hit=0
for r in RK:
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 31-OCTOBER: TTF broke above EUR 100/MWh for the first time since late 2022 (about EUR 103.6-104.0, +6%, +40% on the month) with EU storage at 74.89%; Brent above $113 on US-Iran strike concern (Trading Economics, 30-October). Trend held at UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 31-OCTOBER: Straits Daily Brief - an active maritime emergency (IMF PortWatch: 2 transits on 25-October vs an 85/day baseline); Oman rescued 25 from a burning tanker (Al Jazeera); Iranian claims of four tanker fires, a captured US drone and a destroyed unmanned vessel are UNCONFIRMED. Trend held at UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 31-OCTOBER: December-hike odds eased to about 72% (CME FedWatch via Trading Economics, 30-October) from nearly 83% a day earlier as a tech-led sell-off pulled the ten-year toward seven-week lows near 4.93%; still a majority priced for a hike. Trend held at UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('THE EX-CHINA RESTART PIPELINE'):
        r['risk']+=" UPDATE 31-OCTOBER: SMM expects ex-China primary output to return to positive y/y growth in November (+0.2%) after -1.2% in October, on new capacity and resumptions; EGA has restarted 631 of 1,262 Al Taweelah cells (AL Circle, 26-October). Trend held at UP."; hit+=1; r['trend']='up'
assert hit==4,hit
d['outlook']['ai_analysis'].insert(0,"SATURDAY 31-OCTOBER ON THE FRIDAY 30-OCTOBER OFFICIAL (WEEKLY CLOSE): three-month rose $16.00 to $3,080.00 and cash $43.00 to $3,114.00, regaining 3,077 one session after losing it and closing the week $62.00 higher, while the backwardation widened to $34.00 - back above the $15.00 reversal condition and the widest since mid-September - and visible stock fell to another low (231,200 t). Weights are held at 20/45/35 because the 3,077 trigger was already credited on 28-October and the margin is $3.00; a second consecutive close above 3,077 with the backwardation beyond $15.00 moves five points to bull. Energy is the strongest supportive input this week (TTF above EUR 100/MWh, Brent above $113), while easing December-hike odds (about 72%) removed some macro pressure; ex-China supply recovery (SMM: November output to turn positive) is the main offset.")

EWS=("REVIEWED 31-OCTOBER ON THE FRIDAY 30-OCTOBER OFFICIAL: three-month settled $3,080.00, up $16.00 - an eleventh settled close above the 2,994.50 low of 15-October and BACK ABOVE 3,077, $18.50 above 3,061.5. The sequence 2,994.50 / 3,024.50 / 3,008.00 / 3,018.00 / 3,027.00 / 3,064.00 / 3,084.00 / 3,064.00 / 3,080.00 reads as the first leg of a corrective rebound from a completed wave (v) of C, with 3,064.00 a higher low inside it; neither 3,084.00 nor 3,064.00 is yet a confirmed pivot. Wave (v) ($154.00 from the 3,148.5 wave (iv) high to 2,994.50) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged, NOT re-labelled; base case restored to about 65%: wave (v) ended at 2,994.50 and the rebound extends toward 3,110 then the 3,148.5 wave (iv) area; alternate about 35%: the 3,064-3,084 range is the top of a minor corrective bounce, a settled close beneath 3,061.5 reopens the low, and a close beneath 2,977.5 forces a re-count toward 2,894. Invalidation 3,289; confidence moderate. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED 24-OCTOBER"); assert st.startswith("REVIEWED 30-OCTOBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED 24-OCTOBER"); assert lt.startswith("REVIEWED 30-OCTOBER") and k>0
d['ew']['long_term']['writeup']="REVIEWED 31-OCTOBER (FRIDAY 30-OCTOBER OFFICIAL = WEEKLY CLOSE): three-month closed the week at 3,080.00, up $62.00 from the 3,018.00 weekly close and $3.00 ABOVE the 3,077 50% retracement - the first weekly close above it and the first sign the larger correction may be ending early, but by a thin margin inside the 2,950-3,110 zone. The corrective count toward the 61.8% retracement at 2,894 is NOT voided and is NOT re-labelled; it would lose preference on a weekly close above 3,110, and is reinforced by a weekly close back below 3,061.5. Weekly base case about 55% corrective toward 2,894 / 45% correction ending early; confidence low-to-moderate. "+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="113.4",day="about $112.33-113.43 on 30-October, +1.4-2.4% on the day (Trading Economics; page sections differ); +10.9% on the month",
 note="REFRESHED SATURDAY 31-OCTOBER-2026 (Trading Economics, 30-October): Brent rose above $113, nearing the $116.72 four-year high of 23-October, on reports that a senior US commander briefed the president on options for renewed strikes on Iran, Tehran signalling no softening after the Vance letter, and two tanker incidents in Hormuz; up over 15% in October. The page's snapshot (113.43) and stats (112.33) differ, so the level is approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="104.0",day="about EUR 103.6-104.0/MWh on 30-October, +5.8-6.2% (Trading Economics); up about 40% on the month",
 note="REFRESHED SATURDAY 31-OCTOBER-2026 (Trading Economics): TTF rose above EUR 100/MWh for the first time since late 2022 on reduced Gulf LNG deliveries (Hormuz), colder forecasts and Europe-Asia competition for cargoes; EU storage 74.89% full on 29-October (Germany 61.65%, Netherlands 65.53%), about 849 TWh, roughly 100 TWh below last year. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.96",day="about 101.96 on 30-October, -0.07% (Trading Economics); +0.5% in October",
 note="REFRESHED SATURDAY 31-OCTOBER-2026 (Trading Economics): the dollar held near 102 on a flight to safety after weak major-tech earnings; CME FedWatch December-hike odds about 72%. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="4.93",day="about 4.93% on 30-October, roughly unchanged (Trading Economics); near seven-week lows",
 note="REFRESHED SATURDAY 31-OCTOBER-2026 (Trading Economics): the yield hovered near seven-week lows as a tech sell-off drew flows into Treasuries; December-hike odds eased to about 72% (CME FedWatch) from nearly 83% on 29-October. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.11770',day="LME fixing on 30-October, up from 1.11280; ECB fixing 1.11720, BFIX 1.11756",
 note="REFRESHED SATURDAY 31-OCTOBER-2026 to the 30-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 30-OCTOBER-2026 LME OFFICIAL - THE LAST TRADING SESSION. This run is compiled on SATURDAY 31-October; there is no LME ring on Saturday or Sunday, so the board was CARRIED to the last session because the market was shut, and the next official prints Monday 02-November 13:20 London. The Trading Economics aluminium CFD reference (about $3,059.70, -0.38% on 30-October, a later-in-day reference) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (31-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 30-October session, and the per-metal aluminium daily table's newest row is 30-October (cash 3,114.00, three-month 3,080.00, stock 231,200) with NO later row, so the board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.11280) matches the 29-October board verified on 30-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 29-October, and match the pages' change column: aluminium -475 to 231,200; copper +1,800 to 274,000; nickel -552 to 278,238; zinc -1,400 to 161,275; lead -150 to 311,375.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (30-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means (October's complete with this session and roll in on the first November run); the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the completed October cash average (twenty-two sessions, 01- to 30-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,080.00; the stock chart axis floor of 220,000 t leaves about 11,200 t of headroom below visible stock at 231,200 t and will be re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,114.00 against three-month $3,080.00 is therefore a $34.00 BACKWARDATION, wider than $7.00 on 29-October - the spread and the flat price moved in the same direction (both stronger) this session. In zinc the backwardation NARROWED to $65.50 while three-month rose - spread and outright in opposite directions."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 30-October official cash of $3,114.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $113.4), the dollar index (about 101.96), TTF (about EUR 104.0/MWh) and the US ten-year (about 4.93%) are Trading Economics readings for 30-October shown on 31-October; Trading Economics prices are contract-for-difference references, not official benchmarks. Its Brent and TTF pages again showed different levels in different sections (Brent 113.43 vs 112.33; TTF 103.95 vs 103.58), so levels are approximate. The Straits Daily Brief's oil feed had no print this run. EUR/USD is the 30-October LME fixing, the same session as the board."; hit+=1
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 31-OCTOBER: no authorised fetch was blocked (Westmetall EN, DE and per-metal pages, Trading Economics, AL Circle, news.metal.com and the Straits Daily Brief all fetched). Two individual SMM article pages returned HTTP 404, so the ex-China output figures (-1.2% y/y October, +0.2% y/y November forecast) are cited from the news.metal.com feed summaries. Hormuz items flagged by the Straits brief as unconfirmed are cited as such, not as fact. Chalco's Q3-2026 report was searched for in English and Chinese and not located; a broker estimate found is not published. No Q1-2027 Japanese premium offer has been reported yet (negotiations normally start late November)."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: TWO NEW RESULTS ADDED THIS RUN - Yunnan Aluminium nine-month 2026 (AL Circle, 31-October) and AMAG nine-month/Q3-2026 (AL Circle, 30-October). Neither was added to the per-company history strips: Yunnan Aluminium's source gives only cumulative nine-month figures (no quarterly series), and AMAG has no existing strip and only one verified quarter in hand, so gaps are left rather than estimated. NO NEW COMPANY WAS BACK-FILLED THIS RUN. Chalco's Q3-2026 report was searched for again and not located. Other entries are carried at their last publicly verified figures."; hit+=1
assert hit==4,hit
en=d['earnings_note']
d['earnings_note']=("YUNNAN ALUMINIUM AND AMAG REPORTED (added 31-October): Yunnan Aluminium's nine-month net income rose 164% to CNY 11.6bn on revenue of CNY 52.61bn (+19.4%); AMAG's nine-month EBITDA rose 59% to EUR 181m and it guided full-year EBITDA to EUR 200-220m. Chalco's Q3 is still pending. "+en)
d['earnings'].insert(0,{"company":"AMAG Austria Metall (AMAG)","group":"Downstream / rolled products and primary (Austria)","period":"9M / Q3 2026","reported":"30 Oct 2026","reported_iso":"2026-10-30","sentiment":"Positive",
 "headline":"9M-2026: revenue EUR 1.3bn (+16.4%), EBITDA EUR 181m (+59% from EUR 114m, margin 13.7% from 10%), net income EUR 82m (from EUR 34m), shipments 342,900 t (+7%). Q3: revenue EUR 473m (+35%), EBITDA EUR 80m (+139.5%), net income EUR 41m (from EUR 10m) on shipments of 121,500 t (+21%, including about 9,000 t carried over from Q2). Free cash flow -EUR 67m; net financial debt EUR 401m. Full-year 2026 EBITDA guidance EUR 200-220m.",
 "readthrough":"A European integrated rolled-products and primary producer is converting the 2026 price structure into higher margin, but working capital absorbed cash (negative operating cash flow) as metal prices rose. Generic read: European downstream volumes are firm and margins improved; the cash drain is a reminder that high metal prices tie up working capital along the chain.",
 "eps":None,"revenue_bn":None,"yoy_pct":59.0,"url":S_AM})
d['earnings'].insert(0,{"company":"Yunnan Aluminium (000807.SZ)","group":"Aluminum producer (China, hydro-powered)","period":"9M 2026 (Jan-Sep)","reported":"31 Oct 2026","reported_iso":"2026-10-31","sentiment":"Positive",
 "headline":"9M-2026: revenue CNY 52.61bn (+19.4% y/y from CNY 44.07bn); net income CNY 11.6bn (+164% from CNY 4.39bn); basic and diluted EPS CNY 3.35 (from CNY 1.27). Q3 standalone figures and output were not given in the source.",
 "readthrough":"A large Chinese hydro-powered smelter more than doubled nine-month profit, consistent with Chinese smelting margins widening as aluminium prices rose while alumina fell. Read-through: Chinese smelters are running near the capacity cap with strong margins, so there is no margin-driven curtailment pressure inside China.",
 "eps":3.35,"revenue_bn":None,"yoy_pct":164.0,"url":S_YA})

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 30-OCTOBER: no newer public disclosure","REVIEWED 31-OCTOBER: no newer public disclosure").replace("REVIEWED 30-OCTOBER. NO NEW DATED","REVIEWED 31-OCTOBER. NO NEW DATED")
    return o
PS={p['name']:p for p in d['producer_status']}
c=PS['China operators (aggregate, incl. Chalco and Hongqiao)']
c['update']="UPDATED 31-OCTOBER: Yunnan Aluminium reported nine-month net income of CNY 11.6bn, up 164% (AL Circle, 31-October), consistent with strong Chinese smelting margins; SMM (28-October seminar) puts Chinese capacity utilisation near 98.5% under the cap; Chalco's Q3-2026 report still not located. "+c['update']
c['src']=[L_YA,S_YA]
c=PS['EGA (Al Taweelah)']
c['update']="REVIEWED 31-OCTOBER: AL Circle (26-October) confirms 631 of 1,262 Al Taweelah cells restarted, matching EGA's 21-October release (half of cells); no newer EGA release located. SMM expects ex-China output to return to y/y growth in November as Middle East capacity restarts. "+c['update']
c['src']=[L_EG,S_EG]
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD
for s_ in [[L_TE,S_TE],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG],[L_ST,S_ST],[L_SMM,S_SMM],[L_YA,S_YA],[L_AM,S_AM],[L_RG,S_RG],[L_NA,S_NA],[L_EG,S_EG]]:
    d['sources'].append(s_)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 30-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 29-Oct)",W])
for x in ([L_TG,S_TG],[L_TY,S_TY],[L_ST,S_ST],[L_SMM,S_SMM]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-29'
ph['rows'][-1]=['2026-10-30',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
