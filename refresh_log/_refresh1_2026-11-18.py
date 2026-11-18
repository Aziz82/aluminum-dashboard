# Daily data refresh - 2026-11-18 (WEDNESDAY, ~02:40 UTC, before today's ring). Board ROLLED ONE SESSION to the TUESDAY 17-Nov LME official.
# Westmetall cache-busted EN + DE overviews agree on 17-Nov (Al cash 3,060.50 / 3M 2,940.00 / stock 220,350; MTLE 1.09930);
# Al per-metal table newest row 17-Nov and its 10-16 Nov rows match the stored series. Cash -271.50 -> backwardation $120.50 (from $312.00).
# 3M 2,940 settled BELOW 2,994.50 (ends the daily base count) and BELOW the 2,977.5 wave-(v) cap (pre-registered re-count). Weights 10/45/45 -> 10/40/50.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-18'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-18"; L_ST="Straits Daily Brief - Strait of Hormuz, 18-Nov-2026 (Brent figure AI-assisted)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,937.8 (-1.90%) on 17-Nov-2026, a 2026 low (CFD reference)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$92.7 (-0.47%) on supply signals; US crude stocks +5.3 mb (18-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.61, near strongest since April 2025; ~96% odds of a 25bp December Fed hike (18-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 85.4/MWh; EU storage under 71% vs 89% five-year average (18-Nov-2026)"
S_BRC="https://brecorder.com/news/40449413/copper-falls-as-tech-weakness-saps-risk-appetite"; L_BRC="Business Recorder (Reuters) - LME aluminium -2.2% to $2,938 in official activity, lowest since December at $2,920; cash premium eased from highest since 1988 (18-Nov-2026)"
S_EP="https://www.alcircle.com/news/european-aluminium-premiums-slide-12-6-as-lme-backwardation-forces-stockholders-to-liquidate-121997"; L_EP="AL Circle - European aluminium premiums slide 12.6% as LME backwardation forces stockholders to liquidate (Fastmarkets Rotterdam DP $470-500/t on 13-Nov; 17-Nov-2026)"
S_AB="https://www.alcircle.com/news/alba-q3-2026-profit-plunges-72-5-to-49-3-million-as-production-disruptions-weigh-121999"; L_AB="AL Circle - Alba Q3-2026 profit plunges 72.5% to $49.3 million (BHD 18.5m) as production disruptions weigh (17-Nov-2026)"
S_RT="https://www.alcircle.com/news/rio-tinto-advances-their-1-9b-kangwinan-bauxite-project-to-secure-australia-s-future-supply-121995"; L_RT="AL Circle - Rio Tinto advances its $1.9bn Kangwinan bauxite project (17-Nov-2026)"

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3332.0 and B['LME 3-month']['cur']==3020.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3332.0,3020.0,221900
cash,m3,stk=3060.5,2940.0,220350
spr=cash-m3; psp=pc-pm; assert spr==120.5 and psp==312.0 and ps-1550==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED WEDNESDAY 18-NOVEMBER-2026 ABOUT 02:40 LONDON, BEFORE TODAY'S RING. THE BOARD IS THE TUESDAY 17-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION AND THE CORRECT FIGURE UNTIL TODAY'S OFFICIAL PRINTS AT 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 17-November official for all metals with stocks and FX (EUR/USD MTLE 1.09930; 16-November 1.10140); (2) the aluminium per-metal daily table shows 17-November as its newest row and its 10-16 November rows match the stored series exactly. "
 "The whole board sits on ONE UNIFORM SESSION (17-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" TUESDAY 17-NOVEMBER (the board): CASH SETTLED $3,060.50, DOWN $271.50 OR 8.15% FROM $3,332.00 - reversing all of Monday's $181.50 jump and more. THREE-MONTH SETTLED $2,940.00, DOWN $80.00 OR 2.65% FROM $3,020.00 - BELOW the 2,994.50 October low (by $54.50) and below the 2,977.5 Elliott re-count level, the lowest three-month official in this series and $70.50 BELOW the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION NARROWED TO $120.50 FROM $312.00 - still a twenty-fourth straight backwardation and the thirteenth above $15.00, but the prompt squeeze eased sharply. Spread and flat price moved in the SAME direction (both down). "
 "VISIBLE LME STOCK FELL 1,550 t TO 220,350 t, another new series low and a twentieth straight draw. Reuters (via Business Recorder, 18-November) reports LME aluminium fell 2.2% to $2,938 in official activity after touching $2,920, the lowest since December, and that the cash premium eased after Monday's highest since 1988. The Trading Economics aluminium reference showed about $2,937.8 (-1.90%) for 17-November, a 2026 low - a CFD reference cited in text only.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,060.5","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"2,940.0","pos":False,"delta":VER+AL+" THREE-MONTH IS NOW $54.50 BELOW THE 2,994.50 OCTOBER LOW, $137.00 BELOW THE 3,077 WEEKLY 50% RETRACEMENT and $46.00 ABOVE the 2,894 weekly 61.8% retracement - the next shared Elliott objective. Daily invalidation of the bearish count remains 3,289; nearer, a settled close back above 3,097.50 would negate the re-counted wave (v)."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+120.5","pos":True,"delta":VER+f" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,060.50 against three-month $2,940.00 is a $120.50 BACKWARDATION, DOWN from 16-November's series-high $312.00, as cash fell $271.50 and three-month $80.00 - spread and flat price moved in the SAME direction (both down). It stays above the published $15.00 reversal condition for a thirteenth session and is a twenty-fourth straight backwardation; a contango beyond $24.50 would reverse the structural signal. AL Circle (17-November) reports the backwardation forced European stockholders to liquidate, pushing Rotterdam duty-paid premiums down 12.6%. The October mean spread was ${oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"220,350","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 1,550 t TO 220,350 t (16-November: -2,250 t to 221,900 t), another new series low and a twentieth straight draw; the pace slowed from the two prior draws above 2,000 t. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 16-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $2,940.00, DOWN $80.00 FROM THE 16-NOVEMBER $3,020.00 - a settled close $54.50 BELOW the 2,994.50 October low and below the 2,977.5 re-count level, the lowest three-month official in this series; $70.50 BELOW the 02-January three-month official (year-to-date {ytd:+.2f}%); $46.00 above the 2,894 weekly 61.8%. AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 1,550 t TO 220,350 t, another new series low (16-November 221,900 t). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $120.50 BACKWARDATION, DOWN FROM 16-NOVEMBER'S SERIES-HIGH $312.00. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On Tuesday cash fell $271.50 and three-month $80.00, so the prompt premium unwound by $191.50 while the outright price also fell. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00 and $120.50."},
 {"name":"EUR/USD LME fixing","cur":1.0993,"prev":1.1014,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.09930 ON 17-NOVEMBER FROM 1.10140 ON 16-NOVEMBER as the dollar index held near its strongest since April 2025. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (17-Nov official)","price":"3,060.5","basis":"THE TUESDAY 17-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,060.50, DOWN $271.50 OR 8.15% (16-November $3,332.00). Next official Wednesday 18-November 13:20 London."},
 {"tenor":"3-month (17-Nov official)","price":"2,940.0","basis":"THE 17-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $2,940.00, DOWN $80.00 - $54.50 BELOW the 2,994.50 October low, $46.00 above the 2,894 weekly 61.8% retracement."},
 {"tenor":"Cash-to-3M structure","price":"+120.5 (BACKWARDATION)","basis":"A $120.50 BACKWARDATION, down from the series-high $312.00 - the prompt squeeze eased but the curve stays backwardated."},
 {"tenor":"Visible LME stock","price":"220,350 t","basis":f"DOWN 1,550 t to a new series low on 17-November (twentieth straight draw); October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("THE SQUEEZE EASES AND THE FORWARD BREAKS. On the 17-November official cash $3,060.50 sits $120.50 ABOVE three-month $2,940.00, a BACKWARDATION down from the series-high $312.00 of 16-November, as cash fell $271.50 and three-month $80.00. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00 and now $120.50. "
 f"READ: a twenty-fourth straight backwardation with visible stock at another low (220,350 t), but the one-day spike has largely unwound and the outright three-month price broke below its October low. AL Circle (17-November) reports the backwardation pushed European stockholders to liquidate, cutting Rotterdam duty-paid premiums 12.6% - so the squeeze is pulling metal out of the physical market rather than signalling broad end-use tightness. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2900,3450] and d['chart_stock_axis']==[190000,255000]
d['chart_price_axis']=[2800,3450]   # re-bracketed: three-month 2,940 was only $40 above the 2,900 floor

ls=d['lme_series']; assert ls[-1][0]=='16-Nov'
d['lme_series']=ls[1:]+[["17-Nov",cash,m3,stk]]
assert len(d['lme_series'])==15 and all(190000<r[3]<255000 and 2800<r[2]<3450 and 2800<r[1]<3450 for r in d['lme_series'])
CU=(13225.5,13211.0,327600); NI=(15790.0,15990.0,274140); ZN=(3776.0,3661.0,148375); PB=(1840.0,1874.0,270800)
CU6=(13375.0,13305.0,327475); NI6=(15805.0,16000.0,272682); ZN6=(3848.0,3715.0,141275); PB6=(1856.0,1886.0,279325)
assert CU6[2]+125==CU[2] and NI6[2]+1458==NI[2] and ZN6[2]+7100==ZN[2] and PB6[2]-8525==PB[2]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU6[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI6[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN6[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB6[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU6[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI6[1],1)
zn11=[3935.0,3869.0,3875.0,3877.0,3759.0,3754.0,3768.0,3794.0,3760.5,3745.0,3848.0]; pb11=[1869.5,1862.0,1858.0,1866.5,1857.0,1854.0,1846.0,1845.0,1843.0,1853.0,1856.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zn11)+ZN[0])/12)/(sum(zn11)/11),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(pb11)+PB[0])/12)/(sum(pb11)/11),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU6[0]),('NI',NI[0],NI6[0]),('ZN',ZN[0],ZN6[0]),('PB',PB[0],PB6[0])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-11-17'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending TUESDAY 17-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 27-October dropped, 17-November appended, so the window is 28-October to 17-November. Every point is an official cash settlement from the Westmetall per-metal tables and English/German overviews (17-November read from both overviews, which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (17-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return "unchanged" if a==b else f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,f" COPPER 17-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU6[0])}; three-month ${CU[1]:,.2f}, {chg(CU[1],CU6[1])}. BACKWARDATION narrowed to $14.50 from $70.00. Stock rose 125 t to 327,600 t. Reuters (via Business Recorder) reports three-month touched $13,144, the lowest since 01-July, on tech-stock weakness and a stronger dollar."),
 ("Nickel",NI,f" NICKEL 17-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI6[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI6[1])}. CONTANGO $200.00 from $195.00, still the widest carry on the board. Stock rose 1,458 t to 274,140 t."),
 ("Zinc",ZN,f" ZINC 17-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN6[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN6[1])}. BACKWARDATION eased to $115.00 from $133.00. Stock ROSE 7,100 t to 148,375 t, the largest inflow on the board. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,f" LEAD 17-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB6[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB6[1])}. CONTANGO $34.00 from $30.00. Stock fell 8,525 t to 270,800 t, the largest draw on the board."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Tuesday 17-November official three-month aluminium fell 2.65%, zinc 1.45%, copper 0.71%, lead 0.64% and nickel 0.06% - a broad risk-off session. Trading Economics reports the dollar index near 103.6, near its strongest since April 2025, with about 96% odds of a 25bp Fed hike in December; Brent about $92.7. The LME euro fixing fell to 1.0993.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='16-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["17-Nov",CU[0]]]; assert len(i['hist'])==15
        i['val']="~13,211.00 (3M); 13,225.50 (cash) $/t"; i['ratio']="~13,225.50 $/t cash vs LME 3M 13,211.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the TUESDAY 17-NOVEMBER-2026 session at $13,225.50 (16-November $13,375.00). THE WINDOW ROLLED THIS RUN: 27-October dropped and 17-November appended, so the series is the last fifteen published official cash sessions, 28-October to 17-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English/German overviews. "
                  "Copper structure for context: backwardation $14.50 on 17-November; stock 327,600 t (+125 t).")
