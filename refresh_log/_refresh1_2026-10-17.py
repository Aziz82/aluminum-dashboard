# Daily data refresh - 2026-10-17 (SATURDAY, compiled ~03:40 London). Board ROLLED to FRIDAY 16-Oct LME official (last session of the week; no ring Sat/Sun).
# Westmetall cache-busted EN AND DE overviews BOTH fetched and agree on the full 16-Oct session; per-metal Al table shows NO row after 16-Oct.
# Completeness: 5/5 stock-change lines reconcile vs verified 15-Oct board; prior-day FX column (MTLE 1.12080) matches 15-Oct board.
# TE aluminium/Brent/TTF/DXY/10Y fetched; Rio Tinto Q3-2026 operations review (6-K, 14-Oct) fetched - missed by prior runs; SMM 16-Oct items fetched.
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-17'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (16/17-Oct-2026)"
S_RIO="https://www.sec.gov/Archives/edgar/data/0000863064/000086306426000041/ex1prodresults.htm"; L_RIO="Rio Tinto - Third quarter 2026 operations review (Form 6-K exhibit, 14-Oct-2026)"
S_OV="https://news.metal.com/newscontent/104162844-smm-analysis-overseas-primary-aluminum-market-remains-weak-offer-prices-under-pressure-across-major-markets"; L_OV="SMM - Overseas primary aluminum market remains weak; offer prices under pressure across major markets (16-Oct-2026)"
S_AI="https://news.metal.com/newscontent/104162867-30000-tonnes-alumina-traded-at-382mt-fob-india-shipment-in-november-2026"; L_AI="SMM - 30,000 t alumina traded at $382/mt FOB India, November shipment (16-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (16/17-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (16/17-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (16/17-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (16/17-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
cash,prev_c,m3,prev_m,stk,prev_s=3014.0,2999.0,3012.0,2994.5,237875,238125
spr=cash-m3; pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100
assert spr==2.0
ytd=(m3/3010.5-1)*100

