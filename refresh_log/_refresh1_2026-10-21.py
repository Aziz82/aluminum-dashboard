# Daily data refresh - 2026-10-21 (WEDNESDAY, ~03:35 London, BEFORE the ring). Board ROLLED to TUESDAY 20-Oct LME official (latest published).
# Westmetall cache-busted EN AND DE overviews both fetched and agree on the full 20-Oct session; Al per-metal table top row = 20-Oct.
# Completeness: 5/5 stock lines reconcile vs 19-Oct board; prior FX column (MTLE 1.12290) matches 19-Oct board.
# New public items: SMM 20-Oct three-region ingot stock ~450kt, sixth straight destock day, -9kt; A00 spot premium Y280-300/t;
# TE 21-Oct Brent ~$110.35 (+1.44%), TTF ~EUR87.0 (+2.29%), EU storage 74.62% (lowest seasonal since 2009), DXY ~101.77, UST10Y 5.13%.
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-21'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (20/21-Oct-2026)"
S_SM="https://news.metal.com/newscontent/104169087-aluminum-prices-persistently-low-spot-premiums-fluctuate-at-highs-smm-spot-aluminum-midday-review"; L_SM="SMM - Aluminum prices persistently low, spot premiums fluctuate at highs (Spot Aluminum Midday Review, 20-Oct-2026)"
S_SI="https://news.metal.com/newscontent/104166636-october-20-2026-smm-daily-inventory-data-of-aluminum-ingots-in-three-regions-smm-data"; L_SI="SMM - October 20, 2026 daily inventory data of aluminum ingots in three regions (20-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (21-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (21-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (21-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (21-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
assert B['LME Cash settlement']['cur']==3019.0 and B['LME 3-month']['cur']==3012.0
cash,prev_c,m3,prev_m,stk,prev_s=3003.5,3019.0,2997.0,3012.0,236225,236375
spr=cash-m3; pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100
assert spr==6.5 and prev_s-150==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED WEDNESDAY 21-OCTOBER-2026 (ABOUT 03:35 LONDON, BEFORE TODAY'S RING). THE BOARD IS THE TUESDAY 20-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED OFFICIAL; Wednesday's prints at 13:20 London and will appear on the next run. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 20-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.12110); their prior-day FX column (MTLE 1.12290) matches the verified 19-October board, and the per-metal aluminium table's newest row is 20-October; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 19-October: aluminium 236,375 less 150 to 236,225; copper 232,175 plus 1,625 to 233,800; nickel 280,110 plus 756 to 280,866; zinc 163,050 plus 3,275 to 166,325; lead 338,125 less 3,925 to 334,200. "
 "The whole board sits on ONE UNIFORM SESSION (20-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(" CASH SETTLED $3,003.50 ON THE 20-OCTOBER OFFICIAL, DOWN $15.50 OR 0.51% FROM $3,019.00. THREE-MONTH SETTLED $2,997.00, DOWN $15.00 OR 0.50% - now $13.50 BENEATH the first-published 2026 three-month official of $3,010.50, so aluminium is NEGATIVE year to date ("+f"{ytd:+.2f}%), a SEVENTH settled close beneath the 3,061.5 July low (by $64.50), and only $2.50 above the 2,994.50 settled low of 15-October. "
 "THE BACKWARDATION NARROWED to $6.50 from $7.00 as cash and three-month fell almost together - spread and flat price moved in the SAME direction. "
 "VISIBLE LME STOCK FELL 150 t TO 236,225 t, another new series low.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,003.5","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"2,997.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $64.50 BENEATH THE 3,061.5 JULY LOW, $80.00 beneath the 3,077 weekly 50% retracement and $292.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 still holds - by only $2.50 - and sits $17.00 above the rule-based cap on daily wave (v) near 2,977.5 (three-month is $19.50 above that cap)."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+6.5","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,003.50 against three-month $2,997.00 is a $6.50 BACKWARDATION, narrowed from $7.00 as both legs fell by similar amounts. The reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is still UNMET; the bearish structural confirmation, a contango beyond $24.50, is also unmet. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"236,225","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 150 t TO 236,225 t, another new series low, though the draw slowed sharply from 1,500 t the session before. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $2,997.00, DOWN $15.00 - $64.50 beneath the 3,061.5 July low, a seventh settled close below it, and $13.50 BELOW the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 150 t TO 236,225 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":7.0,"avg":sep_sp,"note":VER+f" A $6.50 BACKWARDATION, NARROWED FROM $7.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Cash fell $15.50 and three-month $15.00, so structure barely moved while the flat price fell. REVERSAL CONDITION, RESTATED UNCHANGED: a BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1211,"prev":1.1229,"avg":1.1465,"note":VER+" THE LME EURO FIXING EASED TO 1.12110 FROM 1.12290 at the Tuesday ring; the ECB fixing printed 1.12150 and BFIX 1.12092. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (20-Oct official)","price":"3,003.5","basis":"THE 20-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,003.50, DOWN $15.50 OR 0.51%. Next official Wednesday 21-October 13:20 London."},
 {"tenor":"3-month (20-Oct official)","price":"2,997.0","basis":"THE 20-OCTOBER-2026 OFFICIAL THREE-MONTH OF $2,997.00, DOWN $15.00 - $64.50 beneath the 3,061.5 July low (seventh settled close below it) and $13.50 below the 02-January official, so negative year to date."},
 {"tenor":"Cash-to-3M structure","price":"+6.5 (BACKWARDATION)","basis":"A $6.50 BACKWARDATION, narrowed from $7.00 as both legs fell."},
 {"tenor":"Visible LME stock","price":"236,225 t","basis":f"DOWN 150 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE FLAT PRICE GAVE BACK, THE STRUCTURE HELD. On the 20-October official cash $3,003.50 sits $6.50 ABOVE three-month $2,997.00, a BACKWARDATION, narrowed from $7.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00, $7.00 and now $6.50. "
 f"READ: a fourth straight backwardation while visible stock keeps setting lows (236,225 t) - a modest prompt-tightness signal that has not stopped the flat price slipping. The September mean spread was ${sep_sp:,.2f}. The reversal condition (a backwardation beyond $15.00) is unmet; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]

ls=d['lme_series']; assert ls[-1][0]=='19-Oct', ls[-1]
d['lme_series']=ls[1:]+[["20-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
# (cash, 3M, prev cash, prev 3M)
CU=(14540.0,14357.0,14496.0,14378.0); NI=(15350.0,15570.0,15275.0,15490.0); ZN=(3736.0,3695.0,3776.0,3737.0); PB=(1851.0,1894.0,1856.0,1891.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average-to-date: 13 sessions to 19-Oct (per 20-Oct script) + 20-Oct
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/14)/(sum(zs)/13),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/14)/(sum(ps)/13),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-20'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending TUESDAY 20-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 29-September dropped and 20-October appended, so the window is 30-September to 20-October. Every point is an official cash settlement; the 20-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 19-October. Next official Wednesday 21-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (20-October-2026 session; stock lines reconciled against 19-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,540.00, up $44.00 or 0.30%; three-month $14,357.00, down $21.00 or 0.15%. The BACKWARDATION WIDENED to $183.00 from $118.00 - spread and flat three-month moved in OPPOSITE directions, a firmer prompt against a softer forward. Stock rose a second session, by 1,625 tonnes to 233,800."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,350.00, up $75.00 or 0.49%; three-month $15,570.00, up $80.00 or 0.52% - the strongest metal on the board this session. CONTANGO $220.00 from $215.00, still the widest carry on the board. Stock rose 756 tonnes to 280,866."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,736.00, down $40.00 or 1.06%; three-month $3,695.00, down $42.00 or 1.12% - the weakest metal on the board this session. BACKWARDATION $41.00 from $39.00 as another 3,275 tonnes were delivered in, lifting stock to 166,325 t - a seventh straight inflow. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,851.00, down $5.00 or 0.27%; three-month $1,894.00, up $3.00 or 0.16%. CONTANGO widened to $43.00 from $35.00. Stock drew 3,925 tonnes to 334,200, a twenty-second consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Tuesday 20-October official the board split again - nickel three-month +0.52% and lead +0.16%, copper -0.15%, aluminium -0.50% and zinc -1.12% - while the dollar index slipped toward 101.5, a three-week low (Trading Economics). The LME euro fixing eased to 1.1211.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='19-Oct'
        i['hist']=i['hist'][1:]+[["20-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,357.00 (3M); 14,540.00 (cash) $/t"
        i['ratio']="~14,540.00 $/t cash vs LME 3M 14,357.00 $/t"
        i['trend']='flat'
        i['src']=("LME official cash settlement, rolled to the TUESDAY 20-OCTOBER-2026 session at $14,540.00, UP $44.00 or 0.30% against $14,496.00. THE WINDOW ROLLED THIS RUN: 29-September dropped and 20-October appended, so the series is the last fifteen published official cash sessions, 30-September to 20-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 19-October). "
                  "Copper structure for context: backwardation $183.00 (from $118.00), stock rose 1,625 t to 233,800 t.")
d['inputs_summary']=("UPDATE 21-OCTOBER: Copper rolled to the Tuesday 20-October LME official cash of $14,540.00, up $44.00, with its fifteen-session window moved to 30-September to 20-October. No new monthly carbon settlement is due until mid-November; the October cycle (Mysteel, 16-October: Shandong prebaked-anode benchmark +Yuan 400/t to Yuan 6,130/t; green petcoke 3B Yuan 3,610.5/t) remains the latest and is already in the histories. No new dated SMM fluoride, silicon or magnesium mark was retrievable this run. Energy inputs stay expensive - Brent about $110 and European gas about EUR 87/MWh with EU storage at 74.6%, the lowest for the season since 2009 (Trading Economics, 21-October). Every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 19-October official cash of \$3,019\.00, or \$1,509\.50, UP \$2\.50 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$893\.50, so 62\.8%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 20-October official cash of $3,003.50, or ${tl:,.2f}, DOWN $7.75 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED TUESDAY 20-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE MONDAY 19-OCTOBER OFFICIAL)."; NEWC="COMPILED WEDNESDAY 21-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE TUESDAY 20-OCTOBER OFFICIAL)."
n=0
for p in d['premiums']:
    p['src'],k=OLDT.subn(NEWT,p['src']); n+=k
    p['src']=p['src'].replace(OLDC,NEWC)
print('premium tariff replaced',n); assert n==len(d['premiums'])
ra=360.40/m3*100; na=0
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    o="THE RATIO: LME Alumina at $360.40/t against the 19-October aluminium three-month of $3,012.00 is 11.97%"
    if o in s: na+=1
    s=s.replace(o,f"THE RATIO: LME Alumina at $360.40/t against the 20-October aluminium three-month of $2,997.00 is {ra:.2f}%")
    a['src']=s
assert na==len(d['alumina'])

d['lme_commentary']=("ALUMINIUM SLIPS BELOW WHERE THE YEAR STARTED. On the Tuesday 20-October official cash settled $3,003.50, down $15.50, and three-month $2,997.00, down $15.00 - $13.50 beneath the 02-January three-month official, so the metal is now negative for 2026, $64.50 beneath the 3,061.5 July low and only $2.50 above the 15-October settled low of 2,994.50. "
 "The backwardation narrowed only slightly to $6.50 from $7.00, and visible stock fell 150 t to another series low of 236,225 t. The board split: nickel +0.5%, copper three-month -0.15% while its backwardation widened to $183, zinc -1.1%. "
 "In China, SMM reported three-region ingot stocks near 450,000 t after a sixth straight working day of destocking (down 9,000 t on 20-October), with spot premiums high at Yuan 280-300/t but downstream buyers purchasing only as needed and SHFE futures stuck at low levels. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND STILL IN CONTROL; PRICE IS PRESSING THE OCTOBER LOW. Against: three-month has settled beneath 3,061.5 seven times and is now below the year's opening official; China ran a record Q3 at an annualised pace of about 46.7 Mt, above its 45 Mt cap, and its September primary imports fell 30% y/y; Chinese downstream buying is hand-to-mouth (SMM); a December Fed hike is still priced; Gulf restarts continue. "
 "Constructive: visible LME stock fell to another 21st-century low of 236,225 t and the curve stays in backwardation ($6.50); Chinese ingot stocks are drawing (six straight days, ~450 kt); carbon costs jumped (October anode benchmark Yuan 6,130/t) and energy stays expensive - Brent about $110, European gas about EUR 87/MWh with EU storage the lowest for the season since 2009 - which lifts the smelter cost floor.")
d['bottom_line']=("BOTTOM LINE: aluminium fell on the Tuesday 20-October LME official - cash $3,003.50 (-$15.50), three-month $2,997.00 (-$15.00) - below the year's opening level and $64.50 beneath the 3,061.5 July low. "
 "The backwardation held at $6.50 and visible stock fell to another low of 236,225 t, while China's record Q3 output keeps the supply side heavy. Scenario weights are held at 10% bull / 45% base / 45% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) is under test - the 2,994.50 settled low is only $2.50 away; a settled close above 3,077 would confirm wave (v) complete, below about 2,977.5 would force a re-count; invalidation 3,289; the weekly corrective count towards 2,894 stays preferred.")
c=d['commercial']; c2=c
for a,b in [("FIRST, THE PROMPT IS FIRMING: a $7.00 backwardation on 19-October, widened from $2.00 with three-month unchanged, so there is no carry reward for waiting, though it is far from a squeeze.","FIRST, THE PROMPT STILL HOLDS A SMALL PREMIUM: a $6.50 backwardation on 20-October, barely narrowed from $7.00 as the flat price fell, so there is no carry reward for waiting, though it is far from a squeeze."),
 ("is $1,509.50 on 19-October cash, 62.8% of the $2,403/t premium",f"is ${tl:,.2f} on 20-October cash, {share:.1f}% of the $2,403/t premium"),
 ("the 19-October official held three-month at $3,012.00 after a 2,994.50 settled low inside the 2,980-3,000 zone, still $49.50 beneath 3,061.5;","the 20-October official took three-month down to $2,997.00, $2.50 above the 2,994.50 settled low inside the 2,980-3,000 zone and $64.50 beneath 3,061.5;")]:
    assert a in c2,a; c2=c2.replace(a,b)
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 21-OCTOBER at 10/45/45: the Tuesday 20-October official took three-month down $15.00 to $2,997.00, below the year's opening level, with the backwardation at $6.50 and stock at a new low; neither pre-registered trigger (2,977.5 / 3,077) was hit. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium slipped to $2,997 on Tuesday's LME official - below where it started 2026 and just above its October low - as hand-to-mouth Chinese buying outweighed another record-low LME stock reading.",
 "points":[
 "WHAT MOVED: Tuesday's LME official settled cash at $3,003.50 (-$15.50) and three-month at $2,997.00 (-$15.00), $13.50 below the 02-January level and $64.50 below the $3,061.5 July low. Cash still trades $6.50 above three-month (backwardation), and LME stock edged down 150 t to a new low of 236,225 t. Nickel rose 0.5%, zinc fell 1.1%.",
 "WHY: China's supply is ample - a record 11.84 Mt in Q3 - and SMM reports downstream buyers purchasing only as needed while Chinese futures stay at low levels, even as Chinese ingot stocks fell for a sixth straight day to about 450,000 t.",
 "COSTS STILL CLIMBING: Brent rebounded to about $110 and European gas to about EUR 87/MWh on doubts over a US-Iran deal, with EU gas storage at 74.6%, the lowest for the season since 2009 - this keeps the smelter cost floor high.",
 "WHAT TO WATCH: whether three-month settles below $2,994.50 and then about $2,977.5 (new leg lower) or recovers above $3,061.5-3,077 (decline ending); Norsk Hydro's Q3 results on Friday 23-October; the 27-28 October FOMC (markets price a hold)."]}

d['feed']=([
 {"when":"Wed 21-Oct","impact":"Bearish","text":"BOARD ROLLED TO THE TUESDAY 20-OCTOBER LME OFFICIAL: cash $3,003.50 (-$15.50), three-month $2,997.00 (-$15.00), below the 02-January level; backwardation $6.50 from $7.00; stock down 150 t to a new low of 236,225 t."},
 {"when":"Wed 21-Oct","impact":"Bullish (cost)","text":"Brent about $110.35 (+1.4%) and EU gas about EUR 87.0/MWh (+2.3%) as a diplomat says a US-Iran deal is not imminent; EU gas storage 74.62% on 20-October, the lowest for the season since 2009 (Trading Economics)."},
 {"when":"Tue 20-Oct","impact":"Mixed","text":"SMM: three-region Chinese ingot stocks near 450,000 t, down 9,000 t, a sixth straight working day of destocking; A00 spot premium Yuan 280-300/t, but downstream buying is just-in-time and SHFE futures remain low."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM TURNS NEGATIVE FOR THE YEAR. The Tuesday 20-October official settled cash at $3,003.50 (-0.51%) and three-month at $2,997.00 (-0.50%), $13.50 below the 02-January three-month official, $64.50 beneath the 3,061.5 July low and only $2.50 above the 15-October settled low. The backwardation narrowed to $6.50 from $7.00 and visible stock fell 150 t to a new low of 236,225 t. Elsewhere nickel three-month rose 0.52% while zinc fell 1.12%; copper's backwardation widened to $183 as three-month eased 0.15%."},
 {"theme":"China","horizon":"0-1 month","impact":"Mixed","url":S_SM,
  "headline":"CHINA: STOCKS DRAW, BUYERS HOLD BACK (SMM, 20-October): ingot stocks in the three regions SMM tracks fell 9,000 t to around 450,000 t, a sixth straight working day of destocking, led by Guangdong and Wuxi. The A00 spot premium stood at Yuan 280-300/t, but downstream processors bought only as needed because of the high premiums, some suppliers cut quotes with few deals done, and SHFE futures stayed at low levels. READ: physical tightness in China is not yet turning into price support."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish (cost)","url":S_TG,
  "headline":"ENERGY REBOUNDS ON US-IRAN DEAL DOUBTS (Trading Economics, 21-October): Brent rose about 1.4% to roughly $110.35 and EU TTF gas about 2.3% to roughly EUR 87/MWh after a diplomat said a US-Iran deal was not imminent. Trading Economics notes at least 18 vessels attacked in the Strait of Hormuz over the past two weeks, Middle East oil flows at about 80% of pre-war levels, and EU gas storage at 74.62% on 20-October - the lowest seasonal level since records began in 2009. READ: European and Gulf smelter energy costs stay elevated."},
]+d['news']
d['news']=d['news'][:20]

hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Tue 20-Oct':
        hitc+=1
        cat['date']='Daily, from Wed 21-Oct'
        cat['event']="3,061.5 BROKEN ON SEVEN SETTLED OFFICIALS; THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE AND $17.00 ABOVE THE RULE-BASED CAP, AND SETTLED $2,997.00 ON 20-OCTOBER - ONLY $2.50 ABOVE THAT LOW. A settled close beneath about 2,977.5 would break the cap on daily wave (v) and force a re-count (extended fifth or larger correction toward the 2,894 weekly 61.8%); a settled recovery above 3,077 would signal wave (v) is complete; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289."
assert hitc==1
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 21-OCTOBER: the backwardation held at $6.50 on 20-October (from $7.00) as both legs fell - a fourth straight backwardation. Trend held at FLAT."
RK[4]['risk']+=" UPDATE 21-OCTOBER: LME stock fell 150 t to a new series low of 236,225 t on 20-October; SMM reports Chinese three-region ingot stocks drawing for a sixth straight day to about 450 kt. Trend held at FLAT."
hit=0
for r in RK:
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 21-OCTOBER: Brent back near $110 and TTF near EUR 87/MWh with EU storage at 74.62%, the lowest for the season since 2009 (Trading Economics). Trend held at UP."; hit+=1
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 21-OCTOBER: Trading Economics (21-October) cites at least 18 vessels attacked in the Strait of Hormuz over the past two weeks while Middle East oil flows are back to about 80% of pre-war levels. Trend held at UP."; hit+=1
assert hit==2
d['outlook']['ai_analysis'].insert(0,"WEDNESDAY 21-OCTOBER ON THE TUESDAY 20-OCTOBER OFFICIAL: three-month fell $15.00 to $2,997.00, below the year's opening official and $2.50 above the 15-October settled low, while the backwardation barely narrowed ($6.50) and visible stock set another low (236,225 t) - tight nearby metal, but no bid for the flat price. China's physical market tells the same story: ingot stocks are drawing (about 450 kt, six straight days, SMM) and spot premiums are high, yet downstream buying is hand-to-mouth and SHFE stays low. Energy costs rebounded (Brent about $110, TTF about EUR 87/MWh), supporting the cost floor rather than driving a rally. Weights held at 10/45/45; a settled break of 2,994.50 then 2,977.5 would tilt them bearish; Norsk Hydro's Q3 on 23-October and the 27-28 October FOMC are next.")

EWS=("REVIEWED 21-OCTOBER ON THE TUESDAY 20-OCTOBER OFFICIAL: three-month settled $2,997.00, down $15.00 - a third settled close above the 2,994.50 low of 15-October, but now by only $2.50, and still $19.50 above the rule-based cap near 2,977.5; wave (v) of C ($154.00 from the 3,148.5 wave (iv) high to 2,994.50) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged, NOT re-labelled; the failure to extend the rebound weakens the case that wave (v) is already complete. Base case trimmed to about 55%: wave (v) ends in the 2,977.5-2,994.5 area and a corrective rebound follows toward 3,061.5-3,077 (confirmed by a settled close above 3,077); alternate raised to about 45%: a settled close beneath 2,977.5 forces a re-count toward 2,894. Invalidation 3,289; confidence moderate to low. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED 17-OCTOBER"); assert st.startswith("REVIEWED 20-OCTOBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED 17-OCTOBER"); assert lt.startswith("REVIEWED 20-OCTOBER") and k>0
d['ew']['long_term']['writeup']="REVIEWED 21-OCTOBER (TUESDAY 20-OCTOBER OFFICIAL): three-month fell to 2,997.00, in the lower part of the 2,950-3,110 zone, beneath the 3,061.5 July low and now below the year's opening level; the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label. "+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="110.35",day="about $110.35 on 21-October, +1.44% (Trading Economics)",
 note="REFRESHED WEDNESDAY 21-OCTOBER-2026 (Trading Economics): Brent rebounded after mixed signals on US-Iran talks - prices fell on Tuesday after Pakistan's army chief met Iranian officials, but a diplomat said a deal was not imminent; oil is up about 11% this month; at least 18 vessels have been attacked in the Strait of Hormuz over the past two weeks, while Middle East oil flows have recovered to roughly 80% of pre-war levels. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="87.0",day="about EUR 87.01/MWh on 21-October, +2.29% (Trading Economics; stats section EUR 87.10, +2.39%)",
 note="REFRESHED WEDNESDAY 21-OCTOBER-2026 (Trading Economics): recovered to about EUR 87/MWh after a 3%+ fall the prior session; gas remains more than double pre-conflict levels with Gulf LNG disrupted; EU storage was 74.62% full on 20-October, the lowest seasonal level since records began in 2009 (Germany just above 61%). Value approximate. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.8",day="about 101.77 on 21-October, +0.05%, after weakening to about 101.5 on Tuesday, a three-week low (Trading Economics)",
 note="REFRESHED WEDNESDAY 21-OCTOBER-2026 (Trading Economics): the dollar weakened on Tuesday on renewed AI concerns, lower oil on hopes of a diplomatic resolution, and weak housing data (September housing starts -5.2%); the Fed is expected to hold next week, with a 25bp December hike priced. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="5.13",day="about 5.13% on 21-October, +0.02pp, after falling about 5bp to 5.09% on Tuesday (Trading Economics)",
 note="REFRESHED WEDNESDAY 21-OCTOBER-2026 (Trading Economics): yields dipped on Tuesday on lower oil and weak housing data, then edged up; markets expect a Fed hold in late October and price a December hike. Higher yields raise the cost of carrying metal. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.12110',day="LME fixing on 20-October, -0.16% from 1.12290; ECB fixing 1.12150, BFIX 1.12092",
 note="REFRESHED WEDNESDAY 21-OCTOBER-2026 to the 20-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE TUESDAY 20-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED OFFICIAL. This Wednesday 21-October run is compiled about 03:35 London, BEFORE today's ring; Wednesday's official prints at 13:20 London and will appear on the next run. Reference and intraday prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (21-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 20-October session, and the per-metal aluminium daily table's newest row is 20-October (cash 3,003.50, three-month 2,997.00, stock 236,225), so the board is current rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.12290, ECB 1.12250, BFIX 1.12288) matches the 19-October board verified on 20-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 19-October: aluminium -150 to 236,225; copper +1,625 to 233,800; nickel +756 to 280,866; zinc +3,275 to 166,325; lead -3,925 to 334,200.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (20-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (fourteen sessions, 01- to 20-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 2,997.00; the stock chart axis floor (225,000 t) brackets visible stock at 236,225 t - both re-checked this run; the stock floor has about 11,200 t of headroom and will be re-bracketed before it is approached.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,003.50 against three-month $2,997.00 is therefore a $6.50 BACKWARDATION, narrowed from $7.00 on 19-October as both legs fell."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 20-October official cash of $3,003.50, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $110.35), the dollar index (about 101.8), TTF (about EUR 87.0/MWh) and the US ten-year (about 5.13%) are Trading Economics readings shown on 21-October (early Wednesday trading) - the source's own sections differ slightly, so they are approximate; EUR/USD is the 20-October LME fixing, the same session as the board."; hit+=1
    if cv.startswith("FETCH NOTE 20-OCTOBER"):
        C[i]=("FETCH NOTE 21-OCTOBER: no authorised fetch was blocked. SMM's 20-October three-region inventory note gives only an approximate total ('450,000 mt level') and a 9,000 t daily fall in the companion midday review, with no regional figures - those are published as stated, not refined. Trading Economics' aluminium page mentions a 25.9% y/y rise in China's September aluminium exports; the customs release could not be located in a primary or second source this run, so that figure is NOT published as a data point. No dated Q3 results date for Century Aluminum was located."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: NO NEW EARNINGS WERE REPORTED BY TRACKED PEERS SINCE ALCOA (15-October); NORSK HYDRO REPORTS Q3 ON 23-OCTOBER. Rio Tinto's row carries its 14-October Q3 operations note (production only). NO NEW COMPANY WAS BACK-FILLED THIS RUN. Other entries are carried at their last publicly verified figures, and gaps stay gaps."; hit+=1
assert hit==4,hit

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 20-OCTOBER: no newer public disclosure","REVIEWED 21-OCTOBER: no newer public disclosure").replace("REVIEWED 20-OCTOBER. NO NEW DATED","REVIEWED 21-OCTOBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('China operators'):
        hit+=1
        p['update']=("UPDATED 21-OCTOBER (SMM, 20-October): Chinese three-region ingot stocks fell 9,000 t to around 450,000 t, a sixth straight working day of destocking; A00 spot premium Yuan 280-300/t with downstream buying just-in-time. ")+p['update']
    if p['name'].startswith('EGA'):
        p['update']=p['update'].replace("REVIEWED 21-OCTOBER: no newer public disclosure located; status below carried.","REVIEWED 21-OCTOBER: no newer company disclosure located; Trading Economics (20-October) restates EGA's statement that a quarter of Al Taweelah's reduction cells are back online with full recovery expected by Q1-2027, consistent with the status below, which is carried.")
assert hit==1
for s in [[L_TE,S_TE],[L_SM,S_SM],[L_SI,S_SI],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG]]:
    d['sources'].append(s)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 20-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 19-Oct)",W])
d['outlook']['sources'].append([L_SM,S_SM]); d['outlook']['sources'].append([L_TG,S_TG])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-19'
ph['rows'][-1]=['2026-10-20',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
