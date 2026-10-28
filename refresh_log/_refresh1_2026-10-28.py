# Daily data refresh - 2026-10-28 (WEDNESDAY, ~02:40 UTC, BEFORE the ring). Board ROLLED to TUESDAY 27-Oct LME official (latest published session).
# Westmetall cache-busted EN and DE overviews both fetched and agree on the full 27-Oct session; Al per-metal table top row = 27-Oct (no later row).
# Completeness: 5/5 stock lines reconcile vs 26-Oct board; prior FX column (MTLE 1.11910) matches 26-Oct board.
# Key: Al cash 3,078.00 (+30.50), 3M 3,064.00 (+37.00) -> FIRST settled 3M close above the 3,061.5 July low after eleven below; BACKWARDATION narrowed to $14.00 (below the $15 trigger) while price rose.
# TE 28-Oct: Brent ~115.64 (+1.55%), TTF EUR97.07 (+1.30%), DXY 102.40, UST10Y ~5.03%; Fed hold ~90%, Dec hike ~82% (TE) / CME 93.4% hold, 78.9% Dec (SMM).
# SMM 28-Oct morning: LME 3M close 3,097 (+1.94%), SHFE 23,660 (+1.09%); three-region ingot ~420,000 t edging up a 2nd session; billet 87,500 (-2,000).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-28'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (27/28-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (28-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (28-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (28-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (28-Oct-2026)"
S_MM="https://news.metal.com/newscontent/104182085-us-fed-rate-hike-expectations-cool-aluminum-price-technical-rebound-momentum-sufficient-smm-aluminum-morning-meeting-summary"
L_MM="SMM - US Fed rate hike expectations cool, aluminum price technical rebound momentum sufficient [Aluminum Morning Meeting Summary] (28-Oct-2026)"
S_ST="https://straits.live/briefs/2026-10-28"; L_ST="Straits Daily Brief - Strait of Hormuz, 28-Oct-2026"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
assert B['LME Cash settlement']['cur']==3047.5 and B['LME 3-month']['cur']==3027.0
cash,prev_c,m3,prev_m,stk,prev_s=3078.0,3047.5,3064.0,3027.0,232100,234050
spr=cash-m3; assert spr==14.0 and prev_s-1950==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED WEDNESDAY 28-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING). THE BOARD IS THE TUESDAY 27-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION; Wednesday's official has not printed yet. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 27-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.11520); their prior-day FX column (MTLE 1.11910) matches the verified 26-October board, and the per-metal aluminium table's newest row is 27-October with NO later row; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 26-October (and match the pages' change column): aluminium 234,050 less 1,950 to 232,100; copper 272,975 less 250 to 272,725; nickel 279,942 plus 276 to 280,218; zinc 166,950 less 1,300 to 165,650; lead 318,650 less 3,975 to 314,675. "
 "The whole board sits on ONE UNIFORM SESSION (27-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(" CASH SETTLED $3,078.00 ON THE 27-OCTOBER OFFICIAL, UP $30.50 OR 1.00% FROM $3,047.50. THREE-MONTH SETTLED $3,064.00, UP $37.00 OR 1.22% FROM $3,027.00 - the highest settled three-month since 09-October, $53.50 ABOVE the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%), $69.50 above the 2,994.50 settled low of 15-October and THE FIRST SETTLED CLOSE ABOVE THE 3,061.5 JULY LOW (by $2.50) after eleven beneath it, though still $13.00 short of 3,077. "
 "THE BACKWARDATION NARROWED TO $14.00 FROM $20.50 because three-month rose more than cash - SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS FOR A SECOND SESSION (price up, structure softer) - and it is now BACK BELOW the published $15.00 reversal condition after three prints beyond it. "
 "VISIBLE LME STOCK FELL 1,950 t TO 232,100 t, another new series low and a fifth straight draw.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,078.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,064.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $2.50 ABOVE THE 3,061.5 JULY LOW (first settled close above it), $13.00 beneath the 3,077 weekly 50% retracement and $225.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for an eighth session; the rule-based cap on daily wave (v) near 2,977.5 was never touched."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+14.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,078.00 against three-month $3,064.00 is a $14.00 BACKWARDATION, NARROWER than 26-October's $20.50 as three-month rose $37.00 and cash $30.50 - THE SPREAD SOFTENED WHILE THE PRICE ROSE, the two moving in opposite directions for a second session. It has slipped BACK BELOW the published $15.00 reversal condition after three consecutive prints beyond it (23-, 26-October and earlier), which WEAKENS that signal; a contango beyond $24.50 would reverse it. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"232,100","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 1,950 t TO 232,100 t, another new series low and a fifth straight draw. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,064.00, UP $37.00 - the highest settled three-month since 09-October and the FIRST settled close above the 3,061.5 July low after eleven beneath it, $53.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 1,950 t TO 232,100 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":20.5,"avg":sep_sp,"note":VER+f" A $14.00 BACKWARDATION, NARROWER THAN 26-OCTOBER'S $20.50. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Three-month rose $37.00 and cash $30.50, so the structure softened while the flat price rose - opposite directions for a second session. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October and held through 26-October, but the 27-October print of $14.00 is BACK BELOW it - the structural signal is weakened, not reversed."},
 {"name":"EUR/USD LME fixing","cur":1.1152,"prev":1.1191,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.11520 FROM 1.11910 at the Tuesday ring; the ECB fixing printed 1.11500 and BFIX 1.11516. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (27-Oct official)","price":"3,078.0","basis":"THE 27-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,078.00, UP $30.50 OR 1.00%. Next official Wednesday 28-October 13:20 London."},
 {"tenor":"3-month (27-Oct official)","price":"3,064.0","basis":"THE 27-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,064.00, UP $37.00 - the highest since 09-October and the first settled close above the 3,061.5 July low (by $2.50), $69.50 above the 2,994.50 October low and $53.50 above the 02-January official."},
 {"tenor":"Cash-to-3M structure","price":"+14.0 (BACKWARDATION)","basis":"A $14.00 BACKWARDATION, narrowed from $20.50 while price rose - back below the $15.00 reversal condition after three prints beyond it."},
 {"tenor":"Visible LME stock","price":"232,100 t","basis":f"DOWN 1,950 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("PRICE BROKE UP, THE CURVE KEPT EASING. On the 27-October official cash $3,078.00 sits $14.00 ABOVE three-month $3,064.00, a BACKWARDATION, narrower than $20.50 on 26-October because three-month rose $37.00 and cash $30.50 - SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS for a second session. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50 and now $14.00. "
 f"READ: a ninth straight backwardation but BACK BELOW the published $15.00 reversal condition, while visible stock set another low (232,100 t). A rally that is led by three-month rather than prompt metal looks more like short-covering and macro relief than physical tightness. The September mean spread was ${sep_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]
d['chart_stock_axis']=[220000,255000]

ls=d['lme_series']; assert ls[-1][0]=='26-Oct', ls[-1]
d['lme_series']=ls[1:]+[["27-Oct",cash,m3,stk]]
assert all(220000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14625.0,14435.0,14500.0,14332.0); NI=(15440.0,15650.0,15535.0,15750.0); ZN=(3927.0,3830.0,3900.0,3797.0); PB=(1900.0,1920.0,1900.0,1921.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average-to-date: 18 sessions to 26-Oct (17 listed in the 27-Oct script + 26-Oct) + 27-Oct
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0,3736.0,3771.0,3727.0,3790.0,3900.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0,1851.0,1880.0,1872.0,1886.0,1900.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/19)/(sum(zs)/18),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/19)/(sum(ps)/18),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-27'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending TUESDAY 27-OCTOBER-2026 (Wednesday's official prints 13:20 London, after this run). THE WINDOW ROLLED THIS RUN: 06-October dropped and 27-October appended, so the window is 07-October to 27-October. Every point is an official cash settlement; the 27-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 26-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (27-October-2026 session; stock lines reconciled against 26-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,625.00, up $125.00 or 0.86%; three-month $14,435.00, up $103.00 or 0.72%. The BACKWARDATION WIDENED to $190.00 from $168.00 - the tightest prompt structure on the board. Stock fell 250 tonnes to 272,725 t."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,440.00, down $95.00 or 0.61%; three-month $15,650.00, down $100.00 or 0.63% - down for a third session. CONTANGO $210.00 from $215.00, still the widest carry on the board. Stock rose 276 tonnes to 280,218 t, the only stock build on the board."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,927.00, up $27.00 or 0.69%; three-month $3,830.00, up $33.00 or 0.87%. BACKWARDATION narrowed to $97.00 from $103.00. Stock fell 1,300 tonnes to 165,650 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,900.00, unchanged; three-month $1,920.00, down $1.00 or 0.05%. CONTANGO $20.00 from $21.00. Stock drew 3,975 tonnes to 314,675, a twenty-seventh consecutive draw."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Tuesday 27-October official aluminium led the board (three-month +1.22%), ahead of zinc +0.87% and copper +0.72%, with lead flat (-0.05%) and nickel -0.63%. Stocks fell for four of five metals (nickel +276 t). Trading Economics shows the US ten-year back near 5.03% and the dollar index near 102.4 on Fed decision day (28-October). The LME euro fixing fell to 1.1152.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='26-Oct'
        i['hist']=i['hist'][1:]+[["27-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,435.00 (3M); 14,625.00 (cash) $/t"
        i['ratio']="~14,625.00 $/t cash vs LME 3M 14,435.00 $/t"
        i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the TUESDAY 27-OCTOBER-2026 session at $14,625.00, UP $125.00 or 0.86% against $14,500.00. THE WINDOW ROLLED THIS RUN: 06-October dropped and 27-October appended, so the series is the last fifteen published official cash sessions, 07-October to 27-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 26-October). "
                  "Copper structure for context: backwardation $190.00 (from $168.00), stock fell 250 t to 272,725 t.")
s=d['inputs_summary']; j=s.find("UPDATE 27-OCTOBER"); s=s[j:] if j>0 else s
d['inputs_summary']=("UPDATE 28-OCTOBER: Copper rolled to the Tuesday 27-October LME official cash of $14,625.00, up $125.00, with its fifteen-session window moved to 07-October to 27-October. No new monthly carbon settlement is due until mid-November, and no new dated SMM fluoride, silicon or magnesium mark was located, so no other hist mark was appended. "
 "Energy firmed again: Brent about $115.64 (+1.55%) and European gas EUR 97.07/MWh (+1.30%, up about 40% on the month) on 28-October, with EU storage about 75% full, a record seasonal low (Trading Economics). SMM (28-October) notes tighter tax inspections keep compliant scrap scarce, with A00-scrap spreads at historical lows, eroding scrap's cost advantage. "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
otl=0.5*3047.5; ores=2403-otl; osh=otl/2403*100
OLDT=f"the tariff leg of the US duty-paid premium is 0.50 times the 26-October official cash of $3,047.50, or ${otl:,.2f}, UP $2.25 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${ores:,.2f}, so {osh:.1f}%"
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 27-October official cash of $3,078.00, or ${tl:,.2f}, UP $15.25 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED TUESDAY 27-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE MONDAY 26-OCTOBER OFFICIAL)."; NEWC="COMPILED WEDNESDAY 28-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE TUESDAY 27-OCTOBER OFFICIAL)."
n=0; nc=0
for p in d['premiums']:
    n+=p['src'].count(OLDT); nc+=p['src'].count(OLDC); p['src']=p['src'].replace(OLDT,NEWT).replace(OLDC,NEWC)
