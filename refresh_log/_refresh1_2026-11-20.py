# Daily data refresh - 2026-11-20 (FRIDAY, ~02:35 UTC, before today's ring). Board ROLLED ONE SESSION to the WEDNESDAY 18-Nov LME official
# (the 19-Nov official not yet on Westmetall at run time). Cache-busted EN + DE overviews agree on 18-Nov (Al cash 3,095.00 / 3M 2,865.00 /
# stock 226,150; MTLE 1.09630); Al per-metal table newest row 18-Nov, 22-Oct..17-Nov rows match stored series; Cu/Ni/Zn/Pb tables re-fetched.
# 3M settled BELOW 2,894 (pre-registered bear-weight trigger) -> weights 10/40/50 -> 10/35/55. Cash UP while 3M DOWN: backwardation widens to $230.
# Stock +5,800 t: first build after twenty straight draws.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-20'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-20"; L_ST="Straits Daily Brief - Strait of Hormuz, 20-Nov-2026 (Brent figure AI-assisted)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,868.35 (+1.18%) on 19-Nov-2026 after a 2026 low below $2,900; forecast 2027 surplus 830 kt (CFD reference)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$92.4-92.6, third straight weekly drop; Hormuz flows at record per US Energy Secretary (20-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.90; December 25bp hike priced, ~10% odds of 50bp (20-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 85.9-86.2/MWh; EU storage 70.15% (20-Nov-2026)"
S_BRC="https://www.brecorder.com/news/40449557/copper-tumbles-to-seven-month-low-on-speculative-selling-and-inflation-fears"; L_BRC="Business Recorder (Reuters) - Copper tumbles to seven-month low; LME aluminium -2.2% to $2,869 by 1100 GMT (18-Nov-2026)"
S_EM="https://www.alcircle.com/news/aluminium-supply-crunch-to-persist-till-2028-driven-by-chinas-45mt-cap-low-stocks-122031"; L_EM="AL Circle - Aluminium supply crunch to persist till 2028 (Emkay Global: ~400 kt deficit in 2027 and 2028; bear case $2,600/t) (19-Nov-2026)"
S_IN="https://www.alcircle.com/news/india-probes-aluminium-dumping-by-china-malaysia-vietnam-thailand-vedanta-hindalco-shares-eyed-122026"; L_IN="AL Circle - India's DGTR opens anti-dumping probe into aluminium extrusions from China, Malaysia, Vietnam, Thailand (19-Nov-2026)"
S_CB="https://www.alcircle.com/news/eu-industrial-emissions-fall-3-3-as-cbam-expansion-eyes-more-aluminium-products-122022"; L_CB="AL Circle - EU industrial emissions fall 3.3% as CBAM expansion eyes more aluminium products (19-Nov-2026)"
S_DB="https://www.alcircle.com/news/dubai-pushes-circular-economy-with-mandatory-material-passport-for-aluminium-from-2027-122030"; L_DB="AL Circle - Dubai mandates a material passport for aluminium from 2027 (19-Nov-2026)"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o

