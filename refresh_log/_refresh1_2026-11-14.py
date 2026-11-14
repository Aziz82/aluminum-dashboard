# Daily data refresh - 2026-11-14 (SATURDAY, ~02:40 UTC; market shut). Board ROLLED ONE SESSION to the FRIDAY 13-Nov LME official.
# Westmetall cache-busted EN + DE overviews agree on 13-Nov (Al cash 3,150.50 / 3M 3,018.00 / stock 224,150; MTLE 1.10510);
# aluminium per-metal table newest row 13-Nov (no later row) and its 29-Oct..12-Nov rows match the stored series.
# 3M 3,018.00 settled BELOW the 3,024.50 bear trigger -> pre-registered rule FIRES: five points bull->bear, 15/45/40 -> 10/45/45.
# EW daily: below 3,024.50 strengthens the alternate (~65/35), no re-label (2,994.50 not broken).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-14'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-14"; L_ST="Straits Daily Brief - Strait of Hormuz, 14-Nov-2026 (ticker AI-assisted)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~3,009 (-0.33%) on 13-Nov-2026 (CFD reference); intraday low 2,983, lowest since October"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$96.08 (+0.27%), second weekly decline (13-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.41 (+0.23%), highest since early 2025; ~85-91% odds of a December hike (13-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 89.7/MWh (-2.8%), up >6% on the week; EU storage below 72% (13-Nov-2026)"
S_AN="https://news.metal.com/newscontent/104189945-shandong-aluminum-producer-raises-november-prebaked-anode-tender-price-by-182-yuanmt-mom"; L_AN="SMM - Shandong aluminium producer raises November prebaked anode tender price by Yuan 182/t to Yuan 6,312/t (02-Nov-2026)"
S_AF="https://news.metal.com/newscontent/ATJLBE5WYX3LPMPXCOZWUWFNORIZ45F2RFLM7KQ-weakening-cost-support-for-anodes-low-aluminum-fluoride-inventory-underpins-spot-cargo-smm-analysis"; L_AF="SMM - Weakening cost support for anodes; low aluminium fluoride inventory underpins spot cargo (13-Nov-2026)"
S_GH="https://www.alcircle.com/news/ghana-to-ban-raw-bauxite-exports-by-2030-under-1-5bn-processing-plan-121957"; L_GH="AL Circle - Ghana to ban raw bauxite exports by 2030 under $1.5bn processing plan (13-Nov-2026)"
S_RT="https://www.alcircle.com/news/20m-tonnes-more-rio-tinto-launches-2-6bn-kangwinan-project-121959"; L_RT="AL Circle - Rio Tinto launches $2.6bn Kangwinan bauxite project, +20 Mt/yr at Weipa (13-Nov-2026)"
S_US="https://www.alcircle.com/news/us-aluminium-tariffs-continue-to-push-up-costs-for-manufacturers-and-consumers-121953"; L_US="AL Circle - US aluminium tariffs continue to push up costs for manufacturers and consumers (13-Nov-2026)"

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3155.5 and B['LME 3-month']['cur']==3032.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3155.5,3032.0,226350
cash,m3,stk=3150.5,3018.0,224150
spr=cash-m3; psp=pc-pm; assert spr==132.5 and psp==123.5 and ps-2200==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED SATURDAY 14-NOVEMBER-2026 ABOUT 02:40 LONDON. THE MARKET IS SHUT (NO RING ON SATURDAY OR SUNDAY), SO THE BOARD IS THE FRIDAY 13-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION AND THE CORRECT FIGURE TO CARRY UNTIL MONDAY 16-NOVEMBER 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 13-November official for all metals with stocks and FX (EUR/USD MTLE 1.10510; 12-November 1.10880); (2) the aluminium per-metal daily table shows 13-November as its newest row, with NO later row, and its 29-October to 12-November rows match the stored series exactly. "
 "The whole board sits on ONE UNIFORM SESSION (13-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" FRIDAY 13-NOVEMBER (the board): CASH SETTLED $3,150.50, DOWN $5.00 OR 0.16% FROM $3,155.50. THREE-MONTH SETTLED $3,018.00, DOWN $14.00 OR 0.46% FROM $3,032.00 - THE FIRST SETTLED CLOSE BELOW THE 3,024.50 BEAR TRIGGER ($6.50 beneath it), $23.50 above the 2,994.50 October low and $7.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION WIDENED TO $132.50 FROM $123.50 WHILE FLAT PRICE FELL - SPREAD AND PRICE MOVED IN OPPOSITE DIRECTIONS (tighter prompt, lower forward): three-month fell nearly three times as much as cash. A twenty-second straight backwardation and the eleventh above $15.00. "
 "VISIBLE LME STOCK FELL 2,200 t TO 224,150 t, another new series low, an eighteenth straight draw and the largest daily draw in weeks. The Trading Economics aluminium reference showed about $3,009 (-0.33%) for 13-November, with an intraday low of 2,983 - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,150.5","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,018.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $59.00 BELOW THE 3,077 WEEKLY 50% RETRACEMENT and $43.50 below the 3,061.5 July low, $130.50 beneath the 3,148.5 wave (iv) high and $271.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a twenty-first session, $23.50 below."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+132.5","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,150.50 against three-month $3,032.00... CORRECTION: against three-month $3,018.00 is a $132.50 BACKWARDATION, WIDER than 12-November's $123.50 as cash fell only $5.00 and three-month $14.00 - SPREAD AND PRICE MOVED IN OPPOSITE DIRECTIONS (structure tighter, price lower). It stays above the published $15.00 reversal condition for an eleventh session and is a twenty-second straight backwardation; a contango beyond $24.50 would reverse the structural signal. The October mean spread was $"+f"{oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"224,150","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 2,200 t TO 224,150 t (12-November: -375 t to 226,350 t), another new series low and an eighteenth straight draw - the largest daily draw in weeks. October's mean stock was {oct_s:,} tonnes."},
]
# tidy the spread card wording (no self-correction text)
d['kpi_cards'][2]['delta']=d['kpi_cards'][2]['delta'].replace("Cash $3,150.50 against three-month $3,032.00... CORRECTION: against three-month $3,018.00","Cash $3,150.50 against three-month $3,018.00")
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 12-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $3,018.00, DOWN $14.00 FROM THE 12-NOVEMBER $3,032.00 - the FIRST settled close below the 3,024.50 bear trigger and $59.00 below 3,077; $23.50 above the 2,994.50 October low; $7.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 2,200 t TO 224,150 t, another new series low (12-November 226,350 t). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $132.50 BACKWARDATION, WIDER THAN 12-NOVEMBER'S $123.50 (11-November series-record $159.50). CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On Friday cash fell $5.00 and three-month $14.00, so STRUCTURE TIGHTENED WHILE PRICE FELL (OPPOSITE directions). REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50 and $132.50."},
 {"name":"EUR/USD LME fixing","cur":1.1051,"prev":1.1088,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.10510 ON 13-NOVEMBER FROM 1.10880 ON 12-NOVEMBER as the dollar index rose to its highest since early 2025. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (13-Nov official)","price":"3,150.5","basis":"THE FRIDAY 13-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,150.50, DOWN $5.00 OR 0.16% (12-November $3,155.50). Market shut over the weekend; next official Monday 16-November 13:20 London."},
 {"tenor":"3-month (13-Nov official)","price":"3,018.0","basis":"THE 13-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $3,018.00, DOWN $14.00 - $6.50 BELOW the 3,024.50 bear trigger (first settled close beneath it), $59.00 below 3,077 and $23.50 above the 2,994.50 October low."},
 {"tenor":"Cash-to-3M structure","price":"+132.5 (BACKWARDATION)","basis":"A $132.50 BACKWARDATION, WIDER than $123.50 with price LOWER (OPPOSITE directions) - above the $15.00 reversal condition for an eleventh session."},
 {"tenor":"Visible LME stock","price":"224,150 t","basis":f"DOWN 2,200 t to a new series low on 13-November (eighteenth straight draw); October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PROMPT TIGHTENS AGAIN WHILE THE FORWARD PRICE BREAKS LOWER. On the 13-November official cash $3,150.50 sits $132.50 ABOVE three-month $3,018.00, a BACKWARDATION, wider than $123.50 on 12-November as three-month fell $14.00 and cash only $5.00 - SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50 and now $132.50. "
 f"READ: a twenty-second straight backwardation, the eleventh above $15.00, with visible stock down 2,200 t to another low (224,150 t) - nearby LME metal stays scarce even as the forward price slips below the bear trigger; that divergence says the weakness is in deferred/macro pricing (a strong dollar), not in prompt physical availability. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2900,3450] and d['chart_stock_axis']==[200000,255000]

ls=d['lme_series']; assert ls[-1][0]=='12-Nov'
d['lme_series']=ls[1:]+[["13-Nov",cash,m3,stk]]
assert len(d['lme_series'])==15 and all(200000<r[3]<255000 and 2900<r[2]<3450 and 2900<r[1]<3450 for r in d['lme_series'])
CU=(13610.0,13545.0,329100); NI=(16025.0,16230.0,272724); ZN=(3745.0,3705.0,142625); PB=(1853.0,1886.0,283350)
CU6=(13712.0,13655.0,328600); NI6=(16010.0,16215.0,272526); ZN6=(3760.5,3722.0,142625); PB6=(1843.0,1879.0,286650)
assert CU6[2]+500==CU[2] and NI6[2]+198==NI[2] and ZN6[2]==ZN[2] and PB6[2]-3300==PB[2]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU6[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI6[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN6[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB6[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU6[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI6[1],1)
zn9=[3935.0,3869.0,3875.0,3877.0,3759.0,3754.0,3768.0,3794.0,3760.5]; pb9=[1869.5,1862.0,1858.0,1866.5,1857.0,1854.0,1846.0,1845.0,1843.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zn9)+ZN[0])/10)/(sum(zn9)/9),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(pb9)+PB[0])/10)/(sum(pb9)/9),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU6[0]),('NI',NI[0],NI6[0]),('ZN',ZN[0],ZN6[0]),('PB',PB[0],PB6[0])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-11-13'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending FRIDAY 13-NOVEMBER-2026 (market shut Saturday 14-November). THE WINDOW ROLLED ONE SESSION THIS RUN: 23-October dropped, 13-November appended, so the window is 26-October to 13-November. Every point is an official cash settlement from the Westmetall per-metal tables and English/German overviews (13-November read from both overviews, which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (13-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,CU6,f" COPPER 13-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU6[0])}; three-month ${CU[1]:,.2f}, {chg(CU[1],CU6[1])}. BACKWARDATION widened to $65.00 from $57.00. Stock rose 500 t to 329,100 t."),
 ("Nickel",NI,NI6,f" NICKEL 13-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI6[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI6[1])}. CONTANGO unchanged at $205.00, still the widest carry on the board. Stock rose 198 t to 272,724 t."),
 ("Zinc",ZN,ZN6,f" ZINC 13-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN6[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN6[1])}. BACKWARDATION $40.00 from $38.50. Stock unchanged at 142,625 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,PB6,f" LEAD 13-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB6[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB6[1])}. CONTANGO $33.00 from $36.00. Stock fell 3,300 t to 283,350 t, the largest draw on the board."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Friday 13-November official three-month copper fell 0.81%, aluminium 0.46% and zinc 0.46%, while lead rose 0.37% and nickel 0.09%. Trading Economics reports the dollar index near 103.41, its highest since early 2025, with roughly 85-91% odds of a Fed hike at the 09-December meeting; Brent about $96.1. The LME euro fixing fell to 1.1051.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,c6,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='12-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["13-Nov",CU[0]]]; assert len(i['hist'])==15
        i['val']="~13,545.00 (3M); 13,610.00 (cash) $/t"; i['ratio']="~13,610.00 $/t cash vs LME 3M 13,545.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the FRIDAY 13-NOVEMBER-2026 session at $13,610.00 (12-November $13,712.00). THE WINDOW ROLLED THIS RUN: 23-October dropped and 13-November appended, so the series is the last fifteen published official cash sessions, 26-October to 13-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English/German overviews. "
                  "Copper structure for context: backwardation $65.00 on 13-November; stock 329,100 t (+500 t).")
    elif i['name'].startswith('Pre-baked anodes'):
        assert i['hist'][-1]==['Oct-26',6130]
        i['hist']=i['hist']+[['Nov-26',6312]]
        i['val']="~6,312"; i['trend']='up'
        i['src']=("UPDATED 14-NOVEMBER: THE NOVEMBER-2026 SETTLEMENT CYCLE IS APPENDED (it printed 02-November and had not been captured by earlier runs). SMM (02-November) reports a large Shandong aluminium producer raised its November prebaked-anode tender price by Yuan 182/t month on month to Yuan 6,312/t (cash; Yuan 6,328/t by acceptance) - consistent with the October Yuan 6,130/t base already in this series. NOTE: a separate SMM analysis (13-November) quotes the same Yuan 6,312/t benchmark as 'up 1.32% MoM', which does not reconcile with +182 on 6,130 (+2.97%); the tender figures are used. SMM (13-November) adds that petroleum coke weakened in November and pitch moved sideways, so anode production cost edged lower, and that environmental controls in Shandong, Henan and Hebei cut anode operating rates; export FOB offers rose $20-30/t. Sources: "+S_AN+" ; "+S_AF+" . Single-smelter benchmark, Yuan/t, not a national average. EARLIER: "+i['src'])
    elif i['name'].startswith('Aluminium fluoride'):
        i['src']=("REVIEWED 14-NOVEMBER: SMM (13-November) reports November aluminium fluoride benchmark TENDER prices held steady at Yuan 12,600-13,000/t, with spot order prices up about Yuan 200/t on low inventory. That is a TENDER basis, different from the mainstream spot basis charted here, so it is NOT appended to the history (gaps stay gaps). Source: "+S_AF+" . "+i['src'])