print('premium tariff replaced',n,nc); assert n==len(d['premiums'])
ra=360.40/m3*100; na=0
o="THE RATIO: LME Alumina at $360.40/t against the 26-October aluminium three-month of $3,027.00 is 11.91%"
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    if o in s: na+=1
    a['src']=s.replace(o,f"THE RATIO: LME Alumina at $360.40/t against the 27-October aluminium three-month of $3,064.00 is {ra:.2f}%")
print('alumina',na,len(d['alumina'])); assert na==len(d['alumina'])

d['lme_commentary']=("THE JULY LOW IS RECLAIMED, BUT THE CURVE DID NOT FOLLOW. On the Tuesday 27-October official cash settled $3,078.00 (+$30.50) and three-month $3,064.00 (+$37.00) - the highest three-month settlement since 09-October and the first settled close above the 3,061.5 July low after eleven beneath it, though $13.00 short of 3,077. "
 "Because three-month outpaced cash again, the backwardation narrowed to $14.00 from $20.50 - back below the $15.00 reversal condition, with spread and flat price moving in opposite directions for a second session; visible stock fell 1,950 t to a new low of 232,100 t. Aluminium led the base metals (zinc +0.9%, copper +0.7%, nickel -0.6%). "
 "After the official, SMM reports LME three-month closing electronic trade at $3,097 (+1.94%) and Shanghai at RMB 23,660 (+1.09%), with SHFE open interest up on new longs and LME open interest down as bears covered; SMM attributes the rebound to cooler Fed-hike expectations after remarks from Williams and Jefferson. Chinese three-region ingot stocks edged up for a second session to about 420,000 t (SMM). Energy firmed again (Brent about $115.64, +1.55%) and the Fed decides on 28-October. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: PRICE HAS TURNED CONSTRUCTIVE, STRUCTURE HAS NOT CONFIRMED. Constructive: three-month settled above 3,061.5 for the first time in twelve sessions ($3,064.00), the 2,994.50 October low has held for eight sessions, visible LME stock fell to another low of 232,100 t, SMM describes a technical rebound with new longs on SHFE and short-covering on LME, and energy costs remain elevated (Brent near $116, TTF near EUR 97) with Hormuz still effectively closed. "
 "Against: the backwardation narrowed to $14.00, back below the $15.00 trigger, so the rally is forward-led rather than physical; Chinese ingot stocks rose for a second session (about 420,000 t, SMM); Gulf supply keeps returning (EGA half of Al Taweelah's cells restarted, Alba near 1.3 Mt operating) and SMM expects new capacity in Indonesia, India and the Middle East to tip 2027 into surplus; markets still price about 79-82% odds of a December Fed hike.")
