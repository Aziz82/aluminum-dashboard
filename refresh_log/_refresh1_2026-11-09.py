# Daily data refresh - 2026-11-09 (MONDAY, ~02:40 UTC / London). Run precedes Monday's ring (13:20 London), so the latest
# PUBLISHED official is still FRIDAY 06-Nov. Westmetall cache-busted EN + DE overviews re-fetched: both show 06-Nov
# (Al cash 3,117 / 3M 3,050 / stock 227,600; MTLE 1.11690); aluminium per-metal table newest row 06-Nov. No board number changes.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-09'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-09"; L_ST="Straits Daily Brief - Strait of Hormuz, 09-Nov-2026 (ticker AI-assisted)"
S_INV="https://news.metal.com/newscontent/JK6QXU5YEUZVKVYCEECL6O3QPAXELZ6GOIW67IA-november-9-2026-smm-daily-inventory-data-of-aluminum-ingots-in-three-regions-smm-data"; L_INV="SMM - three-region aluminium ingot social inventory, 09-Nov-2026"
S_CH="https://www.alcircle.com/news/chinalco-international-transfers-60-jiuye-sanwei-stake-to-shenyang-institute-121884"; L_CH="AL Circle - Chinalco International transfers 60% Jiuye Sanwei stake (07-Nov-2026)"
cash,m3,stk=3117.0,3050.0,227600
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==cash and B['LME 3-month']['cur']==m3 and B['LME warehouse stock (t)']['cur']==stk
assert d['lme_series'][-1]==["06-Nov",cash,m3,stk]

REPL=[("COMPILED SUNDAY 08-NOVEMBER-2026 ABOUT 02:40 LONDON. THERE IS NO LME RING ON SATURDAY OR SUNDAY, SO THE BOARD IS THE FRIDAY 06-NOVEMBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND - THE LAST TRADING SESSION AND THE CORRECT FIGURE UNTIL MONDAY 09-NOVEMBER. RE-CHECKED 08-NOVEMBER: the cache-busted Westmetall English and German overviews still show the identical 06-November session and the aluminium and copper per-metal tables show NO row after 06-November. ",
       "COMPILED MONDAY 09-NOVEMBER-2026 ABOUT 02:40 LONDON, BEFORE MONDAY'S RING (THE OFFICIAL PRINTS 13:20 LONDON), SO THE LATEST PUBLISHED LME OFFICIAL IS STILL FRIDAY 06-NOVEMBER-2026 AND THE BOARD IS CARRIED ON IT. RE-CHECKED 09-NOVEMBER: the cache-busted Westmetall English and German overviews still show the identical 06-November session and the aluminium per-metal table shows NO row after 06-November. "),
      ("COMPILED SUNDAY 08-NOVEMBER-2026 (LME BOARD CARRIED ON THE FRIDAY 06-NOVEMBER OFFICIAL, THE LAST TRADING SESSION; NO RING AT WEEKENDS).",
       "COMPILED MONDAY 09-NOVEMBER-2026 BEFORE THE RING (LME BOARD CARRIED ON THE FRIDAY 06-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; MONDAY'S OFFICIAL PRINTS 13:20 LONDON)."),
      ("REVIEWED 08-NOVEMBER: no newer public disclosure","REVIEWED 09-NOVEMBER: no newer public disclosure"),
      ("REVIEWED 08-NOVEMBER. NO NEW DATED","REVIEWED 09-NOVEMBER. NO NEW DATED")]
cnt={i:0 for i in range(len(REPL))}
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        for i,(a,b) in enumerate(REPL):
            if a in o: cnt[i]+=1; o=o.replace(a,b)
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status'): d[k]=walk(d[k])
assert cnt[0]>=8 and cnt[1]>=6, cnt
print('repl',cnt)

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 09-NOVEMBER: Straits Daily Brief - strait still listed CLOSED, crisis pressure 'extreme' and flat over 24h; latest lagged transit count still 1 vessel on 01-November (IMF PortWatch) vs 85/day; 115 AIS-visible vessels holding (down from 138). Incidents reported 08-November: The Maritime Executive reports a tanker burning after a strike in the strait; the IRGC says it targeted three tankers; US forces fired on and disabled a St. Kitts-flagged cargo ship attempting to breach the blockade in the Gulf of Oman (Al Jazeera, Military.com). Iranian mine/fire claims and a single-source report of an Iraq-US oil-export deal through the strait remain UNCONFIRMED. No reopening agreement. Brent about $97.65 (-0.7%) late Sunday. Trend held at UP."; r['trend']='up'; hit+=1
assert hit==1
for c in d['outlook']['catalysts']:
    if c['date']=='Daily, from Mon 09-Nov':
        c['event']=c['event'].replace("CARRIED THROUGH THE WEEKEND (re-checked 08-November, no new session). ","MONDAY 09-NOVEMBER OFFICIAL DUE 13:20 LONDON (this run precedes it; board still on Friday). ")