B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3060.5 and B['LME 3-month']['cur']==2940.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3060.5,2940.0,220350
cash,m3,stk=3095.0,2865.0,226150
spr=cash-m3; psp=pc-pm; assert spr==230.0 and psp==120.5 and ps+5800==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED FRIDAY 20-NOVEMBER-2026 ABOUT 02:35 LONDON, BEFORE TODAY'S RING. THE BOARD IS THE WEDNESDAY 18-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION AT RUN TIME (the Thursday 19-November official had not yet appeared on Westmetall; it is NOT estimated). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 18-November official for all metals with stocks and FX (EUR/USD MTLE 1.09630; 17-November 1.09930); (2) the aluminium, copper, nickel, zinc and lead per-metal daily tables all show 18-November as their newest row, and the aluminium table's 22-October to 17-November rows match the stored series. "
 "The whole board sits on ONE UNIFORM SESSION (18-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" WEDNESDAY 18-NOVEMBER (the board): CASH SETTLED $3,095.00, UP $34.50 OR 1.13% FROM $3,060.50. THREE-MONTH SETTLED $2,865.00, DOWN $75.00 OR 2.55% FROM $2,940.00 - BELOW the 2,894 weekly 61.8% retracement and below the 2,894-2,906 Elliott target zone, the lowest three-month official in this series and $145.50 BELOW the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION WIDENED TO $230.00 FROM $120.50 - a twenty-fifth straight backwardation and the fourteenth above $15.00. SPREAD AND FLAT PRICE MOVED IN OPPOSITE DIRECTIONS: cash rose while three-month fell, so the prompt premium rebuilt even as the forward price slid. "
 "VISIBLE LME STOCK ROSE 5,800 t TO 226,150 t - the FIRST BUILD after twenty straight draws, consistent with European metal being delivered into the backwardation. Reuters (via Business Recorder, 18-November) had three-month near $2,869 by 11:00 GMT on Wednesday in a broad sell-off (copper -3.5% to a seven-month low). The Trading Economics aluminium reference shows about $2,868.35 (+1.18%) for 19-November - a CFD reference cited in text only.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,095.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"2,865.0","pos":False,"delta":VER+AL+" THREE-MONTH IS NOW $29.00 BELOW THE 2,894 WEEKLY 61.8% RETRACEMENT, $41.50 BELOW the 2,906.5 wave (v) = wave (i) projection and $15.00 ABOVE the top of the 2,830-2,850 extended-(v) alternate zone. A settled close back above 2,994.50 would signal a failed break; above 3,097.50 negates the re-counted wave (v); daily invalidation of the bearish count remains 3,289."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+230.0","pos":True,"delta":VER+f" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,095.00 against three-month $2,865.00 is a $230.00 BACKWARDATION, UP from $120.50 on 17-November, as cash rose $34.50 while three-month fell $75.00 - SPREAD AND FLAT (FORWARD) PRICE MOVED IN OPPOSITE DIRECTIONS. It stays above the published $15.00 reversal condition for a fourteenth session and is a twenty-fifth straight backwardation; a contango beyond $24.50 would reverse the structural signal. The October mean spread was ${oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"226,150","pos":False,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK ROSE 5,800 t TO 226,150 t (17-November: -1,550 t to 220,350 t) - THE FIRST BUILD AFTER TWENTY STRAIGHT DRAWS, ending the draw streak; 220,350 t on 17-November stands as the series low. A steep backwardation rewards delivering metal onto the exchange, and AL Circle (17-November) reported European stockholders liquidating into it. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 17-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $2,865.00, DOWN $75.00 FROM THE 17-NOVEMBER $2,940.00 - $29.00 BELOW the 2,894 weekly 61.8% and below the 2,894-2,906 Elliott zone, the lowest three-month official in this series; $145.50 BELOW the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK UP 5,800 t TO 226,150 t - the first build after twenty straight draws (17-November 220,350 t, the series low). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $230.00 BACKWARDATION, UP FROM $120.50 ON 17-NOVEMBER. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On Wednesday cash ROSE $34.50 while three-month FELL $75.00 - spread and flat price moved in OPPOSITE directions. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50 and $230.00."},
 {"name":"EUR/USD LME fixing","cur":1.0963,"prev":1.0993,"avg":1.1465,"note":VER+" THE LME EURO FIXING FELL TO 1.09630 ON 18-NOVEMBER FROM 1.09930 ON 17-NOVEMBER as the dollar index held near 103.9 after hawkish FOMC minutes. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (18-Nov official)","price":"3,095.0","basis":"THE WEDNESDAY 18-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,095.00, UP $34.50 OR 1.13% (17-November $3,060.50). The 19-November official was not yet published at run time; next print Friday 20-November 13:20 London."},
 {"tenor":"3-month (18-Nov official)","price":"2,865.0","basis":"THE 18-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $2,865.00, DOWN $75.00 - $29.00 BELOW the 2,894 weekly 61.8% retracement, $15.00 above the 2,830-2,850 extended-(v) zone."},
 {"tenor":"Cash-to-3M structure","price":"+230.0 (BACKWARDATION)","basis":"A $230.00 BACKWARDATION, up from $120.50 - cash rose while three-month fell (opposite directions)."},
 {"tenor":"Visible LME stock","price":"226,150 t","basis":f"UP 5,800 t on 18-November - the first build after twenty straight draws; October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PROMPT TIGHT, FORWARD WEAK - THE CURVE STEEPENS. On the 18-November official cash $3,095.00 sits $230.00 ABOVE three-month $2,865.00, a BACKWARDATION up from $120.50, as cash rose $34.50 while three-month fell $75.00 - spread and flat price moved in OPPOSITE directions. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50 and now $230.00. "
 f"READ: a twenty-fifth straight backwardation, but for the first time in twenty-one sessions visible stock ROSE (+5,800 t to 226,150 t) - the backwardation is drawing metal onto the exchange, as AL Circle reported European stockholders liquidating into it. The market is pricing scarce prompt metal against a looser 2027 (Trading Economics cites forecasts of an 830 kt 2027 surplus; Emkay Global, via AL Circle, still sees a ~400 kt deficit). The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2800,3450] and d['chart_stock_axis']==[190000,255000]
d['chart_price_axis']=[2700,3450]   # re-bracketed: three-month 2,865 only $65 above the 2,800 floor

ls=d['lme_series']; assert ls[-1][0]=='17-Nov'
d['lme_series']=ls[1:]+[["18-Nov",cash,m3,stk]]
assert len(d['lme_series'])==15 and all(190000<r[3]<255000 and 2700<r[2]<3450 and 2700<r[1]<3450 for r in d['lme_series'])
CU=(12750.0,12773.5,327400); NI=(15800.0,15985.0,274116); ZN=(3732.0,3600.0,146775); PB=(1831.0,1864.0,269000)
CU7=(13225.5,13211.0,327600); NI7=(15790.0,15990.0,274140); ZN7=(3776.0,3661.0,148375); PB7=(1840.0,1874.0,270800)
assert CU7[2]-200==CU[2] and NI7[2]-24==NI[2] and ZN7[2]-1600==ZN[2] and PB7[2]-1800==PB[2]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU7[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI7[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN7[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB7[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU7[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI7[1],1)
zn12=[3935.0,3869.0,3875.0,3877.0,3759.0,3754.0,3768.0,3794.0,3760.5,3745.0,3848.0,3776.0]; pb12=[1869.5,1862.0,1858.0,1866.5,1857.0,1854.0,1846.0,1845.0,1843.0,1853.0,1856.0,1840.0]
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zn12)+ZN[0])/13)/(sum(zn12)/12),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(pb12)+PB[0])/13)/(sum(pb12)/12),1)
ms=d['metals_series']; R=ms['rows']
for k,v,pv in (('CU',CU[0],CU7[0]),('NI',NI[0],NI7[0]),('ZN',ZN[0],ZN7[0]),('PB',PB[0],PB7[0])):
    assert R[k][-1]==pv,(k,R[k][-1]); R[k]=R[k][1:]+[v]; assert len(R[k])==15
