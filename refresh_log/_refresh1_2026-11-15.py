# Daily data refresh - 2026-11-15 (SUNDAY, ~02:35 UTC). No ring Sat/Sun: board CARRIED on the FRIDAY 13-Nov LME official.
# Westmetall cache-busted EN + DE overviews re-fetched: both show 13-Nov (Al cash 3,150.50 / 3M 3,018.00 / stock 224,150; MTLE 1.10510);
# aluminium per-metal table: newest row 13-Nov, NO later row. No board number changes this run.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-15'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-15"; L_ST="Straits Daily Brief - Strait of Hormuz, 15-Nov-2026 (Brent figure AI-assisted)"
S_RU="https://www.alcircle.com/news/russian-origin-aluminium-makes-up-99-98-of-lme-available-stocks-in-october-despite-inventories-fall-121924"; L_RU="AL Circle - Russian-origin metal 99.98% of LME available aluminium stocks at end-October; available stocks 216,950 t (12-Nov-2026)"
S_IN="https://www.alcircle.com/news/indias-dgtr-opens-anti-dumping-investigation-into-aluminium-extrusions-from-china-and-southeast-asia-121903"; L_IN="AL Circle - India's DGTR opens anti-dumping investigation into aluminium extrusions from China and Southeast Asia (Nov-2026)"
S_IN2="https://www.gktoday.in/dgtr-probes-aluminium-imports-from-four-countries/"; L_IN2="GKToday - DGTR suo motu probe into aluminium imports from China, Malaysia, Vietnam, Thailand initiated 09-Nov-2026"
S_CB="https://www.alcircle.com/news/coolbrook-brings-1-700c-electric-heating-tech-in-australias-alumina-decarbonising-drive-121956"; L_CB="AL Circle - Coolbrook joins HILT CRC AlumiNEXT alumina-calcination electrification work (13-Nov-2026)"
S_JP="https://www.spglobal.com/energy/en/news-research/latest-news/metals/101326-japanese-q4-aluminum-premium-falls-35-to-255mt-cif-japan"
cash,m3,stk=3150.5,3018.0,224150
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==cash and B['LME 3-month']['cur']==m3 and B['LME warehouse stock (t)']['cur']==stk
assert d['lme_series'][-1]==["13-Nov",cash,m3,stk]

REPL=[("COMPILED SATURDAY 14-NOVEMBER-2026 ABOUT 02:40 LONDON. THE MARKET IS SHUT (NO RING ON SATURDAY OR SUNDAY), SO THE BOARD IS THE FRIDAY 13-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION AND THE CORRECT FIGURE TO CARRY UNTIL MONDAY 16-NOVEMBER 13:20 LONDON. ",
       "COMPILED SUNDAY 15-NOVEMBER-2026 ABOUT 02:35 LONDON. THE MARKET IS SHUT (NO RING ON SATURDAY OR SUNDAY), SO THE BOARD IS THE FRIDAY 13-NOVEMBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND - THE LATEST PUBLISHED SESSION AND THE CORRECT FIGURE UNTIL MONDAY 16-NOVEMBER 13:20 LONDON. RE-CHECKED 15-NOVEMBER: the cache-busted Westmetall English and German overviews still show the identical 13-November session and the aluminium per-metal table shows NO row after 13-November. "),
      ("COMPILED SATURDAY 14-NOVEMBER-2026","COMPILED SUNDAY 15-NOVEMBER-2026"),
      ("REVIEWED 14-NOVEMBER: no newer public disclosure","REVIEWED 15-NOVEMBER: no newer public disclosure"),
      ("REVIEWED 14-NOVEMBER. NO NEW DATED","REVIEWED 15-NOVEMBER. NO NEW DATED")]
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
        r['risk']+=" UPDATE 15-NOVEMBER: Straits Daily Brief - strait still listed CLOSED; latest lagged count 3 transits on 08-November (vs 85/day pre-crisis); AIS-visible vessels holding rose to 50 (from 38). Iran's Revolutionary Guard claims two tankers struck mines and caught fire east of the strait - NOT confirmed by any maritime authority. Iran's two-day reopening proposal awaits a US response; Qatar mediating, no terms published. Trend held at UP."; r['trend']='up'; hit+=1
assert hit==1
hc=0
for c in d['outlook']['catalysts']:
    if c['date']=='Daily, from Mon 16-Nov':
        c['event']="CARRIED THROUGH THE WEEKEND (re-checked 15-November, no new session). "+c['event']; hc+=1
