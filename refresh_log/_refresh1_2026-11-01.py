# Daily data refresh - 2026-11-01 (SUNDAY, ~02:40 UTC). Board CARRIED on the FRIDAY 30-Oct LME official (no ring Sat/Sun).
# Westmetall cache-busted EN + DE overviews re-fetched: both show the 30-Oct session (Al cash 3,114 / 3M 3,080 / stock 231,200; MTLE 1.11770).
# Al, Cu, Ni per-metal tables: newest row 30-Oct, NO later row; all 22 October sessions listed.
# MONTH ROLL: October is complete (22 sessions) -> every prior-month average rolls from SEPTEMBER to the completed OCTOBER-2026 official means.
import json,re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-01'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-01"; L_ST="Straits Daily Brief - Strait of Hormuz, 01-Nov-2026"
S_WF="https://www.alcircle.com/news/jiaozuo-wanfang-s-profits-nearly-double-hitting-263m-in-nine-months-121775"; L_WF="AL Circle - JiaoZuo WanFang nine-month net profit nearly doubles (31-Oct-2026)"
S_BE="https://www.alcircle.com/news/aluminium-bears-may-be-getting-it-wrong-as-prices-target-3-625-in-2027-121781"; L_BE="AL Circle - Aluminium bears may be getting it wrong as prices target $3,625 in 2027 (31-Oct-2026)"
S_AW="https://www.alcircle.com/news/europes-9m-2026-aluminium-production-jumps-to-5-56mt-as-smelter-restarts-gain-ground-121723"; L_AW="AL Circle - Europe's 9M-2026 aluminium production 5.56 Mt as restarts gain ground (28-Oct-2026)"

# ---------- October-2026 official means (Westmetall per-metal tables, 22 sessions 01-30 Oct) ----------
AL=[(3114.00,3080.00,231200),(3071.00,3064.00,231675),(3101.00,3084.00,231900),(3078.00,3064.00,232100),(3047.50,3027.00,234050),(3043.00,3018.00,235800),(3033.00,3008.00,236025),(3031.00,3024.50,236125),(3003.50,2997.00,236225),(3019.00,3012.00,236375),(3014.00,3012.00,237875),(2999.00,2994.50,238125),(3010.00,3013.50,238375),(3036.00,3037.00,238625),(3055.00,3060.00,238625),(3055.50,3070.00,238875),(3060.50,3069.00,238875),(3102.50,3114.00,238875),(3134.50,3148.50,238875),(3107.00,3118.00,240375),(3109.50,3122.00,240375),(3120.00,3131.00,240625)]
CUo=[14449.00,14560.00,14675.50,14625.00,14500.00,14415.00,14215.00,14441.00,14540.00,14496.00,14595.00,14539.00,14751.00,14741.00,14822.00,14689.00,14526.00,14510.00,14505.00,14430.00,14355.00,14335.00]
NIo=[15240.00,15360.00,15580.00,15440.00,15535.00,15695.00,15935.00,15830.00,15350.00,15275.00,15170.00,14885.00,15475.00,15445.00,15515.00,15545.00,15415.00,15645.00,15530.00,15470.00,15435.00,15570.00]
ZNo=[3834.0,3798.0,3774.0,3803.0,3799.0,3781.0,3840.0,3811.0,3821.0,3803.0,3724.0,3739.0,3776.0,3736.0,3771.0,3727.0,3790.0,3900.0,3927.0,3960.0,3980.0,3955.5]
PBo=[1837.0,1827.0,1829.5,1837.5,1844.5,1833.0,1847.0,1842.0,1860.0,1866.0,1853.0,1854.0,1856.0,1851.0,1880.0,1872.0,1886.0,1900.0,1900.0,1910.0,1878.0,1890.0]
for L in (AL,CUo,NIo,ZNo,PBo): assert len(L)==22
# cross-check the per-metal tables against the stored 15-session windows (12-Oct..30-Oct)
R=d['metals_series']['rows']
assert R['CU']==list(reversed(CUo[:15])), 'CU window mismatch'
assert R['NI']==list(reversed(NIo[:15])), 'NI window mismatch'
assert [r[1] for r in d['lme_series']]==[a[0] for a in reversed(AL[:15])], 'AL window mismatch'
mean=lambda x: round(sum(x)/len(x),2)
oc=mean([a[0] for a in AL]); om=mean([a[1] for a in AL]); os_=int(round(sum(a[2] for a in AL)/22)); osp=mean([a[0]-a[1] for a in AL])
ocu,oni,ozn,opb=mean(CUo),mean(NIo),mean(ZNo),mean(PBo)
print('Oct means',oc,om,os_,osp,ocu,oni,ozn,opb)
B={b['name']:b for b in d['benchmark']}
sep_c=B['LME Cash settlement']['avg']; sep_m=B['LME 3-month']['avg']; sep_s=B['LME warehouse stock (t)']['avg']; sep_sp=B['Cash-to-3M spread']['avg']
cash,m3,stk,spr=3114.0,3080.0,231200,34.0
assert B['LME Cash settlement']['cur']==cash and B['LME 3-month']['cur']==m3