d['bottom_line']=("BOTTOM LINE: on the Tuesday 27-October LME official aluminium three-month rose $37.00 to $3,064.00 and cash $30.50 to $3,078.00 - the first settled close above the 3,061.5 July low in twelve sessions - while the backwardation narrowed to $14.00, back below the $15.00 tightness trigger, and visible stock fell to another low of 232,100 t. "
 "The two signals now disagree: price has half-confirmed (above 3,061.5, not yet 3,077) and structure has softened. Scenario weights hold at 15% bull / 45% base / 40% bear; a settled close above 3,077 would shift weight to base/bull, while a slip back below 3,061.5 with the spread heading to contango would reverse it. The daily Elliott count now favours wave (v) of the C-wave decline from 3,374 complete at 2,994.50 (about 60%) - a settled close above 3,077 would confirm it, below about 2,977.5 would force a re-count; invalidation 3,289; the weekly corrective count towards 2,894 stays the larger-degree preference. Next catalyst: the Fed decision on 28-October.")
c2=d['commercial']
for a,b in [("FIRST, THE PROMPT PREMIUM HOLDS BUT EASED: a $20.50 backwardation on 26-October, narrower than $25.00 as three-month rose $9.00 and cash $4.50 - a third consecutive print beyond the $15.00 reversal condition, so nearby metal is still valued over forward metal and there is no carry reward for deferring purchases, though the narrowing shows the tightness is not building.",
             "FIRST, THE PRICE ROSE BUT THE PROMPT PREMIUM KEPT EASING: a $14.00 backwardation on 27-October, narrower than $20.50 as three-month rose $37.00 and cash $30.50 - back below the $15.00 reversal condition after three prints beyond it, so nearby metal is still valued over forward metal but by less, and the rally is being carried by forward buying and short-covering rather than prompt physical demand."),
 (f"is ${otl:,.2f} on 26-October cash, {osh:.1f}% of the $2,403/t premium",f"is ${tl:,.2f} on 27-October cash, {share:.1f}% of the $2,403/t premium"),
 ("the 26-October official took three-month to $3,027.00, $32.50 above the 2,994.50 settled low inside the 2,980-3,000 zone and $34.50 beneath 3,061.5; energy eased slightly but stays high (Brent $114.61; European gas EUR 94.92/MWh, 27-October); the Fed decides on 28-October;",
  "the 27-October official took three-month to $3,064.00, $69.50 above the 2,994.50 settled low and $2.50 above 3,061.5 (first close above it), $13.00 short of 3,077; energy firmed again (Brent about $115.64; European gas EUR 97.07/MWh, 28-October); the Fed decides on 28-October;")]:
    assert a in c2,a; c2=c2.replace(a,b)
