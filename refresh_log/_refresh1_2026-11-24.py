# Daily data refresh - 2026-11-24 (TUESDAY, ~02:35 UTC, BEFORE the Tuesday ring). Board ROLLED ONE SESSION to the MONDAY 23-Nov LME official.
# Cache-busted EN + DE overviews agree on 23-Nov (Al cash 3,201.50 / 3M 2,834.00 / stock 221,400; MTLE 1.09460); Al per-metal table newest row 23-Nov.
# All five metals' stock changes reconcile with 20-Nov (DE overview change column). Cash AND 3M both up (same direction); backwardation $367.50 (series widest).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-24'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-24"; L_ST="Straits Daily Brief - Strait of Hormuz, 24-Nov-2026 (closed; 72 vessels holding; new US Treasury sanctions on Iran tanker finance; Brent $89.49)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$88.79 (-0.65%) on 24-Nov-2026 after a fall to a three-month low on 23-Nov on US-Iran diplomacy signals"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~104.23 (24-Nov-2026); ~96% probability priced for a 25bp December Fed hike"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,866.70 (+0.95%) on 23-Nov-2026 (CFD reference)"
S_IN="https://www.alcircle.com/news/india-probes-aluminium-dumping-by-china-malaysia-vietnam-thailand-vedanta-hindalco-shares-eyed-122026"; L_IN="AL Circle - India opens anti-dumping probe into aluminium imports from China, Malaysia, Vietnam, Thailand (19-Nov-2026)"
S_SP="https://www.spglobal.com/energy/en/news-research/latest-news/metals/101326-japanese-q4-aluminum-premium-falls-35-to-255mt-cif-japan"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3184.5 and B['LME 3-month']['cur']==2831.5
oct_c,oct_m,oct_s,oct_sp=B['LME Cash settlement']['avg'],B['LME 3-month']['avg'],B['LME warehouse stock (t)']['avg'],B['Cash-to-3M spread']['avg']
pc,pm,ps=3184.5,2831.5,223525            # 20-Nov (previous column)
cash,m3,stk=3201.5,2834.0,221400          # 23-Nov (board)
spr=cash-m3; psp=pc-pm; assert spr==367.5 and psp==353.0 and ps-2125==stk
ytd=(m3/3010.5-1)*100

VER=("COMPILED TUESDAY 24-NOVEMBER-2026 ABOUT 02:35 LONDON - BEFORE TODAY'S LME RING (13:20 LONDON). THE BOARD IS THE MONDAY 23-NOVEMBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION; it ROLLED ONE SESSION this run (the previous run carried Friday 20-November). "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 23-November official for all metals with stocks and FX (EUR/USD MTLE 1.09460; 20-November 1.09820); (2) the aluminium per-metal daily table shows 23-November as its newest row and its 17- to 20-November rows match the stored series; (3) every metal's 23-November stock change on the German overview reconciles exactly with the stored 20-November stock. "
 "The whole board sits on ONE UNIFORM SESSION (23-November). Average columns are the completed OCTOBER-2026 official means (22 sessions).")
AL=(" MONDAY 23-NOVEMBER (the board): CASH SETTLED $3,201.50, UP $17.00 OR 0.53% FROM FRIDAY'S $3,184.50. THREE-MONTH SETTLED $2,834.00, UP $2.50 OR 0.09% FROM $2,831.50 - the first three-month gain after four straight declines, still inside the 2,830-2,850 Elliott completion zone and $176.50 BELOW the first-published 2026 three-month official of $3,010.50 (year to date "+f"{ytd:+.2f}%). "
 "THE BACKWARDATION WIDENED AGAIN TO $367.50 (20-November $353.00) - the widest in this series, a twenty-eighth straight backwardation and the seventeenth above $15.00. This session cash and three-month moved in the SAME direction (both up), ending three sessions of opposite moves, but cash rose faster so the spread still widened. "
 "VISIBLE LME STOCK FELL 2,125 t TO 221,400 t - a third straight draw, within 1,050 t of the 17-November series low of 220,350 t. The Trading Economics aluminium reference shows about $2,866.70 (+0.95%) for 23-November - a CFD reference cited in text only.")
