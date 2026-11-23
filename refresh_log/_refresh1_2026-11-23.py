# Daily data refresh - 2026-11-23 (MONDAY, ~02:35 UTC = ~02:35 London, BEFORE the Monday ring at 13:20 London).
# Board CARRIED on the Friday 20-Nov official (latest published session; verified again: cache-busted EN + DE overviews agree on 20-Nov
# for all five metals, stocks and MTLE 1.09820; Al per-metal table newest row 20-Nov, no later row).
# Refreshed: Hormuz (Straits 23-Nov: 62 holding; Iranian claims of two supertankers hitting mines unconfirmed; Brent $91.93), AL Circle
# (US UBC scrap / Midwest premium futures 21-Nov), Q1-2027 MJP search (no offers).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-23'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-23"; L_ST="Straits Daily Brief - Strait of Hormuz, 23-Nov-2026 (closed; 62 vessels holding; Iranian claims of two supertankers hitting mines unconfirmed; Brent $91.93)"
S_SC="https://www.alcircle.com/news/us-aluminum-can-scrap-falls-0-66-to-2-636-t-as-midwest-premium-futures-weaken-122055"; L_SC="AL Circle - US aluminum can scrap falls 0.66% to $2,636/t as Midwest premium futures weaken (21-Nov-2026)"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3184.5 and B['LME 3-month']['cur']==2831.5 and B['LME warehouse stock (t)']['cur']==223525
assert d['lme_series'][-1][0]=='20-Nov' and d['metals_series']['asof']=='2026-11-20'

O1="COMPILED SUNDAY 22-NOVEMBER-2026 (WEEKEND, NO RING; LME BOARD CARRIED ON THE FRIDAY 20-NOVEMBER OFFICIAL, THE LAST TRADING SESSION OF THE WEEK, RE-VERIFIED THIS RUN)."
N1="COMPILED MONDAY 23-NOVEMBER-2026 BEFORE THE RING (LME BOARD CARRIED ON THE FRIDAY 20-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION, RE-VERIFIED THIS RUN; MONDAY'S OFFICIAL PRINTS 13:20 LONDON)."
O2="COMPILED SUNDAY 22-NOVEMBER-2026 ABOUT 02:40 LONDON - NO LME RING TODAY (WEEKEND). THE BOARD IS CARRIED ON THE FRIDAY 20-NOVEMBER-2026 LME OFFICIAL, THE LAST TRADING SESSION OF THE WEEK, because the market is shut; it was rolled to 20-November by the Saturday run and RE-VERIFIED this run. "
N2="COMPILED MONDAY 23-NOVEMBER-2026 ABOUT 02:35 LONDON - BEFORE TODAY'S LME RING (13:20 LONDON). THE BOARD IS CARRIED ON THE FRIDAY 20-NOVEMBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION; it was rolled to 20-November by the Saturday run and RE-VERIFIED this run. "
O3="COMPLETENESS CHECKS (RE-RUN 22-NOVEMBER)"; N3="COMPLETENESS CHECKS (RE-RUN 23-NOVEMBER)"
cnt={'1':0,'2':0,'3':0,'rv':0}
def f(s):
    for k,a,b in (('1',O1,N1),('2',O2,N2),('3',O3,N3)):
        if a in s: cnt[k]+=s.count(a); s=s.replace(a,b)
    for a,b in (("REVIEWED 22-NOVEMBER: no newer public disclosure","REVIEWED 23-NOVEMBER: no newer public disclosure"),("REVIEWED 22-NOVEMBER. NO NEW DATED","REVIEWED 23-NOVEMBER. NO NEW DATED")):
        if a in s: cnt['rv']+=1; s=s.replace(a,b)
    return s
for k in list(d.keys()):
    if k in ('report_date','ew','sources'): continue
    d[k]=walk(d[k],f)
print(cnt)

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 20-NOVEMBER-2026 LME OFFICIAL, the latest published session. THIS MONDAY 23-NOVEMBER RUN IS COMPILED AT ABOUT 02:35 LONDON, BEFORE TODAY'S RING; Monday's official prints at 13:20 London, so Friday's official is the correct latest figure - it is not lagging, and nothing was estimated or taken intraday. Next print: Monday 23-November, 13:20 London.")
C[1]=("SOURCE CHECK THIS RUN (23-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched again and AGREE on every price, stock and FX figure for the 20-November session (aluminium cash 3,184.50, three-month 2,831.50, stock 223,525; copper 12,230.50/12,237.00; nickel 15,310.00/15,490.00; zinc 3,670.00/3,502.50; lead 1,825.00/1,861.00; EUR/USD MTLE 1.09820); the aluminium per-metal daily table shows 20-November as its newest row with NO later row.")
hit=0
for i,cv in enumerate(C):
    if cv.startswith("FETCH NOTE"):
        hit+=1
        C[i]=("FETCH NOTE 23-NOVEMBER (MONDAY, PRE-RING): no authorised fetch was blocked. The Westmetall EN and DE overviews and the aluminium per-metal table, AL Circle news (and its 21-November US scrap/Midwest premium futures article) and the Straits Daily Brief (23-November) were fetched. Copper, nickel, zinc and lead per-metal tables were not re-fetched because the overviews show the same 20-November session the Saturday run verified against those tables. Trading Economics macro rows are CARRIED from the Friday 20-November session. A WebSearch for Q1-2027 Japanese premium offers located none; the latest public reference remains S&P Global's report of participant expectations of $190-200/t for Q1 talks - an expectation, not an offer.")
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        hit+=1
        C[i]=cv.replace("The Straits Daily Brief (22-November) shows Brent settled $92.57 at Friday's close","The Straits Daily Brief (23-November) shows Brent at $91.93 in early Monday Asian trade (23:49 UTC Sunday), down 0.69% from Friday's settle")