d['commercial']=c2

O_SC=("HELD 27-OCTOBER at 15/45/40: the 26-October official lifted three-month $9.00 to $3,027.00 with stock at another low, but the backwardation narrowed to $20.50 and price is still beneath 3,061.5, so no weight moves; Chinese ingot stocks rose on 27-October for the first time in eleven working days. ")
for s in d['outlook']['scenarios']:
    assert s['drivers'].startswith(O_SC)
    s['drivers']=("HELD 28-OCTOBER at 15/45/40: the 27-October official lifted three-month $37.00 to $3,064.00, a first settled close above 3,061.5, but the backwardation narrowed to $14.00 - back below the $15.00 trigger - and Chinese ingot stocks rose a second session, so the price and structure signals offset and no weight moves until a close above 3,077 or a slip back below 3,061.5. ")+s['drivers'][len(O_SC):]
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium three-month jumped $37 to $3,064 on Tuesday's LME official - back above the $3,061.5 July low for the first time in twelve sessions - but the backwardation shrank to $14, below the $15 tightness trigger: price is rebounding faster than physical tightness, with the Fed decision on 28 October the next test.",
 "points":[
 "WHAT MOVED: Tuesday's LME official settled cash at $3,078.00 (+$30.50) and three-month at $3,064.00 (+$37.00, +1.2%), the highest since 9 October. Cash still trades $14.00 above three-month (backwardation), down from $20.50 - the spread narrowed while price rose for a second day. LME stock fell 1,950 t to a new low of 232,100 t.",
 "WHY: SMM links the rebound to cooler Fed-hike expectations after remarks from Fed officials, with new longs on Shanghai and short-covering on the LME; aluminium led the base-metals board. But Chinese three-region ingot stocks rose a second session to about 420,000 t (SMM), so the move looks macro- and positioning-led rather than physical.",
 "SUPPLY AND COST: SMM expects new capacity in Indonesia, India and the Middle East to tip 2027 from deficit toward surplus, and Gulf restarts continue. Energy firmed again (Brent about $115.6, European gas about EUR 97/MWh) and Hormuz is still described as effectively closed.",
 "WHAT TO WATCH: the Fed decision on 28-October (hold about 90% priced; December hike about 79-82%); a settled close above $3,077 to confirm the rebound, or a slip back below $3,061.5; whether the backwardation stays above zero or turns to contango."]}

