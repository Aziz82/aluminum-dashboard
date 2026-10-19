# Daily data refresh - 2026-10-19 (MONDAY, ~02:35 UTC, BEFORE the 13:20 London ring). Board CARRIED on the FRIDAY 16-Oct LME official - the latest PUBLISHED official.
# Westmetall cache-busted EN + DE overviews re-fetched: both show 16-Oct, identical figures; Al per-metal table shows NO row after 16-Oct. TE aluminium still shows the 16-Oct close 3,008.50.
# New public item: China NBS Q3 GDP / September activity data released 19-Oct 10:00 Beijing (investingLive, 19-Oct 02:01).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-19'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_CN="https://investinglive.com/news/china-q3-gdp-beats-estimates-as-does-september-retail-sales/"; L_CN="investingLive - China Q3 GDP beats estimates, as does September retail sales (19-Oct-2026)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum (re-checked 19-Oct-2026; still the 16-Oct close)"

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("COMPILED SUNDAY 18-OCTOBER-2026","COMPILED MONDAY 19-OCTOBER-2026 (BEFORE THE 13:20 LONDON RING)")
        o=o.replace("REVIEWED 18-OCTOBER: no newer public disclosure","REVIEWED 19-OCTOBER: no newer public disclosure").replace("REVIEWED 18-OCTOBER. NO NEW DATED","REVIEWED 19-OCTOBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status'):
    d[k]=walk(d[k])
for p in d['producer_status']: p['asof']=RD

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 16-OCTOBER-2026 LME OFFICIAL - STILL THE LATEST PUBLISHED OFFICIAL. This Monday 19-October run is compiled about 03:35 London, BEFORE today's ring; Monday's official prints at 13:20 London and will appear on the next run. No board figure changes this run. Reference and intraday prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (19-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and still show the 16-October session with identical prices, stocks and FX fixings (EUR/USD MTLE 1.12570), and the per-metal aluminium daily table shows NO row after 16-October, so the carried board is complete rather than lagging.")
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=cv.replace("carried through the weekend (no new session); they were not re-fetched individually on Sunday 18-October.","carried through the weekend; Trading Economics' aluminium page was re-checked on Monday 19-October and still shows the 16-October close, other macro rows were not re-fetched individually.")
    if cv.startswith("FETCH NOTE 18-OCTOBER"):
        C[i]="FETCH NOTE 19-OCTOBER: no authorised fetch was blocked this run. One AL Circle article returned HTTP 403 and two SMM flash-news links returned 404; those items were NOT used. China's Q3 GDP and September activity data are taken from investingLive's release table (19-October), not from the statistics bureau page directly. No new wire report on Hormuz dated 18-19 October was located; the 17-October mine-strike report remains unconfirmed."

d['so_what']={"line":"China's Q3 growth beat forecasts (4.5% y/y; September industrial output +5.5%) ahead of today's LME ring, but aluminium still sits on Friday's $3,012 three-month - below the July low and $58 lower on the week - with Hormuz keeping energy-cost risk high.",
 "points":[
 "WHERE IT STANDS: the board is still Friday's 16-October LME official - cash $3,014.00, three-month $3,012.00 (+$17.50), a $2.00 backwardation (cash above three-month) and LME stock at a series low of 237,875 t. Monday's official prints at 13:20 London.",
 "NEW THIS MORNING: China's economy grew 4.5% year on year in the third quarter (forecast 4.4%), 1.2% on the quarter; September industrial output rose 5.5% (fastest in six months) and retail sales 1.1% (forecast 0.5%), but fixed-asset investment is still down 7.2% year to date - supportive for metals sentiment, not a construction-demand turn.",
 "THE BEARISH SIDE IS UNCHANGED: ex-China physical offers are weak (SMM, 16-October), China exported 656,000 t of unwrought aluminium and semis in September, and Gulf restarts continue; the unconfirmed 17-October Hormuz mine-strike report is a cost-side risk, not demand.",
 "WHAT TO WATCH: today's ring - three-month back above $3,061.5-3,077 would argue the decline is ending, below about $2,977.5 would open a new leg lower; China's September aluminium output from the statistics bureau; the October carbon-input settlements; the 27-28 October FOMC."]}

d['feed']=([
 {"when":"Mon 19-Oct","impact":"Bullish","text":"China Q3 GDP +4.5% y/y (f'cast 4.4%), +1.2% q/q; September industrial output +5.5%, retail sales +1.1%, fixed-asset investment -7.2% YTD (investingLive). LME board still on the Friday 16-October official; Monday's prints 13:20 London."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"Macro","horizon":"0-1 month","impact":"Mixed","url":S_CN,
  "headline":"CHINA Q3 GROWTH BEATS FORECASTS (statistics bureau data via investingLive, 19-October): GDP rose 4.5% year on year in the third quarter (forecast 4.4%, prior 4.3%) and 1.2% on the quarter (forecast 1.1%); September industrial production rose 5.5% (forecast 5.4%, prior 5.2%) and retail sales 1.1% (forecast 0.5%, prior 0.4%), while fixed-asset investment was down 7.2% year to date (forecast -7.3%). READ: firmer industry and consumer data support metals sentiment at the margin, but investment - the construction-linked part of aluminium demand - is still contracting, so this is a sentiment support rather than a demand turn. Not a board figure."},
]+d['news']
d['news']=d['news'][:20]

d['outlook']['ai_analysis'].insert(0,"MONDAY 19-OCTOBER, PRE-RING: the board still carries Friday's 16-October official (three-month $3,012.00; week -$58.00; stock 237,875 t). China's Q3 GDP (+4.5% y/y, above forecast) and September industrial output (+5.5%) are a modest macro support, but fixed-asset investment remains -7.2% year to date, so the read is unchanged: a bounce inside a still-bearish trend, with today's ring the first test of whether firmer China data and the Hormuz energy-cost floor outweigh weak ex-China physical demand.")

EWS="REVIEWED 19-OCTOBER (MONDAY, BEFORE THE RING; NO NEW SESSION SINCE 16-OCTOBER): count and levels unchanged - wave (v) low at 2,994.50 possible but not confirmed; invalidation 3,289; rule-based cap near 2,977.5. "
st=d['ew']['short_term']['writeup']; st=st.split("REVIEWED 18-OCTOBER (SUNDAY, NO NEW SESSION): the count and levels are unchanged from the 16-October review - wave (v) low at 2,994.50 is possible but not confirmed; invalidation 3,289; rule-based cap near 2,977.5. ",1)[-1]
d['ew']['short_term']['writeup']=EWS+st
lt=d['ew']['long_term']['writeup']; lt=lt.split("REVIEWED 18-OCTOBER (SUNDAY, NO NEW SESSION): the weekly close of 3,012.00 stands; count unchanged. ",1)[-1]
d['ew']['long_term']['writeup']="REVIEWED 19-OCTOBER (PRE-RING): the weekly close of 3,012.00 stands; count unchanged. "+lt
d['ew']['updated']=RD

for s in d['outlook']['scenarios']:
    s['drivers']=s['drivers'].replace("HELD 18-OCTOBER at 10/45/45: no new session over the weekend; the unconfirmed Hormuz mine-strike report is a cost-side input, not a price confirmation. ","HELD 19-OCTOBER at 10/45/45: no new session yet; China's Q3 beat is a sentiment support, the unconfirmed Hormuz report a cost-side input - neither is a price confirmation. ")

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 16-Oct-2026 session re-checked 19-Oct (English and German overviews agree; no later row)",W])
d['sources'].append([L_CN,S_CN]); d['sources'].append([L_TE,S_TE])
d['outlook']['sources'].append([L_CN,S_CN])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-16'
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
