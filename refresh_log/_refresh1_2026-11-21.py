# Daily data refresh - 2026-11-21 (SATURDAY, ~02:40 UTC; no LME ring today). Board ROLLED TWO SESSIONS to the FRIDAY 20-Nov LME official
# (the 19-Nov and 20-Nov officials were both published after the prior run). Cache-busted EN + DE overviews agree on 20-Nov (Al cash 3,184.50 /
# 3M 2,831.50 / stock 223,525; MTLE 1.09820, 19-Nov 1.09980). Al/Cu/Ni/Zn/Pb per-metal tables newest row 20-Nov, no later row (weekend).
# Cash UP while 3M DOWN for a third session: backwardation $353 (series widest). Stock draws resume (-1,725 then -900). Weekly close below 2,894.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-21'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-21"; L_ST="Straits Daily Brief - Strait of Hormuz, 21-Nov-2026 (48 vessels holding; UKMTO-confirmed tanker fire 20-Nov; Brent $92.56)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,839.75 (-1.00%) on 20-Nov-2026; 51-week low 2,819 on 18-Nov; month -6.54% (CFD reference)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$92.57 on 20-Nov-2026, third straight weekly decline; month -14.9%"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.84 (20-Nov-2026), fourth weekly gain; Waller floats 50bp December hike"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 88.45/MWh (+4.7%) on 20-Nov-2026 on Troll outage and cold forecasts; EU storage ~69.8%"
S_AC="https://www.alcircle.com/news/lme-aluminium-cash-offer-price-rises-to-3-105-t-as-opening-stocks-climb-2-63-to-226-150t-122032"; L_AC="AL Circle - LME aluminium cash offer $3,105/t on 19-Nov; cancelled warrants -9% to 18,450 t; LME alumina (Platts) $398/t (20-Nov-2026)"
S_KZ="https://www.alcircle.com/news/kazakhstan-s-aluminium-exports-to-eu-reached-110-184t-in-as-cbam-reshapes-trade-outlook-122035"; L_KZ="AL Circle - Kazakhstan's aluminium exports to the EU reach 110,184 t as CBAM reshapes trade outlook (20-Nov-2026)"
S_BL="https://www.alcircle.com/news/ball-increases-investment-by-37-as-aluminum-beverage-can-capacity-tightens-122044"; L_BL="AL Circle - Ball raises 2026 capex ~37% to about $650m as beverage-can capacity tightens (Nov-2026)"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3095.0 and B['LME 3-month']['cur']==2865.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
p18=(3095.0,2865.0,226150)
pc,pm,ps=3105.0,2845.0,224425            # 19-Nov (previous column)
cash,m3,stk=3184.5,2831.5,223525          # 20-Nov (board)
spr=cash-m3; psp=pc-pm; assert spr==353.0 and psp==260.0 and ps-900==stk and p18[2]-1725==ps
ytd=(m3/3010.5-1)*100
wk=(m3/3018.0-1)*100   # vs Fri 13-Nov 3M official