d['kpi_cards']=[
 {"label":"LME CASH ($/t)","value":"3,201.5","pos":True,"delta":VER+AL},
 {"label":"LME 3-MONTH ($/t)","value":"2,834.0","pos":True,"delta":VER+AL+" THREE-MONTH HELD INSIDE THE 2,830-2,850 EXTENDED-(v) ZONE, $60.00 BELOW the 2,894 weekly 61.8% retracement. A settled close below about 2,803 would make wave (v) longer than wave (iii) and force a re-label; a settled close back above 2,994.50 would signal a failed break; above 3,097.50 negates the wave (v) count; daily invalidation of the bearish count remains 3,289."},
 {"label":"CASH-TO-3M SPREAD ($/t)","value":"+367.5","pos":True,"delta":VER+f" CONVENTION: CASH ABOVE THREE-MONTH IS BACKWARDATION; CASH BELOW THREE-MONTH IS CONTANGO. Cash $3,201.50 against three-month $2,834.00 is a $367.50 BACKWARDATION, UP from $353.00 on 20-November and $260.00 on 19-November - the widest in this series. On 23-November cash and three-month both rose (same direction), after three sessions of opposite moves. It stays above the published $15.00 reversal condition for a seventeenth session and is a twenty-eighth straight backwardation; a contango beyond $24.50 would reverse the structural signal. The October mean spread was ${oct_sp:,.2f}."},
 {"label":"LME STOCK (t)","value":"221,400","pos":True,"delta":VER+f" VISIBLE LME ALUMINIUM STOCK FELL 2,125 t TO 221,400 t ON 23-NOVEMBER, a third straight draw (20-November -900 t; 19-November -1,725 t), leaving it 1,050 t above the 17-November series low of 220,350 t. October's mean stock was {oct_s:,} tonnes."},
]
d['benchmark']=[
 {"name":"LME Cash settlement","cur":cash,"prev":pc,"avg":oct_c,"note":VER+AL+f" AVERAGE COLUMN: the completed OCTOBER-2026 official cash mean (22 sessions); cash now sits ${abs(cash-oct_c):,.2f} "+("above" if cash>oct_c else "beneath")+" it. PREVIOUS COLUMN = the 20-November official."},
 {"name":"LME 3-month","cur":m3,"prev":pm,"avg":oct_m,"note":VER+f" THREE-MONTH SETTLED $2,834.00, UP $2.50 FROM THE 20-NOVEMBER $2,831.50 - the first gain after four declines, inside the 2,830-2,850 Elliott zone, $60.00 BELOW the 2,894 weekly 61.8%; $176.50 BELOW the 02-January three-month official (year-to-date {ytd:+.2f}%). AVERAGE COLUMN: the completed October-2026 official three-month mean of ${oct_m:,.2f}; three-month sits ${abs(oct_m-m3):,.2f} "+("below" if m3<oct_m else "above")+" it."},
 {"name":"LME warehouse stock (t)","cur":stk,"prev":ps,"avg":oct_s,"note":VER+f" STOCK DOWN 2,125 t TO 221,400 t on 23-November - a third straight draw, 1,050 t above the 17-November series low (220,350 t). AVERAGE COLUMN: the October-2026 mean of {oct_s:,} tonnes; level about {oct_s-stk:,} tonnes below it."},
 {"name":"Cash-to-3M spread","cur":spr,"prev":psp,"avg":oct_sp,"note":VER+f" A $367.50 BACKWARDATION, UP FROM $353.00 ON 20-NOVEMBER - the widest in this series. CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. AVERAGE COLUMN: the October-2026 mean spread of ${oct_sp:,.2f}. On 23-November cash (+$17.00) and three-month (+$2.50) moved in the SAME direction, after opposite moves on 18, 19 and 20 November. REVERSAL CONDITION (a BACKWARDATION BEYOND $15.00 on a settled official): confirmed 23-October, lost 27-October, regained 28-October, lost 29-October, regained 30-October, held every session since - $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00, $353.00 and $367.50."},
 {"name":"EUR/USD LME fixing","cur":1.0946,"prev":1.0982,"avg":1.1465,"note":VER+" THE LME EURO FIXING WAS 1.09460 ON 23-NOVEMBER, DOWN FROM 1.09820 ON 20-NOVEMBER, with the dollar index near 104.2 (Trading Economics, 24-November). AVERAGE CAVEAT: this cell still carries the AUGUST-2026 mean (1.1465) because a full later-month fixing series was not available from the public source; it is labelled rather than estimated."},
]
d['outlook']['forward_path']=[
 {"tenor":"Cash (23-Nov official)","price":"3,201.5","basis":"THE MONDAY 23-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $3,201.50, UP $17.00 OR 0.53% (20-November $3,184.50). Next print Tuesday 24-November 13:20 London."},
 {"tenor":"3-month (23-Nov official)","price":"2,834.0","basis":"THE 23-NOVEMBER-2026 OFFICIAL THREE-MONTH OF $2,834.00, UP $2.50 - inside the 2,830-2,850 extended-(v) zone, $60.00 below the 2,894 weekly 61.8%."},
 {"tenor":"Cash-to-3M structure","price":"+367.5 (BACKWARDATION)","basis":"A $367.50 BACKWARDATION, up from $353.00 - the widest in this series; cash and three-month both rose, cash faster."},
 {"tenor":"Visible LME stock","price":"221,400 t","basis":f"DOWN 2,125 t on 23-November, a third straight draw; October mean {oct_s:,} t."},
]
d['outlook']['curve_note']=("PROMPT TIGHTER STILL - BACKWARDATION AT A NEW SERIES HIGH. On the 23-November official cash $3,201.50 sits $367.50 ABOVE three-month $2,834.00, a BACKWARDATION up from $353.00 (20-November) - the widest in this series. This time cash and three-month both rose (same direction), ending three sessions of opposite moves, but cash rose faster. "
 "CONVENTION: cash below three-month is CONTANGO; cash above three-month is BACKWARDATION. Since 16-September the sequence read backwardations of $21.00, $18.50 and $3.00, then eighteen contangos ($1.00 to $24.50), then backwardations of $4.50, $2.00, $7.00, $6.50, $6.50, $25.00, $25.00, $20.50, $14.00, $17.00, $7.00, $34.00, $35.00, $40.00, $61.00, $62.50, $67.00, $87.50, $110.00, $159.50, $123.50, $132.50, $312.00, $120.50, $230.00, $260.00, $353.00 and now $367.50. "
 f"READ: a twenty-eighth straight backwardation with visible stock drawing for a third session (221,400 t) - nearby metal is scarce while the forward prices a looser 2027 (Trading Economics cites forecasts of an 830 kt 2027 surplus; Emkay Global, via AL Circle, a ~400 kt deficit). The October mean spread was ${oct_sp:,.2f}; a contango beyond $24.50 would be the bearish structural confirmation.")