d['outlook']['ai_analysis'].insert(0,"MONDAY 09-NOVEMBER, PRE-RING: the board is still the Friday 06-November official because Monday's prints at 13:20 London (Westmetall re-checked) - three-month $3,050.00, cash $3,117.00, a $67.00 backwardation, LME stock 227,600 t; weights unchanged at 15/45/40. China's physical market keeps destocking: SMM's three-region ingot social inventory fell 4,500 t day on day to 372,500 t on 09-November (377,000 t on 06-November), every region lower. Hormuz escalated again over the weekend (a tanker reported burning after a strike, the US disabling a blockade-runner in the Gulf of Oman) with no reopening deal, which keeps the energy and freight leg of the cost floor supported. Today's test is unchanged: 3,077 above, 3,042 then 3,024.50 below.")
pre="REVIEWED 09-NOVEMBER (PRE-RING, NO NEW SESSION SINCE FRIDAY): the count is unchanged because there has been no official since Friday's 3,050.00; no pivot is added or re-labelled and no invalidation level is touched; Monday's 13:20 official is the next input. "
for k in ('short_term','long_term'):
    w=d['ew'][k]['writeup']
    w=w.replace("REVIEWED 08-NOVEMBER (WEEKEND, NO NEW SESSION): the count is unchanged from the 07-November review because there has been no official since Friday's 3,050.00; no pivot is added or re-labelled and no invalidation level is touched. ","")
    d['ew'][k]['writeup']=pre+w
d['ew']['updated']=RD

for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('EGA'):
        p['update']=p['update'].replace("REVIEWED 08-NOVEMBER: no newer EGA release located;","REVIEWED 09-NOVEMBER: no newer EGA release located;")
    elif p['name'].startswith('China operators'):
        p['update']="UPDATED 09-NOVEMBER (SMM, 09-November): three-region aluminium ingot social inventory 372,500 t, -4,500 t (-1.2%) day on day - Guangdong 98,000 t, Wuxi 169,500 t, Gongyi 105,000 t, each -1,500 t ("+S_INV+"); Chinalco International (HKEX 2068) is transferring a 60% stake in non-aluminium subsidiary Jiuye Sanwei within the group for RMB 100.08m - an internal restructuring with no smelting-capacity impact (AL Circle, 07-November). "+p['update'].replace("REVIEWED 08-NOVEMBER: no new SMM social-inventory print on news.metal.com (weekend); ","")
    elif p['name'].startswith('Rio Tinto'):
        p['update']=p['update'].replace("REVIEWED 08-NOVEMBER: no newer public disclosure located beyond the 06-November workforce review. ","REVIEWED 09-NOVEMBER: no newer public disclosure located beyond the 06-November workforce review. ")
    elif p['name'].startswith('Alcoa'):
        p['update']="REVIEWED 09-NOVEMBER: no CADE decision or Alcoa response to Trimet's filing located. "+p['update']

