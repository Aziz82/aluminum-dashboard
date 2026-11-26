# Daily data refresh - 2026-11-26 (THURSDAY, ~02:40 UTC, BEFORE the Thursday ring). Board ROLLED ONE SESSION to the WEDNESDAY 25-Nov LME official.
# Cache-busted EN + DE overviews agree on 25-Nov (Al cash 2,849.00 / 3M 2,760.00 / stock 219,200; MTLE 1.09430); Al per-metal table newest row 25-Nov.
# All five metals' stock changes reconcile with 24-Nov. Cash collapsed (-271.50) and 3M fell (-29.00): same direction; backwardation narrowed to $89.00
# on the day the LME cut its aluminium Tom-Next lending threshold from 50% to 30% (effective 25-Nov). No new EW trigger: 3M 2,760 inside the 2,700-2,790 extended-(v) zone.
import json, subprocess
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-26'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_LME="https://fxnewsgroup.com/forex-news/exchanges/lme-recalibrates-lending-rules-for-lme-aluminium-contract/"; L_LME="FX News Group - LME Special Committee cuts the lowest LME Aluminium Tom-Next lending threshold from 50% to 30%, effective 25-Nov-2026; holders of 30-80% of on-warrant stock lend at 0.50% of the previous day's cash price"
S_INV="https://www.investing.com/news/commodities-news/lme-lowers-aluminum-lending-trigger-to-curb-nearby-squeeze-93CH-5048658"; L_INV="Investing.com - LME lowers aluminum lending trigger to curb nearby squeeze (24-Nov-2026): guidance now applies above 30% of available stocks; cash-3M spread above $400/t on 23-Nov"
S_ST="https://straits.live/briefs/2026-11-26"; L_ST="Straits Daily Brief - Strait of Hormuz, 26-Nov-2026 (effectively closed; 1 transit on 22-Nov per IMF PortWatch; IRGC mine claims unconfirmed; Brent settled $94.69)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$94.7 on 26-Nov-2026 after two days of gains on Middle East attacks; OPEC+ meets 29-Nov"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.74 (26-Nov-2026); core PCE +0.3% m/m, 3.3% y/y; Q3 GDP revised 4.3%; 25bp December hike priced, ~60% for January"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,800.75 (+0.92%) on 25-Nov-2026 after touching $2,745, lowest since October 2025 (CFD reference); LME lending-threshold cut; Hua Chin (Indonesia) delivery approval reported"
S_SMM="https://www.metal.com/en/newscontent/3X7LZUZJ4FNPZKZJVPUKS3VHL6ZNIRA3X3235TA-november-26-2026-smm-daily-inventory-data-of-aluminum-ingots-in-three-regions-smm-data"; L_SMM="SMM - China three-region aluminium ingot social inventory 295,500 t on 26-Nov-2026 (-4,000 t)"
S_301="https://www.metal.com/en/newscontent/IV2G6ETZRZSWXFHFB5S4ODBKSZCWIWSEC5YREFY-us-proposes-section-301-tariffs-on-india-13-other-economies-india-rate-capped-at-17-with-deal"; L_301="SMM - US proposes Section 301 tariffs on India and 13 other economies; aluminium among proposed sectors (not final), 26-Nov-2026"
S_SPJ="https://www.spglobal.com/energy/en/news-research/latest-news/metals/101326-japanese-q4-aluminum-premium-falls-35-to-255mt-cif-japan"; L_SPJ="S&P Global - Japanese Q4 aluminum premium falls 35% to $255/mt CIF Japan; participants expect pressure into Q1-2027"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3120.5 and B['LME 3-month']['cur']==2789.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3120.5,2789.0,220350
cash,m3,stk=2849.0,2760.0,219200
spr=cash-m3; psp=pc-pm; assert spr==89.0 and psp==331.5 and ps-1150==stk
ytd=(m3/3010.5-1)*100; dc=cash-pc; dm=m3-pm
assert dc==-271.5 and dm==-29.0

