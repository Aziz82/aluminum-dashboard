# Daily data refresh - 2026-11-28 (SATURDAY, ~02:45 UTC; no LME ring today). Board ROLLED TWO SESSIONS to the FRIDAY 27-Nov LME official
# (the 26-Nov official, missing on the prior run, is now published). Cache-busted EN + DE overviews agree on 27-Nov (Al cash 2,983.00 / 3M 2,835.50 /
# stock 215,625; MTLE 1.09660); Al, Cu, Ni, Zn, Pb per-metal tables all show 27-Nov as newest row (no later row -> complete for the weekend).
# Stock changes reconcile 25->26->27. No EW trigger: 3M 2,835.50 below 2,994.50; weekly close above 2,750 keeps the long-term alternate at ~35%.
import json, re, subprocess
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-28'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-28"; L_ST="Straits Daily Brief - Strait of Hormuz, 28-Nov-2026 (effectively closed; 1 transit on 22-Nov per IMF PortWatch; 38 AIS-visible vessels holding; new IRGC mine claims near Khasab unconfirmed; AI-assisted, flagged data gaps)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$94-95 on 27-Nov-2026 (-2.5% on the day), first weekly gain of the month but -15.8% over the month; OPEC+ meets 29-Nov, reportedly weighing quotas held through January"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~104.04 (+0.36%) on 27-Nov-2026; markets almost fully price a 25bp Fed hike on 9-December, another possible in January"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,782.70 (-0.95%) on 27-Nov-2026 (CFD reference, after the official); 'Aluminum hovers near 13-month low' (25-Nov)"
S_CU="https://news.futunn.com/en/post/1005878894/metals-stage-a-major-comeback-lme-copper-records-its-largest"; L_CU="Futu News - Metals stage a major comeback: LME copper records its largest daily gain in nine months as AI-related panic eases and China signals market stabilisation (27-Nov-2026)"
S_AO="https://www.alcircle.com/news/alumina-output-to-rise-7-6-in-china-in-2027-as-guinea-quota-uncertainty-persists-122142"; L_AO="AL Circle - Alumina output to rise 7.6% in China in 2027 as Guinea quota uncertainty persists (SunSirs; 27-Nov-2026): 102.63 Mt in 2027 vs 95.39 Mt; Guinean bauxite ~$70/t"
S_GH="https://www.alcircle.com/news/ghana-wants-its-bauxite-processed-at-home-not-shipped-out-raw-and-plans-to-end-raw-mineral-exports-by-2028-122147"; L_GH="AL Circle - Ghana targets 50% domestic processing of bauxite and manganese by 2028 and 100% by 2030 (27-Nov-2026)"
S_PM="https://www.alcircle.com/news/press-metal-reports-25-7-revenue-growth-and-51-8-rise-in-shareholder-profit-in-q3-2026-122136"; L_PM="AL Circle - Press Metal reports 25.7% revenue growth and 51.8% rise in shareholder profit in Q3 2026 (27-Nov-2026): revenue MYR 5.13bn, profit attributable MYR 855m (from MYR 563.3m)"
S_SPJ="https://www.spglobal.com/energy/en/news-research/latest-news/metals/101326-japanese-q4-aluminum-premium-falls-35-to-255mt-cif-japan"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==2849.0 and B['LME 3-month']['cur']==2760.0
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
# sessions: 25-Nov (old board), 26-Nov, 27-Nov (new board)
c25,m25,s25=2849.0,2760.0,219200
c26,m26,s26=2980.0,2820.5,216650
pc,pm,ps=c26,m26,s26
cash,m3,stk=2983.0,2835.5,215625
spr=cash-m3; psp=pc-pm; assert spr==147.5 and psp==159.5 and s25-2550==s26 and s26-1025==stk
ytd=(m3/3010.5-1)*100; dc=cash-pc; dm=m3-pm; assert dc==3.0 and dm==15.0