assert d['chart_price_axis']==[2700,3450] and d['chart_stock_axis']==[190000,255000]

ls=d['lme_series']; assert ls[-1][0]=='20-Nov' and len(ls)==15
d['lme_series']=ls[1:]+[["23-Nov",cash,m3,stk]]
assert [tuple(r[1:]) for r in d['lme_series'][-5:]]==[(3060.5,2940.0,220350),(3095.0,2865.0,226150),(3105.0,2845.0,224425),(3184.5,2831.5,223525),(cash,m3,stk)]
CU=(12165.0,12170.0,330975); NI=(15215.0,15380.0,274098); ZN=(3630.5,3488.0,144650); PB=(1788.0,1832.0,259675)
CU0=(12230.5,12237.0,332025); NI0=(15310.0,15490.0,275184); ZN0=(3670.0,3502.5,145675); PB0=(1825.0,1861.0,261525)
assert CU0[2]-1050==CU[2] and NI0[2]-1086==NI[2] and ZN0[2]-1025==ZN[2] and PB0[2]-1850==PB[2]
d['metals_board']=[
 {"name":"Aluminium","price":m3,"day":round((m3/pm-1)*100,2),"ytd":round(ytd,2)},
 {"name":"Copper","price":CU[1],"day":round((CU[1]/CU0[1]-1)*100,2),"ytd":round((CU[1]/12511-1)*100,2)},
 {"name":"Nickel","price":NI[1],"day":round((NI[1]/NI0[1]-1)*100,2),"ytd":round((NI[1]/16915-1)*100,2)},
 {"name":"Zinc","price":ZN[1],"day":round((ZN[1]/ZN0[1]-1)*100,2),"ytd":round((ZN[1]/3130.5-1)*100,2)},
 {"name":"Lead","price":PB[1],"day":round((PB[1]/PB0[1]-1)*100,2),"ytd":round((PB[1]/2008-1)*100,2)}]
mh=d['metals_history']; assert mh['labels'][-1]=='now'
mh['al'][-1]=round(mh['al'][-1]*m3/pm,1); mh['cu'][-1]=round(mh['cu'][-1]*CU[1]/CU0[1],1); mh['ni'][-1]=round(mh['ni'][-1]*NI[1]/NI0[1],1)
ms=d['metals_series']; R=ms['rows']
zn15=list(R['ZN']); pb15=list(R['PB'])   # = 02..20 November (15 sessions = November MTD)
mh['zn'][-1]=round(mh['zn'][-1]*((sum(zn15)+ZN[0])/16)/(sum(zn15)/15),1); mh['pb'][-1]=round(mh['pb'][-1]*((sum(pb15)+PB[0])/16)/(sum(pb15)/15),1)
for k,v in (('CU',CU[0]),('NI',NI[0]),('ZN',ZN[0]),('PB',PB[0])):
    assert len(R[k])==15; R[k]=R[k][1:]+[v]