# verify window against per-metal tables fetched this run (29-Oct..18-Nov)
assert R['CU']==[14560.0,14449.0,14380.0,14110.5,14201.0,14110.0,13955.0,14030.0,13992.0,13875.5,13712.0,13610.0,13375.0,13225.5,12750.0],R['CU']
assert R['PB']==[1878.0,1890.0,1869.5,1862.0,1858.0,1866.5,1857.0,1854.0,1846.0,1845.0,1843.0,1853.0,1856.0,1840.0,1831.0],R['PB']
ms['asof']='2026-11-18'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending WEDNESDAY 18-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 28-October dropped, 18-November appended, so the window is 29-October to 18-November. Every point is an official cash settlement from the Westmetall per-metal tables (all four re-fetched this run and matching the stored window) and the English/German overviews.")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (18-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return "unchanged" if a==b else f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,f" COPPER 18-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU7[0])}; three-month ${CU[1]:,.2f}, {chg(CU[1],CU7[1])} - the lowest three-month official in this window. STRUCTURE FLIPPED TO A $23.50 CONTANGO from a $14.50 backwardation. Stock fell 200 t to 327,400 t. Reuters (via Business Recorder) reported copper's fifth straight loss to its lowest since 13-April on speculative selling and inflation fears."),
 ("Nickel",NI,f" NICKEL 18-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI7[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI7[1])}. CONTANGO $185.00 from $200.00, still the widest carry on the board. Stock fell 24 t to 274,116 t."),
 ("Zinc",ZN,f" ZINC 18-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN7[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN7[1])}. BACKWARDATION widened to $132.00 from $115.00. Stock fell 1,600 t to 146,775 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,f" LEAD 18-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB7[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB7[1])}. CONTANGO $33.00 from $34.00. Stock fell 1,800 t to 269,000 t."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(" CROSS-METAL: on the Wednesday 18-November official three-month copper fell 3.31%, aluminium 2.55%, zinc 1.67%, lead 0.53% and nickel 0.03% - a second broad risk-off session after hawkish FOMC minutes (nearly all policymakers backing further hikes; Trading Economics). Saxo Bank's Ole Hansen cited 'the inflation scare, the risk of higher funding costs' (Reuters via Business Recorder). The LME euro fixing fell to 1.0963.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='17-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["18-Nov",CU[0]]]; assert len(i['hist'])==15
        assert [v for _,v in i['hist']]==R['CU']
        i['val']="~12,773.50 (3M); 12,750.00 (cash) $/t"; i['ratio']="~12,750.00 $/t cash vs LME 3M 12,773.50 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the WEDNESDAY 18-NOVEMBER-2026 session at $12,750.00 (17-November $13,225.50). THE WINDOW ROLLED THIS RUN: 28-October dropped and 18-November appended, so the series is the last fifteen published official cash sessions, 29-October to 18-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall per-metal table and English/German overviews. "
                  "Copper structure for context: a $23.50 contango on 18-November (from a $14.50 backwardation); stock 327,400 t (-200 t).")