OLDVER_END="prior-month averages remain the completed SEPTEMBER-2026 official means (October's means complete with this session and roll in on the first November run)."
NEWVER_END=("THE MONTH HAS ROLLED: every prior-month average on this page now uses the COMPLETED OCTOBER-2026 official means (22 sessions, 01- to 30-October, recomputed from the Westmetall per-metal tables). "
 "RE-CHECKED SUNDAY 01-NOVEMBER-2026: the cache-busted Westmetall English and German overviews still show the 30-October session with identical figures and the aluminium, copper and nickel per-metal tables show NO row after 30-October, so the board is CARRIED through the weekend because the market is shut; the next official prints Monday 02-November 13:20 London.")
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("COMPILED SATURDAY 31-OCTOBER-2026. THERE IS NO LME RING ON SATURDAY,","COMPILED SUNDAY 01-NOVEMBER-2026. THERE IS NO LME RING ON SATURDAY OR SUNDAY,")
        o=o.replace("COMPILED SATURDAY 31-OCTOBER-2026 (NO RING ON SATURDAY)","COMPILED SUNDAY 01-NOVEMBER-2026 (NO RING AT WEEKENDS)")
        o=o.replace(OLDVER_END,NEWVER_END)
        o=o.replace("REVIEWED 31-OCTOBER: no newer public disclosure","REVIEWED 01-NOVEMBER: no newer public disclosure").replace("REVIEWED 31-OCTOBER. NO NEW DATED","REVIEWED 01-NOVEMBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status'):
    d[k]=walk(d[k])
assert all(NEWVER_END in k['delta'] for k in d['kpi_cards'])

# KPI average sentences
K=d['kpi_cards']
K[2]['delta']=re.sub(r"The September mean spread was \$[0-9.,-]+\.", f"The completed October mean spread was a ${osp:,.2f} backwardation (September ${sep_sp:,.2f}).",K[2]['delta'])
K[3]['delta']=K[3]['delta'].replace(f"September's mean stock was {sep_s:,} tonnes.",f"October's mean stock was {os_:,} tonnes (September {sep_s:,}); visible stock sits about {os_-stk:,} t below the October mean.")
assert f"{os_:,} tonnes" in K[3]['delta'] and "completed October mean spread" in K[2]['delta']

# Benchmark: roll avg + rewrite the average sentence
def rep_avg(note,new):
    i=note.find(" AVERAGE COLUMN"); assert i>0; return note[:i]+new
bc=B['LME Cash settlement']; bc['avg']=oc
bc['note']=rep_avg(bc['note'],f" AVERAGE COLUMN ROLLED from the September mean (${sep_c:,.2f}) to the completed OCTOBER-2026 official cash mean of ${oc:,.2f} (22 sessions); Friday's cash of $3,114.00 sits ${cash-oc:,.2f} ABOVE it - the month closed near its high after a mid-month low of $2,999.00 (15-October).")
bm=B['LME 3-month']; bm['avg']=om
bm['note']=rep_avg(bm['note'],f" AVERAGE COLUMN ROLLED from the September mean (${sep_m:,.2f}) to the completed OCTOBER-2026 official three-month mean of ${om:,.2f}; three-month sits ${m3-om:,.2f} above it. October's three-month range was 2,994.50 (15-October) to 3,148.50 (06-October).")
bs=B['LME warehouse stock (t)']; bs['avg']=os_
bs['note']=rep_avg(bs['note'],f" AVERAGE COLUMN ROLLED from the September mean ({sep_s:,} t) to the October-2026 mean of {os_:,} tonnes; the level is about {os_-stk:,} t below it, and stock fell every week in October (240,625 t on 01-October to 231,200 t on 30-October, -9,425 t).")
bp=B['Cash-to-3M spread']; bp['avg']=osp
i=bp['note'].find(" AVERAGE COLUMN"); j=bp['note'].find(" Cash rose $43.00",i); assert i>0 and j>i
bp['note']=bp['note'][:i]+f" AVERAGE COLUMN ROLLED from the September mean (${sep_sp:,.2f}) to the October-2026 mean spread of ${osp:,.2f} ({'backwardation' if osp>0 else 'contango'} on average; the month opened in contango and closed in a $34.00 backwardation)."+bp['note'][j:]
be=B['EUR/USD LME fixing']
be['note']=be['note'].replace("this cell still carries the AUGUST-2026 mean (1.1465) because a full September fixing series was not available from the public source","this cell still carries the AUGUST-2026 mean (1.1465) because full September and October fixing series were not available from the public source")
d['outlook']['forward_path'][3]['basis']=f"DOWN 475 t to a new series low on 30-October; October mean {os_:,} t (September {sep_s:,} t)."

# metals_detail avg roll
OAV={'Copper':ocu,'Nickel':oni,'Zinc':ozn,'Lead':opb}
for m in d['metals_detail']:
    sa=m['avg']; m['avg']=OAV[m['name']]
    s=m['src']
    s=s.replace(" AVERAGE COLUMN: the completed SEPTEMBER-2026 mean of official cash (22 sessions, from the Westmetall per-metal table)."," AVERAGE COLUMN ROLLED THIS RUN: it is now the completed OCTOBER-2026 mean of official cash (22 sessions, 01- to 30-October, from the Westmetall per-metal table).")
    old=f" September cash mean ${sa:,.2f}."; assert old in s,(m['name'])
    s=s.replace(old,f" October cash mean ${OAV[m['name']]:,.2f} (September ${sa:,.2f}); Friday's cash sits ${abs(m['cash']-OAV[m['name']]):,.2f} {'above' if m['cash']>OAV[m['name']] else 'below'} it.")
    assert "OCTOBER-2026 mean" in s; m['src']=s

# curve note / commentary average sentences
cn=d['outlook']['curve_note']; o=f"The September mean spread was ${sep_sp:,.2f};"; assert o in cn
d['outlook']['curve_note']=cn.replace(o,f"The completed October mean spread was ${osp:,.2f} (September ${sep_sp:,.2f});")
lc=d['lme_commentary']; o=f"September's official means were cash ${sep_c:,.2f} and three-month ${sep_m:,.2f}."; assert o in lc
d['lme_commentary']=lc.replace(o,f"October's completed official means were cash ${oc:,.2f} and three-month ${om:,.2f} (September ${sep_c:,.2f} / ${sep_m:,.2f}), so the month closed above its average after a mid-month low.")

# ---------- caveats ----------
C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 30-OCTOBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND BECAUSE THE MARKET IS SHUT (no ring Saturday or Sunday); this Sunday 01-November run changes no board price, stock or FX figure. The next official prints Monday 02-November at 13:20 London. Reference prices (Trading Economics CFD, AL Circle's $3,076.8 price note) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (01-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and still show the 30-October session with identical prices, stocks and FX fixings (EUR/USD MTLE 1.11770), and the aluminium, copper and nickel per-metal daily tables show NO row after 30-October (aluminium cash 3,114.00, three-month 3,080.00, stock 231,200), so the carried board is complete rather than lagging.")
C[2]=("COMPENSATING CHECKS: the per-metal tables' last fifteen October rows match the stored fifteen-session windows exactly (aluminium cash, copper cash, nickel cash), and the overviews' prior-day FX column (MTLE 1.11280) matches the verified 29-October board.")
C[4]=(f"THE WHOLE BOARD SITS ON ONE UNIFORM SESSION (30-October) AND NO INTRADAY OR UNOFFICIAL MARK IS USED IN IT. THE MONTH HAS ROLLED: LME averages are now the completed OCTOBER-2026 official means (22 sessions) - aluminium cash ${oc:,.2f}, three-month ${om:,.2f}, stock {os_:,} t, spread ${osp:,.2f}; copper ${ocu:,.2f}, nickel ${oni:,.2f}, zinc ${ozn:,.2f}, lead ${opb:,.2f} - recomputed from the Westmetall per-metal tables; the EUR/USD average cell still carries the August mean and is labelled as such. Zinc and lead in the history chart use the completed October cash average as their latest point until the first November session. The price chart axis (floor 2,900) brackets three-month at 3,080.00; the stock chart axis floor of 220,000 t leaves about 11,200 t of headroom below visible stock at 231,200 t and will be re-checked each run.")
hit=0
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=cv+" These are the FRIDAY 30-OCTOBER readings carried through the weekend (no new session); the Straits Daily Brief (01-November) independently shows Brent settled at $113.43 (+2.37%) and WTI $104.12 on the latest session."; hit+=1
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 01-NOVEMBER: no authorised fetch was blocked (Westmetall EN, DE and aluminium/copper/nickel per-metal pages, AL Circle, news.metal.com and the Straits Daily Brief all fetched). The Hormuz items in the 01-November brief are labelled by the brief itself as AI-assisted with degraded live feeds; Iranian mine/tanker-fire claims and the reported offer to reopen the strait on seven conditions are UNCONFIRMED by any maritime authority or major wire and are cited as claims only. Chalco's Q3-2026 report was again searched for and not located; no figure is published for it."); hit+=1
    if cv.startswith("PEER EARNINGS:"):
        C[i]="PEER EARNINGS: ONE NEW RESULT ADDED THIS RUN - JiaoZuo WanFang nine-month 2026 (AL Circle, 31-October). It was not added to the per-company history strips because the source gives only cumulative nine-month figures (no quarterly series); gaps are left as gaps. Yunnan Aluminium and AMAG (added 31-October) are likewise nine-month-only. Chalco Q3-2026 remains pending."; hit+=1
assert hit==3,hit

# ---------- so what ----------
d['so_what']={"line":"Weekend check: aluminium starts November above its $3,077 pivot after a month that ended near its high - Friday's $3,080 three-month is $"+f"{m3-om:,.0f}"+" above October's average, with a $34 backwardation and record-low LME stock - while Hormuz stays effectively closed and oil holds above $113.",
 "points":[
 f"WHERE IT STANDS: the board is Friday's 30-October LME official - cash $3,114.00 and three-month $3,080.00, a $34.00 backwardation (cash above three-month) and LME stock at a new low of 231,200 t. Nothing trades on the LME until Monday's 13:20 London official.",
 f"OCTOBER IN NUMBERS: the month's official averages were cash ${oc:,.2f} and three-month ${om:,.2f}, both well below September's (${sep_c:,.0f} / ${sep_m:,.0f}); three-month made its low of $2,994.50 on 15-October and recovered $85.50 into month-end, while LME stock fell about 9,400 t over the month.",
 "WHY IT MATTERS: prompt metal is scarce on the LME and energy costs keep rising - the Strait of Hormuz remains effectively closed to commercial traffic (2 transits on 25-October vs an 85/day baseline; a record 35 attacks on ships reported in October) and Brent settled at $113.43 (Straits Daily Brief). Chinese smelter profits are surging (JiaoZuo WanFang nine-month profit +93.5%, Yunnan Aluminium +164%).",
 "WHAT TO WATCH: Monday's official - a second close above $3,077 with the backwardation above $15 would strengthen the bullish case, a close below $3,061.5 would weaken it; Chalco's Q3 report (still not located); any verified change in Hormuz traffic (Iran's reported reopening conditions are unconfirmed)."]}

d['feed']=([
 {"when":"Sun 01-Nov","impact":"Mixed","text":"BOARD CARRIED ON THE FRIDAY 30-OCTOBER LME OFFICIAL (NO RING AT WEEKENDS): cash $3,114.00, three-month $3,080.00, backwardation $34.00, stock 231,200 t. Westmetall EN/DE overviews and per-metal tables re-checked: no later row."},
 {"when":"Sun 01-Nov","impact":"Bullish","text":f"MONTH ROLL: October official means - aluminium cash ${oc:,.2f}, three-month ${om:,.2f}, stock {os_:,} t; Friday's close sits above both price averages after the 15-October low."},
 {"when":"Sun 01-Nov","impact":"Bullish (cost)","text":"HORMUZ: Straits Daily Brief - strait effectively closed to commercial traffic; 129 AIS-visible vessels holding position; a record 35 attacks on ships reported in October; Brent settled $113.43. Iranian mine claims and reopening conditions UNCONFIRMED."},
 {"when":"Sat 31-Oct","impact":"Bullish (margin)","text":"PEER EARNINGS: JiaoZuo WanFang nine-month net profit CNY 1.75bn (+93.5% y/y) on revenue CNY 5.94bn (+19.2%) (AL Circle)."},
 {"when":"Sat 31-Oct","impact":"Bullish","text":"AL CIRCLE: analysts argue bears may be wrong, citing resilient demand and historically low inventories, with prices targeting $3,625 in 2027 (no named forecaster)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"0-1 month","impact":"Bullish","url":W,
  "headline":f"OCTOBER CLOSES ABOVE ITS AVERAGE. Completed October-2026 official means (22 sessions, Westmetall): aluminium cash ${oc:,.2f} and three-month ${om:,.2f}, both below September (${sep_c:,.2f} / ${sep_m:,.2f}), with the spread averaging ${osp:,.2f}. Friday's month-end official - cash $3,114.00, three-month $3,080.00 - sits above both averages after the $2,994.50 three-month low of 15-October; stock fell from 240,625 t to 231,200 t over the month. Base-metal October cash means: copper ${ocu:,.2f}, nickel ${oni:,.2f}, zinc ${ozn:,.2f}, lead ${opb:,.2f}."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish (cost)","url":S_ST,
  "headline":"HORMUZ EFFECTIVELY CLOSED TO COMMERCIAL TRAFFIC (Straits Daily Brief, 01-November): IMF PortWatch last showed 2 transits on 25-October against an 85/day baseline (feed flagged stale); 129 AIS-visible vessels were holding position in the strait and Gulf watch box; the brief cites outlet reports of a record 35 attacks on ships in October. Brent settled $113.43 (+2.37%), WTI $104.12. Iran's navy claims another mine-struck tanker fire and Iran reportedly offered to reopen the strait within two days if the US accepts seven conditions - both UNCONFIRMED by any maritime authority or major wire."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Bullish (margin)","url":S_WF,
  "headline":"JIAOZUO WANFANG NINE-MONTH PROFIT NEARLY DOUBLES (AL Circle, 31-October): revenue CNY 5,938.64m (+19.2% y/y from CNY 4,981.54m); net profit CNY 1,753.08m (+93.5% from CNY 905.92m); EPS CNY 1.47 (from CNY 0.76). No Q3 standalone or output figures in the source. A second Chinese smelter print, after Yunnan Aluminium, showing profit growing far faster than sales."},
 {"theme":"Outlook","horizon":"6-18 months","impact":"Bullish","url":S_BE,
  "headline":"'ALUMINIUM BEARS MAY BE GETTING IT WRONG' (AL Circle, 31-October): unnamed analysts argue resilient demand and historically low inventories support prices targeting $3,625/t in 2027. The article also notes analysts cut Norsk Hydro's 2026 EBITDA forecast 4% to NOK 34.9bn after a Q3 EBITDA of NOK 9.1bn (+52% y/y, 6% below consensus), Hydro lowered capex guidance to NOK 12.5bn, and Hydro's Slovalco restart targets 75,000 t/yr by February 2027. Third-party view, not a consensus."},
]+d['news']
d['news']=d['news'][:20]

# ---------- peer earnings ----------
d['earnings'].insert(0,{"company":"JiaoZuo WanFang Aluminum (000612.SZ)","group":"Aluminum producer (China)","period":"9M 2026 (Jan-Sep)","reported":"31 Oct 2026","reported_iso":"2026-10-31","sentiment":"Positive",
 "headline":"9M-2026: revenue CNY 5,938.64m (+19.2% y/y from CNY 4,981.54m); net profit CNY 1,753.08m (+93.5% from CNY 905.92m); basic and diluted EPS CNY 1.47 (from CNY 0.76). Q3 standalone figures and output were not given in the source.",
 "readthrough":"A second Chinese smelter's nine-month print shows profit growing roughly five times faster than revenue, consistent with widening Chinese smelting margins (higher aluminium, lower alumina) under the capacity cap. Read-through: no margin pressure for curtailment inside China.",
 "eps":1.47,"revenue_bn":None,"yoy_pct":93.5,"url":S_WF})
d['earnings_note']=("JIAOZUO WANFANG REPORTED (added 01-November): nine-month net profit rose 93.5% to CNY 1.75bn on revenue of CNY 5.94bn (+19.2%). Chalco's Q3 is still pending. "+d['earnings_note'])

# ---------- outlook ----------
for cat in d['outlook']['catalysts']:
    if cat['date']=='Late Oct / early Nov (pending)':
        cat['event']="CHALCO Q3-2026 RESULTS - STILL PENDING: an English search on 01-November again did not locate a Q3-2026 release (latest located: H1-2026 net profit RMB 11.87bn, +67.9%). Yunnan Aluminium (+164% nine-month net income) and JiaoZuo WanFang (+93.5% nine-month net profit) are the Chinese smelter prints located so far. "+cat['event'].split("STILL PENDING:",1)[-1].split(". ",1)[-1]
for s in d['outlook']['scenarios']:
    s['drivers']="HELD 01-NOVEMBER at 20/45/35: no new session over the weekend; October closed with three-month above its monthly mean and the backwardation at $34.00, and Hormuz remains effectively closed - supportive context but not new price confirmation; the pre-registered Monday 02-November test is unchanged. "+s['drivers']
hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 01-NOVEMBER: Straits Daily Brief - effectively closed to commercial traffic; 129 AIS-visible vessels holding position; outlets report a record 35 attacks on ships in October; Iran's reported seven-condition reopening offer is unconfirmed by major wires. Trend held at UP."; r['trend']='up'; hit+=1
assert hit==1
d['outlook']['ai_analysis'].insert(0,f"SUNDAY 01-NOVEMBER (NO NEW SESSION; MONTH ROLL): the board stays on Friday's 30-October official (three-month $3,080.00, cash $3,114.00, $34.00 backwardation, stock 231,200 t). October's completed official means were cash ${oc:,.2f} and three-month ${om:,.2f}; the month closed above both after the $2,994.50 low of 15-October, and stock fell every week. Hormuz remains effectively closed (Straits Daily Brief) and Chinese smelter profits keep surging (JiaoZuo WanFang +93.5%), while third-party commentary (AL Circle) argues low inventories could lift prices toward $3,625 in 2027. Monday's official is the persistence test for the 3,077 break.")

# ---------- EW (no new session) ----------
d['ew']['short_term']['writeup']="REVIEWED 01-NOVEMBER (SUNDAY, NO NEW SESSION): count and levels unchanged from the 31-October review - wave (v) of C low at 2,994.50 favoured as complete; the first weekly close above 3,077 stands; a second settled close above 3,077 (Monday) would strengthen the rebound count, a close below 3,061.5 would weaken it; invalidation 3,289. "+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']="REVIEWED 01-NOVEMBER (SUNDAY, NO NEW SESSION): the 3,080.00 weekly close above the 3,077 50% retracement stands; the October monthly bar closed near its high. Corrective count unchanged pending the next weekly close. "+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

d['inputs_summary']=("UPDATE 01-NOVEMBER (SUNDAY): no new LME session, so Copper's fifteen-session window stays at 12-October to 30-October (last mark $14,449.00 cash); copper's October cash mean was "+f"${ocu:,.2f}"+". No new monthly carbon settlement (due mid-November) or dated SMM fluoride, silicon or magnesium mark was published over the weekend, so no hist mark was appended. Energy context: Brent settled $113.43 (Straits Daily Brief, 01-November). "+d['inputs_summary'])

for p in d['producer_status']: p['asof']=RD
PS={p['name']:p for p in d['producer_status']}
c=PS['China operators (aggregate, incl. Chalco and Hongqiao)']
c['update']="UPDATED 01-NOVEMBER: JiaoZuo WanFang nine-month net profit +93.5% to CNY 1.75bn (AL Circle, 31-October), after Yunnan Aluminium's +164% - both consistent with strong Chinese smelting margins under the cap; Chalco's Q3-2026 report still not located. "+c['update']
c['src']=[L_WF,S_WF]
c=PS['Slovalco (Hydro / Penta JV, Slovakia)']
c['update']="REVIEWED 01-NOVEMBER: AL Circle (31-October) reports Hydro's Slovalco restart targets 75,000 t/yr of capacity by February 2027; no newer company release located. "+c['update']
c['src']=[L_BE,S_BE]

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 30-Oct-2026 session re-checked 01-Nov (EN and DE overviews agree; Al/Cu/Ni per-metal tables show no later row; October means recomputed from 22 sessions)",W])
for x in ([L_ST,S_ST],[L_WF,S_WF],[L_BE,S_BE]): d['sources'].append(x)
d['outlook']['sources'].append([L_ST,S_ST]); d['outlook']['sources'].append([L_BE,S_BE])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-30'; ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
