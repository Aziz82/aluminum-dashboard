# Daily data refresh - 2026-11-13 (FRIDAY, ~02:40 UTC). Board ROLLED ONE SESSION to the THURSDAY 12-Nov LME official.
# Westmetall cache-busted EN + DE overviews agree on 12-Nov (Al cash 3,155.50 / 3M 3,032.00 / stock 226,350; MTLE 1.10880);
# aluminium per-metal table newest row 12-Nov and its 05-11 Nov rows match the stored series.
# 3M 3,032.00: not above 3,077 and not below 3,024.50 -> weights unchanged 15/45/40. Back BELOW 3,042 -> EW daily alternate re-favoured (~60/40, no re-label).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-13'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-13"; L_ST="Straits Daily Brief - Strait of Hormuz, 13-Nov-2026 (ticker AI-assisted)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~3,018.90 (-1.45%) on 12-Nov-2026 (CFD reference); prompt spread at five-month high (13-Nov-2026)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$95.8; Trump says US no longer needs a deal with Iran (13-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.16, strongest since April 2025; ~91% odds of a hike next month (13-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 95.3/MWh (+3.3%) after a ~7% jump on 12-Nov; Troll outage; EU storage below 72% (13-Nov-2026)"
S_EG="https://www.alcircle.com/news/ega-raises-ebitda-margin-to-30-despite-al-taweelah-disruption-while-targeting-full-smelter-recovery-by-q1-2027-121931"; L_EG="AL Circle - EGA 9M-2026: adj. EBITDA $1.572bn, margin 29.8%; 766 of 1,262 Al Taweelah cells restarted; full restart Q1-2027 (12-Nov-2026)"
S_KZ="https://www.alcircle.com/news/kazakhstan-tightens-eaeu-trade-restricts-aluminium-foil-exports-till-2030-121938"; L_KZ="AL Circle - Kazakhstan restricts aluminium foil exports till 2030 (12-Nov-2026)"
S_VN="https://www.alcircle.com/news/vietnams-bauxite-ambitions-vinacomin-proposes-208m-lam-dong-mining-project-121935"; L_VN="AL Circle - Vinacomin proposes $208m Lam Dong bauxite project (12-Nov-2026)"
S_SM="https://www.metal.com/en/newscontent/DSHMAD36YDPF73BDJRVIWKM3KDKRZVLC6JDJQKA-lme-squeeze-heats-up-aluminum-prices-consolidate-on-a-subdued-note-smm-aluminum-morning-meeting-summary"; L_SM="SMM - LME squeeze heats up, aluminium prices consolidate on a subdued note (morning meeting, 13-Nov-2026)"
S_SI="https://www.metal.com/en/newscontent/TNGXYPSE7CLVZXRJOH7DR7GRY6GTNB5YYDVBGAI-chinas-aluminum-ingot-inventory-in-three-regions-falls-on-november-13"; L_SI="SMM - China aluminium ingot inventory in three regions falls into the 340 kt range (13-Nov-2026)"
S_SP="https://www.metal.com/en/newscontent/ONOMWGM74DZ6TKFGQCPTOV2LHB72U45O64DI24Y-environmental-protection-related-controls-combined-with-off-season-weakness-cause-aluminum-processing-operating-rate-to-pull-back-slightly-smm-aluminum-processing-weekly-survey"; L_SP="SMM - China aluminium processing operating rate eases 0.2 pt to 61.8% (weekly survey, 13-Nov-2026)"

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3223.5 and B['LME 3-month']['cur']==3064.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3223.5,3064.0,226725
cash,m3,stk=3155.5,3032.0,226350
spr=cash-m3; psp=pc-pm; assert spr==123.5 and psp==159.5 and ps-375==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED FRIDAY 13-NOVEMBER-2026 ABOUT 02:40 LONDON, BEFORE FRIDAY'S RING, SO THE BOARD IS THE THURSDAY 12-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION (FRIDAY'S PRINTS 13:20 LONDON). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 12-November official for all metals with stocks and FX (EUR/USD MTLE 1.10880; 11-November 1.11320); (2) the aluminium per-metal daily table shows 12-November as its newest row and its 05 to 11-November rows match the stored series exactly. "
 "The whole board sits on ONE UNIFORM SESSION (12-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" THURSDAY 12-NOVEMBER (the board): CASH SETTLED $3,155.50, DOWN $68.00 OR 2.11% FROM $3,223.50. THREE-MONTH SETTLED $3,032.00, DOWN $32.00 OR 1.04% FROM $3,064.00 - back below the 3,042.00 low of 03-November and $45.00 below 3,077, but $7.50 above the 3,024.50 bear-trigger level and $21.50 above the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION NARROWED TO $123.50 FROM A SERIES-RECORD $159.50 AS FLAT PRICE FELL - SPREAD AND PRICE MOVED IN THE SAME DIRECTION (looser and lower): cash fell more than twice as much as three-month. A twenty-first straight backwardation and the tenth above $15.00. "
 "VISIBLE LME STOCK FELL 375 t TO 226,350 t, another new series low and a seventeenth straight draw. The Trading Economics aluminium reference showed about $3,018.90 (-1.45%) for 12-November - cited in text only, not used on the board.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,155.5","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"3,032.0","pos":False,"delta":VER+AL+" THREE-MONTH IS $45.00 BELOW THE 3,077 WEEKLY 50% RETRACEMENT and $29.50 below the 3,061.5 July low, $116.50 beneath the 3,148.5 wave (iv) high and $257.00 below the 3,289 daily invalidation. The 15-October settled low of 2,994.50 held for a twentieth session, $37.50 below."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+123.5","pos":True,"delta":VER+" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,155.50 against three-month $3,032.00 is a $123.50 BACKWARDATION, NARROWER than 11-November's series-record $159.50 as cash fell $68.00 and three-month $32.00 - SPREAD AND PRICE MOVED IN THE SAME DIRECTION (structure looser, price lower). It stays above the published $15.00 reversal condition for a tenth session and is a twenty-first straight backwardation; a contango beyond $24.50 would reverse the structural signal. SMM (13-November) describes the LME squeeze as heating up with a deeply backwardated curve and flags rollover risk after the November contract expires. The October mean spread was $"+f"{oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"226,350","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 375 t TO 226,350 t (11-November: -125 t to 226,725 t), another new series low and a seventeenth straight draw. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 11-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $3,032.00, DOWN $32.00 FROM THE 11-NOVEMBER $3,064.00 - back below 3,042.00 and $45.00 below 3,077; $7.50 above 3,024.50; $21.50 ABOVE the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 375 t TO 226,350 t, another new series low (11-November 226,725 t). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $123.50 BACKWARDATION, NARROWER THAN 11-NOVEMBER'S SERIES-RECORD $159.50 (10-November $110.00). CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On Thursday cash fell $68.00 and three-month $32.00, so STRUCTURE LOOSENED AND PRICE FELL (same direction). REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50 and $123.50."},
 {"name":"EUR/USD LME fixing","cur":1.1088,"prev":1.1132,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.10880 ON 12-NOVEMBER FROM 1.11320 ON 11-NOVEMBER as the dollar strengthened further. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (12-Nov official)","price":"3,155.5","basis":"THE THURSDAY 12-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,155.50, DOWN $68.00 OR 2.11% (11-November $3,223.50). Next official Friday 13-November 13:20 London."},
 {"tenor":"3-month (12-Nov official)","price":"3,032.0","basis":"THE 12-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $3,032.00, DOWN $32.00 - $45.00 below 3,077, $10.00 below 3,042.00, $7.50 above 3,024.50 and $37.50 above the 2,994.50 October low."},
 {"tenor":"Cash-to-3M structure","price":"+123.5 (BACKWARDATION)","basis":"A $123.50 BACKWARDATION, narrower than the $159.50 record with price LOWER (same direction) - above the $15.00 reversal condition for a tenth session."},
 {"tenor":"Visible LME stock","price":"226,350 t","basis":f"DOWN 375 t to a new series low on 12-November (seventeenth straight draw); October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PROMPT SQUEEZE EASES FROM ITS RECORD, OUTRIGHT PRICE GIVES BACK WEDNESDAY'S GAIN. On the 12-November official cash $3,155.50 sits $123.50 ABOVE three-month $3,032.00, a BACKWARDATION, narrower than the series-record $159.50 on 11-November as both legs fell (cash -$68.00, three-month -$32.00) - SPREAD AND FLAT PRICE MOVED IN THE SAME DIRECTION. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50 and now $123.50. "
 f"READ: a twenty-first straight backwardation, the tenth above $15.00, with visible stock at another low (226,350 t) - nearby LME metal stays scarce; SMM flags rollover risk once the November prompt expires. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2900,3450] and d['chart_stock_axis']==[200000,255000]

ls=d['lme_series']; assert ls[-1][0]=='11-Nov'
d['lme_series']=ls[1:]+[["12-Nov",cash,m3,stk]]
assert len(d['lme_series'])==15 and all(200000<r[3]<255000 and 2900<r[2]<3450 and 2900<r[1]<3450 for r in d['lme_series'])
CU=(13712.0,13655.0,328600); NI=(16010.0,16215.0,272526); ZN=(3760.5,3722.0,142625); PB=(1843.0,1879.0,286650)
CU6=(13875.5,13795.0,319675); NI6=(15930.0,16140.0,271632); ZN6=(3794.0,3746.0,143575); PB6=(1845.0,1880.0,292125)
assert CU6[2]+8925==CU[2] and NI6[2]+894==NI[2] and ZN6[2]-950==ZN[2] and PB6[2]-5475==PB[2]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU6[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI6[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN6[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB6[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU6[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI6[1],1)
zn8=[3935.0,3869.0,3875.0,3877.0,3759.0,3754.0,3768.0,3794.0]; pb8=[1869.5,1862.0,1858.0,1866.5,1857.0,1854.0,1846.0,1845.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zn8)+ZN[0])/9)/(sum(zn8)/8),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(pb8)+PB[0])/9)/(sum(pb8)/8),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU6[0]),('NI',NI[0],NI6[0]),('ZN',ZN[0],ZN6[0]),('PB',PB[0],PB6[0])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
ms['asof']='2026-11-12'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending THURSDAY 12-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 22-October dropped, 12-November appended, so the window is 23-October to 12-November. Every point is an official cash settlement from the Westmetall per-metal tables and English/German overviews (12-November read from both overviews, which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (12-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,CU6,f" COPPER 12-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU6[0])}; three-month ${CU[1]:,.2f}, {chg(CU[1],CU6[1])}. BACKWARDATION narrowed to $57.00 from $80.50. Stock ROSE 8,925 t to 328,600 t, the largest build on the board."),
 ("Nickel",NI,NI6,f" NICKEL 12-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI6[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI6[1])}. CONTANGO narrowed to $205.00 from $210.00, still the widest carry on the board. Stock rose 894 t to 272,526 t. Nickel was the only metal up on the day."),
 ("Zinc",ZN,ZN6,f" ZINC 12-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN6[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN6[1])}. BACKWARDATION narrowed to $38.50 from $48.00. Stock fell 950 t to 142,625 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,PB6,f" LEAD 12-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB6[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB6[1])}. CONTANGO $36.00 from $35.00. Stock fell 5,475 t to 286,650 t, the largest draw on the board."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Thursday 12-November official three-month aluminium fell 1.04%, copper 1.01%, zinc 0.64% and lead 0.05%, while nickel rose 0.46%. Copper stock built sharply; aluminium, zinc and lead drew. Trading Economics reports the dollar index near 103.16, its strongest since April 2025, with about 91% odds of a Fed hike next month; Brent rebounded to about $95.8. The LME euro fixing fell to 1.1088.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,c6,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='11-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["12-Nov",CU[0]]]; assert len(i['hist'])==15
        i['val']="~13,655.00 (3M); 13,712.00 (cash) $/t"; i['ratio']="~13,712.00 $/t cash vs LME 3M 13,655.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the THURSDAY 12-NOVEMBER-2026 session at $13,712.00 (11-November $13,875.50). THE WINDOW ROLLED THIS RUN: 22-October dropped and 12-November appended, so the series is the last fifteen published official cash sessions, 23-October to 12-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English/German overviews. "
                  "Copper structure for context: backwardation $57.00 on 12-November; stock 328,600 t (+8,925 t).")
s=d['inputs_summary']; assert s.startswith("UPDATE 12-NOVEMBER")
d['inputs_summary']=("UPDATE 13-NOVEMBER: Copper rolled one session to the Thursday 12-November LME official cash of $13,712.00, its fifteen-session window now 23-October to 12-November. No new monthly carbon settlement (due mid-November) or dated SMM fluoride, silicon or magnesium mark was located, so no other hist mark was appended. Energy turned firmer: Brent rebounded to about $95.8 after the US President said the US no longer needs a deal with Iran, and European gas jumped about 7% on 12-November to roughly EUR 92.7/MWh, then about EUR 95.3/MWh on 13-November, on colder forecasts, a Norwegian Troll outage and EU storage below 72% (Trading Economics). "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
ptl=0.5*pc; presid=2403-ptl; pshare=ptl/2403*100
OT=f"the tariff leg of the US duty-paid premium is 0.50 times the 11-November official cash of $3,223.50, or ${ptl:,.2f}, UP $43.25 against the 10-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${presid:,.2f}, so {pshare:.1f}%"
NT=f"the tariff leg of the US duty-paid premium is 0.50 times the 12-November official cash of $3,155.50, or ${tl:,.2f}, DOWN ${ptl-tl:,.2f} against the 11-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OC1="COMPILED THURSDAY 12-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE WEDNESDAY 11-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; THURSDAY'S OFFICIAL PRINTS 13:20 LONDON)."
NC1="COMPILED FRIDAY 13-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE THURSDAY 12-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; FRIDAY'S OFFICIAL PRINTS 13:20 LONDON)."
for p in d['premiums']:
    assert OT in p['src'] and OC1 in p['src'],p['name']
    p['src']=p['src'].replace(OT,NT).replace(OC1,NC1)
ra=398.24/m3*100; pra=398.24/pm*100
OR=f"THE RATIO: LME Alumina at $398.24/t against the 11-November aluminium three-month of $3,064.00 is {pra:.2f}%"
for a in d['alumina']:
    assert OR in a['src'],a['name']
    a['src']=a['src'].replace(OR,f"THE RATIO: LME Alumina at $398.24/t against the 12-November aluminium three-month of $3,032.00 is {ra:.2f}%").replace(OC1,NC1)
OC0="COMPILED THURSDAY 12-NOVEMBER-2026 ABOUT 02:40 LONDON; THE BOARD IS THE WEDNESDAY 11-NOVEMBER-2026 LME OFFICIAL."
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace(OC1,NC1).replace(OC0,"COMPILED FRIDAY 13-NOVEMBER-2026 ABOUT 02:40 LONDON; THE BOARD IS THE THURSDAY 12-NOVEMBER-2026 LME OFFICIAL.")
        o=o.replace("REVIEWED 12-NOVEMBER: no newer public disclosure","REVIEWED 13-NOVEMBER: no newer public disclosure").replace("REVIEWED 12-NOVEMBER. NO NEW DATED","REVIEWED 13-NOVEMBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status','inputs','logistics','raw_materials'):
    if k in d: d[k]=walk(d[k])

d['lme_commentary']=("RECORD SQUEEZE EASES, PRICE GIVES BACK. The Thursday 12-November official cut cash $68.00 to $3,155.50 and three-month $32.00 to $3,032.00, so the backwardation narrowed to $123.50 from Wednesday's series-record $159.50 - still a twenty-first straight backwardation - with spread and price again moving in the SAME direction. Visible stock fell another 375 t to a new low of 226,350 t. "
 "Three-month slipped back below the 3,042 low of 03-November but held $7.50 above the 3,024.50 bear trigger, so no pre-registered rule fired and weights stay 15/45/40; the daily Elliott alternate is re-favoured without a re-label. "
 "SMM (13-November) describes the LME squeeze as heating up on a deeply backwardated curve, with SHFE consolidating and limited room for deep declines, but flags rollover risk once the November contract expires; China's three-region ingot inventory fell into the 340 kt range. Against that, the dollar index firmed to about 103.16, its strongest since April 2025, and Chinese smelters keep building overseas capacity. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" its October mean.")
d['net_read']=("NET: NEUTRAL - PROMPT STILL TIGHT, FORWARD PRICE CAPPED, ENERGY FLOOR FIRMING. Supportive: a $123.50 backwardation (twenty-first straight, tenth above $15.00), visible LME stock at a new low of 226,350 t, Hormuz still listed closed with three tankers reportedly attacked in two days, and Brent and European gas rebounding sharply. "
 "Against: three-month at $3,032.00 is back below 3,042 and $45.00 under the 3,077 bull trigger; a dollar index near 103.16 with about 91% odds of a Fed hike next month; Chinese overseas smelter build-out; SMM flags rollover risk after the November prompt.")
d['bottom_line']=("BOTTOM LINE: LME aluminium three-month fell $32.00 to $3,032.00 on the Thursday 12-November official and cash $68.00 to $3,155.50, narrowing the backwardation to $123.50 from Wednesday's record $159.50 while visible stock fell to another low of 226,350 t - nearby metal is still scarce, but the forward price gave back Wednesday's gain and sits just $7.50 above the bear trigger against a dollar at its strongest since April 2025. "
 "Weights stay 15% bull / 45% base / 40% bear: no pre-registered rule fired. A settled close above 3,077 with the backwardation beyond $15.00 returns five points to bull; a settled close below 3,024.50, or a contango beyond $24.50, adds bear weight. Daily Elliott invalidation 3,289. Next official Friday 13-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, PROMPT PREMIUM UP AGAIN:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, PROMPT PREMIUM STILL HIGH BUT OFF ITS RECORD: a $123.50 backwardation on 12-November, narrower than the $159.50 record as cash fell $68.00 and three-month $32.00 - a tenth print above the $15.00 reversal condition, so nearby metal is still valued well over forward metal and there is no carry reward for deferring purchases; SMM flags rollover risk once the November prompt expires; the outright three-month price sits $45.00 below the 3,077 bull trigger and $7.50 above the 3,024.50 bear trigger. "+c2[a1:]
o=f"is ${ptl:,.2f} on 11-November cash, {pshare:.1f}% of the $2,403/t premium"; assert o in c2; c2=c2.replace(o,f"is ${tl:,.2f} on 12-November cash, {share:.1f}% of the $2,403/t premium")
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find(" Hindalco's",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 12-November official cut three-month to $3,032.00, back below 3,042 and $37.50 above the 2,994.50 settled low; Brent rebounded to about $95.8 and European gas to about EUR 95.3/MWh (Trading Economics 13-November); the dollar index near 103.16, its strongest since April 2025, with about 91% odds of a Fed hike next month; EGA reported 9M-2026 adjusted EBITDA of $1.572bn at a 29.8% margin with 766 of 1,262 Al Taweelah cells restarted and full restart targeted for Q1-2027 (AL Circle 12-November); a possible US-Canada deal that would cut the US tariff on Canadian aluminium to 25% is reported but unconfirmed (AL Circle 11-November); Maaden (1211) reported Q3-2026 aluminium EBITDA of $419m (Arab News 09-November);"+c2[b1:]
o="EGA has restarted half of Al Taweelah's cells (21-October)"
if o in c2: c2=c2.replace(o,"EGA had restarted half of Al Taweelah's cells by 21-October and 61% by its 9M report")
d['commercial']=c2

for s in d['outlook']['scenarios']:
    s['drivers']=("HELD 13-NOVEMBER at 15/45/40: the Thursday 12-November official settled three-month at $3,032.00 - $45.00 short of 3,077 (the bull trigger, which also needs a backwardation beyond $15.00; it is $123.50) and $7.50 above 3,024.50 (the bear trigger) - so no pre-registered rule fired. ")+s['drivers']
sp=d['outlook']['scenario_paths']
for k in ('bull','base','bear'): sp[k][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 13-NOVEMBER: the 12-November official printed a $123.50 BACKWARDATION, a tenth session above $15.00, narrower than the $159.50 record as flat price fell; SMM flags rollover risk after the November prompt expires. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 13-NOVEMBER: LME stock fell 375 t on 12-November to a new low of 226,350 t, a seventeenth straight draw. Trend held at FLAT: the daily pace remains modest."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 13-NOVEMBER - TREND RAISED FROM DOWN TO FLAT: Brent rebounded to about $95.8 from about $92 after the US President said the US no longer needs a deal with Iran, and the Straits Daily Brief reports oil settling about $3 higher on reported attacks on Saudi energy sites (single source, not independently confirmed); European gas jumped about 7% on 12-November and traded near EUR 95.3/MWh on 13-November on a Norwegian Troll outage, colder forecasts and EU storage below 72% (Trading Economics). The two-session rebound ends the clear downtrend, but Brent remains well below its October peak."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 13-NOVEMBER: Straits Daily Brief - strait still listed CLOSED; lagged count 3 transits on 08-November (vs 85/day pre-crisis); AIS-visible vessels holding rose to 51 from 42 (likely an undercount). Three tankers reportedly attacked in two days (Maritime Executive, gCaptain); Iran's military claims four tankers struck (unconfirmed by any maritime authority); a merchant vessel reportedly hit by a projectile near the UAE (single source, unverified); the IMO Secretary-General called on member states to enforce maritime safety rules. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 13-NOVEMBER: the dollar index held near 103.16, its strongest since April 2025, with about 91% odds of a hike next month and further hikes priced for early 2027 (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('TARIFF POLICY'):
        r['risk']+=" UPDATE 13-NOVEMBER: no official confirmation located of the reported US-Canada deal (25% on Canadian aluminium); the 50% Section 232 rate is unchanged. Trend held at FLAT."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE GULF SUPPLY PICTURE'):
        r['risk']+=" UPDATE 13-NOVEMBER: EGA's 9M-2026 report (AL Circle, 12-November) states 766 of 1,262 Al Taweelah cells requiring recommissioning (61%) have restarted, with full restart targeted for Q1-2027; cast-metal output was 1.376 Mt in 9M against 2.126 Mt a year earlier. Trend held at FLAT."; r['trend']='flat'; hit+=1
assert hit==7,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Thu 12-Nov':
        hc+=1; cat['date']='Daily, from Fri 13-Nov'
        cat['event']=("THURSDAY 12-NOVEMBER OFFICIAL: three-month $3,032.00 (-$32.00), cash $3,155.50 (-$68.00), backwardation $123.50 - no rule fired, $7.50 above the bear trigger and $45.00 below the bull trigger; weights 15/45/40. NEXT: a settled close above 3,077 with the backwardation beyond $15.00 returns five points to bull; a settled close below 3,024.50 adds bear weight; below about 2,977.5 forces a re-count toward 2,894. Invalidation 3,289. LME November prompt expiry and rollover; mid-November carbon (anode/CTP/petcoke) settlements; any official US-Canada tariff announcement; first Q1-2027 Japanese premium offers.")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"FRIDAY 13-NOVEMBER ON THE THURSDAY 12-NOVEMBER OFFICIAL: cash fell $68.00 to $3,155.50 and three-month $32.00 to $3,032.00, narrowing the backwardation to $123.50 from the $159.50 record while stock fell to another low of 226,350 t. The prompt squeeze is intact but eased with price, and SMM flags rollover risk after the November contract expires. The macro backdrop is two-sided: the dollar index is at its strongest since April 2025 on Fed-hike pricing, while Brent and European gas rebounded sharply on Gulf tensions and a Norwegian outage, firming the smelter energy floor. Three-month sits $7.50 above the 3,024.50 bear trigger - the next settled close below it would add bear weight.")

EWP=("REVIEWED 13-NOVEMBER ON THE 12-NOVEMBER OFFICIAL: three-month settled 3,032.00 (-32.00), BACK BELOW the 3,042.00 B/2 low - the pre-registered trigger that FAVOURS THE ALTERNATE - so the preference returns to the alternate at about 60% (the rebound from 2,994.50 to 3,097.50 was a completed corrective bounce and 3,064 on 11-November was a lower high) against about 40% for the base (a deeper wave (ii) of C/3 holding above 2,994.50). The count is NOT re-labelled: no invalidation level broke. A settled close below 3,024.50 strengthens the alternate and below 2,994.50 ends the base count; below about 2,977.5 forces a re-count toward the 2,894 weekly 61.8%. A recovery above 3,097.50 would restore the base toward 3,110 and 3,148.5. Invalidation 3,289; confidence low. ")
EWL=("REVIEWED 13-NOVEMBER (LATE WEEK): the Thursday official at 3,032.00 fell back below the 3,061.5 July low and stays well below the 3,077 50% retracement, REINFORCING the weekly base case - the corrective count toward the 61.8% retracement at 2,894 - which loses preference only on a weekly close above 3,110. Alternate (2,994.50 completed the correction) held at about 30%: the $123.50 backwardation and record-low stock support it, but the forward price failed again below 3,077. Confidence moderate. ")
pre_s="REVIEWED 12-NOVEMBER ON THE 11-NOVEMBER OFFICIAL:"; pre_l="REVIEWED 12-NOVEMBER (MID-WEEK):"
assert d['ew']['short_term']['writeup'].startswith(pre_s) and d['ew']['long_term']['writeup'].startswith(pre_l)
d['ew']['short_term']['writeup']=EWP+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=EWL+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="95.8",day="about $95.4-95.8 on 13-November (Trading Economics; table 95.84 +0.02%, stats 95.43); the Straits Daily Brief shows $95.86, +3.71% over 24h",
 note="REFRESHED FRIDAY 13-NOVEMBER-2026 (Trading Economics): Brent held near $96 after gaining in the prior session as the US President said the US no longer needs a deal with Iran, denting hopes of a diplomatic end to the conflict; Iran says the naval blockade and sanctions must be lifted before direct talks. Oil is still on track for a second weekly decline as Middle Eastern exports recover. The Straits Daily Brief reports oil settled about $3 higher on reported attacks on Saudi energy sites and strait disruptions (single source). Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="95.3",day="about EUR 95.1-95.3/MWh on 13-November (Trading Economics; sections differ), +3.3%, after a ~7% jump to about EUR 92.7 on 12-November",
 note="REFRESHED FRIDAY 13-NOVEMBER-2026 (Trading Economics): colder forecasts, a Norwegian Troll field outage of uncertain duration and Middle East tensions lifted prices; EU storage below 72% against a five-year average of about 89%, Germany below 60%. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="103.16",day="about 103.15-103.16 on 13-November (Trading Economics, -0.01%), strongest since April 2025 after gaining more than 1% over two sessions",
 note="REFRESHED FRIDAY 13-NOVEMBER-2026 (Trading Economics): hotter October inflation and hawkish Fed commentary drove the rally; markets price about 91% odds of a hike next month, with further hikes weighed for January and possibly April. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.10880',day="LME fixing on 12-November, down from 1.11320 on 11-November",note="REFRESHED FRIDAY 13-NOVEMBER-2026 to the 12-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE THURSDAY 12-NOVEMBER-2026 LME OFFICIAL, the latest published session: this Friday 13-November run (about 02:40 London) precedes Friday's ring, whose official prints at 13:20 London and will be picked up by the next run. The board rolled ONE session this run (from Wednesday 11-November). The Trading Economics aluminium reference (about $3,018.90, -1.45% for 12-November) is cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (13-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 12-November session (aluminium cash 3,155.50, three-month 3,032.00, stock 226,350; EUR/USD MTLE 1.10880); the aluminium per-metal daily table shows 12-November as its newest row.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 05 to 11-November rows match the stored series exactly; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 12-November values come from both overviews, which agree, and each metal's stock change reconciles with its 11-November stock.")
C[3]=("STOCK CHANGES 12-November (also shown in the pages' change column): aluminium -375 to 226,350; copper +8,925 to 328,600; nickel +894 to 272,526; zinc -950 to 142,625; lead -5,475 to 286,650.")
c4=C[4]; k=c4.find("The price chart ax"); assert k>0
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (12-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (nine sessions, 02-12 November) as their latest point. ")+c4[k:]
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,155.50 against three-month $3,032.00 is therefore a $123.50 BACKWARDATION, narrower than the $159.50 record on 11-November - on Thursday the spread and the flat price moved in the SAME direction (structure looser, price lower)."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("THE TARIFF DECOMPOSITION IS CALCULATED"):
        o=f"the tariff leg is 0.50 times the 11-November official cash of $3,223.50, or ${ptl:,.2f}, leaving a ${presid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({pshare:.1f}% policy arithmetic)"
        assert o in cv
        C[i]=cv.replace(o,f"the tariff leg is 0.50 times the 12-November official cash of $3,155.50, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic)"); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $95.8), the dollar index (about 103.16) and TTF (about EUR 95.3/MWh) are Trading Economics readings for 13-November (Asian hours); Trading Economics prices are contract-for-difference references, not official benchmarks, and its pages again showed different levels in different sections (Brent 95.84 vs 95.43; TTF 95.33 vs 95.12; dollar 103.164 vs 103.148), so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (13-November) shows Brent about $95.86 (+3.71% over 24h) and its status bar $95.30; the brief labels its ticker AI-assisted, and its incident items are flagged here as reported or unverified where the brief does so."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 13-NOVEMBER: no authorised fetch was blocked (Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/TTF/dollar, AL Circle, news.metal.com and the Straits Daily Brief all fetched). news.metal.com carried SMM's 13-November morning summary (no SHFE price figure quoted), a three-region ingot inventory note (340 kt range) and the weekly processing survey; SHFE/A00 price rows are not refreshed this run. mining.com was not fetched. A search for Q1-2027 Japanese premium offers found none (market talk of $190-200/t is expectation, not an offer), so Q1 stays unpriced. A report of attacks on Saudi energy sites appears only in the Straits Daily Brief; a search did not locate an independent dated confirmation, so it is cited as single-source."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        rest=cv.split("PEER EARNINGS:",1)[1].strip()
        C[i]=("PEER EARNINGS: NO NEW LISTED-PEER RESULT ADDED THIS RUN (13-NOVEMBER). EGA (not listed) published 9M-2026 results (AL Circle, 12-November): adjusted EBITDA $1.572bn (9M-2025 $1.738bn) at a 29.8% margin, revenue $5.282bn, adjusted net profit $744m; these appear in the producer monitor and news, not in the listed-peer table. No earnings_history company was back-filled this run. EARLIER: "+rest); hit+=1
assert hit==4,hit

d['so_what']={"line":"LME aluminium gave back Wednesday's jump on Thursday - three-month fell $32 to $3,032 and cash $68 to $3,155.50 - and the backwardation eased to $123.50 from its $159.50 record, while LME stock hit another low; three-month now sits just $7.50 above the $3,024.50 bear trigger as the dollar holds its strongest level since April 2025.",
 "points":[
 "WHAT MOVED: the Thursday 12-November official cut cash 2.11% to $3,155.50 and three-month 1.04% to $3,032.00, so the backwardation narrowed to $123.50 from $159.50 - spread and price fell together; visible LME stock fell 375 t to 226,350 t, a seventeenth straight draw.",
 "WHY: the squeeze is intact but eased with price - SMM says the LME squeeze is heating up on a deeply backwardated curve yet flags rollover risk once the November contract expires; the dollar index near 103.16 with about 91% odds of a Fed hike next month weighs on metals.",
 "ENERGY FIRMED: Brent rebounded to about $95.8 and European gas to about EUR 95.3/MWh (Trading Economics) on Gulf tensions, a Norwegian outage and low EU storage; Hormuz stays listed closed, with three tankers reportedly attacked in two days (Straits Daily Brief).",
 "WHAT TO WATCH: a settled three-month close below $3,024.50 (bear trigger) or above $3,077 (bull trigger); the LME November prompt rollover; mid-November carbon-input settlements; EGA's Al Taweelah restart (61% of cells back, full restart targeted Q1-2027)."]}

d['feed']=([
 {"when":"Thu 12-Nov","impact":"Bearish","text":"12-NOVEMBER OFFICIAL: three-month $3,032.00 (-$32.00), cash $3,155.50 (-$68.00); backwardation $123.50 from $159.50 record; stock -375 t to 226,350 t."},
 {"when":"Thu 12-Nov","impact":"Mixed","text":"EGA 9M-2026: adj. EBITDA $1.572bn, margin 29.8%; 766 of 1,262 Al Taweelah cells restarted; full restart targeted Q1-2027 (AL Circle)."},
 {"when":"Thu 12-Nov","impact":"Bullish","text":"ENERGY: Brent ~$95.8, TTF ~EUR 95.3/MWh after ~7% jump; Troll outage, EU storage below 72% (Trading Economics)."},
 {"when":"Fri 13-Nov","impact":"Bullish","text":"HORMUZ: still listed closed; vessels holding up to 51; three tankers reportedly attacked in two days (Straits Daily Brief)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM GIVES BACK WEDNESDAY'S JUMP; BACKWARDATION EASES TO $123.50. The Thursday 12-November official settled cash at $3,155.50 (-2.11%) and three-month at $3,032.00 (-1.04%), back below the 3,042 low of 03-November and $7.50 above the 3,024.50 bear trigger; the cash premium narrowed from a series-record $159.50 and visible stock fell 375 t to a new low of 226,350 t. Board: nickel +0.46%, lead -0.05%, zinc -0.64%, copper -1.01%, aluminium -1.04%."},
 {"theme":"LME structure","horizon":"0-1 month","impact":"Mixed","url":S_SM,
  "headline":"LME SQUEEZE HEATS UP, SHFE CONSOLIDATES (SMM morning summary, 13-November): SMM says SHFE aluminium is consolidating with limited room for deep declines, the LME is supported by nearby squeezes and a deeply backwardated curve, and flags rollover risk after the November contract expires."},
 {"theme":"Gulf supply","horizon":"0-6 months","impact":"Bearish","url":S_EG,
  "headline":"EGA: 61% OF AL TAWEELAH CELLS BACK, FULL RESTART BY Q1-2027 (AL Circle, 12-November): EGA's 9M-2026 adjusted EBITDA was $1.572bn (9M-2025 $1.738bn) at a 29.8% margin on revenue of $5.282bn; cast-metal output 1.376 Mt (2.126 Mt a year earlier). 766 of 1,262 cells requiring recommissioning have restarted after the 28-March attack; restoration capex about $400m; the alumina refinery reached about 70% by early September. READ: more Gulf metal returning through Q1-2027."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish","url":S_TG,
  "headline":"EUROPEAN GAS AND BRENT REBOUND (Trading Economics, 12-13 November): TTF jumped about 7% to roughly EUR 92.7/MWh on 12-November and traded near EUR 95.3 on 13-November on colder forecasts, a Norwegian Troll outage and EU storage below 72% (five-year average 89%); Brent held near $96 after the US President said the US no longer needs a deal with Iran. READ: a firmer energy floor for European and Gulf smelting costs."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"DOLLAR HOLDS STRONGEST SINCE APRIL 2025 (Trading Economics, 13-November): the dollar index held near 103.16 after a two-session gain of more than 1% on hotter October inflation and hawkish Fed commentary; markets price about 91% odds of a hike next month."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL CLOSED, MORE TANKER INCIDENTS (Straits Daily Brief, 13-November): 3 transits on 08-November vs 85/day pre-crisis; AIS-visible vessels holding rose to 51 (likely an undercount). Three tankers reportedly attacked in two days; Iran's military claims four tankers struck (unconfirmed); a merchant vessel reportedly hit by a projectile near the UAE (single source); the IMO Secretary-General urged enforcement of maritime safety rules."},
 {"theme":"China","horizon":"0-1 month","impact":"Mixed","url":S_SI,
  "headline":"CHINA INGOT STOCKS FALL, PROCESSING RATE EASES (SMM, 13-November): social aluminium ingot inventory in three regions fell into the 340 kt range and 6063 billet inventory in two regions eased to 63 kt; the leading downstream processing operating rate fell 0.2 points to 61.8% on environmental controls and off-season weakness."},
 {"theme":"Trade policy","horizon":"Structural","impact":"Mixed","url":S_KZ,
  "headline":"KAZAKHSTAN RESTRICTS ALUMINIUM FOIL EXPORTS TILL 2030 (AL Circle, 12-November): Kazakhstan is tightening EAEU trade and restricting aluminium foil exports until 2030."},
 {"theme":"Bauxite","horizon":"Structural","impact":"Mixed","url":S_VN,
  "headline":"VIETNAM BAUXITE PROJECT (AL Circle, 12-November): Vinacomin has proposed a $208m bauxite mining project in Lam Dong province."},
]+d['news']
d['news']=d['news'][:20]

hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('EGA'):
        p['status']="PARTIAL RESTART - 766 OF 1,262 AL TAWEELAH REDUCTION CELLS (61%) RESTARTED PER EGA'S 9M-2026 REPORT; FULL RESTART TARGETED Q1-2027"
        p['update']="UPDATED 13-NOVEMBER (AL Circle, 12-November, on EGA's 9M-2026 results): 766 of 1,262 cells requiring recommissioning (61%) had restarted after the 28-March attack on KEZAD; full restart programme targeted for completion in Q1-2027; restoration capex about $400m, mostly in 2026; the alumina refinery restarted in early July at about 50% and reached about 70% by early September; recycling casting stations at 50%, full production expected H2-2027. 9M cast-metal output 1.376 Mt (9M-2025 2.126 Mt); adjusted EBITDA $1.572bn at a 29.8% margin. "+p['update']
        p['src']=[L_EG,S_EG]; hit+=1
    elif p['name'].startswith('China operators'):
        p['update']="UPDATED 13-NOVEMBER (SMM, 13-November): three-region social ingot inventory fell into the 340 kt range; the leading downstream processing operating rate eased 0.2 points to 61.8% on environmental controls and off-season weakness ("+S_SI+"). "+p['update']; hit+=1
assert hit==2

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 12-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 12-Nov)",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_EG,S_EG],[L_KZ,S_KZ],[L_VN,S_VN],[L_SM,S_SM],[L_SI,S_SI],[L_SP,S_SP]): d['sources'].append(x)
for x in ([L_TE,S_TE],[L_TD,S_TD],[L_ST,S_ST],[L_EG,S_EG],[L_SM,S_SM]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-11-11'
ph['rows'][-1]=['2026-11-12',cash,m3,stk]; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2),d['metals_board'])
