# Daily data refresh - 2026-11-16 (MONDAY, ~02:35 UTC, before today's ring at 13:20 London).
# Board CARRIED on the FRIDAY 13-Nov LME official (latest published). Westmetall cache-busted EN + DE overviews re-fetched: both 13-Nov
# (Al cash 3,150.50 / 3M 3,018.00 / stock 224,150; MTLE 1.10510); Al per-metal table newest row 13-Nov, no later row. No board number changes.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-16'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-16"; L_ST="Straits Daily Brief - Strait of Hormuz, 16-Nov-2026 (Brent figure AI-assisted)"
S_HI="https://news.metal.com/newscontent/IAQGC2TBD54QOIARVGZFVMP63ETXZ2BKCIY4GSA-hindalco-plans-to-triple-copper-recycling-capacity-and-expand-aluminium-production"; L_HI="SMM - Hindalco plans Aditya smelter expansion (181 kt Dec-2027 + 193 kt Dec-2028) and evaluates 370 kt Mahan expansion, citing Q2 FY27 results/call (13-Nov-2026)"
S_BD="https://www.alcircle.com/news/baltic-dry-index-crosses-3-000-mark-as-capesize-freight-rates-hit-october-high-121960"; L_BD="AL Circle - Baltic Dry Index crosses 3,000 (3,020) as capesize rates hit highest since early October (15-Nov-2026)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (page updated 16-Nov-2026; 13-Nov close about $3,009, 4-week low 2,983 intraday)"
cash,m3,stk=3150.5,3018.0,224150
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==cash and B['LME 3-month']['cur']==m3 and B['LME warehouse stock (t)']['cur']==stk
assert d['lme_series'][-1]==["13-Nov",cash,m3,stk]

REPL=[("COMPILED SUNDAY 15-NOVEMBER-2026 ABOUT 02:35 LONDON. THE MARKET IS SHUT (NO RING ON SATURDAY OR SUNDAY), SO THE BOARD IS THE FRIDAY 13-NOVEMBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND - THE LATEST PUBLISHED SESSION AND THE CORRECT FIGURE UNTIL MONDAY 16-NOVEMBER 13:20 LONDON. RE-CHECKED 15-NOVEMBER: the cache-busted Westmetall English and German overviews still show the identical 13-November session and the aluminium per-metal table shows NO row after 13-November. ",
       "COMPILED MONDAY 16-NOVEMBER-2026 ABOUT 02:35 LONDON, BEFORE TODAY'S RING. THE BOARD IS THE FRIDAY 13-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION AND THE CORRECT FIGURE UNTIL TODAY'S OFFICIAL PRINTS AT 13:20 LONDON. RE-CHECKED 16-NOVEMBER: the cache-busted Westmetall English and German overviews both show the identical 13-November session and the aluminium per-metal table shows NO row after 13-November. "),
      ("COMPILED SUNDAY 15-NOVEMBER-2026","COMPILED MONDAY 16-NOVEMBER-2026"),
      ("REVIEWED 15-NOVEMBER: no newer public disclosure","REVIEWED 16-NOVEMBER: no newer public disclosure"),
      ("REVIEWED 15-NOVEMBER. NO NEW DATED","REVIEWED 16-NOVEMBER. NO NEW DATED"),
      ("none was located in Friday trading or the weekend window","none was located in Friday trading, the weekend or early Monday")]
cnt={i:0 for i in range(len(REPL))}
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        for i,(a,b) in enumerate(REPL):
            if a in o: cnt[i]+=1; o=o.replace(a,b)
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status','inputs','logistics','raw_materials'): d[k]=walk(d[k])
assert cnt[0]>=8 and cnt[1]>=6, cnt
print('repl',cnt)

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 16-NOVEMBER: Straits Daily Brief - strait remains effectively closed to commercial traffic; latest lagged count still 3 transits on 08-November (vs 85/day pre-crisis); AIS-visible vessels holding back at 38. Iran's Revolutionary Guard now claims three tankers in total struck mines and caught fire (Iran's army and IRNA cite two) - NOT confirmed by any maritime authority. Iran says its two-day reopening plan remains on the table, contingent on US action. Trend held at UP."; r['trend']='up'; hit+=1
assert hit==1
hc=0
for c in d['outlook']['catalysts']:
    if c['date']=='Daily, from Mon 16-Nov':
        c['event']=c['event'].replace("CARRIED THROUGH THE WEEKEND (re-checked 15-November, no new session). ","TODAY (Monday 16-November, official 13:20 London) - board still on Friday's official as of this 02:35 run. "); hc+=1