s=d['inputs_summary']
d['inputs_summary']=("UPDATE 20-NOVEMBER: Copper rolled one session to the Wednesday 18-November LME official cash of $12,750.00 (window 29-October to 18-November). No new carbon, fluoride, silicon or magnesium mark was located this run, so those series are unchanged (gaps stay gaps). Energy: Brent about $92.4-92.6, on track for a third weekly drop; European gas about EUR 86/MWh with EU storage at 70.15% (Trading Economics, 20-November). AL Circle (19-November) cites LME alumina near $400/t as keeping smelter costs elevated. "+s)

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
ptl=0.5*pc; presid=2403-ptl; pshare=ptl/2403*100
NC0="COMPILED THURSDAY 19-NOVEMBER-2026 BEFORE THE RING (LME BOARD CARRIED ON THE TUESDAY 17-NOVEMBER OFFICIAL - THE WEDNESDAY 18-NOVEMBER OFFICIAL HAD NOT BEEN PUBLISHED ON WESTMETALL AT RUN TIME)."
NC1="COMPILED FRIDAY 20-NOVEMBER-2026 BEFORE THE RING (LME BOARD ROLLED TO THE WEDNESDAY 18-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; THE 19-NOVEMBER OFFICIAL WAS NOT YET ON WESTMETALL AT RUN TIME)."
OT="the tariff leg of the US duty-paid premium is 0.50 times the 17-November official cash of $3,060.50, or $1,530.25, DOWN $135.75 against the 16-November figure used previously (the cash squeeze unwound). Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of $872.75, so 63.7%"
NT=f"the tariff leg of the US duty-paid premium is 0.50 times the 18-November official cash of $3,095.00, or ${tl:,.2f}, UP ${tl-ptl:,.2f} against the 17-November figure used previously. Against a US Midwest duty-paid premium of $2,403/t that leaves a residual market leg of ${resid:,.2f}, so {share:.1f}%"
OCV="the tariff leg is 0.50 times the 17-November official cash of $3,060.50, or $1,530.25, leaving a $872.75 residual market leg out of the $2,403/t US duty-paid premium (63.7% policy arithmetic)"
NCV=f"the tariff leg is 0.50 times the 18-November official cash of $3,095.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}% policy arithmetic)"
OR="THE RATIO: LME Alumina at $398.24/t against the 17-November aluminium three-month of $2,940.00 is 13.55%"
ra=398.24/m3*100
NR=f"THE RATIO: LME Alumina at $398.24/t against the 18-November aluminium three-month of $2,865.00 is {ra:.2f}%"
cnt={'nc':0,'t':0,'r':0,'cv':0,'rv':0}
def f(s):
    if NC0 in s: cnt['nc']+=s.count(NC0); s=s.replace(NC0,NC1)
    if OT in s: cnt['t']+=1; s=s.replace(OT,NT)
    if OR in s: cnt['r']+=1; s=s.replace(OR,NR)
    if OCV in s: cnt['cv']+=1; s=s.replace(OCV,NCV)
    if "REVIEWED 19-NOVEMBER" in s and not s.startswith("REVIEWED 19-NOVEMBER: weights") and not s.startswith("REVIEWED 19-NOVEMBER - "):
        cnt['rv']+=1; s=s.replace("REVIEWED 19-NOVEMBER: no newer public disclosure","REVIEWED 20-NOVEMBER: no newer public disclosure").replace("REVIEWED 19-NOVEMBER. NO NEW DATED","REVIEWED 20-NOVEMBER. NO NEW DATED")
    return s
for k in ('premiums','alumina','producer_status','inputs','logistics','raw_materials','caveats'):
    d[k]=walk(d[k],f)
print(cnt)
assert cnt['nc']==10 and cnt['t']==6 and cnt['r']==4 and cnt['cv']==1, cnt
for k in ('premiums','alumina'): assert "17-November official cash of $3,060.50" not in json.dumps(d[k],ensure_ascii=False), k

d['lme_commentary']=("FORWARD SLIDES THROUGH 2,894 WHILE THE PROMPT TIGHTENS. The Wednesday 18-November official lifted cash $34.50 (+1.13%) to $3,095.00 but cut three-month $75.00 (-2.55%) to $2,865.00, so the backwardation widened to $230.00 from $120.50 - spread and flat price moved in OPPOSITE directions. Three-month settled $29.00 below the 2,894 weekly 61.8% retracement, the lowest official in this series. Visible stock ROSE 5,800 t to 226,150 t, the first build after twenty straight draws. "
 "The sell-off was broad: Reuters (via Business Recorder) had copper down 3.5% to a seven-month low and tin down 7.1% on Wednesday, after October FOMC minutes showed nearly all policymakers backing further hikes. Trading Economics cites forecasts of a swing to an 830 kt surplus in 2027, while Emkay Global (via AL Circle, 19-November) still sees a ~400 kt deficit in 2027 and 2028 - the forecasts disagree. Scenario weights move to 10/35/55 on the pre-registered settled close below 2,894. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} below its October mean.")
d['net_read']=("NET: BEARISH ON THE FORWARD, TIGHT ON THE PROMPT. Against: three-month at $2,865.00 settled below the 2,894 weekly 61.8%; hawkish FOMC minutes with a December hike priced and 50bp discussed; dollar near 103.9; forecasts of a 2027 surplus as Chinese output tops 46 Mt and Gulf metal returns; the first LME stock build in twenty-one sessions. "
 "Supportive: a $230.00 backwardation (twenty-fifth straight), visible stock still near series lows at 226,150 t, Hormuz still effectively closed, and Emkay Global's view of a ~400 kt deficit through 2028.")
d['bottom_line']=("BOTTOM LINE: the Wednesday 18-November official split the curve - cash rose $34.50 to $3,095.00 while three-month fell $75.00 to $2,865.00, below the 2,894 weekly 61.8% - widening the backwardation to $230.00, while visible stock rose 5,800 t to 226,150 t, the first build in twenty-one sessions. "
 "Weights move to 10% bull / 35% base / 55% bear on the pre-registered break below 2,894. The re-counted wave (v) has now overshot its 2,894-2,906 target; next is the 2,830-2,850 extended-(v) zone. A settled close back above 2,994.50 is the first sign the break failed, above 3,097.50 negates the re-count; daily Elliott invalidation 3,289. The 19-November official was not yet published at run time; next print Friday 20-November 13:20 London, then the weekly close.")
