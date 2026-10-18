# Daily data refresh - 2026-10-18 (SUNDAY, ~02:35 UTC). Board CARRIED on the FRIDAY 16-Oct LME official (no ring Sat/Sun).
# Westmetall cache-busted EN + DE overviews re-fetched this run: both still show the 16-Oct session, identical figures; Al per-metal table shows NO row after 16-Oct.
# SMM news page: no aluminium items after 16-Oct. TE aluminium shows 16-Oct close 3,008.50 (+0.79%). Weekend item: Reuters (via BOE Report, 17-Oct) - IRGC says two tankers hit mines in Hormuz (unconfirmed).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-18'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_HZ="https://boereport.com/2026/10/17/irans-guards-say-two-tankers-hit-mines-in-strait-of-hormuz/"; L_HZ="BOE Report / Reuters - Iran's Guards say two tankers hit mines in Strait of Hormuz (17-Oct-2026)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (re-checked 18-Oct-2026; 16-Oct close)"

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("COMPILED SATURDAY 17-OCTOBER-2026","COMPILED SUNDAY 18-OCTOBER-2026")
        o=o.replace("REVIEWED 17-OCTOBER: no newer public disclosure","REVIEWED 18-OCTOBER: no newer public disclosure").replace("REVIEWED 17-OCTOBER. NO NEW DATED","REVIEWED 18-OCTOBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status'):
    d[k]=walk(d[k])
for p in d['producer_status']: p['asof']=RD

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 16-OCTOBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND BECAUSE THE MARKET IS SHUT (no ring Saturday or Sunday); this Sunday 18-October run changes no board figure. The next official prints Monday 19-October at 13:20 London. Reference and intraday prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (18-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and still show the 16-October session with identical prices, stocks and FX fixings (EUR/USD MTLE 1.12570), and the per-metal aluminium daily table shows NO row after 16-October, so the carried board is complete rather than lagging.")
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=cv+" These are the FRIDAY 16-OCTOBER closes, carried through the weekend (no new session); they were not re-fetched individually on Sunday 18-October."
    if cv.startswith("FETCH NOTE 17-OCTOBER"):
        C[i]="FETCH NOTE 18-OCTOBER: no fetch was blocked this run. AL Circle and Mining.com news pages were not used; SMM's news page carried no aluminium item after 16-October. The Hormuz mine-strike report of 17-October is Iranian state-media via Reuters and was NOT independently confirmed - it is cited as reported, not as fact."

d['so_what']={"line":"Weekend check: aluminium holds Friday's bounce to $3,012 three-month - still $58 lower on the week and below the July low - with no new LME session until Monday, while fresh Hormuz mine-strike reports keep energy-cost risk elevated.",
 "points":[
 "WHERE IT STANDS: the board is Friday's 16-October LME official - cash $3,014.00 (+$15.00), three-month $3,012.00 (+$17.50, +0.58%), a $2.00 backwardation (cash above three-month) and LME stock at a new low of 237,875 t. Nothing trades on the LME until Monday's 13:20 London official.",
 "WEEKEND NEWS: Iran's Revolutionary Guards said on Saturday that two crude tankers hit mines in the Strait of Hormuz (reported via Reuters, not independently confirmed), after attacks in the area increased over the past two weeks. That adds to Friday's jump in Brent (~$110) and European gas (~EUR 88/MWh, highest since December 2022) - a higher energy-cost floor for smelters outside China.",
 "THE BEARISH SIDE IS UNCHANGED: ex-China physical demand is weak (SMM, 16-October: offers falling in South Korea, Thailand and Vietnam, a stagnant US market), Gulf restarts are progressing, and markets still price a December Fed hike.",
 "WHAT TO WATCH THIS WEEK: Monday's open after the Hormuz reports; whether three-month settles back above $3,061.5-3,077 (decline ending) or below about $2,977.5 (new leg lower); China's September output data from the statistics bureau (expected around 19-20 October); the October carbon-input settlements; the 27-28 October FOMC."]}

d['feed']=([
 {"when":"Sun 18-Oct","impact":"Mixed","text":"WEEKEND CHECK: board CARRIED on the Friday 16-October LME official (cash $3,014.00, three-month $3,012.00, $2.00 backwardation, stock 237,875 t); Westmetall English and German pages re-checked - no later session. Next official Monday 19-October."},
 {"when":"Sat 17-Oct","impact":"Bullish (cost)","text":"Iran's Revolutionary Guards say two crude tankers (about 2m barrels each) hit mines in the Strait of Hormuz and caught fire; no independent confirmation (Reuters via BOE Report). Adds to energy-cost and shipping risk."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"Logistics","horizon":"0-1 month","impact":"Bullish (cost)","url":S_HZ,
  "headline":"HORMUZ: TWO TANKERS REPORTED HIT BY MINES (Reuters via BOE Report, 17-October): Iran's Revolutionary Guards Navy said two oil tankers, each carrying about 2 million barrels of crude according to state media, caught fire after hitting naval mines in the Strait of Hormuz; IRNA said the ships had switched off positioning and radar and were using a route Iran had not authorised, and one vessel was left immobilised. There was no independent confirmation. Reuters notes attacks in the area have increased over the past two weeks, with a container ship and a dry-bulk carrier sunk near the strait earlier in the week. READ: higher energy and freight-risk costs for Gulf-linked metal and raw-material flows; not a board figure."},
]+d['news']
d['news']=d['news'][:20]

RK=d['outlook']['risks']
for r in RK:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 18-OCTOBER: Iran's Revolutionary Guards said on 17-October that two crude tankers hit mines in the strait (Reuters via BOE Report; not independently confirmed). Trend held at UP."
        r['trend']='up'
d['outlook']['ai_analysis'].insert(0,"SUNDAY CHECK, 18-OCTOBER: no LME session since Friday's 16-October official (three-month $3,012.00, +$17.50; week -$58.00; stock 237,875 t), so the price read is unchanged: a bounce inside a still-bearish trend. The one material weekend item is an unconfirmed Iranian report of two tankers hitting mines in Hormuz, which reinforces the energy-cost floor already lifted by Brent near $110 and TTF near EUR 88/MWh. Monday's open is the first test of whether that cost story outweighs weak ex-China physical demand.")

EWS="REVIEWED 18-OCTOBER (SUNDAY, NO NEW SESSION): the count and levels are unchanged from the 16-October review - wave (v) low at 2,994.50 is possible but not confirmed; invalidation 3,289; rule-based cap near 2,977.5. "
d['ew']['short_term']['writeup']=EWS+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']="REVIEWED 18-OCTOBER (SUNDAY, NO NEW SESSION): the weekly close of 3,012.00 stands; count unchanged. "+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

for s in d['outlook']['scenarios']:
    s['drivers']="HELD 18-OCTOBER at 10/45/45: no new session over the weekend; the unconfirmed Hormuz mine-strike report is a cost-side input, not a price confirmation. "+s['drivers']

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 16-Oct-2026 session re-checked 18-Oct (English and German overviews agree; no later row)",W])
d['sources'].append([L_HZ,S_HZ]); d['sources'].append([L_TE,S_TE])
d['outlook']['sources'].append([L_HZ,S_HZ])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-16'
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