VER=("COMPILED SATURDAY 17-OCTOBER-2026. THE BOARD IS THE FRIDAY 16-OCTOBER-2026 LME OFFICIAL - THE LAST SESSION OF THE WEEK AND THE CORRECT FIGURE TO CARRY, because there is no ring on Saturday or Sunday; the next official prints Monday 19-October 13:20 London. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 16-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.12570); their prior-day FX column (MTLE 1.12080) matches the verified 15-October board, and the per-metal aluminium table shows NO row after 16-October; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 15-October: aluminium 238,125 less 250 to 237,875; copper 226,600 less 1,175 to 225,425; nickel 282,066 less 2,076 to 279,990; zinc 151,050 plus 7,225 to 158,275; lead 339,800 less 525 to 339,275. "
 "The whole board sits on ONE UNIFORM SESSION (16-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(f" CASH SETTLED $3,014.00 ON THE 16-OCTOBER OFFICIAL, UP $15.00 OR {pc:.2f}% FROM $2,999.00. THREE-MONTH SETTLED $3,012.00, UP $17.50 OR {pm:.2f}% FROM $2,994.50 - a first up-day after four consecutive declines, back $1.50 ABOVE the first-published 2026 three-month official of $3,010.50 (year to date {ytd:+.2f}%) but still a FIFTH settled close beneath the 3,061.5 July low (by $49.50). On the week three-month fell $58.00 from the 09-October close of $3,070.00. "
 "THE BACKWARDATION NARROWED to $2.00 from $4.50 - SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS AGAIN (price up, prompt premium smaller). "
 "VISIBLE LME STOCK FELL 250 t TO 237,875 t, another new series low. The rebound came as the dollar index fell 0.75% to about 101.8, its first weekly decline in four weeks (Trading Economics).")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,014.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,012.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $49.50 BENEATH THE 3,061.5 JULY LOW, $65.00 beneath the 3,077 weekly 50% retracement and $277.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held $17.00 above the rule-based cap on daily wave (v) near 2,977.5."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+2.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,014.00 against three-month $3,012.00 is a $2.00 BACKWARDATION, narrowed from $4.50. Spread and flat price moved in OPPOSITE directions this session (price up, prompt premium smaller). The reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is still UNMET; the bearish structural confirmation, a contango beyond $24.50, is also unmet. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"237,875","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 250 t TO 237,875 t, another new series low (the lowest registered level of the 21st century per Crux Investor's 14-October analysis of LME data). September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,012.00, UP $17.50 OR {pm:.2f}% FROM $2,994.50 - $49.50 beneath the 3,061.5 July low, a fifth settled close below it, and $1.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 250 t TO 237,875 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":4.5,"avg":sep_sp,"note":VER+f" A $2.00 BACKWARDATION, NARROWED FROM $4.50. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in OPPOSITE directions this session (three-month up $17.50, backwardation $2.50 smaller). REVERSAL CONDITION, RESTATED UNCHANGED: a BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1257,"prev":1.1208,"avg":1.1465,"note":VER+" THE LME EURO FIXING FIRMED TO 1.12570 FROM 1.12080 at the Friday ring; the ECB fixing printed 1.12530 and BFIX 1.12561. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (16-Oct official)","price":"3,014.0","basis":f"THE 16-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,014.00, UP $15.00 OR {pc:.2f}%. Market shut Saturday/Sunday; next official Monday 19-October 13:20 London."},
 {"tenor":"3-month (16-Oct official)","price":"3,012.0","basis":f"THE 16-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,012.00, UP $17.50 OR {pm:.2f}% - $49.50 beneath the 3,061.5 July low (fifth settled close below it), $1.50 above the 02-January official; down $58.00 on the week."},
 {"tenor":"Cash-to-3M structure","price":"+2.0 (BACKWARDATION)","basis":"A $2.00 BACKWARDATION, narrowed from $4.50. Flat price and spread moved in OPPOSITE directions."},
 {"tenor":"Visible LME stock","price":"237,875 t","basis":f"DOWN 250 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE PROMPT PREMIUM EASED AS THE FLAT PRICE BOUNCED. On the 16-October official cash $3,014.00 sits $2.00 ABOVE three-month $3,012.00, a BACKWARDATION, narrowed from $4.50. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, then backwardations of $4.50 and now $2.00. "
 f"READ: the curve is essentially flat - neither a prompt squeeze nor a glut - while visible stock keeps setting lows (237,875 t). Spread and price moved in OPPOSITE directions for a second session. The September mean spread was ${sep_sp:,.2f}. The reversal condition (a backwardation beyond $15.00) is unmet; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]

ls=d['lme_series']; assert ls[-1][0]=='15-Oct', ls[-1]
d['lme_series']=ls[1:]+[["16-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14595.0,14485.0,14539.0,14362.0); NI=(15170.0,15355.0,14885.0,15125.0); ZN=(3739.0,3699.0,3724.0,3681.5); PB=(1854.0,1891.0,1853.0,1889.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/12)/(sum(zs)/11),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/12)/(sum(ps)/11),1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])): R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-16'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending FRIDAY 16-OCTOBER-2026 (the last session before the weekend). THE WINDOW ROLLED THIS RUN: 25-September dropped and 16-October appended, so the window is 28-September to 16-October. Every point is an official cash settlement; the 16-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 15-October. Next official Monday 19-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (16-October-2026 session; stock lines reconciled against 15-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,595.00, up $56.00 or 0.39%; three-month $14,485.00, up $123.00 or 0.86%. Backwardation NARROWED to $110.00 from $177.00 as the forward led the bounce; stock DREW 1,175 tonnes to 225,425 - a ninth straight draw."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,170.00, up $285.00 or 1.91%; three-month $15,355.00, up $230.00 or 1.52% - the strongest rebound on the board after Thursday's 3.5% fall. CONTANGO narrowed to $185.00 from $240.00, still the widest carry on the board. Stock fell 2,076 tonnes to 279,990."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,739.00, up $15.00 or 0.40%; three-month $3,699.00, up $17.50 or 0.48%. BACKWARDATION eased to $40.00 from $42.50 as another 7,225 tonnes were delivered in, lifting stock to 158,275 t - a fifth straight large inflow. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,854.00, up $1.00 or 0.05%; three-month $1,891.00, up $2.00 or 0.11%. CONTANGO $37.00 from $36.00. Stock drew 525 tonnes to 339,275, a twentieth consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Friday 16-October official every base metal rose - nickel three-month 1.52%, copper 0.86%, aluminium 0.58% to $3,012.00, zinc 0.48% and lead 0.11% - as the dollar index fell about 0.75% to near 101.8, its first weekly decline after three weeks of gains (Trading Economics). The LME euro fixing firmed to 1.1257.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='15-Oct'
        i['hist']=i['hist'][1:]+[["16-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,485.00 (3M); 14,595.00 (cash) $/t"
        i['ratio']="~14,595.00 $/t cash vs LME 3M 14,485.00 $/t"
        i['trend']='flat'
        i['src']=("LME official cash settlement, rolled to the FRIDAY 16-OCTOBER-2026 session at $14,595.00, UP $56.00 or 0.39% against $14,539.00. THE WINDOW ROLLED THIS RUN: 25-September dropped and 16-October appended, so the series is the last fifteen published official cash sessions, 28-September to 16-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 15-October). "
                  "Copper structure for context: backwardation $110.00 (from $177.00), stock drew 1,175 t to 225,425 t.")
d['inputs_summary']=("UPDATE 17-OCTOBER: copper rolled to the Friday 16-October LME official cash of $14,595.00, up $56.00, with its fifteen-session window moved to 28-September to 16-October. No new dated SMM fluoride, silicon or magnesium price mark was retrievable from the panel's sources this run (SMM's 16-October magnesium note reports national inventory down 3.52% m/m and prices at a year low, but its price figure could not be retrieved, so nothing was appended); the October carbon settlement cycle (prebaked anodes, coal tar pitch, green petcoke) has not yet been located in a dated public print and will be appended only when it is. Every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 15-October official cash of \$2,999\.00, or \$1,499\.50, DOWN \$5\.50 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$903\.50, so 62\.4%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 16-October official cash of $3,014.00, or ${tl:,.2f}, UP $7.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED FRIDAY 16-OCTOBER-2026 (LME BOARD ON THE 15-OCTOBER OFFICIAL)."; NEWC="COMPILED SATURDAY 17-OCTOBER-2026 (LME BOARD ON THE FRIDAY 16-OCTOBER OFFICIAL; MARKET SHUT AT THE WEEKEND)."
n=0
for p in d['premiums']:
    p['src'],k=OLDT.subn(NEWT,p['src']); n+=k
    p['src']=p['src'].replace(OLDC,NEWC)
    if p['name'].startswith('MJP Q4'):
        p['src']+=(" SOURCE DISAGREEMENT FLAGGED 17-OCTOBER: SMM's 16-October overseas-market analysis describes Q4 MJP negotiations as slow, with the two sides 'diverging significantly' on price; this is consistent with Reuters' 07-October report that $255/t was agreed with SOME buyers while talks with others continued. The $255/t settlement is retained; no new figure was located. Source: "+S_OV)
print('premium tariff replaced',n); assert n==len(d['premiums'])
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    s=s.replace("THE RATIO: LME Alumina at $360.40/t against the 15-October aluminium three-month of $2,994.50 is 12.04%",f"THE RATIO: LME Alumina at $360.40/t against the 16-October aluminium three-month of $3,012.00 is {360.4/3012*100:.2f}%")
    a['src']=s
d['alumina'][0]['src']+=(" SPOT TRADES 16-OCTOBER (SMM): 30,000 t traded at $382/t FOB India and 30,000 t at $426/t FOB Brazil, both for November shipment - origin-specific trades cited as context only and not substituted into any row. Source: "+S_AI)

d['lme_commentary']=(f"A FRIDAY BOUNCE, BUT A WEEK OF DAMAGE. On the Friday 16-October official cash settled $3,014.00, up $15.00, and three-month $3,012.00, up $17.50 or {pm:.2f}% - back $1.50 above the 02-January three-month official, but still $49.50 beneath the 3,061.5 July low and down $58.00 on the week. "
 "The backwardation narrowed to $2.00 from $4.50 - spread and price moved in opposite directions for a second session - and visible stock slipped 250 t to a new series low of 237,875 t. The whole complex rose (nickel +1.5%, copper +0.9%) as the dollar index fell about 0.75% to near 101.8, its first weekly decline in four weeks (Trading Economics). "
 "Trading Economics continues to frame October's slide as the war premium being erased by faster Gulf restarts, Bell Bay's extension and surging Chinese alloy exports. SMM (16-October) describes ex-China physical markets as weak, with offers under pressure in Korea, Thailand and Vietnam and a stagnant US market. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND STILL IN CONTROL; FRIDAY'S BOUNCE IS NOT YET A REVERSAL. Against: three-month is down $58.00 on the week and has settled beneath 3,061.5 five times; hot US CPI/PPI keep a December Fed hike priced (about 77% per Trading Economics); Gulf restarts, Bell Bay to 2031 and Chinese alloy exports feed the supply-recovery narrative; SMM reports ex-China physical premiums and offers still under pressure; Rio Tinto's Q3 kept 2026 aluminium guidance of 3.25-3.45 Mt. "
 "Constructive: visible LME stock is at a new 21st-century low of 237,875 t, the curve stays in a small backwardation, the dollar posted its first weekly fall in four weeks, and energy costs keep climbing - Brent near $110 and European gas at about EUR 88/MWh, the highest since December 2022 - which raises the smelter cost floor ex-China.")
d['bottom_line']=("BOTTOM LINE: aluminium settled the week on the Friday 16-October LME official at cash $3,014.00 and three-month $3,012.00 - a first up-day after four declines and back to where the year started, but $49.50 beneath the 3,061.5 July low and $58.00 lower on the week. "
 "The backwardation narrowed to $2.00 and visible stock fell to another low of 237,875 t. Scenario weights are held at 10% bull / 45% base / 45% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) made a settled low of 2,994.50 inside its 2,980-3,000 target zone, above the rule-based cap near 2,977.5, and Friday's bounce is consistent with - but does not yet confirm - a wave (v) low; invalidation 3,289; the weekly corrective count towards 2,894 stays preferred.")
c=d['commercial']
c2=c.replace("FIRST, THE CURVE IS FLAT TO SLIGHTLY BACKWARDATED: a $4.50 backwardation on 15-October, flipped from a $3.50 contango, so there is no carry reward for waiting and the prompt is firming even as the flat price falls.","FIRST, THE CURVE IS FLAT: a $2.00 backwardation on 16-October, narrowed from $4.50, so there is no carry reward for waiting and no prompt squeeze either.")
c2=c2.replace("is $1,499.50 on 15-October cash, 62.4% of the $2,403/t premium",f"is ${tl:,.2f} on 16-October cash, {share:.1f}% of the $2,403/t premium")
c2=c2.replace("the 15-October official settled $67.00 beneath 3,061.5, inside the 2,980-3,000 zone and below the 02-January level;","the 16-October official bounced to $3,012.00 after a 2,994.50 settled low inside the 2,980-3,000 zone, still $49.50 beneath 3,061.5;")
c2=c2.replace("China's post-holiday inventory prints and the mid-October carbon settlements are due next week, and the Q3 producer reporting season opens mid-month.","China's September output data and the October carbon settlements are due in the coming week, and the Q3 producer season continues (Rio Tinto's operations review on 14-October kept aluminium guidance; Norsk Hydro reports later in October).")
assert c2.count('16-October')>=2, c2; d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 17-OCTOBER at 10/45/45: the Friday 16-October official bounced three-month $17.50 to $3,012.00 on a weaker dollar after a 2,994.50 settled low, but the week still closed $58.00 lower and beneath the July low; one up-day does not justify moving weight, and the 2,977.5 / 3,077 levels remain the pre-registered triggers. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium bounced on Friday to end the week back where 2026 began - three-month settled $3,012 on a weaker dollar - but it still fell $58 on the week and sits below the July low, while LME stocks hit yet another low and energy costs keep rising.",
 "points":[
 "WHAT MOVED: Friday's LME official settled cash at $3,014.00 (+$15.00) and three-month at $3,012.00 (+$17.50, +0.58%), the first up-day after four declines but $49.50 beneath the $3,061.5 July low and down $58 on the week. Cash's premium over three-month (backwardation) narrowed to $2.00 from $4.50, and LME stock fell to a new low of 237,875 t.",
 "WHY: the whole metals complex rose (nickel +1.5%, copper +0.9%) as the dollar index fell about 0.75% to near 101.8, its first weekly decline in four weeks. But physical demand ex-China remains weak: SMM reports offers falling in South Korea, Thailand and Vietnam and a stagnant US market, and the Q4 Japanese premium talks with remaining buyers are described as slow.",
 "SUPPLY AND COSTS: Rio Tinto's Q3 review (14-October) showed primary aluminium output steady at 842 kt and full-year guidance of 3.25-3.45 Mt kept, with Tomago and Bell Bay power deals signed. Meanwhile Brent rose 3.7% to near $110 and European gas reached about EUR 88/MWh, the highest since December 2022, lifting energy costs for smelters outside China.",
 "WHAT TO WATCH: whether three-month can settle back above $3,061.5-3,077 (a sign the decline has ended) or breaks below about $2,977.5; whether the backwardation extends beyond $15; China's September output data and the October carbon-input settlements next week; the 27-28 October FOMC (markets price a hold, then a December hike)."]}

d['feed']=([
 {"when":"Sat 17-Oct","impact":"Mixed","text":f"BOARD ROLLED TO THE FRIDAY 16-OCTOBER LME OFFICIAL (market shut at the weekend): cash $3,014.00 (+$15.00), three-month $3,012.00 (+$17.50, {pm:+.2f}%) - first up-day after four declines, back above the 02-January level but beneath 3,061.5 and -$58.00 on the week - backwardation narrowed to $2.00, stock down 250 t to 237,875 t."},
 {"when":"Fri 16-Oct","impact":"Bullish (cost)","text":"Brent rose 3.7% to about $109.9 and TTF gas to about EUR 87.6-88.5/MWh, the highest since December 2022, as Hormuz tanker traffic fell after Iranian strikes; EU storage about 74% (Trading Economics)."},
 {"when":"Fri 16-Oct","impact":"Bearish","text":"SMM: ex-China primary aluminium market remains weak - offers under pressure in South Korea, Thailand and Vietnam, US market stagnant, Q4 MJP talks with remaining buyers slow."},
 {"when":"Wed 14-Oct","impact":"Mixed","text":"Rio Tinto Q3-2026 operations review: primary aluminium 842 kt (-2% y/y, flat q/q), alumina 2,071 kt (+10% y/y), bauxite 15.7 Mt (-4% y/y); 2026 aluminium guidance 3.25-3.45 Mt unchanged; average Midwest duty-paid premium $2,420/t applied to ~32% of Q3 volumes (Rio Tinto 6-K)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Mixed","url":W,
  "headline":f"LME ALUMINIUM BOUNCES INTO THE WEEKEND. The Friday 16-October official settled cash at $3,014.00 ({pc:+.2f}%) and three-month at $3,012.00 ({pm:+.2f}%), back $1.50 above the 02-January three-month official but $49.50 beneath the 3,061.5 July low and $58.00 lower on the week. The backwardation narrowed to $2.00 from $4.50 and visible stock fell 250 t to a new low of 237,875 t. Every base metal rose: nickel three-month +1.52%, copper +0.86%; zinc stock rose another 7,225 t to 158,275 t."},
 {"theme":"Supply","horizon":"0-3 months","impact":"Bearish","url":S_RIO,
  "headline":"RIO TINTO Q3-2026 OPERATIONS REVIEW (Rio Tinto, 14-October): primary aluminium 842 kt (-2% y/y, flat q/q; nine months 2,518 kt, flat) with the Arvida closure offset by better performance elsewhere, including Kitimat at higher amperage, Boyne Island and the AP60 ramp-up; alumina 2,071 kt (+10% y/y); bauxite 15,745 kt (-4% y/y, +4% q/q as Weipa recovered). 2026 guidance unchanged at 3.25-3.45 Mt aluminium, 7.6-8.0 Mt alumina and 58-61 Mt bauxite. Tomago and Bell Bay power agreements were signed in Q3. The company reports an average Midwest duty-paid premium of $2,420/t applying to about 32% of Q3 volumes and LME aluminium averaging $3,226/t in the quarter."},
 {"theme":"Premiums","horizon":"0-1 month","impact":"Bearish","url":S_OV,
  "headline":"EX-CHINA PHYSICAL MARKET STAYS WEAK (SMM analysis, 16-October): offers are under pressure across major markets - South Korea's price centre is expected to keep shifting lower, Thailand's brief rebound faded, Vietnam premiums sit at the low end and the US market is stagnant with small volumes. SMM says Q4 MJP negotiations are slow with buyers and sellers diverging significantly on price; Yangshan premiums are expected to stay weak."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Bullish","url":S_TD,
  "headline":"DOLLAR POSTS FIRST WEEKLY FALL IN FOUR WEEKS (Trading Economics, 16-October): the dollar index fell about 0.75% to near 101.8, a two-week low, after an AI-spending-driven risk-off move pulled down stocks and yields. The US ten-year ended near 5.09%, down about 14bp on the week. Markets price about an 85% chance of an October Fed hold and about 77% for a 25bp December hike; Fed Chair Warsh declined at the IMF to signal whether another hike is under consideration."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish (cost)","url":S_TG,
  "headline":"EUROPEAN GAS AT ITS HIGHEST SINCE DECEMBER 2022 (Trading Economics, 16-October): TTF rose to about EUR 88/MWh, a third straight weekly gain of over 7%, with EU storage only about 74% full and Middle Eastern LNG supply about 80% below a year earlier on Hormuz disruption. Brent rose 3.7% to about $109.9, up more than 5% on the week, as tanker traffic through Hormuz fell after Iranian strikes and Ukrainian drones hit Russian refineries."},
 {"theme":"Alumina","horizon":"0-1 month","impact":"Mixed","url":S_AI,
  "headline":"ALUMINA SPOT TRADES (SMM, 16-October): 30,000 t traded at $382/t FOB India and 30,000 t at $426/t FOB Brazil, both for November shipment - a wide $44/t origin spread, against SMM's $373/t FOB Western Australia reference cited in its 15-October weekly review."},
]+d['news'][:14]
d['news']=d['news'][:20]

# Rio Tinto earnings row: H1 earnings carried; add Q3 operations note (production, not earnings)
for e in d['earnings']:
    if e['company']=='Rio Tinto (RIO)':
        e['readthrough']=("UPDATE 17-OCTOBER (Q3-2026 operations review, 14-October, production only - no new earnings figures): primary aluminium 842 kt (-2% y/y), alumina 2,071 kt (+10% y/y), 2026 aluminium guidance 3.25-3.45 Mt unchanged; average Midwest duty-paid premium $2,420/t on about 32% of Q3 volumes. The H1-2026 earnings figures in this row are unchanged. ")+e['readthrough']
cats=d['outlook']['catalysts']
for cat in cats:
    if cat['date']=='Daily, from Fri 16-Oct':
        cat['date']='Daily, from Mon 19-Oct'
        cat['event']="3,061.5 BROKEN ON FIVE SETTLED OFFICIALS; THREE-MONTH MADE A SETTLED LOW OF 2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE AND $17.00 ABOVE THE RULE-BASED CAP, THEN BOUNCED TO 3,012.00 ON 16-OCTOBER. A settled close beneath about 2,977.5 would break the cap on daily wave (v) and force a re-count (extended fifth or larger correction toward the 2,894 weekly 61.8%); a settled recovery above 3,077 would signal wave (v) is complete; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289."
cats.insert(1,{"date":"Mon 19 - Tue 20-Oct","impact":"Medium","event":"CHINA SEPTEMBER ACTIVITY DATA: the National Bureau of Statistics' monthly industrial output release includes primary aluminium and alumina production - the test of whether Chinese smelters are running further through the 45 Mt policy ceiling. Exact date to be confirmed on the NBS calendar."})
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 17-OCTOBER: the backwardation narrowed to $2.00 on 16-October from $4.50 as three-month rose $17.50 - the curve is essentially flat. Trend held at FLAT."
RK[1]['risk']+=" UPDATE 17-OCTOBER: the dollar index fell about 0.75% on 16-October, its first weekly fall in four weeks; markets price about an 85% October hold and about 77% for a December hike (Trading Economics). Trend held at UP."
RK[4]['risk']+=" UPDATE 17-OCTOBER: LME stock fell 250 t to a new series low of 237,875 t on 16-October. Trend held at FLAT."
for r in RK:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 17-OCTOBER: Trading Economics (16-October) reports tanker traffic through the strait fell sharply after Iranian strikes, lifting Brent 3.7% to near $110 and TTF to its highest since December 2022 on Middle East LNG about 80% below a year earlier. Trend held at UP."
d['outlook']['ai_analysis'].insert(0,"WEEKEND REVIEW, 17-OCTOBER: aluminium ended the week with a Friday bounce - three-month +$17.50 to $3,012.00 on the 16-October official as the dollar index fell about 0.75% - but the week still closed $58.00 lower and beneath the 3,061.5 July low for a fifth session. The physical signals are split: visible LME stock set another low (237,875 t) and the curve stays in a small backwardation, while SMM reports ex-China offers and premiums still under pressure and slow Q4 MJP talks with remaining Japanese buyers. Rio Tinto's Q3 review kept aluminium guidance; energy costs rose again (Brent near $110, TTF about EUR 88/MWh). Weights held at 10/45/45; the next technical signals are a settled close above 3,077 (wave (v) complete) or below about 2,977.5 (re-count).")

EWS=("REVIEWED 17-OCTOBER ON THE FRIDAY 16-OCTOBER OFFICIAL: three-month bounced $17.50 to $3,012.00 after a settled low of 2,994.50 on 15-October - inside the 2,980-3,000 target zone and $17.00 above the rule-based cap near 2,977.5, so wave (v) of C ($154.00 from the 3,148.5 wave (iv) high) remains shorter than (iii)'s $171 and the impulse rules hold. The count is unchanged; the bounce is consistent with a wave (v) low at 2,994.50 but that low is NOT yet confirmed and is not locked as a pivot. Base case about 65%: (v) has ended or ends in 2,977.5-3,000 and a corrective rebound toward 3,061.5-3,077 follows (a settled close above 3,077 would confirm); alternate about 35%: a settled close beneath 2,977.5 forces a re-count toward the 2,894 weekly 61.8% level. Invalidation of the bearish count unchanged at 3,289; confidence moderate. ")
EWL=("REVIEWED 17-OCTOBER ON THE FRIDAY 16-OCTOBER OFFICIAL (WEEKLY CLOSE): three-month settled the week at $3,012.00, down $58.00 from 3,070, a fifth close beneath the 3,061.5 July low and in the lower half of the 2,950-3,110 zone; the weekly decline from 3,855 extends and the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label is needed. ")
d['ew']['short_term']['writeup']=EWS+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=EWL+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="109.86",day="+$3.94 (+3.72%) on 16-October, more than +5% on the week (Trading Economics; text section shows $109.69, +3.56%)",
 note="REFRESHED SATURDAY 17-OCTOBER-2026 (Trading Economics): Brent rose toward $110 as tanker traffic through Hormuz fell sharply after Iranian strikes on vessels and Ukrainian drones hit Russian refineries; the IEA's pledged 100m-barrel release partly offsets. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="87.6",day="about EUR 87.55/MWh on 16-October, +1.28% (Trading Economics; stats section shows EUR 88.46, +2.34%)",
 note="REFRESHED SATURDAY 17-OCTOBER-2026 (Trading Economics): highest since December 2022, a third straight weekly gain of over 7%; EU storage about 74.1% full, far below seasonal norms; Middle Eastern LNG supply about 80% below a year earlier. Value approximate. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.8",day="about 101.78 on 16-October, -0.75%; first weekly decline (about -0.4%) after three weeks of gains (Trading Economics)",
 note="REFRESHED SATURDAY 17-OCTOBER-2026 (Trading Economics): the dollar fell to a two-week low as an AI-spending risk-off move pulled down stocks and yields; markets price about 85% for an October hold and about 77% for a December hike. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="5.09",day="about 5.09% on 16-October, +0.01pp; down about 14bp on the week (Trading Economics; summary text cites 5.12% intraday)",
 note="REFRESHED SATURDAY 17-OCTOBER-2026 (Trading Economics): yields steadied after an 11bp drop on 15-October; Fed Chair Warsh declined at the IMF to signal another hike; fed funds 4.00%. Higher yields raise the cost of carrying metal. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.12570',day="LME fixing on 16-October, +0.44% from 1.12080; ECB fixing 1.12530, BFIX 1.12561",
 note="REFRESHED SATURDAY 17-OCTOBER-2026 to the 16-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 16-OCTOBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND BECAUSE THE MARKET IS SHUT (no ring Saturday or Sunday); the next official prints Monday 19-October at 13:20 London. Reference and intraday prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN: the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 16-October session, and the per-metal aluminium daily table shows NO row after 16-October, so the board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.12080, ECB 1.12080, BFIX 1.12077) matches the 15-October board verified on 16-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 15-October: aluminium -250 to 237,875; copper -1,175 to 225,425; nickel -2,076 to 279,990; zinc +7,225 to 158,275; lead -525 to 339,275.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (16-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (twelve sessions, 01- to 16-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,012.00; the stock chart axis floor (225,000 t) brackets visible stock at 237,875 t - both re-checked this run; the stock floor has about 12,900 t of headroom and will be re-bracketed before it is approached.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,014.00 against three-month $3,012.00 is therefore a $2.00 BACKWARDATION, narrowed from $4.50 on 15-October - spread and price moved in OPPOSITE directions this session."
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; Rio Tinto's 14-October review reports an average realised US-destination tariff cost of $1,685/t in Q3, consistent with a 50% rate on its mix), the tariff leg is 0.50 times the 16-October official cash of $3,014.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $109.86), the dollar index (about 101.8), TTF (about EUR 87.6/MWh) and the US ten-year (about 5.09%) are 16-October closes as shown by Trading Economics on 17-October - the source's own sections differ slightly, so they are approximate; EUR/USD is the 16-October LME fixing, the same session as the board."
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: NO NEW EARNINGS WERE REPORTED BY TRACKED PEERS SINCE ALCOA (15-October). RIO TINTO'S ROW CARRIES A NOTE FROM ITS 14-OCTOBER Q3 OPERATIONS REVIEW (production only; this was missed by the 15-16 October runs and is added now); NO NEW COMPANY WAS BACK-FILLED THIS RUN. Other entries are carried at their last publicly verified figures, and gaps stay gaps."
C.append("FETCH NOTE 17-OCTOBER: AL Circle and Mining.com news pages returned HTTP 403 to this run and two SMM item links returned 404 on one URL pattern; the SMM items cited were read on the news.metal.com pattern instead. No figure on this page depends on an unread source.")

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 16-OCTOBER: no newer public disclosure","REVIEWED 17-OCTOBER: no newer public disclosure").replace("REVIEWED 16-OCTOBER. NO NEW DATED","REVIEWED 17-OCTOBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('Rio Tinto'):
        hit+=1
        p['update']=("UPDATED 17-OCTOBER FROM RIO TINTO'S Q3-2026 OPERATIONS REVIEW (14-October): Bell Bay produced 48 kt (100%) in Q3 and Tomago 76 kt (Rio share); power agreements for both were signed in Q3 and Pacific smelter repowering arrangements are 'now well progressed'. Group primary aluminium 842 kt (-2% y/y), with the final Arvida potlines closed in June 2026 as planned and AP60 ramping up; 2026 aluminium guidance 3.25-3.45 Mt unchanged. ")+p['update']
        p['src']=[L_RIO,S_RIO]
assert hit==1

for s in [[L_TE,S_TE],[L_RIO,S_RIO],[L_OV,S_OV],[L_AI,S_AI],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG]]:
    d['sources'].append(s)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 16-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 15-Oct; no later row)",W])
d['outlook']['sources'].append([L_RIO,S_RIO]); d['outlook']['sources'].append([L_OV,S_OV])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-15'
ph['rows'][-1]=['2026-10-16',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