assert hc==1

d['outlook']['ai_analysis'].insert(0,"MONDAY 16-NOVEMBER (02:35 LONDON, BEFORE THE RING), BOARD STILL ON THE FRIDAY 13-NOVEMBER OFFICIAL (Westmetall EN and DE re-checked, no later row): three-month $3,018.00, cash $3,150.50, a $132.50 backwardation, LME stock 224,150 t; weights unchanged at 10/45/45. Trading Economics' Friday reference closed about $3,009 after an intraday four-week low of 2,983 - below the 2,994.50 October low intraday, but the Elliott rule is on SETTLED officials, so the base count stands until today's 13:20 print. New public items are supply-side and long-dated: Hindalco plans 374 kt/yr of new Aditya smelting capacity (181 kt December 2027, 193 kt December 2028) and is evaluating 370 kt at Mahan (SMM, citing its Q2 FY27 call), adding to the 2027 ex-China supply wave behind participants' $190-200/t Q1-2027 Japanese premium expectations. Dry-bulk freight is firming (BDI 3,020, capesize highest since early October). Hormuz is unchanged: closed, with Iranian mine claims rising to three tankers and still unconfirmed.")
pre="REVIEWED 16-NOVEMBER (BEFORE MONDAY'S RING, NO NEW SESSION): the count is unchanged because there has been no official since Friday's 3,018.00. Trading Economics' Friday CFD reference traded down to 2,983 intraday - beneath the 2,994.50 October low - before closing about 3,009; that is NOT a settled official, so no pivot is added or re-labelled and no invalidation level is touched, but it raises the odds that today's official tests 2,994.50. "
for k in ('short_term','long_term'):
    w=d['ew'][k]['writeup']
    w=w.replace("REVIEWED 15-NOVEMBER (WEEKEND, NO NEW SESSION): the count is unchanged from the 14-November review because there has been no official since Friday's 3,018.00; no pivot is added or re-labelled and no invalidation level is touched. ","")
    d['ew'][k]['writeup']=pre+w
d['ew']['updated']=RD

hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('China operators'):
        p['update']=p['update'].replace("REVIEWED 15-NOVEMBER: no new SMM social-inventory or operating-rate print on news.metal.com over the weekend;","REVIEWED 16-NOVEMBER: no new SMM social-inventory or operating-rate print located on news.metal.com this run; REVIEWED 15-NOVEMBER:"); hit+=1
    elif p['name'].startswith('US / Canada'):
        p['update']="REVIEWED 16-NOVEMBER: still no official confirmation of the reported US-Canada deal; 50% Section 232 rate unchanged. "+p['update']; hit+=1
    elif p['name'].startswith('EGA'):
        p['update']=p['update'].replace("REVIEWED 15-NOVEMBER: no newer EGA release","REVIEWED 16-NOVEMBER: no newer EGA release"); hit+=1
assert hit==3,hit