VER=("COMPILED SATURDAY 28-NOVEMBER-2026 ABOUT 02:45 LONDON. THERE IS NO LME RING TODAY (WEEKEND), SO THE BOARD IS THE FRIDAY 27-NOVEMBER-2026 LME OFFICIAL - THE LAST TRADING SESSION AND THE CORRECT FIGURE TO CARRY THROUGH THE WEEKEND. The board ROLLED TWO SESSIONS this run: the Thursday 26-November official, which was not yet on the public source at the previous compile, is now published and is used as the PREVIOUS column. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 27-November official for all metals with stocks and FX (EUR/USD MTLE 1.09660); (2) the aluminium, copper, nickel, zinc and lead per-metal daily tables all show 27-November as their newest row - no later row - and their 25-November rows match the stored board; (3) every metal's 26- and 27-November stock changes reconcile with the stored 25-November stock. "
 "The whole board sits on ONE UNIFORM SESSION (27-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" FRIDAY 27-NOVEMBER (the board): CASH SETTLED $2,983.00, UP $3.00 FROM THURSDAY'S $2,980.00 (and up $134.00 from Wednesday's $2,849.00); THREE-MONTH SETTLED $2,835.50, UP $15.00 OR 0.53% FROM $2,820.50 (Thursday +$60.50 from $2,760.00) - a two-session rebound of $75.50 off the 2,760.00 low inside the 2,700-2,790 extended wave (v) zone; $175.00 BELOW the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION REBUILT: $159.50 on 26-November (from $89.00) then $147.50 on 27-November - a thirty-second straight backwardation and the twenty-first above $15.00. On 27-November flat price ROSE while the spread NARROWED (OPPOSITE directions); on 26-November both rose. "
 "VISIBLE LME STOCK FELL 2,550 t TO 216,650 t (26-November) AND 1,025 t TO 215,625 t (27-November) - seven straight draws and a NEW SERIES LOW. The Trading Economics aluminium reference showed about $2,782.70 (-0.95%) later on 27-November - a CFD reference after the official, cited in text only.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"2,983.0","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"2,835.5","pos":True,"delta":VER+AL+" ELLIOTT: three-month has rebounded $75.50 from the 2,760.00 settlement of 25-November; no rule break and no trigger - the low is a CANDIDATE wave (v) end but is not promoted to a confirmed pivot until a settled close back above 2,994.50 (completed C wave). Above 3,097.50 negates the wave (v) count; daily invalidation of the bearish count remains 3,289."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+147.5","pos":True,"delta":VER+f" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $2,983.00 against three-month $2,835.50 is a $147.50 BACKWARDATION, down $12.00 from $159.50 on 26-November but up from $89.00 on 25-November when the LME's lower lending threshold (50% to 30% of on-warrant stock) took effect. ON 27-NOVEMBER THE SPREAD NARROWED WHILE FLAT PRICE ROSE - OPPOSITE DIRECTIONS. It stays above the published $15.00 reversal condition for a twenty-first session and is a thirty-second straight backwardation; a contango beyond $24.50 would reverse the structural signal. The October mean spread was ${oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"215,625","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 2,550 t TO 216,650 t ON 26-NOVEMBER AND 1,025 t TO 215,625 t ON 27-NOVEMBER - seven straight draws and a NEW SERIES LOW (prior low 219,200 t on 25-November). October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 26-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $2,835.50, UP $15.00 FROM THE 26-NOVEMBER $2,820.50 (which was up $60.50 from 2,760.00) - $58.50 BELOW the 2,894 weekly 61.8% and $159.00 BELOW 2,994.50; $175.00 BELOW the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 1,025 t TO 215,625 t on 27-November (26-November -2,550 t) - seven straight draws and a NEW SERIES LOW. AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $147.50 BACKWARDATION, DOWN $12.00 FROM $159.50 ON 26-NOVEMBER (25-November $89.00). CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On 27-November flat price rose (cash +$3.00, three-month +$15.00) while the spread narrowed - OPPOSITE directions. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00, $353.00, $367.50, $331.50, $89.00, $159.50 and $147.50."},
 {"name":"EUR/USD LME fixing","cur":1.0966,"prev":1.0943,"avg":1.1465,"note":VER+" THE LME EURO FIXING WAS 1.09660 ON 27-NOVEMBER (25-November 1.09430; the 26-November fixing was not separately captured), with the dollar index about 104.04 (Trading Economics, 27-November). PREVIOUS COLUMN = the 25-November fixing. AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (27-Nov official)","price":"2,983.0","basis":"THE FRIDAY 27-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $2,983.00, UP $3.00 (26-November $2,980.00; 25-November $2,849.00). No ring at the weekend; next print Monday 30-November 13:20 London."},
 {"tenor":"3-month (27-Nov official)","price":"2,835.5","basis":"THE 27-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $2,835.50, UP $15.00 - a $75.50 two-session rebound from 2,760.00; weekly close above 2,750."},
 {"tenor":"Cash-to-3M structure","price":"+147.5 (BACKWARDATION)","basis":"A $147.50 BACKWARDATION, rebuilt from $89.00 on 25-November ($159.50 on 26-November); on 27-November the spread narrowed while flat price rose."},
 {"tenor":"Visible LME stock","price":"215,625 t","basis":f"DOWN 1,025 t on 27-November (26-November -2,550 t), seven straight draws and a new series low; October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("THE PROMPT PREMIUM PARTLY REBUILDS. On the 27-November official cash $2,983.00 sits $147.50 ABOVE three-month $2,835.50, a BACKWARDATION rebuilt from $89.00 on 25-November (the day the LME cut its aluminium Tom-Next lending threshold from 50% to 30%) via $159.50 on 26-November. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00, $353.00, $367.50, $331.50, $89.00, $159.50 and now $147.50. "
 f"READ: the lending rule capped the squeeze but did not create metal - visible stock drew another 3,575 t over two sessions to a 215,625 t series low, so nearby metal is again commanding a sizeable premium, while the forward rebounded only modestly alongside a broad metals short-covering rally led by copper. The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2600,3450] and d['chart_stock_axis']==[190000,255000]

ls=d['lme_series']; assert ls[-1][0]=='25-Nov' and len(ls)==15
d['lme_series']=ls[2:]+[["26-Nov",c26,m26,s26],["27-Nov",cash,m3,stk]]
assert [tuple(r[1:]) for r in d['lme_series'][-5:]]==[(3201.5,2834.0,221400),(3120.5,2789.0,220350),(c25,m25,s25),(c26,m26,s26),(cash,m3,stk)]
CU25=(11703.0,11758.0,336750); NI25=(15035.0,15210.0,275604); ZN25=(3520.5,3394.0,143450); PB25=(1792.0,1827.0,256675)
CU0=(11965.0,11960.0,337925); NI0=(15665.0,15770.0,275604); ZN0=(3646.0,3523.0,143325); PB0=(1844.0,1869.0,253825)
CU=(12311.5,12330.0,338325); NI=(15745.0,15845.0,275604); ZN=(3677.0,3565.0,143050); PB=(1840.0,1871.0,252225)
old={m['name']:m for m in d['metals_detail']}
assert (old['Copper']['cash'],old['Copper']['m3'])==CU25[:2] and (old['Zinc']['cash'],old['Lead']['cash'],old['Nickel']['cash'])==(ZN25[0],PB25[0],NI25[0])
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU0[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI0[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN0[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB0[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/m25,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU25[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI25[1],1)
ms=d['metals_series']; R=ms['rows']; assert ms['asof']=='2026-11-25'
o20=json.loads(subprocess.check_output(['git','show','d5d523d:market_data.json']))
z0=o20['metals_series']['rows']['ZN'][:3]; p0=o20['metals_series']['rows']['PB'][:3]
assert z0==[3935.0,3869.0,3875.0] and p0==[1869.5,1862.0,1858.0] and R['ZN'][0]==3877.0 and R['ZN'][-1]==ZN25[0] and R['PB'][-1]==PB25[0]
zs=sum(z0)+sum(R['ZN']); psum=sum(p0)+sum(R['PB'])   # 18 sessions 02..25 Nov
mh['zn'][-1]=round(mh['zn'][-1]*((zs+ZN0[0]+ZN[0])/20)/(zs/18),1); mh['pb'][-1]=round(mh['pb'][-1]*((psum+PB0[0]+PB[0])/20)/(psum/18),1)
for k,a,b in (('CU',CU0[0],CU[0]),('NI',NI0[0],NI[0]),('ZN',ZN0[0],ZN[0]),('PB',PB0[0],PB[0])):
    assert len(R[k])==15; R[k]=R[k][2:]+[a,b]
ms['asof']='2026-11-27'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending FRIDAY 27-NOVEMBER-2026 (the last session before the weekend). THE WINDOW ROLLED TWO SESSIONS THIS RUN: 05- and 06-November dropped, 26- and 27-November appended, so the window is 09-November to 27-November. The 26- and 27-November points were read directly from the Westmetall copper, nickel, zinc and lead per-metal tables on 28-November, whose 25-November rows match the stored series.")
ms['src']=["Westmetall - LME official cash settlements, per-metal tables and English/German overviews (27-November-2026 session)",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return "unchanged" if a==b else f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,f" COPPER 27-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU0[0])} from 26-November (26-November {chg(CU0[0],CU25[0])}); three-month ${CU[1]:,.2f}, {chg(CU[1],CU0[1])} - the strongest metal on the board this session as short covering and a China pledge to support equities lifted metals (press reports put intraday copper gains near 6.5%, the largest since January - not an official). STRUCTURE: an $18.50 CONTANGO (26-November a $5.00 backwardation). Stock rose 1,175 t then 400 t to 338,325 t."),
 ("Nickel",NI,f" NICKEL 27-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI0[0])} (26-November {chg(NI0[0],NI25[0])}); three-month ${NI[1]:,.2f}, {chg(NI[1],NI0[1])}. CONTANGO $100.00 (26-November $105.00; 25-November $175.00). Stock unchanged at 275,604 t for a third session."),
 ("Zinc",ZN,f" ZINC 27-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN0[0])} (26-November {chg(ZN0[0],ZN25[0])}); three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN0[1])}. BACKWARDATION $112.00 (26-November $123.00). Stock fell 125 t then 275 t to 143,050 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,f" LEAD 27-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB0[0])} (26-November {chg(PB0[0],PB25[0])}); three-month ${PB[1]:,.2f}, {chg(PB[1],PB0[1])}. CONTANGO $31.00 (26-November $25.00). Stock fell 2,850 t then 1,600 t to 252,225 t."),
]
CROSS=(f" CROSS-METAL 26-27 NOVEMBER: a two-session rebound across the board after the 25-November selloff - three-month copper +{(CU[1]/CU25[1]-1)*100:.2f}%, zinc +{(ZN[1]/ZN25[1]-1)*100:.2f}%, nickel +{(NI[1]/NI25[1]-1)*100:.2f}%, aluminium +{(m3/m25-1)*100:.2f}% and lead +{(PB[1]/PB25[1]-1)*100:.2f}% - attributed in press to short covering, easing AI-related equity worries and a Chinese pledge to support its stock market (Futu News, 27-November). The dollar index firmed to about 104.04 with a 9-December Fed hike almost fully priced (Trading Economics). The LME euro fixing was 1.0966.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='25-Nov' and len(i['hist'])==15 and i['hist'][0][0]=='05-Nov'
        i['hist']=i['hist'][2:]+[["26-Nov",CU0[0]],["27-Nov",CU[0]]]; assert i['hist'][0][0]=='09-Nov'
        assert [v for _,v in i['hist']]==R['CU']
        i['val']="~12,330.00 (3M); 12,311.50 (cash) $/t"; i['ratio']="~12,311.50 $/t cash vs LME 3M 12,330.00 $/t"; i['trend']='up'
        i['src']=("LME official cash settlement, rolled TWO SESSIONS to the FRIDAY 27-NOVEMBER-2026 session at $12,311.50 (26-November $11,965.00; 25-November $11,703.00). 05- and 06-November dropped and 26- and 27-November appended, so the series is the last fifteen published official cash sessions, 09-November to 27-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall copper per-metal table. "
                  "Copper structure for context: an $18.50 contango on 27-November; stock 338,325 t.")
d['inputs_summary']=("UPDATE 28-NOVEMBER: Copper rolled two sessions to the Friday 27-November LME official cash of $12,311.50 (window 09- to 27-November). No new carbon, fluoride, silicon or magnesium mark was located (gaps stay gaps). Raw materials: SunSirs (via AL Circle, 27-November) sees China alumina output up 7.6% to 102.63 Mt in 2027 with Guinea's export-quota policy still unconfirmed and Guinean bauxite near $70/t; Ghana targets 50% domestic bauxite processing by 2028. Energy: Brent about $94-95 on 27-November (Trading Economics). "+d['inputs_summary'])

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
NC3="COMPILED FRIDAY 27-NOVEMBER-2026 BEFORE THE RING (LME BOARD CARRIED ON THE WEDNESDAY 25-NOVEMBER OFFICIAL - THE THURSDAY 26-NOVEMBER OFFICIAL WAS NOT YET PUBLISHED ON THE PUBLIC SOURCE)."
NC4="COMPILED SATURDAY 28-NOVEMBER-2026 (NO RING AT THE WEEKEND; LME BOARD ROLLED TWO SESSIONS TO THE FRIDAY 27-NOVEMBER OFFICIAL, THE LAST TRADING SESSION)."
REPL=[
 ("0.50 times the 25-November official cash of $2,849.00, or $1,424.50, DOWN $135.75 against the 24-November figure used previously",f"0.50 times the 27-November official cash of $2,983.00, or ${tl:,.2f}, UP ${tl-1424.50:,.2f} against the 25-November figure used previously"),
 ("0.50 times the 25-November official cash of $2,849.00, or $1,424.50, leaving a $978.50 residual market leg out of the $2,403/t US duty-paid premium (59.3%",f"0.50 times the 27-November official cash of $2,983.00, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}%"),
 ("residual market leg of $978.50, so 59.3%",f"residual market leg of ${resid:,.2f}, so {share:.1f}%"),
 ("$1,424.50 on 25-November cash, 59.3%",f"${tl:,.2f} on 27-November cash, {share:.1f}%"),
 ("THE RATIO: LME Alumina at $398.24/t against the 25-November aluminium three-month of $2,760.00 is 14.43%",f"THE RATIO: LME Alumina at $398.24/t against the 27-November aluminium three-month of $2,835.50 is {398.24/m3*100:.2f}%"),
 ("REVIEWED 27-NOVEMBER: no newer public disclosure","REVIEWED 28-NOVEMBER: no newer public disclosure"),
 ("REVIEWED 27-NOVEMBER. NO NEW DATED","REVIEWED 28-NOVEMBER. NO NEW DATED"),
 (NC3,NC4)]
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
assert "$1,424.50" not in blob and "COMPILED FRIDAY 27-NOVEMBER-2026 BEFORE THE RING" not in blob, (blob.count("$1,424.50"),)
# any residual 'THE BOARD IS CARRIED ON THE WEDNESDAY 25-NOVEMBER' verbose preambles in other panels
OLDV=("COMPILED FRIDAY 27-NOVEMBER-2026 ABOUT 02:45 LONDON - BEFORE TODAY'S LME RING (13:20 LONDON). THE BOARD IS CARRIED ON THE WEDNESDAY 25-NOVEMBER-2026 LME OFFICIAL: the Thursday 26-November official COULD NOT BE LOCATED THIS RUN - the cache-busted Westmetall English and German overviews and the aluminium, copper and zinc per-metal tables all still show 25-November as their newest session, and a web search found no published 26-November official. The 25-November figures were verified by the previous run and re-confirmed this run; nothing was estimated. ")
NEWV=("COMPILED SATURDAY 28-NOVEMBER-2026 ABOUT 02:45 LONDON - NO LME RING AT THE WEEKEND. THE BOARD IS THE FRIDAY 27-NOVEMBER-2026 LME OFFICIAL, THE LAST TRADING SESSION; it ROLLED TWO SESSIONS this run (the 26-November official is now published). Figures below that cite an earlier session are labelled with that session. ")
n=blob.count(OLDV); print('oldv',n)
d=walk(d,lambda s: s.replace(OLDV,NEWV))

d['lme_commentary']=("THE SQUEEZE PREMIUM PARTLY REBUILDS; THE FORWARD BOUNCES OFF ITS LOW. Two sessions rolled this run. Thursday 26-November: cash $2,980.00 (+$131.00), three-month $2,820.50 (+$60.50), backwardation $159.50, stock 216,650 t. Friday 27-November: cash $2,983.00 (+$3.00), three-month $2,835.50 (+$15.00), backwardation $147.50 - flat price up while the spread narrowed (opposite directions) - and visible stock 215,625 t, a seventh straight draw and a new series low. "
 "The bounce came with a broad metals rebound led by copper (three-month +4.86% over the two sessions on the officials; press cites short covering and a Chinese pledge to support equities). The three-month weekly close at $2,835.50 held above 2,750, but sits below the 2,894 weekly 61.8% and well below 2,994.50. The Trading Economics CFD reference slipped to about $2,782.70 after the official on Friday - a reference, not used on the board. "
 f"Forecasts still disagree on 2027 (BigMint near balance; Trading Economics-cited surplus; Emkay Global ~400 kt deficit). October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} below its October mean.")
d['net_read']=("NET: BEARISH-TO-NEUTRAL ON THE FORWARD; PROMPT SUPPORT RESTORED. Against: three-month at $2,835.50, still $175.00 below the 2026 starting official and under the 2,894 weekly 61.8%; reported LME approval for Indonesian Hua Chin metal; a firmer dollar (about 104.04) with a 9-December Fed hike almost fully priced; forecasts of 2027 balance or surplus. "
 "Supportive: the backwardation rebuilt to $147.50 within two sessions of the LME lending change, visible stock at a 215,625 t series low after seven draws, a broad metals short-covering rally, and Hormuz still effectively closed.")
d['bottom_line']=("BOTTOM LINE: the board rolled two sessions to Friday 27-November - cash $2,983.00, three-month $2,835.50 (a $75.50 rebound from the 2,760.00 low), a $147.50 backwardation rebuilt after the LME lending change, and visible stock at a 215,625 t series low. "
 "Scenario weights hold at 10% bull / 30% base / 60% bear (no pre-registered trigger fired). The weekly close above 2,750 keeps the long-term alternate at about 35%. A settled close back above 2,994.50 would mark a completed C wave; above 3,097.50 negates the count; daily invalidation 3,289. Next print Monday 30-November 13:20 London; OPEC+ meets Sunday 29-November; the Fed decides 9-December.")
for fp in d['outlook']['forward_path']: pass

c2=d['commercial']
a0=c2.find("FIRST, THE PROMPT PREMIUM DEFLATES - FORWARD STILL WEAK:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, THE PROMPT PREMIUM PARTLY REBUILDS - FORWARD OFF ITS LOW: on 27-November cash settled $2,983.00 and three-month $2,835.50, leaving a $147.50 backwardation (from $89.00 on 25-November, when the LME's cut in the aluminium lending threshold to 30% of on-warrant stock took effect; $159.50 on 26-November); nearby metal again carries a sizeable premium over forward metal, so there is no carry reward for holding stock - and visible LME stock drew for a seventh session to a 215,625 t series low. "+c2[a1:]
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find("; the dollar index near",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 27-November official closed the week with three-month at $2,835.50 (above 2,750) and cash at $2,983.00; OPEC+ meets Sunday 29-November; the Fed decides 9-December with a 25bp hike almost fully priced (Trading Economics 27-November); first Q1-2027 Japanese premium offers, which typically emerge from late November or early December (none located yet; some participants expect $190-200/t CIF Japan per S&P Global, below Q4's $255)"+c2[b1:]
d['commercial']=c2

for s in d['outlook']['scenarios']:
    assert s['prob']=={'Bull':'10%','Base':'30%','Bear':'60%'}[s['case']]
    s['drivers']=("HELD 28-NOVEMBER AT 10/30/60: the 26- and 27-November officials lifted three-month to $2,835.50 (+$75.50 from 2,760.00) - a rebound, but still $159.00 short of the 2,994.50 reversal trigger, so no pre-registered trigger fired; the backwardation rebuilt to $147.50. ")+s['drivers']
for k in ('bull','base','bear'): d['outlook']['scenario_paths'][k][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 28-NOVEMBER: the backwardation rebuilt to $159.50 (26-November) and $147.50 (27-November) from $89.00, restoring a wide cushion against contango two sessions after the LME lending change. Trend cut from FLAT to DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 28-NOVEMBER: stock fell 2,550 t and 1,025 t to 215,625 t on 27-November, a seventh straight draw and a new series low. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 28-NOVEMBER: Brent fell about 2.5% on 27-November to about $94-95 and is down about 15.8% over the month (Trading Economics); OPEC+ meets 29-November, reportedly weighing quotas held through January. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 28-NOVEMBER: Straits Daily Brief - still effectively closed (1 transit on 22-November vs 85/day pre-crisis; 38 AIS-visible vessels holding); new IRGC claims of a tanker mine strike near Khasab are uncorroborated; Iranian state media say the strait will not reopen while the US blockade continues. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 28-NOVEMBER: the dollar index rose to about 104.04 (+0.36%) on 27-November with a 25bp hike on 9-December almost fully priced and another possible in January (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
assert hit==5,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Fri 27-Nov':
        hc+=1; cat['date']='Daily, from Mon 30-Nov'
        cat['event']=("FRIDAY 27-NOVEMBER OFFICIAL (weekly close): cash $2,983.00; three-month $2,835.50 (above 2,750; +$75.50 from the 2,760.00 low); backwardation $147.50; stock a new 215,625 t low. NEXT: Monday 30-November official (13:20 London) - whether the rebound extends toward the 2,894 weekly 61.8% and 2,994.50 (a settled close above it marks a completed C wave) or rolls back toward 2,750-2,700; whether the backwardation holds above $15.00; above 3,097.50 negates the count; invalidation 3,289. OPEC+ meeting Sunday 29-November; the Fed on 9-December (25bp almost fully priced); first Q1-2027 Japanese premium offers (none located; some participants expect $190-200/t CIF Japan).")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"SATURDAY 28-NOVEMBER ON THE FRIDAY 27-NOVEMBER OFFICIAL (two sessions rolled): three-month rebounded $75.50 from 2,760.00 to $2,835.50 and cash to $2,983.00 as metals staged a broad short-covering rally led by copper; the backwardation rebuilt to $147.50 from $89.00 and visible stock drew to a 215,625 t series low - the LME's lending change capped the squeeze but the metal is still scarce. The weekly close held above 2,750, so the long-term alternate is not raised; weights hold at 10/30/60. The contango risk trend moves to DOWN.")

# ---- ELLIOTT WAVE: count held; 2,760 is a candidate (v) low, NOT added as a confirmed pivot ----
st=d['ew']['short_term']; nx=st['now_x']
st['proj']={'bull':[[nx,m3],[0.99997,2994.5],[1.0,3100]],'base':[[nx,m3],[0.99997,2894],[1.0,2950]],'bear':[[nx,m3],[0.99997,2760],[1.0,2700]]}
assert st['fwd_pivots'][0]['t']==0.99996
st['fwd_pivots'][0]['p']=2994.5
st['fwd_pivots'][0]['w']=("COUNT HELD 28-NOVEMBER: three-month settled 2,820.50 (26-November) and 2,835.50 (27-November), a $75.50 rebound from the 2,760.00 settlement of 25-November, which sat inside the 2,700-2,790 objective zone. Cardinal rules intact - wave (ii) at 3,289 below the 3,374 origin, wave (iii) ($294.50) longer than wave (i) ($191), wave (iv) at 3,097.50 clear of the 3,183 wave (i) low. 2,760 is the CANDIDATE wave (v) end; the forward marker is the 2,994.50 wave (iii) low - a settled close above it confirms a completed C wave and promotes 2,760 to a confirmed pivot. A settled close back below 2,760 resumes wave (v) toward 2,750-2,700; above 3,097.50 negates this count.")
lt=d['ew']['long_term']
lt['proj']={'bull':[[lt['now_x'],m3],[0.78,3200],[0.9,3400],[1.0,3550]],'base':[[lt['now_x'],m3],[0.78,2900],[0.9,2980],[1.0,3080]],'bear':[[lt['now_x'],m3],[0.8,2633],[1.0,2550]]}
EWP=("REVIEWED 28-NOVEMBER ON THE 27-NOVEMBER OFFICIAL - COUNT HELD: three-month settled 2,820.50 (+60.50) and 2,835.50 (+15.00) after the 2,760.00 settlement inside the 2,700-2,790 extended wave (v) zone. All three cardinal rules hold, so no re-label. The rebound is consistent with wave (v) having ended at 2,760, but 2,760 is NOT added as a confirmed pivot until a settled close above 2,994.50 (the wave (iii) low) shows the C wave complete. "
 "BASE CASE (about 60%, up from 55%): wave (v) - and the C wave from 3,374 - completed near 2,760, with a corrective rebound toward 2,894 then 2,994.50-3,097.50. ALTERNATE (about 40%): the bounce is a minor fourth within an unfinished wave (v), with a settled close back below 2,760 targeting 2,700 and 2,633 (weekly 78.6%). INVALIDATION: of the count, a settled close above 3,097.50; of the bearish C-wave count, 3,289. Confidence low. ")
EWL=("REVIEWED 28-NOVEMBER (WEEKLY CLOSE): the Friday 27-November official closed the week at 2,835.50, ABOVE 2,750, so the alternate toward the 78.6% retracement near 2,633 is NOT raised and stays at about 35%; the base case (about 65%) - a correction of the 2,300-3,855 advance completing in the 2,700-2,850 zone - is held, with the weekly low so far 2,760.00. A weekly close back above 2,994.50 would favour a completed correction; loses preference only on a weekly close above 3,110. Confidence moderate. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 27-NOVEMBER'),k
    d['ew'][k]['writeup']=pfx+w
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="94.0",day="about $94.00 on 27-November (-2.48%, Trading Economics; its text puts Brent near $95); Straits Daily Brief shows $95.44 (timestamps differ)",
 note="REFRESHED SATURDAY 28-NOVEMBER-2026 (Trading Economics): Brent slipped on Friday despite attacks on Middle Eastern energy infrastructure (Houthi strikes on Saudi Arabia's Jazan refinery and earlier the Ras Tanura hub; tanker attacks near Hormuz), posting a weekly gain of under 2% - its first of the month - but down about 15.8% over the month; OPEC+ meets Sunday 29-November, reportedly weighing quotas held through January. Levels approximate. SOURCE: "+S_BR)
M['US dollar index (DXY)'].update(value="104.04",day="about 104.04 on 27-November (+0.36%, Trading Economics); ended a volatile week little changed",
 note="REFRESHED SATURDAY 28-NOVEMBER-2026 (Trading Economics): markets almost fully price a 25bp Fed hike on 9-December with another possible in January; October core PCE 3.3% y/y, the highest since 2023. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.09660',day="LME fixing on 27-November, up from 1.09430 on 25-November",note="REFRESHED SATURDAY 28-NOVEMBER-2026 to the 27-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 27-NOVEMBER-2026 LME OFFICIAL. THIS SATURDAY 28-NOVEMBER RUN HAS NO RING (WEEKEND), SO THE LAST TRADING SESSION'S OFFICIAL IS CARRIED BECAUSE THE MARKET IS SHUT; it was verified complete - the aluminium, copper, nickel, zinc and lead per-metal tables show NO row after 27-November. The board rolled TWO sessions this run: the Thursday 26-November official, not yet on the public source at the previous compile, is now published and forms the previous column. Nothing was estimated or taken intraday. "
 "The Trading Economics aluminium reference (about $2,782.70, -0.95% on 27-November) and press reports of intraday copper gains near 6.5% are references, not officials, and are cited in text only.")
C[1]=("SOURCE CHECK THIS RUN (28-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on the full 27-November session (aluminium cash 2,983.00, three-month 2,835.50, stock 215,625; copper 12,311.50/12,330.00; nickel 15,745.00/15,845.00; zinc 3,677.00/3,565.00; lead 1,840.00/1,871.00; EUR/USD MTLE 1.09660). All five per-metal tables were fetched and supply the 26-November row (aluminium 2,980.00/2,820.50/216,650; copper 11,965.00/11,960.00; nickel 15,665.00/15,770.00; zinc 3,646.00/3,523.00; lead 1,844.00/1,869.00); their 25-November rows match the stored board.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 02- to 25-November rows match the stored series; the copper, nickel, zinc and lead per-metal tables' 23- to 25-November rows match the stored sparkline points; each metal's 26- and 27-November stock changes reconcile with the stored 25-November stock. The 26-November EUR/USD fixing was not separately captured, so the EUR/USD previous column is the 25-November fixing and is labelled as such.")
C[3]=("STOCK CHANGES 26-November / 27-November: aluminium -2,550 / -1,025 to 215,625 (seven straight draws, new series low); copper +1,175 / +400 to 338,325; nickel unchanged at 275,604; zinc -125 / -275 to 143,050; lead -2,850 / -1,600 to 252,225; tin stock 3,680 on 27-November.")
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (27-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper, nickel, zinc and lead October cash means as shown in the LME Board. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (twenty sessions, 02-27 November) as their latest point. "
 "The price chart axis (floor 2,600 / ceiling 3,450) brackets cash 2,983.00 and three-month 2,835.50; the stock chart axis floor of 190,000 t leaves 25,625 t headroom below visible stock of 215,625 t (about eight sessions at the recent drawdown pace) and will be lowered before stock approaches it; both are re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $2,983.00 against three-month $2,835.50 is therefore a $147.50 BACKWARDATION, down from $159.50 on 26-November and up from $89.00 on 25-November. On 27-November the spread NARROWED while flat price ROSE - opposite directions; on 26-November both rose. The dashboard uses the settled officials only."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $94-95; the Trading Economics page shows $94.00 while its text says about $95, and the Straits brief shows $95.44) and the dollar index (about 104.04) are readings for 27-November; TTF and the US ten-year row are CARRIED from earlier sessions (not re-fetched). Trading Economics prices are contract-for-difference references, not official benchmarks. The Straits Daily Brief (28-November) is AI-assisted; its transit figure is six days old, its AIS count likely undercounts, and the IRGC mine claims (via Press TV) are unattributed and unconfirmed."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 28-NOVEMBER (SATURDAY): no authorised fetch was blocked; mining.com search returned HTTP 403 (not needed). Westmetall EN and DE overviews plus all five per-metal tables, Trading Economics aluminium/Brent/dollar, AL Circle news, SMM news (no aluminium price items dated 27-28 November) and the Straits Daily Brief (28-November) were fetched; the copper rally was corroborated via WebSearch (Futu News). A search for Q1-2027 Japanese premium offers again located none. PEER EARNINGS: Press Metal Q3-2026 added (AL Circle, 27-November) and its earnings_history refreshed. No inputs hist mark other than the Copper roll was appended."); hit+=1
assert hit==2,hit
for i,cv in enumerate(C):
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: PRESS METAL Q3-2026 ADDED THIS RUN (28-NOVEMBER) - revenue MYR 5.13bn (+25.7%) and profit attributable MYR 855m (+51.8% from MYR 563.3m), as reported (rounded) by AL Circle on 27-November; the Bursa filing itself was not fetched. "+cv

d['so_what']={"line":"Aluminium closed the week off its lows - three-month rebounded $75.50 to $2,835.50 over Thursday-Friday in a broad metals short-covering rally, the backwardation rebuilt to $147.50 after the LME's lending change, and LME stocks drew to a new 215,625 t low.",
 "points":[
 "WHAT MOVED: the board rolled two sessions to Friday 27-November. Cash rose to $2,983.00 (from $2,849.00 on Wednesday) and three-month to $2,835.50 (from $2,760.00). The backwardation (cash above three-month) rebuilt to $159.50 on Thursday and $147.50 on Friday; visible LME stock fell 3,575 t over the two sessions to 215,625 t, a seventh straight draw.",
 "WHY: metals bounced together - copper three-month rose about 4.9% over the two officials on short covering, easing AI-related equity worries and a Chinese pledge to support stocks. The LME's lower lending threshold capped the prompt squeeze but did not add metal, so nearby aluminium is again commanding a sizeable premium.",
 "48H DEVELOPMENTS: Hormuz stays effectively closed (new mine claims unconfirmed); Brent eased to about $94-95 after attacks on Saudi energy sites; the dollar firmed to about 104 with a 9-December Fed hike almost fully priced; SunSirs sees China alumina output up 7.6% in 2027 with Guinea's export quota still unconfirmed; Press Metal reported Q3 profit up 51.8%.",
 "WHAT TO WATCH: Monday's official against the 2,894 and 2,994.50 levels (a settle above 2,994.50 would mark a low) versus a slip back under 2,760; OPEC+ on Sunday 29-November; the Fed on 9-December; first Q1-2027 Japanese premium offers (some expect $190-200/t, below Q4's $255)."]}

d['feed']=([
 {"when":"Fri 27-Nov","impact":"Bullish","text":"27-NOVEMBER OFFICIAL (weekly close): cash $2,983.00; three-month $2,835.50 (+$15.00); backwardation $147.50; stock -1,025 t to a new 215,625 t low."},
 {"when":"Thu 26-Nov","impact":"Bullish","text":"26-NOVEMBER OFFICIAL (published after the prior run): cash $2,980.00 (+$131.00); three-month $2,820.50 (+$60.50); backwardation $159.50; stock -2,550 t to 216,650 t."},
 {"when":"Fri 27-Nov","impact":"Bullish","text":"METALS REBOUND: copper three-month official $12,330 (+3.09% d/d); press cites short covering and a China equity-support pledge (Futu News)."},
 {"when":"Sat 28-Nov","impact":"Bullish","text":"HORMUZ: effectively closed (1 transit on 22-Nov; 38 vessels holding); IRGC mine claims near Khasab unconfirmed (Straits brief 28-Nov)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM REBOUNDS OFF 13-MONTH LOW AS BACKWARDATION REBUILDS. The Thursday 26-November official put cash at $2,980.00 (+$131.00) and three-month at $2,820.50 (+$60.50); Friday 27-November settled cash $2,983.00 and three-month $2,835.50 (+$15.00), a $147.50 backwardation. Visible stock fell to a 215,625 t series low after seven straight draws."},
 {"theme":"Base metals","horizon":"Immediate","impact":"Bullish","url":S_CU,
  "headline":"COPPER LEADS A BROAD METALS COMEBACK (Futu News, 27-November): LME copper posted its largest daily gain in nine months as AI-related panic eased and China signalled market stabilisation. On the officials, copper three-month rose to $12,330.00 (+3.09% on the day, +4.86% over two sessions); zinc, nickel and lead also rose."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL EFFECTIVELY CLOSED (Straits Daily Brief, 28-November): 1 transit on 22-November vs 85/day pre-crisis and 38 AIS-visible vessels holding position; IRGC claims (via Press TV) that a tanker may have struck a mine near Khasab are unconfirmed; Iranian state media say the strait will not reopen while the US blockade continues."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Mixed","url":S_BR,
  "headline":"BRENT EASES TO ABOUT $94-95 (Trading Economics, 27-November): despite Houthi strikes on Saudi Arabia's Jazan refinery and tanker attacks near Hormuz, Brent fell on Friday and is down about 15.8% over the month; OPEC+ meets Sunday 29-November, reportedly weighing quotas held through January."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"DOLLAR FIRMS AS FED HIKE NEARLY FULLY PRICED (Trading Economics, 27-November): the dollar index rose about 0.36% to about 104.04; markets almost fully price a 25bp hike on 9-December with another possible in January."},
 {"theme":"Alumina","horizon":"3-12 months","impact":"Bearish","url":S_AO,
  "headline":"CHINA ALUMINA OUTPUT SEEN UP 7.6% IN 2027 (SunSirs via AL Circle, 27-November): to 102.63 Mt from 95.39 Mt; Guinea's bauxite export-quota policy had not been implemented by mid-November; Guinean bauxite near $70/t; a quota near 156.5 Mt could force refinery cuts."},
 {"theme":"Raw materials","horizon":"1-5 years","impact":"Mixed","url":S_GH,
  "headline":"GHANA TARGETS DOMESTIC BAUXITE PROCESSING (AL Circle, 27-November): the government aims to process at least 50% of bauxite and manganese output locally by 2028 and all of it by 2030, with a proposed $1.5bn for processing capacity."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Bullish (margin)","url":S_PM,
  "headline":"PRESS METAL Q3 PROFIT UP 51.8% (AL Circle, 27-November): revenue MYR 5.13bn (+25.7%) and profit attributable MYR 855m (from MYR 563.3m) on higher LME aluminium prices during the quarter."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])
for p in d['producer_status']: p['asof']=RD

# ---- peer earnings: Press Metal Q3-2026 ----
d['earnings'].insert(0,{"company":"Press Metal Aluminium (PMETAL)","group":"Aluminum producer (Malaysia / South-East Asia)","period":"Q3 2026 (Jul-Sep 2026)","reported":"27-Nov-2026","reported_iso":"2026-11-27",
 "headline":"Q3-2026: revenue MYR 5.13bn (US$1.24bn), UP 25.7% y/y from MYR 4.08bn; profit attributable to shareholders MYR 855m (US$207m), UP 51.8% from MYR 563.3m. Figures as reported (rounded) by AL Circle on 27-November; the company attributes the result in part to higher LME aluminium prices.",
 "readthrough":"PRICE LEVERAGE AT A NON-GULF, NON-CHINA SMELTER: Q3 profit rose again from Q2's MYR 801m as the LME averaged well above a year earlier (AL Circle cites $3,075/t at the start of July, a $3,373 peak on 11-August and $3,204 at end-September). With three-month now near $2,835, Q4 faces a lower price base.",
 "sentiment":"Positive","eps":None,"revenue_bn":None,"yoy_pct":51.8,"url":S_PM})
eh=d['earnings_history']['PMETAL']; assert eh['points'][-1][0]=='Q2-26'
eh['points']=eh['points'][1:]+[["Q3-26",855.0]]
eh['src']=["AL Circle - Press Metal Q3-2026: profit attributable MYR 855m (from MYR 563.3m), revenue MYR 5.13bn (+25.7%), 27-Nov-2026; earlier points from prior sourced reports (Q2-26 MYR 801m, The Star 28-Aug-2026)",S_PM]
d['earnings_note']="PRESS METAL REPORTED (added 28-November): Q3-2026 revenue MYR 5.13bn (+25.7%), profit attributable MYR 855m (+51.8%) (AL Circle, 27-November). "+d['earnings_note']

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 27-Nov-2026 session (EN and DE overviews agree; all five per-metal tables newest row 27-Nov, supplying 26-Nov)",W])
for x in ([L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_TE,S_TE],[L_CU,S_CU],[L_AO,S_AO],[L_GH,S_GH],[L_PM,S_PM]): d['sources'].append(x)
for x in ([L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_CU,S_CU],[L_AO,S_AO]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-25',2849.0,2760.0,219200]
ph['rows'][-1]=['2026-11-27',cash,m3,stk]; ph['updated']=RD   # same week (w/c 23-Nov): replace with latest session
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
