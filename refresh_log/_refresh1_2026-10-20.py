# Daily data refresh - 2026-10-20 (TUESDAY, ~03:35 London, BEFORE the ring). Board ROLLED to MONDAY 19-Oct LME official (latest published).
# Westmetall cache-busted EN AND DE overviews both fetched and agree on the full 19-Oct session; Al per-metal table top row = 19-Oct.
# Completeness: 5/5 stock lines reconcile vs 16-Oct board; prior FX column (MTLE 1.12570) matches 16-Oct board.
# New public items: China Sept primary Al output 3.91 Mt, Q3 record 11.84 Mt (+2.2% y/y), ~46.7 Mt/y pace (Finimize citing NBS/Reuters, 19-Oct);
# China Sept unwrought primary Al imports ~172 kt (-30.3% y/y), exports ~45 kt (SMM, 20-Oct); Oct prebaked-anode Shandong benchmark 6,130 Y/t cash, +400 (Mysteel, 16-Oct);
# Hydro Q3 results 23-Oct 07:00 CEST (GlobeNewswire via ariva, 16-Oct). TE macro rows refreshed 20-Oct.
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-20'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (19/20-Oct-2026)"
S_CO="https://finimize.com/content/chinas-aluminum-output-hit-a-record-quarterly-high"; L_CO="Finimize - China's aluminum output hit a record quarterly high (NBS data via Reuters, 19-Oct-2026)"
S_IM="https://news.metal.com/newscontent/104166713-domestic-primary-aluminium-imports-down-303-yoy-in-sep-2026-exports-increase-541"; L_IM="SMM - Domestic primary aluminium imports down 30.3% YoY in Sep 2026, exports increase 54.1% (20-Oct-2026)"
S_AN="https://www.mysteel.net/analysis/5144811-china-prebaked-anode-exceeds-yuan-6-000-on-feedstock-rally-"; L_AN="Mysteel - China prebaked anode exceeds Yuan 6,000 on feedstock rally (16-Oct-2026)"
S_HY="https://www.ariva.de/news/norsk-hydro-reminder-invitation-to-hydro-s-third-quarter-12171152"; L_HY="Norsk Hydro - Reminder: invitation to Hydro's third quarter results 2026 (GlobeNewswire via ariva, 16-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (20-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (20-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (20-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (20-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
cash,prev_c,m3,prev_m,stk,prev_s=3019.0,3014.0,3012.0,3012.0,236375,237875
spr=cash-m3; pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100
assert spr==7.0 and prev_s-1500==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED TUESDAY 20-OCTOBER-2026 (ABOUT 03:35 LONDON, BEFORE TODAY'S RING). THE BOARD IS THE MONDAY 19-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED OFFICIAL; Tuesday's prints at 13:20 London and will appear on the next run. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 19-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.12290); their prior-day FX column (MTLE 1.12570) matches the verified 16-October board, and the per-metal aluminium table's newest row is 19-October; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 16-October: aluminium 237,875 less 1,500 to 236,375; copper 225,425 plus 6,750 to 232,175; nickel 279,990 plus 120 to 280,110; zinc 158,275 plus 4,775 to 163,050; lead 339,275 less 1,150 to 338,125. "
 "The whole board sits on ONE UNIFORM SESSION (19-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(" CASH SETTLED $3,019.00 ON THE 19-OCTOBER OFFICIAL, UP $5.00 OR 0.17% FROM $3,014.00. THREE-MONTH SETTLED $3,012.00, UNCHANGED - still $1.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%) and a SIXTH settled close beneath the 3,061.5 July low (by $49.50). "
 "THE BACKWARDATION WIDENED to $7.00 from $2.00 WITH THE FLAT PRICE UNCHANGED - the prompt firmed while three-month stood still. "
 "VISIBLE LME STOCK FELL 1,500 t TO 236,375 t, another new series low.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,019.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,012.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $49.50 BENEATH THE 3,061.5 JULY LOW, $65.00 beneath the 3,077 weekly 50% retracement and $277.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 still holds, $17.00 above the rule-based cap on daily wave (v) near 2,977.5."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+7.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,019.00 against three-month $3,012.00 is a $7.00 BACKWARDATION, widened from $2.00 while the three-month price was unchanged. The reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is still UNMET; the bearish structural confirmation, a contango beyond $24.50, is also unmet. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"236,375","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 1,500 t TO 236,375 t, another new series low (Crux Investor's 14-October analysis of LME data called the level the lowest registered of the 21st century). September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,012.00, UNCHANGED ON THE DAY - $49.50 beneath the 3,061.5 July low, a sixth settled close below it, and $1.50 above the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 1,500 t TO 236,375 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":2.0,"avg":sep_sp,"note":VER+f" A $7.00 BACKWARDATION, WIDENED FROM $2.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Three-month was unchanged while cash rose $5.00, so the prompt firmed against a flat forward. REVERSAL CONDITION, RESTATED UNCHANGED: a BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1229,"prev":1.1257,"avg":1.1465,"note":VER+" THE LME EURO FIXING EASED TO 1.12290 FROM 1.12570 at the Monday ring; the ECB fixing printed 1.12250 and BFIX 1.12288. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (19-Oct official)","price":"3,019.0","basis":"THE 19-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,019.00, UP $5.00 OR 0.17%. Next official Tuesday 20-October 13:20 London."},
 {"tenor":"3-month (19-Oct official)","price":"3,012.0","basis":"THE 19-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,012.00, UNCHANGED - $49.50 beneath the 3,061.5 July low (sixth settled close below it), $1.50 above the 02-January official."},
 {"tenor":"Cash-to-3M structure","price":"+7.0 (BACKWARDATION)","basis":"A $7.00 BACKWARDATION, widened from $2.00 with three-month unchanged."},
 {"tenor":"Visible LME stock","price":"236,375 t","basis":f"DOWN 1,500 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE PROMPT FIRMED AGAINST A FLAT FORWARD. On the 19-October official cash $3,019.00 sits $7.00 ABOVE three-month $3,012.00, a BACKWARDATION, widened from $2.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50, $2.00 and now $7.00. "
 f"READ: a third straight backwardation while visible stock keeps setting lows (236,375 t) - a modest prompt-tightness signal, not a squeeze. The September mean spread was ${sep_sp:,.2f}. The reversal condition (a backwardation beyond $15.00) is unmet; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]

ls=d['lme_series']; assert ls[-1][0]=='16-Oct', ls[-1]
d['lme_series']=ls[1:]+[["19-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14496.0,14378.0,14595.0,14485.0); NI=(15275.0,15490.0,15170.0,15355.0); ZN=(3776.0,3737.0,3739.0,3699.0); PB=(1856.0,1891.0,1854.0,1891.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# October cash average-to-date: 01-15 Oct (11 sessions, per 17-Oct script, Westmetall tables) + 16-Oct + 19-Oct
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/13)/(sum(zs)/12),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/13)/(sum(ps)/12),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-19'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending MONDAY 19-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 28-September dropped and 19-October appended, so the window is 29-September to 19-October. Every point is an official cash settlement; the 19-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 16-October. Next official Tuesday 20-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (19-October-2026 session; stock lines reconciled against 16-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,496.00, down $99.00 or 0.68%; three-month $14,378.00, down $107.00 or 0.74% - the weakest metal on the board this session. Backwardation $118.00 from $110.00. Stock ROSE 6,750 tonnes to 232,175, the first build after nine straight draws."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,275.00, up $105.00 or 0.69%; three-month $15,490.00, up $135.00 or 0.88%. CONTANGO widened to $215.00 from $185.00, still the widest carry on the board. Stock edged up 120 tonnes to 280,110."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,776.00, up $37.00 or 0.99%; three-month $3,737.00, up $38.00 or 1.03% - the strongest gain on the board. BACKWARDATION $39.00 from $40.00 even as another 4,775 tonnes were delivered in, lifting stock to 163,050 t - a sixth straight large inflow. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,856.00, up $2.00 or 0.11%; three-month $1,891.00, unchanged. CONTANGO $35.00 from $37.00. Stock drew 1,150 tonnes to 338,125, a twenty-first consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Monday 19-October official the board split - zinc three-month +1.03%, nickel +0.88%, aluminium and lead unchanged, copper -0.74% - as the dollar index firmed toward 102 on euro weakness (Trading Economics). The LME euro fixing eased to 1.1229.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='16-Oct'
        i['hist']=i['hist'][1:]+[["19-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,378.00 (3M); 14,496.00 (cash) $/t"
        i['ratio']="~14,496.00 $/t cash vs LME 3M 14,378.00 $/t"
        i['trend']='flat'
        i['src']=("LME official cash settlement, rolled to the MONDAY 19-OCTOBER-2026 session at $14,496.00, DOWN $99.00 or 0.68% against $14,595.00. THE WINDOW ROLLED THIS RUN: 28-September dropped and 19-October appended, so the series is the last fifteen published official cash sessions, 29-September to 19-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 16-October). "
                  "Copper structure for context: backwardation $118.00 (from $110.00), stock rose 6,750 t to 232,175 t.")
    elif i['name']=='Pre-baked anodes':
        assert i['hist'][-1]==['Sep-26',5730]
        i['hist']=i['hist']+[['Oct-26',6130]]; i['hist']=i['hist'][-15:]
        i['val']="~6,130"; i['trend']='up'
        i['src']=("UPDATED 20-OCTOBER: THE OCTOBER-2026 SETTLEMENT CYCLE HAS PRINTED. Mysteel (16-October) reports a major Shandong-based smelter raised its benchmark prebaked-anode purchase price by Yuan 400/t from September to Yuan 6,130/t (cash; Yuan 6,147/t by acceptance) - above Yuan 6,000 for the first time in 44 months on a feedstock rally - against an estimated production cost of about Yuan 6,167.5/t. "
                  "BASIS OF THE HISTORY SERIES: the monthly Shandong benchmark tender, cash price, Yuan/t (one smelter's benchmark, not a national average); October appended at 6,130, consistent with the carried September mark of 5,730 plus the reported Yuan 400 increase. Nothing is interpolated or estimated. Source: "+L_AN+" "+S_AN)
    elif i['name'].startswith('Calcined petroleum coke'):
        assert i['hist'][-1][0]=='Jun cycle'
        i['hist']=i['hist']+[['Oct cycle',3610.5]]
        i['src']=("UPDATED 20-OCTOBER: THE OCTOBER-2026 CARBON SETTLEMENT CYCLE HAS PRINTED FOR THE FEEDSTOCK. This row's value column is the anode-grade CPC range ($/t, carried at its last public assessment); its HISTORY charts the FEEDSTOCK - Shandong green petroleum coke grade 3B, settlement-cycle average, Yuan/t. Mysteel (16-October) reports the October-cycle 3B average at Yuan 3,610.5/t, DOWN Yuan 27.6, while 3A rose Yuan 49.8 to 3,743.4 and 3C rose Yuan 231.4 to 3,305.2; appended as 'Oct cycle'. "
                  "The July-September cycles were not located in a dated public print and remain gaps - nothing is interpolated or estimated. Source: "+L_AN+" "+S_AN)
    elif i['name'].startswith('Coal tar pitch'):
        i['src']=("REVIEWED 20-OCTOBER: Mysteel (16-October) reports the October settlement-cycle average for MODIFIED coal-tar pitch at Yuan 7,244/t in Shandong (up Yuan 2,222) and Yuan 7,148/t in Shanxi (up Yuan 2,167) - a sharp rise that fed the Yuan 400/t anode increase. That print is on a DIFFERENT BASIS (settlement-cycle average, modified pitch) from this row's weekly history series, so it is reported here as context and NOT appended to the history; the value column is carried at its last same-basis mark. Gaps stay gaps; nothing is interpolated or estimated. Source: "+L_AN+" "+S_AN)
d['inputs_summary']=("UPDATE 20-OCTOBER: THE OCTOBER CARBON SETTLEMENT CYCLE HAS PRINTED (Mysteel, 16-October): the Shandong benchmark prebaked-anode price rose Yuan 400/t to Yuan 6,130/t (appended to the anode history), above Yuan 6,000 for the first time in 44 months, as modified coal-tar pitch jumped about Yuan 2,200/t (context only - different basis from the pitch history) while green petcoke 3B eased Yuan 27.6 to Yuan 3,610.5/t (appended to the CPC feedstock history). Copper rolled to the Monday 19-October LME official cash of $14,496.00, down $99.00, with its fifteen-session window moved to 29-September to 19-October. No new dated SMM fluoride, silicon or magnesium mark was retrievable this run. Every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 16-October official cash of \$3,014\.00, or \$1,507\.00, UP \$7\.50 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$896\.00, so 62\.7%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 19-October official cash of $3,019.00, or ${tl:,.2f}, UP $2.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED MONDAY 19-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE FRIDAY 16-OCTOBER OFFICIAL; MARKET SHUT AT THE WEEKEND)."; NEWC="COMPILED TUESDAY 20-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING) (LME BOARD ON THE MONDAY 19-OCTOBER OFFICIAL)."
n=0;nc=0
for p in d['premiums']:
    p['src'],k=OLDT.subn(NEWT,p['src']); n+=k; nc+=p['src'].count(OLDC)
    p['src']=p['src'].replace(OLDC,NEWC)
print('premium tariff replaced',n,'compiled',nc); assert n==len(d['premiums'])
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    s=s.replace("THE RATIO: LME Alumina at $360.40/t against the 16-October aluminium three-month of $3,012.00 is 11.97%","THE RATIO: LME Alumina at $360.40/t against the 19-October aluminium three-month of $3,012.00 is 11.97%")
    a['src']=s

d['lme_commentary']=("A FLAT FORWARD, A FIRMER PROMPT. On the Monday 19-October official cash settled $3,019.00, up $5.00, and three-month $3,012.00, unchanged - still $49.50 beneath the 3,061.5 July low and $1.50 above the 02-January three-month official. "
 "The backwardation widened to $7.00 from $2.00, a third straight backwardation, and visible stock fell 1,500 t to a new series low of 236,375 t. The rest of the board split: zinc +1.0% and nickel +0.9%, copper -0.7% as its stocks rose 6,750 t; the dollar index firmed toward 102 on euro weakness (Trading Economics). "
 "Fresh China data cut both ways: the statistics bureau's September primary aluminium output of 3.91 Mt took Q3 to a record 11.84 Mt (+2.2% y/y), a pace of about 46.7 Mt a year - above the 45 Mt policy ceiling (Finimize, citing Reuters' calculation) - while September unwrought primary imports fell 30.3% y/y to about 172 kt (SMM). "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND STILL IN CONTROL; THE PROMPT IS FIRMING BUT PRICE IS NOT. Against: three-month has settled beneath 3,061.5 six times; China ran a record Q3 at an annualised pace of about 46.7 Mt, above its 45 Mt ceiling, and its September primary imports fell 30% y/y, so less Chinese pull on ex-China metal; a December Fed hike is still priced and the dollar firmed toward 102; Gulf restarts continue. "
 "Constructive: visible LME stock fell to another 21st-century low of 236,375 t and the backwardation widened to $7.00; China's Q3 GDP beat (4.5%); carbon costs jumped (October anode benchmark +Yuan 400/t to Yuan 6,130/t) and energy stays expensive - Brent near $109, European gas about EUR 88/MWh - which lifts the smelter cost floor.")
d['bottom_line']=("BOTTOM LINE: aluminium held on the Monday 19-October LME official - cash $3,019.00 (+$5.00), three-month $3,012.00 (unchanged) - $49.50 beneath the 3,061.5 July low. "
 "The backwardation widened to $7.00 and visible stock fell to another low of 236,375 t, while China's record Q3 output (11.84 Mt) keeps the supply side heavy. Scenario weights are held at 10% bull / 45% base / 45% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) still has its 2,994.50 settled low unconfirmed as the wave (v) end; a settled close above 3,077 would confirm it, below about 2,977.5 would force a re-count; invalidation 3,289; the weekly corrective count towards 2,894 stays preferred.")
c=d['commercial']
c2=c.replace("FIRST, THE CURVE IS FLAT: a $2.00 backwardation on 16-October, narrowed from $4.50, so there is no carry reward for waiting and no prompt squeeze either.","FIRST, THE PROMPT IS FIRMING: a $7.00 backwardation on 19-October, widened from $2.00 with three-month unchanged, so there is no carry reward for waiting, though it is far from a squeeze.")
c2=c2.replace("is $1,507.00 on 16-October cash, 62.7% of the $2,403/t premium",f"is ${tl:,.2f} on 19-October cash, {share:.1f}% of the $2,403/t premium")
c2=c2.replace("the 16-October official bounced to $3,012.00 after a 2,994.50 settled low inside the 2,980-3,000 zone, still $49.50 beneath 3,061.5;","the 19-October official held three-month at $3,012.00 after a 2,994.50 settled low inside the 2,980-3,000 zone, still $49.50 beneath 3,061.5;")
c2=c2.replace("China's September output data and the October carbon settlements are due in the coming week, and the Q3 producer season continues (Rio Tinto's operations review on 14-October kept aluminium guidance; Norsk Hydro reports later in October).","China's September output came in at 3.91 Mt for a record Q3 and the October anode benchmark rose Yuan 400/t; the Q3 producer season continues (Rio Tinto's operations review on 14-October kept aluminium guidance; Norsk Hydro reports on 23-October).")
assert c2.count('19-October')>=2 and '23-October' in c2, c2; d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 20-OCTOBER at 10/45/45: the Monday 19-October official left three-month unchanged at $3,012.00 with a wider $7.00 backwardation and stock at a new low, but China's record Q3 output keeps supply heavy; neither pre-registered trigger (2,977.5 / 3,077) was hit. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium held flat at $3,012 on Monday's LME official as stocks hit another low and the cash premium widened, but China's record third-quarter output - running above Beijing's 45 Mt ceiling - keeps the supply side heavy.",
 "points":[
 "WHAT MOVED: Monday's LME official settled cash at $3,019.00 (+$5.00) and three-month at $3,012.00 (unchanged), $49.50 below the $3,061.5 July low. Cash's premium over three-month (backwardation) widened to $7.00 from $2.00, and LME stock fell 1,500 t to a new low of 236,375 t. Zinc and nickel rose about 1%, copper fell 0.7%.",
 "WHY IT IS STUCK: China produced 3.91 Mt of primary aluminium in September for a record 11.84 Mt in Q3 (+2.2% y/y), an annual pace of about 46.7 Mt - above the 45 Mt policy cap - and its September primary-metal imports fell 30% y/y to about 172 kt, so less Chinese demand for metal from elsewhere. The dollar firmed toward 102.",
 "COSTS ARE RISING: China's October prebaked-anode benchmark rose Yuan 400/t to Yuan 6,130/t, above Yuan 6,000 for the first time in 44 months, on a jump in pitch prices; Brent holds near $109 and European gas near EUR 88/MWh, the highest since December 2022.",
 "WHAT TO WATCH: whether three-month settles back above $3,061.5-3,077 (decline ending) or below about $2,977.5 (new leg lower); whether the backwardation extends beyond $15; Norsk Hydro's Q3 results on 23-October; the 27-28 October FOMC (markets price a hold)."]}

d['feed']=([
 {"when":"Tue 20-Oct","impact":"Mixed","text":"BOARD ROLLED TO THE MONDAY 19-OCTOBER LME OFFICIAL: cash $3,019.00 (+$5.00), three-month $3,012.00 (unchanged), backwardation widened to $7.00 from $2.00, stock down 1,500 t to a new low of 236,375 t."},
 {"when":"Tue 20-Oct","impact":"Mixed","text":"China September unwrought primary aluminium imports about 172 kt (-7.2% m/m, -30.3% y/y), exports about 45 kt; January-September imports about 1.829 Mt, -6.8% y/y (SMM)."},
 {"when":"Mon 19-Oct","impact":"Bearish","text":"China September primary aluminium output 3.91 Mt; Q3 a record 11.84 Mt (+2.2% y/y), annualised pace about 46.7 Mt vs the 45 Mt cap (NBS data, Reuters calculation via Finimize)."},
 {"when":"Fri 16-Oct","impact":"Bullish (cost)","text":"October prebaked-anode benchmark (major Shandong smelter) +Yuan 400/t to Yuan 6,130/t cash, above Yuan 6,000 for the first time in 44 months; modified pitch settlement averages up about Yuan 2,200/t (Mysteel)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Mixed","url":W,
  "headline":"LME ALUMINIUM HOLDS, PROMPT FIRMS. The Monday 19-October official settled cash at $3,019.00 (+0.17%) and three-month unchanged at $3,012.00, $49.50 beneath the 3,061.5 July low. The backwardation widened to $7.00 from $2.00 and visible stock fell 1,500 t to a new low of 236,375 t. Elsewhere zinc three-month rose 1.03% and nickel 0.88% while copper fell 0.74% as copper stock rose 6,750 t, its first build after nine draws."},
 {"theme":"Supply","horizon":"0-3 months","impact":"Bearish","url":S_CO,
  "headline":"CHINA RUNS A RECORD QUARTER ABOVE ITS CAP (statistics bureau data, 19-October, as reported by Finimize citing Reuters): primary aluminium output was 3.91 Mt in September, taking the third quarter to a record 11.84 Mt, up 2.2% year on year. Reuters estimates output is running at about 46.7 Mt a year, roughly 1.7 Mt above the 45 Mt capacity cap in place since 2017. READ: Chinese supply is not tightening on its own, which keeps the global balance heavier than the LME stock draw alone suggests."},
 {"theme":"Trade","horizon":"0-3 months","impact":"Bearish","url":S_IM,
  "headline":"CHINA'S PRIMARY-METAL IMPORTS FALL (SMM, 20-October, customs data): September imports of unwrought primary aluminium were about 172 kt, down 7.2% m/m and 30.3% y/y; exports about 45 kt, up 54.1% y/y; net imports about 127 kt, down 41.5% y/y. January-September imports about 1.829 Mt (-6.8% y/y). READ: less Chinese pull on ex-China metal, consistent with the weak offers SMM reported across Asia on 16-October."},
 {"theme":"Costs","horizon":"0-1 month","impact":"Bullish (cost)","url":S_AN,
  "headline":"ANODE COSTS JUMP (Mysteel, 16-October): a major Shandong smelter raised its October prebaked-anode benchmark by Yuan 400/t to Yuan 6,130/t (cash), above Yuan 6,000 for the first time in 44 months, against an estimated production cost of about Yuan 6,167.5/t. Modified coal-tar pitch settlement averages rose about Yuan 2,200/t (Shandong Yuan 7,244/t), while green petcoke 3B eased Yuan 27.6 to Yuan 3,610.5/t. READ: carbon is a rising line in smelter cash cost, adding to the energy-cost floor."},
 {"theme":"Earnings","horizon":"0-1 month","impact":"Mixed","url":S_HY,
  "headline":"NORSK HYDRO REPORTS Q3 ON 23-OCTOBER (company notice, 16-October): results and presentation at 07:00 CEST on hydro.com, followed by a webinar at 08:30 CEST. The next read on European premiums, energy costs and the Qatalum and Slovalco restarts."},
]+d['news']
d['news']=d['news'][:20]

cats=d['outlook']['catalysts']
for cat in cats:
    if cat['date']=='Mon 19 - Tue 20-Oct' and cat['event'].startswith('CHINA SEPTEMBER ACTIVITY DATA'):
        cat['date']='Resolved Mon 19-Oct'
        cat['event']="CHINA SEPTEMBER ACTIVITY DATA - RESOLVED: September primary aluminium output 3.91 Mt, Q3 a record 11.84 Mt (+2.2% y/y), an annualised pace of about 46.7 Mt against the 45 Mt cap (Finimize citing Reuters' calculation from statistics bureau data, 19-October). Q3 GDP +4.5% y/y."
        cat['impact']='Medium'
    if cat['date']=='Daily, from Mon 19-Oct':
        cat['date']='Daily, from Tue 20-Oct'
        cat['event']="3,061.5 BROKEN ON SIX SETTLED OFFICIALS; THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE AND $17.00 ABOVE THE RULE-BASED CAP, THEN HELD 3,012.00 ON 16- AND 19-OCTOBER. A settled close beneath about 2,977.5 would break the cap on daily wave (v) and force a re-count (extended fifth or larger correction toward the 2,894 weekly 61.8%); a settled recovery above 3,077 would signal wave (v) is complete; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289."
cats.insert(1,{"date":"Fri 23-Oct","impact":"Medium","event":"NORSK HYDRO Q3-2026 RESULTS, 07:00 CEST (company notice, 16-October): European premiums, energy costs and restart progress at Qatalum and Slovalco."})
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 20-OCTOBER: the backwardation widened to $7.00 on 19-October from $2.00 with three-month unchanged - a third straight backwardation. Trend held at FLAT."
RK[4]['risk']+=" UPDATE 20-OCTOBER: LME stock fell 1,500 t to a new series low of 236,375 t on 19-October. Trend held at FLAT."
hitc=0
for r in RK:
    if r['risk'].startswith('THE CHINESE TRADE PULL'):
        r['risk']+=" UPDATE 20-OCTOBER: China's September unwrought primary imports fell 30.3% y/y to about 172 kt (SMM) while output ran a record Q3 at about 46.7 Mt annualised (Reuters via Finimize). Trend held at UP."; hitc+=1
    if r['risk'].startswith('THE CHINESE DOWNSTREAM OVERHANG'):
        r['risk']+=" UPDATE 20-OCTOBER: record Q3 primary output (11.84 Mt, +2.2% y/y) above the 45 Mt cap pace supports the overhang read. Trend held at UP."; hitc+=1
    if r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 20-OCTOBER: the October Shandong anode benchmark rose Yuan 400/t to Yuan 6,130/t on a ~Yuan 2,200/t pitch jump (Mysteel, 16-October), and TTF holds near EUR 88/MWh. Trend RAISED from FLAT to UP: carbon and energy costs are both rising."; r['trend']='up'; hitc+=1
assert hitc==3
d['outlook']['ai_analysis'].insert(0,"TUESDAY 20-OCTOBER ON THE MONDAY 19-OCTOBER OFFICIAL: three-month unchanged at $3,012.00 with cash up $5.00, so the backwardation widened to $7.00 and visible stock fell to a new low of 236,375 t - the prompt is firming even though the flat price is not. Against that, China's statistics bureau data show a record Q3 (11.84 Mt, about 46.7 Mt annualised, above the 45 Mt cap) and September primary imports down 30% y/y, so Chinese supply is ample and its pull on ex-China metal is weaker. Costs are rising - the October anode benchmark +Yuan 400/t - which supports a floor rather than a rally. Weights held at 10/45/45; Norsk Hydro's Q3 on 23-October and the 27-28 October FOMC are the next catalysts.")

EWS=("REVIEWED 20-OCTOBER ON THE MONDAY 19-OCTOBER OFFICIAL: three-month settled unchanged at $3,012.00, a second close above the 2,994.50 settled low of 15-October, which remains $17.00 above the rule-based cap near 2,977.5; wave (v) of C ($154.00 from the 3,148.5 wave (iv) high) stays shorter than (iii)'s $171 and the impulse rules hold. Count unchanged; the 2,994.50 low is consistent with a completed wave (v) but is NOT yet confirmed and not locked. Base case about 65%: a corrective rebound toward 3,061.5-3,077 (confirmed by a settled close above 3,077); alternate about 35%: a settled close beneath 2,977.5 forces a re-count toward 2,894. Invalidation 3,289; confidence moderate. ")
st=d['ew']['short_term']['writeup']; pre="REVIEWED 19-OCTOBER (MONDAY, BEFORE THE RING; NO NEW SESSION SINCE 16-OCTOBER): count and levels unchanged - wave (v) low at 2,994.50 possible but not confirmed; invalidation 3,289; rule-based cap near 2,977.5. "
assert st.startswith(pre); d['ew']['short_term']['writeup']=EWS+st[len(pre):]
lt=d['ew']['long_term']['writeup']; pre="REVIEWED 19-OCTOBER (PRE-RING): the weekly close of 3,012.00 stands; count unchanged. "
assert lt.startswith(pre)
d['ew']['long_term']['writeup']="REVIEWED 20-OCTOBER (MONDAY 19-OCTOBER OFFICIAL, FIRST SESSION OF THE NEW WEEK): three-month unchanged at 3,012.00, still in the lower half of the 2,950-3,110 zone and beneath the 3,061.5 July low; the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label. "+lt[len(pre):]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="109.46",day="about $109.46 on 20-October, -0.09% (Trading Economics)",
 note="REFRESHED TUESDAY 20-OCTOBER-2026 (Trading Economics): Brent held just above $109 as traders weighed Middle East and Eastern European conflicts; the US Energy Secretary said Persian Gulf oil shipments had recovered to about 80% of pre-war levels, though refined-product deliveries remain limited; Iranian attacks on commercial ships near Hormuz were also reported. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="88.4",day="about EUR 88.42/MWh on 20-October, +0.43% (Trading Economics; stats section EUR 88.43, +0.45%)",
 note="REFRESHED TUESDAY 20-OCTOBER-2026 (Trading Economics): above EUR 88/MWh, the highest since December 2022; limited Gulf LNG (about 80% below last year) is slowing storage refill, which sits below seasonal norms. Value approximate. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.9",day="about 101.89 on 20-October, -0.11%, after rising toward 102 on Monday (Trading Economics)",
 note="REFRESHED TUESDAY 20-OCTOBER-2026 (Trading Economics): the dollar rose toward 102 on Monday mainly on euro weakness tied to protests in France and Russia-Ukraine escalation; markets price about an 84% chance of an October 27-28 Fed hold. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="5.13",day="about 5.13% on 20-October, -0.01pp; edged up on Monday after a ~15bp fall the prior week (Trading Economics)",
 note="REFRESHED TUESDAY 20-OCTOBER-2026 (Trading Economics): markets see high odds of a Fed hold next week and a meaningful chance of a December hike after above-forecast CPI and PPI. Higher yields raise the cost of carrying metal. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.12290',day="LME fixing on 19-October, -0.25% from 1.12570; ECB fixing 1.12250, BFIX 1.12288",
 note="REFRESHED TUESDAY 20-OCTOBER-2026 to the 19-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE MONDAY 19-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED OFFICIAL. This Tuesday 20-October run is compiled about 03:35 London, BEFORE today's ring; Tuesday's official prints at 13:20 London and will appear on the next run. Reference and intraday prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (20-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 19-October session, and the per-metal aluminium daily table's newest row is 19-October (cash 3,019.00, three-month 3,012.00, stock 236,375), so the board is current rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.12570, ECB 1.12530, BFIX 1.12561) matches the 16-October board verified on 17-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 16-October: aluminium -1,500 to 236,375; copper +6,750 to 232,175; nickel +120 to 280,110; zinc +4,775 to 163,050; lead -1,150 to 338,125.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (19-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (thirteen sessions, 01- to 19-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,012.00; the stock chart axis floor (225,000 t) brackets visible stock at 236,375 t - both re-checked this run; the stock floor has about 11,400 t of headroom and will be re-bracketed before it is approached.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,019.00 against three-month $3,012.00 is therefore a $7.00 BACKWARDATION, widened from $2.00 on 16-October while three-month was unchanged."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 19-October official cash of $3,019.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."; hit+=1
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $109.46), the dollar index (about 101.9), TTF (about EUR 88.4/MWh) and the US ten-year (about 5.13%) are Trading Economics readings shown on 20-October (early Tuesday trading) - the source's own sections differ slightly, so they are approximate; EUR/USD is the 19-October LME fixing, the same session as the board."; hit+=1
    if cv.startswith("FETCH NOTE 19-OCTOBER"):
        C[i]=("FETCH NOTE 20-OCTOBER: no authorised fetch was blocked. AL Circle's news page and the Mining Weekly, Business Recorder and AL Circle articles on China's September output returned HTTP 403; China's output figures are therefore taken from Finimize's article citing the statistics bureau and Reuters' calculation (3.91 Mt September, 11.84 Mt Q3 +2.2% y/y, ~46.7 Mt annualised) and other figures seen only in search snippets are NOT published. "
              "The anode, pitch and petcoke figures come from a single Mysteel report of one Shandong smelter's benchmark and were not cross-checked against a second source. No new dated wire report on Hormuz traffic was located; Trading Economics' 20-October Brent note cites the US Energy Secretary on Gulf oil shipments at about 80% of pre-war levels."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: NO NEW EARNINGS WERE REPORTED BY TRACKED PEERS SINCE ALCOA (15-October); NORSK HYDRO REPORTS Q3 ON 23-OCTOBER. Rio Tinto's row carries its 14-October Q3 operations note (production only). NO NEW COMPANY WAS BACK-FILLED THIS RUN. Other entries are carried at their last publicly verified figures, and gaps stay gaps."; hit+=1
assert hit==4,hit

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 19-OCTOBER: no newer public disclosure","REVIEWED 20-OCTOBER: no newer public disclosure").replace("REVIEWED 19-OCTOBER. NO NEW DATED","REVIEWED 20-OCTOBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('China operators'):
        hit+=1
        p['update']=re.sub(r"^REVIEWED 20-OCTOBER: no newer public disclosure located; status below carried\. ","",p['update'])
        p['update']=("UPDATED 20-OCTOBER FROM THE STATISTICS BUREAU'S SEPTEMBER DATA (19-October, as reported by Finimize citing Reuters): primary aluminium output 3.91 Mt in September and a record 11.84 Mt in Q3 (+2.2% y/y), an annualised pace of about 46.7 Mt - roughly 1.7 Mt above the 45 Mt capacity cap in place since 2017. September unwrought primary imports fell 30.3% y/y to about 172 kt (SMM, 20-October). ")+p['update']
        p['src']=[L_CO,S_CO]
assert hit==1

for s in [[L_TE,S_TE],[L_CO,S_CO],[L_IM,S_IM],[L_AN,S_AN],[L_HY,S_HY],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG]]:
    d['sources'].append(s)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 19-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 16-Oct)",W])
d['outlook']['sources'].append([L_CO,S_CO]); d['outlook']['sources'].append([L_IM,S_IM]); d['outlook']['sources'].append([L_AN,S_AN])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-16'
ph['rows'].append(['2026-10-19',cash,m3,stk]); ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
