# 2026-10-13 SECOND PASS (owner present, Westmetall fetch now GRANTED): board ROLLED to MONDAY 12-Oct LME official.
# EN+DE cache-busted overviews agree exactly on 12-Oct; Al per-metal table shows 12-Oct newest with 09-Oct prior unchanged;
# 5/5 stock lines reconcile vs 09-Oct. Replaces the first pass's "board kept on 09-Oct" text.
import json, re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
W="https://www.westmetall.com/en/markdaten.php"
B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
cash,prev_c,m3,prev_m,stk,prev_s=3055.0,3055.5,3060.0,3070.0,238625,238875
spr=cash-m3; pc=(cash-prev_c)/prev_c*100; pm=(m3-prev_m)/prev_m*100

VER=("COMPILED TUESDAY 13-OCTOBER-2026. THE BOARD IS THE MONDAY 12-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION (Tuesday's official prints at 13:20 London). "
 "COMPLETENESS CHECKS: (1) the cache-busted English and German Westmetall overviews AGREE EXACTLY on 12-October across all six metals, all six stock lines and the foreign-exchange fixings (EUR/USD MTLE 1.11770); (2) the aluminium per-metal daily table shows 12-October as the newest row with 09-October reproduced unchanged as the prior row; "
 "(3) ALL FIVE STOCK LINES RECONCILE against 09-October: aluminium 238,875 less 250 to 238,625; copper 233,025 less 1,750 to 231,275; nickel 282,864 less 636 to 282,228; zinc 126,850 plus 6,000 to 132,850; lead 347,125 less 1,575 to 345,550. "
 "The whole board sits on ONE UNIFORM SESSION (12-October); no intraday or reference mark is used in it. Prior-month averages remain the completed SEPTEMBER-2026 official means.")