d['feed']=([
 {"when":"Wed 28-Oct","impact":"Bullish","text":"BOARD ROLLED TO THE TUESDAY 27-OCTOBER LME OFFICIAL: cash $3,078.00 (+$30.50), three-month $3,064.00 (+$37.00), first settled close above the 3,061.5 July low in twelve sessions; stock -1,950 t to a new low of 232,100 t."},
 {"when":"Wed 28-Oct","impact":"Bearish","text":"STRUCTURE SOFTER: the cash-to-three-month backwardation narrowed to $14.00 from $20.50, back below the $15.00 reversal condition - spread and price moving in opposite directions for a second session."},
 {"when":"Wed 28-Oct","impact":"Mixed","text":"SMM: LME three-month closed electronic trade at $3,097 (+1.94%), SHFE RMB 23,660 (+1.09%) on cooler Fed-hike expectations; three-region ingot stocks edged up a second session to about 420,000 t; 6063 billet -2,000 t to 87,500 t."},
 {"when":"Wed 28-Oct","impact":"Mixed","text":"ENERGY / HORMUZ: Brent back above $115 (+1.55%) after two losses, TTF EUR 97.07/MWh (Trading Economics); Straits Daily Brief still describes the strait as effectively closed with 161 vessels holding position; Qatar urged Iran to reopen it."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM RECLAIMS THE JULY LOW. The Tuesday 27-October official settled cash at $3,078.00 (+1.00%) and three-month at $3,064.00 (+1.22%) - the highest three-month settlement since 09-October and the first settled close above the 3,061.5 July low after eleven beneath it. Visible stock fell 1,950 t to a new low of 232,100 t. Aluminium led the board: zinc three-month +0.87%, copper +0.72%, lead -0.05%, nickel -0.63%."},
 {"theme":"LME","horizon":"0-1 month","impact":"Bearish","url":W,
  "headline":"BUT THE CURVE KEEPS EASING: the cash-to-three-month backwardation narrowed to $14.00 from $20.50 on 27-October, back below the $15.00 reversal condition after three prints beyond it, because three-month rose more than cash for a second session. READ: a forward-led rally with a softening prompt spread points to positioning and macro relief rather than physical tightness."},
 {"theme":"China","horizon":"0-1 month","impact":"Mixed","url":S_MM,
  "headline":"SMM MORNING SUMMARY (28-October): LME three-month closed at $3,097 (+1.94%, range 3,023.5-3,105) and the most-traded SHFE contract at RMB 23,660/t (+1.09%), breaking above its 5- to 60-day moving averages; SHFE open interest rose 4,026 lots on new longs while LME open interest fell 4,559 lots as bears covered. SMM credits cooler Fed-hike expectations (CME: 93.4% hold, 78.9% chance of a 25bp hike by December). East China A00 premiums slipped to RMB 180-200/t; three-region ingot stocks edged up a second session to about 420,000 t while 6063 billet fell 2,000 t to 87,500 t. SMM still expects ex-China capacity in Indonesia, India and the Middle East to move 2027 toward surplus."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Mixed","url":S_BR,
  "headline":"ENERGY FIRMS AGAIN (Trading Economics, 28-October): Brent rose back above $115 (about $115.64, +1.55%) after two losing sessions, with traders watching Israeli election results and Middle East diplomacy and a roughly 2 million barrel US crude draw; TTF rose to about EUR 97.07/MWh, up about 40% on the month, with EU storage about 75% full, a record seasonal low. The Straits Daily Brief (28-October) still describes Hormuz as effectively closed to commercial traffic, with 161 vessels holding position; Iranian state media's claim of a mine strike on a tanker is unconfirmed, and Qatar has urged Iran to reopen the strait. READ: smelter energy costs stay elevated."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Mixed","url":S_TD,
  "headline":"FED DECISION DAY (Trading Economics, 28-October): the dollar index rose for a third session to about 102.4, a two-week high, and the US ten-year was back near 5.03%; markets price about 90% odds of a hold today and about 82% odds of a December hike. READ: the metals rebound leans on cooler hike expectations, so hawkish guidance would test it."},
]+d['news']
d['news']=d['news'][:20]

hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Tue 27-Oct':
        hitc+=1
        cat['date']='Daily, from Wed 28-Oct'
        cat['event']="3,061.5 RECLAIMED ON THE 27-OCTOBER OFFICIAL ($3,064.00) AFTER ELEVEN SETTLED CLOSES BENEATH IT; THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE AND $17.00 ABOVE THE RULE-BASED CAP, RETESTED IT ON 20-OCTOBER ($2,997.00), AND HAS SINCE SETTLED $3,024.50, $3,008.00, $3,018.00, $3,027.00 AND $3,064.00. A settled recovery above 3,077 would confirm wave (v) complete; a slip back beneath 3,061.5 would weaken the rebound and a settled close beneath about 2,977.5 would force a re-count toward the 2,894 weekly 61.8%; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289. STRUCTURE: the $15.00 backwardation reversal condition (confirmed 23-October) was LOST on 27-October at $14.00; a return to contango would undo it."
    elif cat['date']=='Tue 27 - Wed 28-Oct':
        hitc+=1
        cat['event']="FOMC MEETING (decision Wednesday 28-October): markets price about a 90% chance of a hold and about 82% odds of a 25bp hike in December (Trading Economics, 28-October; CME FedWatch via SMM shows 93.4% hold and 78.9% for December); hike expectations cooled after remarks from Williams and Jefferson. The US ten-year is near 5% and the dollar index near 102.4. Hawkish guidance would test the metals rebound; a softer tone would extend it."
assert hitc==2,hitc
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 28-OCTOBER: the 27-October official printed a $14.00 BACKWARDATION, back BELOW the $15.00 reversal condition after three prints beyond it, narrowing for a second session as three-month outpaced cash. Trend moved from DOWN to FLAT: contango is still $14.00 away, but the structural support is fading."
RK[0]['trend']='flat'
RK[4]['risk']+=" UPDATE 28-OCTOBER: LME stock fell 1,950 t to a new series low of 232,100 t on 27-October; SMM's Chinese three-region ingot inventory edged up a second session to about 420,000 t, while 6063 billet fell 2,000 t. Mixed evidence: trend held at FLAT."
RK[4]['trend']='flat'
hit=0
for r in RK:
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 28-OCTOBER: Brent rose back to about $115.64 (+1.55%) and TTF to EUR 97.07/MWh (+1.30%, up about 40% on the month), with EU storage at a record seasonal low (Trading Economics). Trend held at UP."; hit+=1
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 28-OCTOBER: Straits Daily Brief - strait still effectively closed to commercial traffic (4 transits on 18-October vs an 85/day baseline), 161 vessels holding position (up from 125); Iranian state media claim a tanker struck mines (unconfirmed; CENTCOM says main lanes are clear); Qatar urged Iran to reopen the strait. Trend held at UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 28-OCTOBER: decision due today; markets price about 90% odds of a hold and about 82% odds of a December hike (Trading Economics), CME 78.9% (via SMM) after cooler remarks from Williams and Jefferson; US ten-year back near 5.03%, dollar index at a two-week high. Trend held at UP."; hit+=1; r['trend']='up'
    if r['risk'].startswith('THE EX-CHINA RESTART PIPELINE'):
        r['risk']+=" UPDATE 28-OCTOBER: SMM (28-October) again cites ex-China restarts and new capacity in Indonesia, India and the Middle East as pushing 2027 from deficit toward surplus. Trend held at UP."; hit+=1; r['trend']='up'
assert hit==4,hit
d['outlook']['ai_analysis'].insert(0,"WEDNESDAY 28-OCTOBER ON THE TUESDAY 27-OCTOBER OFFICIAL: three-month rose $37.00 to $3,064.00 and cash $30.50 to $3,078.00 - the first settled close above the 3,061.5 July low in twelve sessions - but the backwardation narrowed to $14.00 from $20.50, back below the $15.00 reversal condition, as price and spread moved in opposite directions for a second session; visible stock set another low (232,100 t). Scenario weights hold at 15/45/40 because the price and structure signals now offset. SMM frames the move as a technical rebound on cooler Fed-hike expectations, with new longs on SHFE and short-covering on the LME, while Chinese ingot stocks rose a second session. Energy firmed again and Hormuz remains effectively closed. The Fed decision on 28-October is the next test; a settled close above 3,077 would shift weight to base/bull, a slip back below 3,061.5 with the spread heading to contango would reverse it.")

EWS=("REVIEWED 28-OCTOBER ON THE TUESDAY 27-OCTOBER OFFICIAL: three-month settled $3,064.00, up $37.00 - an eighth settled close above the 2,994.50 low of 15-October, the highest since 09-October and the first back above 3,061.5; the sequence 2,994.50 / 3,024.50 / 3,008.00 / 3,018.00 / 3,027.00 / 3,064.00 now reads as a clear first leg up of a corrective rebound from a completed wave (v). Wave (v) of C ($154.00 from the 3,148.5 wave (iv) high to 2,994.50) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged, NOT re-labelled; base case raised to about 60%: wave (v) ended at 2,994.50 and a corrective rebound toward 3,077 then the 3,110-3,148.5 area is under way (confirmed by a settled close above 3,077); alternate about 40%: the rebound fails beneath 3,077 and a settled close beneath 2,977.5 forces a re-count toward 2,894. The narrower $14.00 backwardation is context, not an Elliott signal. Invalidation 3,289; confidence moderate. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED 24-OCTOBER"); assert st.startswith("REVIEWED 27-OCTOBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED 24-OCTOBER"); assert lt.startswith("REVIEWED 27-OCTOBER") and k>0
d['ew']['long_term']['writeup']="REVIEWED 28-OCTOBER (TUESDAY 27-OCTOBER OFFICIAL, WEEK IN PROGRESS): three-month at 3,064.00, up $46.00 from the 3,018.00 weekly close and back above the 3,061.5 July low, mid-way in the 2,950-3,110 zone; a weekly close above 3,077 (the 50% retracement) would be the first sign the larger correction is ending early, but the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label. "+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="115.64",day="about $115.64 on 28-October, +1.55% (Trading Economics); back above $115 after two losses",
 note="REFRESHED WEDNESDAY 28-OCTOBER-2026 (Trading Economics): Brent rose back above $115 after two straight losing sessions as traders watched Israeli election results and renewed Middle East diplomacy, and a roughly 2 million barrel drop in US crude inventories pointed to tighter supply. The Straits Daily Brief shows $114.35 at 00:09 UTC - a different time stamp. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="97.1",day="EUR 97.07/MWh on 28-October, +1.30% (Trading Economics); up about 40% on the month",
 note="REFRESHED WEDNESDAY 28-OCTOBER-2026 (Trading Economics): TTF rebounded to about EUR 97/MWh after dipping below EUR 96 on peace hopes; it stays near multi-year highs as Hormuz shipping attacks continue. EU storage is about 75% full, a record seasonal low (Germany just over 61%); colder weather, Norwegian outages and Europe-Asia LNG competition are cited. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="102.40",day="about 102.40 on 28-October, +0.01% (Trading Economics); third straight gain, two-week high",
 note="REFRESHED WEDNESDAY 28-OCTOBER-2026 (Trading Economics): the dollar index rose for a third session to its highest in about two weeks ahead of the Fed decision; markets price about 90% odds of a hold and about 82% odds of a December hike; safe-haven demand on Iran concerns and euro weakness on France's fiscal outlook are cited. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="5.03",day="about 5.03% on 28-October, +2bp (Trading Economics); back above 5% after a three-week decline",
 note="REFRESHED WEDNESDAY 28-OCTOBER-2026 (Trading Economics): the quote shows about 5.03%, back above 5% after a three-week decline to one-month lows; investors await the Fed decision and GDP and PCE inflation data. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.11520',day="LME fixing on 27-October, down from 1.11910; ECB fixing 1.11500, BFIX 1.11516",
 note="REFRESHED WEDNESDAY 28-OCTOBER-2026 to the 27-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE TUESDAY 27-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION. This Wednesday 28-October run is compiled about 02:40 London, BEFORE the ring, so Wednesday's official (13:20 London) has not printed. Reference and electronic-close prices (Trading Economics aluminium about $3,100, SMM LME e-close $3,097) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (28-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 27-October session, and the per-metal aluminium daily table's newest row is 27-October (cash 3,078.00, three-month 3,064.00, stock 232,100) with NO later row, so the board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.11910) matches the 26-October board verified on 27-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 26-October, and match the pages' change column: aluminium -1,950 to 232,100; copper -250 to 272,725; nickel +276 to 280,218; zinc -1,300 to 165,650; lead -3,975 to 314,675.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (27-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (nineteen sessions, 01- to 27-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,064.00; the stock chart axis floor of 220,000 t leaves about 12,000 t of headroom below visible stock at 232,100 t and will be re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,078.00 against three-month $3,064.00 is therefore a $14.00 BACKWARDATION, narrower than $20.50 on 26-October - the spread softened while the flat price rose, the two moving in opposite directions for a second session."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 27-October official cash of $3,078.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $115.64), the dollar index (about 102.40), TTF (EUR 97.07/MWh) and the US ten-year (about 5.03%) are Trading Economics readings shown on 28-October; Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages were internally inconsistent by a few cents or basis points this run (header vs stats section), so they are approximate; EUR/USD is the 27-October LME fixing, the same session as the board. The Straits Daily Brief (28-October) shows Brent at $114.35 at 00:09 UTC - a different time stamp, cited in text only."; hit+=1
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 28-OCTOBER: no authorised fetch was blocked (Westmetall EN, DE and per-metal pages, Trading Economics, news.metal.com and the Straits Daily Brief all fetched). The SMM morning summary's metal.com/en mirror returned HTTP 404 and the same article was read on news.metal.com. SMM's 28-October three-region ingot figure (about 420,000 t) is taken from SMM's related-news summary on that article; the dated flash itself was not located, so it is cited as approximate. Hormuz items from Iranian state media in the Straits Daily Brief are cited as reported, not as fact. The SMM-reported LME three-month electronic close of $3,097 on Tuesday is a post-official price and is NOT used on the board. No Q1-2027 Japanese premium offer has been reported yet (negotiations normally start late November); a search this run found none."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: NO NEW PEER RESULT WAS REPORTED IN THIS WINDOW. Norsk Hydro's Q3-2026 (23-October) remains the latest addition; Chalco's Q3-2026 report was searched for again and not yet located (it normally publishes in late October; the BOC International forecast of about RMB 6.03bn is a broker estimate and is NOT published as a result). NO NEW COMPANY WAS BACK-FILLED THIS RUN. Century Aluminum has not yet announced its Q3 date. Other entries are carried at their last publicly verified figures, and gaps stay gaps."; hit+=1
assert hit==4,hit
en=d['earnings_note']
d['earnings_note']=en.replace("(added 24-October; no newer peer result to 27-October):","(added 24-October; no newer peer result to 28-October):",1)

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 27-OCTOBER: no newer public disclosure","REVIEWED 28-OCTOBER: no newer public disclosure").replace("REVIEWED 27-OCTOBER. NO NEW DATED","REVIEWED 28-OCTOBER. NO NEW DATED")
    return o
PS={p['name']:p for p in d['producer_status']}
c=PS['China operators (aggregate, incl. Chalco and Hongqiao)']
c['update']="UPDATED 28-OCTOBER (SMM, 28-October): three-region aluminium ingot inventory edged up a second session to about 420,000 t (Guangdong destocking, Wuxi and Gongyi building); 6063 billet fell 2,000 t to 87,500 t; SHFE most-traded RMB 23,660/t (+1.09%). Chalco's Q3-2026 report not yet located. "+c['update']
c['src']=[L_MM,S_MM]
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD
for s_ in [[L_TE,S_TE],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG],[L_MM,S_MM],[L_ST,S_ST]]:
    d['sources'].append(s_)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 27-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 26-Oct)",W])
for x in ([L_MM,S_MM],[L_TD,S_TD],[L_ST,S_ST]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-26'
ph['rows'][-1]=['2026-10-27',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