VER=("COMPILED THURSDAY 26-NOVEMBER-2026 ABOUT 02:40 LONDON - BEFORE TODAY'S LME RING (13:20 LONDON). THE BOARD IS THE WEDNESDAY 25-NOVEMBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION; it ROLLED ONE SESSION this run (the previous run carried Tuesday 24-November). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 25-November official for all metals with stocks and FX (EUR/USD MTLE 1.09430; 24-November 1.09600); (2) the aluminium per-metal daily table shows 25-November as its newest row and its 18- to 24-November rows match the stored series; (3) every metal's 25-November stock change reconciles exactly with the stored 24-November stock. "
 "The whole board sits on ONE UNIFORM SESSION (25-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" WEDNESDAY 25-NOVEMBER (the board): CASH SETTLED $2,849.00, DOWN $271.50 OR 8.70% FROM TUESDAY'S $3,120.50 - the largest one-session cash fall in this dashboard's record - on the day the LME's cut in the aluminium Tom-Next lending threshold (50% to 30% of on-warrant stock) took effect. THREE-MONTH SETTLED $2,760.00, DOWN $29.00 OR 1.04% FROM $2,789.00 - inside the 2,700-2,790 extended wave (v) zone, a new low for three-month officials in this dashboard's 2026 record, and $250.50 BELOW the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION COLLAPSED TO $89.00 (24-November $331.50; 23-November series high $367.50) - still a thirtieth straight backwardation and the nineteenth above $15.00. Cash and three-month fell in the SAME direction, cash nine times faster, so the squeeze premium deflated. "
 "VISIBLE LME STOCK FELL 1,150 t TO 219,200 t - a fifth straight draw and a NEW SERIES LOW, below the 220,350 t prior low. The Trading Economics aluminium reference shows about $2,800.75 (+0.92%) for 25-November after an intraday low near $2,745 (lowest since October 2025) - a CFD reference cited in text only.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"2,849.0","pos":False,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"2,760.0","pos":False,"delta":VER+AL+" ELLIOTT: the extended wave (v) from 3,097.50 now measures $337.50; three-month settled inside the 2,700-2,790 objective zone (2,750 next). No rule break and no new trigger; the wave (v) low is NOT confirmed until a reversal settles. A settled close back above 2,994.50 would signal a completed C wave; above 3,097.50 negates the wave (v) count; daily invalidation of the bearish count remains 3,289."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+89.0","pos":True,"delta":VER+f" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $2,849.00 against three-month $2,760.00 is an $89.00 BACKWARDATION, DOWN $242.50 from $331.50 on 24-November (series high $367.50 on 23-November). On 25-November cash (-$271.50) and three-month (-$29.00) both fell (same direction), cash far faster. The collapse coincides with the LME Special Committee's cut of the lowest aluminium Tom-Next lending threshold from 50% to 30%, effective 25-November (holders of 30-80% of on-warrant stock must lend at 0.50% of the previous day's cash price, per the LME notice as reported by FX News Group). It stays above the published $15.00 reversal condition for a nineteenth session and is a thirtieth straight backwardation; a contango beyond $24.50 would reverse the structural signal. The October mean spread was ${oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"219,200","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 1,150 t TO 219,200 t ON 25-NOVEMBER, a fifth straight draw (24-November -1,050 t; 23-November -2,125 t) and a NEW SERIES LOW below the 220,350 t of 17- and 24-November. The LME notes limited stock ingress reflects physical tightness, with new production expected through 2027. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 24-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $2,760.00, DOWN $29.00 FROM THE 24-NOVEMBER $2,789.00 - inside the 2,700-2,790 extended-(v) zone, $134.00 BELOW the 2,894 weekly 61.8%; $250.50 BELOW the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 1,150 t TO 219,200 t on 25-November - a fifth straight draw and a NEW SERIES LOW. AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" AN $89.00 BACKWARDATION, DOWN $242.50 FROM $331.50 ON 24-NOVEMBER (series high $367.50 on 23-November), as the LME's lower lending threshold took effect. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On 25-November cash (-$271.50) and three-month (-$29.00) moved in the SAME direction. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00, $353.00, $367.50, $331.50 and $89.00."},
 {"name":"EUR/USD LME fixing","cur":1.0943,"prev":1.096,"avg":1.1465,"note":VER+" THE LME EURO FIXING WAS 1.09430 ON 25-NOVEMBER, DOWN FROM 1.09600 ON 24-NOVEMBER, with the dollar index near 103.7 (Trading Economics, 26-November). AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (25-Nov official)","price":"2,849.0","basis":"THE WEDNESDAY 25-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $2,849.00, DOWN $271.50 OR 8.70% (24-November $3,120.50) as the LME's lower lending threshold took effect. Next print Thursday 26-November 13:20 London."},
 {"tenor":"3-month (25-Nov official)","price":"2,760.0","basis":"THE 25-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $2,760.00, DOWN $29.00 - inside the 2,700-2,790 extended wave (v) zone."},
 {"tenor":"Cash-to-3M structure","price":"+89.0 (BACKWARDATION)","basis":"An $89.00 BACKWARDATION, down from $331.50; cash and three-month both fell, cash far faster - the squeeze premium deflated."},
 {"tenor":"Visible LME stock","price":"219,200 t","basis":f"DOWN 1,150 t on 25-November, a fifth straight draw and a new series low; October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("THE SQUEEZE PREMIUM DEFLATES; THE FORWARD STAYS WEAK. On the 25-November official cash $2,849.00 sits $89.00 ABOVE three-month $2,760.00, a BACKWARDATION down from $331.50 (24-November) and the $367.50 series high (23-November). Cash fell $271.50 and three-month $29.00 (same direction), on the day the LME cut its aluminium Tom-Next lending threshold from 50% to 30% of on-warrant stock (lending at 0.50% of the previous day's cash price for 30-80% holders). "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00, $353.00, $367.50, $331.50 and now $89.00. "
 f"READ: the exchange's rule change released the concentrated prompt position rather than any new metal arriving - visible stock fell again to a 219,200 t series low - so the remaining backwardation still says nearby metal is scarce, while the forward prices a looser 2027 (Trading Economics cites an 830 kt 2027 surplus and reported LME delivery approval for Indonesia's Hua Chin smelter). The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2600,3450] and d['chart_stock_axis']==[190000,255000]

ls=d['lme_series']; assert ls[-1][0]=='24-Nov' and len(ls)==15
d['lme_series']=ls[1:]+[["25-Nov",cash,m3,stk]]
assert [tuple(r[1:]) for r in d['lme_series'][-6:]]==[(3095.0,2865.0,226150),(3105.0,2845.0,224425),(3184.5,2831.5,223525),(3201.5,2834.0,221400),(3120.5,2789.0,220350),(cash,m3,stk)]
CU=(11703.0,11758.0,336750); NI=(15035.0,15210.0,275604); ZN=(3520.5,3394.0,143450); PB=(1792.0,1827.0,256675)
CU0=(12035.0,12055.0,337825); NI0=(15060.0,15295.0,275604); ZN0=(3665.0,3508.0,143425); PB0=(1786.0,1828.0,256950)
assert CU0[2]-1075==CU[2] and NI0[2]==NI[2] and ZN0[2]+25==ZN[2] and PB0[2]-275==PB[2]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU0[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI0[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN0[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB0[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU0[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI0[1],1)
ms=d['metals_series']; R=ms['rows']; assert ms['asof']=='2026-11-24'
# November MTD: 02..24 Nov = 17 sessions = 02-Nov + 03-Nov (from prior engine states) + current 04..24 window; add 25-Nov -> 18
o23=json.loads(subprocess.check_output(['git','show','d5d523d:market_data.json']))
o24=json.loads(subprocess.check_output(['git','show','9ac8798:market_data.json']))
z02=o23['metals_series']['rows']['ZN'][0]; p02=o23['metals_series']['rows']['PB'][0]; assert (z02,p02)==(3935.0,1869.5)
z03=o24['metals_series']['rows']['ZN'][0]; p03=o24['metals_series']['rows']['PB'][0]
assert o24['metals_series']['rows']['ZN'][1:]==R['ZN'][:-1] and o24['metals_series']['rows']['PB'][1:]==R['PB'][:-1]
zs=z02+z03+sum(R['ZN']); psum=p02+p03+sum(R['PB'])
mh['zn'][-1]=round(mh['zn'][-1]*((zs+ZN[0])/18)/(zs/17),1); mh['pb'][-1]=round(mh['pb'][-1]*((psum+PB[0])/18)/(psum/17),1)
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])):
    assert len(R[k])==15; R[k]=R[k][1:]+[v]
ms['asof']='2026-11-25'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending WEDNESDAY 25-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 04-November dropped, 25-November appended, so the window is 05-November to 25-November. Earlier points were asserted against the Westmetall per-metal tables on 21-November; the 23- to 25-November points are the official cash from the English and German overviews (which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (25-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return "unchanged" if a==b else f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,f" COPPER 25-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU0[0])} from 24-November; three-month ${CU[1]:,.2f}, {chg(CU[1],CU0[1])} - a new low for this window; zinc three-month fell more (-3.25%). STRUCTURE: a $55.00 CONTANGO (24-November $20.00). Stock fell 1,075 t to 336,750 t."),
 ("Nickel",NI,f" NICKEL 25-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI0[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI0[1])}. CONTANGO narrowed to $175.00 (24-November $235.00), still the widest carry on the board. Stock unchanged at 275,604 t."),
 ("Zinc",ZN,f" ZINC 25-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN0[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN0[1])}. BACKWARDATION narrowed to $126.50 (24-November $157.00). Stock rose 25 t to 143,450 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,f" LEAD 25-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB0[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB0[1])}. CONTANGO $35.00 (24-November $42.00). Stock fell 275 t to 256,675 t."),
]
oldm={m['name']:m for m in d['metals_detail']}
CROSS=(f" CROSS-METAL 25-NOVEMBER: three-month fell across the board - copper {abs(CU[1]/CU0[1]-1)*100:.2f}%, zinc {abs(ZN[1]/ZN0[1]-1)*100:.2f}%, aluminium {abs(m3/pm-1)*100:.2f}%, nickel {abs(NI[1]/NI0[1]-1)*100:.2f}% and lead {abs(PB[1]/PB0[1]-1)*100:.2f}% - amid a broader risk-asset selloff; prompt spreads narrowed in aluminium and zinc. The dollar index was about 103.7 with a 25bp December Fed hike priced after core PCE rose to 3.3% y/y (Trading Economics). The LME euro fixing was 1.0943.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":oldm[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${oldm[n]['avg']:,.2f}; cash sits ${abs(c[0]-oldm[n]['avg']):,.2f} "+("above" if c[0]>oldm[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='24-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["25-Nov",CU[0]]]; assert i['hist'][0][0]=='05-Nov'
        assert [v for _,v in i['hist']]==R['CU']
        i['val']="~11,758.00 (3M); 11,703.00 (cash) $/t"; i['ratio']="~11,703.00 $/t cash vs LME 3M 11,758.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the WEDNESDAY 25-NOVEMBER-2026 session at $11,703.00 (24-November $12,035.00). 04-November dropped and 25-November appended, so the series is the last fifteen published official cash sessions, 05-November to 25-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English/German overviews. "
                  "Copper structure for context: a $55.00 contango on 25-November; stock 336,750 t (-1,075 t).")
d['inputs_summary']=("UPDATE 26-NOVEMBER: Copper rolled one session to the Wednesday 25-November LME official cash of $11,703.00 (window 05-November to 25-November). No new carbon, fluoride, silicon or magnesium mark was located this run, so those series are unchanged (gaps stay gaps); AL Circle (25-November) reports US aluminium trihydrate prices up 0.89% in October on freight. Energy: Brent about $94.7 on 26-November after two days of gains on renewed Middle East attacks (Trading Economics). "+d['inputs_summary'])

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
NC1="COMPILED WEDNESDAY 25-NOVEMBER-2026 BEFORE THE RING (LME BOARD ROLLED TO THE TUESDAY 24-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION)."
NC2="COMPILED THURSDAY 26-NOVEMBER-2026 BEFORE THE RING (LME BOARD ROLLED TO THE WEDNESDAY 25-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION)."
REPL=[
 ("0.50 times the 24-November official cash of $3,120.50, or $1,560.25, DOWN $40.50 against the 23-November figure used previously",f"0.50 times the 25-November official cash of $2,849.00, or ${tl:,.2f}, DOWN ${1560.25-tl:,.2f} against the 24-November figure used previously"),
 ("residual market leg of $842.75, so 64.9%",f"residual market leg of ${resid:,.2f}, so {share:.1f}%"),
 ("0.50 times the 24-November official cash of $3,120.50, or $1,560.25, leaving a $842.75 residual market leg out of the $2,403/t US duty-paid premium (64.9%",f"0.50 times the 25-November official cash of $2,849.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}%"),
 ("$1,560.25 on 24-November cash, 64.9%",f"${tl:,.2f} on 25-November cash, {share:.1f}%"),
 ("THE RATIO: LME Alumina at $398.24/t against the 24-November aluminium three-month of $2,789.00 is 14.28%",f"THE RATIO: LME Alumina at $398.24/t against the 25-November aluminium three-month of $2,760.00 is {398.24/m3*100:.2f}%"),
 ("REVIEWED 25-NOVEMBER: no newer public disclosure","REVIEWED 26-NOVEMBER: no newer public disclosure"),
 ("REVIEWED 25-NOVEMBER. NO NEW DATED","REVIEWED 26-NOVEMBER. NO NEW DATED"),
 (NC1,NC2)]
cnt={}
def f(s):
    for a,b in REPL:
        if a in s: cnt[a[:25]]=cnt.get(a[:25],0)+s.count(a); s=s.replace(a,b)
    return s
for k in list(d.keys()):
    if k in ('report_date','ew','sources','kpi_cards','benchmark','metals_detail'): continue
    d[k]=walk(d[k],f)
print(cnt)
blob=json.dumps(d,ensure_ascii=False)
assert "$1,560.25" not in blob and "WEDNESDAY 25-NOVEMBER-2026 BEFORE THE RING" not in blob, [blob.count("$1,560.25")]

d['lme_commentary']=("THE EXCHANGE DEFLATES THE SQUEEZE; THE FORWARD KEEPS SLIPPING. On Wednesday 25-November cash fell $271.50 (8.70%) to $2,849.00 and three-month $29.00 to $2,760.00 - inside the 2,700-2,790 extended wave (v) zone and a new 2026 low for three-month officials on this record. The backwardation collapsed to $89.00 from $331.50 on the day the LME's cut in the aluminium Tom-Next lending threshold (50% to 30% of on-warrant stock) took effect - forcing large holders to lend nearby metal. Visible stock still fell 1,150 t to 219,200 t, a fifth straight draw and a new series low. "
 "Trading Economics adds reported LME delivery approval for Indonesia's 480 ktpa Hua Chin smelter and Chinese output on track for a record above 46 Mt, and cites an 830 kt 2027 surplus; Emkay Global (via AL Circle) sees a ~400 kt deficit in 2027 and 2028 - the forecasts disagree. Macro stays a headwind (core PCE 3.3% y/y; December hike priced) while Brent rebounded to about $94.7. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} below its October mean.")
d['net_read']=("NET: BEARISH ON THE FORWARD; THE PROMPT SQUEEZE IS BEING DISMANTLED. Against: three-month at $2,760.00, $134.00 under the 2,894 weekly 61.8%; the LME's lending rule has cut the cash premium by $271.50 in one session; reported LME approval for Indonesian Hua Chin metal; a hawkish Fed (December hike priced, core PCE 3.3%); forecasts of a 2027 surplus. "
 "Supportive: a backwardation still at $89.00 (thirtieth straight), stock at a new 219,200 t series low, Hormuz still effectively closed with fresh attacks on Gulf energy infrastructure lifting Brent, and Emkay Global's view of a ~400 kt deficit through 2028.")
d['bottom_line']=("BOTTOM LINE: the LME's lower lending threshold broke the prompt squeeze in one session - cash $2,849.00 (-$271.50), backwardation $89.00 (from $331.50) - while three-month slipped to $2,760.00 inside the extended wave (v) zone and visible stock drew to a new 219,200 t low. "
 "Scenario weights hold at 10% bull / 30% base / 60% bear (no new trigger). A settled close back above 2,994.50 would mark a completed C wave; above 3,097.50 negates the count; daily invalidation 3,289. Next print Thursday 26-November 13:20 London; Friday's weekly close is tested against 2,750.")
c2=d['commercial']
a0=c2.find("FIRST, THE CURVE STEEPENS AGAIN - PROMPT TIGHT, FORWARD WEAK:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, THE PROMPT PREMIUM DEFLATES - FORWARD STILL WEAK: on 25-November cash fell $271.50 to $2,849.00 and three-month to $2,760.00, leaving an $89.00 backwardation (from $331.50; series high $367.50 on 23-November) as the LME's cut in the aluminium lending threshold to 30% of on-warrant stock took effect; nearby metal still carries a premium over forward metal, so there is still no carry reward for holding stock - and visible LME stock drew for a fifth session to a 219,200 t series low. "+c2[a1:]
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find("; the dollar index near",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 25-November official took three-month to $2,760.00 and cash to $2,849.00 as the LME lending change took effect; core PCE printed 3.3% y/y and a 25bp December Fed hike is priced (Trading Economics 26-November); OPEC+ meets 29-November; first Q1-2027 Japanese premium offers, which typically emerge from late November or early December (none located yet; S&P Global says participants expect pressure into Q1)"+c2[b1:]
d['commercial']=c2

for s in d['outlook']['scenarios']:
    assert s['prob']=={'Bull':'10%','Base':'30%','Bear':'60%'}[s['case']]
    s['drivers']=("HELD 26-NOVEMBER AT 10/30/60: the 25-November official settled three-month at $2,760.00, inside the 2,700-2,790 extended-(v) zone - no new pre-registered trigger. The LME lending-threshold cut collapsed the backwardation to $89.00, which removes some prompt support but does not move the forward count. REVERSAL: a settled close back above 2,994.50 returns five points to base. ")+s['drivers']
d['outlook']['scenario_paths']['bull'][0]=m3; d['outlook']['scenario_paths']['base'][0]=m3; d['outlook']['scenario_paths']['bear'][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 26-NOVEMBER: the 25-November official printed an $89.00 backwardation, down from $331.50, as the LME's lower lending threshold took effect - a nineteenth session above $15.00 but the cushion against contango has shrunk sharply. Trend raised from DOWN to FLAT."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 26-NOVEMBER: the pre-registered condition was met - LME stock fell 1,150 t to 219,200 t on 25-November, a settled break below the 220,350 t series low (fifth straight draw). Trend moved from FLAT to UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 26-NOVEMBER: Brent rebounded to about $94.7 on 26-November after two days of gains on Middle East attacks (Trading Economics), but remains about 13-20% lower over the month. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 26-NOVEMBER: Straits Daily Brief - effectively closed; IMF PortWatch 1 transit on 22-November (pre-crisis 85/day; transit feed 15 hours stale). IRGC claims of two tankers striking mines remain UNCONFIRMED; Al Jazeera reports Houthi targeting of Saudi Red Sea ports. Iran's reopening terms not accepted; Qatari and Omani mediation continues. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 26-NOVEMBER: core PCE rose 0.3% m/m and 3.3% y/y (highest since 2023) and Q3 GDP was revised to 4.3%; a 25bp December hike is priced with about 60% for January; dollar index about 103.74 (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('TARIFF POLICY'):
        r['risk']+=" UPDATE 26-NOVEMBER: the US proposed Section 301 tariffs on India and 13 other economies with aluminium among the sectors named; proposals are not final (SMM, 26-November)."; hit+=1
assert hit==6,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Wed 25-Nov':
        hc+=1; cat['date']='Daily, from Thu 26-Nov'
        cat['event']=("WEDNESDAY 25-NOVEMBER OFFICIAL: cash $2,849.00 (-$271.50) as the LME lending-threshold cut (50% to 30%) took effect; three-month $2,760.00 (-$29.00), inside the 2,700-2,790 extended-(v) zone; backwardation $89.00; stock a new 219,200 t low. NEXT: Thursday 26-November official (13:20 London) - 2,750 and 2,700 are the remaining objectives; whether the backwardation holds above $15.00; a settled close back above 2,994.50 marks a completed C wave; above 3,097.50 negates the count; invalidation 3,289. Friday 27-November weekly close against 2,750; OPEC+ meeting 29-November; the December Fed meeting (25bp priced); first Q1-2027 Japanese premium offers (none located yet).")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"THURSDAY 26-NOVEMBER ON THE WEDNESDAY 25-NOVEMBER OFFICIAL: the LME's cut in the aluminium Tom-Next lending threshold from 50% to 30% of on-warrant stock took effect and cash fell $271.50 to $2,849.00, collapsing the backwardation to $89.00 from $331.50 - the exchange has dismantled most of the squeeze premium in one session. Three-month slipped $29.00 to $2,760.00, inside the 2,700-2,790 extended wave (v) zone, while visible stock still drew to a new 219,200 t low - so the metal itself is no less scarce. Weights hold at 10/30/60; the stock drawdown risk trend moves to UP.")

# ---- ELLIOTT WAVE: no re-label; count consistent, wave (v) progressing in its objective zone ----
st=d['ew']['short_term']; nx=st['now_x']
st['proj']={'bull':[[nx,m3],[0.99997,2900],[1.0,3000]],'base':[[nx,m3],[0.99997,2730],[1.0,2900]],'bear':[[nx,m3],[0.99997,2700],[1.0,2633]]}
assert st['fwd_pivots'][0]['t']==0.99996
st['fwd_pivots'][0]['w']=("COUNT HELD 26-NOVEMBER: three-month settled 2,760.00 on 25-November, inside the 2,700-2,790 objective zone; extended wave (v) from 3,097.50 now measures $337.50. Cardinal rules intact - wave (ii) at 3,289 below the 3,374 origin, wave (iii) ($294.50) longer than wave (i) ($191), wave (iv) at 3,097.50 clear of the 3,183 wave (i) low. Count: (i) 3,374-3,183, (ii) 3,289, (iii) to 2,994.50, (iv) 3,097.50, extended (v) under way; objectives 2,750-2,700 (2,633 = the weekly 78.6%). The wave (v) low is NOT confirmed until a reversal settles; a settled close above 3,097.50 negates this count.")
lt=d['ew']['long_term']
lt['proj']={'bull':[[lt['now_x'],m3],[0.78,3200],[0.9,3400],[1.0,3550]],'base':[[lt['now_x'],m3],[0.78,2740],[0.9,2950],[1.0,3080]],'bear':[[lt['now_x'],m3],[0.8,2633],[1.0,2550]]}
EWP=("REVIEWED 26-NOVEMBER ON THE 25-NOVEMBER OFFICIAL - COUNT HELD: three-month settled 2,760.00 (-29.00), inside the 2,700-2,790 extended wave (v) zone; wave (v) from 3,097.50 now measures $337.50. All three cardinal rules hold, so no re-label. The one-session $271.50 cash collapse reflects the LME's lending-rule change at the prompt, not the three-month count, and the 2,760 settlement is not added as a pivot because no reversal has confirmed a low. "
 "BASE CASE (about 55%): wave (v) completes in 2,700-2,760 (2,750 and 2,700 the remaining objectives), ending the C wave from 3,374, followed by a corrective rebound toward 2,994.50-3,097.50; the deflated backwardation makes that rebound less explosive than the squeeze would have implied. ALTERNATE (about 45%): a larger-degree leg toward 2,633 (weekly 78.6%) or lower. INVALIDATION: of the count, a settled close above 3,097.50; of the bearish C-wave count, 3,289; a settled close back above 2,994.50 would mark a completed C wave. Confidence low. ")
EWL=("REVIEWED 26-NOVEMBER (MID-WEEK): the Wednesday official at 2,760.00 sits $134.00 below the 2,894 weekly 61.8% retracement, inside the widened 2,700-2,850 base-case completion zone. The base case (about 65%) is held: a correction of the 2,300-3,855 advance completing before a rebound. The alternate toward the 78.6% retracement near 2,633 stays at about 35% and is raised to about 45% on a WEEKLY close below 2,750 (Friday 27-November). A weekly close back above 2,994.50 would favour a completed correction; loses preference only on a weekly close above 3,110. Confidence moderate. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 25-NOVEMBER'),k
    d['ew'][k]['writeup']=pfx+w
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="94.7",day="about $94.69 on 26-November (+0.09%, Trading Economics) after two sessions of gains; Straits Daily Brief settled $94.69 (+3.60% prior session)",
 note="REFRESHED THURSDAY 26-NOVEMBER-2026 (Trading Economics): Brent traded above $94 on escalating Middle East attacks, including Houthi targeting of Saudi Arabia and Iranian reports of vessels striking mines in Hormuz; recovering Gulf shipments and an IEA-projected Q4 surplus limit gains; OPEC+ meets 29-November. Levels approximate. SOURCE: "+S_BR)
M['US dollar index (DXY)'].update(value="103.74",day="about 103.74 on 26-November (+0.04%, Trading Economics)",
 note="REFRESHED THURSDAY 26-NOVEMBER-2026 (Trading Economics): core PCE rose 0.3% m/m and 3.3% y/y, the highest since 2023; Q3 GDP revised to 4.3%; markets price a 25bp December hike and about a 60% chance of another in January. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.09430',day="LME fixing on 25-November, down from 1.09600 on 24-November",note="REFRESHED THURSDAY 26-NOVEMBER-2026 to the 25-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE WEDNESDAY 25-NOVEMBER-2026 LME OFFICIAL, the latest published session. THIS THURSDAY 26-NOVEMBER RUN IS COMPILED AT ABOUT 02:40 LONDON, BEFORE TODAY'S RING; Thursday's official prints at 13:20 London, so Wednesday's official is the correct latest figure. The board rolled ONE session this run. Nothing was estimated or taken intraday. The Trading Economics aluminium reference (about $2,800.75, +0.92% for 25-November, intraday low near $2,745) is a CFD reference cited in text only. Wednesday 25-November had no Tom-Next market (US Thanksgiving), per the LME notice.")
C[1]=("SOURCE CHECK THIS RUN (26-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 25-November session (aluminium cash 2,849.00, three-month 2,760.00, stock 219,200; copper 11,703.00/11,758.00; nickel 15,035.00/15,210.00; zinc 3,520.50/3,394.00; lead 1,792.00/1,827.00; EUR/USD MTLE 1.09430); the aluminium per-metal daily table shows 25-November as its newest row and confirms the $271.50 cash fall.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 18- to 24-November rows match the stored series; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 05- to 20-November points were asserted against those tables on 21-November and the 23- to 25-November points come from agreeing overviews; each metal's 25-November stock change reconciles exactly with the stored 24-November stock. The LME lending-rule details are taken from press reproductions of the LME notice (FX News Group; Investing.com) - the LME notice itself was not fetched; reported wording of the upper band differs between outlets.")
C[3]=("STOCK CHANGES 25-November: aluminium -1,150 to 219,200 (fifth straight draw, new series low); copper -1,075 to 336,750; nickel unchanged at 275,604; zinc +25 to 143,450; lead -275 to 256,675; tin +80 to 3,805.")
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (25-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (eighteen sessions, 02-25 November) as their latest point. "
 "The price chart axis (floor 2,600 / ceiling 3,450) brackets cash 2,849.00 and three-month 2,760.00 ($160 headroom above the floor); the stock chart axis floor of 190,000 t leaves 29,200 t headroom below visible stock of 219,200 t; both are re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $2,849.00 against three-month $2,760.00 is therefore an $89.00 BACKWARDATION, down from $331.50 on 24-November. On 25-November cash and three-month moved in the SAME direction (both down), cash far faster. Press figures for the spread differ by measure and time (traded intraday levels above $400/t were reported on 23-November); the dashboard uses the settled officials only."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $94.7) and the dollar index (about 103.74) are Trading Economics readings for 26-November; TTF (about EUR 88.45/MWh) and the US ten-year row are CARRIED from earlier sessions (not re-fetched). Trading Economics prices are contract-for-difference references, not official benchmarks, so levels are approximate. The Straits Daily Brief (26-November) is flagged DEGRADED (transit feed 15 hours stale, latest transit data 22-November); its mine-strike items are IRGC claims not confirmed by any maritime authority."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 26-NOVEMBER (THURSDAY, PRE-RING): no authorised fetch was blocked. Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/dollar, AL Circle news, SMM news and the Straits Daily Brief (26-November) were fetched; the LME lending-rule change was located by WebSearch and read via FX News Group and Investing.com. A WebSearch for Q1-2027 Japanese premium offers located none; S&P Global reports participants expect premiums under pressure into Q1-2027. No earnings_history company was back-filled this run."); hit+=1
assert hit==2,hit

d['so_what']={"line":"The LME's lower lending threshold broke the aluminium prompt squeeze in a single session - cash fell $271.50 to $2,849 and the backwardation collapsed to $89 from $331.50 - while three-month slipped to a fresh 2026 low of $2,760 and LME stocks drew to a new 219,200 t low.",
 "points":[
 "WHAT MOVED: on the 25-November official cash fell $271.50 (8.7%) to $2,849.00 and three-month $29.00 to $2,760.00. The backwardation (cash above three-month) narrowed to $89.00 from $331.50, and visible LME stock fell 1,150 t to 219,200 t, a fifth straight draw and a new series low. Copper fell 2.5% on the board as metals joined a wider risk selloff.",
 "WHY: the LME cut the stock-holding level that forces large aluminium holders to lend nearby metal from 50% to 30%, effective 25-November - releasing concentrated prompt metal rather than adding new supply. The forward stays heavy on reported LME approval for Indonesian Hua Chin metal, record Chinese output and a hawkish Fed (core PCE 3.3%).",
 "48H DEVELOPMENTS: Brent rebounded to about $94.7 on fresh attacks around the Gulf, with Hormuz still effectively closed (IRGC mine claims unconfirmed); the US proposed Section 301 tariffs on India and 13 other economies naming aluminium; China's three-region ingot inventory fell 4,000 t to 295,500 t.",
 "WHAT TO WATCH: whether the backwardation holds above $15 under the new lending rule, three-month against $2,750-2,700 (a settle back above $2,994.50 would mark a low), Friday's weekly close, OPEC+ on 29-November, and the first Q1-2027 Japanese premium offers (none reported; S&P sees pressure into Q1)."]}

d['feed']=([
 {"when":"Wed 25-Nov","impact":"Bearish","text":"25-NOVEMBER OFFICIAL: cash $2,849.00 (-$271.50); three-month $2,760.00 (-$29.00); backwardation $89.00 (from $331.50); stock -1,150 t to a new 219,200 t low."},
 {"when":"Wed 25-Nov","impact":"Bearish","text":"LME RULES: aluminium Tom-Next lending threshold cut from 50% to 30% of on-warrant stock, effective 25-Nov; 30-80% holders lend at 0.50% of prior cash (FX News Group)."},
 {"when":"Thu 26-Nov","impact":"Bullish","text":"HORMUZ: effectively closed (1 transit on 22-Nov); IRGC mine claims unconfirmed; Houthi targeting of Saudi ports reported (Straits brief 26-Nov)."},
 {"when":"Thu 26-Nov","impact":"Bullish (cost)","text":"ENERGY: Brent ~$94.7 after two days of gains on Middle East attacks; OPEC+ meets 29-Nov (Trading Economics)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":W,
  "headline":"LME ALUMINIUM CASH PLUNGES $271.50 AS SQUEEZE UNWINDS. The Wednesday 25-November official put cash at $2,849.00 (-8.70%) and three-month at $2,760.00 (-1.04%), cutting the backwardation to $89.00 from $331.50. Visible stock still fell 1,150 t to a new 219,200 t series low. Copper fell 2.46% on three-month, zinc 3.25%, nickel 0.56% and lead 0.05%."},
 {"theme":"Market structure","horizon":"Immediate","impact":"Bearish","url":S_LME,
  "headline":"LME CUTS ALUMINIUM LENDING THRESHOLD TO 30% (FX News Group, 25-November): the LME Special Committee reduced the lowest threshold of the aluminium Tom-Next lending rules from 50% to 30%, effective 25-November; holders of 30-80% of on-warrant stock must lend at 0.50% of the previous day's cash price, with holding periods counted from 18-November. The LME said it does not regard backwardations as inherently unhealthy and attributed limited stock ingress to physical tightness."},
 {"theme":"Supply","horizon":"0-6 months","impact":"Bearish","url":S_TE,
  "headline":"INDONESIAN METAL HEADING FOR LME APPROVAL (Trading Economics, 25-November): the exchange is reportedly preparing to approve deliveries from Indonesia's 480 ktpa Hua Chin smelter; aluminium touched about $2,745, its lowest since October 2025, before recovering to about $2,800 (CFD reference)."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL EFFECTIVELY CLOSED (Straits Daily Brief, 26-November): 1 transit on 22-November (IMF PortWatch) vs 85/day pre-crisis. Al Jazeera reports Houthi forces targeting Saudi Red Sea ports; IRGC claims two tankers struck mines remain unconfirmed. Washington has not accepted Iran's reopening terms; Qatari and Omani mediation continues."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish (cost)","url":S_BR,
  "headline":"BRENT REBOUNDS ABOVE $94 (Trading Economics, 26-November): two sessions of gains on escalating Middle East attacks; recovering Gulf shipments and an IEA-projected Q4 surplus cap gains; OPEC+ ministers meet 29-November on 2027 policy - higher oil lifts smelter energy and freight costs."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"CORE PCE AT 3.3%, HIGHEST SINCE 2023 (Trading Economics, 26-November): core PCE rose 0.3% m/m; Q3 GDP revised to 4.3%; a 25bp December hike is priced with about 60% for January; dollar index about 103.74."},
 {"theme":"Trade policy","horizon":"3-12 months","impact":"Mixed","url":S_301,
  "headline":"US PROPOSES SECTION 301 TARIFFS ON 14 ECONOMIES (SMM, 26-November): the proposal covers India and 13 other economies with aluminium among the named sectors; it is not final."},
 {"theme":"China","horizon":"Immediate","impact":"Bullish","url":S_SMM,
  "headline":"CHINA INGOT STOCKS DRAW (SMM, 26-November): three-region aluminium ingot social inventory fell 4,000 t to 295,500 t; cast-alloy ingot inventory fell 3,000 t w/w to a new low of 12,400 t."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])
for p in d['producer_status']: p['asof']=RD

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 25-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 25-Nov)",W])
for x in ([L_LME,S_LME],[L_INV,S_INV],[L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_TE,S_TE],[L_SMM,S_SMM],[L_301,S_301],[L_SPJ,S_SPJ]): d['sources'].append(x)
for x in ([L_LME,S_LME],[L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_TE,S_TE],[L_SPJ,S_SPJ]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-24',3120.5,2789.0,220350]
ph['rows'][-1]=['2026-11-25',cash,m3,stk]; ph['updated']=RD   # same week (w/c 23-Nov): replace
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],d['metals_board'])