ms['asof']='2026-11-23'
ms['basis']=("Last fifteen PUBLISHED LME official cash sessions per metal, ending MONDAY 23-NOVEMBER-2026. THE WINDOW ROLLED ONE SESSION THIS RUN: 02-November dropped, 23-November appended, so the window is 03-November to 23-November. Earlier points were asserted against the Westmetall per-metal tables on 21-November; the 23-November point is the official cash from the English and German overviews (which agree).")
ms['src']=["Westmetall - LME official cash settlements, English/German overviews (23-November-2026 session) and per-metal tables",W]
AVGNOTE=" AVERAGE COLUMN: the completed OCTOBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal tables). No reference or contract-for-difference mark is used in this panel."
def chg(a,b): return "unchanged" if a==b else f"{'up' if a>b else 'down'} ${abs(a-b):,.2f} or {abs(a/b-1)*100:.2f}%"
MD=[
 ("Copper",CU,f" COPPER 23-NOVEMBER: cash ${CU[0]:,.2f}, {chg(CU[0],CU0[0])} from 20-November; three-month ${CU[1]:,.2f}, {chg(CU[1],CU0[1])} - a new low for this window. STRUCTURE: a $5.00 CONTANGO (20-November $6.50). Stock fell 1,050 t to 330,975 t."),
 ("Nickel",NI,f" NICKEL 23-NOVEMBER: cash ${NI[0]:,.2f}, {chg(NI[0],NI0[0])}; three-month ${NI[1]:,.2f}, {chg(NI[1],NI0[1])}. CONTANGO $165.00 (20-November $180.00), still the widest carry on the board. Stock fell 1,086 t to 274,098 t."),
 ("Zinc",ZN,f" ZINC 23-NOVEMBER: cash ${ZN[0]:,.2f}, {chg(ZN[0],ZN0[0])}; three-month ${ZN[1]:,.2f}, {chg(ZN[1],ZN0[1])}. BACKWARDATION narrowed to $142.50 (20-November $167.50). Stock fell 1,025 t to 144,650 t. Zinc remains the strongest metal on this board year to date."),
 ("Lead",PB,f" LEAD 23-NOVEMBER: cash ${PB[0]:,.2f}, {chg(PB[0],PB0[0])}; three-month ${PB[1]:,.2f}, {chg(PB[1],PB0[1])}. CONTANGO $44.00 (20-November $36.00). Stock fell 1,850 t to 259,675 t."),
]
old={m['name']:m for m in d['metals_detail']}
CROSS=(f" CROSS-METAL 23-NOVEMBER: aluminium was the only board metal whose three-month rose (+0.09%); copper fell {abs(CU[1]/CU0[1]-1)*100:.2f}%, nickel {abs(NI[1]/NI0[1]-1)*100:.2f}%, zinc {abs(ZN[1]/ZN0[1]-1)*100:.2f}% and lead {abs(PB[1]/PB0[1]-1)*100:.2f}%; every board metal's LME stock fell. The dollar index was about 104.2 with a 25bp December Fed hike about 96% priced (Trading Economics). The LME euro fixing was 1.0946.")
d['metals_detail']=[{"name":n,"cash":c[0],"m3":c[1],"avg":old[n]['avg'],"src":VER+AVGNOTE+txt+f" October cash mean ${old[n]['avg']:,.2f}; cash sits ${abs(c[0]-old[n]['avg']):,.2f} "+("above" if c[0]>old[n]['avg'] else "below")+" it."+CROSS,"src_url":W} for (n,c,txt) in MD]

for i in d['inputs']:
    if i['name'].startswith('Copper'):
        assert i['hist'][-1][0]=='20-Nov' and len(i['hist'])==15
        i['hist']=i['hist'][1:]+[["23-Nov",CU[0]]]; assert i['hist'][0][0]=='03-Nov'
        assert [v for _,v in i['hist']]==R['CU']
        i['val']="~12,170.00 (3M); 12,165.00 (cash) $/t"; i['ratio']="~12,165.00 $/t cash vs LME 3M 12,170.00 $/t"; i['trend']='down'
        i['src']=("LME official cash settlement, rolled ONE SESSION to the MONDAY 23-NOVEMBER-2026 session at $12,165.00 (20-November $12,230.50). 02-November dropped and 23-November appended, so the series is the last fifteen published official cash sessions, 03-November to 23-November - the same window as the LME Board sparklines. Official settlement only, from the Westmetall English/German overviews and per-metal table. "
                  "Copper structure for context: a $5.00 contango on 23-November; stock 330,975 t (-1,050 t).")
d['inputs_summary']=("UPDATE 24-NOVEMBER: Copper rolled one session to the Monday 23-November LME official cash of $12,165.00 (window 03-November to 23-November). No new carbon, fluoride, silicon or magnesium mark was located this run, so those series are unchanged (gaps stay gaps). Energy: Brent fell to a three-month low on 23-November and was about $88.8 on 24-November (Trading Economics) on US-Iran diplomacy signals. "+d['inputs_summary'])