assert hit==2

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=(" UPDATE 23-NOVEMBER: Straits Daily Brief - still listed as CLOSED; latest IMF PortWatch count still 2 transits on 15-November; AIS-visible vessels holding rose again to 62 (from 58). Iranian state outlets (Press TV, Mehr) claim two supertankers struck naval mines or exploded east of the Strait after ignoring IRGC instructions - NOT confirmed by any maritime authority. No reopening agreement. Trend held at UP.")
        r['trend']='up'; hit+=1
assert hit==1
d['outlook']['ai_analysis'].insert(0,"MONDAY 23-NOVEMBER (PRE-RING, BOARD CARRIED ON THE 20-NOVEMBER OFFICIAL): no new LME print yet - three-month $2,831.50, cash $3,184.50, backwardation $353.00, stock 223,525 t. Weekend Gulf news stayed supply-negative: vessels holding near Hormuz rose to 62 and Iranian state media claim (unconfirmed) two supertankers hit mines, while Brent eased to about $91.9 in early Asian trade. In the US, AL Circle reports Midwest premium futures weakening (first-month $2,388.81/t on 17-November, third-month $2,065/t) - the forward curve prices a lower duty-paid premium ahead. Today's 13:20 official is the test of the $2,800-2,850 zone.")

for p in d['producer_status']: p['asof']=RD

d['so_what']={"line":"Monday pre-ring: LME aluminium sits on Friday's settings - three-month $2,831.50 just above the $2,800-2,850 support with a $353 cash premium over three-month - while Gulf shipping risk keeps building (62 vessels holding, unconfirmed Iranian claims of mine strikes) and US Midwest premium futures point lower.",
 "points":[
 "WHAT MOVED: no LME session since Friday; today's official prints at 13:20 London. Friday closed three-month at $2,831.50 (about -6.2% on the week) and cash at $3,184.50, a $353 backwardation (cash above three-month), with visible stock 223,525 t.",
 "WHY IT MATTERS: a falling forward and a very tight prompt market at the same time - the curve rewards selling nearby metal rather than storing it, and leaves prices sensitive to any Gulf supply shock.",
 "48H DEVELOPMENTS: vessels holding near Hormuz rose to 62; Iranian state media claim two supertankers hit mines east of the Strait (unconfirmed by maritime authorities), after UKMTO's confirmed tanker strike on 21-November; Iran's foreign minister has signalled conditional readiness for talks. US Midwest premium futures are pricing a lower premium (first-month about $2,389/t vs third-month $2,065/t).",
 "WHAT TO WATCH: Monday's official against $2,800-2,850 (a settle below about $2,803 opens a deeper leg), whether the mine-strike claims are confirmed, any US-Iran contact on Hormuz, and first Q1-2027 Japanese premium offers (none reported; earlier talk $190-200/t)."]}

d['feed']=([
 {"when":"Mon 23-Nov","impact":"Bullish","text":"HORMUZ: vessels holding rise to 62; Iranian state media claim two supertankers hit mines east of the Strait - unconfirmed (Straits brief 23-Nov)."},
 {"when":"Sat 21-Nov","impact":"Bearish","text":"US PREMIUM: Midwest premium futures weaken - first-month $2,388.81/t vs third-month $2,065/t; UBC scrap -0.66% to $2,636/t (AL Circle)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ: UNCONFIRMED IRANIAN CLAIMS OF MINE STRIKES; VESSELS HOLDING RISE TO 62 (Straits Daily Brief, 23-November): Iranian state outlets claim two supertankers struck naval mines or exploded east of the Strait after ignoring IRGC navigation instructions - no maritime authority has confirmed this. The Strait is listed as closed; 62 AIS-visible vessels were holding (from 58); the latest IMF PortWatch count is 2 transits on 15-November against 85/day pre-crisis. Brent was about $91.93 in early Monday Asian trade."},
 {"theme":"Premiums","horizon":"0-3 months","impact":"Bearish","url":S_SC,
  "headline":"US MIDWEST PREMIUM FUTURES WEAKEN (AL Circle, 21-November): the first-month Midwest premium contract closed at $2,388.81/t on 17-November with third-month at $2,065/t, a steep backwardation pointing to a lower duty-paid premium ahead; the spot Midwest premium was $1.12/lb on 4-November, down from a record $1.19/lb in late May. US UBC scrap fell 0.66% to $2,635.63/t on 18-November."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 20-Nov-2026 session RE-VERIFIED 23-Nov pre-ring (EN and DE overviews agree; Al per-metal table newest row 20-Nov, no later row)",W])
for x in ([L_ST,S_ST],[L_SC,S_SC]): d['sources'].append(x)
for x in ([L_ST,S_ST],[L_SC,S_SC]): d['outlook']['sources'].append(x)

for k in ('short_term','long_term'):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 22-NOVEMBER'),k
    w=w.replace("REVIEWED 22-NOVEMBER (WEEKEND, NO NEW SESSION): count, targets, alternates and invalidation levels unchanged from the 21-November review below. ","",1)
    d['ew'][k]['writeup']="REVIEWED 23-NOVEMBER (MONDAY PRE-RING, NO NEW SESSION SINCE 20-NOVEMBER): count, targets, alternates and invalidation levels unchanged from the 21-November review below; Monday's official is the next test. "+w
d['ew']['updated']=RD

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-20',3184.5,2831.5,223525]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
