# Daily data refresh - 2026-10-16 (FRIDAY, compiled ~03:40 London). Board ROLLED to THURSDAY 15-Oct LME official.
# Westmetall cache-busted EN AND DE overviews BOTH fetched this run and agree on the full 15-Oct session (all six metals, stocks, FX).
# Completeness: 5/5 stock-change lines reconcile vs the verified 14-Oct board; prior-day FX column (MTLE 1.11930) matches 14-Oct board.
# Trading Economics aluminium / Brent / TTF / DXY / 10Y pages fetched; Alcoa Q3 press release fetched; SMM briefs fetched.
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-16'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (15/16-Oct-2026)"
S_AA="https://news.alcoa.com/press-releases/press-release-details/2026/Alcoa-Corporation-Reports-Third-Quarter-2026-Results/default.aspx"; L_AA="Alcoa - Alcoa Corporation Reports Third Quarter 2026 Results (15-Oct-2026)"
S_AAI="https://uk.investing.com/news/stock-market-news/earnings-call-transcript-alcoa-tops-q3-2026-eps-forecast-as-revenue-misses-93CH-4913266"; L_AAI="Investing.com - Alcoa tops Q3 2026 EPS forecast as revenue misses (15-Oct-2026)"
S_SF="https://news.metal.com/newscontent/104159774-shfe-aluminum-falls-on-higher-volume-alumina-continues-to-decline-us-dollar-rate-hike-expectations-pressure-aluminum-industry-chain-smm-aluminum-futures-brief"; L_SF="SMM - SHFE aluminum falls on higher volume, alumina continues to decline [SMM aluminum futures brief] (15-Oct-2026)"
S_SA="https://news.metal.com/newscontent/104159741-supply-demand-surplus-pattern-unchanged-spot-prices-fall-under-pressure-price-spread-between-chinese-and-overseas-markets-continues-to-widen-smm-alumina-weekly-review"; L_SA="SMM - Alumina weekly review: surplus unchanged, spot prices fall (15-Oct-2026)"
S_SO="https://news.metal.com/newscontent/104160284-dollar-falls-gold-and-silver-rise-together-metals-broadly-decline-lme-copper-lme-zinc-and-lme-nickel-lead-losses-shfe-tin-rebounds-overnight-market"; L_SO="SMM - Dollar falls, metals broadly decline; LME copper, zinc and nickel lead losses [Overnight market] (16-Oct-2026)"
S_S32="https://aluminiumtoday.com/news/south32-shareholders-approve-alcoa-aluminium-deal"; L_S32="Aluminium Today - South32 shareholders approve Alcoa aluminium deal (15-Oct-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent crude oil (16-Oct-2026)"
S_TY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TY="Trading Economics - US 10-year Treasury yield (15/16-Oct-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - US dollar index (16-Oct-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - EU natural gas TTF (16-Oct-2026)"

B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
cash,prev_c,m3,prev_m,stk,prev_s=2999.0,3010.0,2994.5,3013.5,238125,238375
spr=cash-m3; pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100
assert spr==4.5