tl=0.5*cash; resid=2403-tl; share=tl/2403*100
NC1="COMPILED MONDAY 23-NOVEMBER-2026 BEFORE THE RING (LME BOARD CARRIED ON THE FRIDAY 20-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION, RE-VERIFIED THIS RUN; MONDAY'S OFFICIAL PRINTS 13:20 LONDON)."
NC2="COMPILED TUESDAY 24-NOVEMBER-2026 BEFORE THE RING (LME BOARD ROLLED TO THE MONDAY 23-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION)."
REPL=[
 ("0.50 times the 20-November official cash of $3,184.50, or $1,592.25, UP $44.75 against the 18-November figure used previously",f"0.50 times the 23-November official cash of $3,201.50, or ${tl:,.2f}, UP ${tl-1592.25:,.2f} against the 20-November figure used previously"),
 ("residual market leg of $810.75, so 66.3%",f"residual market leg of ${resid:,.2f}, so {share:.1f}%"),
 ("0.50 times the 20-November official cash of $3,184.50, or $1,592.25, leaving a $810.75 residual market leg out of the $2,403/t US duty-paid premium (66.3%",f"0.50 times the 23-November official cash of $3,201.50, or ${tl:,.2f}, leaving a ${resid:,.2f} residual market leg out of the $2,403/t US duty-paid premium ({share:.1f}%"),
 ("$1,592.25 on 20-November cash, 66.3%",f"${tl:,.2f} on 23-November cash, {share:.1f}%"),
 ("THE RATIO: LME Alumina at $398.24/t against the 20-November aluminium three-month of $2,831.50 is 14.06%",f"THE RATIO: LME Alumina at $398.24/t against the 23-November aluminium three-month of $2,834.00 is {398.24/m3*100:.2f}%"),
 ("REVIEWED 23-NOVEMBER: no newer public disclosure","REVIEWED 24-NOVEMBER: no newer public disclosure"),
 ("REVIEWED 23-NOVEMBER. NO NEW DATED","REVIEWED 24-NOVEMBER. NO NEW DATED"),
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
assert "$1,592.25" not in blob and "MONDAY 23-NOVEMBER-2026 BEFORE THE RING" not in blob, [blob.count("$1,592.25")]

d['lme_commentary']=("NEW SERIES-WIDE BACKWARDATION AS STOCKS DRAW AGAIN. On Monday 23-November cash rose $17.00 to $3,201.50 and three-month $2,50 to $2,834.00 - the first three-month gain after four declines and the only rise among board metals - widening the backwardation to $367.50, the widest in this series. Three-month holds inside the 2,830-2,850 Elliott completion zone, $60.00 below the 2,894 weekly 61.8%. Visible stock fell 2,125 t to 221,400 t, a third straight draw. "
 "Macro stays the headwind - the dollar index near 104.2 with a 25bp December hike about 96% priced - while energy eased: Brent fell to a three-month low on US-Iran diplomacy signals (Trading Economics). Trading Economics cites forecasts of an 830 kt 2027 surplus, while Emkay Global (via AL Circle) sees a ~400 kt deficit in 2027 and 2028 - the forecasts disagree. "
 f"October's official means were cash ${oct_c:,.2f} and three-month ${oct_m:,.2f}; three-month now sits ${abs(oct_m-m3):,.2f} below its October mean.").replace("$2,50 ","$2.50 ")
d['net_read']=("NET: BEARISH ON THE FORWARD, TIGHT ON THE PROMPT. Against: three-month at $2,834.00 stays below the 2,894 weekly 61.8%; a hawkish Fed (December hike ~96% priced) and a firm dollar; forecasts of a 2027 surplus as Chinese output tops 46 Mt and Gulf metal returns; copper at a fresh window low; Brent at a three-month low lowers the energy-cost floor. "
 "Supportive: a $367.50 backwardation (the widest in this series, twenty-eighth straight), stock drawing for a third session to 221,400 t, Hormuz still closed with 72 vessels holding, and Emkay Global's view of a ~400 kt deficit through 2028.")
d['bottom_line']=("BOTTOM LINE: Monday's official held the forward inside the completion zone - three-month $2,834.00 (+$2.50), cash $3,201.50 (+$17.00), a $367.50 backwardation, the widest in this series - and visible stock drew for a third session to 221,400 t. "
 "Weights held at 10% bull / 35% base / 55% bear. A settled close below about 2,803 would force a wave re-label; back above 2,994.50 would signal a failed break; above 3,097.50 negates the count; daily invalidation 3,289. Next print Tuesday 24-November 13:20 London.")
c2=d['commercial']
a0=c2.find("FIRST, THE CURVE STEEPENS AGAIN - PROMPT TIGHT, FORWARD WEAK:"); a1=c2.find("SECOND,",a0); assert a0>=0 and a1>a0
c2=c2[:a0]+"FIRST, THE CURVE STEEPENS AGAIN - PROMPT TIGHT, FORWARD WEAK: the backwardation widened to $367.50 on 23-November (from $353.00) as cash rose to $3,201.50 and three-month only edged up to $2,834.00, still below the 2,894 weekly 61.8%; nearby metal commands the largest premium over forward metal in this series, so there is no carry reward for holding stock - and visible LME stock drew for a third session to 221,400 t. "+c2[a1:]
b0=c2.find("FOURTH, WATCH THE CALENDAR: "); b1=c2.find("; the dollar index near",b0); assert b0>=0 and b1>b0
c2=c2[:b0]+"FOURTH, WATCH THE CALENDAR: the 23-November official left three-month at $2,834.00, inside the 2,830-2,850 Elliott zone, while cash rose to $3,201.50; a 25bp December Fed hike is about 96% priced (Trading Economics 24-November); first Q1-2027 Japanese premium offers, which typically emerge from late November (none located yet)"+c2[b1:]
d['commercial']=c2

for s in d['outlook']['scenarios']:
    assert s['prob']=={'Bull':'10%','Base':'35%','Bear':'55%'}[s['case']]
    s['drivers']=("HELD 24-NOVEMBER AT 10/35/55: the 23-November official left three-month at $2,834.00 (+$2.50), inside 2,830-2,850; no pre-registered trigger was hit (a settled close below about 2,803 adds bear weight; back above 2,994.50 returns weight to base). ")+s['drivers']
d['outlook']['scenario_paths']['bull'][0]=m3; d['outlook']['scenario_paths']['base'][0]=m3; d['outlook']['scenario_paths']['bear'][0]=m3

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('THE CONTANGO RISK'):
        r['risk']+=" UPDATE 24-NOVEMBER: the 23-November official printed a $367.50 backwardation - a new series high and a seventeenth session above $15.00. Contango risk remains remote near term. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE STOCK DRAWDOWN'):
        r['risk']+=" UPDATE 24-NOVEMBER: a third straight draw - LME stock fell 2,125 t to 221,400 t on 23-November, 1,050 t above the 17-November series low. Trend held at FLAT pending a break of that low."; r['trend']='flat'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 24-NOVEMBER: Brent fell to a three-month low on 23-November and was about $88.8 on 24-November (Trading Economics) on US-Iran diplomacy signals, lowering the energy-cost floor further. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 24-NOVEMBER: Straits Daily Brief - still CLOSED; latest IMF PortWatch count still 2 transits on 15-November; AIS-visible vessels holding rose to 72 (from 62). New Iranian state-media claims that three tankers caught fire after striking mines remain UNCONFIRMED by any maritime authority; Gulf News reports a search for a missing sailor after a tanker attack. The US Treasury announced new sanctions on financial networks linked to Iran's tanker fleet; Trading Economics notes Iran wants the US naval blockade and sanctions lifted before fully reopening the Strait. No reopening agreement. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 24-NOVEMBER: markets assign about 96% probability to a 25bp December hike and expect another in January; dollar index about 104.23 (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
assert hit==5,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Mon 23-Nov':
        hc+=1; cat['date']='Daily, from Tue 24-Nov'
        cat['event']=("MONDAY 23-NOVEMBER OFFICIAL: three-month $2,834.00 (+$2.50), inside the 2,830-2,850 extended-(v) zone and below the 2,894 weekly 61.8%; cash $3,201.50; backwardation $367.50 (series widest); stock 221,400 t (third draw). NEXT: Tuesday 24-November official (13:20 London) - a settled close below about 2,803 forces a wave re-label and adds bear weight; back above 2,994.50 signals a failed break; above 3,097.50 negates the count; invalidation 3,289. The December Fed meeting (25bp ~96% priced); any official US-Canada tariff announcement; first Q1-2027 Japanese premium offers (none located yet; S&P Global reported participant expectations of $190-200/t).")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"TUESDAY 24-NOVEMBER ON THE MONDAY 23-NOVEMBER OFFICIAL: cash rose $17.00 to $3,201.50 and three-month $2.50 to $2,834.00 - the first forward gain after four declines and the only rise on the base-metals board - widening the backwardation to $367.50, the widest in this series. Visible stock drew for a third session to 221,400 t. Brent fell to a three-month low on US-Iran diplomacy signals even as vessels holding near Hormuz rose to 72 and the US added Iran tanker-finance sanctions. The forward stays inside the 2,830-2,850 Elliott zone; weights held at 10/35/55.")

