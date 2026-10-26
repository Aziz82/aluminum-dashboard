# Daily data refresh - 2026-10-26 (MONDAY, ~02:40 UTC, BEFORE the ring). Latest PUBLISHED LME official is still FRIDAY 23-Oct (Monday prints 13:20 London).
# Westmetall cache-busted EN + DE overviews re-fetched: both show 23-Oct (Al cash 3,043 / 3M 3,018 / stock 235,800; MTLE 1.11910); Al per-metal table top row = 23-Oct, no later row.
# New: SMM Aluminum Morning Meeting (26-Oct 09:58 GMT+8): China ingot social inventory -30kt vs Thu, -54kt vs last Mon; LME 3M electronic close 3,040.5 (+1.15%) Fri; SHFE 23,575 (+0.96%);
# SMM three-region ingot ~410kt, tenth straight working-day decline. straits.live 26-Oct brief: strait effectively closed; 4 transits 18-Oct vs 85/day baseline; Brent $115.43 00:08 UTC (-1.11% 24h).
# AL Circle 24-Oct: Sual Partners / RusHydro production-sharing deal, up to 150kt from Boguchany smelter.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-26'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_MM="https://news.metal.com/newscontent/104177213-china-destocking-continues-to-support-ex-china-supply-caps-upside-smm-aluminum-morning-meeting-summary"
L_MM="SMM - China destocking continues to support, ex-China supply caps upside [Aluminum Morning Meeting Summary] (26-Oct-2026)"
S_IN="https://news.metal.com/newscontent/104177049-chinas-aluminum-ingot-inventory-in-three-regions-falls-on-october-26"
L_IN="SMM - China's aluminum ingot inventory in three regions falls on October 26 (26-Oct-2026)"
S_ST="https://straits.live/briefs/2026-10-26"; L_ST="Straits Daily Brief - Strait of Hormuz, 26-Oct-2026"
S_SU="https://www.alcircle.com/news/a-new-rival-for-rusal-sual-deal-puts-150-000-tonnes-of-russian-aluminium-in-focus-121674"
L_SU="AL Circle - Sual deal puts 150,000 tonnes of Russian aluminium in focus (24-Oct-2026)"

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("COMPILED SUNDAY 25-OCTOBER-2026 (MARKET SHUT FOR THE WEEKEND)","COMPILED MONDAY 26-OCTOBER-2026 (BEFORE THE RING; LATEST PUBLISHED OFFICIAL)")
        o=o.replace("COMPILED SUNDAY 25-OCTOBER-2026","COMPILED MONDAY 26-OCTOBER-2026 (BEFORE THE RING)")
        o=o.replace("REVIEWED 25-OCTOBER: no newer public disclosure","REVIEWED 26-OCTOBER: no newer public disclosure").replace("REVIEWED 25-OCTOBER. NO NEW DATED","REVIEWED 26-OCTOBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status'):
    d[k]=walk(d[k])
for p in d['producer_status']: p['asof']=RD

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 23-OCTOBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION: this Monday 26-October run is compiled about 02:40 London, BEFORE the ring, so Monday's official (13:20 London) has not printed yet and no board figure changes. Reference and electronic-close prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (26-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and show the 23-October session with identical prices, stocks and FX fixings (EUR/USD MTLE 1.11910), and the per-metal aluminium daily table shows NO row after 23-October (cash 3,043.00, three-month 3,018.00, stock 235,800), so the board is the latest complete official rather than lagging.")
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        cut=cv.find(" These are the FRIDAY 23-OCTOBER closes, carried through the weekend")
        if cut>0: cv=cv[:cut]
        C[i]=cv+" These are the FRIDAY 23-OCTOBER closes, not re-fetched individually on Monday 26-October before the European open. The Straits Daily Brief (26-October) shows Brent at $115.43 at 00:08 UTC, down 1.11% over 24 hours - cited in text only."
    if cv.startswith("FETCH NOTE 25-OCTOBER"):
        C[i]=("FETCH NOTE 26-OCTOBER: no authorised fetch was blocked for the board (Westmetall EN, DE and per-metal pages all fetched). One search-found news link (Deccan Herald, Brent settlement) returned HTTP 403 and is not cited. "
              "Hormuz items from Iranian state media and single-source reports in the Straits Daily Brief are cited as reported, not as fact. The SMM-reported LME three-month electronic close of $3,040.5 on Friday is a post-official price and is NOT used on the board.")

d['so_what']={"line":"Monday pre-ring: aluminium starts the week on Friday's $3,018 three-month official with a $25 backwardation and record-low LME stock, Chinese ingot stocks still falling, and Hormuz still effectively closed - the test today is whether price follows the tight curve above $3,061.5.",
 "points":[
 "WHERE IT STANDS: the latest published official is Friday 23-October - cash $3,043.00, three-month $3,018.00, a $25.00 backwardation (cash above three-month) and LME stock 235,800 t, the lowest on this page's record. Monday's official prints at 13:20 London.",
 "AFTER FRIDAY'S RING: SMM's morning summary (26-October) shows LME three-month closing Friday's electronic trade at $3,040.5 (+1.15%) and Shanghai at RMB 23,575 (+0.96%) - a firmer start than the official, but not an official price.",
 "CHINA KEEPS DRAWING: SMM reports Chinese ingot social inventory down 30,000 t since Thursday and 54,000 t on the week; three-region stocks are near 410,000 t after a tenth straight working-day decline. Against that, SMM says ex-China restarts and new capacity cap the upside and expects consolidation.",
 "WHAT TO WATCH: today's official versus $3,061.5-3,077 (a break would confirm the tight curve) and $2,994.50 (downside); Hormuz, still described as effectively closed (4 transits on 18-October against 85 a day pre-crisis) with Brent near $115; the Fed decision on 28-October; China's Fifth Plenary Session (26-29 October)."]}

d['feed']=([
 {"when":"Mon 26-Oct","impact":"Bullish","text":"SMM morning summary: China aluminium ingot social inventory down 30,000 t since Thursday and 54,000 t week-on-week; three-region ingot stocks about 410,000 t, a tenth straight working-day decline. SMM expects consolidation as ex-China restarts cap the upside."},
 {"when":"Mon 26-Oct","impact":"Mixed","text":"PRE-RING: board stays on the Friday 23-October LME official (cash $3,043.00, three-month $3,018.00, $25.00 backwardation, stock 235,800 t); Westmetall English and German pages re-checked - no later session. Monday's official prints 13:20 London."},
 {"when":"Mon 26-Oct","impact":"Bullish (cost)","text":"Hormuz: Straits Daily Brief says the strait is effectively closed to commercial traffic (4 transits on 18-October vs an 85/day baseline); Brent $115.43 at 00:08 UTC, -1.11% over 24 hours."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"China","horizon":"0-1 month","impact":"Bullish","url":S_MM,
  "headline":"CHINA DESTOCKING CONTINUES, EX-CHINA SUPPLY CAPS UPSIDE (SMM morning summary, 26-October): Chinese aluminium ingot social inventory fell 30,000 t from last Thursday and 54,000 t from last Monday. In Friday's session the most-traded SHFE contract closed at RMB 23,575/t (+RMB 225, +0.96%) and LME three-month closed electronic trade at $3,040.5/t (+$34.5, +1.15%); East China spot premiums were RMB 240-260/t. SMM describes ex-China premiums as generally weak and expects prices to consolidate, with ex-China restarts and new capacity weighing against Chinese destocking. READ: physical China is tight; the ceiling comes from Gulf and other ex-China supply returning."},
 {"theme":"China","horizon":"0-1 month","impact":"Bullish","url":S_IN,
  "headline":"THREE-REGION INGOT STOCKS FALL AGAIN (SMM, 26-October): aluminium ingot inventory across three major Chinese consumption hubs stood in the 410,000-tonne range, a tenth straight working-day decline with all three regions destocking. READ: the post-holiday draw is extending into late October, supporting Shanghai prices and import arbitrage interest."},
 {"theme":"Logistics","horizon":"0-3 months","impact":"Bullish (cost)","url":S_ST,
  "headline":"HORMUZ STILL EFFECTIVELY CLOSED (Straits Daily Brief, 26-October): the brief describes the strait as effectively closed to commercial traffic, with 4 transits recorded on 18-October (IMF PortWatch) against a pre-crisis baseline of 85 a day and 118 vessels holding position in the Gulf watch box. Brent was $115.43 at 00:08 UTC, down 1.11% over 24 hours. Iranian state media denies making new reopening proposals via Pakistan; reports of an Iranian reopening offer and of mine-free routes are single-source and unverified. READ: Gulf metal and raw-material flows stay exposed; energy-cost support for prices persists."},
 {"theme":"Supply","horizon":"3-12 months","impact":"Mixed","url":S_SU,
  "headline":"RUSSIA: SECOND SELLER OF PRIMARY METAL (AL Circle, 24-October): Sual Partners signed a production-sharing agreement with state-controlled RusHydro giving it access to up to 150,000 t of aluminium (up to half the output) from the Boguchany smelter in Siberia, with supply of alumina, anodes, aluminium fluoride and silicon also covered. Announced 15-October during Russian Energy Week. READ: no change to total Russian supply; a marketing shift worth watching for Russian metal flows. The article does not confirm sales have started."},
]+d['news']
d['news']=d['news'][:20]

for r in d['outlook']['risks']:
    if 'HORMUZ' in r['risk']:
        r['risk']+=" UPDATE 26-OCTOBER: Straits Daily Brief - strait effectively closed (4 transits 18-October vs 85/day baseline); Brent $115.43 (-1.11% over 24h); Iran denies new reopening proposals. Trend held at UP."
        r['trend']='up'
d['outlook']['ai_analysis'].insert(0,"MONDAY PRE-RING, 26-OCTOBER: the latest official is still Friday's 23-October print (three-month $3,018.00; backwardation $25.00; stock 235,800 t). Friday's electronic close was firmer ($3,040.5, SMM) and China keeps destocking (social inventory -54,000 t on the week; three-region stocks near 410,000 t), while SMM flags ex-China restarts and new capacity as the cap. Hormuz remains effectively closed with Brent near $115. The read is unchanged: a tight curve without price confirmation; today's official against 3,061.5-3,077 is the test.")

def reprefix(s,old_prefix,new):
    if s.startswith(old_prefix): s=s[len(old_prefix):]
    return new+s
O_EWS="REVIEWED 25-OCTOBER (SUNDAY, NO NEW SESSION): count and levels unchanged from the 24-October review - wave (v) low at 2,994.50 favoured as complete but not confirmed; confirmation is a settled close above 3,077; re-count below about 2,977.5; invalidation 3,289. The firmer post-official trade on Friday is not a settled official and does not change the count. "
N_EWS="REVIEWED 26-OCTOBER (MONDAY, BEFORE THE RING; NO NEW OFFICIAL): count and levels unchanged - wave (v) low at 2,994.50 favoured as complete but not confirmed; confirmation is a settled close above 3,077; re-count below about 2,977.5; invalidation 3,289. Friday's firmer electronic close ($3,040.5, SMM) is not a settled official and does not change the count. "
d['ew']['short_term']['writeup']=reprefix(d['ew']['short_term']['writeup'],O_EWS,N_EWS)
O_EWL="REVIEWED 25-OCTOBER (SUNDAY, NO NEW SESSION): the weekly close of 3,018.00 stands; corrective count towards 2,894 unchanged. "
d['ew']['long_term']['writeup']=reprefix(d['ew']['long_term']['writeup'],O_EWL,"REVIEWED 26-OCTOBER (NO NEW OFFICIAL YET THIS WEEK): last weekly close 3,018.00; corrective count towards 2,894 unchanged. ")
d['ew']['updated']=RD

O_SC="HELD 25-OCTOBER at 15/45/40: no new session over the weekend; firmer post-official trade and a fourth weekly oil gain are supportive but not price confirmation. "
for s in d['outlook']['scenarios']:
    s['drivers']=reprefix(s['drivers'],O_SC,"HELD 26-OCTOBER at 15/45/40: no new official before Monday's ring; continued Chinese destocking and Hormuz closure are supportive, ex-China restarts cap the upside. ")

O_IS_START="UPDATE 25-OCTOBER (SUNDAY):"
s=d['inputs_summary']
if s.startswith(O_IS_START):
    j=s.find("UPDATE 24-OCTOBER")
    s=s[j:] if j>0 else s
d['inputs_summary']=("UPDATE 26-OCTOBER (MONDAY, BEFORE THE RING): no new LME official yet, so Copper's fifteen-session window stays at 05-October to 23-October (last mark $14,415.00 cash). No new monthly carbon settlement or dated SMM fluoride, silicon or magnesium mark was located for this run, so no hist mark was appended. Energy: Brent $115.43 at 00:08 UTC 26-October (Straits Daily Brief), Hormuz effectively closed. "+s)

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 23-Oct-2026 session re-checked 26-Oct before the ring (English and German overviews agree; no later row)",W])
for x in ([L_MM,S_MM],[L_IN,S_IN],[L_ST,S_ST],[L_SU,S_SU]): d['sources'].append(x)
d['outlook']['sources'].append([L_MM,S_MM]); d['outlook']['sources'].append([L_ST,S_ST])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-23', ph['rows'][-1]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