assert hc==1
d['outlook']['ai_analysis'].insert(0,"SUNDAY 15-NOVEMBER, BOARD CARRIED ON THE FRIDAY 13-NOVEMBER OFFICIAL (no ring at weekends; Westmetall re-checked): three-month $3,018.00, cash $3,150.50, a $132.50 backwardation, LME stock 224,150 t; weights unchanged at 10/45/45 after Friday's bear-trigger break. Weekend news is structural: AL Circle reports Russian-origin metal made up 99.98% of LME available aluminium stocks at end-October (216,950 t available, lowest since March 2025), so the deliverable pool for buyers who avoid Russian metal is effectively nil - consistent with the wide backwardation; India's DGTR has opened a suo motu anti-dumping probe into aluminium extrusions from China, Malaysia, Vietnam and Thailand. Hormuz remains closed with new, unverified mine claims and an Iranian reopening proposal awaiting a US reply. Monday's test: 2,994.50 below (ends the Elliott base count), 3,042 above (reverses Friday's weight shift).")
pre="REVIEWED 15-NOVEMBER (WEEKEND, NO NEW SESSION): the count is unchanged from the 14-November review because there has been no official since Friday's 3,018.00; no pivot is added or re-labelled and no invalidation level is touched. "
d['ew']['short_term']['writeup']=pre+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=pre+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('China operators'):
        p['update']="REVIEWED 15-NOVEMBER: no new SMM social-inventory or operating-rate print on news.metal.com over the weekend; India's DGTR suo motu anti-dumping probe into aluminium extrusions from China, Malaysia, Vietnam and Thailand (initiated 09-November; the four account for about 90% of India's imports of the products, per press) is a new export headwind for Chinese and Southeast Asian extruders ("+S_IN+"). "+p['update']; hit+=1
    elif p['name'].startswith('US / Canada'):
        p['update']="REVIEWED 15-NOVEMBER: no official confirmation of the reported US-Canada deal located over the weekend; 50% Section 232 rate unchanged. "+p['update']; hit+=1
    elif p['name'].startswith('EGA'):
        p['update']="REVIEWED 15-NOVEMBER: no newer EGA release located since 766 of 1,262 cells (61%) restarted (12-November); full recovery targeted Q1-2027. "+p['update']; hit+=1
assert hit==3,hit

