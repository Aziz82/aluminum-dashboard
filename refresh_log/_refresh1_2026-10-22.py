# Daily data refresh - 2026-10-22 (THURSDAY, ~03:40 London, BEFORE the ring). Board ROLLED to WEDNESDAY 21-Oct LME official (latest published).
# Westmetall cache-busted EN AND DE overviews both fetched and agree on the full 21-Oct session; Al per-metal table top row = 21-Oct.
# Completeness: 5/5 stock lines reconcile vs 20-Oct board; prior FX column (MTLE 1.12110) matches 20-Oct board.
# New public items: EGA 21-Oct release - 631 of 1,262 Al Taweelah cells restarted (50%), full output Q1-2027, refinery ~50%;
# SMM 22-Oct: ingots -53kt w/w (two post-holiday weeks -103kt), billets -20kt; TE 22-Oct Brent ~$110.30, TTF ~EUR87.3, storage 74.58%, DXY ~101.67, UST10Y ~5.09%.
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-22'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (21/22-Oct-2026)"
S_EGA="https://media.ega.ae/ega-reaches-50-completion-of-al-taweelah-smelter-restart/"; L_EGA="EGA - EGA reaches 50% completion of Al Taweelah smelter restart (press release, 21-Oct-2026)"
S_SI="https://news.metal.com/newscontent/104171871-smm-statistics-changes-in-aluminum-ingot-and-billet-inventory-before-and-after-national-day-2020-2026-as-of-october-22"; L_SI="SMM - Changes in aluminum ingot and billet inventory before and after National Day, 2020-2026 (as of 22-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (22-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (22-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (22-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (22-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
assert B['LME Cash settlement']['cur']==3003.5 and B['LME 3-month']['cur']==2997.0
cash,prev_c,m3,prev_m,stk,prev_s=3031.0,3003.5,3024.5,2997.0,236125,236225
spr=cash-m3; assert spr==6.5 and prev_s-100==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED THURSDAY 22-OCTOBER-2026 (ABOUT 03:40 LONDON, BEFORE TODAY'S RING). THE BOARD IS THE WEDNESDAY 21-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED OFFICIAL; Thursday's prints at 13:20 London and will appear on the next run. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 21-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.12290); their prior-day FX column (MTLE 1.12110) matches the verified 20-October board, and the per-metal aluminium table's newest row is 21-October; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 20-October: aluminium 236,225 less 100 to 236,125; copper 233,800 plus 11,475 to 245,275; nickel 280,866 unchanged; zinc 166,325 plus 1,500 to 167,825; lead 334,200 less 4,900 to 329,300. "
 "The whole board sits on ONE UNIFORM SESSION (21-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(" CASH SETTLED $3,031.00 ON THE 21-OCTOBER OFFICIAL, UP $27.50 OR 0.92% FROM $3,003.50. THREE-MONTH SETTLED $3,024.50, UP $27.50 OR 0.92% - back $14.00 ABOVE the first-published 2026 three-month official of $3,010.50, so aluminium is again POSITIVE year to date ("+f"{ytd:+.2f}%), $30.00 above the 2,994.50 settled low of 15-October, but an EIGHTH settled close beneath the 3,061.5 July low (by $37.00). "
 "THE BACKWARDATION WAS UNCHANGED at $6.50 as cash and three-month rose by the same $27.50 - the flat price rallied while the spread stood still. "
 "VISIBLE LME STOCK FELL 100 t TO 236,125 t, another new series low.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,031.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,024.5","pos":True,"delta":VER+AL+" THREE-MONTH IS $37.00 BENEATH THE 3,061.5 JULY LOW, $52.50 beneath the 3,077 weekly 50% retracement and $264.50 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held and now sits $30.00 beneath price; the rule-based cap on daily wave (v) near 2,977.5 was never touched."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+6.5","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,031.00 against three-month $3,024.50 is a $6.50 BACKWARDATION, unchanged from 20-October as both legs rose $27.50. The reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is still UNMET; the bearish structural confirmation, a contango beyond $24.50, is also unmet. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"236,125","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 100 t TO 236,125 t, another new series low, the draw slowing again from 150 t the session before. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,024.50, UP $27.50 - $37.00 beneath the 3,061.5 July low, an eighth settled close below it, and $14.00 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 100 t TO 236,125 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":6.5,"avg":sep_sp,"note":VER+f" A $6.50 BACKWARDATION, UNCHANGED. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Cash and three-month both rose $27.50, so the flat price rallied with no change in structure. REVERSAL CONDITION, RESTATED UNCHANGED: a BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1229,"prev":1.1211,"avg":1.1465,"note":VER+" THE LME EURO FIXING FIRMED TO 1.12290 FROM 1.12110 at the Wednesday ring; the ECB fixing printed 1.12340 and BFIX 1.12292. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (21-Oct official)","price":"3,031.0","basis":"THE 21-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,031.00, UP $27.50 OR 0.92%. Next official Thursday 22-October 13:20 London."},
 {"tenor":"3-month (21-Oct official)","price":"3,024.5","basis":"THE 21-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,024.50, UP $27.50 - $37.00 beneath the 3,061.5 July low (eighth settled close below it) and $14.00 above the 02-January official, so back positive year to date."},
 {"tenor":"Cash-to-3M structure","price":"+6.5 (BACKWARDATION)","basis":"A $6.50 BACKWARDATION, unchanged as both legs rose $27.50."},
 {"tenor":"Visible LME stock","price":"236,125 t","basis":f"DOWN 100 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE FLAT PRICE BOUNCED, THE STRUCTURE STOOD STILL. On the 21-October official cash $3,031.00 sits $6.50 ABOVE three-month $3,024.50, a BACKWARDATION, unchanged from 20-October. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00, $7.00, $6.50 and now $6.50. "
 f"READ: a fifth straight backwardation while visible stock keeps setting lows (236,125 t) - a modest prompt-tightness signal; this session the flat price finally responded, but the spread did not widen with it. The September mean spread was ${sep_sp:,.2f}. The reversal condition (a backwardation beyond $15.00) is unmet; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]

ls=d['lme_series']; assert ls[-1][0]=='20-Oct', ls[-1]
d['lme_series']=ls[1:]+[["21-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14441.0,14315.0,14540.0,14357.0); NI=(15830.0,16040.0,15350.0,15570.0); ZN=(3771.0,3724.0,3736.0,3695.0); PB=(1880.0,1904.0,1851.0,1894.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average-to-date: 14 sessions to 20-Oct (13 per 20-Oct script + 20-Oct) + 21-Oct
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0,3736.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0,1851.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/15)/(sum(zs)/14),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/15)/(sum(ps)/14),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-21'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending WEDNESDAY 21-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 30-September dropped and 21-October appended, so the window is 01-October to 21-October. Every point is an official cash settlement; the 21-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 20-October. Next official Thursday 22-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (21-October-2026 session; stock lines reconciled against 20-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,441.00, down $99.00 or 0.68%; three-month $14,315.00, down $42.00 or 0.29%. The BACKWARDATION NARROWED to $126.00 from $183.00 as cash fell faster than three-month, alongside the largest stock inflow on the board - 11,475 tonnes, lifting stock to 245,275 t, a third straight rise."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,830.00, up $480.00 or 3.13%; three-month $16,040.00, up $470.00 or 3.02% - the strongest metal on the board for a second session. CONTANGO $210.00 from $220.00, still the widest carry on the board. Stock unchanged at 280,866 tonnes."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,771.00, up $35.00 or 0.94%; three-month $3,724.00, up $29.00 or 0.78%. BACKWARDATION widened to $47.00 from $41.00 even as another 1,500 tonnes were delivered in, lifting stock to 167,825 t - an eighth straight inflow. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,880.00, up $29.00 or 1.57%; three-month $1,904.00, up $10.00 or 0.53%. CONTANGO narrowed to $24.00 from $43.00 as cash outpaced three-month. Stock drew 4,900 tonnes to 329,300, a twenty-third consecutive draw. Lead and nickel are now both about 5.2% lower year to date, the weakest on this board."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Wednesday 20-October official the board turned mostly higher - nickel three-month +3.02%, aluminium +0.92%, zinc +0.78% and lead +0.53%, with copper the exception at -0.29% - while the dollar index held near 101.7 (Trading Economics). The LME euro fixing firmed to 1.1229.").replace("Wednesday 20-October","Wednesday 21-October")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='20-Oct'
        i['hist']=i['hist'][1:]+[["21-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,315.00 (3M); 14,441.00 (cash) $/t"
        i['ratio']="~14,441.00 $/t cash vs LME 3M 14,315.00 $/t"
        i['trend']='flat'
        i['src']=("LME official cash settlement, rolled to the WEDNESDAY 21-OCTOBER-2026 session at $14,441.00, DOWN $99.00 or 0.68% against $14,540.00. THE WINDOW ROLLED THIS RUN: 30-September dropped and 21-October appended, so the series is the last fifteen published official cash sessions, 01-October to 21-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 20-October). "
                  "Copper structure for context: backwardation $126.00 (from $183.00), stock rose 11,475 t to 245,275 t.")
d['inputs_summary']=("UPDATE 22-OCTOBER: Copper rolled to the Wednesday 21-October LME official cash of $14,441.00, down $99.00, with its fifteen-session window moved to 01-October to 21-October. No new monthly carbon settlement is due until mid-November; the October cycle (Mysteel, 16-October: Shandong prebaked-anode benchmark +Yuan 400/t to Yuan 6,130/t; green petcoke 3B Yuan 3,610.5/t) remains the latest and is already in the histories. No new dated SMM fluoride, silicon or magnesium mark was retrievable this run. Energy inputs stay expensive - Brent about $110 and European gas about EUR 87/MWh with EU storage at 74.58%, the lowest for the season since 2009 (Trading Economics, 22-October). Every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 20-October official cash of \$3,003\.50, or \$1,501\.75, DOWN \$7\.75 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$901\.25, so 62\.5%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 21-October official cash of $3,031.00, or ${tl:,.2f}, UP $13.75 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED WEDNESDAY 21-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE TUESDAY 20-OCTOBER OFFICIAL)."; NEWC="COMPILED THURSDAY 22-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE WEDNESDAY 21-OCTOBER OFFICIAL)."
n=0
for p in d['premiums']:
    p['src'],k=OLDT.subn(NEWT,p['src']); n+=k
    p['src']=p['src'].replace(OLDC,NEWC)
print('premium tariff replaced',n); assert n==len(d['premiums'])
ra=360.40/m3*100; na=0
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    o="THE RATIO: LME Alumina at $360.40/t against the 20-October aluminium three-month of $2,997.00 is 12.03%"
    if o in s: na+=1
    s=s.replace(o,f"THE RATIO: LME Alumina at $360.40/t against the 21-October aluminium three-month of $3,024.50 is {ra:.2f}%")
    a['src']=s
print('alumina',na,len(d['alumina'])); assert na==len(d['alumina'])

d['lme_commentary']=("ALUMINIUM BOUNCES OFF THE OCTOBER LOW. On the Wednesday 21-October official cash settled $3,031.00 and three-month $3,024.50, both up $27.50 - back $14.00 above the 02-January three-month official, so positive for 2026 again, and $30.00 above the 15-October settled low of 2,994.50, though still $37.00 beneath the 3,061.5 July low. "
 "The backwardation was unchanged at $6.50 and visible stock fell 100 t to another series low of 236,125 t. Most of the board rose: nickel +3.0%, zinc +0.8%, lead +0.5%; copper three-month eased 0.3% as 11,475 t were delivered into LME sheds. "
 "Supply news cut the other way: EGA said on 21-October that 631 of the 1,262 reduction cells at Al Taweelah - half - are now restarted, with full production still expected in Q1-2027. In China, SMM reports ingot stocks fell 53,000 t in the second week after National Day (103,000 t over two weeks, the fastest post-holiday pace since at least 2020). "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND STILL IN CONTROL, BUT THE OCTOBER LOW HELD. Against: three-month has settled beneath 3,061.5 eight times; Gulf supply is returning - EGA now has half of Al Taweelah's 1,262 cells restarted (21-October) and guides full output in Q1-2027; China ran a record Q3 at an annualised pace of about 46.7 Mt, above its 45 Mt cap; a December Fed hike is still priced. "
 "Constructive: the 2,994.50 settled low held and three-month rallied $27.50 to $3,024.50; visible LME stock fell to another 21st-century low of 236,125 t and the curve stays in backwardation ($6.50); Chinese ingot stocks fell 103,000 t over the two post-holiday weeks (SMM) - the fastest post-holiday draw since at least 2020; energy stays expensive - Brent about $110, European gas about EUR 87/MWh with EU storage the lowest for the season since 2009 - which lifts the smelter cost floor.")
d['bottom_line']=("BOTTOM LINE: aluminium rebounded on the Wednesday 21-October LME official - cash $3,031.00 (+$27.50), three-month $3,024.50 (+$27.50) - back above the year's opening level, though still $37.00 beneath the 3,061.5 July low. "
 "The backwardation held at $6.50 and visible stock fell to another low of 236,125 t, while EGA's half-way restart at Al Taweelah adds to a heavy supply side. Scenario weights are held at 10% bull / 45% base / 45% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) now leans to wave (v) complete at 2,994.50 - a settled close above 3,077 would confirm it, below about 2,977.5 would force a re-count; invalidation 3,289; the weekly corrective count towards 2,894 stays preferred.")
c2=d['commercial']
for a,b in [("FIRST, THE PROMPT STILL HOLDS A SMALL PREMIUM: a $6.50 backwardation on 20-October, barely narrowed from $7.00 as the flat price fell, so there is no carry reward for waiting, though it is far from a squeeze.","FIRST, THE PROMPT STILL HOLDS A SMALL PREMIUM: a $6.50 backwardation on 21-October, unchanged as the flat price rose $27.50, so there is no carry reward for waiting, though it is far from a squeeze."),
 ("is $1,501.75 on 20-October cash, 62.5% of the $2,403/t premium",f"is ${tl:,.2f} on 21-October cash, {share:.1f}% of the $2,403/t premium"),
 ("the 20-October official took three-month down to $2,997.00, $2.50 above the 2,994.50 settled low inside the 2,980-3,000 zone and $64.50 beneath 3,061.5;","the 21-October official lifted three-month to $3,024.50, $30.00 above the 2,994.50 settled low inside the 2,980-3,000 zone but $37.00 beneath 3,061.5; EGA has restarted half of Al Taweelah's cells (21-October);")]:
    assert a in c2,a; c2=c2.replace(a,b)
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 22-OCTOBER at 10/45/45: the Wednesday 21-October official lifted three-month $27.50 to $3,024.50, back above the year's opening level, with the backwardation unchanged at $6.50 and stock at a new low; EGA's half-way Al Taweelah restart offsets the bounce; neither pre-registered trigger (2,977.5 / 3,077) was hit. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium bounced $27.50 to $3,024.50 on Wednesday's LME official, holding its October low and turning positive for 2026 again, but EGA's half-way restart at Al Taweelah keeps the supply side heavy.",
 "points":[
 "WHAT MOVED: Wednesday's LME official settled cash at $3,031.00 and three-month at $3,024.50, both up $27.50, $14.00 above the 02-January level but still $37.00 below the $3,061.5 July low. Cash still trades $6.50 above three-month (backwardation, unchanged), and LME stock edged down 100 t to a new low of 236,125 t. Nickel jumped 3.0%; copper slipped 0.3% as 11,475 t arrived in LME sheds.",
 "WHY: Chinese physical demand is pulling metal out of storage - SMM says ingot stocks fell 53,000 t last week and 103,000 t over the two weeks since National Day, the fastest post-holiday draw since at least 2020 - and energy stays expensive (Brent about $110, European gas about EUR 87/MWh).",
 "SUPPLY RETURNING: EGA said on 21-October that half of Al Taweelah's 1,262 reduction cells (631) are restarted, up from a quarter in late August, with full production still expected in Q1-2027 - more Gulf metal is coming back.",
 "WHAT TO WATCH: whether three-month can settle above $3,061.5 and then $3,077 (decline likely over) or slips back below the $2,994.50 low; Norsk Hydro's Q3 results on Friday 23-October; the 27-28 October FOMC (markets price a hold)."]}

d['feed']=([
 {"when":"Thu 22-Oct","impact":"Bullish","text":"BOARD ROLLED TO THE WEDNESDAY 21-OCTOBER LME OFFICIAL: cash $3,031.00 (+$27.50), three-month $3,024.50 (+$27.50), back above the 02-January level; backwardation unchanged at $6.50; stock down 100 t to a new low of 236,125 t."},
 {"when":"Wed 21-Oct","impact":"Bearish","text":"EGA: 631 of 1,262 reduction cells at Al Taweelah restarted (50%), up from about 25% in late August; full production still expected in Q1-2027; alumina refinery at about 50% (EGA press release)."},
 {"when":"Thu 22-Oct","impact":"Bullish","text":"SMM: Chinese aluminium ingot stocks fell 53,000 t in the second week after National Day (103,000 t over two weeks, fastest post-holiday pace since at least 2020); billets -20,000 t."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM BOUNCES OFF THE OCTOBER LOW. The Wednesday 21-October official settled cash at $3,031.00 (+0.92%) and three-month at $3,024.50 (+0.92%), $14.00 above the 02-January three-month official - positive for 2026 again - and $30.00 above the 15-October settled low, though still $37.00 beneath the 3,061.5 July low. The backwardation was unchanged at $6.50 and visible stock fell 100 t to a new low of 236,125 t. Nickel three-month jumped 3.02%; copper eased 0.29% as LME copper stock rose 11,475 t."},
 {"theme":"Gulf supply","horizon":"0-6 months","impact":"Bearish","url":S_EGA,
  "headline":"EGA REACHES HALF-WAY ON AL TAWEELAH RESTART (EGA, 21-October): 631 of the smelter's 1,262 reduction cells have been restarted since the first on 26-May, after the 28-March emergency shutdown; each cell takes about a week to stabilise. The company still expects full production in Q1-2027, and the Al Taweelah alumina refinery runs at about 50% of capacity. READ: Gulf supply recovery is on schedule, adding to ex-China availability."},
 {"theme":"China","horizon":"0-1 month","impact":"Bullish","url":S_SI,
  "headline":"CHINA: FASTEST POST-HOLIDAY DESTOCK IN SIX YEARS (SMM, 22-October): aluminium ingot social inventory fell 53,000 t in the second week after National Day, after 50,000 t the week before - 103,000 t over two weeks, and SMM says the single-week fall is the largest for the period since 2020. Billet stocks fell 20,000 t (39,000 t over two weeks). During the holiday ingots had built only 48,000 t. READ: Chinese physical offtake is firmer than prices suggest."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish (cost)","url":S_BR,
  "headline":"ENERGY HOLDS HIGH (Trading Economics, 22-October): Brent near $110.30 (+1.4%) after Trading Economics reported a drone attack on Saudi Aramco's Shaybah field and a US order for some embassy staff to leave Saudi Arabia; Middle East export flows are nearing pre-war levels. EU TTF gas was about EUR 87.3/MWh with storage 74.58% full on 21-October, the lowest seasonal level since records began in 2009. READ: European and Gulf smelter energy costs stay elevated."},
]+d['news']
d['news']=d['news'][:20]

hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Wed 21-Oct':
        hitc+=1
        cat['date']='Daily, from Thu 22-Oct'
        cat['event']="3,061.5 BROKEN ON EIGHT SETTLED OFFICIALS; THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE AND $17.00 ABOVE THE RULE-BASED CAP, RETESTED IT ON 20-OCTOBER ($2,997.00) AND BOUNCED TO $3,024.50 ON 21-OCTOBER. A settled close beneath about 2,977.5 would break the cap on daily wave (v) and force a re-count (extended fifth or larger correction toward the 2,894 weekly 61.8%); a settled recovery above 3,077 would signal wave (v) is complete; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289."
assert hitc==1
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 22-OCTOBER: the backwardation held at $6.50 on 21-October as both legs rose $27.50 - a fifth straight backwardation. Trend held at FLAT."
RK[4]['risk']+=" UPDATE 22-OCTOBER: LME stock fell 100 t to a new series low of 236,125 t on 21-October; SMM reports Chinese ingot stocks down 103,000 t over the two post-holiday weeks. Trend held at FLAT."
RK[5]['risk']+=" UPDATE 22-OCTOBER: EGA (21-October) reports 631 of 1,262 Al Taweelah cells restarted - half - up from about a quarter in late August, with full production still guided for Q1-2027; this is the first new dated company disclosure in the window and it points to supply returning on schedule. Trend held at FLAT pending corroboration of GCC output data."
hit=0
for r in RK:
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 22-OCTOBER: Brent near $110 and TTF near EUR 87/MWh with EU storage at 74.58%, the lowest for the season since 2009 (Trading Economics). Trend held at UP."; hit+=1
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 22-OCTOBER: Trading Economics (22-October) reports a drone attack on Saudi Aramco's Shaybah oil field and a US order for some embassy personnel to leave Saudi Arabia (not independently confirmed this run), while Middle East export flows near pre-war levels. Trend held at UP."; hit+=1
assert hit==2
d['outlook']['ai_analysis'].insert(0,"THURSDAY 22-OCTOBER ON THE WEDNESDAY 21-OCTOBER OFFICIAL: three-month rose $27.50 to $3,024.50, holding the 2,994.50 October low on its retest and returning above the year's opening official, while the backwardation stayed at $6.50 and visible stock set another low (236,125 t). Two public data points pull in opposite directions: SMM reports the fastest post-holiday Chinese ingot destock since at least 2020 (-103,000 t over two weeks), but EGA has now restarted half of Al Taweelah and keeps a Q1-2027 full-output target. Energy costs stay high (Brent about $110, TTF about EUR 87/MWh). Weights held at 10/45/45; a settled close above 3,061.5-3,077 would tilt them toward the base/bull side, a break of 2,994.50 then 2,977.5 bearish; Norsk Hydro's Q3 on 23-October and the 27-28 October FOMC are next.")

EWS=("REVIEWED 22-OCTOBER ON THE WEDNESDAY 21-OCTOBER OFFICIAL: three-month settled $3,024.50, up $27.50 - a fourth settled close above the 2,994.50 low of 15-October, which held on the 20-October retest ($2,997.00) and was never close to the rule-based cap near 2,977.5; wave (v) of C ($154.00 from the 3,148.5 wave (iv) high to 2,994.50) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged, NOT re-labelled. Base case raised back to about 60%: wave (v) ended at 2,994.50 and a corrective rebound is starting toward 3,061.5-3,077 (confirmed by a settled close above 3,077); alternate about 40%: a settled close beneath 2,977.5 forces a re-count toward 2,894. Invalidation 3,289; confidence moderate. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED 17-OCTOBER"); assert st.startswith("REVIEWED 21-OCTOBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED 17-OCTOBER"); assert lt.startswith("REVIEWED 21-OCTOBER") and k>0
d['ew']['long_term']['writeup']="REVIEWED 22-OCTOBER (WEDNESDAY 21-OCTOBER OFFICIAL): three-month rose to 3,024.50, in the lower part of the 2,950-3,110 zone, still beneath the 3,061.5 July low but back above the year's opening level; the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label. "+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="110.30",day="about $110.30 on 22-October, +1.36% (Trading Economics; stats section $110.12, +1.20%)",
 note="REFRESHED THURSDAY 22-OCTOBER-2026 (Trading Economics): Brent climbed toward $110, recovering earlier losses, after Trading Economics reported a drone attack on Saudi Aramco's Shaybah oil field and a US order for some embassy personnel to leave Saudi Arabia; Ukrainian drone strikes on Russian oil infrastructure added support, while Middle East crude export flows near pre-war levels may cap gains. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="87.3",day="about EUR 87.27/MWh on 22-October, -0.18% (Trading Economics; stats section EUR 87.23, -0.23%)",
 note="REFRESHED THURSDAY 22-OCTOBER-2026 (Trading Economics): near the highest levels in almost four years with Middle East LNG exports about 80% below year-ago levels and vessel attacks in the Strait of Hormuz; EU storage was 74.58% full on 21-October, the lowest seasonal level since records began in 2009 (Germany just above 61%). Value approximate. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.7",day="about 101.67 on 22-October, -0.02% (Trading Economics)",
 note="REFRESHED THURSDAY 22-OCTOBER-2026 (Trading Economics): the dollar held near 101.7 ahead of next week's Fed meeting, where a hold is widely expected, with a December hike still possible on energy-driven inflation; recent housing data were weak (pending home sales at a record low). SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="5.09",day="about 5.09-5.10% on 22-October, about -0.03pp (Trading Economics)",
 note="REFRESHED THURSDAY 22-OCTOBER-2026 (Trading Economics): the yield held near 5.1% ahead of the Fed decision, with markets pricing a hold and a meaningful chance of a December hike; earlier in October yields reached multi-decade highs. Higher yields raise the cost of carrying metal. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.12290',day="LME fixing on 21-October, +0.16% from 1.12110; ECB fixing 1.12340, BFIX 1.12292",
 note="REFRESHED THURSDAY 22-OCTOBER-2026 to the 21-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE WEDNESDAY 21-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED OFFICIAL. This Thursday 22-October run is compiled about 03:40 London, BEFORE today's ring; Thursday's official prints at 13:20 London and will appear on the next run. Reference and intraday prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (22-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 21-October session, and the per-metal aluminium daily table's newest row is 21-October (cash 3,031.00, three-month 3,024.50, stock 236,125), so the board is current rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.12110, ECB 1.12150, BFIX 1.12092) matches the 20-October board verified on 21-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 20-October: aluminium -100 to 236,125; copper +11,475 to 245,275; nickel unchanged at 280,866; zinc +1,500 to 167,825; lead -4,900 to 329,300.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (21-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (fifteen sessions, 01- to 21-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,024.50; the stock chart axis floor (225,000 t) brackets visible stock at 236,125 t - both re-checked this run; the stock floor has about 11,100 t of headroom and will be re-bracketed before it is approached.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,031.00 against three-month $3,024.50 is therefore a $6.50 BACKWARDATION, unchanged from 20-October as both legs rose $27.50."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 21-October official cash of $3,031.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $110.30), the dollar index (about 101.7), TTF (about EUR 87.3/MWh) and the US ten-year (about 5.09%) are Trading Economics readings shown on 22-October (early Thursday trading) - the source's own sections differ slightly, so they are approximate; EUR/USD is the 21-October LME fixing, the same session as the board."; hit+=1
    if cv.startswith("FETCH NOTE 21-OCTOBER"):
        C[i]=("FETCH NOTE 22-OCTOBER: AL Circle's news index and mining.com's search page returned HTTP 403 this run; per the fallback, a web search was used and the EGA item was taken from EGA's own press release. SMM's 22-October inventory note gives weekly changes but no total ingot stock level, so no total is published. The Shaybah drone-attack report rests on Trading Economics' Brent commentary only; a search did not find a second source this run, so it is attributed rather than stated as fact. A web-search summary attributing remarks on US-Mexico tariffs to the US Commerce Secretary could not be verified and is NOT published."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: NO NEW EARNINGS WERE REPORTED BY TRACKED PEERS SINCE ALCOA (15-October); NORSK HYDRO REPORTS Q3 ON FRIDAY 23-OCTOBER. Rio Tinto's row carries its 14-October Q3 operations note (production only). NO NEW COMPANY WAS BACK-FILLED THIS RUN. Other entries are carried at their last publicly verified figures, and gaps stay gaps."; hit+=1
assert hit==4,hit

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 21-OCTOBER: no newer public disclosure","REVIEWED 22-OCTOBER: no newer public disclosure").replace("REVIEWED 21-OCTOBER. NO NEW DATED","REVIEWED 22-OCTOBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('China operators'):
        hit+=1
        p['update']=("UPDATED 22-OCTOBER (SMM, 22-October): Chinese aluminium ingot social inventory fell 53,000 t in the second week after National Day, 103,000 t over two weeks - the fastest post-holiday pace since at least 2020; billets -20,000 t. ")+p['update']
    if p['name'].startswith('EGA'):
        hit+=1
        p['status']="PARTIAL RESTART - HALF OF AL TAWEELAH'S REDUCTION CELLS (631 OF 1,262) RESTARTED PER THE COMPANY (21-OCTOBER), FULL PRODUCTION STILL EXPECTED IN Q1-2027; REFINERY ~50%; SEPARATELY IN TALKS WITH THE US GOVERNMENT OVER INCENTIVES FOR A US SMELTER CONTINGENT ON COMPETITIVE LONG-TERM POWER; HAS ALSO LICENSED ITS DX+ ULTRA SMELTING TECHNOLOGY TO NALCO FOR A PROPOSED 500,000 t/y ANGUL EXPANSION"
        u=p['update']; k=u.find("UPDATED 05-OCTOBER"); assert k>0
        p['update']=("UPDATED 22-OCTOBER FROM EGA'S PRESS RELEASE (21-October): 631 of the 1,262 reduction cells at Al Taweelah have been restarted - about half - since the first restored cell on 26-May, following the 28-March emergency shutdown; each restarted cell takes about a week to stabilise; the CEO said EGA continues to expect full production during Q1-2027; the alumina refinery runs at about 50% of capacity, with further ramp-up dependent on supply chains and sourcing. ")+u[k:]
        p['src']=[L_EGA,S_EGA]
assert hit==2
for s in [[L_TE,S_TE],[L_EGA,S_EGA],[L_SI,S_SI],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG]]:
    d['sources'].append(s)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 21-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 20-Oct)",W])
d['outlook']['sources'].append([L_EGA,S_EGA]); d['outlook']['sources'].append([L_SI,S_SI])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-20'
ph['rows'][-1]=['2026-10-21',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