VER=("COMPILED SATURDAY 21-NOVEMBER-2026 ABOUT 02:40 LONDON - NO LME RING TODAY (WEEKEND). THE BOARD IS THE FRIDAY 20-NOVEMBER-2026 LME OFFICIAL, THE LAST TRADING SESSION OF THE WEEK; it ROLLED TWO SESSIONS this run because the Thursday 19-November and Friday 20-November officials were both published after the previous run. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 20-November official for all metals with stocks and FX (EUR/USD MTLE 1.09820; 19-November 1.09980); (2) the aluminium, copper, nickel, zinc and lead per-metal daily tables all show 20-November as their newest row with NO later row (market shut for the weekend), and the aluminium table's 26-October to 18-November rows match the stored series. "
 "The whole board sits on ONE UNIFORM SESSION (20-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" FRIDAY 20-NOVEMBER (the board): CASH SETTLED $3,184.50, UP $79.50 OR 2.56% FROM THE THURSDAY 19-NOVEMBER $3,105.00 (itself +$10.00 on 18-November). THREE-MONTH SETTLED $2,831.50, DOWN $13.50 OR 0.47% FROM $2,845.00 (19-November: -$20.00) - inside the 2,830-2,850 Elliott completion zone, the lowest three-month official in this series and $179.00 BELOW the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%; week {wk:+.2f}% vs the 13-November $3,018.00). "
 "THE BACKWARDATION WIDENED TO $353.00 (19-November $260.00, 18-November $230.00) - the widest in this series, a twenty-seventh straight backwardation and the sixteenth above $15.00. SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS FOR A THIRD STRAIGHT SESSION: cash rose while three-month fell. "
 "VISIBLE LME STOCK FELL 1,725 t TO 224,425 t ON 19-NOVEMBER AND 900 t TO 223,525 t ON 20-NOVEMBER - the draws resumed after the single 18-November build. AL Circle (20-November) reports cancelled warrants down 9% to 18,450 t on 19-November. The Trading Economics aluminium reference shows about $2,839.75 (-1.00%) for 20-November - a CFD reference cited in text only.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,184.5","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"2,831.5","pos":False,"delta":VER+AL+" THREE-MONTH IS NOW INSIDE THE 2,830-2,850 EXTENDED-(v) ZONE and $62.50 BELOW the 2,894 weekly 61.8% retracement - and the WEEK CLOSED BELOW 2,894. A settled close below about 2,803 would make wave (v) longer than wave (iii) and force a re-label; a settled close back above 2,994.50 would signal a failed break; above 3,097.50 negates the wave (v) count; daily invalidation of the bearish count remains 3,289."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+353.0","pos":True,"delta":VER+f" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,184.50 against three-month $2,831.50 is a $353.00 BACKWARDATION, UP from $260.00 on 19-November and $230.00 on 18-November - the widest in this series - as cash rose and three-month fell on each of the last three sessions: SPREAD AND FLAT (FORWARD) PRICE MOVED IN OPPOSITE DIRECTIONS. It stays above the published $15.00 reversal condition for a sixteenth session and is a twenty-seventh straight backwardation; a contango beyond $24.50 would reverse the structural signal. The October mean spread was ${oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"223,525","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 900 t TO 223,525 t ON 20-NOVEMBER after -1,725 t to 224,425 t on 19-November - the draws RESUMED after the single 5,800 t build on 18-November; 220,350 t (17-November) remains the series low. Cancelled warrants fell 9% to 18,450 t on 19-November (AL Circle), so less metal is queued to leave. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 19-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $2,831.50, DOWN $13.50 FROM THE 19-NOVEMBER $2,845.00 (which was -$20.00 from 18-November's $2,865.00) - inside the 2,830-2,850 Elliott zone, $62.50 BELOW the 2,894 weekly 61.8%, the lowest three-month official in this series; $179.00 BELOW the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 900 t TO 223,525 t on 20-November after -1,725 t on 19-November - draws resumed after the 18-November build (17-November 220,350 t is the series low). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $353.00 BACKWARDATION, UP FROM $260.00 ON 19-NOVEMBER - the widest in this series. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On each of 18, 19 and 20 November cash ROSE while three-month FELL - spread and flat price moved in OPPOSITE directions. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00 and $353.00."},
 {"name":"EUR/USD LME fixing","cur":1.0982,"prev":1.0998,"avg":1.1465,"note":VER+" THE LME EURO FIXING WAS 1.09820 ON 20-NOVEMBER, DOWN FROM 1.09980 ON 19-NOVEMBER (18-November 1.09630) as the dollar index held near 103.8 on a fourth weekly gain. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (20-Nov official)","price":"3,184.5","basis":"THE FRIDAY 20-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,184.50, UP $79.50 OR 2.56% (19-November $3,105.00). No ring at the weekend; next print Monday 23-November 13:20 London."},
 {"tenor":"3-month (20-Nov official)","price":"2,831.5","basis":"THE 20-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $2,831.50, DOWN $13.50 - inside the 2,830-2,850 extended-(v) zone, $62.50 below the 2,894 weekly 61.8%; the week closed below 2,894."},
 {"tenor":"Cash-to-3M structure","price":"+353.0 (BACKWARDATION)","basis":"A $353.00 BACKWARDATION, up from $260.00 - the widest in this series; cash rose while three-month fell for a third session (opposite directions)."},
 {"tenor":"Visible LME stock","price":"223,525 t","basis":f"DOWN 900 t on 20-November and 1,725 t on 19-November - draws resumed after one build; October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PROMPT TIGHTER STILL, FORWARD WEAKER - THE CURVE STEEPENS FOR A THIRD SESSION. On the 20-November official cash $3,184.50 sits $353.00 ABOVE three-month $2,831.50, a BACKWARDATION up from $260.00 (19-November) and $230.00 (18-November) - the widest in this series - as cash rose while three-month fell on each session: spread and flat price moved in OPPOSITE directions. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00 and now $353.00. "
 f"READ: a twenty-seventh straight backwardation with visible stock drawing again (223,525 t) and cancelled warrants down to 18,450 t (AL Circle) - nearby metal is scarce while the forward prices a looser 2027 (Trading Economics cites forecasts of an 830 kt 2027 surplus; Emkay Global, via AL Circle, a ~400 kt deficit). The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2700,3450] and d['chart_stock_axis']==[190000,255000]

ls=d['lme_series']; assert ls[-1][0]=='18-Nov'
d['lme_series']=ls[2:]+[["19-Nov",pc,pm,ps],["20-Nov",cash,m3,stk]]
assert len(d['lme_series'])==15 and all(190000<r[3]<255000 and 2700<r[2]<3450 and 2700<r[1]<3450 for r in d['lme_series'])
TBL=[(3095.0,3060.0,230775),(3082.0,3042.0,229475),(3135.0,3074.0,228750),(3160.0,3097.5,228475),(3117.0,3050.0,227600),(3147.0,3059.5,226975),(3137.0,3027.0,226850),(3223.5,3064.0,226725),(3155.5,3032.0,226350),(3150.5,3018.0,224150),(3332.0,3020.0,221900),(3060.5,2940.0,220350),(3095.0,2865.0,226150),(pc,pm,ps),(cash,m3,stk)]
assert [tuple(r[1:]) for r in d['lme_series']]==TBL, d['lme_series']
CU=(12230.5,12237.0,332025); NI=(15310.0,15490.0,275184); ZN=(3670.0,3502.5,145675); PB=(1825.0,1861.0,261525)
CU9=(12570.0,12555.0,327525); NI9=(15425.0,15625.0,275118); ZN9=(3714.5,3536.0,146200); PB9=(1822.0,1860.0,266325)
CU8m3,NI8m3=12773.5,15985.0
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU9[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI9[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN9[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB9[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/2865.0,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU8m3,1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI8m3,1)
zn13=[3935.0,3869.0,3875.0,3877.0,3759.0,3754.0,3768.0,3794.0,3760.5,3745.0,3848.0,3776.0,3732.0]; pb13=[1869.5,1862.0,1858.0,1866.5,1857.0,1854.0,1846.0,1845.0,1843.0,1853.0,1856.0,1840.0,1831.0]
zn_new=(sum(zn13)+ZN9[0]+ZN[0])/15; pb_new=(sum(pb13)+PB9[0]+PB[0])/15
mh['zn'][-1]=round(mh['zn'][-1]*zn_new/(sum(zn13)/13),1); mh['pb'][-1]=round(mh['pb'][-1]*pb_new/(sum(pb13)/13),1)
ms=d['metals_series']; R=ms['rows']
for k,v9,v in (('CU',CU9[0],CU[0]),('NI',NI9[0],NI[0]),('ZN',ZN9[0],ZN[0]),('PB',PB9[0],PB[0])):
    R[k]=R[k][2:]+[v9,v]; assert len(R[k])==15
assert R['CU']==[14380.0,14110.5,14201.0,14110.0,13955.0,14030.0,13992.0,13875.5,13712.0,13610.0,13375.0,13225.5,12750.0,12570.0,12230.5],R['CU']
assert R['NI']==[15260.0,15200.0,15465.0,16100.0,16095.0,16190.0,15875.0,15930.0,16010.0,16025.0,15805.0,15790.0,15800.0,15425.0,15310.0],R['NI']
assert R['ZN']==[3935.0,3869.0,3875.0,3877.0,3759.0,3754.0,3768.0,3794.0,3760.5,3745.0,3848.0,3776.0,3732.0,3714.5,3670.0],R['ZN']
assert R['PB']==[1869.5,1862.0,1858.0,1866.5,1857.0,1854.0,1846.0,1845.0,1843.0,1853.0,1856.0,1840.0,1831.0,1822.0,1825.0],R['PB']
ms['asof']='2026-11-20'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending FRIDAY 20-NOVEMBER-2026 (the last session before the weekend). THE WINDOW ROLLED TWO SESSIONS THIS RUN: 29- and 30-October dropped, 19- and 20-November appended, so the window is 02-November to 20-November. Every point is an official cash settlement from the Westmetall per-metal tables (all four re-fetched this run and asserted equal to the stored window) and the English/German overviews.")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (20-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return "unchanged" if a==b else f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,f" COPPER 20-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU9[0])} from 19-November (${CU9[0]:,.2f}, itself {chg(CU9[0],12750.0)}); three-month ${CU[1]:,.2f}, {chg(CU[1],CU9[1])} - the lowest three-month official in this window, about {abs(CU[1]/13545-1)*100:.1f}% down on the week. STRUCTURE: a $6.50 CONTANGO (19-November a $15.00 backwardation). Stock rose 4,500 t to 332,025 t on 20-November (19-November +125 t)."),
 ("Nickel",NI,f" NICKEL 20-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI9[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI9[1])}. CONTANGO $180.00 (19-November $200.00), still the widest carry on the board. Stock 275,184 t (+66 t; 19-November +1,002 t)."),
 ("Zinc",ZN,f" ZINC 20-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN9[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN9[1])}. BACKWARDATION widened to $167.50 (19-November $178.50, 18-November $132.00). Stock fell 525 t to 145,675 t (19-November -575 t). Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,f" LEAD 20-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB9[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB9[1])}. CONTANGO $36.00 (19-November $38.00). Stock fell 4,800 t to 261,525 t (19-November -2,675 t)."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(f" CROSS-METAL: over the two sessions since the 18-November official, three-month copper fell {abs(CU[1]/CU8m3-1)*100:.2f}%, nickel {abs(NI[1]/NI8m3-1)*100:.2f}%, zinc {abs(ZN[1]/3600-1)*100:.2f}%, aluminium {abs(m3/2865-1)*100:.2f}% and lead {abs(PB[1]/1864-1)*100:.2f}% - a third week of macro risk-off with the dollar index on a fourth weekly gain and Fed Governor Waller floating a 50bp December hike (Trading Economics). The LME euro fixing was 1.0982.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='18-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][2:]+[["19-Nov",CU9[0]],["20-Nov",CU[0]]]; assert len(i['hist'])==15 and i['hist'][0][0]=='02-Nov',i['hist'][0]
        assert [v for _,v in i['hist']]==R['CU']
        i['val']="~12,237.00 (3M); 12,230.50 (cash) $/t"; i['ratio']="~12,230.50 $/t cash vs LME 3M 12,237.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled TWO SESSIONS to the FRIDAY 20-NOVEMBER-2026 session at $12,230.50 (19-November $12,570.00; 18-November $12,750.00). THE WINDOW ROLLED THIS RUN: 29- and 30-October dropped and 19- and 20-November appended, so the series is the last fifteen published official cash sessions, 02-November to 20-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall per-metal table and English/German overviews. "
                  "Copper structure for context: a $6.50 contango on 20-November; stock 332,025 t (+4,500 t).")
s=d['inputs_summary']
d['inputs_summary']=("UPDATE 21-NOVEMBER (WEEKEND): Copper rolled two sessions to the Friday 20-November LME official cash of $12,230.50 (window 02-November to 20-November). No new carbon, fluoride, silicon or magnesium mark was located this run, so those series are unchanged (gaps stay gaps). Energy: Brent about $92.6, a third straight weekly decline; European gas jumped about 4.7% to about EUR 88.45/MWh on a Troll field outage and colder forecasts, with EU storage about 69.8% (Trading Economics, 20-November). LME alumina (Platts) $398/t (AL Circle, 20-November). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
NC1="COMPILED FRIDAY 20-NOVEMBER-2026 BEFORE THE RING (LME BOARD ROLLED TO THE WEDNESDAY 18-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; THE 19-NOVEMBER OFFICIAL WAS NOT YET ON WESTMETALL AT RUN TIME)."
NC2="COMPILED SATURDAY 21-NOVEMBER-2026 (WEEKEND, NO RING; LME BOARD ROLLED TWO SESSIONS TO THE FRIDAY 20-NOVEMBER OFFICIAL, THE LAST TRADING SESSION OF THE WEEK)."
OT="the tariff leg of the US duty-paid premium is 0.50 times the 18-November official cash of $3,095.00, or $1,547.50, UP $17.25 against the 17-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of $855.50, so 64.4%"
NT=f"the tariff leg of the US duty-paid premium is 0.50 times the 20-November official cash of $3,184.50, or ${tl:,.2f}, UP ${tl-1547.5:,.2f} against the 18-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OCV="the tariff leg is 0.50 times the 18-November official cash of $3,095.00, or $1,547.50, leaving a $855.50 residual market leg out of the $2,403/t US duty-paid premium (64.4% policy arithmetic)"
NCV=f"the tariff leg is 0.50 times the 20-November official cash of $3,184.50, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic)"
ra=398.24/m3*100
OR="THE RATIO: LME Alumina at $398.24/t against the 18-November aluminium three-month of $2,865.00 is 13.90%"
NR=f"THE RATIO: LME Alumina at $398.24/t against the 20-November aluminium three-month of $2,831.50 is {ra:.2f}%"
cnt={'nc':0,'t':0,'r':0,'cv':0,'rv':0}
def f(s):
    if NC1 in s: cnt['nc']+=s.count(NC1); s=s.replace(NC1,NC2)
    if OT in s: cnt['t']+=1; s=s.replace(OT,NT)
    if OR in s: cnt['r']+=1; s=s.replace(OR,NR)
    if OCV in s: cnt['cv']+=1; s=s.replace(OCV,NCV)
    for a,b in (("REVIEWED 20-NOVEMBER: no newer public disclosure","REVIEWED 21-NOVEMBER: no newer public disclosure"),("REVIEWED 20-NOVEMBER. NO NEW DATED","REVIEWED 21-NOVEMBER. NO NEW DATED")):
        if a in s: cnt['rv']+=1; s=s.replace(a,b)
    return s
for k in ('premiums','alumina','producer_status','inputs','logistics','raw_materials','caveats'):
    d[k]=walk(d[k],f)
print(cnt)
assert cnt['nc']==10 and cnt['t']==6 and cnt['r']==4 and cnt['cv']==1, cnt
for k in ('premiums','alumina'): assert "18-November official cash of $3,095.00" not in json.dumps(d[k],ensure_ascii=False), k

d['lme_commentary']=("WEEK CLOSES BELOW 2,894 WITH THE PROMPT AT ITS TIGHTEST. Over Thursday and Friday cash rose $10.00 and then $79.50 to $3,184.50, while three-month fell $20.00 and $13.50 to $2,831.50 - so the backwardation widened to $353.00, the widest in this series, with spread and flat price moving in OPPOSITE directions for a third session. Three-month closed the week $62.50 below the 2,894 weekly 61.8% retracement and inside the 2,830-2,850 Elliott zone, down "+f"{abs(wk):.2f}% on the week. Visible stock fell 1,725 t and 900 t to 223,525 t, so the 18-November build was a one-off; cancelled warrants fell 9% to 18,450 t (AL Circle). "
 "Macro stays the headwind: the dollar index posted a fourth weekly gain near 103.8 and Fed Governor Waller floated a 50bp December hike; copper lost about 9.7% on the week to $12,237. Trading Economics cites forecasts of an 830 kt 2027 surplus, while Emkay Global (via AL Circle) still sees a ~400 kt deficit in 2027 and 2028 - the forecasts disagree. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} below its October mean.")
d['net_read']=("NET: BEARISH ON THE FORWARD, TIGHT ON THE PROMPT. Against: three-month at $2,831.50 closed the week below the 2,894 weekly 61.8%; a hawkish Fed (December hike priced, 50bp floated) and a dollar on a fourth weekly gain; forecasts of a 2027 surplus as Chinese output tops 46 Mt and Gulf metal returns; copper's slide to a seven-month low. "
 "Supportive: a $353.00 backwardation (the widest in this series, twenty-seventh straight), stock drawing again to 223,525 t with cancelled warrants falling, Hormuz still effectively closed with a UKMTO-confirmed tanker strike on 20-November, and Emkay Global's view of a ~400 kt deficit through 2028.")
d['bottom_line']=("BOTTOM LINE: the week ended with the curve at its steepest - cash $3,184.50, three-month $2,831.50, a $353.00 backwardation - after cash rose and three-month fell for a third session; visible stock resumed drawing to 223,525 t. "
 "The WEEKLY close below 2,894 keeps the 10% bull / 35% base / 55% bear weights and lifts the weekly alternate toward the 78.6% near 2,633. Three-month is inside the 2,830-2,850 wave (v) completion zone; a settled close below about 2,803 would force a re-label, back above 2,994.50 would signal a failed break, above 3,097.50 negates the count; daily invalidation 3,289. No ring at the weekend; next print Monday 23-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, THE CURVE STEEPENS - PROMPT TIGHT, FORWARD WEAK:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, THE CURVE STEEPENS AGAIN - PROMPT TIGHT, FORWARD WEAK: the backwardation widened to $353.00 on 20-November (from $230.00 on 18-November) as cash rose to $3,184.50 while three-month fell to $2,831.50, below the 2,894 weekly 61.8% on a weekly close; nearby metal commands a record premium over forward metal in this series, so there is no carry reward for holding stock - and visible LME stock resumed drawing to 223,525 t after a one-day build. "+c2[a1:]
o="is $1,547.50 on 18-November cash, 64.4% of the $2,403/t premium"; assert o in c2; c2=c2.replace(o,f"is ${tl:,.2f} on 20-November cash, {share:.1f}% of the $2,403/t premium")
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find("; the dollar index near",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 20-November official left three-month at $2,831.50, inside the 2,830-2,850 Elliott zone, after a weekly close below 2,894, while cash rose to $3,184.50; Fed Governor Waller floated a 50bp December hike (Trading Economics 20-November); first Q1-2027 Japanese premium offers, which typically emerge from late November (none located yet)"+c2[b1:]
d['commercial']=c2

for s in d['outlook']['scenarios']:
    assert s['prob']=={'Bull':'10%','Base':'35%','Bear':'55%'}[s['case']]
    s['drivers']=("HELD 21-NOVEMBER AT 10/35/55: the week closed with three-month at $2,831.50, below 2,894, confirming the 20-November bear weighting; no further pre-registered trigger was hit (the next is a settled close below about 2,803 for more bear weight, or back above 2,994.50 to return weight to base). ")+s['drivers']
d['outlook']['scenario_paths']={'labels':['Now','Nov-26','Dec-26','Mar-27','Jun-27'],'bull':[m3,3000,3300,3500,3650],'base':[m3,2860,2960,3080,3150],'bear':[m3,2800,2780,2770,2750]}

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 21-NOVEMBER: the 19- and 20-November officials printed backwardations of $260.00 and $353.00 - the widest in this series and a sixteenth session above $15.00. Contango risk remains remote near term. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 21-NOVEMBER: draws resumed - LME stock fell 1,725 t on 19-November and 900 t on 20-November to 223,525 t after the single 18-November build; cancelled warrants fell 9% to 18,450 t (AL Circle), so the pace of outflow may slow. Trend held at FLAT."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 21-NOVEMBER: three-month at $2,831.50 is nearer the energy-cost floor; Brent about $92.6 (third weekly decline) but European gas jumped about 4.7% to EUR 88.45/MWh on a Troll outage and cold forecasts (Trading Economics); LME alumina (Platts) $398/t. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 21-NOVEMBER: Straits Daily Brief - still effectively closed; latest transit count 2 on 15-November; 48 AIS-visible vessels holding (from 45). UKMTO CONFIRMED a tanker caught fire after a projectile strike near the Strait on 20-November; Iranian claims of supertankers striking mines remain unconfirmed by any maritime authority. Iranian-linked reporting says Tehran is ready to reopen if the US meets its commitments - no agreement announced. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 21-NOVEMBER: Governor Waller suggested a 50bp December hike could be considered; markets price 25bp in December, another in January and at least one more by end-2027; dollar index about 103.84, a fourth weekly gain (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
assert hit==5,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Fri 20-Nov':
        hc+=1; cat['date']='Daily, from Mon 23-Nov'
        cat['event']=("FRIDAY 20-NOVEMBER OFFICIAL (WEEKLY CLOSE): three-month $2,831.50, BELOW the 2,894 weekly 61.8% and inside the 2,830-2,850 extended-(v) zone; cash $3,184.50; backwardation $353.00 (series widest); stock 223,525 t (draws resumed). NEXT: Monday 23-November official (13:20 London) - a settled close below about 2,803 forces a wave re-label and adds bear weight; back above 2,994.50 signals a failed break; above 3,097.50 negates the count; invalidation 3,289. The December Fed meeting (50bp floated); any official US-Canada tariff announcement; first Q1-2027 Japanese premium offers (none located yet).")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"SATURDAY 21-NOVEMBER ON THE FRIDAY 20-NOVEMBER OFFICIAL (WEEKLY CLOSE): the curve steepened for a third session - cash rose to $3,184.50 while three-month fell to $2,831.50, widening the backwardation to $353.00, the widest in this series. Three-month closed the week below the 2,894 weekly 61.8% and sits inside the 2,830-2,850 Elliott completion zone. Visible stock resumed drawing to 223,525 t and cancelled warrants fell to 18,450 t (AL Circle). Macro remains the driver: a fourth weekly dollar gain and a 50bp December hike floated by Fed Governor Waller; copper fell about 9.7% on the week. Weights held at 10/35/55.")

st=d['ew']['short_term']; nx=st['now_x']
st['proj']={"bull":[[nx,m3],[0.99997,2950],[1.0,3050]],"base":[[nx,m3],[0.99997,2815],[1.0,2950]],"bear":[[nx,m3],[0.99997,2790],[1.0,2700]]}
assert st['fwd_pivots'][0]['p']==2840.0
st['fwd_pivots'][0]={"t":0.99996,"p":2830.0,"w":"UPDATED 21-NOVEMBER: three-month settled 2,831.50 on 20-November, inside the 2,830-2,850 completion zone (0.618 x (i)-(iii) from 3,097.50 near 2,863 already met). Count unchanged: (i) 3,374-3,183, (ii) 3,289, (iii) to 2,994.50, (iv) 3,097.50, (v) under way and extending ($266 so far vs $294.50 for (iii)). A settled close below about 2,803 would make (v) longer than (iii) - not a rule break since (iii) exceeds (i), but it would favour an extended-(v) re-label toward 1.618 x (i) near 2,788 or lower. The wave (v) low is NOT confirmed until a reversal settles; a settled close above 3,097.50 negates this count."}
lt=d['ew']['long_term']
lt['proj']={"bull":lt['proj']['bull'],"base":[[lt['now_x'],m3],[0.78,2800],[0.9,2950],[1.0,3080]],"bear":[[lt['now_x'],m3],[0.8,2700],[1.0,2633]]}
EWP=("REVIEWED 21-NOVEMBER ON THE 20-NOVEMBER OFFICIAL (WEEKLY CLOSE) - COUNT HELD, PRICE IN THE COMPLETION ZONE: three-month settled 2,845.00 on 19-November and 2,831.50 on 20-November, inside 2,830-2,850. No cardinal rule is broken: wave (ii) at 3,289 holds below the 3,374 origin, wave (iii) ($294.50) is not the shortest, and wave (iv) at 3,097.50 stays clear of the 3,183 wave (i) low. Neither settlement is added as a pivot because no reversal has confirmed a low. BASE CASE (about 55%): wave (v) completes in 2,800-2,850, ending the C wave from 3,374, followed by a corrective rebound toward 2,994.50-3,097.50. ALTERNATE (about 45%): an extended (v) toward 2,788 (1.618 x (i)) and possibly 2,700. INVALIDATION of the count: a settled close above 3,097.50; of the bearish C-wave count, 3,289. Confidence low. ")
EWL=("REVIEWED 21-NOVEMBER (WEEKLY CLOSE BELOW 2,894): the week closed with three-month at 2,831.50, $62.50 below the 2,894 weekly 61.8% retracement - the pre-stated condition that lifts the alternate toward the 78.6% retracement near 2,633 to about 35%. The base case (about 65%) remains a correction completing near 2,800-2,850 before a rebound; a weekly close back above 2,994.50 would favour a completed correction. Loses preference only on a weekly close above 3,110. Confidence moderate. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 20-NOVEMBER'),k
    d['ew'][k]['writeup']=pfx+w
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="92.6",day="about $92.57 on 20-November (+0.6%, Trading Economics; page commentary differs on direction); third straight weekly decline, month -14.9%; Straits Daily Brief $92.56",
 note="REFRESHED SATURDAY 21-NOVEMBER-2026 (Trading Economics, 20-November session): weighed by ample supply - the IEA projects a ~2 mb/d surplus this quarter and Goldman Sachs warns of oversupply next year; the US Energy Secretary said Hormuz oil flows reached record levels (contrasting with transit-count trackers - see Hormuz risk); concerns about renewed US strikes on Iran lend some support. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="88.5",day="about EUR 88.45/MWh on 20-November (+4.7%; stats section shows EUR 89.54, +6.0% - sections differ)",
 note="REFRESHED SATURDAY 21-NOVEMBER-2026 (Trading Economics): lower Norwegian exports (Troll field outage) and colder Northwest-Europe forecasts lifted prices; EU storage about 69.8% on 19-November vs 81.2% a year earlier. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="103.84",day="about 103.84 on 20-November (-0.05%, Trading Economics); up about 0.5% on the week, a fourth straight weekly gain; +2.0% over the month",
 note="REFRESHED SATURDAY 21-NOVEMBER-2026 (Trading Economics): Governor Waller suggested a 50bp December hike could be considered; markets price 25bp in December, another in January and at least one more before end-2027; fed funds 4.00%. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.09820',day="LME fixing on 20-November, down from 1.09980 on 19-November",note="REFRESHED SATURDAY 21-NOVEMBER-2026 to the 20-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 20-NOVEMBER-2026 LME OFFICIAL, the last trading session before the weekend. THIS SATURDAY 21-NOVEMBER RUN IS COMPILED AT ABOUT 02:40 LONDON; THERE IS NO LME RING ON SATURDAY OR SUNDAY, so the board is CARRIED ON FRIDAY'S OFFICIAL because the market is shut - it is not lagging. The board rolled TWO sessions this run (19- and 20-November, both published after the previous run, which carried 18-November). Nothing was estimated. The Trading Economics aluminium reference (about $2,839.75, -1.00% for 20-November) is a CFD reference cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (21-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 20-November session (aluminium cash 3,184.50, three-month 2,831.50, stock 223,525; EUR/USD MTLE 1.09820); the aluminium, copper, nickel, zinc and lead per-metal daily tables all show 20-November as their newest row with NO later row, confirming the board is complete for the week. AL Circle's 19-November cash offer of $3,105/t and three-month offer of $2,845/t match the 19-November officials.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 26-October to 18-November rows match the stored series; the copper, nickel, zinc and lead fifteen-session windows (02-November to 20-November) were asserted equal to the re-fetched per-metal tables; each metal's 19- and 20-November stock changes reconcile with the prior session.")
C[3]=("STOCK CHANGES 19-November / 20-November: aluminium -1,725 to 224,425 / -900 to 223,525 (draws resumed after the 18-November build); copper +125 to 327,525 / +4,500 to 332,025; nickel +1,002 to 275,118 / +66 to 275,184; zinc -575 to 146,200 / -525 to 145,675; lead -2,675 to 266,325 / -4,800 to 261,525.")
c4=C[4]; k=c4.find("The price chart ax"); assert k>0
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (20-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (fifteen sessions, 02-20 November) as their latest point. "
 "The price chart axis (floor 2,700, ceiling 3,450) brackets cash 3,184.50 and three-month 2,831.50 ($131.50 above the floor; it will be lowered again if three-month approaches 2,750); the stock chart axis floor of 190,000 t leaves 33,525 t headroom below visible stock of 223,525 t; both are re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,184.50 against three-month $2,831.50 is therefore a $353.00 BACKWARDATION, up from $260.00 on 19-November. On 18, 19 and 20 November spread and flat price moved in OPPOSITE directions (cash up, three-month down). Press figures for the spread differ by measure and time; the dashboard uses the settled officials only."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $92.6), the dollar index (about 103.84) and TTF (about EUR 88.45/MWh) are Trading Economics readings for the Friday 20-November session; Trading Economics prices are contract-for-difference references, not official benchmarks, and its Brent and TTF pages again showed differing figures in different sections, so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (21-November) shows Brent $92.56; its only maritime-authority-confirmed incident is the UKMTO-reported 20-November tanker fire - all other incident items are media reports or Iranian claims."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 21-NOVEMBER (SATURDAY, WEEKEND): no authorised fetch was blocked. Westmetall EN and DE overviews and all five per-metal tables, Trading Economics aluminium/Brent/TTF/dollar, AL Circle news and the Straits Daily Brief were fetched. mining.com search returned HTTP 403 (not retried by any other client) and the S&P Global Q4 premium article returned 403; WebSearch was used instead. Searches for Q1-2027 Japanese premium offers located none (S&P Global reported participants expect Q1 pressure, with talk of $190-200/t - an expectation, not an offer). An official US-Canada aluminium tariff deal was again not located, so it stays pending."); hit+=1
assert hit==2,hit

d['so_what']={"line":"LME aluminium closed the week with its curve at its steepest: three-month fell to $2,831.50 - a weekly close below the $2,894 support - while cash rose to $3,184.50, a record-for-this-series $353 backwardation, and LME stocks resumed drawing.",
 "points":[
 "WHAT MOVED: over Thursday and Friday three-month slipped $33.50 to $2,831.50 (about -6.2% on the week) while cash climbed $89.50 to $3,184.50, so the backwardation (cash above three-month) widened to $353.00 from $230.00; visible LME stock fell 2,625 t to 223,525 t and cancelled warrants dropped to 18,450 t.",
 "WHY: the forward is pricing macro risk and a looser 2027 - the dollar logged a fourth weekly gain, a Fed governor floated a 50bp December hike, copper lost nearly 10% on the week, and forecasts cited by Trading Economics see an 830 kt surplus next year - while prompt metal stays scarce; Emkay Global still sees a ~400 kt deficit through 2028.",
 "SUPPLY AND ENERGY: Hormuz remains effectively closed, with 48 vessels holding and a UKMTO-confirmed tanker strike on 20-November; European gas jumped about 5% on a Norwegian outage, a reminder of smelter power-cost risk.",
 "WHAT TO WATCH: Monday's official against the $2,800-2,850 zone (a settle below about $2,803 opens a deeper leg), whether the $353 backwardation keeps pulling metal onto the LME, and first Q1-2027 Japanese premium offers."]}

d['feed']=([
 {"when":"Fri 20-Nov","impact":"Bearish","text":"20-NOVEMBER OFFICIAL (WEEKLY CLOSE): three-month $2,831.50 (-$13.50), weekly close below 2,894; cash $3,184.50 (+$79.50); backwardation $353.00, widest in series; stock -900 t to 223,525 t."},
 {"when":"Thu 19-Nov","impact":"Mixed","text":"19-NOVEMBER OFFICIAL: three-month $2,845.00 (-$20.00); cash $3,105.00 (+$10.00); backwardation $260.00; stock -1,725 t; cancelled warrants -9% to 18,450 t (AL Circle)."},
 {"when":"Fri 20-Nov","impact":"Bullish","text":"HORMUZ: UKMTO confirms a tanker caught fire after a projectile strike near the Strait; 48 vessels holding (Straits brief)."},
 {"when":"Fri 20-Nov","impact":"Bearish","text":"MACRO: dollar index fourth weekly gain (~103.84); Fed's Waller floats 50bp December hike (Trading Economics)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM WEEK CLOSES BELOW 2,894 AS BACKWARDATION HITS $353. The Friday 20-November official left three-month at $2,831.50 (Thursday $2,845.00), the lowest in this series and about 6.2% down on the week, while cash rose to $3,184.50 (Thursday $3,105.00) - a $353.00 backwardation, the widest in this series, with cash up and three-month down for a third session. Visible stock fell 1,725 t and 900 t to 223,525 t. Board three-month moves Thursday-Friday: copper -4.20%, nickel -3.10%, zinc -2.71%, aluminium -1.17%, lead -0.16%."},
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":S_AC,
  "headline":"LME CANCELLED WARRANTS FALL 9% (AL Circle, 20-November): on 19-November opening stocks were 226,150 t (+2.63%), live warrants 205,975 t and cancelled warrants down 1,825 t to 18,450 t; cash offer $3,105/t, three-month offer $2,845/t, December-2027 offer $2,788/t; three-month Asian Reference Price $2,869.5/t; LME alumina (Platts) $398/t."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Mixed","url":S_ST,
  "headline":"HORMUZ: UKMTO CONFIRMS TANKER STRIKE (Straits Daily Brief, 21-November): a tanker caught fire after a projectile struck it near the Strait while outbound on 20-November - the only maritime-authority-confirmed incident; Iranian claims of supertankers striking mines remain unconfirmed. Latest IMF PortWatch count 2 transits on 15-November vs 85/day pre-crisis; 48 vessels holding. Iranian-linked reporting says Tehran would reopen if the US meets its commitments; no agreement announced."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"DOLLAR'S FOURTH WEEKLY GAIN; 50BP FLOATED (Trading Economics, 20-November): the dollar index held near 103.84, up about 0.5% on the week; Governor Waller suggested a 50bp December hike could be considered; markets price 25bp in December and another in January. Brent about $92.6 on a third weekly decline."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish (cost)","url":S_TG,
  "headline":"EUROPEAN GAS JUMPS ON TROLL OUTAGE (Trading Economics, 20-November): TTF rose about 4.7% to about EUR 88.45/MWh as lower Norwegian exports and colder forecasts met EU storage near 69.8% (81.2% a year earlier) - higher power-cost risk for European smelters."},
 {"theme":"Policy","horizon":"Structural","impact":"Mixed","url":S_KZ,
  "headline":"KAZAKHSTAN-EU ALUMINIUM TRADE AND CBAM (AL Circle, 20-November): Kazakhstan's aluminium exports to the EU reached 110,184 t as the EU carbon border mechanism adds compliance demands for exporters."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])

for p in d['producer_status']:
    p['asof']=RD

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 20-Nov-2026 session (EN and DE overviews agree; Al/Cu/Ni/Zn/Pb per-metal tables newest row 20-Nov, no later row - weekend)",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_AC,S_AC],[L_KZ,S_KZ]): d['sources'].append(x)
for x in ([L_AC,S_AC],[L_TD,S_TD],[L_ST,S_ST],[L_TG,S_TG]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-18',3095.0,2865.0,226150]
ph['rows'][-1]=['2026-11-20',cash,m3,stk]; ph['updated']=RD   # same week (w/c 16-Nov): replace the week's row with its last session
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2),round(wk,2),d['metals_board'])