c2=d['commercial']
a0=c2.find("FIRST, PROMPT PREMIUM UNWINDS AS THE FORWARD BREAKS LOWER:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, THE CURVE STEEPENS - PROMPT TIGHT, FORWARD WEAK: the backwardation widened to $230.00 on 18-November from $120.50 as cash rose $34.50 to $3,095.00 while three-month fell $75.00 to $2,865.00, below the 2,894 weekly 61.8%; nearby metal commands a growing premium over forward metal, so there is still no carry reward for holding stock - and visible LME stock rose 5,800 t, the first build in twenty-one sessions, as metal is delivered into the spread. "+c2[a1:]
o="is $1,530.25 on 17-November cash, 63.7% of the $2,403/t premium"; assert o in c2; c2=c2.replace(o,f"is ${tl:,.2f} on 18-November cash, {share:.1f}% of the $2,403/t premium")
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find("; the dollar index near 103.6",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 18-November official took three-month to $2,865.00, below the 2,894 weekly 61.8%, with 2,830-2,850 the next Elliott zone, while cash rose to $3,095.00; hawkish FOMC minutes (Trading Economics 19-November); India's DGTR anti-dumping probe into aluminium extrusions from China, Malaysia, Vietnam and Thailand (AL Circle 19-November)"+c2[b1:]
d['commercial']=c2

NEWP={'Bull':'10%','Base':'35%','Bear':'55%'}
for s in d['outlook']['scenarios']:
    assert s['prob']=={'Bull':'10%','Base':'40%','Bear':'50%'}[s['case']]
    s['prob']=NEWP[s['case']]
    s['drivers']=("SHIFTED 20-NOVEMBER TO 10/35/55: the 18-November official settled three-month at $2,865.00, BELOW 2,894 - the pre-registered level that adds bear weight - so five points move from base to bear. A settled close back above 2,994.50 would return them. ")+s['drivers']
    if s['case']=='Bear': s['target']='$2,750-2,950'
    if s['case']=='Base': s['target']='$2,900-3,200'
d['outlook']['scenario_paths']={'labels':['Now','Nov-26','Dec-26','Mar-27','Jun-27'],'bull':[m3,3050,3300,3500,3650],'base':[m3,2900,2980,3080,3150],'bear':[m3,2830,2800,2780,2760]}

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 20-NOVEMBER: the 18-November official printed a $230.00 BACKWARDATION, up from $120.50 - a fourteenth session above $15.00, with cash rising as three-month fell. Contango risk remains remote near term. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 20-NOVEMBER: LME stock ROSE 5,800 t on 18-November to 226,150 t - the first build after twenty straight draws, consistent with metal being delivered into the backwardation; 220,350 t (17-November) is the series low. One build does not reverse the trend; trend cut from UP to FLAT pending further sessions."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 20-NOVEMBER: three-month at $2,865.00 is nearer the energy-cost floor; Brent about $92.4-92.6 (third weekly drop) and TTF about EUR 86/MWh (Trading Economics). AL Circle cites LME alumina near $400/t raising smelter costs, and Emkay Global's bear case uses $2,600/t. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 20-NOVEMBER: Straits Daily Brief - still effectively closed; latest transit count 2 on 15-November; 45 AIS-visible vessels holding. Iran claims intensified tanker attacks and mine strikes (conflicting IRGC/navy accounts) - NOT confirmed by UKMTO or any maritime authority; the TARA GAS fire is reported extinguished (Maritime Executive); the ADNOC L&S vessel attack left one missing and 11 injured (Shipping Telegraph). The US Energy Secretary is reported saying Hormuz oil flows hit record levels (Trading Economics) - the sources conflict. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 20-NOVEMBER: markets price a 25bp December hike, another in January and at least one more by end-2027; about 10% odds of 50bp in December; dollar index about 103.90 (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('TARIFF POLICY'):
        r['risk']+=" UPDATE 20-NOVEMBER: India's DGTR opened an anti-dumping investigation into aluminium extrusions from China, Malaysia, Vietnam and Thailand (about 90% of India's imports of the product; AL Circle 19-November); still no official US-Canada deal on the 50% Section 232 rate. Trend unchanged."; hit+=1
assert hit==6,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Thu 19-Nov':
        hc+=1; cat['date']='Daily, from Fri 20-Nov'
        cat['event']=("WEDNESDAY 18-NOVEMBER OFFICIAL: three-month $2,865.00 (-$75.00), BELOW the 2,894 weekly 61.8%; cash $3,095.00 (+$34.50); backwardation $230.00 from $120.50; stock +5,800 t (first build in twenty-one sessions); weights moved to 10/35/55. NEXT: the 19- and 20-November officials (13:20 London) against the 2,830-2,850 extended-(v) zone; Friday's weekly close vs 2,894 (a weekly close below opens the 78.6% near 2,633); a settled close back above 2,994.50 would signal a failed break; above 3,097.50 negates the re-count; invalidation 3,289. The December Fed meeting; any official US-Canada tariff announcement; first Q1-2027 Japanese premium offers (none located yet).")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"FRIDAY 20-NOVEMBER ON THE WEDNESDAY 18-NOVEMBER OFFICIAL: the curve split - cash rose $34.50 to $3,095.00 while three-month fell $75.00 to $2,865.00, below the 2,894 weekly 61.8%, widening the backwardation to $230.00. Visible stock rose 5,800 t to 226,150 t, the first build in twenty-one sessions, as metal is drawn onto the exchange by the spread. The sell-off was macro-led: hawkish FOMC minutes, copper at a seven-month low and tin -7.1% (Reuters via Business Recorder). Forecasts diverge - Trading Economics cites an 830 kt 2027 surplus; Emkay Global (via AL Circle) a ~400 kt deficit through 2028. Weights move to 10/35/55 on the pre-registered break below 2,894.")

st=d['ew']['short_term']; nx=st['now_x']
st['ymin']=2700; st['yticks']=[2700,2900,3100,3300,3500,3700]
st['proj']={"bull":[[nx,m3],[0.99997,2950],[1.0,3050]],"base":[[nx,m3],[0.99997,2840],[1.0,2920]],"bear":[[nx,m3],[0.99997,2820],[1.0,2760]]}
assert st['fwd_pivots'][0]['p']==2894.0
st['fwd_pivots'][0]={"t":0.99996,"p":2840.0,"w":"UPDATED 20-NOVEMBER: three-month settled 2,865.00 on 18-November, through the 2,894-2,906 base target (wave (v) = wave (i) at 2,906.5; weekly 61.8% at 2,894). Count unchanged: (i) 3,374-3,183, (ii) 3,289, (iii) to 2,994.50 (longest), (iv) 3,097.50, (v) under way and now EXTENDING. Next objective the 2,830-2,850 zone (0.618 of (i)-(iii) projected from 3,097.50). The wave (v) low is NOT confirmed until a reversal settles; a settled close above 3,097.50 negates this count."}
lt=d['ew']['long_term']
lt['proj']={"bull":lt['proj']['bull'],"base":[[lt['now_x'],m3],[0.78,2830],[0.9,2950],[1.0,3080]],"bear":[[lt['now_x'],m3],[0.8,2700],[1.0,2633]]}
EWP=("REVIEWED 20-NOVEMBER ON THE 18-NOVEMBER OFFICIAL - TARGET ZONE OVERSHOT, COUNT HELD: three-month settled 2,865.00 (-75.00), below the 2,894-2,906 zone. No cardinal rule is broken: wave (v) from 3,097.50 now measures $232.50, shorter than the $294.50 wave (iii), so (iii) remains the longest; wave (iv) at 3,097.50 stays clear of the 3,183 wave (i) low. The 2,865 settlement is not added as a pivot because no reversal has confirmed it. BASE CASE (about 55%): wave (v) extends into 2,830-2,850 and completes the C wave from 3,374, followed by a corrective rebound toward 2,994.50-3,097.50. ALTERNATE (about 45%): a deeper extension (v = 1.0 x (i)-(iii) near 2,620-2,700 is the outer limit while (v) stays shorter than (iii), i.e. above about 2,803) - a settled close below about 2,803 would make (v) longer than (iii) and force a re-label (e.g. a larger extended (v) or a new degree). INVALIDATION of the count: a settled close above 3,097.50; of the bearish C-wave count, 3,289. Confidence low. ")
EWL=("REVIEWED 20-NOVEMBER (FRIDAY, DAILY CLOSE BELOW 2,894): the 18-November official at 2,865.00 settled below the 2,894 weekly 61.8% retracement. The weekly base case - the correction toward 2,894 - is effectively met; whether it holds is decided by Friday's WEEKLY close. A weekly close below 2,894 raises the alternate toward the 78.6% retracement near 2,633 to about 35%; a weekly close back above 2,994.50 would favour a completed correction. Loses preference only on a weekly close above 3,110. Confidence moderate. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 19-NOVEMBER'),k
    d['ew'][k]['writeup']=pfx+w
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="92.4",day="about $92.38-92.60 on 20-November (+0.4-0.7%, Trading Economics; sections differ); on track for a third straight weekly drop; Straits Daily Brief $92.38",
 note="REFRESHED FRIDAY 20-NOVEMBER-2026 (Trading Economics): the US Energy Secretary said oil flows through the Strait of Hormuz reached record levels as Middle Eastern supply recovers (contrasting with transit-count trackers - see Hormuz risk); the US, China and Russia agreed to raise refined-product supply; the IEA projects a ~2 mb/d surplus this quarter. Reports of possible renewed US strikes on Iran lend some support. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="85.9",day="about EUR 85.9-86.2/MWh on 20-November (+1.7-2.1%, Trading Economics; sections differ)",
 note="REFRESHED FRIDAY 20-NOVEMBER-2026 (Trading Economics): EU gas inventories at 70.15%, about 11.75 points below 81.9% a year earlier and against a five-year seasonal average of 89%. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="103.90",day="about 103.90 on 20-November (-0.02%, Trading Economics); about +2.1% over the month",
 note="REFRESHED FRIDAY 20-NOVEMBER-2026 (Trading Economics): after minutes showing nearly all Fed officials expect further hikes, traders price a 25bp December hike, another in January and at least one more before end-2027; CME FedWatch about 10% odds of 50bp in December. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.09630',day="LME fixing on 18-November, down from 1.09930 on 17-November",note="REFRESHED FRIDAY 20-NOVEMBER-2026 to the 18-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE WEDNESDAY 18-NOVEMBER-2026 LME OFFICIAL, the latest published session at run time. THIS FRIDAY 20-NOVEMBER RUN IS COMPILED AT ABOUT 02:35 LONDON, BEFORE TODAY'S RING. The board rolled ONE session this run (from Tuesday 17-November, which the 19-November run had carried). The THURSDAY 19-NOVEMBER official had NOT yet been published on Westmetall at run time, so the board is one session behind the calendar; nothing was estimated. The Trading Economics aluminium reference (about $2,868.35, +1.18% for 19-November) is a CFD reference cited in text only and is NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (20-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 18-November session (aluminium cash 3,095.00, three-month 2,865.00, stock 226,150; EUR/USD MTLE 1.09630); the aluminium, copper, nickel, zinc and lead per-metal daily tables all show 18-November as their newest row. The three-month settlement of 2,865.00 is consistent with Reuters' intraday report of about $2,869 at 11:00 GMT on 18-November (Business Recorder).")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 22-October to 17-November rows match the stored series; the copper and lead fifteen-session windows (29-October to 18-November) were asserted equal to the re-fetched per-metal tables; each metal's 18-November stock change reconciles with its 17-November stock.")
C[3]=("STOCK CHANGES 18-November: aluminium +5,800 to 226,150 (first build after twenty straight draws); copper -200 to 327,400; nickel -24 to 274,116; zinc -1,600 to 146,775; lead -1,800 to 269,000.")
c4=C[4]; k=c4.find("The price chart ax"); assert k>0
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (18-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (thirteen sessions, 02-18 November) as their latest point. "
 "The price chart axis (floor 2,700, ceiling 3,450) brackets cash 3,095.00 and three-month 2,865.00 after the price-axis floor was LOWERED THIS RUN from 2,800 to 2,700 (three-month was only $65 above the old floor); the stock chart axis floor of 190,000 t leaves 36,150 t headroom below visible stock of 226,150 t; it is re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,095.00 against three-month $2,865.00 is therefore a $230.00 BACKWARDATION, up from $120.50 on 17-November. On Wednesday spread and flat price moved in OPPOSITE directions (cash up, three-month down). Press figures for the spread differ by measure and time; the dashboard uses the settled officials only."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $92.4-92.6), the dollar index (about 103.90) and TTF (about EUR 85.9-86.2/MWh) are Trading Economics readings for 20-November (early, pre-European session); Trading Economics prices are contract-for-difference references, not official benchmarks, and its Brent and TTF pages again showed two levels in different sections, so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (20-November) shows Brent $92.38 (AI-assisted); it cites NO UKMTO confirmation for any incident this edition - all incident items are media reports or Iranian claims."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 20-NOVEMBER (FRIDAY, PRE-RING): no authorised fetch was blocked. Westmetall EN and DE overviews and all five per-metal tables, Trading Economics aluminium/Brent/TTF/dollar, AL Circle news and the Straits Daily Brief were fetched; the 18-November official was published, the 19-November official not yet. Searches for Q1-2027 Japanese premium offers (none located; S&P Global reports participants expect pressure into Q1) and for a Reuters 19-November metals report (none located) were run. An official US-Canada aluminium tariff deal was again not located, so it stays pending."); hit+=1
