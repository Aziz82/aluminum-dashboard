# Daily data refresh - 2026-11-07 (SATURDAY, ~02:35 UTC). No ring today. Board ROLLED TWO SESSIONS to the FRIDAY 06-Nov LME official
# (the 06-Nov run had to carry 04-Nov). Westmetall EN + DE overviews agree on 06-Nov (Al cash 3,117 / 3M 3,050 / stock 227,600 -875; MTLE 1.11690 vs 1.12260);
# all five per-metal tables show 06-Nov as newest row with NO later row (Saturday - complete, not lagging) and supply the 05-Nov session.
# 05-Nov: 3M 3,097.50 (>3,077, backwardation $62.50) => +5 bull (20/45/35). 06-Nov: 3M 3,050 (<3,061.5 weekly close) => 5 back to bear (15/45/40).
import json,re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-07'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_AC="https://www.alcircle.com/news/lme-aluminium-cash-price-rises-0-8-to-3-160-t-on-november-5-as-stocks-decline-121859"; L_AC="AL Circle - LME aluminium cash +0.8% to $3,160/t on 05-Nov; cancelled warrants 17,375 t; LME alumina (Platts) $398.24/t (06-Nov-2026)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum 3,065.60 (+0.13%) on 06-Nov-2026 (CFD reference)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$97.8-98.3, weekly loss >12.5%, steepest since 2020 (06-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index 102.28 (+0.72%); October payrolls +165k vs 65k forecast (06-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 85.6/MWh (-5.6%), two-week low; EU storage 74% (06-Nov-2026)"
S_ST="https://straits.live/briefs/2026-11-07"; L_ST="Straits Daily Brief - Strait of Hormuz, 07-Nov-2026"
S_CX="https://www.sec.gov/Archives/edgar/data/0000949157/000162828026071024/a20260930q3ex991earningsre.htm"; L_CX="Century Aluminum - Q3-2026 earnings release (8-K Ex.99.1, 05-Nov-2026)"
S_CXA="https://www.alcircle.com/news/century-aluminum-gets-a-production-boost-as-iceland-smelter-restarts-lifting-q3-performance-121867"; L_CXA="AL Circle - Century Aluminum Q3 lifted by Grundartangi Line 2 restart (06-Nov-2026)"
S_NV="https://www.alcircle.com/news/novelis-q2-sees-net-sales-rise-25-while-rolled-product-shipments-fell-2-121860"; L_NV="AL Circle - Novelis Q2 FY27: net sales +25% to $5.9bn, adj EBITDA $508m, shipments -2% (06-Nov-2026)"
S_AO="https://www.alcircle.com/news/global-alumina-production-remains-below-2025-levels-despite-a-q3-rebound-reaching-114-million-tonnes-in-9m2026-121868"; L_AO="AL Circle - Global alumina output 9M-2026 114.625 Mt (-0.29% y/y); Q3 39.396 Mt (06-Nov-2026)"
S_BB="https://www.alcircle.com/news/bell-bay-aluminium-navigates-workforce-changes-after-government-backed-rescue-121870"; L_BB="AL Circle - Bell Bay Aluminium workforce review, up to 10 redundancies (06-Nov-2026)"
S_S3="https://www.alcircle.com/news/south32-maintains-june-2027-timeline-for-alcoa-s-acquisition-of-aluminium-assets-121864"; L_S3="AL Circle - South32 maintains June 2027 timeline for Alcoa acquisition (06-Nov-2026)"

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3135.0 and B['LME 3-month']['cur']==3074.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
c5,m5,s5=3160.0,3097.5,228475
cash,m3,stk=3117.0,3050.0,227600
prev_c,prev_m,prev_s=c5,m5,s5
spr=cash-m3; sp5=c5-m5; assert spr==67.0 and sp5==62.5 and s5-875==stk and 228750-275==s5
ytd=(m3/3010.5-1)*100