d['news']=[
 {"theme":"Supply","horizon":"12-36 months","impact":"Bearish","url":S_HI,
  "headline":"HINDALCO PLANS NEW INDIAN SMELTING CAPACITY (SMM, 13-November, citing Hindalco's Q2 FY27 results and earnings call): the Aditya smelter expansion adds 374,000 t/yr of primary aluminium in two phases - 181,000 t/yr targeted for December 2027 and 193,000 t/yr for December 2028 - alongside an 850,000 t/yr Aditya alumina refinery; a further 370,000 t/yr Mahan expansion is under evaluation pending environmental clearances and investment decisions. READ: adds to the 2027-28 ex-China supply wave (India, Indonesia, Middle East) that participants cite for softer Japanese premium expectations."},
 {"theme":"Freight","horizon":"0-3 months","impact":"Mixed","url":S_BD,
  "headline":"DRY-BULK FREIGHT FIRMS (AL Circle, 15-November): the Baltic Dry Index rose 61 points (2.1%) to 3,020, its highest since 05-October; the capesize index rose 2.9% to 4,836 with average daily earnings up $1,232 to $40,357. READ: higher capesize rates lift delivered bauxite and alumina costs for import-dependent refineries and smelters."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL CLOSED; MINE CLAIMS RISE TO THREE TANKERS, UNCONFIRMED (Straits Daily Brief, 16-November): latest lagged count 3 transits on 08-November vs 85/day pre-crisis; 38 AIS-visible vessels holding. Iran's Revolutionary Guard claims three tankers in total struck mines and caught fire (Iran's army and IRNA cite two); no maritime authority has confirmed any incident. Iran's deputy foreign minister says the two-day reopening plan remains on the table, contingent on US action. Brent about $95.5 (brief's AI-assisted figure)."},
 {"theme":"LME","horizon":"0-1 month","impact":"Bearish","url":S_TE,
  "headline":"ALUMINIUM AT A FOUR-WEEK LOW INTO MONDAY (Trading Economics, page updated 16-November): the CFD reference fell to 2,983 intraday on Friday - its lowest since October - before closing about $3,009 (-0.33%). The LME three-month OFFICIAL on Friday was $3,018.00; Monday's official prints at 13:20 London."},
]+d['news']
d['news']=d['news'][:20]
d['feed']=([
 {"when":"Mon 16-Nov","impact":"Mixed","text":"BOARD STILL ON THE FRIDAY 13-NOVEMBER OFFICIAL before Monday's ring (Westmetall re-checked): three-month $3,018.00, cash $3,150.50, backwardation $132.50, stock 224,150 t."},
 {"when":"Fri 13-Nov","impact":"Bearish","text":"INDIA: Hindalco plans 374 kt/yr Aditya smelter expansion (Dec-2027 / Dec-2028) and evaluates 370 kt at Mahan (SMM, citing Q2 FY27 call)."},
 {"when":"Sun 15-Nov","impact":"Mixed","text":"FREIGHT: Baltic Dry Index 3,020, highest since 05-October; capesize 4,836, earnings $40,357/day (AL Circle)."},
 {"when":"Mon 16-Nov","impact":"Bullish","text":"HORMUZ: still closed; IRGC claims three tankers hit mines (unconfirmed); Iran's two-day reopening plan 'on the table' pending US action (Straits brief)."},
]+d['feed'])[:12]

d['so_what']={"line":"Into Monday's ring LME aluminium sits on Friday's $3,018 three-month official - below the bear trigger with the CFD reference already probing a four-week low near $2,983 - while prompt metal stays scarce ($132.50 backwardation, 224,150 t stock); today's official at 13:20 London decides whether $2,994.50 breaks.",
 "points":[
 "WHERE IT STANDS: no new LME official yet today, so the board is Friday 13-November's - three-month $3,018.00, cash $3,150.50, a $132.50 backwardation (cash above three-month) and stock at a low of 224,150 t. The Trading Economics reference touched 2,983 intraday on Friday before closing about $3,009.",
 "WHY FORWARD IS SOFT BUT PROMPT IS TIGHT: a strong dollar and December Fed-hike pricing weigh on the three-month price, while available LME stock is almost entirely Russian-origin, leaving little deliverable metal for many buyers.",
 "SUPPLY PIPELINE GROWS: Hindalco plans 374 kt/yr of new Indian smelting capacity for December 2027-28 and is weighing 370 kt more - part of the 2027 ex-China wave behind softer early Q1-2027 Japanese premium expectations ($190-200/t, participants via S&P Global; no offers yet). Dry-bulk freight is firming (BDI 3,020).",
 "WHAT TO WATCH TODAY: a settled official below $2,994.50 (ends the Elliott base count) or back above $3,042; whether the backwardation holds; the November prompt rollover; Hormuz (still closed, Iranian mine claims unconfirmed)."]}

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 13-NOVEMBER-2026 LME OFFICIAL, CARRIED BECAUSE THIS MONDAY 16-NOVEMBER RUN IS COMPILED AT ABOUT 02:35 LONDON, BEFORE TODAY'S RING (today's official prints at 13:20 London); no board price, stock or FX figure changes this run. The Thursday 12-November official (cash 3,155.50, three-month 3,032.00, stock 226,350) is recorded in the series. The Trading Economics aluminium reference (about $3,009 close for 13-November, 2,983 intraday low) is a CFD reference cited in text only.")
C[1]=("SOURCE CHECK THIS RUN (16-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and AGREE on the identical 13-November session (aluminium cash 3,150.50, three-month 3,018.00, stock 224,150; EUR/USD MTLE 1.10510), and the aluminium per-metal daily table shows NO row after 13-November, so the board is the latest published session rather than lagging.")
hit=0
for i,cv in enumerate(C):
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 16-NOVEMBER (MONDAY, PRE-RING): no authorised fetch was blocked. Westmetall EN and DE overviews and the aluminium per-metal table, AL Circle, news.metal.com, Trading Economics aluminium and the Straits Daily Brief were fetched. Other Trading Economics macro pages were not re-fetched - no Western session has traded since Friday - so macro rows carry the 13-November readings (Straits brief Brent about $95.5 early Monday; approximate, AI-assisted). news.metal.com's front page showed no aluminium print; the Hindalco expansion item was found via search on SMM and fetched. A Tiwai Point potline-restart report (The Press, 15-November) was found by search but its page returned no article text, so it is NOT published. mining.com was not fetched. A search for Q1-2027 Japanese premium offers again found none (S&P Global's $190-200/t is participant expectation, not an offer), so Q1 stays unpriced. Straits brief incident items are cited as claims/unconfirmed."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        rest=cv.split("EARLIER:",1)[-1].strip()
        C[i]=("PEER EARNINGS: NO NEW LISTED-PEER RESULT AND NO earnings_history BACK-FILL THIS RUN (16-NOVEMBER); Hindalco's expansion guidance from its Q2 FY27 call is reported in news only. EARLIER: "+rest); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=cv.replace("CARRIED THROUGH THE WEEKEND (15-November): no session since Friday.","CARRIED THROUGH THE WEEKEND AND INTO MONDAY 16-November (pre-ring): no Western session since Friday."); hit+=1
    elif "stock chart axis floor of 200,000 t leaves about 26,725 t headroom below visible stock of 226,725 t" in cv:
        C[i]=cv.replace("brackets cash 3,223.50 and three-month 3,064.00; the stock chart axis floor of 200,000 t leaves about 26,725 t headroom below visible stock of 226,725 t","brackets cash 3,150.50 and three-month 3,018.00; the stock chart axis floor of 200,000 t leaves about 24,150 t headroom below visible stock of 224,150 t"); hit+=1