assert hit==2,hit

d['so_what']={"line":"LME aluminium's curve split on Wednesday: three-month fell $75 to $2,865 - below the $2,894 support and its lowest settlement in this series - while cash rose to $3,095, widening the backwardation to $230; LME stock rose for the first time in twenty-one sessions.",
 "points":[
 "WHAT MOVED: the 18-November official cut three-month 2.55% to $2,865.00 but lifted cash 1.13% to $3,095.00, so the backwardation (cash above three-month) widened to $230.00 from $120.50; visible LME stock rose 5,800 t to 226,150 t, ending twenty straight draws.",
 "WHY: a broad macro sell-off after hawkish Fed minutes (a December hike priced, 50bp discussed) - copper hit a seven-month low and tin fell 7%. The forward is pricing a looser 2027 (forecasts cited by Trading Economics see an 830 kt surplus), while prompt metal stays scarce; Emkay Global still sees a ~400 kt deficit through 2028.",
 "SUPPLY AND TRADE: Hormuz remains effectively closed with 45 vessels holding (new attack claims unconfirmed); India opened an anti-dumping probe into aluminium extrusions from China, Malaysia, Vietnam and Thailand.",
 "WHAT TO WATCH: today's weekly close against $2,894 (a close below opens the next leg lower); the $2,830-2,850 zone; whether the stock build continues as metal is delivered into the backwardation."]}

