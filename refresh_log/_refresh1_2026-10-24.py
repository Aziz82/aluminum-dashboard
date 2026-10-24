# Daily data refresh - 2026-10-24 (SATURDAY, ~03:40 London). Board ROLLED to FRIDAY 23-Oct LME official (last session of the week; no ring Sat/Sun).
# Westmetall cache-busted EN AND DE overviews both fetched and agree on the full 23-Oct session; Al per-metal table top row = 23-Oct (no later row).
# Completeness: 5/5 stock lines reconcile vs 22-Oct board; prior FX column (MTLE 1.11990) matches 22-Oct board.
# Key: Al cash 3,043 (+10.00), 3M 3,018 (+10.00) -> BACKWARDATION $25.00 unchanged: SECOND settled print beyond $15 = reversal condition CONFIRMED.
# TE 23/24-Oct: Brent 116.91 (+3.30%, highest since Jun-2022), TTF EUR93.19 (+3.49%), DXY 101.75, UST10Y 5.00%. Norsk Hydro Q3 (23-Oct): adj EBITDA NOK 9,089m.
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-24'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (23/24-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (23/24-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (23/24-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (23/24-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (23/24-Oct-2026)"
S_NH="https://www.manilatimes.net/2026/10/23/tmt-newswire/globenewswire/norsk-hydro-solid-results-and-strong-performance/2452499"; L_NH="Norsk Hydro - 'Solid results and strong performance', Q3-2026 release (GlobeNewswire reprint, 23-Oct-2026)"
S_NHI="https://www.investing.com/news/company-news/norsk-hydro-q3-2026-slides-ebitda-rises-despite-cash-flow-pressure-93CH-4968209"; L_NHI="Investing.com - Norsk Hydro Q3 2026 slides: EBITDA rises despite cash flow pressure (23-Oct-2026)"
S_SMM="https://news.metal.com/newscontent/104174167-chinas-aluminum-ingot-inventory-in-three-regions-falls-on-october-23"; L_SMM="SMM - China aluminium ingot inventory in three regions falls on October 23 (23-Oct-2026)"
S_IN="https://in.investing.com/news/commodities-news/aluminium-declines-as-ega-restarts-half-of-al-taweelah-smelters-reduction-cells-5650067"; L_IN="Investing.com (Kedia Advisory) - Aluminium declines as EGA restarts half of Al Taweelah's reduction cells (23-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
assert B['LME Cash settlement']['cur']==3033.0 and B['LME 3-month']['cur']==3008.0
cash,prev_c,m3,prev_m,stk,prev_s=3043.0,3033.0,3018.0,3008.0,235800,236025
spr=cash-m3; assert spr==25.0 and prev_s-225==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED SATURDAY 24-OCTOBER-2026. THE BOARD IS THE FRIDAY 23-OCTOBER-2026 LME OFFICIAL - THE LAST SESSION OF THE WEEK AND THE CORRECT FIGURE TO CARRY, because there is no ring on Saturday or Sunday; the next official prints Monday 26-October 13:20 London. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 23-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.11910); their prior-day FX column (MTLE 1.11990) matches the verified 22-October board, and the per-metal aluminium table shows NO row after 23-October; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 22-October: aluminium 236,025 less 225 to 235,800; copper 272,950 plus 800 to 273,750; nickel 280,674 unchanged; zinc 167,075 less 50 to 167,025; lead 323,975 less 1,800 to 322,175. "
 "The whole board sits on ONE UNIFORM SESSION (23-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(" CASH SETTLED $3,043.00 ON THE 23-OCTOBER OFFICIAL, UP $10.00 OR 0.33% FROM $3,033.00. THREE-MONTH SETTLED $3,018.00, UP $10.00 OR 0.33% FROM $3,008.00 - back $7.50 ABOVE the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%), $23.50 above the 2,994.50 settled low of 15-October and a TENTH settled close beneath the 3,061.5 July low (by $43.50). On the week three-month rose $6.00 from the 16-October close of $3,012.00. "
 "THE BACKWARDATION HELD AT $25.00 as cash and three-month rose by the same $10.00 - the SECOND consecutive settled official beyond the published $15.00 reversal condition, which is therefore CONFIRMED. "
 "VISIBLE LME STOCK FELL 225 t TO 235,800 t, another new series low.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,043.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,018.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $43.50 BENEATH THE 3,061.5 JULY LOW, $59.00 beneath the 3,077 weekly 50% retracement and $271.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a sixth session; the rule-based cap on daily wave (v) near 2,977.5 was never touched."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+25.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,043.00 against three-month $3,018.00 is a $25.00 BACKWARDATION, UNCHANGED from 22-October as both legs rose $10.00 - spread flat while price rose. THE PUBLISHED REVERSAL CONDITION - A BACKWARDATION BEYOND $15.00 ON A SETTLED OFFICIAL - IS NOW MET ON TWO CONSECUTIVE OFFICIALS, WHICH WAS THE STATED CONFIRMATION. The bearish structural confirmation, a contango beyond $24.50, is far away. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"235,800","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 225 t TO 235,800 t, another new series low, a third straight draw. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,018.00, UP $10.00 - $43.50 beneath the 3,061.5 July low, a tenth settled close below it, and $7.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 225 t TO 235,800 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":25.0,"avg":sep_sp,"note":VER+f" A $25.00 BACKWARDATION, UNCHANGED FROM 22-OCTOBER. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Both legs rose $10.00, so the structure held while the flat price rose. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): MET ON 22-OCTOBER AND AGAIN ON 23-OCTOBER - CONFIRMED."},
 {"name":"EUR/USD LME fixing","cur":1.1191,"prev":1.1199,"avg":1.1465,"note":VER+" THE LME EURO FIXING EASED TO 1.11910 FROM 1.11990 at the Friday ring; the ECB fixing printed 1.11930 and BFIX 1.11890. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (23-Oct official)","price":"3,043.0","basis":"THE 23-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,043.00, UP $10.00 OR 0.33%. Market shut Saturday/Sunday; next official Monday 26-October 13:20 London."},
 {"tenor":"3-month (23-Oct official)","price":"3,018.0","basis":"THE 23-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,018.00, UP $10.00 - $43.50 beneath the 3,061.5 July low (tenth settled close below it), $23.50 above the 2,994.50 October low and $7.50 above the 02-January official; up $6.00 on the week."},
 {"tenor":"Cash-to-3M structure","price":"+25.0 (BACKWARDATION)","basis":"A $25.00 BACKWARDATION, unchanged - the second consecutive settled print beyond the $15.00 reversal condition, which confirms it."},
 {"tenor":"Visible LME stock","price":"235,800 t","basis":f"DOWN 225 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE TIGHTER STRUCTURE HELD FOR A SECOND SESSION. On the 23-October official cash $3,043.00 sits $25.00 ABOVE three-month $3,018.00, a BACKWARDATION, unchanged from 22-October as both legs rose $10.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00 and now $25.00. "
 f"READ: a seventh straight backwardation and a second consecutive print beyond the published $15.00 reversal condition, so the condition is CONFIRMED, while visible stock keeps setting lows (235,800 t). Prompt metal is being valued over forward metal. The September mean spread was ${sep_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]

ls=d['lme_series']; assert ls[-1][0]=='22-Oct', ls[-1]
d['lme_series']=ls[1:]+[["23-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
# (cash, 3M, prev cash, prev 3M)
CU=(14415.0,14270.0,14215.0,14096.0); NI=(15695.0,15900.0,15935.0,16135.0); ZN=(3790.0,3726.0,3727.0,3692.0); PB=(1886.0,1908.0,1872.0,1897.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average-to-date: 16 sessions to 22-Oct (15 listed in 23-Oct script + 22-Oct) + 23-Oct
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0,3736.0,3771.0,3727.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0,1851.0,1880.0,1872.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/17)/(sum(zs)/16),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/17)/(sum(ps)/16),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-23'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending FRIDAY 23-OCTOBER-2026 (the last session of the week; no ring on Saturday or Sunday). THE WINDOW ROLLED THIS RUN: 02-October dropped and 23-October appended, so the window is 05-October to 23-October. Every point is an official cash settlement; the 23-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 22-October. Next official Monday 26-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (23-October-2026 session; stock lines reconciled against 22-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,415.00, up $200.00 or 1.41%; three-month $14,270.00, up $174.00 or 1.23% - the strongest metal on the board. The BACKWARDATION WIDENED to $145.00 from $119.00. Stock rose 800 tonnes to 273,750 t, a fifth straight rise but a far smaller inflow than the prior two sessions."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,695.00, down $240.00 or 1.51%; three-month $15,900.00, down $235.00 or 1.46% - the only metal down on the board. CONTANGO $205.00 from $200.00, still the widest carry on the board. Stock unchanged at 280,674 t."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,790.00, up $63.00 or 1.69%; three-month $3,726.00, up $34.00 or 0.92%. BACKWARDATION widened to $64.00 from $35.00. Stock fell 50 tonnes to 167,025 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,886.00, up $14.00 or 0.75%; three-month $1,908.00, up $11.00 or 0.58%. CONTANGO $22.00 from $25.00. Stock drew 1,800 tonnes to 322,175, a twenty-fifth consecutive draw."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Friday 23-October official the board turned mostly higher - copper three-month +1.23%, zinc +0.92%, lead +0.58% and aluminium +0.33%, with nickel the exception at -1.46%. Trading Economics reported the US ten-year back near 5.00% after Thursday's flight to safety and the dollar index little changed near 101.75. The LME euro fixing eased to 1.1191.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='22-Oct'
        i['hist']=i['hist'][1:]+[["23-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,270.00 (3M); 14,415.00 (cash) $/t"
        i['ratio']="~14,415.00 $/t cash vs LME 3M 14,270.00 $/t"
        i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the FRIDAY 23-OCTOBER-2026 session at $14,415.00, UP $200.00 or 1.41% against $14,215.00. THE WINDOW ROLLED THIS RUN: 02-October dropped and 23-October appended, so the series is the last fifteen published official cash sessions, 05-October to 23-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 22-October). "
                  "Copper structure for context: backwardation $145.00 (from $119.00), stock rose 800 t to 273,750 t.")
d['inputs_summary']=("UPDATE 24-OCTOBER: Copper rolled to the Friday 23-October LME official cash of $14,415.00, up $200.00, with its fifteen-session window moved to 05-October to 23-October. No new monthly carbon settlement is due until mid-November; the October cycle (Mysteel, 16-October: Shandong prebaked-anode benchmark +Yuan 400/t to Yuan 6,130/t; green petcoke 3B Yuan 3,610.5/t) remains the latest and is already in the histories. No new dated SMM fluoride, silicon or magnesium mark was retrievable this run, so no hist mark was appended other than Copper. Energy inputs rose again - Brent $116.91 (+3.30%), the highest since June 2022, and European gas EUR 93.19/MWh (+3.49%), a fourth weekly gain, with EU storage 74.62% full on 22-October, the lowest for the season since 2009 (Trading Economics, 23/24-October). Norsk Hydro's Q3 release (23-October) cites higher energy and carbon costs in its Aluminium Metal segment and higher LNG sourcing costs at Alunorte. Every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT="the tariff leg of the US duty-paid premium is 0.50 times the 22-October official cash of $3,033.00, or $1,516.50, UP $1.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of $886.50, so 63.1%"
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 23-October official cash of $3,043.00, or ${tl:,.2f}, UP $5.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED FRIDAY 23-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE THURSDAY 22-OCTOBER OFFICIAL)."; NEWC="COMPILED SATURDAY 24-OCTOBER-2026 (MARKET SHUT FOR THE WEEKEND) (LME BOARD ON THE FRIDAY 23-OCTOBER OFFICIAL)."
n=0
for p in d['premiums']:
    n+=p['src'].count(OLDT); p['src']=p['src'].replace(OLDT,NEWT).replace(OLDC,NEWC)
print('premium tariff replaced',n); assert n==len(d['premiums'])
ra=360.40/m3*100; na=0
o=f"THE RATIO: LME Alumina at $360.40/t against the 22-October aluminium three-month of $3,008.00 is {360.40/3008*100:.2f}%"
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    if o in s: na+=1
    a['src']=s.replace(o,f"THE RATIO: LME Alumina at $360.40/t against the 23-October aluminium three-month of $3,018.00 is {ra:.2f}%")
print('alumina',na,len(d['alumina'])); assert na==len(d['alumina'])

d['lme_commentary']=("TIGHTNESS CONFIRMED ON A QUIET UP-DAY. On the Friday 23-October official cash settled $3,043.00 and three-month $3,018.00, both up $10.00 - three-month back $7.50 above the 02-January official, so fractionally positive for 2026, $23.50 above the 15-October settled low of 2,994.50 and $43.50 beneath the 3,061.5 July low; on the week three-month gained $6.00. "
 "The backwardation held at $25.00 - a second consecutive settled print beyond the published $15.00 reversal condition, which confirms it - and visible stock fell 225 t to another series low of 235,800 t. Most of the board rose: copper +1.2%, zinc +0.9%, lead +0.6%; nickel -1.5%. "
 "Energy kept climbing: Trading Economics reported Brent at $116.91 (+3.30%), the highest since June 2022, and TTF at EUR 93.19/MWh on reports of possible renewed US strikes on Iran and continued Houthi attacks on Saudi Arabia. Norsk Hydro's Q3 (23-October) showed adjusted EBITDA up to NOK 9,089m on higher all-in metal prices. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND STILL IN CONTROL ON PRICE, BUT THE STRUCTURE HAS NOW CONFIRMED A TURN. Against: three-month has settled beneath 3,061.5 ten times; Gulf supply is returning - EGA has half of Al Taweelah's 1,262 cells restarted (21-October) and guides full output in Q1-2027, and Slovalco's first 75,000 t is now targeted by end-February 2027 (Norsk Hydro, 23-October); Trading Economics reports Chinese aluminium exports up 25.9% year on year in September; a December Fed hike is still priced (about 76%). "
 "Constructive: the backwardation printed $25.00 on two consecutive officials, confirming the $15.00 reversal condition; visible LME stock fell to another low of 235,800 t; the 2,994.50 October low has held for six sessions; Chinese three-region ingot stocks fell for a ninth working day to the 420,000 t range (SMM, 23-October); energy costs rose again - Brent the highest since June 2022 - which lifts the smelter cost floor.")
d['bottom_line']=("BOTTOM LINE: on the Friday 23-October LME official aluminium cash and three-month both rose $10.00, to $3,043.00 and $3,018.00, so the backwardation held at $25.00 - the second consecutive close beyond the $15.00 tightness trigger, which CONFIRMS it - with visible stock at another low of 235,800 t. "
 "The structure has turned but the price has not: three-month is still beneath 3,061.5 for a tenth session. Scenario weights move to 15% bull / 45% base / 40% bear on the confirmed structural signal; a settled close above 3,061.5-3,077 would add to the base/bull side, a break of 2,994.50 then 2,977.5 would reverse the shift. The daily Elliott count (wave (v) of a C-wave decline from 3,374) still leans to wave (v) complete at 2,994.50 - a settled close above 3,077 would confirm it, below about 2,977.5 would force a re-count; invalidation 3,289; the weekly corrective count towards 2,894 stays preferred.")
c2=d['commercial']
for a,b in [("FIRST, THE PROMPT PREMIUM JUMPED: a $25.00 backwardation on 22-October, up from $6.50, as cash held while three-month fell $16.50 - the first print beyond the $15.00 reversal condition, so nearby metal is now clearly valued over forward metal, though one print is not yet a squeeze.","FIRST, THE PROMPT PREMIUM IS CONFIRMED: a $25.00 backwardation on 23-October for a second consecutive official, as cash and three-month both rose $10.00 - two prints beyond the $15.00 reversal condition, so nearby metal is clearly valued over forward metal and there is no carry reward for deferring purchases, though it is still far from a squeeze."),
 ("is $1,516.50 on 22-October cash, 63.1% of the $2,403/t premium",f"is ${tl:,.2f} on 23-October cash, {share:.1f}% of the $2,403/t premium"),
 ("the 22-October official took three-month to $3,008.00, $13.50 above the 2,994.50 settled low inside the 2,980-3,000 zone and $53.50 beneath 3,061.5; energy rose again (Brent above $114, European gas the highest since late 2022);","the 23-October official took three-month to $3,018.00, $23.50 above the 2,994.50 settled low inside the 2,980-3,000 zone and $43.50 beneath 3,061.5; energy rose again (Brent $116.91, the highest since June 2022; European gas EUR 93.19/MWh);"),
 ("Norsk Hydro reports on 23-October)","Norsk Hydro's Q3 on 23-October lifted adjusted EBITDA to NOK 9,089m and moved Slovalco's first-phase restart target to end-February 2027)")]:
    assert a in c2,a; c2=c2.replace(a,b)
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=s['drivers'].replace("HELD 23-OCTOBER at 10/45/45:","PRIOR (23-OCTOBER) HELD at 10/45/45:",1)
    s['drivers']=("MOVED 24-OCTOBER to 15/45/40: the Friday 23-October official printed a $25.00 backwardation for a SECOND consecutive session - the pre-registered confirmation of the $15.00 reversal condition - with three-month up $10.00 to $3,018.00 and stock at another low; the price trigger (3,061.5-3,077) is not yet hit, so only five points move from bear to bull. ")+s['drivers']
P3={'Bull':'15%','Base':'45%','Bear':'40%'}
for s in d['outlook']['scenarios']: s['prob']=P3[s['case']]
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium's backwardation held at $25.00 on Friday's LME official - a second straight close beyond the $15 tightness trigger - as three-month rose $10.00 to $3,018.00 and stocks hit another low: the curve now confirms nearby tightness even though the price is still below its July low.",
 "points":[
 "WHAT MOVED: Friday's LME official settled cash at $3,043.00 and three-month at $3,018.00, both up $10.00; three-month is back $7.50 above its 02-January level, up $6.00 on the week, but still $43.50 below the $3,061.5 July low. Cash trades $25.00 above three-month (backwardation) for a second session and LME stock fell 225 t to a new low of 235,800 t.",
 "WHY: prompt metal remains scarce in LME sheds and Chinese ingot stocks fell for a ninth working day to about 420,000 t (SMM). Energy costs keep rising - Brent $116.91, the highest since June 2022, and European gas EUR 93.19/MWh - on reports of possible renewed US strikes on Iran and Houthi attacks on Saudi Arabia (Trading Economics).",
 "SUPPLY SIDE: more metal is coming back - EGA has half of Al Taweelah's cells running, and Norsk Hydro (Q3 results, 23-October) targets Slovalco's first 75,000 t by end-February 2027; Hydro's Q3 adjusted EBITDA rose to NOK 9,089m on higher all-in metal prices.",
 "WHAT TO WATCH: a settled close above $3,061.5-3,077 (price confirming the curve) or below $2,994.50; the 27-28 October FOMC (markets price a hold, about 76% odds of a December hike); further Gulf energy-security headlines."]}

d['feed']=([
 {"when":"Sat 24-Oct","impact":"Bullish","text":"BOARD ROLLED TO THE FRIDAY 23-OCTOBER LME OFFICIAL: cash $3,043.00 and three-month $3,018.00, both +$10.00; backwardation held at $25.00 - second consecutive print beyond the $15.00 reversal condition (confirmed); stock down 225 t to a new low of 235,800 t."},
 {"when":"Fri 23-Oct","impact":"Mixed","text":"NORSK HYDRO Q3-2026: adjusted EBITDA NOK 9,089m (Q2 NOK 8,923m; Q3-2025 NOK 5,996m); Aluminium Metal NOK 7,031m; Bauxite & Alumina down to NOK 283m on lower alumina prices and LNG costs at Alunorte; free cash flow NOK 1.4bn; Slovalco first 75,000 t targeted by end-February 2027."},
 {"when":"Fri 23-Oct","impact":"Bullish (cost)","text":"ENERGY: Brent $116.91 (+3.30%), the highest since June 2022, and TTF EUR 93.19/MWh (+3.49%) on reports of possible renewed US strikes on Iran; Saudi Aramco reportedly told Dhahran headquarters staff to work remotely amid Houthi attacks (Trading Economics)."},
 {"when":"Fri 23-Oct","impact":"Bullish","text":"SMM: China three-region aluminium ingot social inventory in the 420,000 t range on 23-October, a ninth straight working-day decline."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM: TIGHTNESS CONFIRMED. The Friday 23-October official settled cash at $3,043.00 and three-month at $3,018.00, both +0.33%, three-month back above the 02-January official and up $6.00 on the week. The backwardation held at $25.00 - the second consecutive settled print beyond the $15.00 reversal condition - and visible stock fell 225 t to a new low of 235,800 t. Copper three-month +1.23%, zinc +0.92%, nickel -1.46%."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Mixed","url":S_NH,
  "headline":"NORSK HYDRO Q3-2026 (23-October): adjusted EBITDA NOK 9,089m against NOK 8,923m in Q2 and NOK 5,996m a year earlier; Aluminium Metal NOK 7,031m (from NOK 2,732m) on higher all-in metal prices, partly offset by lower volumes and higher energy and carbon costs; Bauxite & Alumina fell to NOK 283m on lower alumina prices, LNG sourcing costs at Alunorte and BRL effects. Free cash flow NOK 1.4bn on higher working capital; shares fell about 7% on the day (Investing.com). Hydro describes the ex-China alumina market as oversupplied and ex-China primary demand as declining. READ: price leverage is intact for smelters; alumina margins are compressing."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish (cost)","url":S_BR,
  "headline":"ENERGY CLIMBS AGAIN (Trading Economics, 23/24-October): Brent rose 3.30% to $116.91, the highest since June 2022 and a third weekly gain, on expectations of renewed US strikes on Iran; continued Houthi attacks on Saudi Arabia reportedly led the US State Department to order non-essential personnel out and Saudi Aramco to tell Dhahran headquarters staff to work remotely. TTF rose 3.49% to EUR 93.19/MWh, a fourth weekly gain, with EU storage 74.62% full on 22-October. READ: smelter energy costs rise further. These reports are attributed to Trading Economics and were not independently confirmed this run."},
 {"theme":"China inventory","horizon":"0-1 month","impact":"Bullish","url":S_SMM,
  "headline":"CHINESE INGOT DESTOCKING EXTENDS (SMM, 23-October): three-region aluminium ingot social inventory stood in the 420,000 t range, falling for a ninth straight working day with all three consumption regions destocking. READ: post-holiday downstream restocking is absorbing metal inside China, a partial offset to elevated exports."},
 {"theme":"Supply","horizon":"0-6 months","impact":"Bearish","url":S_IN,
  "headline":"GULF RESTART WEIGHS ON PRODUCER EQUITIES (Investing.com/Kedia, 23-October): Indian aluminium shares fell up to 5% after EGA confirmed 631 of Al Taweelah's 1,262 cells restarted, with full output guided for Q1-2027; the same note cites International Aluminium Institute data showing September primary output of 6.014 Mt, below 6.10 Mt a year earlier."},
]+d['news']
d['news']=d['news'][:20]

hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Fri 23-Oct':
        hitc+=1
        cat['date']='Daily, from Mon 26-Oct'
        cat['event']="3,061.5 BROKEN ON TEN SETTLED OFFICIALS; THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE AND $17.00 ABOVE THE RULE-BASED CAP, RETESTED IT ON 20-OCTOBER ($2,997.00), AND HAS SINCE SETTLED $3,024.50, $3,008.00 AND $3,018.00 (23-OCTOBER). A settled close beneath about 2,977.5 would break the cap on daily wave (v) and force a re-count (extended fifth or larger correction toward the 2,894 weekly 61.8%); a settled recovery above 3,077 would signal wave (v) is complete; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289. STRUCTURE: the $15.00 backwardation reversal condition was CONFIRMED on 23-October (second consecutive print at $25.00); a return to contango would undo it."
    elif cat['date']=='Fri 23-Oct' and cat['event'].startswith('NORSK HYDRO'):
        hitc+=1
        cat['date']='Resolved Fri 23-Oct'
        cat['event']="NORSK HYDRO Q3-2026 - RESOLVED SOLID ON EARNINGS, WEAKER ON CASH: adjusted EBITDA NOK 9,089m (Q2 NOK 8,923m), Aluminium Metal NOK 7,031m; Bauxite & Alumina NOK 283m on lower alumina prices and Alunorte LNG costs; free cash flow NOK 1.4bn; Slovalco first-phase 75,000 t targeted by end-February 2027 (Hydro release via GlobeNewswire, 23-October)."
assert hitc==2,hitc
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 24-OCTOBER: CONFIRMED - the 23-October official printed a $25.00 BACKWARDATION for a second consecutive session, the stated confirmation of the reversal condition. Trend held at DOWN: the contango risk keeps receding."
RK[0]['trend']='down'
RK[4]['risk']+=" UPDATE 24-OCTOBER: LME stock fell 225 t to a new series low of 235,800 t on 23-October; SMM's Chinese three-region ingot inventory fell for a ninth working day to the 420,000 t range. Trend held at FLAT."
hit=0
for r in RK:
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 24-OCTOBER: Brent $116.91, the highest since June 2022, and TTF EUR 93.19/MWh, a fourth weekly gain (Trading Economics); Norsk Hydro's Q3 cites higher energy and carbon costs in Aluminium Metal. Trend held at UP."; hit+=1
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 24-OCTOBER: Trading Economics (23/24-October) reports continued Houthi attacks on Saudi Arabia, a US State Department order for non-essential personnel to leave, Saudi Aramco staff at Dhahran told to work remotely, and reports of US/Israeli strike planning on Iran after the US midterms (not independently confirmed this run). Trend held at UP."; hit+=1
    if r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 24-OCTOBER: the US ten-year recovered to about 5.00%; markets price about 91% odds of a hold next week and about 76% odds of a December hike (Trading Economics). Trend held at UP."; hit+=1
assert hit==3
d['outlook']['ai_analysis'].insert(0,"SATURDAY 24-OCTOBER ON THE FRIDAY 23-OCTOBER OFFICIAL: cash and three-month both rose $10.00 to $3,043.00 and $3,018.00, so the backwardation held at $25.00 - the second consecutive settled print beyond the published $15.00 reversal condition, which is now CONFIRMED - and visible stock set another low (235,800 t). The structural signal moves scenario weights to 15/45/40, but price has not confirmed: three-month is still beneath 3,061.5 for a tenth session and ex-China supply keeps returning (EGA half restarted; Slovalco's first 75,000 t by end-February 2027 per Norsk Hydro). Rising energy (Brent the highest since June 2022) supports the cost floor, while Hydro's Q3 shows smelter earnings still strong but alumina margins compressing and the ex-China alumina market oversupplied. A settled close above 3,061.5-3,077 would add to base/bull; a return to contango or a break of 2,994.50 would reverse the shift; the 27-28 October FOMC is next.")

EWS=("REVIEWED 24-OCTOBER ON THE FRIDAY 23-OCTOBER OFFICIAL: three-month settled $3,018.00, up $10.00 - a sixth settled close above the 2,994.50 low of 15-October and well clear of the rule-based cap near 2,977.5; the sequence 2,994.50 / 3,024.50 / 3,008.00 / 3,018.00 reads as a small first leg up and a shallow pullback holding above the low, consistent with a completed wave (v). Wave (v) of C ($154.00 from the 3,148.5 wave (iv) high to 2,994.50) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged, NOT re-labelled. Base case about 55%: wave (v) ended at 2,994.50 and a corrective rebound toward 3,061.5-3,077 is under way (confirmed by a settled close above 3,077); alternate about 45%: a settled close beneath 2,977.5 forces a re-count toward 2,894. The confirmed $25.00 backwardation is supportive context but not an Elliott signal. Invalidation 3,289; confidence moderate. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED 17-OCTOBER"); assert st.startswith("REVIEWED 23-OCTOBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED 17-OCTOBER"); assert lt.startswith("REVIEWED 23-OCTOBER") and k>0
d['ew']['long_term']['writeup']="REVIEWED 24-OCTOBER (FRIDAY 23-OCTOBER OFFICIAL, WEEKLY CLOSE): three-month closed the week at 3,018.00, up $6.00 on the week, in the lower part of the 2,950-3,110 zone and still beneath the 3,061.5 July low; the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label. "+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="116.91",day="$116.91 on 23-October, +3.30% (Trading Economics)",
 note="REFRESHED SATURDAY 24-OCTOBER-2026 (Trading Economics): Brent rose to $116.91, the highest since June 2022 and a third straight weekly gain, as expectations grew that the US could resume strikes on Iran and Houthi attacks on Saudi Arabia continued; Trading Economics reports the US State Department ordered non-essential personnel out and Saudi Aramco told Dhahran headquarters staff to work remotely. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="93.2",day="EUR 93.19/MWh on 23-October, +3.49% (Trading Economics)",
 note="REFRESHED SATURDAY 24-OCTOBER-2026 (Trading Economics): TTF rose to EUR 93.19/MWh, a fourth straight weekly gain of over 6%, on Persian Gulf supply disruption (Middle East LNG shipments about 80% below year-ago) and reports of possible new US strikes on Iran; EU storage was 74.62% full on 22-October, the lowest seasonal level since records began in 2009. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.75",day="101.75 on 23-October, +0.14% (Trading Economics); down about 0.2% on the week",
 note="REFRESHED SATURDAY 24-OCTOBER-2026 (Trading Economics): the dollar index edged up to about 101.75 but fell about 0.2% on the week as Treasury yields slipped on safe-haven demand; the euro was weighed by French political uncertainty. Markets price about 91% odds of a Fed hold next week and about 76% odds of a December hike. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="5.00",day="about 5.00% on 23-October, +4bp after a sharp fall on 22-October (Trading Economics)",
 note="REFRESHED SATURDAY 24-OCTOBER-2026 (Trading Economics): the yield recovered to about 5.00% after Thursday's sharp drop on a flight to safety; drivers cited are Middle East tension, AI-spending doubts and the US midterms less than two weeks away; markets price about a 91% chance of a Fed hold and about 76% odds of a December hike. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.11910',day="LME fixing on 23-October, -0.07% from 1.11990; ECB fixing 1.11930, BFIX 1.11890",
 note="REFRESHED SATURDAY 24-OCTOBER-2026 to the 23-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 23-OCTOBER-2026 LME OFFICIAL - THE LAST SESSION OF THE WEEK. This Saturday 24-October run is compiled while the market is shut (no ring on Saturday or Sunday), so the board was carried from Friday by design; the next official prints Monday 26-October 13:20 London. Reference and intraday prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (24-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 23-October session, and the per-metal aluminium daily table's newest row is 23-October (cash 3,043.00, three-month 3,018.00, stock 235,800) with NO later row, so the board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.11990, ECB 1.12050, BFIX 1.11951) matches the 22-October board verified on 23-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 22-October: aluminium -225 to 235,800; copper +800 to 273,750; nickel unchanged at 280,674; zinc -50 to 167,025; lead -1,800 to 322,175.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (23-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (seventeen sessions, 01- to 23-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,018.00; the stock chart axis floor (225,000 t) brackets visible stock at 235,800 t - both re-checked this run; the stock floor has about 10,800 t of headroom and will be re-bracketed before it is approached.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,043.00 against three-month $3,018.00 is therefore a $25.00 BACKWARDATION, unchanged from 22-October as both legs rose $10.00."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 23-October official cash of $3,043.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent ($116.91), the dollar index (about 101.75), TTF (EUR 93.19/MWh) and the US ten-year (about 5.00%) are Trading Economics readings for the 23-October close shown on 24-October; Trading Economics prices are contract-for-difference references, not official benchmarks, and its own commentary differs slightly from its quoted levels, so they are approximate; EUR/USD is the 23-October LME fixing, the same session as the board."; hit+=1
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 24-OCTOBER: the GlobeNewswire copy of Norsk Hydro's Q3 release returned HTTP 403; per the fallback, a web search was used and the same release was read from a GlobeNewswire reprint (Manila Times wire page), cross-checked against Investing.com. Sources differ on Hydro's net-debt direction (the release reprint gives adjusted net debt NOK 21.9bn against NOK 22.8bn last quarter), so only the release figures are used. No new dated SMM fluoride, silicon or magnesium figure was retrievable, so none is published. The Houthi-attack, Aramco and possible-strike reports and the Chinese September export growth figure (+25.9% y/y) rest on Trading Economics commentary only and are attributed rather than stated as fact. No Q1-2027 Japanese premium offer has been reported yet (negotiations normally start late November)."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: NORSK HYDRO REPORTED Q3-2026 ON 23-OCTOBER and is added this run (its per-company history rolled to Q3-26 at adjusted EBITDA NOK 9.1bn, Q3-25 dropped). Rio Tinto's row carries its 14-October Q3 operations note (production only). NO NEW COMPANY WAS BACK-FILLED THIS RUN. Century Aluminum has not yet announced its Q3 date; third-party calendars estimate early November, which is not published as a catalyst until the company confirms it. Other entries are carried at their last publicly verified figures, and gaps stay gaps."; hit+=1
assert hit==4,hit

# Peer earnings: replace Hydro Q2 row with Q3 row; roll Hydro history
ix=[i for i,e in enumerate(d['earnings']) if e['company']=='Norsk Hydro (NHY)']; assert len(ix)==1
d['earnings'][ix[0]]={'company':'Norsk Hydro (NHY)','group':'Aluminum producer','period':'Q3 2026','reported':'23 Oct 2026','reported_iso':'2026-10-23',
 'headline':"Q3-2026: adjusted EBITDA NOK 9,089m against NOK 8,923m in Q2 and NOK 5,996m in Q3-2025; Aluminium Metal adjusted EBITDA NOK 7,031m (Q3-2025 NOK 2,732m); Bauxite & Alumina NOK 283m (from NOK 1,290m); Energy NOK 411m (from NOK 828m). Reported net income NOK 5,263m, adjusted net income NOK 4,372m, adjusted EPS NOK 2.3 (Q3-2025 NOK 1.0). Free cash flow NOK 1.4bn, reduced by higher working capital tied to higher metal prices; adjusted net debt NOK 21.9bn (NOK 22.8bn last quarter). Capex guidance cut to about NOK 12.5bn from NOK 13.5bn; Slovalco's first restart phase targets 75,000 t/y by end-February 2027. Shares fell about 7% on the day (Investing.com).",
 'readthrough':"THE SMELTER LEG IS STILL EARNING ON PRICE, THE ALUMINA LEG IS NOT. Aluminium Metal EBITDA more than doubled year on year on higher all-in metal prices despite lower volumes and higher energy and carbon costs, while Bauxite & Alumina fell nearly 80% on lower alumina prices, LNG sourcing costs at Alunorte (about $85m in Q3, $90-110m guided for Q4 per management) and BRL effects. Hydro describes the ex-China alumina market as oversupplied and ex-China primary demand as declining, with Middle East tension keeping aluminium prices elevated - the same split as Alcoa's Q3: metal margin intact, alumina margin compressing, cash absorbed by working capital.",
 'sentiment':'Mixed','eps':None,'revenue_bn':None,'yoy_pct':51.6,'url':S_NH}
eh=d['earnings_history']['NHY']; assert eh['points'][-1][0]=='Q2-26'
eh['points']=eh['points'][1:]+[['Q3-26',9.1]]
eh['src']=["Norsk Hydro quarterly reports (adj EBITDA NOK 5.6bn / 8.7bn / 8.9bn / 9.1bn for Q4-25 to Q3-26; Q3-26 = NOK 9,089m per the 23-Oct-2026 release; Q3-25 dropped as the window rolled)",S_NH]
en=d['earnings_note']
d['earnings_note']=("NORSK HYDRO REPORTED Q3-2026 ON 23-OCTOBER (added this run): adjusted EBITDA NOK 9,089m, up from NOK 8,923m in Q2 and NOK 5,996m a year earlier, with Aluminium Metal at NOK 7,031m but Bauxite & Alumina down to NOK 283m on lower alumina prices and Alunorte LNG costs; free cash flow fell to NOK 1.4bn. Hydro's per-company history was rolled to Q3-26 (Q3-25 dropped). NO NEW COMPANY WAS BACK-FILLED INTO THE PER-COMPANY HISTORY THIS RUN; gaps stay gaps. Both Q3 producer prints so far (Alcoa, Hydro) show the same split: smelting margin intact on price, alumina margin compressing. ")+en

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 23-OCTOBER: no newer public disclosure","REVIEWED 24-OCTOBER: no newer public disclosure").replace("REVIEWED 23-OCTOBER. NO NEW DATED","REVIEWED 24-OCTOBER. NO NEW DATED")
    return o
PS={p['name']:p for p in d['producer_status']}
a=PS['Norsk Hydro (NHY) - Alunorte']; pre="REVIEWED 23-OCTOBER: no newer public disclosure located; status below carried. "; assert a['update'].startswith(pre)
a['update']=("UPDATED 24-OCTOBER FROM NORSK HYDRO'S Q3-2026 RELEASE (23-October): gas supply disruptions temporarily reduced Alunorte output; Hydro secured alternative LNG supply and restored alumina production; Bauxite & Alumina adjusted EBITDA fell to NOK 283m from NOK 1,290m, partly on higher LNG sourcing costs; management put the Q3 impact at about $85m and guided $90-110m for Q4 (earnings call, per search-located coverage). ")+a['update'][len(pre):]
a['src']=[L_NH,S_NH]
s=PS['Slovalco (Hydro / Penta JV, Slovakia)']; assert s['update'].startswith(pre)
s['status']="RESTARTING - FIRST PHASE OF 75,000 t/y (OF 175,000 t) NOW TARGETED BY END-FEBRUARY 2027 PER NORSK HYDRO'S Q3 RELEASE (EARLIER GUIDED Q4-2026); FIRST POTS RESTARTED (AL CIRCLE, SEPTEMBER)"
s['update']=("UPDATED 24-OCTOBER: Norsk Hydro's Q3-2026 release (23-October) states the first Slovalco restart phase targets 75,000 tonnes of annual capacity by end-February 2027; the July announcement had guided production resuming in Q4-2026, and AL Circle reported in September that the first pots had restarted, with 100 of 226 pots expected running by end-February 2027. ")+s['update'][len(pre):]
s['src']=[L_NH,S_NH]
c=PS['China operators (aggregate, incl. Chalco and Hongqiao)']
c['update']="UPDATED 24-OCTOBER (SMM, 23-October): three-region aluminium ingot social inventory in the 420,000 t range, a ninth straight working-day decline with all three regions destocking. "+c['update']
c['src']=[L_SMM,S_SMM]
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD
for s_ in [[L_TE,S_TE],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG],[L_NH,S_NH],[L_NHI,S_NHI],[L_SMM,S_SMM],[L_IN,S_IN]]:
    d['sources'].append(s_)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 23-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 22-Oct)",W])
d['outlook']['sources'].append([L_NH,S_NH]); d['outlook']['sources'].append([L_BR,S_BR]); d['outlook']['sources'].append([L_SMM,S_SMM])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-22'
ph['rows'][-1]=['2026-10-23',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