VER=("COMPILED FRIDAY 16-OCTOBER-2026. THE BOARD IS THE THURSDAY 15-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION (Friday's official prints at 13:20 London). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 15-October official for all six metals with stocks and FX fixings (EUR/USD MTLE 1.12080); their prior-day FX column (MTLE 1.11930) matches the verified 14-October board; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 14-October: aluminium 238,375 less 250 to 238,125; copper 228,000 less 1,400 to 226,600; nickel 282,654 less 588 to 282,066; zinc 144,125 plus 6,925 to 151,050; lead 340,075 less 275 to 339,800. "
 "The whole board sits on ONE UNIFORM SESSION (15-October); prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(f" CASH SETTLED $2,999.00 ON THE 15-OCTOBER OFFICIAL, DOWN $11.00 OR {pc:.2f}% FROM $3,010.00. THREE-MONTH SETTLED $2,994.50, DOWN $19.00 OR {pm:.2f}% FROM $3,013.50 - a FOURTH settled close beneath the 3,061.5 July low, now by $67.00, and $16.00 BELOW the first-published 2026 three-month official of $3,010.50, so aluminium is now NEGATIVE for the year on the official series. "
 "THE CURVE FLIPPED BACK TO BACKWARDATION: cash $4.50 ABOVE three-month, from a $3.50 contango - SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS this session (price down, prompt firmer). "
 "VISIBLE LME STOCK FELL 250 t TO 238,125 t, another new series low. Base metals sold off broadly on the day as hot US inflation data kept Fed-hike bets alive and a tech-led risk-off move spread (SMM; Trading Economics).")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"2,999.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"2,994.5","pos":False,"delta":VER+AL+" THREE-MONTH IS $67.00 BENEATH THE 3,061.5 JULY LOW, $82.50 beneath the 3,077 weekly 50% retracement and $294.50 below the 3,289 daily invalidation. The rule-based cap on daily wave (v) near 2,977.5 HOLDS on a settled basis ($17.00 above it)."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+4.5","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $2,999.00 against three-month $2,994.50 is a $4.50 BACKWARDATION, flipped from a $3.50 contango - an $8.00 swing toward the prompt. Spread and flat price moved in OPPOSITE directions this session (price down, prompt firmer relative to the forward). The reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is still UNMET; the bearish structural confirmation, a contango beyond $24.50, is also unmet. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"238,125","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 250 t TO 238,125 t, another new series low - the lowest registered level of the 21st century per Crux Investor's 14-October analysis of LME data. September's mean stock was {sep_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $2,994.50, DOWN $19.00 OR {pm:.2f}% FROM $3,013.50 - $67.00 beneath the 3,061.5 July low, a fourth settled close below it, and $16.00 BELOW the 02-January three-month official (year-to-date now {(m3/3010.5-1)*100:.2f}%). AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DOWN 250 t TO 238,125 t, another new series low. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-3.5,"avg":sep_sp,"note":VER+f" A $4.50 BACKWARDATION, FLIPPED FROM A $3.50 CONTANGO. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in OPPOSITE directions this session (three-month down $19.00, prompt firmer by $8.00). REVERSAL CONDITION, RESTATED UNCHANGED: a BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1208,"prev":1.1193,"avg":1.1465,"note":VER+" THE LME EURO FIXING FIRMED TO 1.12080 FROM 1.11930 at the Thursday ring; the ECB fixing printed 1.12080 and BFIX 1.12077. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (15-Oct official)","price":"2,999.0","basis":f"THE 15-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $2,999.00, DOWN $11.00 OR {pc:.2f}%. Next official Friday 16-October 13:20 London."},
 {"tenor":"3-month (15-Oct official)","price":"2,994.5","basis":f"THE 15-OCTOBER-2026 OFFICIAL THREE-MONTH OF $2,994.50, DOWN $19.00 OR {pm:.2f}% - $67.00 beneath the 3,061.5 July low (fourth settled close below it), $16.00 below the 02-January official."},
 {"tenor":"Cash-to-3M structure","price":"+4.5 (BACKWARDATION)","basis":"A $4.50 BACKWARDATION, flipped from a $3.50 contango. Flat price and spread moved in OPPOSITE directions."},
 {"tenor":"Visible LME stock","price":"238,125 t","basis":f"DOWN 250 t to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE PROMPT FIRMED EVEN AS THE FLAT PRICE FELL. On the 15-October official cash $2,999.00 sits $4.50 ABOVE three-month $2,994.50, a BACKWARDATION, flipped from a $3.50 contango. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50, $5.00, $1.00 and $3.50, and now a $4.50 backwardation. "
 f"READ: spread and price moved in OPPOSITE directions - the forward led the fall while the prompt held, with visible stock at a new series low of 238,125 t. The slide is a macro (US inflation, Fed-hike pricing, risk-off) and supply-recovery repricing, not a prompt glut. The September mean spread was ${sep_sp:,.2f}. The reversal condition (a backwardation beyond $15.00) is unmet; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]

ls=d['lme_series']; assert ls[-1][0]=='14-Oct', ls[-1]
d['lme_series']=ls[1:]+[["15-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14539.0,14362.0,14751.0,14635.0); NI=(14885.0,15125.0,15475.0,15680.0); ZN=(3724.0,3681.5,3803.0,3749.0); PB=(1853.0,1889.0,1866.0,1906.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+ZN[0])/11)/(sum(zs)/10),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+PB[0])/11)/(sum(ps)/10),1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])): R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-15'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending THURSDAY 15-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 24-September dropped and 15-October appended, so the window is 25-September to 15-October. Every point is an official cash settlement; the 15-October points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 14-October. Next official Friday 16-October.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (15-October-2026 session; stock lines reconciled against 14-October)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,539.00, down $212.00 or 1.44%; three-month $14,362.00, down $273.00 or 1.87%. Backwardation WIDENED to $177.00 from $116.00 as the forward fell faster than the prompt; stock DREW 1,400 tonnes to 226,600 - an eighth straight draw. Bloomberg and Quartz reported copper heading for a third daily loss as the strong US inflation data lifted the dollar and spurred a risk-off selloff (15-October)."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $14,885.00, down $590.00 or 3.81%; three-month $15,125.00, down $555.00 or 3.54% - the steepest fall on the board. CONTANGO widened to $240.00 from $205.00, still the widest carry on the board. Stock fell 588 tonnes to 282,066."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,724.00, down $79.00 or 2.08%; three-month $3,681.50, down $67.50 or 1.80%. BACKWARDATION NARROWED to $42.50 from $54.00 as another 6,925 tonnes were delivered in, lifting stock to 151,050 t - a fourth straight large inflow. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,853.00, down $13.00 or 0.70%; three-month $1,889.00, down $17.00 or 0.89%. CONTANGO narrowed to $36.00 from $40.00. Stock drew 275 tonnes to 339,800, a nineteenth consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Thursday 15-October official every base metal fell - nickel three-month 3.54%, copper 1.87%, zinc 1.80%, lead 0.89% and aluminium 0.63% to $2,994.50, now below its 02-January level. SMM's overnight report (16-October) shows LME copper, zinc and nickel leading further losses while the dollar index eased 0.55% to 101.97. The LME euro fixing firmed to 1.1208.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='14-Oct'
        i['hist']=i['hist'][1:]+[["15-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,362.00 (3M); 14,539.00 (cash) $/t"
        i['ratio']="~14,539.00 $/t cash vs LME 3M 14,362.00 $/t"
        i['trend']='down'
        i['src']=("LME official cash settlement, rolled to the THURSDAY 15-OCTOBER-2026 session at $14,539.00, DOWN $212.00 or 1.44% against $14,751.00. THE WINDOW ROLLED THIS RUN: 24-September dropped and 15-October appended, so the series is the last fifteen published official cash sessions, 25-September to 15-October - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 14-October). "
                  "Copper structure for context: backwardation $177.00 (from $116.00), stock drew 1,400 t to 226,600 t.")
d['inputs_summary']=("UPDATE 16-OCTOBER: copper rolled to the Thursday 15-October LME official cash of $14,539.00, down $212.00, with its fifteen-session window moved to 25-September to 15-October. No new SMM fluoride, silicon or magnesium weekly mark was located on the panel's sources this run; the carbon settlement cycle (prebaked anodes, coal tar pitch, green petcoke) is due around 17-18 October and will be appended only when a dated public print is located. Every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 14-October official cash of \$3,010\.00, or \$1,505\.00, DOWN \$13\.00 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$898\.00, so 62\.6%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 15-October official cash of $2,999.00, or ${tl:,.2f}, DOWN $5.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED THURSDAY 15-OCTOBER-2026 (LME BOARD ON THE 14-OCTOBER OFFICIAL)."; NEWC="COMPILED FRIDAY 16-OCTOBER-2026 (LME BOARD ON THE 15-OCTOBER OFFICIAL)."
n=0
for p in d['premiums']:
    p['src'],k=OLDT.subn(NEWT,p['src']); n+=k
    p['src']=p['src'].replace(OLDC,NEWC)
print('premium tariff replaced',n); assert n==len(d['premiums'])
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    s=s.replace("THE RATIO: LME Alumina at $360.40/t against the 14-October aluminium three-month of $3,013.50 is 11.96%",f"THE RATIO: LME Alumina at $360.40/t against the 15-October aluminium three-month of $2,994.50 is {360.4/2994.5*100:.2f}%")
    s=s.replace("the SMM alumina index is carried at its 30-September print of 2,669.99 yuan/tonne.","the SMM alumina index is UPDATED THIS RUN to its 15-October weekly print of 2,661.08 yuan/tonne, down 7.59 yuan week on week (SMM alumina weekly review, 15-October: total alumina inventory up 47,500 t to 7.48 Mt, refinery operating rate 77.84%, surplus expected to persist; SMM's FOB Western Australia reference was $373/t - a different basis from the East Australia trade row, so it is cited here as context and not substituted).")
    a['src']=s
    if a['name'].startswith('SMM Alumina Index'):
        a['val']=2661.08; a['asof']='15-Oct-26'; a['trend']='down'

d['lme_commentary']=(f"ALUMINIUM SLIPPED BELOW WHERE 2026 STARTED. On the Thursday 15-October official cash settled $2,999.00, down $11.00, and three-month $2,994.50, down $19.00 or {abs(pm):.2f}% - $67.00 beneath the 3,061.5 July low and $16.00 below the 02-January three-month official, so the official series is now negative for the year. "
 "Yet the curve flipped to a $4.50 BACKWARDATION from a $3.50 contango - spread and price moved in opposite directions - and visible stock slipped 250 t to a new series low of 238,125 t. The whole complex fell (nickel -3.5%, copper -1.9%, zinc -1.8%) as hot US inflation data kept Fed-hike pricing alive and a tech-led risk-off move spread (Bloomberg; SMM). "
 "Trading Economics continues to frame the move as the war premium being erased by faster Gulf restarts, Bell Bay's extension and surging Chinese alloy exports. SHFE aluminium 2611 fell 1.31% to RMB 23,040 with a 5/10-day 'death cross', and SMM alumina 2701 fell 1.94% to RMB 2,584 on a growing alumina surplus. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND IN CONTROL, BUT THE PROMPT IS PUSHING BACK. Against: three-month settled $2,994.50, a fourth close beneath 3,061.5 and now below the 02-January level; US September CPI (3.7%) and a hot PPI keep a December Fed hike priced; Gulf restarts, Bell Bay to 2031 and Chinese alloy/semis exports feed the supply-recovery narrative; Alcoa's Q3 shows a realised aluminium price down about 5% quarter on quarter; SHFE and alumina are weak. "
 "Constructive: the curve flipped back to a $4.50 backwardation while the flat price fell, visible LME stock is at a new 21st-century low of 238,125 t, the dollar eased from its 18-month high and the US ten-year fell about 13bp on 15-October; Hormuz attacks continue and European gas holds near EUR 85/MWh, keeping smelter energy and freight costs high.")
d['bottom_line']=("BOTTOM LINE: aluminium settled on the Thursday 15-October LME official at cash $2,999.00 and three-month $2,994.50 - a fourth settled close beneath the 3,061.5 July low (now by $67.00) and $16.00 below the level the year started. "
 "The curve flipped to a $4.50 backwardation and visible stock fell to a new low of 238,125 t, so the prompt is tightening as the forward falls. Scenario weights are held at 10% bull / 45% base / 45% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) is inside its 2,980-3,000 target zone on a settled basis with the rule-based cap near 2,977.5 intact and invalidation at 3,289; the weekly corrective count towards 2,894 stays preferred.")
c=d['commercial']
c=c.replace("FIRST, THE CURVE IS NEAR FLAT: a $3.50 contango on 14-October, widened from $1.00, so there is little carry reward for waiting.","FIRST, THE CURVE IS FLAT TO SLIGHTLY BACKWARDATED: a $4.50 backwardation on 15-October, flipped from a $3.50 contango, so there is no carry reward for waiting and the prompt is firming even as the flat price falls.")
c=c.replace("is $1,505.00 on 14-October cash, 62.6% of the $2,403/t premium",f"is ${tl:,.2f} on 15-October cash, {share:.1f}% of the $2,403/t premium")
c=c.replace("the 14-October official settled $48.00 beneath 3,061.5 and intraday trade reached about 2,978, inside the 2,980-3,000 zone; the hot US CPI has put an October Fed hike in play; Alcoa's results on 15-October;","the 15-October official settled $67.00 beneath 3,061.5, inside the 2,980-3,000 zone and below the 02-January level; Fed-hike pricing has shifted toward December; Alcoa's Q3 (15-October) showed a realised aluminium price of $4,527/t, down from $4,752/t;")
assert c!=d['commercial'] and '2,999.00 on 15' not in c; d['commercial']=c

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 16-OCTOBER at 10/45/45: the 15-October official took three-month to $2,994.50, $67.00 beneath the July low and below the 02-January level, in a broad base-metals selloff; but the curve flipped back to a $4.50 backwardation and visible stock set another low, so the evidence does not justify shifting weight further toward the bear path before the 2,977.5 technical level is tested on a settled basis. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium is now below where 2026 began - three-month settled $2,994.50 on Thursday in a broad metals selloff driven by US inflation and Fed-hike bets - but the curve flipped back to backwardation and LME stocks hit another low, so the physical market is tightening even as the forward price falls.",
 "points":[
 "WHAT MOVED: Thursday's LME official settled cash at $2,999.00 (-$11.00) and three-month at $2,994.50 (-$19.00, -0.63%), $67 beneath the $3,061.5 July low and $16 below the 02-January level. Cash moved to a $4.50 premium over three-month (backwardation) from a $3.50 discount - price and spread moved in opposite directions - and LME stock fell to a new low of 238,125 t.",
 "WHY: the whole metals complex fell (nickel -3.5%, copper -1.9%, zinc -1.8%) as hot US inflation (CPI 3.7%, PPI +1.3% m/m) kept Fed-hike bets alive and a tech-led risk-off move spread. Commentary continues to cite faster Gulf restarts, Bell Bay secured to 2031 and surging Chinese alloy exports; in China, SHFE aluminium fell 1.3% and alumina 1.9% on a growing alumina surplus.",
 "PRODUCERS: Alcoa's Q3 beat on earnings (adjusted EPS $1.82 vs about $1.54 expected) on higher alumina output and prices, but its realised aluminium price fell to $4,527/t from $4,752/t and revenue slipped 7%; South32 shareholders approved the sale of its aluminium chain to Alcoa.",
 "WHAT TO WATCH: whether three-month settles beneath about $2,977.5, which would force a re-count of the daily wave structure; whether the backwardation extends beyond $15 (a reversal signal); the mid-October carbon settlements around 17-18 October; Fed Chair remarks before the blackout and the 27-28 October FOMC."]}

d['feed']=([
 {"when":"Fri 16-Oct","impact":"Bearish","text":f"BOARD ROLLED TO THE THURSDAY 15-OCTOBER LME OFFICIAL: cash $2,999.00 (-$11.00), three-month $2,994.50 (-$19.00, {pm:.2f}%) - a fourth settled close beneath the 3,061.5 July low and below the 02-January level - curve FLIPPED to a $4.50 backwardation from a $3.50 contango, stock down 250 t to 238,125 t."},
 {"when":"Thu 15-Oct","impact":"Mixed","text":"Alcoa Q3-2026: revenue $3.70bn (-7% q/q), adjusted EPS $1.82 (beat), adjusted EBITDA ex-special items $789m; realised aluminium $4,527/t (from $4,752/t), alumina $353/t (from $334/t); FY2026 production guidance reaffirmed (Alcoa)."},
 {"when":"Thu 15-Oct","impact":"Bearish","text":"Base metals broadly lower: copper heads for a third daily loss as US inflation lifts the dollar and a tech-led risk-off move spreads (Bloomberg); SHFE aluminium -1.31% to RMB 23,040, alumina -1.94% (SMM)."},
 {"when":"Thu 15-Oct","impact":"Mixed","text":"South32 shareholders approve the sale of its aluminium value chain (Worsley, Hillside, Brazil interests, MRN stake) to Alcoa; completion guided H1-2027 subject to approvals (Aluminium Today)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Mixed","url":W,
  "headline":f"LME ALUMINIUM NOW NEGATIVE FOR 2026 - BUT THE PROMPT FIRMS. The Thursday 15-October official settled cash at $2,999.00 ({pc:.2f}%) and three-month at $2,994.50 ({pm:.2f}%), $67.00 beneath the 3,061.5 July low and $16.00 below the 02-January three-month official. The curve flipped to a $4.50 backwardation from a $3.50 contango and visible stock fell 250 t to a new low of 238,125 t. Nickel three-month fell 3.54% and copper 1.87%; zinc stock rose another 6,925 t to 151,050 t."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Mixed","url":S_AA,
  "headline":"ALCOA Q3-2026 (Alcoa, 15-October): revenue $3.704bn against $3.966bn in Q2; net income attributable $483m ($1.81/share) and adjusted EPS $1.82 against $2.12 in Q2 - above the roughly $1.54 consensus cited by Investing.com, while revenue missed. Adjusted EBITDA excluding special items $789m (Q2 $901m). Alumina production rose 11% to 2.467 Mt on Pinjarra stability and aluminium production 2% to 649 kt with the Alumar restart complete; realised aluminium fell to $4,527/t from $4,752/t while third-party alumina rose to $353/t from $334/t. Full-year production guidance was reaffirmed; Q4 aluminium segment EBITDA faces about $30m from higher raw-material costs and maintenance."},
 {"theme":"Market","horizon":"Immediate","impact":"Bearish","url":S_SO,
  "headline":"METALS BROADLY LOWER ON INFLATION AND RISK-OFF (SMM overnight, 16-October; Bloomberg, 15-October): LME copper, zinc and nickel led losses overnight while aluminium held flat near $2,987.50; the dollar index eased 0.55% to 101.97 from its 18-month high. Bloomberg reported copper heading for a third daily fall as strong US inflation spurred a selloff, with technology stocks bearing the brunt of the risk-off tone."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Mixed","url":S_TY,
  "headline":"YIELDS RETREAT AFTER THE CPI SPIKE (Trading Economics, 15/16-October): the US ten-year fell nearly 13bp to about 5.05% on 15-October as an equity and tech selloff driven by doubts over AI spending pushed investors into Treasuries, after touching about 5.3% on the hot CPI. September PPI rose 1.3% m/m against 0.5% expected and retail sales rose 0.8%. Markets now expect the Fed to hold at its 27-28 October meeting and price a 25bp hike in December."},
 {"theme":"China","horizon":"0-1 month","impact":"Bearish","url":S_SF,
  "headline":"SHFE ALUMINIUM FORMS A 'DEATH CROSS' (SMM, 15-October): SHFE aluminium 2611 closed down 305 yuan or 1.31% at RMB 23,040/t on higher volume, below all four major moving averages, with the 5-day line crossing beneath the 10-day; alumina 2701 fell 1.94% to RMB 2,584/t. SMM expects aluminium to stay weak short term under Fed-hike expectations, although billet stocks fell 19,000 t week on week to 168,000 t."},
 {"theme":"Alumina","horizon":"0-3 months","impact":"Bearish","url":S_SA,
  "headline":"ALUMINA SURPLUS PERSISTS (SMM weekly review, 15-October): the SMM alumina index fell 7.59 yuan to 2,661.08 yuan/t; total alumina inventory rose 47,500 t to 7.48 Mt with refinery finished-product stock up 26,000 t; the national operating rate edged up to 77.84%. FOB Western Australia was $373/t, implying an import price about 523 yuan/t above the domestic index. No cuts or maintenance are reported and SMM expects spot prices to keep falling."},
 {"theme":"Corporate","horizon":"3-12 months","impact":"Mixed","url":S_S32,
  "headline":"SOUTH32 HOLDERS APPROVE ALUMINIUM SALE TO ALCOA (Aluminium Today, 15-October): shareholders voted at the AGM to dispose of South32's aluminium value chain - Worsley Alumina (86%), Hillside Aluminium (100%), the Brazil Alumina (36%) and Brazil Aluminium (40%) interests and a 33% MRN bauxite stake subject to pre-emptive rights - for up to $5.6bn; completion is guided for H1-2027 subject to regulatory approvals."},
]+d['news'][:13]
d['news']=d['news'][:20]

E=None
for e in d['earnings']:
    if e['company']=='Alcoa (AA)': E=e
assert E
E.update(period="Q3 2026",reported="15 Oct 2026",reported_iso="2026-10-15",eps=1.82,revenue_bn=3.70,yoy_pct=None,sentiment="Mixed",
 headline="Q3-2026: revenue $3.704bn (-7% q/q from $3.966bn); net income attributable $483m, $1.81/share; ADJUSTED EPS $1.82 against $2.12 in Q2 - a BEAT against the ~$1.54 consensus cited by Investing.com while revenue missed (~$3.78bn expected). Adjusted EBITDA excluding special items $789m (Q2 $901m). Alumina production +11% to 2.467 Mt (Pinjarra stability); aluminium production +2% to 649 kt (Alumar restart complete); total aluminium shipments -5% to 693 kt. Realised aluminium $4,527/t (Q2 $4,752/t); third-party alumina $353/t (Q2 $334/t). FY2026 production and shipment guidance reaffirmed.",
 readthrough="THE FIRST Q3 PRODUCER PRINT SHOWS THE PEAK IS BEHIND THE AVERAGE REALISED PRICE: a ~5% q/q fall in realised aluminium and a 7% revenue drop, offset by better costs and a higher alumina price. Q4 guidance flags about $30m of higher raw-material costs and maintenance in the aluminium segment and about $30m higher alumina costs - consistent with an industry where the metal price is easing faster than input costs. The South32 aluminium chain acquisition (shareholder-approved 15-October) is guided to close in H1-2027. Generic public read-through, not advice.",
 url=S_AA)
eh=d['earnings_history']['AA']; assert eh['points'][-1][0]=='Q2-26'
eh['points']=eh['points'][1:]+[["Q3-26",1.82]]
eh['src']=["Alcoa quarterly results (adj EPS: Q4-25 $1.26, Q1-26 $1.40, Q2-26 $2.12, Q3-26 $1.82 per the 15-Oct-2026 release)",S_AA]
d['earnings_note']=("ALCOA OPENED THE Q3-2026 PRODUCER SEASON ON 15-OCTOBER (refreshed this run): adjusted EPS $1.82 beat the ~$1.54 consensus on better costs and higher alumina output and prices, while revenue fell 7% q/q as the realised aluminium price eased to $4,527/t. Alcoa's per-company history was rolled to Q3-26 (Q3-25 dropped). NO NEW COMPANY WAS BACK-FILLED INTO THE PER-COMPANY HISTORY THIS RUN; gaps stay gaps. Next in the season: Norsk Hydro and Rio Tinto later in October. "+d['earnings_note'])

cats=d['outlook']['catalysts']
for cat in cats:
    if cat['date']=='Daily, from Thu 15-Oct':
        cat['date']='Daily, from Fri 16-Oct'
        cat['event']="3,061.5 BROKEN ON FOUR SETTLED OFFICIALS (NOW BY $67.00); THREE-MONTH SETTLED $2,994.50 ON 15-OCTOBER, INSIDE THE 2,980-3,000 TARGET ZONE AND $17.00 ABOVE THE RULE-BASED CAP. A settled close beneath about 2,977.5 would break the cap on daily wave (v) and force a re-count (extended fifth or larger correction toward the 2,894 weekly 61.8%); a settled recovery above 3,077 would signal wave (v) is complete; above 3,148.5 the C wave would be complete and above 3,183 the impulsive labelling void. Invalidation 3,289."
    elif cat['date']=='Thu 15-Oct (after NYSE close)':
        cat['date']='Resolved Thu 15-Oct'
        cat['event']="ALCOA Q3-2026 - RESOLVED MIXED: adjusted EPS $1.82 beat (~$1.54 expected) while revenue of $3.70bn missed; realised aluminium fell to $4,527/t from $4,752/t, third-party alumina rose to $353/t; FY2026 production guidance reaffirmed (Alcoa, Investing.com)."
cats.insert(0,{"date":"Tue 27 - Wed 28-Oct","impact":"High","event":"FOMC MEETING: after the hot September CPI and PPI, markets now expect a hold in October and price a 25bp hike in December (Trading Economics, 15/16-October). A hawkish surprise would extend the dollar and rate pressure on metals."})
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 16-OCTOBER: the curve FLIPPED to a $4.50 BACKWARDATION on 15-October from a $3.50 contango as three-month fell $19.00 - spread and price in OPPOSITE directions; the contango risk recedes further. Trend held at FLAT."
RK[1]['risk']+=" UPDATE 16-OCTOBER: September PPI rose 1.3% m/m (0.5% expected) after the hot CPI; markets now expect an October hold and price a December hike, while the ten-year fell about 13bp to near 5.05% on a risk-off bid (Trading Economics). Trend held at UP."
RK[4]['risk']+=" UPDATE 16-OCTOBER: LME stock fell 250 t to a new series low of 238,125 t on 15-October. Trend held at FLAT."
for r in RK:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 16-OCTOBER: Trading Economics (16-October) reports the container ship that sank in the strait was reportedly hit by an Iranian projectile and that tanker rates hit record highs. Trend held at UP."
d['outlook']['ai_analysis'].insert(0,"FRIDAY REVIEW, 16-OCTOBER: the selloff broadened to the whole metals complex - nickel -3.5%, copper -1.9%, zinc -1.8% on the 15-October official - as hot US CPI and PPI kept a December Fed hike priced and a tech-led risk-off move spread. Aluminium three-month settled $2,994.50, below the 02-January level, but fell least among the majors and the curve flipped back to a $4.50 backwardation with visible stock at another low: the prompt is not confirming the forward's weakness. Alcoa's Q3 confirmed realised aluminium prices have peaked (-5% q/q) while alumina prices rose. Weights held at 10/45/45; a settled break below about 2,977.5 remains the next technical signal, and a backwardation beyond $15 would be the first reversal signal.")

EWS=("REVIEWED 16-OCTOBER ON THE THURSDAY 15-OCTOBER OFFICIAL: three-month settled $2,994.50, down $19.00, a fourth settled close beneath the 3,061.5 July low (now by $67.00); wave (v) of C has travelled $154.00 from the 3,148.5 wave (iv) high on a settled basis and now sits INSIDE the 2,980-3,000 target zone, $17.00 above the rule-based cap near 2,977.5 (wave (v) must stay shorter than (iii)'s $171 so that (iii) is not the shortest). The count is unchanged and wave (v) is mature: the flip to a $4.50 backwardation is a weak, non-price hint of exhaustion. Base case about 65%: (v) terminates in 2,977.5-3,000 and a corrective rebound toward 3,061.5-3,077 follows; alternate about 35%: a settled close beneath 2,977.5 forces a re-count toward the 2,894 weekly 61.8% level. Invalidation of the bearish count unchanged at 3,289; confidence moderate. ")
EWL=("REVIEWED 16-OCTOBER ON THE THURSDAY 15-OCTOBER OFFICIAL: three-month settled $2,994.50, a fourth close beneath the 3,061.5 July low and in the lower half of the 2,950-3,110 zone; the weekly decline from 3,855 extends and the corrective count towards the 61.8% retracement at 2,894 stays preferred - no re-label is needed. ")
d['ew']['short_term']['writeup']=EWS+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=EWL+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="105.30",day="-$0.62 (-0.59%) quoted 16-October (Trading Economics; stats section shows $105.49)",
 note="REFRESHED FRIDAY 16-OCTOBER-2026 (Trading Economics): Brent eased as the IEA agreed to release the remaining 100m barrels of its March coordinated stock draw, despite Hormuz risk (a container ship reportedly hit by an Iranian projectile; tanker rates at record highs) and an 8.6m-barrel US crude draw. Energy is a major smelter cash-cost line. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="85.6",day="about EUR 85.6/MWh on 16-October, -0.9% (Trading Economics; stats section shows EUR 85.42, -1.17%)",
 note="REFRESHED FRIDAY 16-OCTOBER-2026 (Trading Economics): TTF up 12% over a month on Hormuz-constrained Middle East LNG; EU storage about 74% full, below the seasonal norm; Norwegian supply recovery provides some relief. Value approximate. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="102.0",day="about 102.02 on 16-October, +0.03%; fell 0.55% overnight to 101.97 from its 18-month high (Trading Economics; SMM)",
 note="REFRESHED FRIDAY 16-OCTOBER-2026 (Trading Economics): the dollar is consolidating below its post-CPI 18-month high as Treasury yields fell; markets await Fed Chair remarks before the blackout. SOURCE: "+S_TD)
M['US 10-year Treasury yield (%)'].update(value="5.08",day="fell nearly 13bp to about 5.05% on 15-October on a tech/AI risk-off bid; about 5.08% on 16-October (Trading Economics)",
 note="REFRESHED FRIDAY 16-OCTOBER-2026 (Trading Economics): yields retreated from about 5.3% after the CPI print as equities sold off; September PPI +1.3% m/m and retail sales +0.8% keep a December hike priced. Higher yields raise the cost of carrying metal. SOURCE: "+S_TY)
M['EUR/USD'].update(value='1.12080',day="LME fixing on 15-October, +0.13% from 1.11930; ECB fixing 1.12080, BFIX 1.12077",
 note="REFRESHED FRIDAY 16-OCTOBER-2026 to the 15-October LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE THURSDAY 15-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION; Friday's official prints at 13:20 London. Reference and intraday prices (Trading Economics, SMM, Bloomberg) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN: the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 15-October session, so the usual EN/DE agreement test passed.")
C[2]=("COMPENSATING CHECKS: the overviews' prior-day FX column (MTLE 1.11930, ECB 1.11950, BFIX 1.11928) matches the 14-October board verified on 15-October.")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 14-October: aluminium -250 to 238,125; copper -1,400 to 226,600; nickel -588 to 282,066; zinc +6,925 to 151,050; lead -275 to 339,800.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (15-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (eleven sessions, 01- to 15-October) as their latest point. The price chart axis (floor 2,900) brackets three-month at 2,994.50; the stock chart axis floor (225,000 t) brackets visible stock at 238,125 t - both re-checked this run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $2,999.00 against three-month $2,994.50 is therefore a $4.50 BACKWARDATION, flipped from a $3.50 contango on 14-October - spread and price moved in OPPOSITE directions this session."
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a 50% Section 232 rate on full customs value (no change located this run; still described as 50% in Reuters-cited reporting on 14-October), the tariff leg is 0.50 times the 15-October official cash of $2,999.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $105.30), the dollar index (about 102.0), TTF (about EUR 85.6/MWh) and the US ten-year (about 5.08%) are 16-October Trading Economics quotes - the source's own sections differ slightly, so they are approximate; EUR/USD is the 15-October LME fixing, the same session as the board."
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: ALCOA'S ROW AND PER-COMPANY HISTORY WERE REFRESHED THIS RUN TO Q3-2026 from its 15-October release (adjusted EPS $1.82); NO NEW COMPANY WAS BACK-FILLED. Other entries are carried at their last publicly verified figures, and gaps stay gaps."

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 15-OCTOBER: no newer public disclosure","REVIEWED 16-OCTOBER: no newer public disclosure").replace("REVIEWED 15-OCTOBER. NO NEW DATED","REVIEWED 16-OCTOBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']:
    p['asof']=RD
    if p['name']=='Alcoa (AA)':
        p['update']=("UPDATED 16-OCTOBER: Alcoa's Q3-2026 release (15-October) reports alumina production up 11% q/q to 2.467 Mt on improved Pinjarra stability and aluminium production up 2% to 649 kt with the ALUMAR RESTART COMPLETE; FY2026 guidance reaffirmed at 9.5-9.6 Mt alumina and 2.4-2.6 Mt aluminium; a fatal accident at Alumar on 16-September was disclosed; an agreement to sell part of the Massena East site for up to $315m was announced. South32 shareholders APPROVED the sale of its aluminium value chain to Alcoa on 15-October (Aluminium Today); completion guided H1-2027 subject to regulatory approvals. ")+p['update'].replace("REVIEWED 16-OCTOBER. NO NEW DATED PUBLIC DISCLOSURE FOR THIS SPECIFIC ASSET IN THIS WINDOW","PRIOR NOTE")
        p['status']="2026 ALUMINA GUIDANCE 9.5-9.6 Mt REAFFIRMED IN Q3 (ALUMINA OUTPUT +11% Q/Q ON PINJARRA STABILITY); ALUMAR RESTART COMPLETE; SAN CIPRIAN RUNNING CLOSE TO FULL; PORTLAND RESTART COMPLETED; SOUTH32 ALUMINIUM VALUE CHAIN ACQUISITION (UP TO $5.6bn) APPROVED BY SOUTH32 SHAREHOLDERS 15-OCTOBER, CLOSE GUIDED H1-2027"
        p['src']=[L_AA,S_AA]

for s in [[L_TE,S_TE],[L_AA,S_AA],[L_AAI,S_AAI],[L_SF,S_SF],[L_SA,S_SA],[L_SO,S_SO],[L_S32,S_S32],[L_BR,S_BR],[L_TY,S_TY],[L_TD,S_TD],[L_TG,S_TG]]:
    d['sources'].append(s)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 15-Oct-2026 session (English and German overviews agree; stock lines reconciled vs 14-Oct)",W])
d['outlook']['sources'].append([L_AA,S_AA]); d['outlook']['sources'].append([L_SO,S_SO])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-14'
ph['rows'][-1]=['2026-10-15',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