d['feed']=([
 {"when":"Wed 18-Nov","impact":"Bearish","text":"18-NOVEMBER OFFICIAL: three-month $2,865.00 (-$75.00), below the 2,894 weekly 61.8%; cash $3,095.00 (+$34.50); backwardation widens to $230.00; stock +5,800 t to 226,150 t, first build in 21 sessions."},
 {"when":"Thu 19-Nov","impact":"Mixed","text":"INDIA: DGTR opens anti-dumping probe into aluminium extrusions from China, Malaysia, Vietnam and Thailand (AL Circle)."},
 {"when":"Thu 19-Nov","impact":"Bullish","text":"OUTLOOK: Emkay Global sees an aluminium supply crunch to 2028, ~400 kt deficit in 2027 and 2028 (AL Circle)."},
 {"when":"Fri 20-Nov","impact":"Mixed","text":"HORMUZ: effectively closed, 45 vessels holding; Iranian claims of new tanker/mine strikes unconfirmed; TARA GAS fire extinguished (Straits brief)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM THREE-MONTH BREAKS 2,894 AS THE CURVE STEEPENS. The Wednesday 18-November official cut three-month $75.00 (-2.55%) to $2,865.00, the lowest in this series, while cash rose $34.50 to $3,095.00, widening the backwardation to $230.00; visible stock rose 5,800 t to 226,150 t, the first build after twenty straight draws. Board three-month moves: copper -3.31%, aluminium -2.55%, zinc -1.67%, lead -0.53%, nickel -0.03%; copper flipped to a $23.50 contango."},
 {"theme":"Outlook","horizon":"Structural","impact":"Bullish","url":S_EM,
  "headline":"EMKAY: SUPPLY CRUNCH TO PERSIST TILL 2028 (AL Circle, 19-November): Emkay Global expects a global deficit of about 400 kt in both 2027 and 2028; LME stocks down 57% year to date to about 220 kt; LME alumina near $400/t lifting costs; even its bear case ($2,600/t, 1.5% demand growth, two Fed hikes by March 2027) shows only a marginal surplus. EGA restoring ~585 kt by Q1-2027; Alba and Qatalum (~567 kt) restarts less certain. Contrasts with the 830 kt 2027 surplus forecast cited by Trading Economics."},
 {"theme":"Trade policy","horizon":"0-6 months","impact":"Mixed","url":S_IN,
  "headline":"INDIA OPENS ANTI-DUMPING PROBE ON ALUMINIUM EXTRUSIONS (AL Circle, 19-November): the DGTR initiated an investigation into extrusions from China, Malaysia, Vietnam and Thailand - about 90% of India's imports of the product - on a petition by nine domestic manufacturers; preliminary evidence reportedly shows dumping above de minimis. No duty rates or timelines stated."},
 {"theme":"Policy","horizon":"Structural","impact":"Mixed","url":S_CB,
  "headline":"EU CBAM EXPANSION EYES MORE ALUMINIUM PRODUCTS (AL Circle, 19-November): EU industrial emissions fell 3.3% as the bloc considers widening the carbon border mechanism to more downstream aluminium products."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Mixed","url":S_ST,
  "headline":"HORMUZ STILL EFFECTIVELY CLOSED (Straits Daily Brief, 20-November): latest IMF PortWatch count 2 transits on 15-November vs 85/day pre-crisis; 45 AIS-visible vessels holding. Iran claims intensified tanker attacks and mine strikes on supertankers (conflicting IRGC and navy accounts) - not confirmed by UKMTO; the TARA GAS fire is reported extinguished; the ADNOC L&S attack left one missing and 11 injured (Shipping Telegraph). Separately, the US Energy Secretary is reported saying Hormuz oil flows hit records (Trading Economics) - accounts conflict."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"FED HIKES PRICED (Trading Economics, 20-November): after minutes showing nearly all officials expect further increases, markets price a 25bp December hike, another in January and at least one more by end-2027; ~10% odds of 50bp in December; dollar index about 103.90. Brent about $92.4-92.6, heading for a third weekly drop."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])

for p in d['producer_status']:
    p['asof']=RD

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 18-Nov-2026 session (EN and DE overviews agree; Al/Cu/Ni/Zn/Pb per-metal tables newest row 18-Nov; 19-Nov not yet published at run time)",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_EM,S_EM],[L_IN,S_IN],[L_CB,S_CB],[L_DB,S_DB]): d['sources'].append(x)
for x in ([L_EM,S_EM],[L_IN,S_IN],[L_TD,S_TD],[L_ST,S_ST]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-17',3060.5,2940.0,220350]
ph['rows'][-1]=['2026-11-18',cash,m3,stk]; ph['updated']=RD   # same week (w/c 16-Nov): replace the week's row
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],round(ra,2),d['metals_board'])
# --- FIXUP (same run): EW short-term base/alternate wording corrected (wave (v) longer than (iii) is NOT a rule break since (iii)>(i));
# applied inline via a follow-up read-modify-write: base = 0.618 x (i)-(iii) from 3,097.50 ~2,863 (met), alternate 1.618 x (i) ~2,788.