VER=("COMPILED SATURDAY 07-NOVEMBER-2026 ABOUT 02:35 LONDON. THERE IS NO LME RING ON SATURDAY, SO THE BOARD IS THE FRIDAY 06-NOVEMBER-2026 LME OFFICIAL - THE LAST TRADING SESSION AND THE CORRECT FIGURE TO CARRY UNTIL MONDAY. "
 "THE BOARD ROLLED TWO SESSIONS THIS RUN: the 06-November run had to carry 04-November because Thursday's official was not yet published; both the THURSDAY 05-NOVEMBER and FRIDAY 06-NOVEMBER officials are now sourced and recorded. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 06-November official for all metals with stocks and FX (EUR/USD MTLE 1.11690; prior-day 1.12260); (2) all five per-metal daily tables (aluminium, copper, nickel, zinc, lead) show 06-November as the newest row with NO later row, and supply the 05-November session; "
 "(3) ALL FIVE STOCK LINES RECONCILE 06-November against 05-November via the change column: aluminium 228,475 less 875 to 227,600; copper 318,675 less 2,000 to 316,675; nickel 273,042 less 1,074 to 271,968; zinc 148,225 less 1,350 to 146,875; lead 308,650 less 4,650 to 304,000. "
 "The whole board sits on ONE UNIFORM SESSION (06-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" THURSDAY 05-NOVEMBER: cash $3,160.00 (+$25.00), three-month $3,097.50 (+$23.50) - a settled close ABOVE 3,077 and above the 3,084.00 rebound high, with a $62.50 backwardation; stock 228,475 t (-275 t). "
 "FRIDAY 06-NOVEMBER (the board): CASH SETTLED $3,117.00, DOWN $43.00 OR 1.36% FROM $3,160.00. THREE-MONTH SETTLED $3,050.00, DOWN $47.50 OR 1.53% FROM $3,097.50 - back below 3,061.5 and 3,077 on the WEEKLY CLOSE, but $25.50 above the 3,024.50 bear-trigger level, $8.00 above the 3,042.00 low of 03-November and $55.50 above the 2,994.50 settled low of 15-October; $39.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). On the week three-month is down $30.00 from $3,080.00 (30-October). "
 "THE BACKWARDATION WIDENED TO $67.00 FROM $62.50 WHILE THE FLAT PRICE FELL - SPREAD AND PRICE MOVED IN OPPOSITE DIRECTIONS on Friday (on Thursday they moved together, both firmer) - a seventeenth straight backwardation and the widest since mid-September. "
 "VISIBLE LME STOCK FELL 875 t TO 227,600 t, another new series low and a thirteenth straight draw. The Trading Economics aluminium reference showed $3,065.60 (+0.13%) for 06-November - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,117.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,050.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $27.00 BELOW THE 3,077 WEEKLY 50% RETRACEMENT and $11.50 below the 3,061.5 July low, $98.50 beneath the 3,148.5 wave (iv) high and $239.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a sixteenth session."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+67.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,117.00 against three-month $3,050.00 is a $67.00 BACKWARDATION, WIDER than 05-November's $62.50 even though cash fell $43.00 and three-month $47.50 - SPREAD AND PRICE MOVED IN OPPOSITE DIRECTIONS. It stays above the published $15.00 reversal condition for a sixth session, the widest print since mid-September and a seventeenth straight backwardation; a contango beyond $24.50 would reverse the structural signal. The October mean spread was $"+f"{oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"227,600","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 875 t TO 227,600 t (05-November: -275 t to 228,475 t), another new series low and a thirteenth straight draw. AL Circle reports cancelled warrants rose 2,200 t to 17,375 t on 05-November (live warrants 211,100 t). October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 05-November official."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $3,050.00, DOWN $47.50 FROM THE 05-NOVEMBER $3,097.50 - $27.00 below 3,077, $11.50 below 3,061.5 and $25.50 above 3,024.50; $39.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":oct_s,"note":VER+f" STOCK DOWN 875 t TO 227,600 t, another new series low (05-November 228,475 t). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":sp5,"avg":oct_sp,"note":VER+f" A $67.00 BACKWARDATION, WIDER THAN 05-NOVEMBER'S $62.50 (04-November $61.00). CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On Friday cash fell $43.00 and three-month $47.50, so structure FIRMED while price FELL - opposite directions. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50 and $67.00."},
 {"name":"EUR/USD LME fixing","cur":1.1169,"prev":1.1226,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.11690 FROM 1.12260 at the Friday ring as the dollar firmed after strong US payrolls (05-November fixing 1.12260, up from 1.12640? no - see caveat). AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
# fix the EUR note wording (no speculative text)
d['benchmark'][4]['note']=VER+" THE LME EURO FIXING FELL TO 1.11690 ON 06-NOVEMBER FROM 1.12260 ON 05-NOVEMBER (04-November 1.12640) as the dollar firmed after a strong US payrolls report. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."
d['outlook']['forward_path']=[
 {"tenor":"Cash (06-Nov official)","price":"3,117.0","basis":"THE FRIDAY 06-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,117.00, DOWN $43.00 OR 1.36% (05-November $3,160.00). No ring on Saturday; next official Monday 09-November 13:20 London."},
 {"tenor":"3-month (06-Nov official)","price":"3,050.0","basis":"THE 06-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $3,050.00, DOWN $47.50 after Thursday's $3,097.50 - $27.00 below 3,077, $11.50 below 3,061.5, $25.50 above 3,024.50 and $55.50 above the 2,994.50 October low."},
 {"tenor":"Cash-to-3M structure","price":"+67.0 (BACKWARDATION)","basis":"A $67.00 BACKWARDATION, wider than $62.50 as price fell (opposite directions) - above the $15.00 reversal condition for a sixth session."},
 {"tenor":"Visible LME stock","price":"227,600 t","basis":f"DOWN 875 t to a new series low on 06-November (thirteenth straight draw); October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("STRUCTURE KEEPS TIGHTENING WHILE PRICE GIVES BACK THURSDAY'S GAIN. On the 06-November official cash $3,117.00 sits $67.00 ABOVE three-month $3,050.00, a BACKWARDATION, wider than $62.50 on 05-November even as cash fell $43.00 and three-month $47.50 - spread and flat price moved in OPPOSITE directions on Friday after moving together on Thursday. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50 and now $67.00. "
 f"READ: a seventeenth straight backwardation, the sixth above $15.00, with visible stock at another low (227,600 t) and cancelled warrants rising (17,375 t on 05-November, AL Circle) - prompt LME metal is tight, but the outright price is being held back by macro (a firmer dollar after strong payrolls) and collapsing energy. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2900,3450] and d['chart_stock_axis']==[210000,255000]
# stock 227,600 leaves 17,600 t headroom over the 210,000 floor; re-bracket early to keep room
d['chart_stock_axis']=[200000,255000]

ls=d['lme_series']; assert ls[-1][0]=='04-Nov', ls[-1]
d['lme_series']=ls[2:]+[["05-Nov",c5,m5,s5],["06-Nov",cash,m3,stk]]
assert all(200000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(13955.0,13780.0,14110.0,14030.0); NI=(16095.0,16280.0,16100.0,16265.0); ZN=(3759.0,3735.0,3877.0,3842.0); PB=(1857.0,1887.0,1866.5,1899.0)
CU4,NI4=(14201.0,14095.0),(15465.0,15675.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/3074.0,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU4[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI4[1],1)
zn_old=(3935.0+3869.0+3875.0)/3; zn_mtd=(3935.0+3869.0+3875.0+ZN[2]+ZN[0])/5
pb_old=(1869.5+1862.0+1858.0)/3; pb_mtd=(1869.5+1862.0+1858.0+PB[2]+PB[0])/5
mh['zn'][-1]=round(mh['zn'][-1]*zn_mtd/zn_old,1); mh['pb'][-1]=round(mh['pb'][-1]*pb_mtd/pb_old,1)
ms=d['metals_series']; R=ms['rows']
for k,v5,v6,pv in (('CU',CU[2],CU[0],14201.0),('NI',NI[2],NI[0],15465.0),('ZN',ZN[2],ZN[0],3875.0),('PB',PB[2],PB[0],1858.0)):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][2:]+[v5,v6]; assert len(R[k])==15
ms['asof']='2026-11-06'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending FRIDAY 06-NOVEMBER-2026 (no ring on Saturday). THE WINDOW ROLLED TWO SESSIONS THIS RUN (the 06-November run had carried 04-November): 15 and 16-October dropped, 05 and 06-November appended, so the window is 19-October to 06-November. Every point is an official cash settlement from the Westmetall per-metal tables and English/German overviews, with the 06-November stock lines reconciled five-for-five against 05-November.")
ms['src']=["Westmetall - LME official cash settlements, per-metal tables and English/German overviews (05 and 06-November-2026 sessions)",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: 05-November cash $14,110.00, three-month $14,030.00, stock +6,425 t to 318,675 t. 06-NOVEMBER: cash $13,955.00, down $155.00 or 1.10%; three-month $13,780.00, down $250.00 or 1.78%. BACKWARDATION WIDENED to $175.00 from $80.00 while price fell (opposite directions). Stock fell 2,000 t to 316,675 t after six straight builds."),
 ("Nickel",NI[0],NI[1]," NICKEL: 05-November cash $16,100.00, three-month $16,265.00 (a +3.8% jump in three-month on the day). 06-NOVEMBER: cash $16,095.00, down $5.00 or 0.03%; three-month $16,280.00, up $15.00 or 0.09%. CONTANGO $185.00 from $165.00, still the widest carry on the board. Stock fell 1,074 t to 271,968 t."),
 ("Zinc",ZN[0],ZN[1]," ZINC: 05-November cash $3,877.00, three-month $3,842.00. 06-NOVEMBER: cash $3,759.00, down $118.00 or 3.04%; three-month $3,735.00, down $107.00 or 2.79% - the weakest metal on Friday. BACKWARDATION narrowed to $24.00 from $35.00 with price (same direction). Stock fell 1,350 t to 146,875 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: 05-November cash $1,866.50, three-month $1,899.00. 06-NOVEMBER: cash $1,857.00, down $9.50 or 0.51%; three-month $1,887.00, down $12.00 or 0.63%. CONTANGO $30.00 from $32.50. Stock fell 4,650 t to 304,000 t."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Friday 06-November official four of five base metals fell - zinc three-month -2.79%, copper -1.78%, aluminium -1.53%, lead -0.63%; nickel +0.09%. All five drew stock. Trading Economics (06-November) reports the dollar index up about 0.7% to 102.28 after October US payrolls rose 165,000 against a 65,000 forecast, Brent near $98 and down more than 12.5% on the week, and European gas down about 5.6% to near EUR 85.6/MWh. The LME euro fixing fell to 1.1169.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c-old[n]['avg']):,.2f} "+("above" if c>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='04-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][2:]+[["05-Nov",CU[2]],["06-Nov",CU[0]]]; assert len(i['hist'])==15
        i['val']="~13,780.00 (3M); 13,955.00 (cash) $/t"; i['ratio']="~13,955.00 $/t cash vs LME 3M 13,780.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled TWO SESSIONS to the FRIDAY 06-NOVEMBER-2026 session at $13,955.00 (05-November $14,110.00; 04-November $14,201.00). THE WINDOW ROLLED THIS RUN: 15 and 16-October dropped and 05 and 06-November appended, so the series is the last fifteen published official cash sessions, 19-October to 06-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall per-metal copper table and English/German overviews. "
                  "Copper structure for context: backwardation $175.00 on 06-November; stock 316,675 t (-2,000 t).")
s=d['inputs_summary']; assert s.startswith("UPDATE 06-NOVEMBER")
d['inputs_summary']=("UPDATE 07-NOVEMBER: Copper rolled two sessions to the Friday 06-November LME official cash of $13,955.00 (05-November $14,110.00), its fifteen-session window now 19-October to 06-November. No new monthly carbon settlement (due mid-November) or dated SMM fluoride, silicon or magnesium mark was located, so no other hist mark was appended. Energy kept falling: Brent near $98 and down more than 12.5% on the week, the steepest weekly drop since 2020; European gas down about 5.6% to near EUR 85.6/MWh, a two-week low, with EU storage 74% against a 90% five-year norm (Trading Economics, 06-November). LME alumina (Platts) printed $398.24/t for 05-November (AL Circle). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
pat=re.compile(r"the tariff leg of the US duty-paid premium is 0\.50 times the 04-November official cash of \$3,135\.00, or \$1,567\.50, UP \$26\.50 on the day\. Against a US Midwest duty-paid premium of \$2,403/t that leaves a residual market leg of \$835\.50, so 65\.2%")
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 06-November official cash of $3,117.00, or ${tl:,.2f}, DOWN $9.00 against the 04-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED FRIDAY 06-NOVEMBER-2026 (LME BOARD CARRIED ON THE WEDNESDAY 04-NOVEMBER OFFICIAL - THE 05-NOVEMBER OFFICIAL WAS NOT YET AVAILABLE FROM THE PUBLIC SOURCE)."
NEWC="COMPILED SATURDAY 07-NOVEMBER-2026 (LME BOARD ON THE FRIDAY 06-NOVEMBER OFFICIAL, THE LAST TRADING SESSION; NO RING ON SATURDAY)."
n=0; nc=0
for p in d['premiums']:
    s2,k=pat.subn(NEWT,p['src']); n+=k; nc+=s2.count(OLDC); p['src']=s2.replace(OLDC,NEWC)
assert n==len(d['premiums']) and nc==len(d['premiums']),(n,nc)
ALU=398.24; ra=ALU/m3*100; na=0
o="THE RATIO: LME Alumina at $397.00/t against the 04-November aluminium three-month of $3,074.00 is 12.91%"
o2="THE LME ALUMINA (PLATTS) ROW IS CARRIED at AL Circle's $397.00/t print for the 02-November session (no newer dated LME alumina print located on 05 or 06-November);"
n2=f"THE LME ALUMINA (PLATTS) ROW IS UPDATED THIS RUN to AL Circle's $398.24/t print for the 05-November session ({S_AC}), up from $397.00/t on 02-November. EARLIER NOTE:"
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    if o in s: na+=1
    s=s.replace(o2,n2+" the row was carried at $397.00/t for 02-November on 05 and 06-November;",1)
    a['src']=s.replace(o,f"THE RATIO: LME Alumina at ${ALU:,.2f}/t against the 06-November aluminium three-month of $3,050.00 is {ra:.2f}%")
    if a['name'].startswith('LME Alumina'): a['val']=ALU; a['asof']='05-Nov-26'; a['trend']='up'
assert na==len(d['alumina']),na

d['lme_commentary']=("A ROUND TRIP ON THE WEEK, WITH THE STRUCTURE STILL TIGHTENING. Two officials were added this run. Thursday 05-November lifted three-month $23.50 to $3,097.50 - a settled close above 3,077 and the 3,084.00 rebound high - with cash $3,160.00 and a $62.50 backwardation. Friday 06-November then gave it all back: cash $3,117.00 (-$43.00) and three-month $3,050.00 (-$47.50), back below 3,061.5 on the weekly close, though still $25.50 above the 3,024.50 bear trigger. Under the pre-registered rules the bull gained five points on Thursday and returned them on Friday, so weights end the week at 15/45/40. "
 "Structure went the other way: the backwardation widened to $67.00, the widest since mid-September, visible stock fell 875 t to a new low of 227,600 t, and cancelled warrants rose to 17,375 t on 05-November (AL Circle) - spread and price moved in OPPOSITE directions on Friday. "
 "The Friday drop was broad - zinc three-month -2.79%, copper -1.78%, aluminium -1.53%, lead -0.63%, nickel flat - as the dollar index rose about 0.7% to 102.28 after October US payrolls of 165,000 beat a 65,000 forecast, and Brent and European gas extended steep weekly losses on hopes of a US-Iran diplomatic track (Trading Economics, 06-November). "
 f"On the week three-month is down $30.00 (from $3,080.00 on 30-October). October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" its October mean.")
d['net_read']=("NET: NEUTRAL - PRICE SOFT, STRUCTURE TIGHT. Supportive: a $67.00 backwardation (seventeenth straight, sixth above $15.00), visible LME stock at a new low of 227,600 t with cancelled warrants rising, and Thursday's brief settled close above 3,077. "
 "Against: the weekly close at $3,050.00 is below both 3,061.5 and 3,077; a firmer dollar after strong US payrolls; energy collapsing (Brent down more than 12.5% on the week, European gas at a two-week low), which lowers the smelter cost floor; Gulf and Icelandic restarts (Century's Grundartangi Line 2) adding ex-China supply.")
d['bottom_line']=("BOTTOM LINE: the week ended with LME aluminium three-month at $3,050.00 on the Friday 06-November official, down $47.50 on the day and $30.00 on the week, after Thursday briefly settled above 3,077 at $3,097.50. The backwardation nevertheless widened to $67.00 and visible stock fell to a new low of 227,600 t, so prompt tightness and outright price are diverging. "
 "Weights end at 15% bull / 45% base / 40% bear: the bull gained five points on Thursday's pre-registered close above 3,077 and returned them on Friday's settled close below 3,061.5. Re-crediting the bull needs another settled close above 3,077 with the backwardation beyond $15.00; a close below 3,024.50, or a contango beyond $24.50, adds bear weight. Daily Elliott invalidation 3,289. No ring on Saturday - next official Monday 09-November.")
c2=d['commercial']
for a,b in [("FIRST, PRICE AND PROMPT PREMIUM ROSE TOGETHER: a $61.00 backwardation on 04-November, wider than $40.00 as cash rose $53.00 and three-month $32.00 - a fourth print above the $15.00 reversal condition, so nearby metal is valued clearly over forward metal and there is no carry reward for deferring purchases; the outright price is now only $3.00 below 3,077.",
             "FIRST, PROMPT PREMIUM UP, PRICE DOWN: a $67.00 backwardation on 06-November, wider than $62.50 even as cash fell $43.00 and three-month $47.50 - a sixth print above the $15.00 reversal condition, so nearby metal is valued clearly over forward metal and there is no carry reward for deferring purchases; the outright price closed the week $27.00 below 3,077 after briefly settling above it on Thursday."),
 ("is $1,567.50 on 04-November cash, 65.2% of the $2,403/t premium",f"is ${tl:,.2f} on 06-November cash, {share:.1f}% of the $2,403/t premium"),
 ("the 04-November official took three-month to $3,074.00, back above 3,061.5 but $3.00 below 3,077, $79.50 above the 2,994.50 settled low; energy collapsed (Brent about -9% in one session to near $94, European gas near EUR 86/MWh, Trading Economics 05-November); the dollar index sits at a five-week low near 101.3; December-hike odds about 77%; IAI data show Q3 global primary output +2.1% q/q (AL Circle, 04-November);",
  "the 06-November official took three-month to $3,050.00 for the weekly close, below 3,061.5 and 3,077, $55.50 above the 2,994.50 settled low; energy fell further (Brent near $98 and down more than 12.5% on the week, European gas near EUR 85.6/MWh, Trading Economics 06-November); the dollar index rose to 102.28 after October payrolls of 165,000 beat forecasts; December-hike odds roughly 68-71%; Century Aluminum's Q3 adjusted EBITDA was $331.6m with Grundartangi Line 2 restarted (05-November release); IAI data show Q3 global primary output +2.1% q/q (AL Circle, 04-November);")]:
    assert a in c2,a[:60]; c2=c2.replace(a,b)
d['commercial']=c2

SC={'Bull':'15%','Base':'45%','Bear':'40%'}
for s in d['outlook']['scenarios']:
    t=s['drivers']; assert t.startswith("HELD 06-NOVEMBER at 15/45/40 ON A CARRIED BOARD")
    s['prob']=SC[s['case']]
    s['drivers']=("NET UNCHANGED 07-NOVEMBER at 15/45/40 AFTER TWO RULE-BASED MOVES. (1) THURSDAY 05-NOVEMBER: three-month settled $3,097.50, ABOVE 3,077, with a $62.50 backwardation beyond $15.00 - the pre-registered condition - so five points moved from bear to bull (20/45/35). (2) FRIDAY 06-NOVEMBER (weekly close): three-month settled $3,050.00, BELOW 3,061.5 - the pre-registered reversal for the 20/45/35 state - so the five points returned to bear (15/45/40); the $67.00 backwardation and new stock low do not override the price rule. $25.50 above the 3,024.50 bear trigger, so no further bear weight. PRE-REGISTERED NEXT: a settled close above 3,077 with the backwardation beyond $15.00 returns five points to bull; a settled close below 3,024.50 or a contango beyond $24.50 adds five to bear. ")+t
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

RK=d['outlook']['risks']; hit=0
for r in RK:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 07-NOVEMBER: the 05 and 06-November officials printed BACKWARDATIONS of $62.50 and $67.00, a sixth session above $15.00 and the widest since mid-September. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 07-NOVEMBER: LME stock fell 275 t on 05-November and 875 t on 06-November to a new low of 227,600 t, a thirteenth straight draw; cancelled warrants rose 2,200 t to 17,375 t on 05-November (AL Circle). Trend held at FLAT: the pace remains modest."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 07-NOVEMBER: Brent near $98, down more than 12.5% on the week - the steepest weekly drop since 2020 - and TTF down about 5.6% to near EUR 85.6/MWh, a two-week low, on hopes of a US-Iran diplomatic track (Trading Economics, 06-November). Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 07-NOVEMBER: Straits Daily Brief - still effectively closed; latest lagged PortWatch count 2 transits on 25-October vs 85/day; one seafarer killed in a suspected missile attack on the tanker MT Velos Sapphire in the Gulf (gCaptain, MarineLink, 06-November); IRGC claims two tankers hit mines (Iranian state media, UNCONFIRMED); Iran reportedly told Russia the strait stays closed until the US meets seven conditions; 140 vessels holding in the watch box. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 07-NOVEMBER: October payrolls rose 165,000 against a 65,000 forecast and unemployment fell to 4.1%; the dollar index rose about 0.7% to 102.28; Trading Economics cites December-hike odds of roughly 68-71% (sections differ) (06-November). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE EX-CHINA RESTART PIPELINE'):
        r['risk']+=" UPDATE 07-NOVEMBER: Century Aluminum's Q3 release (05-November) attributes higher sales to the restart of Line 2 at Grundartangi, Iceland, with shipments up to 173,483 t from 130,632 t in Q2. Trend held at UP."; r['trend']='up'; hit+=1
assert hit==6,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Fri 06-Nov':
        hc+=1; cat['date']='Daily, from Mon 09-Nov'
        cat['event']=("THE WEEK CLOSED AT $3,050.00 (06-NOVEMBER OFFICIAL), below 3,061.5 and 3,077, after Thursday's $3,097.50 briefly cleared 3,077 - weights 20/45/35 on Thursday, back to 15/45/40 on Friday. NEXT (from Monday 09-November): a settled close above 3,077 with the backwardation beyond $15.00 (last $67.00) returns five points to bull; resistance 3,097.5 then 3,110 and the 3,148.5 wave (iv) high. A settled close below 3,042.00 weakens the daily base count; below 3,024.50 adds bear weight; below about 2,977.5 forces a re-count toward 2,894. Invalidation 3,289.")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"SATURDAY 07-NOVEMBER ON THE FRIDAY 06-NOVEMBER OFFICIAL (two sessions added): three-month rose to $3,097.50 on Thursday - a settled close above 3,077 that moved five points to bull - then fell $47.50 to $3,050.00 on Friday, below 3,061.5 on the weekly close, returning them; weights end at 15/45/40. Structure diverged from price: the backwardation widened to $67.00 and visible stock fell to a new low of 227,600 t. Friday's broad metals sell-off (zinc -2.8%, copper -1.8%) came with a firmer dollar after strong US payrolls and a further slide in energy (Brent down more than 12.5% on the week). Watch Monday: whether 3,042-3,024.50 holds, and whether the backwardation stays above $15.")

EWS=("REVIEWED 07-NOVEMBER ON THE 05 AND 06-NOVEMBER OFFICIALS: Thursday settled three-month at 3,097.50, ABOVE the 3,084.00 wave A/1 high - the base case's confirmation that wave C/3 was under way - but Friday fell back to 3,050.00, holding $8.00 above the 3,042.00 B/2 low. The sequence 2,994.50 / ... / 3,084.00 / 3,064.00 / 3,080.00 / 3,060.00 / 3,042.00 / 3,074.00 / 3,097.50 / 3,050.00 remains overlapping, which fits a developing (i)-(ii) of C/3 or a corrective bounce equally. Count NOT re-labelled (no invalidation broke). Base case trimmed to about 50% (from 55%): 3,042.00 is the B/2 low, 3,097.50 a first leg of C/3, and a settled close back above 3,097.50 targets 3,110 then the 3,148.5 wave (iv) high. Alternate about 50%: the rebound from 2,994.50 is complete or nearly so; a settled close below 3,042.00 would favour it and below 2,977.5 force a re-count toward the 2,894 weekly 61.8%. Invalidation 3,289; confidence low. ")
st=d['ew']['short_term']['writeup']; assert st.startswith("REVIEWED 06-NOVEMBER")
k=st.find("REVIEWED 05-NOVEMBER"); assert k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; assert lt.startswith("REVIEWED 06-NOVEMBER")
k=lt.find("REVIEWED 05-NOVEMBER"); assert k>0
d['ew']['long_term']['writeup']=("REVIEWED 07-NOVEMBER (WEEKLY CLOSE): the week ending 06-November closed at 3,050.00, down $30.00, BELOW both the 3,061.5 July low and the 3,077 50% retracement, after an intra-week official high of 3,097.50 failed to hold. As pre-registered, a weekly close below 3,061.5 REINFORCES the weekly base case: the corrective count toward the 61.8% retracement at 2,894, which would lose preference only on a weekly close above 3,110. Alternate trimmed to about 35% (from 40%): the 2,994.50 low completed the weekly correction, supported by the steepening backwardation and record-low stock. Confidence moderate. ")+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="98.0",day="about $97.8-98.3 on 06-November (Trading Economics; sections differ: header $98.32 +0.03%, stats $97.76 -0.54%); down more than 12.5% on the week, the steepest weekly drop since 2020",
 note="REFRESHED SATURDAY 07-NOVEMBER-2026 (Trading Economics, 06-November): Brent held near $98 as traders weighed renewed US-Iran escalation risk against hopes of a diplomatic deal; Iran reportedly sent a nuclear proposal to Washington via Qatar; UKMTO data show vessel attacks continuing at a near-record pace. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="85.6",day="about EUR 85.6-86.8/MWh on 06-November (Trading Economics; sections differ), about -4.3% to -5.6%, a two-week low; down about 15% on the week",
 note="REFRESHED SATURDAY 07-NOVEMBER-2026 (Trading Economics): TTF fell about 5% after Qatar's Emir discussed de-escalation with President Trump; EU storage 74% against a 90% five-year seasonal average, Germany below 61%; Middle East LNG disruption (about a fifth of global supply) keeps prices far above pre-war levels. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="102.28",day="about 102.28 on 06-November (Trading Economics), +0.72%",
 note="REFRESHED SATURDAY 07-NOVEMBER-2026 (Trading Economics): October nonfarm payrolls rose 165,000 against a 65,000 forecast and unemployment eased to 4.1%; December 25bp-hike odds cited at roughly 68-71% in different sections. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.11690',day="LME fixing on 06-November, down from 1.12260 on 05-November",note="REFRESHED SATURDAY 07-NOVEMBER-2026 to the 06-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 06-NOVEMBER-2026 LME OFFICIAL. This Saturday run falls on a day with no LME ring, so the last trading session's official is the correct figure to carry until Monday 09-November. The board ROLLED TWO SESSIONS this run because the 06-November run had to carry 04-November; the Thursday 05-November official (cash 3,160.00, three-month 3,097.50, stock 228,475) is recorded in the series and text. The Trading Economics aluminium reference ($3,065.60, +0.13% for 06-November) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (07-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 06-November session; all five per-metal daily tables show 06-November as the newest row with NO later row, so the board is complete rather than lagging. AL Circle's 05-November LME report (cash $3,160, three-month $3,097.50, opening stock 228,750 t) independently corroborates the 05-November session.")
C[2]=("COMPENSATING CHECKS: the per-metal aluminium table's 12-October to 04-November rows match the stored series exactly; the overviews' prior-day FX column (MTLE 1.12260) is the 05-November fixing.")
C[3]=("ALL FIVE STOCK LINES RECONCILE 06-November against 05-November via the pages' change column: aluminium -875 to 227,600; copper -2,000 to 316,675; nickel -1,074 to 271,968; zinc -1,350 to 146,875; lead -4,650 to 304,000.")
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (06-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (five sessions, 02-06 November) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,050.00; the stock chart axis floor was LOWERED THIS RUN to 200,000 t (from 210,000) to keep headroom below visible stock of 227,600 t; it is re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,117.00 against three-month $3,050.00 is therefore a $67.00 BACKWARDATION, wider than $62.50 on 05-November - on Friday the spread and the flat price moved in OPPOSITE directions (spread wider, price lower); on Thursday both firmed together."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=cv.replace("the tariff leg is 0.50 times the 04-November official cash of $3,135.00, or $1,567.50, leaving a $835.50 residual market leg out of the $2,403/t US duty-paid premium (65.2% policy arithmetic)",
                    f"the tariff leg is 0.50 times the 06-November official cash of $3,117.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic)")
        assert C[i]!=cv; hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $98.0), the dollar index (about 102.28) and TTF (about EUR 85.6/MWh) are Trading Economics readings for 06-November; Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages again showed different levels in different sections (Brent $98.32 vs $97.76; TTF 85.59 vs 86.79; hike odds 68% vs 71%), so levels are approximate. The US ten-year row is CARRIED from 30-October (not re-fetched). The Straits Daily Brief (07-November) shows Brent $97.76 (-0.54%); the brief labels its ticker as AI-assisted. EUR/USD is the 06-November LME fixing, the same session as the board."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 07-NOVEMBER: no authorised fetch was blocked (Westmetall EN and DE overviews plus all five per-metal tables, Trading Economics aluminium/Brent/TTF/dollar, AL Circle, news.metal.com and the Straits Daily Brief all fetched). news.metal.com showed no SHFE settlement or Chinese social-inventory figure for 06/07-November, so none is used this run. Century Aluminum's Q3 figures were taken from its SEC-filed earnings release, located by web search. A search for Q1-2027 Japanese premium offers found none - Q1 stays unpriced. Iranian mine claims are cited as UNCONFIRMED per the brief."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        C[i]=("PEER EARNINGS: TWO NEW PEER RESULTS ADDED THIS RUN (07-NOVEMBER) - CENTURY ALUMINUM Q3-2026 (SEC 8-K exhibit, 05-November) and NOVELIS Q2 FY27 (AL Circle, 06-November) - and both earnings_history strips were REFRESHED with the new quarter (Century adjusted EPS $2.58; Novelis adjusted EBITDA $508m), dropping their oldest point; no other company was back-filled. "+cv.split("NO COMPANY WAS BACK-FILLED THIS RUN. ",1)[-1]); hit+=1
assert hit==4,hit

d['so_what']={"line":"Aluminium round-tripped the week: Thursday's LME official briefly cleared $3,077 at $3,097.50, but Friday's fell $47.50 to a $3,050 weekly close as a strong US jobs report lifted the dollar - even as the cash premium over three-month widened to $67 and LME stock hit another low.",
 "points":[
 "WHAT MOVED: two officials were added. Thursday 05-November: three-month $3,097.50 (+$23.50), cash $3,160.00. Friday 06-November: three-month $3,050.00 (-$47.50, -1.53%), cash $3,117.00 (-$43.00); down $30.00 on the week. No ring on Saturday.",
 "WHY: Friday's sell-off was broad (zinc -2.8%, copper -1.8%, aluminium -1.5%) as October US payrolls of 165,000 beat a 65,000 forecast and the dollar index rose about 0.7% to 102.28; Brent (down more than 12.5% on the week) and European gas (two-week low) kept falling on US-Iran diplomacy hopes, lowering the smelter cost floor (Trading Economics).",
 "THE DIVERGENCE: prompt LME metal keeps tightening - a $67.00 backwardation (widest since mid-September), stock down to 227,600 t, cancelled warrants up to 17,375 t (AL Circle) - while the outright price weakens. Scenario weights moved to 20/45/35 on Thursday and back to 15/45/40 on Friday under the published rules.",
 "WHAT TO WATCH: Monday's official versus $3,042-3,024.50 support and $3,077 resistance; whether the backwardation stays above $15; Hormuz (a fatal tanker attack reported 06-November; Iranian mine claims unconfirmed); first Q1-2027 Japanese premium offers (none public yet)."]}

d['feed']=([
 {"when":"Sat 07-Nov","impact":"Bearish","text":"BOARD ROLLED TO THE FRIDAY 06-NOVEMBER OFFICIAL: three-month $3,050.00 (-$47.50), cash $3,117.00 (-$43.00) - weekly close below 3,061.5; weights back to 15/45/40."},
 {"when":"Thu 05-Nov","impact":"Bullish","text":"05-NOVEMBER OFFICIAL: three-month $3,097.50 (+$23.50), cash $3,160.00 - settled close above 3,077; weights briefly 20/45/35."},
 {"when":"Fri 06-Nov","impact":"Bullish","text":"STRUCTURE TIGHTENS: backwardation $67.00 (from $62.50), widest since mid-September; LME stock -875 t to a new low of 227,600 t; cancelled warrants 17,375 t (05-Nov)."},
 {"when":"Fri 06-Nov","impact":"Bearish","text":"US PAYROLLS +165,000 vs 65,000 forecast; dollar index +0.7% to 102.28 (Trading Economics). Base metals broadly lower."},
 {"when":"Fri 06-Nov","impact":"Bearish (cost)","text":"ENERGY: Brent near $98, down >12.5% on the week (steepest since 2020); TTF -5.6% to ~EUR 85.6/MWh (Trading Economics)."},
 {"when":"Fri 06-Nov","impact":"Mixed","text":"HORMUZ: one seafarer killed in suspected missile attack on tanker Velos Sapphire (gCaptain/MarineLink); IRGC mine claims UNCONFIRMED."},
 {"when":"Thu 05-Nov","impact":"Bullish (margin)","text":"CENTURY Q3: adjusted EBITDA $331.6m, adjusted EPS $2.58; Grundartangi Line 2 restarted; Q4 guide $275-300m."},
 {"when":"Fri 06-Nov","impact":"Mixed","text":"NOVELIS Q2 FY27: net sales $5.9bn (+25%), adjusted EBITDA $508m (+20%), shipments 919 kt (-2%) (AL Circle)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM GIVES BACK THURSDAY'S BREAKOUT. The Friday 06-November official settled cash at $3,117.00 (-1.36%) and three-month at $3,050.00 (-1.53%), a weekly close below 3,061.5 and 3,077, after Thursday's official lifted three-month to $3,097.50 and cash to $3,160.00. Visible stock fell 875 t to a new low of 227,600 t. Friday board: zinc three-month -2.79%, copper -1.78%, aluminium -1.53%, lead -0.63%, nickel +0.09%; all five drew stock."},
 {"theme":"LME","horizon":"0-1 month","impact":"Bullish","url":S_AC,
  "headline":"BACKWARDATION WIDENS TO $67 WHILE PRICE FALLS: the cash-to-three-month spread rose to $62.50 on 05-November and $67.00 on 06-November, the widest since mid-September and a seventeenth straight backwardation; AL Circle reports cancelled warrants rose 2,200 t to 17,375 t on 05-November with live warrants 211,100 t. READ: prompt LME tightness and outright price are diverging."},
 {"theme":"Macro","horizon":"0-2 months","impact":"Bearish","url":S_TD,
  "headline":"STRONG US JOBS LIFT THE DOLLAR (Trading Economics, 06-November): October nonfarm payrolls rose 165,000, more than double the 65,000 forecast, and unemployment eased to 4.1%; the dollar index rose about 0.7% to 102.28. December Fed-hike odds are cited at roughly 68-71%. READ: a firmer dollar weighs on dollar-priced metals."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bearish (cost)","url":S_BR,
  "headline":"BRENT'S STEEPEST WEEKLY DROP SINCE 2020 (Trading Economics, 06-November): Brent near $98, down more than 12.5% on the week, on hopes of a US-Iran diplomatic breakthrough; Iran reportedly sent a nuclear proposal to Washington via Qatar but still wants the naval blockade lifted before fully reopening Hormuz. European gas fell about 5.6% to near EUR 85.6/MWh, a two-week low; EU storage 74% vs a 90% norm."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Mixed","url":S_ST,
  "headline":"HORMUZ STILL CLOSED; FATAL TANKER ATTACK (Straits Daily Brief, 07-November): latest lagged PortWatch count 2 transits on 25-October vs 85/day; one seafarer killed in a suspected missile attack on the unladen products tanker MT Velos Sapphire bound for Bahrain (gCaptain, MarineLink); IRGC claims two tankers hit mines (Iranian state media, UNCONFIRMED); an explosion reported on a tanker near Khasab (Arab News); Iran reportedly told Russia the strait stays closed until the US meets seven conditions; 140 vessels holding."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Bullish (margin)","url":S_CX,
  "headline":"CENTURY ALUMINUM Q3-2026 (earnings release, 05-November): net sales $961.2m (+$209.1m q/q), net income $302.6m, adjusted EPS $2.58 (Q2 $2.46), adjusted EBITDA attributable $331.6m (Q2 $326.9m), shipments 173,483 t (Q2 130,632 t) on the Grundartangi Line 2 restart; Q4 adjusted EBITDA guided $275-300m. READ: US tariff-inflated premiums keep converting to cash, but guidance points to a softer Q4."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Mixed","url":S_NV,
  "headline":"NOVELIS Q2 FY27 (AL Circle, 06-November): net sales $5.9bn (+25% y/y), net income attributable $210m (+29%), adjusted EBITDA $508m (+20%), rolled-product shipments 919,000 t (-2%). READ: higher metal prices lift revenue faster than volume; downstream demand is flat."},
 {"theme":"Alumina","horizon":"0-6 months","impact":"Mixed","url":S_AO,
  "headline":"GLOBAL ALUMINA OUTPUT STILL BELOW 2025 (AL Circle on IAI data, 06-November): Q3-2026 39.396 Mt (+5.54% q/q, -0.70% y/y); January-September 114.625 Mt (-0.29%); China's share up to 60.19%. LME alumina (Platts) $398.24/t for 05-November (AL Circle)."},
 {"theme":"Supply","horizon":"0-12 months","impact":"Mixed","url":S_BB,
  "headline":"BELL BAY WORKFORCE REVIEW (AL Circle, 06-November): Rio Tinto's Tasmanian smelter is offering redundancies for up to 10 non-frontline roles a month after the AUD 200m government support package; about 550 FTE retained; Rio calls it routine planning. No change to the 2031 operating horizon."},
 {"theme":"Deals","horizon":"2027","impact":"Mixed","url":S_S3,
  "headline":"SOUTH32 KEEPS JUNE 2027 TIMELINE for Alcoa's acquisition of its aluminium assets (AL Circle, 06-November)."},
]+d['news']
d['news']=d['news'][:20]

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 06-NOVEMBER: no newer public disclosure","REVIEWED 07-NOVEMBER: no newer public disclosure").replace("REVIEWED 06-NOVEMBER. NO NEW DATED","REVIEWED 07-NOVEMBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('Rio Tinto'):
        p['update']="UPDATED 07-NOVEMBER (AL Circle, 06-November): Bell Bay is reviewing its workforce and offering redundancies for up to 10 non-frontline roles; about 550 FTE retained; Rio Tinto describes it as routine operational planning - no change to the secured-to-2031 status ("+S_BB+"). "+p['update']
    if p['name'].startswith('Alcoa'):
        p['update']="UPDATED 07-NOVEMBER: AL Circle (06-November) reports South32 maintains a June 2027 timeline for Alcoa's acquisition of its aluminium assets ("+S_S3+"). "+p['update']
    if p['name'].startswith('EGA') and not p['update'].startswith("REVIEWED 07-NOVEMBER"):
        p['update']="REVIEWED 07-NOVEMBER: no newer EGA release located; latest company figure remains 631 of 1,262 cells (21-October), full output targeted Q1-2027. "+p['update']
    if p['name'].startswith('China operators'):
        p['update']="REVIEWED 07-NOVEMBER: no newer SMM social-inventory print located on news.metal.com this run; last 377,000 t ingot / 73,500 t billet (06-November). "+p['update']

# Earnings: two new rows
d['earnings']=[
 {"company":"Century Aluminum (CENX)","group":"Aluminum producer (US)","period":"Q3 2026 (Jul-Sep)","reported":"05 Nov 2026","reported_iso":"2026-11-05","sentiment":"Positive",
  "headline":"Q3-2026: net sales $961.2m (+$209.1m q/q from $752.1m); net income attributable $302.6m, diluted EPS $2.89; adjusted net income $271.6m, adjusted EPS $2.58 (Q2 $2.46); adjusted EBITDA attributable $331.6m (Q2 $326.9m), inside the $325-345m guide; shipments 173,483 t (Q2 130,632 t). Q4-2026 adjusted EBITDA guided $275-300m.",
  "readthrough":"VOLUME DROVE THE QUARTER, NOT MARGIN: shipments rose about a third on the restart of Line 2 at Grundartangi, Iceland, but adjusted EBITDA rose only about 1% q/q, and the company cited weaker power-price realisation in extreme heat. The lower Q4 guide is consistent with the softer LME and Japanese premium reset seen since the summer peak. Source: company earnings release filed with the SEC.",
  "eps":2.58,"revenue_bn":0.9612,"yoy_pct":None,"url":S_CX},
 {"company":"Novelis (NVL)","group":"Downstream / rolled products","period":"Q2 FY27 (Jul-Sep 2026)","reported":"06 Nov 2026","reported_iso":"2026-11-06","sentiment":"Positive (mixed)",
  "headline":"Q2 FY27: net sales $5.9bn (+25% y/y from $4.7bn); net income attributable to common shareholder $210m (+29% from $163m); adjusted EBITDA $508m (+20% y/y); rolled-product shipments 919,000 t (-2%).",
  "readthrough":"PRICE, NOT VOLUME: revenue rose with the metal price while shipments slipped 2%, so the downstream demand signal is flat. Adjusted EBITDA eased from $516m in Q1 FY27. Source: AL Circle report of the company's results.",
  "eps":None,"revenue_bn":5.9,"yoy_pct":20.0,"url":S_NV},
]+d['earnings']
d['earnings_note']=("CENTURY ALUMINUM REPORTED (added 07-November): Q3-2026 adjusted EBITDA $331.6m, adjusted EPS $2.58, shipments 173,483 t on the Grundartangi Line 2 restart; Q4 guide $275-300m (SEC 8-K exhibit, 05-November). NOVELIS REPORTED (added 07-November): Q2 FY27 net sales $5.9bn (+25%), adjusted EBITDA $508m (+20%), shipments -2% (AL Circle, 06-November). ")+d['earnings_note']
EH=d['earnings_history']
assert EH['CENX']['points'][-1]==['Q2-26',2.46]
EH['CENX']['points']=EH['CENX']['points'][1:]+[['Q3-26',2.58]]
EH['CENX']['src']=["Century Aluminum - Q3-2026 earnings release (8-K Ex.99.1, 05-Nov-2026): adjusted EPS $2.58 (Q2-26 $2.46, Q1-26 $1.63, Q4-25 $1.25 from prior company releases). REFRESHED 07-NOVEMBER with the Q3-2026 print; the oldest point (Q2-25) dropped. Exact reported figures only; no quarter is interpolated.",S_CX]
assert EH['NVL']['points'][-1]==['Q1-FY27',516]
EH['NVL']['points']=EH['NVL']['points'][1:]+[['Q2-FY27',508]]
EH['NVL']['src']=["Novelis adjusted EBITDA: Q3-FY26 $348m, Q4-FY26 $459m, Q1-FY27 $516m (company releases); Q2-FY27 $508m to 30-Sep-2026 (AL Circle, 06-Nov-2026, reporting the company's results). REFRESHED 07-NOVEMBER; oldest point (Q2-FY26) dropped. Exact reported figures only.",S_NV]

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 05 and 06-Nov-2026 sessions (EN and DE overviews agree; all five per-metal tables; stock lines reconciled 06 vs 05-Nov)",W])
for x in ([L_AC,S_AC],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_ST,S_ST],[L_CX,S_CX],[L_CXA,S_CXA],[L_NV,S_NV],[L_AO,S_AO],[L_BB,S_BB],[L_S3,S_S3]): d['sources'].append(x)
for x in ([L_BR,S_BR],[L_TD,S_TD],[L_ST,S_ST],[L_AC,S_AC]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-11-04'
ph['rows'][-1]=['2026-11-06',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2))
