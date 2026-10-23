# Daily data refresh - 2026-10-23 (FRIDAY, ~03:35 London, BEFORE the ring). Board ROLLED to THURSDAY 22-Oct LME official (latest published).
# Westmetall cache-busted EN AND DE overviews both fetched and agree on the full 22-Oct session; Al per-metal table top row = 22-Oct.
# Completeness: 5/5 stock lines reconcile vs 21-Oct board; prior FX column (MTLE 1.12290) matches 21-Oct board.
# Key: Al cash 3,033 (+2.00), 3M 3,008 (-16.50) -> BACKWARDATION $25.00 from $6.50: published reversal condition (backwardation > $15) MET; spread and 3M moved OPPOSITE.
# TE 23-Oct: Brent ~$114.12 (5-month high), TTF ~EUR91.1 (highest since late 2022), DXY ~101.66, UST10Y ~4.97% (one-month low). TE aluminium commentary: China Sept exports +25.9% y/y.
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-23'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (22/23-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (23-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (23-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (23-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (23-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
assert B['LME Cash settlement']['cur']==3031.0 and B['LME 3-month']['cur']==3024.5
cash,prev_c,m3,prev_m,stk,prev_s=3033.0,3031.0,3008.0,3024.5,236025,236125
spr=cash-m3; assert spr==25.0 and prev_s-100==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED FRIDAY 23-OCTOBER-2026 (ABOUT 03:35 LONDON, BEFORE TODAY'S RING). THE BOARD IS THE THURSDAY 22-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED OFFICIAL; Friday's prints at 13:20 London and will appear on the next run. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 22-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.11990); their prior-day FX column (MTLE 1.12290) matches the verified 21-October board, and the per-metal aluminium table's newest row is 22-October; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 21-October: aluminium 236,125 less 100 to 236,025; copper 245,275 plus 27,675 to 272,950; nickel 280,866 less 192 to 280,674; zinc 167,825 less 750 to 167,075; lead 329,300 less 5,325 to 323,975. "
 "The whole board sits on ONE UNIFORM SESSION (22-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(" CASH SETTLED $3,033.00 ON THE 22-OCTOBER OFFICIAL, UP $2.00 OR 0.07% FROM $3,031.00. THREE-MONTH SETTLED $3,008.00, DOWN $16.50 OR 0.55% - $2.50 BENEATH the first-published 2026 three-month official of $3,010.50, so aluminium is marginally NEGATIVE year to date ("+f"{ytd:+.2f}%), $13.50 above the 2,994.50 settled low of 15-October and a NINTH settled close beneath the 3,061.5 July low (by $53.50). "
 "THE BACKWARDATION WIDENED $18.50 TO $25.00 as cash edged up while three-month fell - SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS: the curve tightened while the three-month price weakened. This is the widest backwardation of the sequence tracked since 16-September and the FIRST settled official beyond the published $15.00 reversal condition. "
 "VISIBLE LME STOCK FELL 100 t TO 236,025 t, another new series low.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,033.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,008.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $53.50 BENEATH THE 3,061.5 JULY LOW, $69.00 beneath the 3,077 weekly 50% retracement and $281.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a fifth session and sits $13.50 beneath price; the rule-based cap on daily wave (v) near 2,977.5 was never touched."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+25.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,033.00 against three-month $3,008.00 is a $25.00 BACKWARDATION, WIDENED $18.50 from $6.50 as cash rose $2.00 and three-month fell $16.50 - spread and flat price moved in OPPOSITE directions. THE PUBLISHED REVERSAL CONDITION - A BACKWARDATION BEYOND $15.00 ON A SETTLED OFFICIAL - IS MET FOR THE FIRST TIME in this sequence; one print is not a trend, so a second settled official beyond $15.00 is the confirmation to watch. The bearish structural confirmation, a contango beyond $24.50, is far away. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"236,025","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 100 t TO 236,025 t, another new series low, a second straight 100 t draw. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,008.00, DOWN $16.50 - $53.50 beneath the 3,061.5 July low, a ninth settled close below it, and $2.50 BELOW the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 100 t TO 236,025 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":6.5,"avg":sep_sp,"note":VER+f" A $25.00 BACKWARDATION, WIDENED $18.50 FROM $6.50. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Cash rose $2.00 while three-month fell $16.50, so the structure TIGHTENED while the flat price WEAKENED - opposite directions. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): MET for the first time; confirmation needs a second settled official beyond $15.00."},
 {"name":"EUR/USD LME fixing","cur":1.1199,"prev":1.1229,"avg":1.1465,"note":VER+" THE LME EURO FIXING EASED TO 1.11990 FROM 1.12290 at the Thursday ring; the ECB fixing printed 1.12050 and BFIX 1.11951. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (22-Oct official)","price":"3,033.0","basis":"THE 22-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,033.00, UP $2.00 OR 0.07%. Next official Friday 23-October 13:20 London."},
 {"tenor":"3-month (22-Oct official)","price":"3,008.0","basis":"THE 22-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,008.00, DOWN $16.50 - $53.50 beneath the 3,061.5 July low (ninth settled close below it), $13.50 above the 2,994.50 October low and $2.50 below the 02-January official, so marginally negative year to date."},
 {"tenor":"Cash-to-3M structure","price":"+25.0 (BACKWARDATION)","basis":"A $25.00 BACKWARDATION, widened $18.50 as cash rose and three-month fell - the first settled print beyond the $15.00 reversal condition."},
 {"tenor":"Visible LME stock","price":"236,025 t","basis":f"DOWN 100 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE STRUCTURE TIGHTENED WHILE THE FLAT PRICE SLIPPED. On the 22-October official cash $3,033.00 sits $25.00 ABOVE three-month $3,008.00, a BACKWARDATION, widened $18.50 from $6.50 on 21-October - the spread and the three-month price moved in OPPOSITE directions. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50 and now $25.00. "
 f"READ: a sixth straight backwardation, now the widest of the sequence, while visible stock keeps setting lows (236,025 t) - prompt metal is being valued over forward metal. The published reversal condition (a backwardation beyond $15.00) is MET for the first time; a second settled official beyond $15.00 would confirm it. The September mean spread was ${sep_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]

ls=d['lme_series']; assert ls[-1][0]=='21-Oct', ls[-1]
d['lme_series']=ls[1:]+[["22-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14215.0,14096.0,14441.0,14315.0); NI=(15935.0,16135.0,15830.0,16040.0); ZN=(3727.0,3692.0,3771.0,3724.0); PB=(1872.0,1897.0,1880.0,1904.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average-to-date: 15 sessions to 21-Oct (14 listed in 22-Oct script + 21-Oct) + 22-Oct
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0,3736.0,3771.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0,1851.0,1880.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/16)/(sum(zs)/15),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/16)/(sum(ps)/15),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-22'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending THURSDAY 22-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 01-October dropped and 22-October appended, so the window is 02-October to 22-October. Every point is an official cash settlement; the 22-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 21-October. Next official Friday 23-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (22-October-2026 session; stock lines reconciled against 21-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,215.00, down $226.00 or 1.57%; three-month $14,096.00, down $219.00 or 1.53% - the weakest metal on the board. The BACKWARDATION NARROWED to $119.00 from $126.00, alongside the largest stock inflow on the board for a second session - 27,675 tonnes, lifting stock to 272,950 t, a fourth straight rise."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,935.00, up $105.00 or 0.66%; three-month $16,135.00, up $95.00 or 0.59% - the only metal up on the three-month board. CONTANGO $200.00 from $210.00, still the widest carry on the board. Stock fell 192 tonnes to 280,674."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,727.00, down $44.00 or 1.17%; three-month $3,692.00, down $32.00 or 0.86%. BACKWARDATION narrowed to $35.00 from $47.00. Stock fell 750 tonnes to 167,075 t, ending an eight-session run of inflows. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,872.00, down $8.00 or 0.42%; three-month $1,897.00, down $7.00 or 0.37%. CONTANGO $25.00 from $24.00. Stock drew 5,325 tonnes to 323,975, a twenty-fourth consecutive draw."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Thursday 22-October official the board turned mostly lower - copper three-month -1.53%, zinc -0.86%, aluminium -0.55% and lead -0.37%, with nickel the exception at +0.59% - while Trading Economics reported a flight to safety (US ten-year yield near 4.97%, a one-month low) on equity volatility and Middle East tension. The LME euro fixing eased to 1.1199.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='21-Oct'
        i['hist']=i['hist'][1:]+[["22-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,096.00 (3M); 14,215.00 (cash) $/t"
        i['ratio']="~14,215.00 $/t cash vs LME 3M 14,096.00 $/t"
        i['trend']='down'
        i['src']=("LME official cash settlement, rolled to the THURSDAY 22-OCTOBER-2026 session at $14,215.00, DOWN $226.00 or 1.57% against $14,441.00. THE WINDOW ROLLED THIS RUN: 01-October dropped and 22-October appended, so the series is the last fifteen published official cash sessions, 02-October to 22-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 21-October). "
                  "Copper structure for context: backwardation $119.00 (from $126.00), stock rose 27,675 t to 272,950 t.")
d['inputs_summary']=("UPDATE 23-OCTOBER: Copper rolled to the Thursday 22-October LME official cash of $14,215.00, down $226.00, with its fifteen-session window moved to 02-October to 22-October. No new monthly carbon settlement is due until mid-November; the October cycle (Mysteel, 16-October: Shandong prebaked-anode benchmark +Yuan 400/t to Yuan 6,130/t; green petcoke 3B Yuan 3,610.5/t) remains the latest and is already in the histories. No new dated SMM fluoride, silicon or magnesium mark was retrievable this run. Energy inputs got MORE expensive - Brent above $114, a five-month high, and European gas about EUR 91/MWh, the highest since late 2022, with EU storage at 74.58%, the lowest for the season since 2009 (Trading Economics, 23-October). Every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 21-October official cash of \$3,031\.00, or \$1,515\.50, UP \$13\.75 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$887\.50, so 63\.1%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 22-October official cash of $3,033.00, or ${tl:,.2f}, UP $1.00 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED THURSDAY 22-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE WEDNESDAY 21-OCTOBER OFFICIAL)."; NEWC="COMPILED FRIDAY 23-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE THURSDAY 22-OCTOBER OFFICIAL)."
n=0
for p in d['premiums']:
    p['src'],k=OLDT.subn(NEWT,p['src']); n+=k
    p['src']=p['src'].replace(OLDC,NEWC)
print('premium tariff replaced',n); assert n==len(d['premiums'])
ra=360.40/m3*100; na=0
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    o="THE RATIO: LME Alumina at $360.40/t against the 21-October aluminium three-month of $3,024.50 is 11.92%"
    if o in s: na+=1
    s=s.replace(o,f"THE RATIO: LME Alumina at $360.40/t against the 22-October aluminium three-month of $3,008.00 is {ra:.2f}%")
    a['src']=s
print('alumina',na,len(d['alumina'])); assert na==len(d['alumina'])

d['lme_commentary']=("THE CURVE TIGHTENS AS THE PRICE SLIPS. On the Thursday 22-October official cash settled $3,033.00 (+$2.00) while three-month fell $16.50 to $3,008.00 - $2.50 beneath the 02-January three-month official, so fractionally negative for 2026 again, but $13.50 above the 15-October settled low of 2,994.50 and $53.50 beneath the 3,061.5 July low. "
 "The backwardation jumped $18.50 to $25.00 - the widest of the sequence since mid-September and the first settled print beyond the published $15.00 reversal condition - and visible stock fell 100 t to another series low of 236,025 t. Spread and flat price moved in opposite directions. Most of the board fell: copper -1.5% as another 27,675 t were delivered into LME sheds, zinc -0.9%, lead -0.4%; nickel +0.6%. "
 "Macro was risk-off: Trading Economics reported a flight to safety into bonds (US ten-year near 4.97%) on equity volatility and Middle East tension, while Brent rose above $114 and European gas above EUR 89/MWh on reports of possible renewed strikes on Iran. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND STILL IN CONTROL ON PRICE, BUT THE STRUCTURE HAS TURNED. Against: three-month has settled beneath 3,061.5 nine times and slipped back below the year's opening level; Gulf supply is returning - EGA has half of Al Taweelah's 1,262 cells restarted (21-October) and guides full output in Q1-2027; China ran a record Q3 and Trading Economics reports Chinese aluminium exports up 25.9% year on year in September; a December Fed hike is still priced (about 76%). "
 "Constructive: the backwardation widened to $25.00, the first settled print beyond the $15.00 reversal condition; visible LME stock fell to another low of 236,025 t; the 2,994.50 October low has held for five sessions; Chinese ingot stocks fell 103,000 t over the two post-holiday weeks (SMM); energy costs rose again - Brent above $114, European gas the highest since late 2022 - which lifts the smelter cost floor.")
d['bottom_line']=("BOTTOM LINE: on the Thursday 22-October LME official three-month aluminium slipped $16.50 to $3,008.00 while cash held at $3,033.00, so the backwardation widened to $25.00 - the first close beyond the $15.00 tightness trigger - with visible stock at another low of 236,025 t. "
 "Price and structure disagree: the trend is still down (nine settled closes beneath 3,061.5) but prompt metal is tightening and energy costs are rising. Scenario weights are held at 10% bull / 45% base / 45% bear pending a second backwardation print beyond $15.00 or a price trigger; the daily Elliott count (wave (v) of a C-wave decline from 3,374) still leans to wave (v) complete at 2,994.50 - a settled close above 3,077 would confirm it, below about 2,977.5 would force a re-count; invalidation 3,289; the weekly corrective count towards 2,894 stays preferred.")
c2=d['commercial']
for a,b in [("FIRST, THE PROMPT STILL HOLDS A SMALL PREMIUM: a $6.50 backwardation on 21-October, unchanged as the flat price rose $27.50, so there is no carry reward for waiting, though it is far from a squeeze.","FIRST, THE PROMPT PREMIUM JUMPED: a $25.00 backwardation on 22-October, up from $6.50, as cash held while three-month fell $16.50 - the first print beyond the $15.00 reversal condition, so nearby metal is now clearly valued over forward metal, though one print is not yet a squeeze."),
 ("is $1,515.50 on 21-October cash, 63.1% of the $2,403/t premium",f"is ${tl:,.2f} on 22-October cash, {share:.1f}% of the $2,403/t premium"),
 ("the 21-October official lifted three-month to $3,024.50, $30.00 above the 2,994.50 settled low inside the 2,980-3,000 zone but $37.00 beneath 3,061.5;","the 22-October official took three-month to $3,008.00, $13.50 above the 2,994.50 settled low inside the 2,980-3,000 zone and $53.50 beneath 3,061.5; energy rose again (Brent above $114, European gas the highest since late 2022);")]:
    assert a in c2,a; c2=c2.replace(a,b)
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 23-OCTOBER at 10/45/45: the Thursday 22-October official took three-month down $16.50 to $3,008.00 while the backwardation widened to $25.00 - the first settled print beyond the $15.00 reversal condition - and stock set a new low; price and structure point opposite ways, and neither pre-registered price trigger (2,977.5 / 3,077) was hit, so weights are held pending a second backwardation print beyond $15.00. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium three-month slipped $16.50 to $3,008.00 on Thursday's LME official, but cash held and the backwardation jumped to $25.00 with stocks at another low - the first sign in this run of data that nearby metal is tightening even as the price drifts.",
 "points":[
 "WHAT MOVED: Thursday's LME official settled cash at $3,033.00 (+$2.00) and three-month at $3,008.00 (-$16.50), $2.50 below the 02-January level and $53.50 below the $3,061.5 July low, but still above the $2,994.50 October low. Cash now trades $25.00 above three-month (backwardation, up from $6.50) - price and spread moved in opposite directions - and LME stock fell 100 t to a new low of 236,025 t.",
 "WHY: the base-metals board was risk-off - copper fell 1.5% as another 27,675 t arrived in LME sheds - amid a flight to safety into bonds (Trading Economics), while prompt aluminium stayed scarce. Energy costs rose: Brent above $114 (a five-month high) and European gas above EUR 89/MWh (the highest since late 2022) on reports of possible new strikes on Iran.",
 "SUPPLY SIDE: Gulf restarts continue (EGA has half of Al Taweelah's cells back) and Trading Economics reports Chinese aluminium exports up 25.9% year on year in September - more metal is available outside China.",
 "WHAT TO WATCH: whether a second official prints a backwardation above $15.00 (confirming tightness); a settled close above $3,061.5-3,077 or below $2,994.50; Norsk Hydro's Q3 results on Friday 23-October; the 27-28 October FOMC (markets price a hold)."]}

d['feed']=([
 {"when":"Fri 23-Oct","impact":"Mixed","text":"BOARD ROLLED TO THE THURSDAY 22-OCTOBER LME OFFICIAL: cash $3,033.00 (+$2.00), three-month $3,008.00 (-$16.50), back fractionally below the 02-January level; backwardation widened to $25.00 from $6.50 - first print beyond the $15.00 reversal condition; stock down 100 t to a new low of 236,025 t."},
 {"when":"Fri 23-Oct","impact":"Bullish (cost)","text":"ENERGY: Brent above $114, a five-month high, and TTF gas about EUR 91/MWh, the highest since late 2022, on reports of possible renewed US/Israeli strikes on Iran (Trading Economics)."},
 {"when":"Thu 22-Oct","impact":"Bearish","text":"Trading Economics: Chinese aluminium exports rose 25.9% year on year in September, the highest monthly level in three months; Gulf output still depressed but recovering."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Mixed","url":W,
  "headline":"LME ALUMINIUM: CURVE TIGHTENS AS PRICE SLIPS. The Thursday 22-October official settled cash at $3,033.00 (+0.07%) and three-month at $3,008.00 (-0.55%), $2.50 below the 02-January three-month official and $13.50 above the 15-October settled low. The backwardation widened $18.50 to $25.00 - the first settled print beyond the $15.00 reversal condition - and visible stock fell 100 t to a new low of 236,025 t. Copper three-month fell 1.53% as LME copper stock rose 27,675 t; nickel +0.59%."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish (cost)","url":S_BR,
  "headline":"ENERGY SPIKES AGAIN (Trading Economics, 23-October): Brent climbed above $114, its highest in over five months, on Houthi attacks on Saudi targets and reports of possible renewed US strikes on Iran, even as Persian Gulf crude exports are near pre-war levels. EU TTF gas rose above EUR 89/MWh on Thursday, the highest since late 2022, with Middle East LNG exports about 80% below year-ago levels and EU storage 74.58% full on 21-October, the lowest for the season since 2009. READ: European and Gulf smelter energy costs rise further. These reports are attributed to Trading Economics and were not independently confirmed this run."},
 {"theme":"China trade","horizon":"0-3 months","impact":"Bearish","url":S_TE,
  "headline":"CHINESE EXPORTS RISE (Trading Economics, 22-October): Chinese aluminium exports rose 25.9% year on year in September to their highest monthly level in three months, with domestic output near record levels despite the 45 Mt capacity cap; Indonesian exports exceeded 150,000 t in August. READ: more metal is reaching ex-China markets, which caps the LME price even as LME stocks fall."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Mixed","url":S_TY,
  "headline":"FLIGHT TO SAFETY (Trading Economics, 22/23-October): the US ten-year yield fell more than 10 basis points to about 4.97%, a one-month low, on equity volatility around AI valuations and Middle East tension; the dollar index held near 101.7. Markets price about a 90% chance of a Fed hold next week and about 76% odds of a December hike. READ: lower carry cost helps, but risk-off weighed on industrial metals."},
]+d['news']
d['news']=d['news'][:20]

hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Thu 22-Oct':
        hitc+=1
        cat['date']='Daily, from Fri 23-Oct'
        cat['event']="3,061.5 BROKEN ON NINE SETTLED OFFICIALS; THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE AND $17.00 ABOVE THE RULE-BASED CAP, RETESTED IT ON 20-OCTOBER ($2,997.00), BOUNCED TO $3,024.50 ON 21-OCTOBER AND EASED TO $3,008.00 ON 22-OCTOBER WHILE THE BACKWARDATION WIDENED TO $25.00. A settled close beneath about 2,977.5 would break the cap on daily wave (v) and force a re-count (extended fifth or larger correction toward the 2,894 weekly 61.8%); a settled recovery above 3,077 would signal wave (v) is complete; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289. STRUCTURE: a second settled backwardation beyond $15.00 would confirm the reversal condition first met on 22-October."
assert hitc==1
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 23-OCTOBER: THE PUBLISHED REVERSAL CONDITION WAS MET - the 22-October official printed a $25.00 BACKWARDATION, up from $6.50, as cash held and three-month fell $16.50; it is the sixth straight backwardation and the widest of the sequence since 16-September. Trend moved from FLAT to DOWN: the contango risk is receding; a second print beyond $15.00 would confirm it."
RK[0]['trend']='down'
RK[4]['risk']+=" UPDATE 23-OCTOBER: LME stock fell 100 t to a new series low of 236,025 t on 22-October. Trend held at FLAT."
hit=0
for r in RK:
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 23-OCTOBER: Brent above $114, a five-month high, and TTF above EUR 89/MWh, the highest since late 2022, with EU storage at 74.58% (Trading Economics). Trend held at UP."; hit+=1
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 23-OCTOBER: Trading Economics (23-October) reports Houthi attacks on Saudi targets and reports of possible renewed US and Israeli strikes on Iran, while Persian Gulf crude exports are near pre-war levels and Middle East LNG exports run about 80% below year-ago (not independently confirmed this run). Trend held at UP."; hit+=1
    if r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 23-OCTOBER: the US ten-year fell to about 4.97%, a one-month low, on a flight to safety; markets still price about 76% odds of a December hike (Trading Economics). Trend held at UP."; hit+=1
assert hit==3
d['outlook']['ai_analysis'].insert(0,"FRIDAY 23-OCTOBER ON THE THURSDAY 22-OCTOBER OFFICIAL: three-month fell $16.50 to $3,008.00, still above the 2,994.50 October low, but cash held at $3,033.00 so the backwardation widened to $25.00 - the first settled print beyond the published $15.00 reversal condition - and visible stock set another low (236,025 t). Price and structure now disagree: the flat price is being held down by a risk-off base-metals board (copper -1.5% on a 27,675 t stock inflow) and by more ex-China supply (Trading Economics reports Chinese aluminium exports +25.9% y/y in September; EGA half restarted), while prompt tightness and rising energy costs (Brent above $114, TTF the highest since late 2022) argue for a firmer floor. Weights held at 10/45/45; a second backwardation beyond $15.00 or a settled close above 3,061.5-3,077 would tilt them toward base/bull, a break of 2,994.50 then 2,977.5 bearish; Norsk Hydro's Q3 on 23-October and the 27-28 October FOMC are next.")

EWS=("REVIEWED 23-OCTOBER ON THE THURSDAY 22-OCTOBER OFFICIAL: three-month settled $3,008.00, down $16.50 - a fifth settled close above the 2,994.50 low of 15-October and still clear of the rule-based cap near 2,977.5; the pullback from 3,024.50 reads as a small corrective dip inside the first leg of a rebound, not a new low. Wave (v) of C ($154.00 from the 3,148.5 wave (iv) high to 2,994.50) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged, NOT re-labelled. Base case trimmed to about 55%: wave (v) ended at 2,994.50 and a corrective rebound toward 3,061.5-3,077 is under way (confirmed by a settled close above 3,077); alternate about 45%: a settled close beneath 2,977.5 forces a re-count toward 2,894. The widening backwardation ($25.00) is supportive context but not an Elliott signal. Invalidation 3,289; confidence moderate. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED 17-OCTOBER"); assert st.startswith("REVIEWED 22-OCTOBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED 17-OCTOBER"); assert lt.startswith("REVIEWED 22-OCTOBER") and k>0
d['ew']['long_term']['writeup']="REVIEWED 23-OCTOBER (THURSDAY 22-OCTOBER OFFICIAL): three-month eased to 3,008.00, in the lower part of the 2,950-3,110 zone and still beneath the 3,061.5 July low; the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label. "+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="114.12",day="about $114.12 on 23-October, +0.84% (Trading Economics; stats section $114.15, +0.87%)",
 note="REFRESHED FRIDAY 23-OCTOBER-2026 (Trading Economics): Brent climbed above $114, its highest in over five months, as Houthi attacks on Saudi targets and reports of possible renewed US strikes on Iran raised Middle East supply concerns, although Persian Gulf crude exports have recovered close to pre-war levels. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="91.1",day="about EUR 91.08/MWh on 23-October, +1.15% (Trading Economics; stats section EUR 91.19, +1.27%)",
 note="REFRESHED FRIDAY 23-OCTOBER-2026 (Trading Economics): TTF climbed above EUR 89/MWh on Thursday, the highest since late 2022, on reports of possible new US and Israeli strikes on Iran; Middle East LNG exports run about 80% below year-ago levels; EU storage was 74.58% full on 21-October, the lowest seasonal level since records began in 2009. Value approximate. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.7",day="about 101.66 on 23-October, +0.01% (Trading Economics)",
 note="REFRESHED FRIDAY 23-OCTOBER-2026 (Trading Economics): the dollar traded little changed around 101.7, near three-week lows, as doubts about the AI trade and Middle East tension pushed safe-haven demand toward the yen and Swiss franc; markets price about 89% odds of a Fed hold next week and about 76% odds of a December hike. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="4.97",day="about 4.97% on 23-October, after falling more than 10bp on 22-October (Trading Economics)",
 note="REFRESHED FRIDAY 23-OCTOBER-2026 (Trading Economics): the yield fell more than 10 basis points to almost 5%, its lowest in about a month, on a broad flight to safety triggered by equity volatility and Middle East tension; markets price about a 90% chance of a Fed hold and about 76% odds of a December hike. Lower yields reduce the cost of carrying metal. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.11990',day="LME fixing on 22-October, -0.27% from 1.12290; ECB fixing 1.12050, BFIX 1.11951",
 note="REFRESHED FRIDAY 23-OCTOBER-2026 to the 22-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE THURSDAY 22-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED OFFICIAL. This Friday 23-October run is compiled about 03:35 London, BEFORE today's ring; Friday's official prints at 13:20 London and will appear on the next run. Reference and intraday prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (23-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 22-October session, and the per-metal aluminium daily table's newest row is 22-October (cash 3,033.00, three-month 3,008.00, stock 236,025), so the board is current rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.12290, ECB 1.12340, BFIX 1.12292) matches the 21-October board verified on 22-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 21-October: aluminium -100 to 236,025; copper +27,675 to 272,950; nickel -192 to 280,674; zinc -750 to 167,075; lead -5,325 to 323,975.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (22-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (sixteen sessions, 01- to 22-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,008.00; the stock chart axis floor (225,000 t) brackets visible stock at 236,025 t - both re-checked this run; the stock floor has about 11,000 t of headroom and will be re-bracketed before it is approached.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,033.00 against three-month $3,008.00 is therefore a $25.00 BACKWARDATION, widened from $6.50 on 21-October as cash rose $2.00 and three-month fell $16.50 - spread and flat price moved in OPPOSITE directions."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 22-October official cash of $3,033.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $114.12), the dollar index (about 101.7), TTF (about EUR 91.1/MWh) and the US ten-year (about 4.97%) are Trading Economics readings shown on 23-October (early Friday trading) - the source's own sections differ slightly, so they are approximate; EUR/USD is the 22-October LME fixing, the same session as the board."; hit+=1
    if cv.startswith("FETCH NOTE 22-OCTOBER"):
        C[i]=("FETCH NOTE 23-OCTOBER: AL Circle's news index returned HTTP 403 and an SMM morning-meeting note returned HTTP 500 this run; per the fallback, web searches were used. No new dated SMM inventory, fluoride, silicon or magnesium figure was retrievable, so none is published. The Houthi-attack and possible-strike reports and the Chinese September export growth figure (+25.9% y/y) rest on Trading Economics commentary only and are attributed rather than stated as fact; a search did not locate the official customs total this run. No Q1-2027 Japanese premium offer has been reported yet (negotiations normally start late November)."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: NO NEW EARNINGS WERE REPORTED BY TRACKED PEERS SINCE ALCOA (15-October); NORSK HYDRO REPORTS Q3 ON FRIDAY 23-OCTOBER, AFTER THIS RUN WAS COMPILED, and will be added on the next run. Rio Tinto's row carries its 14-October Q3 operations note (production only). NO NEW COMPANY WAS BACK-FILLED THIS RUN. Other entries are carried at their last publicly verified figures, and gaps stay gaps."; hit+=1
assert hit==4,hit

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 22-OCTOBER: no newer public disclosure","REVIEWED 23-OCTOBER: no newer public disclosure").replace("REVIEWED 22-OCTOBER. NO NEW DATED","REVIEWED 23-OCTOBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD
for s in [[L_TE,S_TE],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG]]:
    d['sources'].append(s)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 22-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 21-Oct)",W])
d['outlook']['sources'].append([L_TE,S_TE]); d['outlook']['sources'].append([L_BR,S_BR])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-21'
ph['rows'][-1]=['2026-10-22',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