s=d['inputs_summary']; assert s.startswith("UPDATE 13-NOVEMBER")
d['inputs_summary']=("UPDATE 14-NOVEMBER: Copper rolled one session to the Friday 13-November LME official cash of $13,610.00 (window 26-October to 13-November). ONE NEW CARBON MARK APPENDED: the November prebaked-anode tender at a large Shandong smelter rose Yuan 182/t to Yuan 6,312/t (SMM, 02-November), a second straight monthly increase - although SMM (13-November) says petroleum coke weakened in November and pitch moved sideways, so cost support is now easing. Aluminium fluoride November tenders held at Yuan 12,600-13,000/t (tender basis, not appended). Energy was mixed on Friday: Brent about $96.1 heading for a second weekly decline, European gas about EUR 89.7/MWh (-2.8%) but up more than 6% on the week with EU storage below 72% (Trading Economics). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
ptl=0.5*pc; presid=2403-ptl; pshare=ptl/2403*100
OT=f"the tariff leg of the US duty-paid premium is 0.50 times the 12-November official cash of $3,155.50, or ${ptl:,.2f}, DOWN $34.00 against the 11-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${presid:,.2f}, so {pshare:.1f}%"
NT=f"the tariff leg of the US duty-paid premium is 0.50 times the 13-November official cash of $3,150.50, or ${tl:,.2f}, DOWN ${ptl-tl:,.2f} against the 12-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OC1="COMPILED FRIDAY 13-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE THURSDAY 12-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; FRIDAY'S OFFICIAL PRINTS 13:20 LONDON)."
NC1="COMPILED SATURDAY 14-NOVEMBER-2026 WITH THE MARKET SHUT (LME BOARD ON THE FRIDAY 13-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; NEXT OFFICIAL MONDAY 16-NOVEMBER 13:20 LONDON)."
for p in d['premiums']:
    assert OT in p['src'] and OC1 in p['src'],p['name']
    p['src']=p['src'].replace(OT,NT).replace(OC1,NC1)
ra=398.24/m3*100; pra=398.24/pm*100
OR=f"THE RATIO: LME Alumina at $398.24/t against the 12-November aluminium three-month of $3,032.00 is {pra:.2f}%"
for a in d['alumina']:
    assert OR in a['src'],a['name']
    a['src']=a['src'].replace(OR,f"THE RATIO: LME Alumina at $398.24/t against the 13-November aluminium three-month of $3,018.00 is {ra:.2f}%").replace(OC1,NC1)
OC0="COMPILED FRIDAY 13-NOVEMBER-2026 ABOUT 02:40 LONDON; THE BOARD IS THE THURSDAY 12-NOVEMBER-2026 LME OFFICIAL."
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace(OC1,NC1).replace(OC0,"COMPILED SATURDAY 14-NOVEMBER-2026 ABOUT 02:40 LONDON (MARKET SHUT); THE BOARD IS THE FRIDAY 13-NOVEMBER-2026 LME OFFICIAL.")
        o=o.replace("REVIEWED 13-NOVEMBER: no newer public disclosure","REVIEWED 14-NOVEMBER: no newer public disclosure").replace("REVIEWED 13-NOVEMBER. NO NEW DATED","REVIEWED 14-NOVEMBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status','inputs','logistics','raw_materials'):
    if k in d: d[k]=walk(d[k])

d['lme_commentary']=("BEAR TRIGGER HIT ON THE FORWARD, PROMPT TIGHTER STILL. The Friday 13-November official cut three-month $14.00 to $3,018.00 - the first settled close below the 3,024.50 bear trigger - while cash eased only $5.00 to $3,150.50, so the backwardation WIDENED to $132.50 (a twenty-second straight backwardation): spread and price moved in OPPOSITE directions. Visible stock fell 2,200 t to a new low of 224,150 t, the largest draw in weeks. "
 "The pre-registered rule fired: five points move from bull to bear (15/45/40 to 10/45/45); the daily Elliott alternate strengthens to about 65%, still without a re-label because 2,994.50 held. "
 "The pressure is macro, not physical: the dollar index rose to about 103.41, its highest since early 2025, with roughly 85-91% odds of a Fed hike on 09-December (Trading Economics), and the Trading Economics reference touched 2,983 intraday, its lowest since October. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" its October mean.")
d['net_read']=("NET: NEUTRAL-TO-BEARISH ON THE FORWARD, STILL TIGHT ON THE PROMPT. Against: three-month at $3,018.00 is below the 3,024.50 bear trigger and $59.00 under the 3,077 bull trigger; a dollar index near 103.41, highest since early 2025, with a December Fed hike largely priced; more Gulf metal returning through Q1-2027. "
 "Supportive: a $132.50 backwardation that widened as price fell (twenty-second straight, eleventh above $15.00), visible LME stock at a new low of 224,150 t, Hormuz still listed closed with further unverified incident claims, and European gas up more than 6% on the week.")
d['bottom_line']=("BOTTOM LINE: LME aluminium three-month fell $14.00 to $3,018.00 on the Friday 13-November official - the first settled close below the 3,024.50 bear trigger - while cash eased only $5.00 to $3,150.50, widening the backwardation to $132.50 and taking visible stock down 2,200 t to another low of 224,150 t. The forward curve is weakening on a strong dollar while nearby metal stays scarce. "
 "Weights move to 10% bull / 45% base / 45% bear under the pre-registered rule. A settled close back above 3,042 returns the five points to bull; a settled close below 2,994.50 ends the Elliott base count and adds further bear weight; a contango beyond $24.50 would confirm the bear case structurally. Daily Elliott invalidation 3,289. Market shut for the weekend; next official Monday 16-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, PROMPT PREMIUM STILL HIGH BUT OFF ITS RECORD:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, PROMPT PREMIUM WIDENS AS THE FORWARD BREAKS LOWER: a $132.50 backwardation on 13-November, wider than $123.50 as three-month fell $14.00 and cash only $5.00 - an eleventh print above the $15.00 reversal condition, so nearby metal is still valued well over forward metal and there is no carry reward for deferring purchases; the outright three-month price settled $6.50 BELOW the 3,024.50 bear trigger and $59.00 below the 3,077 bull trigger, so forward pricing is softening while prompt metal is not. "+c2[a1:]
o=f"is ${ptl:,.2f} on 12-November cash, {pshare:.1f}% of the $2,403/t premium"; assert o in c2; c2=c2.replace(o,f"is ${tl:,.2f} on 13-November cash, {share:.1f}% of the $2,403/t premium")
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find(" Hindalco's",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 13-November official cut three-month to $3,018.00, below the 3,024.50 bear trigger and $23.50 above the 2,994.50 settled low; the dollar index near 103.41, highest since early 2025, with a 25bp Fed hike widely expected on 09-December (Trading Economics 13-November); Brent about $96.1 and European gas about EUR 89.7/MWh, up more than 6% on the week; November Shandong prebaked-anode tender up Yuan 182/t to Yuan 6,312/t (SMM 02-November) though petcoke is now weakening (SMM 13-November); EGA reported 9M-2026 adjusted EBITDA of $1.572bn at a 29.8% margin with 766 of 1,262 Al Taweelah cells restarted and full restart targeted for Q1-2027 (AL Circle 12-November); Ghana plans to ban raw bauxite exports by end-2030 (AL Circle 13-November); a possible US-Canada deal cutting the US tariff on Canadian aluminium to 25% remains unconfirmed; Maaden (1211) reported Q3-2026 aluminium EBITDA of $419m (Arab News 09-November);"+c2[b1:]
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("RULE FIRED 14-NOVEMBER - 15/45/40 TO 10/45/45: the Friday 13-November official settled three-month at $3,018.00, $6.50 BELOW 3,024.50 (the pre-registered bear trigger), so five points move from bull to bear. The $132.50 backwardation (wider, not a contango) and record-low stock are why the move is held to the minimum five points and taken from bull, not base. REVERSAL: a settled close back above 3,042 returns the five points to bull; a settled close below 2,994.50, or a contango beyond $24.50, adds further bear weight. ")+s['drivers']
    s['prob']={'Bull':'10%','Base':'45%','Bear':'45%'}[s['case']]
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 14-NOVEMBER: the 13-November official printed a $132.50 BACKWARDATION, wider than $123.50 even as three-month fell below the bear trigger - an eleventh session above $15.00. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 14-NOVEMBER: LME stock fell 2,200 t on 13-November to a new low of 224,150 t, an eighteenth straight draw and the largest daily draw in weeks. Trend held at FLAT pending a second large draw: a single print does not establish a faster pace."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 14-NOVEMBER: Brent held near $96.1 but is heading for a second weekly decline as Saudi output rose 26% in October and US crude stocks built 4.66 Mb (Trading Economics); European gas eased 2.8% to about EUR 89.7/MWh on Friday yet rose more than 6% on the week on the Troll outage, colder forecasts and EU storage below 72%. China's November anode tender rose Yuan 182/t, but SMM says petcoke is now weakening. Trend held at FLAT."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 14-NOVEMBER: Straits Daily Brief - strait still listed CLOSED, traffic near a standstill; lagged count 3 transits on 08-November (vs 85/day pre-crisis); AIS-visible vessels holding 38 (likely an undercount). Iran's Revolutionary Guard claims a gas carrier struck a mine and caught fire, and claims a US drone was downed - both unverified by any maritime or independent authority. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 14-NOVEMBER: the dollar index rose to about 103.41 (+0.23%), its highest since early 2025, after October producer prices rose 6.5% year on year; markets widely expect a 25bp Fed hike on 09-December (Trading Economics cites about 85% and about 91% in different notes). It coincided with three-month aluminium breaking the bear trigger. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('TARIFF POLICY'):
        r['risk']+=" UPDATE 14-NOVEMBER: AL Circle (13-November) reiterates the 50% Section 232 rate continues to raise US manufacturer and consumer costs; still no official confirmation of the reported US-Canada deal. Trend held at FLAT."; r['trend']='flat'; hit+=1
assert hit==6,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Fri 13-Nov':
        hc+=1; cat['date']='Daily, from Mon 16-Nov'
        cat['event']=("FRIDAY 13-NOVEMBER OFFICIAL: three-month $3,018.00 (-$14.00), cash $3,150.50 (-$5.00), backwardation $132.50 - the BEAR RULE FIRED (first settled close below 3,024.50), weights now 10/45/45. NEXT (from Monday 16-November): a settled close back above 3,042 returns five points to bull; a settled close below 2,994.50 ends the Elliott base count and adds bear weight; below about 2,977.5 forces a re-count toward 2,894. Invalidation 3,289. LME November prompt expiry and rollover; Fed meeting 09-December (hike widely expected); any official US-Canada tariff announcement; first Q1-2027 Japanese premium offers.")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"SATURDAY 14-NOVEMBER ON THE FRIDAY 13-NOVEMBER OFFICIAL: three-month fell $14.00 to $3,018.00, the first settled close below the 3,024.50 bear trigger, while cash eased only $5.00 to $3,150.50, so the backwardation widened to $132.50 and stock fell 2,200 t to a new low of 224,150 t. The weakness is in the forward price and tracks a dollar at its highest since early 2025 on December Fed-hike pricing, not a loosening of nearby supply. The pre-registered rule moved five points from bull to bear (10/45/45). The next test is the 2,994.50 October low: a settled break ends the Elliott base count; a recovery above 3,042 reverses Friday's shift.")

EWP=("REVIEWED 14-NOVEMBER ON THE 13-NOVEMBER OFFICIAL: three-month settled 3,018.00 (-14.00), BELOW 3,024.50 - the pre-registered level that STRENGTHENS THE ALTERNATE - so the alternate (the rebound from 2,994.50 to 3,097.50 was a completed corrective bounce, 3,064 a lower high, and a new leg down toward and below 2,994.50 is under way) rises to about 65% against about 35% for the base (a deep wave (ii) of C/3 that must hold 2,994.50). The count is NOT re-labelled: no invalidation level broke. A settled close below 2,994.50 ends the base count; below about 2,977.5 forces a re-count toward the 2,894 weekly 61.8%. A recovery above 3,042 would restore the 60/40 balance and above 3,097.50 the base toward 3,110 and 3,148.5. Invalidation 3,289; confidence low. ")
EWL=("REVIEWED 14-NOVEMBER (WEEK CLOSE): the week ended on the Friday official at 3,018.00, down from 3,050.00 a week earlier, below the 3,061.5 July low and well below the 3,077 50% retracement - REINFORCING the weekly base case, the corrective count toward the 61.8% retracement at 2,894, which loses preference only on a weekly close above 3,110. Alternate (2,994.50 completed the correction) cut to about 25%: the $132.50 backwardation and record-low stock still argue for it, but the forward price closed the week at its lowest since mid-October. Confidence moderate. ")
pre_s="REVIEWED 13-NOVEMBER ON THE 12-NOVEMBER OFFICIAL:"; pre_l="REVIEWED 13-NOVEMBER (LATE WEEK):"
assert d['ew']['short_term']['writeup'].startswith(pre_s) and d['ew']['long_term']['writeup'].startswith(pre_l)
d['ew']['short_term']['writeup']=EWP+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=EWL+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="96.1",day="about $96.08 on 13-November (+0.27%, Trading Economics); heading for a second weekly decline after a ten-week low of $91.5 on 10-November",
 note="REFRESHED SATURDAY 14-NOVEMBER-2026 (Trading Economics, 13-November): Brent hovered near $96 after the US President said the US no longer needs a deal with Iran; Saudi Arabia reported a 26% rise in October production and Middle Eastern exports are resuming; US crude inventories rose 4.657 Mb in the week to 06-November. The Straits Daily Brief (14-November) shows $96.08. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="89.7",day="about EUR 89.4-89.7/MWh on 13-November (-2.8%, Trading Economics; sections differ), up more than 6% on the week",
 note="REFRESHED SATURDAY 14-NOVEMBER-2026 (Trading Economics): Friday profit-taking after three sessions of gains; EU storage below 72% against a five-year average of about 89%, Germany below 60%; colder weather expected from 17-November; Norwegian flows weakened by the Troll outage. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="103.41",day="about 103.41 on 13-November (+0.23%, Trading Economics), highest since early 2025",
 note="REFRESHED SATURDAY 14-NOVEMBER-2026 (Trading Economics): firm inflation data (October producer prices +6.5% y/y) and hawkish Fed commentary; a 25bp hike on 09-December is widely expected (the page cites about 85% in one note and about 91% in another). SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.10510',day="LME fixing on 13-November, down from 1.10880 on 12-November",note="REFRESHED SATURDAY 14-NOVEMBER-2026 to the 13-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 13-NOVEMBER-2026 LME OFFICIAL, the latest published session. THIS RUN IS ON SATURDAY 14-NOVEMBER WITH THE MARKET SHUT (no ring on Saturday or Sunday), so the board was CARRIED from Friday because the market is closed - it is the correct figure until Monday 16-November's official at 13:20 London. The board rolled ONE session this run (from Thursday 12-November). The Trading Economics aluminium reference (about $3,009, -0.33% for 13-November) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (14-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 13-November session (aluminium cash 3,150.50, three-month 3,018.00, stock 224,150; EUR/USD MTLE 1.10510); the aluminium per-metal daily table shows 13-November as its newest row with NO later row, confirming the board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 29-October to 12-November rows match the stored series exactly; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 13-November values come from both overviews, which agree, and each metal's stock change reconciles with its 12-November stock.")
C[3]=("STOCK CHANGES 13-November (also shown in the pages' change column): aluminium -2,200 to 224,150; copper +500 to 329,100; nickel +198 to 272,724; zinc unchanged at 142,625; lead -3,300 to 283,350.")
c4=C[4]; k=c4.find("The price chart ax"); assert k>0
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (13-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (ten sessions, 02-13 November) as their latest point. ")+c4[k:]
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,150.50 against three-month $3,018.00 is therefore a $132.50 BACKWARDATION, wider than $123.50 on 12-November - on Friday the spread and the flat price moved in OPPOSITE directions (structure tighter, price lower)."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        o=f"the tariff leg is 0.50 times the 12-November official cash of $3,155.50, or ${ptl:,.2f}, leaving a ${presid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({pshare:.1f}% policy arithmetic)"
        assert o in cv
        C[i]=cv.replace(o,f"the tariff leg is 0.50 times the 13-November official cash of $3,150.50, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic)"); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $96.1), the dollar index (about 103.41) and TTF (about EUR 89.7/MWh) are Trading Economics readings for Friday 13-November; Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages again showed different levels in different sections (TTF 89.66 vs 89.40 vs about 91; dollar 103.411 vs 103.416; Fed-hike odds about 85% in one note and about 91% in another), so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (14-November) labels its ticker AI-assisted, and its incident items are flagged here as claims or unverified where the brief does so."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 14-NOVEMBER (SATURDAY): no authorised fetch was blocked (Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/TTF/dollar, AL Circle, news.metal.com and the Straits Daily Brief all fetched). news.metal.com's front page carried no dated aluminium items for 13-14 November; SMM articles were reached via search results (November anode tender; 13-November anode/fluoride analysis). An SMM link on India's anti-dumping probe returned 404 and is not used. SHFE/A00 price rows are not refreshed this run. mining.com was not fetched. A search for Q1-2027 Japanese premium offers again found none (talk of $190-200/t is expectation, not an offer), so Q1 stays unpriced. The November prebaked-anode settlement printed 02-November and was missed by earlier runs; it is appended this run."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        rest=cv.split("PEER EARNINGS:",1)[1].strip()
        C[i]=("PEER EARNINGS: NO NEW LISTED-PEER RESULT ADDED THIS RUN (14-NOVEMBER) and no earnings_history company was back-filled. EARLIER: "+rest); hit+=1
assert hit==4,hit

d['so_what']={"line":"LME aluminium three-month settled $3,018 on Friday 13-November - the first close below the $3,024.50 bear trigger, shifting the scenario weights to 10/45/45 - even as the backwardation widened to $132.50 and LME stock fell 2,200 t to a new low: the forward price is weakening on a strong dollar while nearby metal stays scarce.",
 "points":[
 "WHAT MOVED: the Friday 13-November official cut three-month 0.46% to $3,018.00 and cash 0.16% to $3,150.50, so the backwardation widened to $132.50 from $123.50 - spread and price moved in opposite directions; visible LME stock fell 2,200 t to 224,150 t, an eighteenth straight draw.",
 "WHY: the dollar index rose to about 103.41, its highest since early 2025, with a 25bp Fed hike widely expected on 09-December (Trading Economics); the weakness is in forward pricing, not in prompt availability.",
 "COSTS AND SUPPLY: China's November prebaked-anode tender rose Yuan 182/t to Yuan 6,312/t, though petcoke is now weakening (SMM); Brent about $96 and EU gas up more than 6% on the week; Ghana plans to ban raw bauxite exports by 2030 and Rio Tinto launched a $2.6bn, 20 Mt/yr Weipa bauxite project (AL Circle).",
 "WHAT TO WATCH (from Monday 16-November): a settled close below the $2,994.50 October low (bearish break) or back above $3,042 (reverses Friday's weight shift); the LME November prompt rollover; Hormuz, still listed closed."]}

d['feed']=([
 {"when":"Fri 13-Nov","impact":"Bearish","text":"13-NOVEMBER OFFICIAL: three-month $3,018.00 (-$14.00), first close below the 3,024.50 bear trigger; cash $3,150.50 (-$5.00); backwardation widens to $132.50; stock -2,200 t to 224,150 t."},
 {"when":"Fri 13-Nov","impact":"Bearish","text":"DOLLAR: index ~103.41, highest since early 2025; 25bp Fed hike widely expected 09-December (Trading Economics)."},
 {"when":"Fri 13-Nov","impact":"Mixed","text":"GHANA: raw bauxite export ban by end-2030 under a $1.5bn processing plan (AL Circle)."},
 {"when":"Fri 13-Nov","impact":"Mixed","text":"RIO TINTO: $2.6bn Kangwinan bauxite project, +20 Mt/yr at Weipa, first output 2029 (AL Circle)."},
 {"when":"Sat 14-Nov","impact":"Bullish","text":"HORMUZ: still listed closed; 38 vessels holding; IRGC claims a gas carrier hit a mine (unverified) (Straits Daily Brief)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM THREE-MONTH BREAKS THE BEAR TRIGGER; BACKWARDATION WIDENS TO $132.50. The Friday 13-November official settled three-month at $3,018.00 (-0.46%), the first close below 3,024.50 and $23.50 above the 2,994.50 October low, while cash eased only 0.16% to $3,150.50; visible stock fell 2,200 t to a new low of 224,150 t. Board: lead +0.37%, nickel +0.09%, aluminium -0.46%, zinc -0.46%, copper -0.81%."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"DOLLAR AT HIGHEST SINCE EARLY 2025 (Trading Economics, 13-November): the dollar index rose to about 103.41 after October producer prices rose 6.5% year on year and Fed officials sounded hawkish; a 25bp hike on 09-December is widely expected."},
 {"theme":"Raw materials","horizon":"0-1 month","impact":"Mixed (cost)","url":S_AN,
  "headline":"NOVEMBER ANODE TENDER UP YUAN 182/T (SMM, 02-November): a large Shandong aluminium producer set its November prebaked-anode tender at Yuan 6,312/t cash (Yuan 6,328/t acceptance). SMM (13-November) adds that petroleum coke weakened in November and pitch moved sideways, so anode cost support is easing; aluminium fluoride tenders held at Yuan 12,600-13,000/t."},
 {"theme":"Bauxite","horizon":"Structural","impact":"Bullish","url":S_GH,
  "headline":"GHANA TO BAN RAW BAUXITE EXPORTS BY 2030 (AL Circle, 13-November): the finance minister's 2027 budget sets a $1.5bn processing programme, at least 50% local processing of bauxite and manganese by end-2028 and a raw-export ban by end-2030; no refinery volumes or timelines were specified."},
 {"theme":"Bauxite","horizon":"Structural","impact":"Bearish","url":S_RT,
  "headline":"RIO TINTO LAUNCHES $2.6BN KANGWINAN BAUXITE PROJECT (AL Circle, 13-November): about 20 Mt/yr of new bauxite at Weipa, Queensland, lifting Weipa to about 44 Mt/yr from about 38 Mt; first output 2029, full production 2032; replaces the depleting Andoom mine and offsets Gove's planned 2029 closure."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL CLOSED, NEW CLAIMS (Straits Daily Brief, 14-November): traffic near a standstill; 3 transits on 08-November vs 85/day pre-crisis; 38 AIS-visible vessels holding (likely an undercount). Iran's Revolutionary Guard claims a gas carrier struck a mine and caught fire and that it downed a US drone - neither confirmed by any maritime or independent authority."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Mixed","url":S_TG,
  "headline":"EUROPEAN GAS UP >6% ON THE WEEK, BRENT HEADS FOR SECOND WEEKLY DROP (Trading Economics, 13-November): TTF eased 2.8% to about EUR 89.7/MWh on Friday but gained more than 6% on the week on the Troll outage, colder forecasts and EU storage below 72%; Brent near $96 with Saudi October output up 26%."},
 {"theme":"Trade policy","horizon":"Structural","impact":"Mixed","url":S_US,
  "headline":"US TARIFFS KEEP RAISING COSTS (AL Circle, 13-November): the 50% Section 232 aluminium tariff continues to push up costs for US manufacturers and consumers; no official confirmation of the reported US-Canada deal has been located."},
]+d['news']
d['news']=d['news'][:20]

hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('US / Canada'):
        p['update']="REVIEWED 14-NOVEMBER: AL Circle (13-November) reiterates the 50% Section 232 tariff on most aluminium imports; no official confirmation of the reported US-Canada deal located. "+p['update']; hit+=1
assert hit==1

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 13-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 13-Nov, no later row)",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_AN,S_AN],[L_AF,S_AF],[L_GH,S_GH],[L_RT,S_RT],[L_US,S_US]): d['sources'].append(x)
for x in ([L_TE,S_TE],[L_TD,S_TD],[L_ST,S_ST],[L_AN,S_AN]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-11-12'
ph['rows'][-1]=['2026-11-13',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2),d['metals_board'])