AL=(f" CASH SETTLED $3,055.00 ON THE 12-OCTOBER OFFICIAL, DOWN $0.50 OR {pc:.2f}% FROM $3,055.50. THREE-MONTH SETTLED $3,060.00, DOWN $10.00 OR {pm:.2f}% FROM $3,070.00 - THE FIRST SETTLED THREE-MONTH OFFICIAL BENEATH THE 3,061.5 JULY LOW (by $1.50), after an intraday low of $3,023, the lowest since 13-February (Reuters). "
 "SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS: three-month fell faster than cash, so the CONTANGO NARROWED $9.50 TO $5.00 from $14.50 - the prompt end held up while the forward fell. "
 "VISIBLE LME STOCK DREW 250 TONNES TO 238,625, a new series low. The LME euro fixing eased to 1.1177 from 1.1209 as the dollar index rose to about 102.5 (Trading Economics).")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,055.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,060.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $1.50 BENEATH THE 3,061.5 JULY LOW, $17.00 beneath the 3,077 weekly 50% retracement, $123.00 below the broken 3,183 daily level and $229.00 below the 3,289 daily invalidation."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"-5.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,055.00 against three-month $3,060.00 is a $5.00 CONTANGO, NARROWED $9.50 from $14.50. Spread and flat price moved in OPPOSITE directions (three-month down $10.00, contango narrower). The reversal condition, a BACKWARDATION BEYOND $15.00 on a settled official, is UNMET; the bearish structural confirmation, a contango beyond $24.50, is also unmet. The September mean spread was $"+f"{sep_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"238,625","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK DREW 250 TONNES TO 238,625, a new series low on this page, after four unchanged sessions. September's mean stock was {sep_s:,} tonnes. A small draw with a narrower contango says the prompt end is not loosening even as price breaks lower."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":sep_c,"note":VER+AL+" AVERAGE COLUMN: the completed SEPTEMBER-2026 official cash mean; cash now sits $"+f"{sep_c-cash:,.2f} beneath it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":sep_m,"note":VER+f" THREE-MONTH SETTLED $3,060.00, DOWN $10.00 OR {pm:.2f}% FROM $3,070.00 - $1.50 beneath the 3,061.5 July low, the first settled close below it. AVERAGE COLUMN: the completed September-2026 official three-month mean of ${sep_m:,.2f}; three-month sits ${sep_m-m3:,.2f} below it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":sep_s,"note":VER+f" STOCK DREW 250 TONNES TO 238,625. AVERAGE COLUMN: the September-2026 mean of {sep_s:,} tonnes; level about {sep_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":-14.5,"avg":sep_sp,"note":VER+f" A $5.00 CONTANGO, NARROWED $9.50 FROM $14.50. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the September-2026 mean spread of ${sep_sp:,.2f}. Flat price and spread moved in OPPOSITE directions (three-month down, contango narrower). REVERSAL CONDITION, RESTATED UNCHANGED: a return to BACKWARDATION BEYOND $15.00 on a settled official."},
 {"name":"EUR/USD LME fixing","cur":1.1177,"prev":1.1209,"avg":1.1465,"note":VER+" THE LME EURO FIXING EASED TO 1.11770 FROM 1.12090 at the Monday ring; the ECB fixing printed 1.11810 and BFIX 1.11756. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (12-Oct official)","price":"3,055.0","basis":f"THE 12-OCTOBER-2026 OFFICIAL CASH SETTLEMENT OF $3,055.00, DOWN $0.50 OR {pc:.2f}%. Next official Tuesday 13-October 13:20 London."},
 {"tenor":"3-month (12-Oct official)","price":"3,060.0","basis":f"THE 12-OCTOBER-2026 OFFICIAL THREE-MONTH OF $3,060.00, DOWN $10.00 OR {pm:.2f}% - $1.50 beneath the 3,061.5 July low (first settled close below it), $17.00 beneath the 3,077 weekly retracement."},
 {"tenor":"Cash-to-3M structure","price":"-5.0 (CONTANGO)","basis":"A $5.00 CONTANGO, narrowed $9.50 from $14.50. Flat price and spread moved in OPPOSITE directions."},
 {"tenor":"Visible LME stock","price":"238,625 t","basis":f"DREW 250 t on the session to a new series low; September mean {sep_s:,} t."},
]
d['outlook']['curve_note']=("THE CURVE FIRMED AS THE FLAT PRICE BROKE LOWER. On the 12-October official cash $3,055.00 sits $5.00 BELOW three-month $3,060.00, a CONTANGO narrowed $9.50 from $14.50. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. The sequence since 16-September reads backwardations of $21.00, $18.50 and $3.00, then contangos of $10.50, $22.00, $20.00, $24.50, $13.00, $3.50, $6.50, $6.00, $11.00, $12.50, $11.00, $14.00, $11.50, $8.50, $14.50 and now $5.00. "
 f"READ: the forward led the fall while the prompt held, and visible stock drew to a new low at 238,625 t - so the break below the July low is a macro and supply-recovery repricing, not a prompt glut. The September mean spread was ${sep_sp:,.2f}. The reversal condition (a backwardation beyond $15.00) is unmet; a contango beyond $24.50 would be the bearish structural confirmation.")

ls=d['lme_series']; assert ls[-1][0]=='09-Oct', ls[-1]
d['lme_series']=ls[1:]+[["12-Oct",cash,m3,stk]]
assert all(225000<r[3]<255000 for r in d['lme_series']) and all(2950<r[1]<3450 and 2950<r[2]<3450 for r in d['lme_series'])
# (cash, 3M, prev cash, prev 3M)
CU=(14822.0,14657.5,14689.0,14570.0); NI=(15515.0,15720.0,15545.0,15720.0); ZN=(3811.0,3760.0,3840.0,3781.5); PB=(1842.0,1885.0,1847.0,1883.5)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round((m3/3010.5-1)*100,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
zs=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0]; ps=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zs)+3811.0)/8)/(sum(zs)/7),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(ps)+1842.0)/8)/(sum(ps)/7),1)
ms=d['metals_series']; R=ms['rows']
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])): R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-10-12'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending MONDAY 12-OCTOBER-2026. THE WINDOW ROLLED THIS RUN: 21-September dropped and 12-October appended, so the window is 22-September to 12-October. Every point is an official cash settlement, verified against the cache-busted Westmetall English and German overviews, which agree to the cent, the aluminium per-metal daily table (12-October newest, 09-October unchanged), and five-for-five stock-line reconciliation. Next official Tuesday 13-October.")
ms['src']=["Westmetall - LME official cash settlements, EN and DE overviews cache-busted and in exact agreement (12-October-2026 session)",W]
AVGNOTE=" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,822.00, up $133.00 or 0.91%; three-month $14,657.50, up $87.50 or 0.60%. The BACKWARDATION WIDENED to $164.50 from $119.00 while stock DREW 1,750 tonnes to 231,275 - prompt tightness firming for a fifth session. Reuters (12-October) cited a fatal landslide that partially suspended Codelco's El Teniente mine and a continuing strike at Centinela."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,515.00, down $30.00 or 0.19%; three-month $15,720.00, unchanged. CONTANGO widened to $205.00 from $175.00, still the widest carry on the board. Stock drew 636 tonnes to 282,228. Reuters reported an intraday low near $15,500, the lowest since late December."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,811.00, down $29.00 or 0.76%; three-month $3,760.00, down $21.50 or 0.57%. BACKWARDATION narrowed to $51.00 from $58.50 as 6,000 tonnes were delivered in, lifting stock to 132,850 - the highest since mid-2025 per Reuters. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,842.00, down $5.00 or 0.27%; three-month $1,885.00, up $1.50 or 0.08%. CONTANGO widened to $43.00 from $36.50. Stock drew 1,575 tonnes to 345,550, a sixteenth consecutive draw. Lead remains the weakest metal on this board year to date."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Monday 12-October official copper three-month rose 0.60% and lead 0.08%, nickel was flat, zinc fell 0.57% and aluminium fell 0.33% to a settled close beneath its July low. The LME euro fixing eased to 1.1177.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" September cash mean ${old[n]['avg']:,.2f}."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='09-Oct'
        i['hist']=i['hist'][1:]+[["12-Oct",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,657.50 (3M); 14,822.00 (cash) $/t"
        i['ratio']="~14,822.00 $/t cash vs LME 3M 14,657.50 $/t"
        i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the MONDAY 12-OCTOBER-2026 session at $14,822.00, UP $133.00 or 0.91% against $14,689.00. THE WINDOW ROLLED THIS RUN: 21-September dropped and 12-October appended, so the series is the last fifteen published official cash sessions, 22-September to 12-October - the same window as the LME Board sparklines. Official settlement only, verified on the cache-busted Westmetall English and German overviews, which agree to the cent. "
                  "Copper structure for context: backwardation $164.50 (from $119.00), stock drew 1,750 t to 231,275 t.")
d['inputs_summary']=("UPDATE 13-OCTOBER: copper rolled to the Monday 12-October LME official cash of $14,822.00, up $133.00, with its fifteen-session window moved to 22-September to 12-October; Reuters tied copper's strength to a fatal landslide that partially suspended Codelco's El Teniente mine. No new SMM fluoride, silicon or magnesium weekly mark was located, and the carbon settlement cycle (anodes, pitch, green coke) is due around 17-18 October - so every other row is carried at its own dated public mark and no value was interpolated.")

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 09-October official cash of \$3,055\.50, or \$1,527\.75, DOWN \$2\.50 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$875\.25, so 63\.6%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 12-October official cash of $3,055.00, or ${tl:,.2f}, DOWN $0.25 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
n=0
for p in d['premiums']:
    p['src'],k=OLDT.subn(NEWT,p['src']); n+=k
    p['src']=p['src'].replace("COMPILED TUESDAY 13-OCTOBER-2026 (LME BOARD KEPT ON 09-OCTOBER - SEE CAVEATS).","COMPILED TUESDAY 13-OCTOBER-2026 (LME BOARD ON THE 12-OCTOBER OFFICIAL).")
print('premium tariff replaced',n); assert n==len(d['premiums'])

d['lme_commentary']=(f"ALUMINIUM SETTLED BENEATH ITS JULY LOW FOR THE FIRST TIME. On the Monday 12-October official cash settled $3,055.00, down $0.50, and three-month $3,060.00, down $10.00 or {abs(pm):.2f}% - $1.50 beneath the 3,061.5 July low - after an intraday low of $3,023, the lowest since 13-February, before a partial recovery (Reuters). "
 "Three-month fell faster than cash, so the contango NARROWED $9.50 to $5.00 (spread and price in OPPOSITE directions), and visible stock drew 250 t to a new low of 238,625 t. "
 "Reuters attributed the slide to a dollar near an 18-month high ahead of US inflation data, easing Gulf supply concerns and expectations of more Indonesian capacity; Citi sees a 1.8 Mt surplus in 2027 against a 941,000 t deficit this year. Copper rose on Chilean supply disruption while zinc fell on a 6,000 t delivery. "
 f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}.")
d['net_read']=("NET: BEARISH TREND IN CONTROL; THE JULY LOW HAS BROKEN ON A SETTLED BASIS, NARROWLY. Against: three-month settled $1.50 beneath 3,061.5 after an eight-month intraday low of $3,023; the dollar is near its highest since April 2025; Citi now forecasts a 2027 surplus; spot Japanese premiums ($230/t, SMM) sit below the $255/t Q4 benchmark; the narrative is supply recovery. "
 "Constructive: the break is marginal and the intraday low was bought; the contango narrowed to $5.00 and visible stock drew to a new low of 238,625 t; European gas at its highest since December 2022 and fresh Hormuz tanker attacks keep smelter energy and freight costs high.")
d['bottom_line']=("BOTTOM LINE: aluminium settled on the Monday 12-October LME official at cash $3,055.00 and three-month $3,060.00 - the first settled close beneath the 3,061.5 July low, by $1.50, after an intraday eight-month low of $3,023. "
 "The contango narrowed to $5.00 and visible stock drew to 238,625 t, so the prompt is not loosening. Scenario weights move to 10% bull / 45% base / 45% bear; the daily Elliott count (wave (v) of a C-wave decline from 3,374) now targets 2,980-3,000 with a rule-based floor near 2,977, invalidation 3,289; the weekly corrective count towards 2,894 stays preferred.")
d['commercial']=d['commercial'].replace("FIRST, THE CURVE PAYS BUYERS A LITTLE MORE TO WAIT: a $14.50 contango on 09-October, widened from $8.50.","FIRST, THE CURVE IS NEAR FLAT: a $5.00 contango on 12-October, narrowed from $14.50, so there is little carry reward for waiting.")
d['commercial']=re.sub(r"on 09-October cash, 63\.6% of the \$2,403/t premium",f"on 12-October cash, {share:.1f}% of the $2,403/t premium",d['commercial'])
d['commercial']=d['commercial'].replace("the first verified post-weekend official decides whether 3,061.5 has broken on a settled basis (Reuters reported an intraday $3,023 on 12-October);","the 12-October official settled $1.50 beneath 3,061.5 - follow-through below $3,023 would open 2,980-3,000;")

for s in d['outlook']['scenarios']:
    s['prob']={'Bull':'10%','Base':'45%','Bear':'45%'}[s['case']]
    s['drivers']=re.sub(r"^HELD 13-OCTOBER \(board kept on 09-October.*?no verified new official\) AND ","",s['drivers'],flags=re.S)
    s['drivers']=("MOVED 13-OCTOBER (from 11/45/44 to 10/45/45): the 12-October official settled three-month at $3,060.00, the first settled close beneath the 3,061.5 July low, after an eight-month intraday low of $3,023; Citi's 2027 surplus call adds to the bear weight. The marginal size of the break, the narrower $5.00 contango and a further stock draw argue against a bigger shift. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

d['so_what']={"line":"Aluminium settled beneath its early-July floor for the first time on Monday - three-month $3,060 after an eight-month intraday low of $3,023 - as a strong dollar, easing Gulf supply fears and Citi's 2027 surplus call weigh, though a near-flat curve and falling LME stock show the prompt market is not loosening.",
 "points":[
 "WHAT MOVED: Monday's LME official settled cash at $3,055.00 (-$0.50) and three-month at $3,060.00 (-$10.00, -0.33%), $1.50 beneath the $3,061.5 July low; the contango narrowed to $5.00 from $14.50 (spread and price moved in opposite directions) and LME stock drew 250 t to a new low of 238,625 t.",
 "WHY: the dollar index near 102.5, its highest since April 2025, ahead of US inflation data; easing Gulf supply concerns and expected Indonesian capacity; Citi sees a 1.8 Mt surplus in 2027 versus a 941,000 t deficit this year (Reuters). Copper rose 0.6% on Chilean mine disruption while aluminium fell.",
 "ENERGY AND LOGISTICS: two more tankers were attacked near Hormuz on Sunday; Brent is near $105 and European gas hit its highest since December 2022 at about 84 EUR/MWh - raising smelter power-cost risk in Europe.",
 "WHAT TO WATCH: follow-through beneath $3,023 opens $2,980-3,000; US inflation data this week; Alcoa's Q3 results on Thursday 15-October after the New York close; the mid-October carbon settlements around 17-18 October."]}

d['feed'][0]={"when":"Tue 13-Oct","impact":"Bearish","text":f"BOARD ROLLED TO THE MONDAY 12-OCTOBER LME OFFICIAL: cash $3,055.00 (-$0.50), three-month $3,060.00 (-$10.00, {pm:.2f}%) - the first settled close beneath the 3,061.5 July low - contango NARROWED to $5.00 from $14.50, stock drew 250 t to 238,625 t. Verified on cache-busted English and German overviews in exact agreement, the aluminium per-metal table, and five-for-five stock reconciliation."}
d['news'].insert(0,{"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
 "headline":f"LME ALUMINIUM SETTLES BENEATH THE JULY LOW. The Monday 12-October official settled cash at $3,055.00 ({pc:.2f}%) and three-month at $3,060.00 ({pm:.2f}%), $1.50 beneath the 3,061.5 July low. The contango narrowed to $5.00 from $14.50 and visible stock drew 250 t to 238,625 t. Copper three-month rose to $14,657.50 with its backwardation widening to $164.50; zinc stock jumped 6,000 t to 132,850 t."})
d['news']=d['news'][:20]

for c in d['outlook']['catalysts']:
    if c['date']=='Daily, from Mon 12-Oct':
        c['date']='Daily, from Tue 13-Oct'
        c['event']="3,061.5 BROKEN ON A SETTLED BASIS (BY $1.50), 3,023 INTRADAY LOW, 3,148.5 / 3,183 OVERHEAD, 3,289 INVALIDATION. Three-month settled $3,060.00 on Monday 12-October after an intraday $3,023. Follow-through beneath 3,023 opens the 2,980 area (wave (v) of C, rule cap near 2,977); a recovery back above 3,077 on a settled official would weaken the break; above 3,148.5 would warn the C wave is complete and above 3,183 would void the impulsive C-wave labelling."
RK=d['outlook']['risks']
RK[0]['risk']+=" UPDATE 13-OCTOBER: the contango NARROWED $9.50 to $5.00 on 12-October even as three-month fell $10.00 - spread and price in opposite directions; well inside the $24.50 bearish-confirmation threshold. Trend held at FLAT."
RK[4]['risk']+=" UPDATE 13-OCTOBER: LME stock drew 250 t to 238,625 t on 12-October, a new series low after four flat sessions. Trend held at FLAT."
d['outlook']['ai_analysis'][0]=("TUESDAY REVIEW, 13-OCTOBER: the July floor broke on a settled basis, narrowly. Monday's official settled three-month at $3,060.00, $1.50 beneath 3,061.5, after an eight-month intraday low of $3,023 (Reuters). The drivers are macro and supply: a dollar near its highest since April 2025, easing Gulf supply concerns, and Citi's call for a 1.8 Mt 2027 surplus. Against that, the contango narrowed to $5.00, LME stock drew to a new low, European gas is at a near three-year high and fresh Hormuz tanker attacks raise smelter energy and freight costs. Bear weight raised to 45%; US inflation data and Alcoa's 15-October results are next.")

EWOLD=re.compile(r"^REVIEWED 13-OCTOBER \(BOARD KEPT ON 09-OCTOBER; COUNT UNCHANGED PENDING VERIFICATION\)\..*?not a re-label trigger\. ",re.S)
EWS=("REVIEWED 13-OCTOBER ON THE MONDAY 12-OCTOBER OFFICIAL: three-month settled $3,060.00, down $10.00, the FIRST SETTLED CLOSE BENEATH THE 3,061.5 JULY LOW (by $1.50), after an intraday low of $3,023, the lowest since 13-February. This confirms the daily base case that wave (v) of C is extending; targets 2,980-3,000 with the rule-based cap on (v) near 2,977.5 (it must stay shorter than (iii)'s $171). The double-bottom alternate is cut to about 30% and needs a settled recovery above 3,077 to revive. Invalidation unchanged at 3,289. ")
EWL=("REVIEWED 13-OCTOBER ON THE MONDAY 12-OCTOBER OFFICIAL: three-month settled $3,060.00, beneath the 3,061.5 July low, extending the weekly decline from 3,855 and keeping the corrective count towards 2,894 preferred; no re-label. ")
for k,t in (('short_term',EWS),('long_term',EWL)):
    w=d['ew'][k]['writeup']; w2,nn=EWOLD.subn(t,w); assert nn==1,k; d['ew'][k]['writeup']=w2
d['ew']['short_term']['writeup']=d['ew']['short_term']['writeup'].replace("BASE CASE, ABOUT 62%","BASE CASE, ABOUT 70% (RAISED 13-OCTOBER FROM 62%)").replace("ALTERNATE, ABOUT 38%","ALTERNATE, ABOUT 30% (CUT FROM 38%)")

for m in d['macro']:
    if m['name']=='EUR/USD':
        m['value']='1.11770'; m['day']="LME fixing on 12-October, -0.29% from 1.12090; ECB fixing 1.11810, BFIX 1.11756"
        m['note']="REFRESHED TUESDAY 13-OCTOBER-2026 to the 12-October LME fixing via Westmetall, the same session as the LME board."

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE MONDAY 12-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION; Tuesday's official prints at 13:20 London. Reference prices (Reuters, Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("THE COMPLETENESS TEST PASSES: the aluminium per-metal daily table shows 12-October as the newest row with 09-October reproduced unchanged as the prior row ($3,055.50 / $3,070.00 / 238,875 t).")
C[2]=("THE ENGLISH AND GERMAN OVERVIEWS WERE BOTH REQUESTED CACHE-BUSTED ON 13-OCTOBER AND AGREE EXACTLY on 12-October across all six metals, stocks and FX fixings (EUR/USD MTLE 1.11770).")
C[3]=("ALL FIVE STOCK LINES RECONCILE ARITHMETICALLY against 09-October: aluminium -250 to 238,625; copper -1,750 to 231,275; nickel -636 to 282,228; zinc +6,000 to 132,850; lead -1,575 to 345,550.")
C[4]=("THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (12-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME averages are the completed September-2026 official means; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the October cash average-to-date (eight sessions, 01- to 12-October) as their latest point. The price chart axis floor (2,950) brackets three-month at 3,060; the stock chart axis floor (225,000 t) brackets visible stock at 238,625 t.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,055.00 against three-month $3,060.00 is therefore a $5.00 CONTANGO, narrowed $9.50 from $14.50 on 09-October - and it narrowed while three-month fell, i.e. spread and price moved in OPPOSITE directions."
for i,c in enumerate(C):
    if c.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=f"THE TARIFF DECOMPOSITION IS CALCULATED, NOT ASSESSED, AND THE TWO ARE NEVER MIXED. At a re-verified 50% Section 232 rate on full customs value, the tariff leg is 0.50 times the 12-October official cash of $3,055.00, or ${tl:,.2f}, leaving an ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic). This page does not fabricate freight, financing or tightness splits for any premium row."
    if c.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]="MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent ($105.32) and the dollar index (102.45) and the US ten-year (5.20%) are Trading Economics reference marks viewed 13-October; TTF (84.20 EUR/MWh) is the 12-October close; EUR/USD is the 12-October LME fixing, the same session as the board."

# KPI/raw/scenario/etc text from the first pass that described the board as kept - scrub
KPI_FIRST=("COMPILED TUESDAY 13-OCTOBER-2026 AT ABOUT 03:30 LONDON. THE MONDAY 12-OCTOBER OFFICIAL HAS PRINTED BUT COULD NOT BE VERIFIED THIS RUN")
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str) and KPI_FIRST in o:
        j=o.find(KPI_FIRST); e=o.find("The 09-October board was verified by the 10- and 11-October runs.",j)
        assert e>0; o=o[:j]+"COMPILED TUESDAY 13-OCTOBER-2026 ON THE VERIFIED MONDAY 12-OCTOBER OFFICIAL (see the LME panel)."+o[e+len("The 09-October board was verified by the 10- and 11-October runs."):]
    return o
d=walk(d)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 12-Oct-2026 session (EN+DE, cache-busted, in exact agreement)",W])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-09'
ph['rows'].append(['2026-10-12',cash,m3,stk]); ph['updated']='2026-10-13'
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
s=json.dumps(d)
for bad in ["ONE SESSION BEHIND","COULD NOT BE VERIFIED","could not be verified","BOARD KEPT","board kept","KEPT ON THE FRIDAY"]:
    print(bad, s.count(bad))
print('ok')