assert [r for r in d['inputs'] if r['name'].startswith('Copper')][0]['hist'][-1]==["17-Nov",13225.5]
s=d['inputs_summary']
d['inputs_summary']=("UPDATE 18-NOVEMBER: Copper rolled one session to the Tuesday 17-November LME official cash of $13,225.50 (window 28-October to 17-November). No new carbon, fluoride, silicon or magnesium mark was located this run, so those series are unchanged (gaps stay gaps). Energy broadly steady: Brent about $92.7 and European gas about EUR 85.4/MWh, with EU storage under 71% against an 89% five-year average (Trading Economics, 18-November). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
ptl=0.5*pc; presid=2403-ptl; pshare=ptl/2403*100
OT=f"the tariff leg of the US duty-paid premium is 0.50 times the 16-November official cash of $3,332.00, or ${ptl:,.2f}, UP $90.75 against the 13-November figure used previously (the cash squeeze lifts the tariff leg). Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${presid:,.2f}, so {pshare:.1f}%"
NT=f"the tariff leg of the US duty-paid premium is 0.50 times the 17-November official cash of $3,060.50, or ${tl:,.2f}, DOWN ${ptl-tl:,.2f} against the 16-November figure used previously (the cash squeeze unwound). Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OC1="COMPILED TUESDAY 17-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE MONDAY 16-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; TUESDAY'S OFFICIAL PRINTS 13:20 LONDON)."
NC1="COMPILED WEDNESDAY 18-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE TUESDAY 17-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; WEDNESDAY'S OFFICIAL PRINTS 13:20 LONDON)."
EUN=(" EUROPEAN ROWS REFRESHED 18-NOVEMBER FROM A NEW PUBLIC MARK: AL Circle (17-November) reports Fastmarkets' Rotterdam P1020A in-warehouse DUTY-UNPAID premium at $390-420/t on 13-November (midpoint $405, carried in the EDU row; the prior $485 row value was an earlier mark not from this assessment) and DUTY-PAID at $470-500/t, down 12.6% from $540-570/t on 10-November, with one standard-tonnage deal at $485/t duty-paid; the article attributes the slide to the LME backwardation forcing stockholders to liquidate. Billets Rotterdam is carried unchanged.")
for p in d['premiums']:
    assert OT in p['src'] and OC1 in p['src'],p['name']
    p['src']=p['src'].replace(OT,NT).replace(OC1,NC1)+EUN
    if p['name'].startswith('European Duty Unpaid'):
        assert p['cur']==485; p['prev']=485; p['cur']=405
ra=398.24/m3*100; pra=398.24/pm*100
OR=f"THE RATIO: LME Alumina at $398.24/t against the 16-November aluminium three-month of $3,020.00 is {pra:.2f}%"
for a in d['alumina']:
    assert OR in a['src'] and OC1 in a['src'],a['name']
    a['src']=a['src'].replace(OR,f"THE RATIO: LME Alumina at $398.24/t against the 17-November aluminium three-month of $2,940.00 is {ra:.2f}%").replace(OC1,NC1)
pd=d['premium_drivers']; assert pd[2]['t'].startswith('Chinese primary imports fell')
pd[2]={"t":"The LME backwardation is draining European physical premiums","d":"AL Circle (17-November), citing Fastmarkets: Rotterdam duty-paid P1020A premiums fell 12.6% to $470-500/t on 13-November from $540-570/t on 10-November, and duty-unpaid to $390-420/t, as the extreme LME backwardation made holding metal costly and stockholders released inventory. WHY IT MATTERS: a steep backwardation pulls physical metal toward the exchange and cheapens regional premiums at the same time; lower European premiums could eventually draw metal back into LME warehouses, though limited available metal and pending brand registrations may slow that.","src":[L_EP,S_EP]}
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("REVIEWED 17-NOVEMBER: no newer public disclosure","REVIEWED 18-NOVEMBER: no newer public disclosure").replace("REVIEWED 17-NOVEMBER. NO NEW DATED","REVIEWED 18-NOVEMBER. NO NEW DATED")
    return o
for k in ('producer_status','inputs','logistics','raw_materials','premiums','alumina'):
    if k in d: d[k]=walk(d[k])
for k in ('premiums','alumina'): assert "16-November official cash of $3,332.00" not in json.dumps(d[k]), k

d['lme_commentary']=("SQUEEZE UNWINDS, FORWARD BREAKS ITS OCTOBER LOW. The Tuesday 17-November official cut cash $271.50 (-8.15%) to $3,060.50 and three-month $80.00 (-2.65%) to $2,940.00, so the backwardation narrowed to $120.50 from Monday's series-high $312.00. Three-month settled $54.50 below the 2,994.50 October low, the lowest official in this series; Reuters reports the market touched $2,920, the lowest since December. Visible stock still fell 1,550 t to a new low of 220,350 t. "
 "The squeeze is reshaping the physical market rather than signalling end-use tightness: AL Circle reports Rotterdam duty-paid premiums fell 12.6% to $470-500/t as stockholders liquidated into the backwardation. "
 "Macro is the headwind: the dollar index near 103.6 with about 96% odds of a 25bp December Fed hike, tech-led risk-off (copper at its lowest since July) and expectations of a 2027 surplus. Scenario weights move to 10/40/50 on the pre-registered break below 2,994.50. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" its October mean.")
d['net_read']=("NET: BEARISH ON THE FORWARD, STILL TIGHT BUT EASING ON THE PROMPT. Against: three-month at $2,940.00 broke below the 2,994.50 October low; the dollar near its strongest since April 2025 with a December Fed hike about 96% priced; European physical premiums sliding; a growing 2027-31 ex-China capacity pipeline and Gulf metal returning through Q1-2027. "
 "Supportive: a $120.50 backwardation (twenty-fourth straight), visible LME stock at a new low of 220,350 t, and Hormuz still closed with UKMTO confirming another tanker attack.")
d['bottom_line']=("BOTTOM LINE: the Tuesday 17-November official reversed Monday's squeeze - cash fell $271.50 to $3,060.50 and three-month $80.00 to $2,940.00, below the 2,994.50 October low - narrowing the backwardation to $120.50 while visible stock fell to another low of 220,350 t. "
 "Weights move to 10% bull / 40% base / 50% bear on the pre-registered break. Next support is the 2,894 weekly 61.8% retracement (re-counted wave (v) target 2,894-2,906); a settled close back above 2,994.50 is the first sign the break failed, above 3,097.50 negates the re-count. Daily Elliott invalidation 3,289. Next official Wednesday 18-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, PROMPT PREMIUM EXPLODES WHILE THE FORWARD STALLS:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, PROMPT PREMIUM UNWINDS AS THE FORWARD BREAKS LOWER: the backwardation narrowed to $120.50 on 17-November from the series-high $312.00, as cash fell $271.50 and three-month $80.00 to $2,940.00 - $54.50 below the 2,994.50 October low; nearby metal still commands a premium over forward metal, so there is still no carry reward for holding stock, but the extreme one-day squeeze has largely reversed. "+c2[a1:]
o=f"is ${ptl:,.2f} on 16-November cash, {pshare:.1f}% of the $2,403/t premium"; assert o in c2; c2=c2.replace(o,f"is ${tl:,.2f} on 17-November cash, {share:.1f}% of the $2,403/t premium")
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find(" Hindalco's",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 17-November official broke three-month below 2,994.50 to $2,940.00, with 2,894 the next weekly support, while cash fell to $3,060.50; the dollar index near 103.6 with about 96% odds of a 25bp Fed hike in December (Trading Economics 18-November); Brent about $92.7 and European gas about EUR 85.4/MWh; Rotterdam duty-paid premiums fell 12.6% to $470-500/t (Fastmarkets via AL Circle 17-November); Alba reported a 72.5% fall in Q3-2026 profit to BHD 18.5m (AL Circle 17-November); EGA targets full Al Taweelah production in Q1-2027 (AL Circle 16-November); a possible US-Canada deal cutting the US tariff on Canadian aluminium to 25% remains unconfirmed; Maaden (1211) reported Q3-2026 aluminium EBITDA of $419m (Arab News 09-November);"+c2[b1:]
d['commercial']=c2

NEWP={'Bull':'10%','Base':'40%','Bear':'50%'}
for s in d['outlook']['scenarios']:
    assert s['prob']=={'Bull':'10%','Base':'45%','Bear':'45%'}[s['case']]
    s['prob']=NEWP[s['case']]
    s['drivers']=("SHIFTED 18-NOVEMBER TO 10/40/50: the 17-November official settled three-month at $2,940.00, BELOW 2,994.50 - the pre-registered level that adds bear weight - so five points move from base to bear. A settled close back above 2,994.50 would return them; above 3,042 returns five points to bull. ")+s['drivers']
    if s['case']=='Bear': s['target']='$2,850-3,000'
    if s['case']=='Base': s['target']='$3,000-3,250'
d['outlook']['scenario_paths']={'labels':['Now','Nov-26','Dec-26','Mar-27','Jun-27'],'bull':[m3,3150,3350,3550,3700],'base':[m3,2980,3050,3150,3220],'bear':[m3,2900,2880,2860,2850]}

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 18-NOVEMBER: the 17-November official printed a $120.50 BACKWARDATION, down from the series-high $312.00 - a thirteenth session above $15.00. Contango risk remains remote near term. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 18-NOVEMBER: LME stock fell 1,550 t on 17-November to a new low of 220,350 t, a twentieth straight draw though slower than the two prior 2,000 t+ draws; European stockholders are reported liquidating into the backwardation (AL Circle 17-November). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 18-NOVEMBER: Brent about $92.7 (-0.47%) as US crude stocks rose 5.3 mb, European gas about EUR 85.4/MWh with storage under 71% (Trading Economics). Energy support little changed; with three-month now at $2,940 the cost floor is closer to being tested. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 18-NOVEMBER: Straits Daily Brief - strait effectively closed; 2 transits on 15-November (vs 85/day pre-crisis); 37 AIS-visible vessels holding. UKMTO reported a tanker off Oman struck twice and set on fire (16-November); an Iranian claim of a third mined tanker, a six-tanker total and an LPG carrier hit are unconfirmed by any maritime authority. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 18-NOVEMBER: the dollar index held near 103.6, near its strongest since April 2025; CME FedWatch about 96% odds of a 25bp December hike (4% for 50bp) after hawkish remarks from Fed officials Musalem and Williams (Trading Economics). Reuters links Tuesday's metals weakness partly to the stronger dollar. Trend held at UP."; r['trend']='up'; hit+=1
assert hit==5,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Tue 17-Nov':
        hc+=1; cat['date']='Daily, from Wed 18-Nov'
        cat['event']=("TUESDAY 17-NOVEMBER OFFICIAL: three-month $2,940.00 (-$80.00), cash $3,060.50 (-$271.50), backwardation $120.50 from $312.00; three-month BROKE the 2,994.50 October low and weights moved to 10/40/50. NEXT (from Wednesday 18-November, official 13:20 London): the 2,894-2,906 zone (weekly 61.8% and re-counted wave (v) target); a settled close back above 2,994.50 would signal a failed break; above 3,097.50 negates the re-count; invalidation 3,289. Friday's weekly close vs 2,994.50; FOMC minutes and the December Fed meeting (hike about 96% priced); any official US-Canada tariff announcement; first Q1-2027 Japanese premium offers.")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"WEDNESDAY 18-NOVEMBER ON THE TUESDAY 17-NOVEMBER OFFICIAL: Monday's prompt squeeze largely reversed - cash fell $271.50 to $3,060.50 and the backwardation narrowed to $120.50 from $312.00 - while three-month fell $80.00 to $2,940.00, settling below the 2,994.50 October low for the first time (Reuters: lowest since December, intraday $2,920). Visible stock still fell to a new low of 220,350 t. AL Circle reports the squeeze pushed European stockholders to liquidate, cutting Rotterdam duty-paid premiums 12.6%, and Alba's Q3 profit fell 72.5% on production disruption. With the dollar near its strongest since April 2025 and a December Fed hike about 96% priced, the forward is pricing a looser 2027; weights move to 10/40/50.")

# --- Elliott Wave: pre-registered re-count on the settled break below 2,977.5 ---
st=d['ew']['short_term']
lab={w['p']:w for w in st['waves']}
assert lab[3118.0]['w']=='(iii) of C' and lab[3148.5]['w']=='(iv) of C - confirmed 07-Oct'
lab[3118.0]['w']='3 of (iii) of C (re-counted 18-Nov; formerly (iii))'
lab[3148.5]['w']='4 of (iii) of C (re-counted 18-Nov; formerly (iv))'
nx=st['now_x']; assert nx==0.99994
st['waves']+= [{"t":0.99980,"p":2994.5,"w":"(iii) of C - 15-Oct settled low (re-counted 18-Nov)"},{"t":0.99988,"p":3097.5,"w":"(iv) of C - rebound high (re-counted 18-Nov)"}]
assert all(w['t']<nx for w in st['waves'])
st['ymin']=2800; st['yticks']=[2800,3000,3200,3400,3600,3800]
st['proj']={"bull":[[nx,m3],[0.99997,3000],[1.0,3100]],"base":[[nx,m3],[0.99997,2900],[1.0,2960]],"bear":[[nx,m3],[0.99997,2890],[1.0,2850]]}
st['fwd_pivots'][0]={"t":0.99996,"p":2894.0,"w":"RE-COUNTED 18-NOVEMBER: the settled break below 2,977.5 ruled out a single wave (v) from 3,148.5 (it would have made wave (iii) the shortest). Re-count: (i) 3,374-3,183 ($191), (ii) 3,289, (iii) 3,289-2,994.50 ($294.50, the longest), (iv) 3,097.50 (no overlap with the 3,183 wave (i) low), (v) under way. Wave (v) = wave (i) projects 2,906.5, in confluence with the 2,894 weekly 61.8% - the 2,894-2,906 target zone. A settled close above 3,097.50 negates this count."}
lt=d['ew']['long_term']
lt['proj']={"bull":lt['proj']['bull'],"base":[[lt['now_x'],m3],[0.78,2900],[0.9,3000],[1.0,3100]],"bear":[[lt['now_x'],m3],[0.8,2800],[1.0,2650]]}
EWP=("REVIEWED 18-NOVEMBER ON THE 17-NOVEMBER OFFICIAL - RE-COUNT ON A PRE-REGISTERED BREAK: three-month settled 2,940.00 (-80.00), BELOW 2,994.50 (which ENDS the base count of a deep wave (ii) of C/3) and BELOW about 2,977.5 (which forces a re-count). The decline from 3,148.5 cannot be a single wave (v) because it would now be longer than wave (iii), so the C wave from the 3,374 B high is re-counted: (i) 3,183, (ii) 3,289, an extended (iii) to 2,994.50 (the former (iii) 3,118 and (iv) 3,148.5 become sub-waves 3 and 4 of it), (iv) 3,097.50, and (v) now under way - all three cardinal rules hold. BASE CASE (about 70%): wave (v) completes in the 2,894-2,906 zone (wave (v) = wave (i) at 2,906.5; weekly 61.8% at 2,894), ending the C wave. ALTERNATE (about 30%): an extended (v) toward 2,830-2,850 (0.618 of (i) through (iii) from 3,097.50). INVALIDATION of the re-count: a settled close above 3,097.50; of the bearish C-wave count, 3,289. Confidence low-to-moderate. ")
EWL=("REVIEWED 18-NOVEMBER (MID-WEEK, DAILY BREAK): the Tuesday official at 2,940.00 settled below the 2,994.50 October low, so the alternate that 2,994.50 completed the correction is cut to about 10% and is removed outright on a weekly close below 2,994.50. The weekly base case - the corrective count toward the 61.8% retracement at 2,894 - is REINFORCED and now about $46 away; it loses preference only on a weekly close above 3,110. A new alternate (about 20%): a weekly close below 2,894 would open the 78.6% retracement near 2,633. Confidence moderate. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 17-NOVEMBER'),k
    d['ew'][k]['writeup']=pfx+w
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="92.7",day="about $92.70 on 18-November (-0.47%, Trading Economics); Straits Daily Brief $93.33 (+1.30% over 24 hours; its header shows $92.77)",
 note="REFRESHED WEDNESDAY 18-NOVEMBER-2026 (Trading Economics): Brent slipped below $93, extending the week's losses, as signs of strengthening global supply offset Gulf conflict - the IEA projects a surplus of about 2 mb/d this quarter, Goldman Sachs warned of a possible glut next year and US crude inventories rose 5.3 million barrels. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="85.4",day="about EUR 85.3-85.4/MWh on 18-November, little changed (Trading Economics; sections differ)",
 note="REFRESHED WEDNESDAY 18-NOVEMBER-2026 (Trading Economics): prices eased after recent losses on milder forecasts and record US LNG exports; storage is under 71% full against a five-year seasonal average of 89%, Germany below 58%. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="103.61",day="about 103.61 on 18-November (+0.01%, Trading Economics), near its strongest since April 2025",
 note="REFRESHED WEDNESDAY 18-NOVEMBER-2026 (Trading Economics): hawkish remarks from Fed officials (Musalem: 'several rate increases'; Williams: higher rates needed) lifted hike bets; CME FedWatch about 96% odds of a 25bp December hike and 4% for 50bp; markets await FOMC minutes. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.09930',day="LME fixing on 17-November, down from 1.10140 on 16-November",note="REFRESHED WEDNESDAY 18-NOVEMBER-2026 to the 17-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE TUESDAY 17-NOVEMBER-2026 LME OFFICIAL, the latest published session. THIS WEDNESDAY 18-NOVEMBER RUN IS COMPILED AT ABOUT 02:40 LONDON, BEFORE TODAY'S RING (today's official prints at 13:20 London). The board rolled ONE session this run (from Monday 16-November). The Trading Economics aluminium reference (about $2,937.8, -1.90% for 17-November, a 2026 low) is a CFD reference cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (18-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 17-November session (aluminium cash 3,060.50, three-month 2,940.00, stock 220,350; EUR/USD MTLE 1.09930); the aluminium per-metal daily table shows 17-November as its newest row. Because the cash move (-$271.50) is again exceptional, it was checked in all three pages and against Reuters' 'fell 2.2% to $2,938 in official activity' (Business Recorder, 18-November); all agree.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 10-16 November rows match the stored series exactly; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 17-November values come from both overviews, which agree, and each metal's stock change reconciles with its 16-November stock.")
C[3]=("STOCK CHANGES 17-November (also shown in the pages' change column): aluminium -1,550 to 220,350; copper +125 to 327,600; nickel +1,458 to 274,140; zinc +7,100 to 148,375; lead -8,525 to 270,800.")
c4=C[4]; k=c4.find("The price chart ax"); assert k>0
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (17-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (twelve sessions, 02-17 November) as their latest point. ")+c4[k:]
o4="brackets cash 3,332.00 and three-month 3,020.00; the stock chart axis floor was LOWERED THIS RUN from 200,000 t to 190,000 t, ahead of need, because visible stock of 221,900 t is drawing about 2,200 t per session (31,900 t headroom now)"
assert o4 in C[4]
C[4]=C[4].replace(o4,"brackets cash 3,060.50 and three-month 2,940.00 after the price-axis floor was LOWERED THIS RUN from 2,900 to 2,800 (three-month was only $40 above the old floor); the stock chart axis floor of 190,000 t leaves 30,350 t headroom below visible stock of 220,350 t")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,060.50 against three-month $2,940.00 is therefore a $120.50 BACKWARDATION, down from the series-high $312.00 on 16-November. On Tuesday spread and flat price moved in the SAME direction (both down). Press figures for the spread differ by measure and time; the dashboard uses the settled officials only."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        o=f"the tariff leg is 0.50 times the 16-November official cash of $3,332.00, or ${ptl:,.2f}, leaving a ${presid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({pshare:.1f}% policy arithmetic; the cash squeeze inflates the tariff leg)"
        assert o in cv,cv[:600]
        C[i]=cv.replace(o,f"the tariff leg is 0.50 times the 17-November official cash of $3,060.50, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic)"); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $92.7), the dollar index (about 103.61) and TTF (about EUR 85.4/MWh) are Trading Economics readings for 18-November (early, pre-European session); Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages again showed slightly different levels in different sections (TTF 85.38 vs 85.32), so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (18-November) shows Brent $93.33 (AI-assisted; header $92.77); its incident items are flagged as claims or unconfirmed except the UKMTO-reported attack."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 18-NOVEMBER (WEDNESDAY, PRE-RING): no authorised fetch was blocked. Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/TTF/dollar, AL Circle news, news.metal.com and the Straits Daily Brief were fetched. An SMM article on lifted production restrictions in central China returned 404 and is not used; news.metal.com carried no SMM input mark, so none is appended. The Reuters metals report (via Business Recorder, 18-November) was found by search and fetched. A search for Q1-2027 Japanese premium offers again found none (market expectations of $190-200/t are not offers), so Q1 stays unpriced."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        rest=cv.split("EARLIER:",1)[-1].strip()
        C[i]=("PEER EARNINGS: ALBA Q3-2026 ADDED THIS RUN (18-NOVEMBER) - profit attributable BHD 18.5m (US$49.3m), down 72.5% from BHD 67.3m, per AL Circle (17-November); the article does not state the release date, so the reported date shown is the article date. earnings_history ALBH refreshed with the Q3-26 point (H1 BHD 140.2m + Q3 BHD 18.5m reconciles to the reported 9M BHD 158.7m); oldest point (Q3-25) dropped to keep four quarters. EARLIER: "+rest); hit+=1
assert hit==4,hit

d['so_what']={"line":"Monday's LME aluminium squeeze reversed on Tuesday: cash fell $271.50 to $3,060.50 and three-month dropped $80 to $2,940 - below its October low for the first time - narrowing the backwardation to $120.50 even as LME stock fell to another low of 220,350 t.",
 "points":[
 "WHAT MOVED: the Tuesday 17-November official cut cash 8.15% to $3,060.50 and three-month 2.65% to $2,940.00, so the backwardation (cash above three-month) narrowed to $120.50 from a series-high $312.00; visible LME stock fell 1,550 t to 220,350 t.",
 "WHY: a broad risk-off session - the dollar near its strongest since April 2025 with a December Fed hike about 96% priced and copper at its lowest since July - on top of expectations of a 2027 surplus. The squeeze is also pushing metal out of Europe: Rotterdam duty-paid premiums fell 12.6% as stockholders liquidated.",
 "SUPPLY SIGNALS: Alba's Q3 profit fell 72.5% on production disruptions, and Hormuz stays effectively closed with UKMTO reporting another tanker attack - supportive, but not enough to hold the forward price.",
 "WHAT TO WATCH: the $2,894-2,906 support zone; a settled three-month close back above $2,994.50 would signal a failed break; Friday's weekly close; FOMC minutes."]}

d['feed']=([
 {"when":"Tue 17-Nov","impact":"Bearish","text":"17-NOVEMBER OFFICIAL: cash $3,060.50 (-$271.50); three-month $2,940.00 (-$80.00), below the October low; backwardation narrows to $120.50; stock -1,550 t to 220,350 t."},
 {"when":"Tue 17-Nov","impact":"Bearish","text":"EUROPE: Rotterdam duty-paid premiums fall 12.6% to $470-500/t as stockholders liquidate into the backwardation (Fastmarkets via AL Circle)."},
 {"when":"Tue 17-Nov","impact":"Mixed","text":"ALBA: Q3-2026 profit down 72.5% to BHD 18.5m on production disruptions; 9M sales 800,792 t, -33% (AL Circle)."},
 {"when":"Tue 17-Nov","impact":"Mixed","text":"RIO TINTO: advances its $1.9bn Kangwinan bauxite project in Australia (AL Circle)."},
 {"when":"Wed 18-Nov","impact":"Bullish","text":"HORMUZ: effectively closed; UKMTO-reported tanker attack off Oman; further Iranian claims unconfirmed (Straits brief)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM SQUEEZE REVERSES; THREE-MONTH BREAKS OCTOBER LOW. The Tuesday 17-November official cut cash $271.50 (-8.15%) to $3,060.50 and three-month $80.00 (-2.65%) to $2,940.00, below the 2,994.50 October low; the backwardation narrowed to $120.50 from $312.00 while visible stock fell 1,550 t to a new low of 220,350 t. Board three-month moves: aluminium -2.65%, zinc -1.45%, copper -0.71%, lead -0.64%, nickel -0.06%."},
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":S_BRC,
  "headline":"REUTERS: ALUMINIUM AT LOWEST SINCE DECEMBER (via Business Recorder, 18-November): LME aluminium fell 2.2% to $2,938 in official activity after touching $2,920; the cash premium eased after Monday's highest since 1988. Copper touched its lowest since 01-July on tech-stock weakness and a dollar at a fresh 19-month peak. ING expects near-term tightness to keep supporting prices, with supply less supportive later."},
 {"theme":"Premiums","horizon":"0-1 month","impact":"Bearish","url":S_EP,
  "headline":"EUROPEAN PREMIUMS SLIDE 12.6% (AL Circle, 17-November, citing Fastmarkets): Rotterdam P1020A duty-paid fell to $470-500/t on 13-November from $540-570/t on 10-November, duty-unpaid to $390-420/t, as the LME backwardation forced stockholders to liquidate; LME stocks were 89.16% on warrant and Russian-origin metal made up 99.98% of open primary tonnage on 10-November."},
 {"theme":"Supply","horizon":"0-6 months","impact":"Mixed","url":S_AB,
  "headline":"ALBA Q3-2026 PROFIT DOWN 72.5% (AL Circle, 17-November): profit attributable BHD 18.5m (US$49.3m) vs BHD 67.3m; 9M profit BHD 158.7m, +44.3%; 9M sales 800,792 t (-33%) and net finished production 709,395 t (-41%) after the controlled shutdown of Reduction Lines 1-3; capacity progressively restored in Q3 and Line 4 ramping toward full."},
 {"theme":"Raw materials","horizon":"Structural","impact":"Mixed","url":S_RT,
  "headline":"RIO TINTO ADVANCES $1.9BN KANGWINAN BAUXITE PROJECT (AL Circle, 17-November), aimed at securing future Australian bauxite supply; AL Circle also reports China took 70.8% of Australian bauxite exports in January-October 2026."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ EFFECTIVELY CLOSED (Straits Daily Brief, 18-November): 2 transits on 15-November vs 85/day pre-crisis; 37 AIS-visible vessels holding. UKMTO reported a tanker off Oman struck twice and set on fire; an Iranian claim of a third mined tanker, a six-tanker total and an LPG carrier hit are unconfirmed by any maritime authority."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"DOLLAR NEAR STRONGEST SINCE APRIL 2025 (Trading Economics, 18-November): DXY about 103.61; CME FedWatch about 96% odds of a 25bp December hike after hawkish remarks from Fed officials; Brent about $92.7 as US crude stocks rose 5.3 mb."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])

e0=[x for x in d['earnings'] if x['company'].startswith('Alba - ')][0]
d['earnings'].insert(0,{"company":"Alba - Aluminium Bahrain (ALBH)","group":"Gulf producer","period":"Q3 2026 (Jul-Sep 2026)","reported":"17-Nov-2026","reported_iso":"2026-11-17",
 "headline":"Q3-2026 profit attributable to equity holders BHD 18.5m (US$49.3m), DOWN 72.5% y/y from BHD 67.3m (US$178.9m); EPS 13 fils vs 48 fils. 9M-2026 profit BHD 158.7m (US$422.1m), +44.3%; 9M sales volume 800,792 t, -33%; net finished production 709,395 t, -41%; value-added sales 532,591 t (67% of shipments). Reported by AL Circle 17-November; release date not stated in the article.",
 "readthrough":"VOLUME LOSS FINALLY OUTWEIGHS PRICE: after a near-tripling of H1 profit on high LME prices, Q3 profit fell 72.5% as the controlled shutdown of Reduction Lines 1-3, shipping constraints and raw-material adjustments cut volumes. Capacity was progressively restored during Q3 and Line 4 is ramping toward full - the restart that adds ex-China supply into 2027.",
 "sentiment":"Negative","eps":None,"revenue_bn":None,"yoy_pct":-72.5,"url":S_AB})
eh=d['earnings_history']['ALBH']; assert eh['points'][-1]==['Q2-26',64.9]
eh['points']=eh['points'][1:]+[['Q3-26',18.5]]
eh['src']=[eh['src'][0].replace("REFRESHED THIS RUN:","EARLIER:")+" UPDATED 18-NOVEMBER-2026: Q3-2026 point BHD 18.5m (US$49.3m, EPS 13 fils, -72.5% y/y) added from AL Circle's 17-November report of Alba's Q3 results; H1-2026 BHD 140.2m + Q3 BHD 18.5m reconciles to the reported 9M-2026 BHD 158.7m. Q3-2025 dropped to keep four quarters.",S_AB]
d['earnings_note']=("ALBA REPORTED (added 18-November): Q3-2026 profit attributable BHD 18.5m (US$49.3m), -72.5% y/y; 9M BHD 158.7m, +44.3%; 9M sales -33% on the Lines 1-3 shutdown (AL Circle, 17-November). ")+d['earnings_note']

hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('Aluminium Bahrain'):
        p['update']=("UPDATED 18-NOVEMBER: Alba's Q3-2026 results (AL Circle, 17-November) - Q3 profit BHD 18.5m, -72.5%; 9M sales 800,792 t (-33%) and net finished production 709,395 t (-41%) after the controlled shutdown of Reduction Lines 1, 2 and 3; operational stability improved in Q3 as capacity was progressively restored and Line 4 continued toward full ramp-up. ")+p['update']
        p['src']=[L_AB,S_AB]; hit+=1
    elif p['name'].startswith('US / Canada'):
        p['update']=p['update'].replace("REVIEWED 17-NOVEMBER: still no official confirmation","REVIEWED 18-NOVEMBER: still no official confirmation",1); hit+=1
assert hit==2,hit

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 17-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 17-Nov)",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_BRC,S_BRC],[L_EP,S_EP],[L_AB,S_AB],[L_RT,S_RT]): d['sources'].append(x)
for x in ([L_BRC,S_BRC],[L_EP,S_EP],[L_TD,S_TD],[L_ST,S_ST]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-16',3332.0,3020.0,221900]
ph['rows'][-1]=['2026-11-17',cash,m3,stk]; ph['updated']=RD   # same week (w/c 16-Nov): replace the week's row
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2),d['metals_board'])