st=d['ew']['short_term']; nx=st['now_x']
for k in ('bull','base','bear'): st['proj'][k][0]=[nx,m3]
lt=d['ew']['long_term']
for k in ('bull','base','bear'):
    if lt['proj'][k] and lt['proj'][k][0][0]==lt['now_x']: lt['proj'][k][0]=[lt['now_x'],m3]
EWP=("REVIEWED 24-NOVEMBER ON THE 23-NOVEMBER OFFICIAL - COUNT HELD: three-month settled 2,834.00 (+2.50), still inside the 2,830-2,850 completion zone; the small gain is not a confirmed reversal, so no new pivot is added and the wave (v) low remains unconfirmed. Base case, alternates, probabilities and invalidation levels are unchanged from the 21-November review below. ")
EWL=("REVIEWED 24-NOVEMBER: three-month 2,834.00 remains below the 2,894 weekly 61.8%; weekly count, alternate weighting and invalidation unchanged from the 21-November review below. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 23-NOVEMBER'),k
    w=w.split("Monday's official is the next test. ",1)[1] if "Monday's official is the next test. " in w else w
    d['ew'][k]['writeup']=pfx+w
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="88.8",day="about $88.79 on 24-November (-0.65%, Trading Economics) after falling sharply to a three-month low on 23-November; Straits Daily Brief $89.49 (-2.59%) at 23:40 UTC 23-November",
 note="REFRESHED TUESDAY 24-NOVEMBER-2026 (Trading Economics): pressured by signs of renewed US-Iran diplomacy; Iran wants the US naval blockade and sanctions lifted before fully reopening Hormuz, and Hormuz crude flows have fallen this month. Levels approximate. SOURCE: "+S_BR)
