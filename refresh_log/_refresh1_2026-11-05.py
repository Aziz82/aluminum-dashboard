# Daily data refresh - 2026-11-05 (THURSDAY, ~02:40 UTC, BEFORE the ring). Board ROLLED to the WEDNESDAY 04-Nov LME official.
# Westmetall cache-busted EN + DE overviews both show 04-Nov and agree (Al cash 3,135 / 3M 3,074 / stock 228,750 -725; MTLE 1.12640 vs 1.11820 prior);
# Al per-metal table newest row = 04-Nov. Stock change column reconciles vs 03-Nov for all five metals (Cu +2,600; Ni -2,262; Zn -3,900; Pb -650).
# 3M +32 to 3,074: $3 SHORT of 3,077 and above 3,024.50 => no pre-registered trigger; weights HELD 15/45/40. Backwardation WIDENED $40 -> $61 WITH price (same direction).
import json,re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-05'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum 3,069.85 (+0.82%) on 04-Nov-2026"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent near $94 after ~9% slide, two-month low (05-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~101.3, five-week low after midterms (05-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 85.7/MWh (05-Nov-2026)"
S_ST="https://straits.live/briefs/2026-11-05"; L_ST="Straits Daily Brief - Strait of Hormuz, 05-Nov-2026"
S_IAI="https://www.alcircle.com/news/global-primary-aluminium-output-rebounds-2-1-in-q3-2026-despite-september-slump-is-supply-deficit-easing-121830"; L_IAI="AL Circle - Global primary aluminium output +2.1% q/q in Q3-2026 (IAI data, 04-Nov-2026)"
S_VE="https://www.alcircle.com/news/venezuela-eyes-second-primary-aluminum-shipment-to-us-as-trade-links-reopen-121835"; L_VE="AL Circle - Venezuela eyes second primary aluminium shipment to US (04-Nov-2026)"
S_SA="https://www.metal.com/en/newscontent/104205676-30000-mt-alumina-traded-at-397mt-fob-western-australia-for-december-shipment"; L_SA="SMM - 30,000 mt alumina traded at $397/mt FOB Western Australia, December shipment (05-Nov-2026)"
S_SM="https://www.metal.com/en/newscontent/104205516-central-china-aluminum-market-sees-stable-premiums-improved-trading-sentiment-boosts-buying-interest"; L_SM="SMM - Central China aluminium: stable premiums, discount RMB 80-100/t to SHFE November (05-Nov-2026)"

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3082.0 and B['LME 3-month']['cur']==3042.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
cash,prev_c,m3,prev_m,stk,prev_s=3135.0,3082.0,3074.0,3042.0,228750,229475
spr=cash-m3; assert spr==61.0 and prev_s-725==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED THURSDAY 05-NOVEMBER-2026 ABOUT 02:40 LONDON, BEFORE THE RING, SO THE BOARD IS THE WEDNESDAY 04-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION; Thursday's official prints 13:20 London. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched this run and AGREE on the full 04-November official for all metals with stocks and FX fixings (EUR/USD MTLE 1.12640); their prior-day FX column (MTLE 1.11820) matches the verified 03-November board, and the per-metal aluminium table's newest row is 04-November; "
 "(2) ALL FIVE STOCK LINES RECONCILE against 03-November via the pages' change column: aluminium 229,475 less 725 to 228,750; copper 309,650 plus 2,600 to 312,250; nickel 277,854 less 2,262 to 275,592; zinc 154,350 less 3,900 to 150,450; lead 310,900 less 650 to 310,250. "
 "The whole board sits on ONE UNIFORM SESSION (04-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" CASH SETTLED $3,135.00 ON THE 04-NOVEMBER OFFICIAL, UP $53.00 OR 1.72% FROM $3,082.00. THREE-MONTH SETTLED $3,074.00, UP $32.00 OR 1.05% FROM $3,042.00 - back above 3,061.5 but $3.00 SHORT of 3,077, $49.50 above the 3,024.50 bear-trigger level, $79.50 above the 2,994.50 settled low of 15-October and $63.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION WIDENED SHARPLY TO $61.00 FROM $40.00 because cash rose more than three-month - THIS TIME SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION (both firmer), after two sessions of divergence - a fifteenth straight backwardation, the widest since mid-September and a fourth session above the $15.00 condition. "
 "VISIBLE LME STOCK FELL 725 t TO 228,750 t, another new series low and an eleventh straight draw. The Trading Economics aluminium reference showed $3,069.85 (+0.82%) for 04-November - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,135.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,074.0","pos":True,"delta":VER+AL+" THREE-MONTH IS $3.00 BELOW THE 3,077 WEEKLY 50% RETRACEMENT, $12.50 above the 3,061.5 July low, $74.50 beneath the 3,148.5 wave (iv) high and $215.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a fourteenth session."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+61.0","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,135.00 against three-month $3,074.00 is a $61.00 BACKWARDATION, WIDER than 03-November's $40.00 as cash rose $53.00 and three-month $32.00 - SPREAD AND PRICE MOVED IN THE SAME DIRECTION. It stays above the published $15.00 reversal condition for a fourth session, the widest print since mid-September and a fifteenth straight backwardation; a contango beyond $24.50 would reverse the structural signal. The October mean spread was $"+f"{oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"228,750","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 725 t TO 228,750 t, another new series low and an eleventh straight draw. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":prev_c,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it."},
 {"name":"LME 3-month","cur":m3,"prev":prev_m,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $3,074.00, UP $32.00 - $3.00 below 3,077, $12.50 above 3,061.5 and $49.50 above 3,024.50; $63.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":prev_s,"avg":oct_s,"note":VER+f" STOCK DOWN 725 t TO 228,750 t, another new series low. AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":40.0,"avg":oct_sp,"note":VER+f" A $61.00 BACKWARDATION, WIDER THAN 03-NOVEMBER'S $40.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. Cash rose $53.00 and three-month $32.00, so structure and price firmed TOGETHER. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October at $34.00, held 02-November at $35.00, 03-November at $40.00 and 04-November at $61.00."},
 {"name":"EUR/USD LME fixing","cur":1.1264,"prev":1.1182,"avg":1.1465,"note":VER+" THE LME EURO FIXING ROSE TO 1.12640 FROM 1.11820 at the Wednesday ring as the dollar weakened. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (04-Nov official)","price":"3,135.0","basis":"THE 04-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,135.00, UP $53.00 OR 1.72%. Next official Thursday 05-November 13:20 London."},
 {"tenor":"3-month (04-Nov official)","price":"3,074.0","basis":"THE 04-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $3,074.00, UP $32.00 - $3.00 below 3,077, $12.50 above 3,061.5, $49.50 above 3,024.50 and $79.50 above the 2,994.50 October low."},
 {"tenor":"Cash-to-3M structure","price":"+61.0 (BACKWARDATION)","basis":"A $61.00 BACKWARDATION, wider than $40.00 as price rose (same direction) - above the $15.00 reversal condition for a fourth session."},
 {"tenor":"Visible LME stock","price":"228,750 t","basis":f"DOWN 725 t to a new series low on 04-November; October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PRICE AND STRUCTURE FIRM TOGETHER. On the 04-November official cash $3,135.00 sits $61.00 ABOVE three-month $3,074.00, a BACKWARDATION, wider than $40.00 on 03-November because cash rose $53.00 and three-month $32.00 - spread and flat price moved in the SAME direction, ending two sessions of divergence. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00 and now $61.00. "
 f"READ: a fifteenth straight backwardation, the fourth above $15.00, with visible stock at another low (228,750 t) - prompt LME metal is tightening at an accelerating pace, and on 04-November the outright price followed. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
d['chart_price_axis']=[2900,3450]; d['chart_stock_axis']=[210000,255000]

ls=d['lme_series']; assert ls[-1][0]=='03-Nov', ls[-1]
d['lme_series']=ls[1:]+[["04-Nov",cash,m3,stk]]
assert all(210000<r[3]<255000 for r in d['lme_series']) and all(2900<r[1]<3450 and 2900<r[2]<3450 for r in d['lme_series'])
CU=(14201.0,14095.0,14110.5,14001.0); NI=(15465.0,15675.0,15200.0,15375.0); ZN=(3875.0,3840.0,3869.0,3810.0); PB=(1858.0,1886.5,1862.0,1894.0)
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/prev_m-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU[3]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI[3]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN[3]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB[3]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/prev_m,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU[3],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI[3],1)
# zn/pb 'now' = November month-to-date cash average: was mean(02,03-Nov), now mean(02,03,04-Nov)
zn_old=(3935.0+3869.0)/2; zn_mtd=(3935.0+3869.0+ZN[0])/3; pb_old=(1869.5+1862.0)/2; pb_mtd=(1869.5+1862.0+PB[0])/3
mh['zn'][-1]=round(mh['zn'][-1]*zn_mtd/zn_old,1); mh['pb'][-1]=round(mh['pb'][-1]*pb_mtd/pb_old,1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU[2]),('NI',NI[0],NI[2]),('ZN',ZN[0],ZN[2]),('PB',PB[0],PB[2])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-11-04'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending WEDNESDAY 04-NOVEMBER-2026 (Thursday's official prints 13:20 London, after this page compiles). THE WINDOW ROLLED THIS RUN: 14-October dropped and 04-November appended, so the window is 15-October to 04-November. Every point is an official cash settlement; the 04-November points come from the Westmetall English and German overviews, which agree, checked by five-for-five stock-line reconciliation against 03-November.")
ms['src']=["Westmetall - LME official cash settlements, English and German overviews (04-November-2026 session; stock lines reconciled against 03-November)",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
MD=[
 ("Copper",CU[0],CU[1]," COPPER: cash $14,201.00, up $90.50 or 0.64%; three-month $14,095.00, up $94.00 or 0.67%. BACKWARDATION narrowed slightly to $106.00 from $109.50 while price rose (opposite directions). STOCK ROSE ANOTHER 2,600 tonnes to 312,250 t, a fifth straight build."),
 ("Nickel",NI[0],NI[1]," NICKEL: cash $15,465.00, up $265.00 or 1.74%; three-month $15,675.00, up $300.00 or 1.95%. CONTANGO widened to $210.00 from $175.00, still the widest carry on the board. Stock fell 2,262 t to 275,592 t."),
 ("Zinc",ZN[0],ZN[1]," ZINC: cash $3,875.00, up $6.00 or 0.16%; three-month $3,840.00, up $30.00 or 0.79%. BACKWARDATION narrowed to $35.00 from $59.00 while price rose (opposite directions). Stock fell 3,900 tonnes to 150,450 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB[0],PB[1]," LEAD: cash $1,858.00, down $4.00 or 0.21%; three-month $1,886.50, down $7.50 or 0.40%. CONTANGO $28.50 from $32.00. Stock fell 650 t to 310,250 t."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Wednesday 04-November official four of five base metals rose - nickel three-month +1.95%, aluminium +1.05%, zinc +0.79%, copper +0.67%, lead -0.40%. Copper built 2,600 t; aluminium, nickel, zinc and lead drew. Trading Economics (05-November) reports Brent near $94 after a ~9% one-session slide to a two-month low following the US midterm results, European gas near EUR 85.7/MWh, and the dollar index at a five-week low near 101.3; December-hike odds about 77%. The LME euro fixing rose to 1.1264.")
d['metals_detail']=[{"name":n,"cash":c,"m3":m,"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c-old[n]['avg']):,.2f} "+("above" if c>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,m,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='03-Nov'
        i['hist']=i['hist'][1:]+[["04-Nov",CU[0]]]; assert len(i['hist'])==15
        i['val']="~14,095.00 (3M); 14,201.00 (cash) $/t"; i['ratio']="~14,201.00 $/t cash vs LME 3M 14,095.00 $/t"; i['trend']='up'
        i['src']=("LME official cash settlement, rolled to the WEDNESDAY 04-NOVEMBER-2026 session at $14,201.00, UP $90.50 or 0.64% against $14,110.50. THE WINDOW ROLLED THIS RUN: 14-October dropped and 04-November appended, so the series is the last fifteen published official cash sessions, 15-October to 04-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English and German overviews (stock lines reconciled against 03-November). "
                  "Copper structure for context: backwardation $106.00 (from $109.50); stock rose 2,600 t to 312,250 t.")
s=d['inputs_summary']; k=s.find("UPDATE 04-NOVEMBER"); assert k==0
d['inputs_summary']=("UPDATE 05-NOVEMBER: Copper rolled to the Wednesday 04-November LME official cash of $14,201.00 (+$90.50), its fifteen-session window moved to 15-October to 04-November. No new monthly carbon settlement (due mid-November) or dated SMM fluoride, silicon or magnesium mark was located for this run, so no other hist mark was appended. Energy fell sharply: Brent near $94 after a ~9% one-session slide to a two-month low on the US midterm result and Gulf export recovery (Trading Economics, 05-November; Straits Daily Brief $94.85 at 23:48 UTC 04-November) and European gas near EUR 85.7/MWh; EU storage below 75%. "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
OLDT="the tariff leg of the US duty-paid premium is 0.50 times the 03-November official cash of $3,082.00, or $1,541.00, DOWN $6.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of $862.00, so 64.1%"
NEWT=f"the tariff leg of the US duty-paid premium is 0.50 times the 04-November official cash of $3,135.00, or ${tl:,.2f}, UP $26.50 on the day. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OLDC="COMPILED WEDNESDAY 04-NOVEMBER-2026 (BEFORE THE RING) (LME BOARD ON THE TUESDAY 03-NOVEMBER OFFICIAL)."; NEWC="COMPILED THURSDAY 05-NOVEMBER-2026 (BEFORE THE RING) (LME BOARD ON THE WEDNESDAY 04-NOVEMBER OFFICIAL)."
n=0; nc=0
for p in d['premiums']:
    n+=p['src'].count(OLDT); nc+=p['src'].count(OLDC); p['src']=p['src'].replace(OLDT,NEWT).replace(OLDC,NEWC)
assert n==len(d['premiums']) and nc==len(d['premiums']),(n,nc)
ALU=397.0; ra=ALU/m3*100; na=0
o="THE RATIO: LME Alumina at $397.00/t against the 03-November aluminium three-month of $3,042.00 is 13.05%"
o2="THE LME ALUMINA (PLATTS) ROW IS UPDATED THIS RUN to AL Circle's $397.00/t print for the 02-November session"
n2=("THE LME ALUMINA (PLATTS) ROW IS CARRIED at AL Circle's $397.00/t print for the 02-November session (no newer dated LME alumina print located this run); SMM separately reports a 30,000 t trade at $397/t FOB WESTERN Australia for December shipment (05-November, "+S_SA+"), which corroborates that level but is a different basis from the FOB East Australia row, which stays at its 18-September mark. Original note:")
for a in d['alumina']:
    s=a['src'].replace(OLDC,NEWC)
    if o in s: na+=1
    if o2 in s: s=s.replace(o2,n2+" "+o2.replace("IS UPDATED THIS RUN","WAS UPDATED 04-NOVEMBER"),1)
    a['src']=s.replace(o,f"THE RATIO: LME Alumina at ${ALU:,.2f}/t against the 04-November aluminium three-month of $3,074.00 is {ra:.2f}%")
assert na==len(d['alumina']),na

d['lme_commentary']=("PRICE CATCHES UP WITH STRUCTURE. On the Wednesday 04-November official cash settled $3,135.00 (+$53.00) and three-month $3,074.00 (+$32.00) - back above 3,061.5 but $3.00 short of 3,077, and well above the 3,024.50 bear trigger, so scenario weights are HELD at 15/45/40. "
 "The backwardation widened to $61.00 from $40.00, the widest since mid-September, and visible stock fell 725 t to a new low of 228,750 t - this time price and structure moved together. Four of five base metals rose - nickel three-month +1.95%, aluminium +1.05%, zinc +0.79%, copper +0.67%; lead -0.40%. "
 "The rally came despite a collapse in energy: Brent fell about 9% in one session to a two-month low near $94 after the Democratic midterm sweep raised pressure to end the Iran war and Gulf crude exports recovered (Trading Economics, 05-November), and European gas eased toward EUR 86/MWh. The dollar sat at a five-week low near 101.3, a tailwind for metals. The Straits Daily Brief (05-November) still shows Hormuz transits far below baseline, with US strikes acknowledged and Iranian mine claims UNCONFIRMED. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" its October mean.")
d['net_read']=("NET: NEUTRAL WITH A FIRMING BIAS ON STRUCTURE. Supportive: the backwardation widened to $61.00 (fifteenth straight session, fourth above $15.00), visible LME stock fell to another low of 228,750 t, the dollar is at a five-week low, and three-month bounced back above 3,061.5. "
 "Against: three-month is still $3.00 below 3,077; Brent's slide to about $94 sharply lowers the energy cost floor and the Hormuz risk premium; IAI data show global primary output up 2.1% q/q in Q3 with GCC output recovering (+8.1% q/q), and Chinese spot still trades at a discount to SHFE (SMM).")
d['bottom_line']=("BOTTOM LINE: on the Wednesday 04-November LME official aluminium three-month rose $32.00 to $3,074.00 and cash $53.00 to $3,135.00 while the backwardation widened to $61.00 and visible stock fell to a new low of 228,750 t - price followed the tightening structure. "
 "No pre-registered trigger fired (three-month is $3.00 below 3,077 and $49.50 above 3,024.50), so weights stay 15% bull / 45% base / 40% bear. Re-crediting the bull needs a settled close above 3,077 with the backwardation beyond $15.00 - one more modest gain would do it; a close below 3,024.50, or a contango beyond $24.50, adds bear weight. The daily Elliott count is not re-labelled; invalidation is 3,289. Collapsing energy prices are the main headwind; the tight prompt LME market is the main support.")
c2=d['commercial']
for a,b in [("FIRST, PRICE EASED AGAIN BUT THE PROMPT PREMIUM ROSE: a $40.00 backwardation on 03-November, wider than $35.00 even as cash fell $13.00 and three-month $18.00 - a third print above the $15.00 reversal condition, so nearby metal is valued clearly over forward metal and there is no carry reward for deferring purchases, while the outright price sits $35.00 below 3,077.",
             "FIRST, PRICE AND PROMPT PREMIUM ROSE TOGETHER: a $61.00 backwardation on 04-November, wider than $40.00 as cash rose $53.00 and three-month $32.00 - a fourth print above the $15.00 reversal condition, so nearby metal is valued clearly over forward metal and there is no carry reward for deferring purchases; the outright price is now only $3.00 below 3,077."),
 ("is $1,541.00 on 03-November cash, 64.1% of the $2,403/t premium",f"is ${tl:,.2f} on 04-November cash, {share:.1f}% of the $2,403/t premium"),
 ("the 03-November official took three-month to $3,042.00, below 3,077 and 3,061.5 for a second session, $47.50 above the 2,994.50 settled low; energy eased further (Brent at a four-week low near $103, European gas below EUR 92/MWh, Trading Economics 03/04-November); the dollar index hit a five-week low near 101.4; December-hike odds about 75%;",
  "the 04-November official took three-month to $3,074.00, back above 3,061.5 but $3.00 below 3,077, $79.50 above the 2,994.50 settled low; energy collapsed (Brent about -9% in one session to near $94, European gas near EUR 86/MWh, Trading Economics 05-November); the dollar index sits at a five-week low near 101.3; December-hike odds about 77%; IAI data show Q3 global primary output +2.1% q/q (AL Circle, 04-November);")]:
    assert a in c2,a[:60]; c2=c2.replace(a,b)
d['commercial']=c2

SC={'Bull':'15%','Base':'45%','Bear':'40%'}
O_SC="HELD 04-NOVEMBER at 15/45/40"
for s in d['outlook']['scenarios']:
    t=s['drivers']; assert t.startswith(O_SC)
    s['prob']=SC[s['case']]
    s['drivers']=("HELD 05-NOVEMBER at 15/45/40. The Wednesday 04-November official settled three-month at $3,074.00, $3.00 BELOW the 3,077 bull-credit level and $49.50 above the 3,024.50 bear trigger, with the backwardation widening to $61.00 and stock at a new low of 228,750 t - no trigger fired either way. PRE-REGISTERED NEXT: a settled close above 3,077 with the backwardation beyond $15.00 returns five points to bull; a settled close below 3,024.50 or a contango beyond $24.50 adds five to bear. ")+t
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

RK=d['outlook']['risks']; hit=0
for r in RK:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 05-NOVEMBER: the 04-November official printed a $61.00 BACKWARDATION, a fourth session above $15.00 and the widest since mid-September. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 05-NOVEMBER: LME stock fell 725 t to a new low of 228,750 t, an eleventh straight draw (about 7,000 t over eleven sessions). Trend held at FLAT: the pace remains modest."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 05-NOVEMBER: energy collapsed - Brent fell about 9% in one session to near $94, a two-month low, after the US midterm result and as Gulf crude exports recover; TTF near EUR 85.7/MWh (Trading Economics, 05-November); EU storage below 75%. Trend moved to DOWN: the energy cost floor is falling fast."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 05-NOVEMBER: Straits Daily Brief - still effectively closed on the latest (lagged) PortWatch count of 2 transits on 25-October vs 85/day; US military acknowledges strikes on Iranian targets; IRGC claims four tankers destroyed by mines (Iranian state media, UNCONFIRMED); US sanctions on shadow-fleet registries (gCaptain). Trump says no immediate plans to escalate (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 05-NOVEMBER: markets price about a 77% chance of a December hike (down from 84% a week earlier); the dollar index is at a five-week low near 101.3 after the Democratic sweep of Congress (Trading Economics, 05-November). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE EX-CHINA RESTART PIPELINE'):
        r['risk']+=" UPDATE 05-NOVEMBER: IAI data show Q3-2026 global primary output 18.377 Mt, +2.1% q/q (-1.64% y/y), with GCC output +8.1% q/q to 306 kt in September as Gulf smelters recover (AL Circle, 04-November); Venezuela's state-owned Venalum is negotiating a second primary cargo to the US (AL Circle, 04-November). Trend held at UP."; r['trend']='up'; hit+=1
assert hit==6,hit
hitc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Wed 04-Nov':
        hitc+=1; cat['date']='Daily, from Thu 05-Nov'
        cat['event']=("THE 04-NOVEMBER OFFICIAL SETTLED THREE-MONTH AT $3,074.00, back above 3,061.5 but $3.00 short of 3,077 - no pre-registered trigger; weights held at 15/45/40. NEXT: a settled close above 3,077 with the backwardation beyond $15.00 (now $61.00) returns five points to bull; resistance 3,110 then the 3,148.5 wave (iv) high. A settled close below 3,024.50 would add bear weight and below about 2,977.5 would force a re-count toward the 2,894 weekly 61.8%. Invalidation of the daily count 3,289. Also this week: US payrolls (Friday) and US-Iran talks.")
assert hitc==1
d['outlook']['ai_analysis'].insert(0,"THURSDAY 05-NOVEMBER ON THE WEDNESDAY 04-NOVEMBER OFFICIAL: three-month rose $32.00 to $3,074.00 and cash $53.00 to $3,135.00, $3.00 short of the 3,077 bull-credit level - weights held at 15/45/40. The backwardation widened to $61.00 and visible stock fell 725 t to a new low (228,750 t): after two sessions of divergence, price followed the structure. The rally came despite Brent collapsing about 9% to near $94 on the US midterm result and recovering Gulf exports - lowering the energy cost floor - with a five-week-low dollar helping. Watch: a settled close above 3,077 would restore the rebound case; a close below 3,024.50 or a contango would confirm the bear case.")

EWS=("REVIEWED 05-NOVEMBER ON THE WEDNESDAY 04-NOVEMBER OFFICIAL: three-month settled $3,074.00, up $32.00 - a fourteenth settled close above the 2,994.50 low of 15-October, and back above 3,061.5 but $3.00 below 3,077. The sequence 2,994.50 / 3,024.50 / 3,008.00 / 3,018.00 / 3,027.00 / 3,064.00 / 3,084.00 / 3,064.00 / 3,080.00 / 3,060.00 / 3,042.00 / 3,074.00 remains an overlapping rebound; the 3,042.00 dip held well above 2,994.50, so it now reads as a candidate wave B/2 low, NOT yet confirmed as a pivot. Count NOT re-labelled (no invalidation broke). Base case about 55% (up from 50%): wave (v) of C ended at 2,994.50, 3,084.00 was wave A/1 and 3,042.00 the B/2 pullback, so a settled close above 3,084.00 would confirm a wave C/3 advance toward 3,110 and then the 3,148.5 wave (iv) high; alternate about 45%: the rebound is a corrective bounce that fails below 3,084-3,110 and the decline resumes toward a retest of 2,994.50, with a settled close below 2,977.5 forcing a re-count toward the 2,894 weekly 61.8%. A close below 3,042.00 would tilt back toward the alternate. Invalidation 3,289; confidence low-to-moderate. ")
st=d['ew']['short_term']['writeup']; k=st.find("REVIEWED",1); assert st.startswith("REVIEWED 04-NOVEMBER") and k>0
d['ew']['short_term']['writeup']=EWS+st[k:]
lt=d['ew']['long_term']['writeup']; k=lt.find("REVIEWED",1); assert lt.startswith("REVIEWED 04-NOVEMBER") and k>0
d['ew']['long_term']['writeup']=("REVIEWED 05-NOVEMBER (MID-WEEK): the Wednesday official at 3,074.00 recovered most of the week's losses but remains $3.00 below the 3,077 50% retracement. The weekly corrective count toward the 61.8% retracement at 2,894 stays the weekly base case, but with less conviction than on Tuesday; it would lose preference on a weekly close above 3,110, and is reinforced by a weekly close below 3,061.5 this Friday. Alternate (about 40%, up from 35%): the 2,994.50 low completed the weekly correction and a new advance is starting, supported by the steepening backwardation. Confidence moderate. ")+lt[k:]
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="94.2",day="about $93.9-94.2 on 05-November (Trading Economics; sections differ), -0.5% after a ~9% slide in the prior session to a two-month low; Straits Daily Brief $94.85 at 23:48 UTC 04-November",
 note="REFRESHED THURSDAY 05-NOVEMBER-2026 (Trading Economics): Brent trades just under $95 after falling nearly 9% in the prior session, its lowest in two months, after the Democratic sweep in the US midterms increased pressure on the administration to end the Iran war; Trump said he has no immediate plans to escalate strikes; Gulf crude exports are recovering. Down about 16% on the week. Levels approximate (header 94.15, stats 93.91). SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="85.7",day="about EUR 85.3-85.7/MWh on 05-November (Trading Economics; sections differ), about -2.7% to -3.1%",
 note="REFRESHED THURSDAY 05-NOVEMBER-2026 (Trading Economics): TTF near EUR 85.7/MWh; traders weigh mixed signals on US-Iran talks, Iranian attacks on shipping in Hormuz and rising heating demand in Northwest Europe; EU storage below 75%, the lowest for the time of year, with Germany about 61% against a 70% target. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="101.31",day="about 101.31 on 05-November (Trading Economics), -0.18%, a five-week low",
 note="REFRESHED THURSDAY 05-NOVEMBER-2026 (Trading Economics): the dollar fell to a five-week low as traders weighed the Democratic sweep of Congress; markets price about a 77% chance of a 25bp December Fed hike (down from 84% a week earlier). SOURCE: "+S_TD)
y=M['US 10-year Treasury yield (%)']['note']
if not y.startswith("CARRIED FROM 30-OCTOBER"): y="CARRIED FROM 30-OCTOBER (not re-fetched this run): "+y
M['US 10-year Treasury yield (%)']['note']=y
M['EUR/USD'].update(value='1.12640',day="LME fixing on 04-November, up from 1.11820",note="REFRESHED THURSDAY 05-NOVEMBER-2026 to the 04-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE WEDNESDAY 04-NOVEMBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION: this Thursday 05-November run is compiled about 02:40 London, BEFORE the ring, so Thursday's official (13:20 London) has not printed. The Trading Economics aluminium reference ($3,069.85, +0.82% for 04-November) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (05-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 04-November session, and the per-metal aluminium daily table's newest row is 04-November (cash 3,135.00, three-month 3,074.00, stock 228,750), so the board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the per-metal aluminium table's 28-October to 03-November rows match the stored series exactly; the overviews' prior-day FX column (MTLE 1.11820) matches the verified 03-November board.")
C[3]=("ALL FIVE STOCK LINES RECONCILE against 03-November via the pages' change column: aluminium -725 to 228,750; copper +2,600 to 312,250; nickel -2,262 to 275,592; zinc -3,900 to 150,450; lead -650 to 310,250.")
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (04-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (three sessions, 02-04 November) as their latest point. The price chart axis (floor 2,900) brackets three-month at 3,074.00; the stock chart axis floor of 210,000 t (lowered 04-November) brackets visible stock of 228,750 t with about 18,750 t headroom; it is re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,135.00 against three-month $3,074.00 is therefore a $61.00 BACKWARDATION, wider than $40.00 on 03-November - this session the spread and the flat price moved in the SAME direction (both firmer), after two sessions in opposite directions."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        C[i]=re.sub(r"the tariff leg is 0\.50 times the 03-November official cash of \$3,082\.00, or \$1,541\.00, leaving a \$862\.00 residual market leg out of the \$2,403/t US duty-paid premium \(64\.1% policy arithmetic\)",
                    f"the tariff leg is 0.50 times the 04-November official cash of $3,135.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic)",cv)
        assert C[i]!=cv; hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $94.2), the dollar index (about 101.31) and TTF (about EUR 85.7/MWh) are Trading Economics readings for 05-November; Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages again showed slightly different levels in different sections, so levels are approximate. The US ten-year row is CARRIED from 30-October (not re-fetched). The Straits Daily Brief shows Brent $94.85 at 23:48 UTC 04-November, cited in text only; the brief labels its ticker as AI-assisted. EUR/USD is the 04-November LME fixing, the same session as the board."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 05-NOVEMBER: no authorised fetch was blocked (Westmetall EN, DE and aluminium per-metal pages, Trading Economics aluminium/Brent/TTF/dollar, AL Circle, news.metal.com and the Straits Daily Brief all fetched). news.metal.com showed no SHFE settlement or Chinese social-inventory figure for 04/05-November, so none is used; only SMM's central-China spot discount (RMB 80-100/t to SHFE November) and a 30 kt FOB Western Australia alumina trade at $397/t are cited. A search for Q1-2027 Japanese premium offers found none - Q1 stays unpriced. Iranian mine claims are cited as UNCONFIRMED per the brief."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        C[i]=("PEER EARNINGS: NO NEW PEER RESULT ADDED THIS RUN, AND NO COMPANY WAS BACK-FILLED THIS RUN. NALCO Q2 FY27 (added 04-November) remains on secondary-source net sales and EBITDA only; its net-profit strip is not extended - the gap stays a gap. "+cv.split("NO COMPANY WAS BACK-FILLED THIS RUN. ",1)[-1]); hit+=1
assert hit==4,hit
d['so_what']={"line":"Aluminium bounced - Wednesday's LME official lifted three-month $32 to $3,074 and widened the cash premium over three-month to $61 as LME stock hit another low - even as oil collapsed about 9%, leaving price just $3 short of the $3,077 level that would revive the rebound case.",
 "points":[
 "WHAT MOVED: the 04-November official settled cash at $3,135.00 (+$53.00) and three-month at $3,074.00 (+$32.00, +1.05%). Cash trades $61.00 above three-month (backwardation, up from $40.00, the widest since mid-September) and LME stock fell 725 t to a new low of 228,750 t - price and structure firmed together.",
 "WHY: prompt LME metal keeps tightening, and a five-week-low dollar after the US midterms helped dollar-priced metals (nickel +2.0%, zinc +0.8%, copper +0.7%). That outweighed energy: Brent fell about 9% in one session to near $94 and European gas toward EUR 86/MWh (Trading Economics), lowering smelter cost support.",
 "SUPPLY: IAI data show global primary output up 2.1% q/q in Q3 to 18.38 Mt, with Gulf output recovering (+8.1% q/q) (AL Circle). Hormuz remains effectively closed on the latest lagged transit count, with US strikes acknowledged and Iranian mine claims unconfirmed.",
 "WHAT TO WATCH: a settled close above $3,077 with the backwardation above $15 would revive the rebound case; a close below $3,024.50 or a flip to contango would confirm the bear case. Also: Friday's US payrolls, US-Iran talks and the first Q1-2027 Japanese premium offers (not yet public)."]}

d['feed']=([
 {"when":"Thu 05-Nov","impact":"Bullish","text":"BOARD ROLLED TO THE WEDNESDAY 04-NOVEMBER LME OFFICIAL: cash $3,135.00 (+$53.00), three-month $3,074.00 (+$32.00) - back above 3,061.5, $3.00 short of 3,077; weights held at 15/45/40."},
 {"when":"Thu 05-Nov","impact":"Bullish","text":"STRUCTURE TIGHTENS FURTHER: backwardation $61.00 (from $40.00), widest since mid-September; LME stock -725 t to a new low of 228,750 t (eleventh straight draw)."},
 {"when":"Thu 05-Nov","impact":"Bearish (cost)","text":"OIL COLLAPSES: Brent about -9% in one session to near $94, a two-month low, after the US midterms; European gas near EUR 85.7/MWh (Trading Economics). Dollar at a five-week low near 101.3."},
 {"when":"Thu 05-Nov","impact":"Mixed","text":"HORMUZ: Straits Daily Brief - still effectively closed on lagged PortWatch data; US strikes acknowledged; IRGC mine claims on four tankers UNCONFIRMED; new US shadow-fleet sanctions."},
 {"when":"Wed 04-Nov","impact":"Bearish","text":"IAI: global primary aluminium output +2.1% q/q in Q3-2026 to 18.377 Mt (-1.64% y/y); GCC +8.1% q/q (AL Circle)."},
 {"when":"Wed 04-Nov","impact":"Mixed","text":"VENEZUELA: Mercuria and Heeney Capital negotiating a second Venalum primary cargo to the US, potentially before end-2026 (AL Circle)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM REBOUNDS. The Wednesday 04-November official settled cash at $3,135.00 (+1.72%) and three-month at $3,074.00 (+1.05%), back above 3,061.5 but $3.00 short of 3,077. Visible stock fell 725 t to a new low of 228,750 t. Board: nickel three-month +1.95%, aluminium +1.05%, zinc +0.79%, copper +0.67%, lead -0.40%; copper stock +2,600 t."},
 {"theme":"LME","horizon":"0-1 month","impact":"Bullish","url":W,
  "headline":"BACKWARDATION WIDENS TO $61: the cash-to-three-month spread rose to $61.00 from $40.00 on 04-November as cash outpaced three-month - spread and price in the same direction this time - the widest backwardation since mid-September and a fifteenth straight. READ: prompt LME tightness is accelerating and the outright price is starting to follow."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bearish (cost)","url":S_BR,
  "headline":"BRENT PLUNGES ABOUT 9% TO A TWO-MONTH LOW (Trading Economics, 05-November): Brent trades just under $95 after the Democratic sweep in the US midterms raised pressure on the administration to end the Iran war; Trump said he has no immediate plans to escalate strikes; Gulf crude exports are recovering; Brent is down about 16% this week. European gas near EUR 85.7/MWh, with EU storage below 75%. READ: the energy cost floor for ex-China smelters is falling fast."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Mixed","url":S_ST,
  "headline":"HORMUZ STILL EFFECTIVELY CLOSED (Straits Daily Brief, 05-November): latest IMF PortWatch count 2 transits on 25-October vs an 85/day baseline (weekly, lagged); Brent $94.85 at 23:48 UTC, -8.89% on 24h. The US military acknowledges strikes on Iranian targets; the IRGC claims four tankers were destroyed by naval mines (Iranian state media, UNCONFIRMED); the US sanctioned operators of fraudulent shadow-fleet registries (gCaptain)."},
 {"theme":"Macro","horizon":"0-2 months","impact":"Bullish","url":S_TD,
  "headline":"DOLLAR AT FIVE-WEEK LOW (Trading Economics, 05-November): the dollar index near 101.31 after the Democratic sweep of Congress, seen as a check on new fiscal spending; markets price about a 77% chance of a December Fed hike, down from 84% a week earlier. READ: a softer dollar is a tailwind for dollar-priced metals."},
 {"theme":"Supply","horizon":"0-6 months","impact":"Bearish","url":S_IAI,
  "headline":"GLOBAL PRIMARY OUTPUT +2.1% Q/Q IN Q3 (AL Circle on IAI data, 04-November): Q3-2026 output 18.377 Mt vs 18.003 Mt in Q2 (-1.64% y/y); January-September 54.76 Mt (-1%); September 6.014 Mt, about 200,500 t/day. China 11.481 Mt (+1.8% q/q); GCC +8.1% q/q to 306 kt in September; Europe incl. Russia 1.91 Mt (+3.1%). READ: Gulf supply is recovering from its war-hit lows."},
 {"theme":"Trade","horizon":"0-3 months","impact":"Mixed","url":S_VE,
  "headline":"VENEZUELA EYES SECOND PRIMARY ALUMINIUM CARGO TO THE US (AL Circle, 04-November): Mercuria and Heeney Capital are reportedly negotiating with Venezuelan officials on a second shipment from state-owned CVG Venalum, potentially departing before end-2026, after a first cargo arrived in New Orleans in October. Volumes not disclosed."},
 {"theme":"China","horizon":"Immediate","impact":"Mixed","url":S_SM,
  "headline":"CENTRAL CHINA PREMIUMS STABLE (SMM, 05-November): transactions in central China at a discount of RMB 80-100/t to the SHFE November contract; premiums basically stable with improved trading sentiment boosting buying interest."},
 {"theme":"Alumina","horizon":"0-1 month","impact":"Mixed","url":S_SA,
  "headline":"ALUMINA TRADE AT $397/T FOB WESTERN AUSTRALIA (SMM, 05-November): 30,000 t traded for December shipment, in line with the $397/t LME Alumina (Platts) print for 02-November. Alumina is about 12.9% of the aluminium three-month price, still below the 15-17% decade norm."},
]+d['news']
d['news']=d['news'][:20]

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 04-NOVEMBER: no newer public disclosure","REVIEWED 05-NOVEMBER: no newer public disclosure").replace("REVIEWED 04-NOVEMBER. NO NEW DATED","REVIEWED 05-NOVEMBER. NO NEW DATED")
    return o
d['producer_status']=walk(d['producer_status'])
for p in d['producer_status']: p['asof']=RD
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 04-Nov-2026 session (English and German overviews agree; stock lines reconciled vs 03-Nov)",W])
for x in ([L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_ST,S_ST],[L_IAI,S_IAI],[L_VE,S_VE],[L_SA,S_SA],[L_SM,S_SM]): d['sources'].append(x)
for x in ([L_BR,S_BR],[L_TG,S_TG],[L_ST,S_ST],[L_IAI,S_IAI]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-11-03'
ph['rows'][-1]=['2026-11-04',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2))
