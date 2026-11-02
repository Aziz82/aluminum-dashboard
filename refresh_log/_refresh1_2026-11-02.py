# Daily data refresh - 2026-11-02 (MONDAY, ~02:40 UTC, BEFORE the ring). Latest PUBLISHED LME official is still FRIDAY 30-Oct (Monday prints 13:20 London).
# Westmetall cache-busted EN + DE overviews re-fetched: both show 30-Oct (Al cash 3,114 / 3M 3,080 / stock 231,200; MTLE 1.11770 vs 1.11280 prior); Al per-metal table top row = 30-Oct, no later row.
# New: SMM Aluminum Morning Meeting (02-Nov 09:55 GMT+8): SHFE 2612 23,280 (-85, -0.36%); LME 3M electronic close 3,062.5 (-0.18%) Fri; social inventory 547kt (-2kt vs Thu, -6kt w/w), destocking slowing.
# SMM billet 6063 131kt (-7kt w/w). straits.live 02-Nov: effectively closed; 2 transits 25-Oct vs 85/day; 122 vessels holding; Brent $111.84 00:10 UTC (-1.40% 24h).
# CHALCO Q3-2026 LOCATED (Finimize citing HKEX filing): Q3 attributable NP RMB 6.04bn (+59%), revenue RMB 61.18bn (+1.7%); 9M NP 17.92bn (10.87bn). 
# CORRECTION: H1-2026 per FilingReader (27-Aug): NP 11.871bn (+67.91%), revenue 125.413bn (+7.74%) -> stored H1 row (7.071bn) and Q2-26 hist point 3.53bn conflict and are corrected/removed.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-02'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_MM="https://news.metal.com/newscontent/104190124-macro-sentiment-in-a-tug-of-war-between-longs-and-shorts-destocking-slowdown-aluminum-prices-consolidate-smm-aluminum-morning-meeting-summary"
L_MM="SMM - Macro sentiment in a tug-of-war, destocking slowdown, aluminum prices consolidate [Aluminum Morning Meeting Summary] (02-Nov-2026)"
S_BL="https://www.metal.com/en/newscontent/104190007-november-2-2026-aluminum-billet-inventory-smm-data"; L_BL="SMM - November 2, 2026 Aluminum Billet Inventory (02-Nov-2026)"
S_ST="https://straits.live/briefs/2026-11-02"; L_ST="Straits Daily Brief - Strait of Hormuz, 02-Nov-2026"
S_CQ="https://finimize.com/content/chalcos-q3-profit-jumped-59-on-cost-cuts"; L_CQ="Finimize - Chalco's Q3 profit jumped 59% on cost cuts (citing Chalco HKEX filing; Q3-2026)"
S_CH="https://filingreader.com/news-wire/shanghai/2026-08-27/chalco-posts-surge-in-first-half-profit-and-revenue"; L_CH="FilingReader - Chalco posts surge in first-half profit and revenue (27-Aug-2026)"
S_BX="https://www.alcircle.com/news/149-5mt-bauxite-in-focus-guinea-drives-africas-quadrupled-export-growth-to-china-121778"; L_BX="AL Circle - 149.5Mt bauxite in focus: Guinea drives Africa's export growth to China (31-Oct-2026)"

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("COMPILED SUNDAY 01-NOVEMBER-2026. THERE IS NO LME RING ON SATURDAY OR SUNDAY, SO THE BOARD IS THE FRIDAY 30-OCTOBER-2026 LME OFFICIAL - THE LAST TRADING SESSION AND THE WEEKLY CLOSE; the next official prints Monday 02-November 13:20 London.",
                    "COMPILED MONDAY 02-NOVEMBER-2026 ABOUT 02:40 LONDON, BEFORE THE RING, SO THE BOARD IS THE FRIDAY 30-OCTOBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION AND THE WEEKLY CLOSE; Monday's official prints 13:20 London.")
        o=o.replace("RE-CHECKED SUNDAY 01-NOVEMBER-2026: the cache-busted Westmetall English and German overviews still show the 30-October session with identical figures and the aluminium, copper and nickel per-metal tables show NO row after 30-October, so the board is CARRIED through the weekend because the market is shut; the next official prints Monday 02-November 13:20 London.",
                    "RE-CHECKED MONDAY 02-NOVEMBER-2026 BEFORE THE RING: the cache-busted Westmetall English and German overviews still show the 30-October session with identical figures and the aluminium per-metal table shows NO row after 30-October, so the board is the latest complete official; Monday's official prints 13:20 London.")
        o=o.replace("COMPILED SUNDAY 01-NOVEMBER-2026 (NO RING AT WEEKENDS)","COMPILED MONDAY 02-NOVEMBER-2026 (BEFORE THE RING)")
        o=o.replace("REVIEWED 01-NOVEMBER: no newer public disclosure","REVIEWED 02-NOVEMBER: no newer public disclosure").replace("REVIEWED 01-NOVEMBER. NO NEW DATED","REVIEWED 02-NOVEMBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status'):
    d[k]=walk(d[k])
assert all("COMPILED MONDAY 02-NOVEMBER-2026" in k['delta'] and "RE-CHECKED MONDAY 02-NOVEMBER" in k['delta'] for k in d['kpi_cards'])
assert all("COMPILED MONDAY 02-NOVEMBER-2026" in p['src'] for p in d['premiums'])
for p in d['producer_status']: p['asof']=RD

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 30-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION: this Monday 02-November run is compiled about 02:40 London, BEFORE the ring, so Monday's official (13:20 London) has not printed yet and no board price, stock or FX figure changes. Reference and electronic-close prices (SMM's $3,062.5 Friday electronic close, Trading Economics) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (02-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and show the 30-October session with identical prices, stocks and FX fixings (EUR/USD MTLE 1.11770; prior 1.11280), and the per-metal aluminium daily table shows NO row after 30-October (cash 3,114.00, three-month 3,080.00, stock 231,200), so the board is the latest complete official rather than lagging.")
hit=0
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        cut=cv.find(" These are the FRIDAY 30-OCTOBER readings carried through the weekend")
        if cut>0: cv=cv[:cut]
        C[i]=cv+" These are the FRIDAY 30-OCTOBER readings, not re-fetched individually on Monday 02-November before the European open. The Straits Daily Brief (02-November) shows Brent at $111.84 at 00:10 UTC, down 1.40% over 24 hours - cited in text only."; hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 02-NOVEMBER: no authorised fetch was blocked (Westmetall EN, DE and aluminium per-metal pages, news.metal.com, AL Circle and the Straits Daily Brief all fetched). Two SMM article links on the metal.com/en path returned HTTP 404 and were re-fetched on the news.metal.com path. The Hormuz items in the 02-November brief are labelled by the brief itself as AI-assisted; IRGC claims of two mine-struck tankers are single-source and UNCONFIRMED by any maritime authority."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        C[i]=("PEER EARNINGS: CHALCO Q3-2026 LOCATED THIS RUN via Finimize, which cites Chalco's Hong Kong exchange filing; the article does not state its publication or the filing date, so the row is dated to the day it was located (02-November) and is labelled single-source until the filing itself is retrieved. CORRECTION: Chalco's H1-2026 row previously showed attributable net profit of RMB 7.071bn (+0.81%) - those figures match H1-2025, not H1-2026. FilingReader (27-August) reports H1-2026 attributable net profit RMB 11.871bn (+67.91%) on revenue RMB 125.413bn (+7.74%), consistent with Finimize's nine-month total of RMB 17.92bn; the row is corrected and the conflicting Q2-2026 point (RMB 3.53bn) is REMOVED from the Chalco history strip and left as a gap, because no source retrieved states the Q2-2026 standalone figure. JiaoZuo WanFang, Yunnan Aluminium and AMAG remain nine-month-only."); hit+=1
assert hit==3,hit

d['so_what']={"line":"Monday pre-ring: aluminium starts the week on Friday's $3,080 three-month official with a $34 backwardation and record-low LME stock, but post-official trade slipped to $3,062.5 and Chinese destocking is slowing - today's official decides whether the break above $3,077 holds.",
 "points":[
 "WHERE IT STANDS: the latest published official is Friday 30-October - cash $3,114.00, three-month $3,080.00, a $34.00 backwardation (cash above three-month) and LME stock 231,200 t, the lowest on this page's record. Monday's official prints at 13:20 London.",
 "AFTER FRIDAY'S RING: SMM's morning summary (02-November) shows LME three-month closing Friday's electronic trade at $3,062.5 (-0.18%) - below the official and just above the $3,061.5 support - and Shanghai's most-traded contract at RMB 23,280 (-0.36%). These are not official prices.",
 "CHINA DESTOCKING IS SLOWING: SMM puts Chinese ingot social inventory at 547,000 t, down only 2,000 t from Thursday and 6,000 t on the week, and says the peak season is ending with some reports of weaker downstream demand. Chalco's Q3-2026 profit rose 59% to RMB 6.04bn on revenue up only 1.7% (Finimize, citing the company's filing) - Chinese smelting margins remain strong.",
 "WHAT TO WATCH: today's official against $3,077 (hold = rebound intact) and $3,061.5 (a close below weakens it); Hormuz, still effectively closed (2 transits on 25-October vs 85 a day) with Brent easing to $111.84; whether the backwardation stays above $15."]}

d['feed']=([
 {"when":"Mon 02-Nov","impact":"Mixed","text":"PRE-RING: board stays on the Friday 30-October LME official (cash $3,114.00, three-month $3,080.00, $34.00 backwardation, stock 231,200 t); Westmetall English and German pages re-checked - no later session. SMM: Friday's electronic close $3,062.5 (-0.18%)."},
 {"when":"Mon 02-Nov","impact":"Bearish","text":"SMM morning summary: China ingot social inventory 547,000 t, -2,000 t vs Thursday and -6,000 t week-on-week - destocking slowing as the peak season ends; SHFE 2612 RMB 23,280 (-0.36%); prices expected to consolidate."},
 {"when":"Mon 02-Nov","impact":"Bullish (margin)","text":"CHALCO Q3-2026: attributable net profit RMB 6.04bn (+59% y/y) on revenue RMB 61.18bn (+1.7%); nine-month profit RMB 17.92bn vs 10.87bn (Finimize, citing HKEX filing)."},
 {"when":"Mon 02-Nov","impact":"Bullish (cost)","text":"HORMUZ: Straits Daily Brief - strait effectively closed; 122 AIS-visible vessels holding; Brent $111.84 at 00:10 UTC (-1.40% over 24h). IRGC mine claims UNCONFIRMED."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"China","horizon":"0-1 month","impact":"Bearish","url":S_MM,
  "headline":"CHINA DESTOCKING SLOWS, PRICES SEEN CONSOLIDATING (SMM morning summary, 02-November 09:55 GMT+8): Chinese aluminium ingot social inventory was 547,000 t on Monday, down 2,000 t from Thursday and 6,000 t week-on-week. The most-traded SHFE 2612 contract closed Friday's night session at RMB 23,280/t (-RMB 85, -0.36%) and LME three-month closed electronic trade at $3,062.5/t (-0.18%). East China A00 traded at a RMB 110-130/t premium to SHFE 2611, Central China at a RMB 60-80/t discount. SMM describes macro sentiment as mixed, notes the traditional peak season is nearing its end and some reports of weakening downstream demand, and expects short-term consolidation. READ: the Chinese draw that supported October is fading."},
 {"theme":"China","horizon":"0-1 month","impact":"Mixed","url":S_BL,
  "headline":"BILLET STOCKS STILL FALLING (SMM, 02-November): 6063 aluminium billet inventory at major Chinese consumption sites was 131,000 t, down 7,000 t (-5.1%) week-on-week, with Foshan the largest decline and Wuxi and Nanchang slightly higher. READ: semi-finished stocks are still drawing even as ingot destocking slows."},
 {"theme":"Earnings","horizon":"0-3 months","impact":"Bullish (margin)","url":S_CQ,
  "headline":"CHALCO Q3-2026 PROFIT +59% (Finimize, citing Chalco's Hong Kong exchange filing): attributable net profit RMB 6.04bn for July-September, up 59% year-on-year, on revenue of RMB 61.18bn (+1.7%), with the gain attributed mainly to cost cuts and efficiency. Nine-month attributable profit RMB 17.92bn (RMB 10.87bn a year earlier), revenue RMB 186.59bn (RMB 176.55bn), operating cash flow RMB 40.99bn (RMB 25.39bn). Reported nine-month output: metallurgical alumina 11.3 Mt (-13.4%), refined alumina 3.5 Mt (+6.1%), primary aluminium incl. alloys 6.08 Mt (+1.33%). READ: the third large Chinese smelter print of the season confirms margins expanding far faster than sales under the 45 Mt cap."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish (cost)","url":S_ST,
  "headline":"HORMUZ STILL EFFECTIVELY CLOSED (Straits Daily Brief, 02-November): IMF PortWatch last showed 2 transits on 25-October against an 85/day baseline (data about a week old); 122 AIS-visible vessels were holding position in the strait and Gulf watch box at 23:59 UTC. Brent was $111.84 at 00:10 UTC, down 1.40% over 24 hours. UKMTO reported a vessel struck by an unknown projectile on 01-November (per Anadolu); the IRGC claims two tankers struck naval mines - UNCONFIRMED by any maritime authority. No reopening confirmed; reported US-Iran talks via Qatar have no published outcome."},
 {"theme":"Raw materials","horizon":"6-18 months","impact":"Mixed","url":S_BX,
  "headline":"GUINEA BAUXITE TO CHINA NEARLY QUADRUPLED (AL Circle, 31-October): Guinea's bauxite exports to China rose from 38.2 Mt in 2018 to about 149.5 Mt in 2025, and their value from $2.20bn to $12bn. READ: China's alumina chain depends ever more on a single West African supplier - a concentration risk for the bauxite leg of the cost basket."},
]+d['news']
d['news']=d['news'][:20]

# ---------- peer earnings ----------
d['earnings'].insert(0,{"company":"Aluminum Corporation of China (Chalco, 2600.HK / 601600)","group":"Aluminum producer (China)","period":"Q3 2026 (Jul-Sep) and 9M 2026","reported":"Located 02 Nov 2026 (filing date not stated in source)","reported_iso":"2026-11-02","sentiment":"Positive",
 "headline":"Q3-2026: attributable net profit RMB 6.04bn (+59% y/y); revenue RMB 61.18bn (+1.7%). 9M-2026: attributable net profit RMB 17.92bn (RMB 10.87bn in 9M-2025); revenue RMB 186.59bn (RMB 176.55bn); operating cash flow RMB 40.99bn (RMB 25.39bn). Reported 9M output: metallurgical alumina 11.3 Mt (-13.4%), refined alumina 3.5 Mt (+6.1%), primary aluminium incl. alloys 6.08 Mt (+1.33%). Single secondary source (Finimize) citing the HKEX filing.",
 "readthrough":"Profit growth driven by cost and efficiency rather than sales; with aluminium output roughly flat and metallurgical alumina output down, the result points to a strong smelting margin and cheaper alumina inside China's 45 Mt cap. Read-through: no margin-driven curtailment pressure in China.",
 "eps":None,"revenue_bn":61.18,"yoy_pct":59.0,"url":S_CQ})
fixed=0
for e in d['earnings']:
    if e.get('reported_iso')=='2026-08-28' and 'Chalco' in e['company']:
        e.update({"sentiment":"Positive","period":"H1-2026 (six months to 30-Jun-2026)","revenue_bn":"RMB 125.413bn (H1)","eps":"n/d","yoy_pct":"+67.91% (H1 attributable net profit)","url":S_CH,
         "reported":"27-Aug-2026","reported_iso":"2026-08-27",
         "headline":"H1-2026 interim results (CORRECTED 02-November): net profit attributable RMB 11.871bn, +67.91% y/y; total operating revenue RMB 125.413bn, +7.74% (FilingReader, 27-August). This row previously carried RMB 7.071bn (+0.81%) and a Q2 split, which match the prior-year period and are withdrawn. Q2-2026 standalone figures are not stated in the source.",
         "readthrough":"Chinese smelting margins widened sharply in H1-2026 on higher aluminium prices and lower alumina costs, consistent with the Q1 (+56%) and Q3 (+59%) prints; the earlier 'margin compression' reading on this row rested on prior-year figures and is withdrawn."}); fixed+=1
assert fixed==1,fixed
eh=d['earnings_history']['2600']
eh['points']=[p for p in eh['points'] if p[0]!='Q2-26']+[["Q3-26",6.04]]
eh['src']=["Chalco (2600.HK / 601600) quarterly net profit attributable, RMB bn. UPDATED 02-NOVEMBER: Q3-2026 point RMB 6.04bn added (Finimize, citing Chalco's HKEX filing; +59% y/y vs RMB 3.80bn in Q3-2025, matching the Q3-25 point on this strip). CORRECTION: the Q2-2026 point previously shown (RMB 3.53bn) is REMOVED and left as a gap - it conflicts with the reported H1-2026 attributable profit of RMB 11.871bn (FilingReader, 27-August) and appears to be a prior-year figure; no retrieved source states the Q2-2026 standalone figure, so none is derived or interpolated.",S_CQ]
d['earnings_note']=("CHALCO Q3-2026 LOCATED (added 02-November): attributable net profit RMB 6.04bn (+59%) on revenue RMB 61.18bn (+1.7%); the H1-2026 row is corrected to RMB 11.871bn (+67.91%). "+d['earnings_note'])

# ---------- outlook ----------
hit=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Late Oct / early Nov (pending)':
        cat['date']='Located Mon 02-Nov'
        cat['event']="CHALCO Q3-2026 RESULTS - RESOLVED STRONG: Q3 attributable net profit RMB 6.04bn (+59% y/y) on revenue RMB 61.18bn (+1.7%), nine-month RMB 17.92bn vs 10.87bn (Finimize, citing the HKEX filing). With Yunnan Aluminium (+164% nine-month) and JiaoZuo WanFang (+93.5%), all three Chinese smelter prints located this season show sharply higher profit - no margin pressure for curtailment inside the cap."
        hit+=1  # impact keeps its High|Medium|Low vocabulary
assert hit==1
O_SC="HELD 01-NOVEMBER at 20/45/35: no new session over the weekend; October closed with three-month above its monthly mean and the backwardation at $34.00, and Hormuz remains effectively closed - supportive context but not new price confirmation; the pre-registered Monday 02-November test is unchanged. "
for s in d['outlook']['scenarios']:
    t=s['drivers']; t=t[len(O_SC):] if t.startswith(O_SC) else t
    s['drivers']="HELD 02-NOVEMBER at 20/45/35: no new official before Monday's ring; Friday's electronic close faded to $3,062.5 and SMM reports Chinese destocking slowing, offset by the $34.00 backwardation, record-low LME stock and a closed Hormuz; today's official against 3,077 / 3,061.5 is the test. "+t
hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 02-NOVEMBER: Straits Daily Brief - effectively closed (2 transits 25-October vs 85/day); 122 vessels holding; UKMTO reports a vessel struck by an unknown projectile on 01-November; Brent $111.84 (-1.40% over 24h). Trend held at UP."; r['trend']='up'; hit+=1
assert hit==1
d['outlook']['ai_analysis'].insert(0,"MONDAY PRE-RING, 02-NOVEMBER: the latest official is still Friday's 30-October print (three-month $3,080.00; backwardation $34.00; stock 231,200 t). Friday's electronic close faded to $3,062.5 (SMM) and Chinese ingot destocking has slowed to 6,000 t a week (547,000 t) as the peak season ends, so the Chinese support that lifted October is weakening. Against that, LME stock is at a record low, the curve is backwardated and Hormuz stays effectively closed. Chalco's Q3 (+59% profit) confirms strong Chinese margins - no supply-side relief from Chinese cuts. Today's official against 3,077 / 3,061.5 is the persistence test.")

def reprefix(s,old,new): return new+(s[len(old):] if s.startswith(old) else s)
O_EWS="REVIEWED 01-NOVEMBER (SUNDAY, NO NEW SESSION): count and levels unchanged from the 31-October review - wave (v) of C low at 2,994.50 favoured as complete; the first weekly close above 3,077 stands; a second settled close above 3,077 (Monday) would strengthen the rebound count, a close below 3,061.5 would weaken it; invalidation 3,289. "
d['ew']['short_term']['writeup']=reprefix(d['ew']['short_term']['writeup'],O_EWS,"REVIEWED 02-NOVEMBER (MONDAY, BEFORE THE RING; NO NEW OFFICIAL): count and levels unchanged - wave (v) of C low at 2,994.50 favoured as complete; the weekly close above 3,077 stands; a second settled close above 3,077 today would strengthen the rebound count, a close below 3,061.5 would weaken it; invalidation 3,289. Friday's softer electronic close ($3,062.5, SMM) is not a settled official and does not change the count. ")
O_EWL="REVIEWED 01-NOVEMBER (SUNDAY, NO NEW SESSION): the 3,080.00 weekly close above the 3,077 50% retracement stands; the October monthly bar closed near its high. Corrective count unchanged pending the next weekly close. "
d['ew']['long_term']['writeup']=reprefix(d['ew']['long_term']['writeup'],O_EWL,"REVIEWED 02-NOVEMBER (NO NEW OFFICIAL YET THIS WEEK): last weekly close 3,080.00, above the 3,077 50% retracement; corrective count unchanged pending this week's close. ")
d['ew']['updated']=RD

s=d['inputs_summary']; j=s.find("UPDATE 31-OCTOBER")
s=s[j:] if (s.startswith("UPDATE 01-NOVEMBER") and j>0) else s
d['inputs_summary']=("UPDATE 02-NOVEMBER (MONDAY, BEFORE THE RING): no new LME official yet, so Copper's fifteen-session window stays at 12-October to 30-October (last mark $14,449.00 cash). No new monthly carbon settlement (due mid-November) or dated SMM fluoride, silicon or magnesium mark was located for this run, so no hist mark was appended. Energy: Brent $111.84 at 00:10 UTC 02-November (Straits Daily Brief), Hormuz effectively closed. Bauxite: Guinea's exports to China reached about 149.5 Mt in 2025 (AL Circle). "+s)

PS={p['name']:p for p in d['producer_status']}
c=PS['China operators (aggregate, incl. Chalco and Hongqiao)']
c['update']="UPDATED 02-NOVEMBER: Chalco Q3-2026 attributable profit +59% to RMB 6.04bn on revenue +1.7%; reported nine-month primary aluminium output 6.08 Mt (+1.33%) and metallurgical alumina 11.3 Mt (-13.4%) (Finimize, citing the HKEX filing). SMM reports Chinese ingot destocking slowing (social inventory 547,000 t, -6,000 t w/w). "+c['update']
c['src']=[L_CQ,S_CQ]

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 30-Oct-2026 session re-checked 02-Nov before the ring (English and German overviews agree; Al per-metal table shows no later row)",W])
for x in ([L_MM,S_MM],[L_BL,S_BL],[L_ST,S_ST],[L_CQ,S_CQ],[L_CH,S_CH],[L_BX,S_BX]): d['sources'].append(x)
d['outlook']['sources'].append([L_MM,S_MM]); d['outlook']['sources'].append([L_ST,S_ST]); d['outlook']['sources'].append([L_CQ,S_CQ])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-30', ph['rows'][-1]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