M['US dollar index (DXY)'].update(value="104.23",day="about 104.23 on 24-November (-0.08%, Trading Economics)",
 note="REFRESHED TUESDAY 24-NOVEMBER-2026 (Trading Economics): markets assign about 96% probability to a 25bp December hike and expect another in January. SOURCE: "+S_TD)
M['EUR/USD'].update(value='1.09460',day="LME fixing on 23-November, down from 1.09820 on 20-November",note="REFRESHED TUESDAY 24-NOVEMBER-2026 to the 23-November LME fixing via Westmetall, the same session as the LME board.")

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE MONDAY 23-NOVEMBER-2026 LME OFFICIAL, the latest published session. THIS TUESDAY 24-NOVEMBER RUN IS COMPILED AT ABOUT 02:35 LONDON, BEFORE TODAY'S RING; Tuesday's official prints at 13:20 London, so Monday's official is the correct latest figure. The board rolled ONE session this run. Nothing was estimated or taken intraday. The Trading Economics aluminium reference (about $2,866.70, +0.95% for 23-November) is a CFD reference cited in text only.")
C[1]=("SOURCE CHECK THIS RUN (24-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on every price, stock and FX figure for the 23-November session (aluminium cash 3,201.50, three-month 2,834.00, stock 221,400; copper 12,165.00/12,170.00; nickel 15,215.00/15,380.00; zinc 3,630.50/3,488.00; lead 1,788.00/1,832.00; EUR/USD MTLE 1.09460); the aluminium per-metal daily table shows 23-November as its newest row.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 17- to 20-November rows match the stored series; the copper, nickel, zinc and lead per-metal tables were not re-fetched this run - their 03- to 20-November points were asserted against those tables on 21-November and the 23-November point comes from the two agreeing overviews; each metal's 23-November stock change (German overview change column) reconciles exactly with the stored 20-November stock.")
C[3]=("STOCK CHANGES 23-November: aluminium -2,125 to 221,400 (third straight draw); copper -1,050 to 330,975; nickel -1,086 to 274,098; zinc -1,025 to 144,650; lead -1,850 to 259,675; tin -50 to 3,670.")
c4=C[4]
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (23-November) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. LME average columns are the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oct_c:,.2f}, three-month ${oct_m:,.2f}, stock {oct_s:,} t, spread ${oct_sp:,.2f}; copper $14,532.48, nickel $15,470.00, zinc $3,820.43, lead $1,861.52. The EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the November month-to-date cash average (sixteen sessions, 02-23 November) as their latest point. "
 "The price chart axis (floor 2,700, ceiling 3,450) brackets cash 3,201.50 and three-month 2,834.00 ($134.00 above the floor; it will be lowered if three-month approaches 2,750); the stock chart axis floor of 190,000 t leaves 31,400 t headroom below visible stock of 221,400 t; both are re-checked each run.")
C[5]="SPREAD CONVENTION, STATED EVERY RUN BECAUSE IT IS THE MOST MISREAD FIGURE ON THE PAGE: cash ABOVE three-month is BACKWARDATION; cash BELOW three-month is CONTANGO. Cash $3,201.50 against three-month $2,834.00 is therefore a $367.50 BACKWARDATION, up from $353.00 on 20-November. On 23-November cash and three-month moved in the SAME direction (both up) after opposite moves on 18-20 November. Press figures for the spread differ by measure and time; the dashboard uses the settled officials only."
hit=0
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $88.8) and the dollar index (about 104.23) are Trading Economics readings for 24-November; TTF (about EUR 88.45/MWh) and the US ten-year row are CARRIED from earlier sessions (not re-fetched). Trading Economics prices are contract-for-difference references, not official benchmarks, so levels are approximate. The Straits Daily Brief (24-November) shows Brent $89.49 at 23:40 UTC 23-November; its incident items this run are Iranian state-media claims or single-source media reports - none is maritime-authority-confirmed."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 24-NOVEMBER (TUESDAY, PRE-RING): no authorised fetch was blocked. Westmetall EN and DE overviews and the aluminium per-metal table, Trading Economics aluminium/Brent/dollar, AL Circle news and the Straits Daily Brief (24-November) were fetched. A WebSearch for Q1-2027 Japanese premium offers located none; the latest public reference remains S&P Global's report of participant expectations of $190-200/t for Q1 talks - an expectation, not an offer. A search for dated smelter news from 23-November located nothing new."); hit+=1
assert hit==2,hit