d['news']=[
 {"theme":"China","horizon":"0-1 month","impact":"Bullish","url":S_INV,
  "headline":"CHINA INGOT STOCKS FALL AGAIN (SMM, 09-November): three-region aluminium ingot social inventory 372,500 t, down 4,500 t (-1.2%) day on day and down from 377,000 t on 06-November - Guangdong 98,000 t, Wuxi 169,500 t, Gongyi 105,000 t, each -1,500 t. SMM's morning read: destocking provides a floor, but weakening downstream demand and recovering ex-China supply keep prices consolidating. READ: physical tightness persists in China even as end-demand softens seasonally."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ ESCALATES OVER THE WEEKEND, STILL CLOSED (Straits Daily Brief, 09-November): The Maritime Executive reports a tanker burning after a strike in the strait; the IRGC says it targeted three tankers; US forces disabled a St. Kitts-flagged cargo ship attempting to breach the blockade in the Gulf of Oman (Al Jazeera, Military.com). 115 vessels holding; latest lagged transit count 1 on 01-November vs 85/day. Iranian mine claims and a single-source Iraq-US export-deal report are UNCONFIRMED; no reopening agreement. Brent about $97.65 late Sunday. READ: Gulf freight, war-risk and energy costs stay elevated."},
]+d['news']
d['news']=d['news'][:20]
d['feed']=([
 {"when":"Mon 09-Nov","impact":"Mixed","text":"PRE-RING: board still on the FRIDAY 06-NOVEMBER OFFICIAL (Monday's prints 13:20 London; Westmetall re-checked) - three-month $3,050.00, cash $3,117.00, backwardation $67.00, stock 227,600 t."},
 {"when":"Mon 09-Nov","impact":"Bullish","text":"CHINA: SMM three-region ingot social inventory 372,500 t, -4,500 t d/d (377,000 t on 06-Nov); all three regions lower."},
 {"when":"Sun 08-Nov","impact":"Bullish","text":"HORMUZ: tanker reported burning after a strike; US disables a blockade-runner in the Gulf of Oman; strait still closed, 115 vessels holding (Straits brief; Iranian claims UNCONFIRMED)."},
]+d['feed'])[:12]

d['so_what']={"line":"Monday pre-ring: LME aluminium still stands on Friday's $3,050 three-month close with a $67 backwardation and record-low 227,600 t LME stock, while Chinese ingot stocks keep falling and a weekend Hormuz escalation keeps the energy-cost floor in place.",
 "points":[
 "WHERE IT STANDS: Monday's LME official prints at 13:20 London, after this update, so the board is Friday 06-November's - three-month $3,050.00 (down $30.00 on the week), cash $3,117.00, a $67.00 backwardation (cash above three-month) and LME stock at 227,600 t. Scenario weights unchanged at 15/45/40.",
 "CHINA: SMM's three-region ingot social inventory fell another 4,500 t to 372,500 t on 09-November (377,000 t on Friday), with every region lower - physical metal stays tight even as SMM flags softer downstream demand.",
 "HORMUZ: the strait remains closed and the weekend brought more incidents - a tanker reported burning after a strike and US forces disabling a blockade-runner in the Gulf of Oman; no reopening deal. Brent is about $97.65.",
 "WHAT TO WATCH: today's official versus $3,077 resistance and $3,042 / $3,024.50 support; whether the backwardation holds above $15; any response to Trimet's challenge of the Alcoa-South32 alumina deal; first Q1-2027 Japanese premium offers (none public yet)."]}

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 06-NOVEMBER-2026 LME OFFICIAL, CARRIED BECAUSE THIS MONDAY 09-NOVEMBER RUN (about 02:40 London) PRECEDES MONDAY'S RING - the 09-November official prints at 13:20 London and will be picked up by the next run. No board price, stock or FX figure changes this run. The Thursday 05-November official (cash 3,160.00, three-month 3,097.50, stock 228,475) is recorded in the series. Trading Economics aluminium ($3,065.60 for 06-November) is a reference cited in text only.")
C[1]=("SOURCE CHECK THIS RUN (09-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and AGREE on the identical 06-November session (aluminium cash 3,117.00, three-month 3,050.00, stock 227,600; EUR/USD MTLE 1.11690), and the aluminium per-metal daily table shows NO row after 06-November, so the board is the latest published session rather than a lagging cache.")
hit=0
for i,cv in enumerate(C):
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 09-NOVEMBER: Westmetall EN and DE overviews, the aluminium per-metal table, AL Circle, news.metal.com (plus one SMM inventory article) and the Straits Daily Brief were fetched; no fetch was blocked. Two SMM article links returned HTTP 404 on the metal.com mirror and were read on news.metal.com instead. mining.com was not fetched this run; a web search for dated weekend smelter news found nothing new. Trading Economics macro pages were not re-fetched (no Western session since Friday) - macro rows carry the 06-November readings, with the Straits brief's late-Sunday Brent ($97.65) cited in text. A search for Q1-2027 Japanese premium offers again found none, so Q1 stays unpriced. The Straits brief labels its ticker AI-assisted and its transit count lags (01-November); Iranian claims and the Iraq-US export-deal report are cited as UNCONFIRMED."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        C[i]=cv.replace("NO NEW PEER RESULT AND NO earnings_history BACK-FILL THIS RUN (08-NOVEMBER, weekend).","NO NEW PEER RESULT AND NO earnings_history BACK-FILL THIS RUN (09-NOVEMBER)."); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=cv.replace("CARRIED THROUGH THE WEEKEND (08-November): no session since Friday; the Straits Daily Brief (08-November) shows Brent's Friday close at $98.32 (+0.03%).","CARRIED (09-November, pre-ring): no Western session since Friday; the Straits Daily Brief (09-November) shows Brent about $97.65 (-0.68%) at 23:39 UTC Sunday."); hit+=1
assert hit==3,hit
assert "09-NOVEMBER)" in C[10] or any("(09-NOVEMBER)" in c for c in C)

for x in ([L_ST,S_ST],[L_INV,S_INV],[L_CH,S_CH]): d['sources'].append(x)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 06-Nov-2026 session re-checked 09-Nov pre-ring (EN and DE overviews agree; Al per-metal table shows no later row)",W])
for x in ([L_ST,S_ST],[L_INV,S_INV]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-06',cash,m3,stk]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