assert hit==4,hit

# logistics: BDI refreshed on a newer dated public mark
for l in d['logistics']:
    if l['name'].startswith('Baltic Dry'):
        l['val']="3,020 (AL Circle, 15-November) - REFRESHED ON A NEWER DATED PUBLIC MARK, replacing the 3,430 (23-September) carried for several runs. Up 61 points (2.1%), highest since 05-October; capesize 4,836 (+2.9%, highest since 02-October), capesize earnings $40,357/day (+$1,232)"
        l['trend']='up'
        l['note']="REVIEWED MONDAY 16-NOVEMBER-2026: AL Circle (15-November) reports the BDI crossing 3,000 on firmer capesize rates; the article gives the session as a Thursday without a calendar date. Higher capesize rates raise delivered costs on bauxite and alumina lanes. PRIOR NOTE: "+l['note']
        l['src']="UPDATED 16-NOVEMBER-2026: "+L_BD+" ("+S_BD+"). PRIOR: "+l['src']
    elif l['name'].startswith('Strait of Hormuz'):
        l['val']="CLOSED TO COMMERCIAL TRAFFIC (Straits Daily Brief, 16-November): 3 transits on 08-November (lagged) vs 85/day pre-crisis; 38 vessels holding; Iranian mine claims (two to three tankers) unconfirmed; Iran's two-day reopening plan pending US action"
        l['note']="REVIEWED MONDAY 16-NOVEMBER-2026 (Straits Daily Brief): transit, holding and incident figures as in the value field; incidents are Iranian claims carried by multiple outlets with conflicting totals and NO maritime-authority confirmation. Arrow stays UP. PRIOR NOTE: "+l['note']
        l['src']="UPDATED 16-NOVEMBER-2026: "+L_ST+" ("+S_ST+"). PRIOR: "+l['src']

for x in ([L_ST,S_ST],[L_HI,S_HI],[L_BD,S_BD],[L_TE,S_TE]): d['sources'].append(x)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 13-Nov-2026 session re-checked 16-Nov pre-ring (EN and DE overviews agree; Al per-metal table shows no later row)",W])
for x in ([L_HI,S_HI],[L_ST,S_ST]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-13',cash,m3,stk]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