d['news']=[
 {"theme":"LME","horizon":"0-3 months","impact":"Bullish","url":S_RU,
  "headline":"RUSSIAN METAL IS 99.98% OF LME AVAILABLE ALUMINIUM STOCK (AL Circle, 12-November): at end-October Russian-origin aluminium made up 216,900 t of 216,950 t of available (non-cancelled) LME stock, which fell 4% m/m to its lowest since March 2025; Russian-origin units fell 9,725 t in the month and the only other origin was 50 t of Indian metal. READ: for consumers that avoid Russian units the deliverable LME pool is effectively nil, which supports the prompt squeeze and the wide backwardation."},
 {"theme":"Trade policy","horizon":"0-12 months","impact":"Mixed","url":S_IN,
  "headline":"INDIA OPENS ANTI-DUMPING PROBE INTO ALUMINIUM EXTRUSIONS (AL Circle; GKToday): the DGTR initiated a suo motu investigation on 09-November into aluminium extrusion profiles, structures and articles from China, Malaysia, Vietnam and Thailand, citing information from the Aluminium Extrusion Manufacturers Association of India; press reports the four supply about 90% of India's imports of the products. Any duty would be recommended by DGTR and decided by the Finance Ministry; no timeline published."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL CLOSED; NEW MINE CLAIMS, REOPENING PROPOSAL PENDING (Straits Daily Brief, 15-November): 3 transits on 08-November (lagged) vs 85/day pre-crisis; AIS-visible vessels holding up to 50 from 38. Iran's Revolutionary Guard claims two tankers struck mines and caught fire east of the strait - unconfirmed by any maritime authority. Iran's two-day reopening proposal awaits a US response, with Qatar mediating and no terms published. Brent settled $95.84 on Friday (brief's figure, AI-assisted)."},
 {"theme":"Alumina","horizon":"Structural","impact":"Mixed","url":S_CB,
  "headline":"ALUMINA DECARBONISATION (AL Circle, 13-November): Finland's Coolbrook has joined Australia's HILT CRC to test its 1,700C electric rotating heater for alumina calcination under the AlumiNEXT project, whose partners include EGA, Alcoa, Rio Tinto, South32 and Hydro; no refinery, capacity, timeline or funding disclosed."},
]+d['news']
d['news']=d['news'][:20]
d['feed']=([
 {"when":"Sun 15-Nov","impact":"Mixed","text":"BOARD CARRIED ON THE FRIDAY 13-NOVEMBER OFFICIAL (no ring at weekends; Westmetall re-checked): three-month $3,018.00, cash $3,150.50, backwardation $132.50, stock 224,150 t."},
 {"when":"Thu 12-Nov","impact":"Bullish","text":"LME: Russian-origin metal 99.98% of available aluminium stock at end-October; available stock 216,950 t, lowest since March 2025 (AL Circle)."},
 {"when":"Mon 09-Nov","impact":"Mixed","text":"INDIA: DGTR suo motu anti-dumping probe into aluminium extrusions from China, Malaysia, Vietnam and Thailand (AL Circle; GKToday)."},
 {"when":"Sun 15-Nov","impact":"Bullish","text":"HORMUZ: still closed; 50 vessels holding; IRGC claims two tankers hit mines (unconfirmed); Iran reopening proposal awaits US reply (Straits brief)."},
]+d['feed'])[:12]

d['so_what']={"line":"Weekend check: LME aluminium holds Friday's $3,018 three-month close - below the bear trigger, weights 10/45/45 - while prompt metal stays scarce ($132.50 backwardation, record-low 224,150 t stock, and Russian units now 99.98% of available LME stock); Monday's test is $2,994.50 below and $3,042 above.",
 "points":[
 "WHERE IT STANDS: no LME trading at weekends, so the board is Friday 13-November's official - three-month $3,018.00 (down $32.00 on the week), cash $3,150.50, a $132.50 backwardation (cash above three-month) and LME stock at a new low of 224,150 t.",
 "WHY PROMPT IS TIGHT: AL Circle reports Russian-origin metal was 99.98% of available LME aluminium stock at end-October (216,950 t, lowest since March 2025) - buyers avoiding Russian units have almost nothing deliverable on the LME. The forward weakness instead tracks a dollar at its highest since early 2025 on December Fed-hike pricing.",
 "TRADE AND SUPPLY: India's DGTR opened an anti-dumping probe into aluminium extrusions from China, Malaysia, Vietnam and Thailand; Hormuz stays closed with new, unconfirmed Iranian mine claims and a reopening proposal awaiting a US reply.",
 "WHAT TO WATCH (Monday 16-November): a settled close below the $2,994.50 October low (ends the Elliott base count) or back above $3,042 (returns weight to bull); whether the backwardation holds above $15; the November prompt rollover; first Q1-2027 Japanese premium offers (still none public)."]}

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 13-NOVEMBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND BECAUSE THE MARKET IS SHUT (no ring Saturday or Sunday); this Sunday 15-November run changes no board price, stock or FX figure. The next official prints Monday 16-November at 13:20 London. The Thursday 12-November official (cash 3,155.50, three-month 3,032.00, stock 226,350) is recorded in the series. The Trading Economics aluminium reference (about $3,009 for 13-November) is cited in text only.")
C[1]=("SOURCE CHECK THIS RUN (15-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and still AGREE on the identical 13-November session (aluminium cash 3,150.50, three-month 3,018.00, stock 224,150; EUR/USD MTLE 1.10510), and the aluminium per-metal daily table shows NO row after 13-November, so the board is complete and correctly carried rather than lagging.")
hit=0
for i,cv in enumerate(C):
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 15-NOVEMBER (SUNDAY): no authorised fetch was blocked. Westmetall EN and DE overviews and the aluminium per-metal table, AL Circle, news.metal.com and the Straits Daily Brief were fetched. Trading Economics macro pages were not re-fetched because no market has traded since Friday - macro rows carry the 13-November readings (the Straits brief shows Brent's Friday settle at $95.84 vs Trading Economics' about $96.08; both approximate). news.metal.com showed no weekend SHFE or inventory print; its India anti-dumping link again returned 404, so the probe is sourced to AL Circle and GKToday via search. mining.com was not fetched. A search for Q1-2027 Japanese premium offers again found none (S&P Global's $190-200/t is participant expectation, not an offer), so Q1 stays unpriced. Straits brief incident items are cited as claims/unconfirmed."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        rest=cv.split("EARLIER:",1)[-1].strip()
        C[i]=("PEER EARNINGS: NO NEW LISTED-PEER RESULT AND NO earnings_history BACK-FILL THIS RUN (15-NOVEMBER, weekend). EARLIER: "+rest); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=cv+" CARRIED THROUGH THE WEEKEND (15-November): no session since Friday."; hit+=1
assert hit==3,hit

for x in ([L_ST,S_ST],[L_RU,S_RU],[L_IN,S_IN],[L_IN2,S_IN2],[L_CB,S_CB]): d['sources'].append(x)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 13-Nov-2026 session re-checked 15-Nov (EN and DE overviews agree; Al per-metal table shows no later row)",W])
for x in ([L_RU,S_RU],[L_ST,S_ST],[L_IN,S_IN]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-13',cash,m3,stk]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