d['so_what']={"line":"LME aluminium's prompt squeeze tightened again on Monday: cash rose to $3,201.50 while three-month only edged up to $2,834.00, taking the backwardation to a series-high $367.50 as LME stocks drew for a third session - the forward is still pinned near $2,800-2,850 support.",
 "points":[
 "WHAT MOVED: on the 23-November official cash rose $17.00 to $3,201.50 and three-month $2.50 to $2,834.00 - aluminium was the only base metal on the board whose three-month rose. The backwardation (cash above three-month) widened to $367.50 and visible LME stock fell 2,125 t to 221,400 t, near the 17-November low.",
 "WHY IT MATTERS: nearby metal is scarce while the forward prices a looser 2027 and a hawkish Fed (25bp December hike about 96% priced); the steep curve gives no reward for holding stock and keeps the prompt sensitive to any supply shock.",
 "48H DEVELOPMENTS: vessels holding near Hormuz rose to 72 and the US added sanctions on Iran's tanker-finance networks; new Iranian claims of mine strikes remain unconfirmed. Brent nonetheless fell to a three-month low (about $88.8) on signs of US-Iran diplomacy, easing smelter energy-cost pressure. India opened an anti-dumping probe into aluminium imports from China, Malaysia, Vietnam and Thailand.",
 "WHAT TO WATCH: Tuesday's official against $2,800-2,850 (a settle below about $2,803 opens a deeper leg), whether stocks break the 220,350 t low, any US-Iran talks on Hormuz, and first Q1-2027 Japanese premium offers (none reported; earlier talk $190-200/t)."]}

d['feed']=([
 {"when":"Mon 23-Nov","impact":"Mixed","text":"23-NOVEMBER OFFICIAL: three-month $2,834.00 (+$2.50); cash $3,201.50 (+$17.00); backwardation $367.50, widest in series; stock -2,125 t to 221,400 t."},
 {"when":"Tue 24-Nov","impact":"Bullish","text":"HORMUZ: vessels holding rise to 72; US Treasury sanctions Iran tanker-finance networks; Iranian claims of three tankers on fire after mine strikes unconfirmed (Straits brief 24-Nov)."},
 {"when":"Mon 23-Nov","impact":"Bearish (cost)","text":"ENERGY: Brent falls to a three-month low on US-Iran diplomacy signals; ~$88.8 on 24-Nov (Trading Economics)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bullish","url":W,
  "headline":"LME ALUMINIUM BACKWARDATION HITS A SERIES-HIGH $367.50 AS STOCKS DRAW AGAIN. The Monday 23-November official put cash at $3,201.50 (+$17.00) and three-month at $2,834.00 (+$2.50) - aluminium was the only base metal whose three-month rose (copper -0.55%, nickel -0.71%, zinc -0.41%, lead -1.56%). Visible stock fell 2,125 t to 221,400 t, a third straight draw; three-month stays inside the 2,830-2,850 Elliott zone."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ: VESSELS HOLDING RISE TO 72; NEW US SANCTIONS (Straits Daily Brief, 24-November): the Strait is listed as closed with 72 AIS-visible vessels holding (from 62); latest IMF PortWatch count 2 transits on 15-November vs 85/day pre-crisis. Iranian state media claim three tankers caught fire after striking mines - unconfirmed by any maritime authority. The US Treasury announced sanctions on financial networks linked to Iran's tanker fleet."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bearish (cost)","url":S_BR,
  "headline":"BRENT AT A THREE-MONTH LOW ON US-IRAN DIPLOMACY SIGNALS (Trading Economics, 24-November): Brent traded below $90, about $88.79, after a sharp fall on 23-November; Iran wants the US naval blockade and sanctions lifted before fully reopening Hormuz - lower oil eases smelter energy and freight cost pressure."},
 {"theme":"Policy","horizon":"0-6 months","impact":"Mixed","url":S_IN,
  "headline":"INDIA OPENS ALUMINIUM ANTI-DUMPING PROBE (AL Circle, 19-November): India's trade remedies authority opened an investigation into aluminium imports from China, Malaysia, Vietnam and Thailand, potentially affecting about 228 domestic manufacturers - a possible further redirection of Asian semi-finished flows."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"FED DECEMBER HIKE ~96% PRICED (Trading Economics, 24-November): the dollar index was about 104.23; markets assign about 96% probability to a 25bp December rate hike and expect another in January."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])
for p in d['producer_status']: p['asof']=RD

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 23-Nov-2026 session (EN and DE overviews agree; Al per-metal table newest row 23-Nov)",W])
for x in ([L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_TE,S_TE],[L_IN,S_IN]): d['sources'].append(x)
for x in ([L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_IN,S_IN]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-20',3184.5,2831.5,223525]
ph['rows'].append(['2026-11-23',cash,m3,stk]); ph['updated']=RD   # new week (w/c 23-Nov)
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',tl,resid,round(share,1),mh['al'][-1],mh['cu'][-1],mh['ni'][-1],mh['zn'][-1],mh['pb'][-1],d['metals_board'])
