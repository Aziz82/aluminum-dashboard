# Daily data refresh - 2026-11-22 (SUNDAY, ~02:40 UTC; no LME ring). Board CARRIED on the Friday 20-Nov official (verified again this run:
# cache-busted EN + DE overviews agree on 20-Nov for all five metals, stocks and MTLE 1.09820; Al per-metal table newest row 20-Nov, no later row).
# Refreshed: Hormuz (Straits 22-Nov: 58 holding, UKMTO tanker strike 21-Nov off Khasab, Araghchi talks), AL Circle news, Q1-2027 MJP search (no offers).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-22'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-22"; L_ST="Straits Daily Brief - Strait of Hormuz, 22-Nov-2026 (closed; 58 vessels holding; UKMTO tanker strike 21-Nov ~11nm N of Khasab; Brent $92.57)"
S_IN="https://www.alcircle.com/news/inola-residents-weigh-environmental-risks-of-proposed-750-000-tonne-aluminium-smelter-122049"; L_IN="AL Circle - Inola residents weigh environmental risks of proposed 750,000 t Oklahoma smelter (21-Nov-2026)"
S_KA="https://www.alcircle.com/news/korea-aluminium-s-us-tariff-dispute-puts-base-group-s-150m-trump-linked-deal-under-scrutiny-122051"; L_KA="AL Circle - Korea Aluminium's US tariff dispute (preliminary rate up to 105.8% on foil) (21-Nov-2026)"
S_GU="https://www.alcircle.com/news/al-circle-analysis-guineas-183mt-bauxite-output-china-s-46mt-aluminium-push-indonesias-2-77bt-reserves-rewrite-global-supply-scene-122057"; L_GU="AL Circle Analysis - Guinea 183 Mt bauxite, China 46 Mt aluminium push, Indonesia 2.77 bt reserves (21-Nov-2026)"
S_HK="https://www.alcircle.com/news/aluminium-prices-jump-26-squeezing-hyundai-and-kia-s-automotive-profitability-122042"; L_HK="AL Circle - Aluminium prices jump 26%, squeezing Hyundai and Kia profitability (20-Nov-2026)"
S_MJ="https://www.spglobal.com/energy/en/news-research/latest-news/metals/101326-japanese-q4-aluminum-premium-falls-35-to-255mt-cif-japan"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==3184.5 and B['LME 3-month']['cur']==2831.5 and B['LME warehouse stock (t)']['cur']==223525
assert d['lme_series'][-1][0]=='20-Nov' and d['metals_series']['asof']=='2026-11-20'

O1="COMPILED SATURDAY 21-NOVEMBER-2026 (WEEKEND, NO RING; LME BOARD ROLLED TWO SESSIONS TO THE FRIDAY 20-NOVEMBER OFFICIAL, THE LAST TRADING SESSION OF THE WEEK)."
N1="COMPILED SUNDAY 22-NOVEMBER-2026 (WEEKEND, NO RING; LME BOARD CARRIED ON THE FRIDAY 20-NOVEMBER OFFICIAL, THE LAST TRADING SESSION OF THE WEEK, RE-VERIFIED THIS RUN)."
O2="COMPILED SATURDAY 21-NOVEMBER-2026 ABOUT 02:40 LONDON - NO LME RING TODAY (WEEKEND). THE BOARD IS THE FRIDAY 20-NOVEMBER-2026 LME OFFICIAL, THE LAST TRADING SESSION OF THE WEEK; it ROLLED TWO SESSIONS this run because the Thursday 19-November and Friday 20-November officials were both published after the previous run. "
N2="COMPILED SUNDAY 22-NOVEMBER-2026 ABOUT 02:40 LONDON - NO LME RING TODAY (WEEKEND). THE BOARD IS CARRIED ON THE FRIDAY 20-NOVEMBER-2026 LME OFFICIAL, THE LAST TRADING SESSION OF THE WEEK, because the market is shut; it was rolled to 20-November by the Saturday run and RE-VERIFIED this run. "
O3="COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched"
N3="COMPLETENESS CHECKS (RE-RUN 22-NOVEMBER): (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched again"
cnt={'1':0,'2':0,'3':0,'rv':0}
def f(s):
    for k,a,b in (('1',O1,N1),('2',O2,N2),('3',O3,N3)):
        if a in s: cnt[k]+=s.count(a); s=s.replace(a,b)
    for a,b in (("REVIEWED 21-NOVEMBER: no newer public disclosure","REVIEWED 22-NOVEMBER: no newer public disclosure"),("REVIEWED 21-NOVEMBER. NO NEW DATED","REVIEWED 22-NOVEMBER. NO NEW DATED")):
        if a in s: cnt['rv']+=1; s=s.replace(a,b)
    return s
for k in list(d.keys()):
    if k in ('report_date','ew','sources'): continue
    d[k]=walk(d[k],f)
print(cnt); assert cnt['1']>=8 and cnt['2']>=5, cnt

C=d['caveats']
assert C[0].startswith("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 20-NOVEMBER-2026")
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 20-NOVEMBER-2026 LME OFFICIAL, the last trading session before the weekend. THIS SUNDAY 22-NOVEMBER RUN IS COMPILED AT ABOUT 02:40 LONDON; THERE IS NO LME RING ON SATURDAY OR SUNDAY, so the board is CARRIED ON FRIDAY'S OFFICIAL because the market is shut - it is not lagging, and nothing was estimated. The board was rolled to 20-November by the Saturday run and is unchanged this run. Next print: Monday 23-November, 13:20 London.")
C[1]=("SOURCE CHECK THIS RUN (22-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched again and AGREE on every price, stock and FX figure for the 20-November session (aluminium cash 3,184.50, three-month 2,831.50, stock 223,525; copper 12,230.50/12,237.00; nickel 15,310.00/15,490.00; zinc 3,670.00/3,502.50; lead 1,825.00/1,861.00; EUR/USD MTLE 1.09820); the aluminium per-metal daily table shows 20-November as its newest row with NO later row, confirming the board is complete for the week.")
hit=0
for i,cv in enumerate(C):
    if cv.startswith("FETCH NOTE"):
        hit+=1
        C[i]=("FETCH NOTE 22-NOVEMBER (SUNDAY, WEEKEND): no authorised fetch was blocked. The Westmetall EN and DE overviews and the aluminium per-metal table, AL Circle news and the Straits Daily Brief (22-November) were fetched. Copper, nickel, zinc and lead per-metal tables were not re-fetched because the overviews show the same 20-November session the Saturday run verified against those tables. Trading Economics macro rows are CARRIED from the Friday 20-November session (no trading since). A WebSearch for Q1-2027 Japanese premium offers located none; the latest public reference remains S&P Global's report of participant expectations of $190-200/t for Q1 talks - an expectation, not an offer.")
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        hit+=1
        C[i]=cv.replace("The Straits Daily Brief (21-November) shows Brent $92.56","The Straits Daily Brief (22-November) shows Brent settled $92.57 at Friday's close")
assert hit==2

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=(" UPDATE 22-NOVEMBER: Straits Daily Brief - still listed as CLOSED; latest IMF PortWatch count still 2 transits on 15-November (week-old); AIS-visible vessels holding rose to 58 (from 48). UKMTO reported an outbound tanker struck by an unknown projectile about 11 nm north of Khasab, Oman, on 21-November (no casualties) - a second confirmed strike in two days; a report of two tankers hit is not confirmed against a UKMTO release, and Iranian claims of mine strikes remain unconfirmed by any maritime authority. Multiple outlets attribute to Foreign Minister Araghchi a readiness for talks with the US on reopening, with conditions; no agreement announced. Trend held at UP.")
        r['trend']='up'; hit+=1
assert hit==1
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Mon 23-Nov':
        cat['event']=cat['event'].replace("first Q1-2027 Japanese premium off","any US-Iran talks on reopening Hormuz (Araghchi signalled readiness with conditions, 22-November); first Q1-2027 Japanese premium off",1)
d['outlook']['ai_analysis'].insert(0,"SUNDAY 22-NOVEMBER (WEEKEND, BOARD CARRIED ON THE 20-NOVEMBER OFFICIAL): no price change - three-month $2,831.50, cash $3,184.50, backwardation $353.00, stock 223,525 t. The weekend news flow tilts supply risk higher rather than lower: UKMTO confirmed a second projectile strike on a tanker near the Strait of Hormuz in two days (21-November, off Khasab) and vessels holding rose to 58, while Iran's foreign minister signalled readiness for conditional talks on reopening - a two-sided risk for Gulf metal flows into Monday. No Q1-2027 Japanese premium offer has been reported yet.")

for p in d['producer_status']:
    p['asof']=RD
    if p['name']=='EGA (Al Taweelah)':
        p['update']=("ALSO NOTED 22-NOVEMBER (AL Circle, 21-November): the proposed up-to-750,000 t/yr Oklahoma Primary Aluminum smelter at Inola - a joint project of EGA and Century Aluminum - remains under state environmental review (ODEQ reviewing an earlier study; detailed air modelling still in development; no permit reported); a Jacobs risk evaluation presented at a town meeting estimates 328 t/yr of fluoride releases. This does not change the Al Taweelah status. ")+p['update']

d['so_what']={"line":"Weekend: LME aluminium stays on Friday's settings - three-month $2,831.50 below the $2,894 support with a record-for-this-series $353 cash premium over three-month - while a second confirmed tanker strike near Hormuz and Iranian talk of conditional reopening talks make Gulf supply the swing factor for Monday.",
 "points":[
 "WHAT MOVED: nothing on the LME (no weekend trading). The week closed with three-month at $2,831.50 (about -6.2% on the week) and cash at $3,184.50, a $353 backwardation (cash above three-month), with visible stock at 223,525 t after renewed draws.",
 "WHY IT MATTERS: the forward is pricing a hawkish Fed, a strong dollar and forecasts of a 2027 surplus, while prompt metal stays scarce - an unusually steep curve that rewards selling nearby metal rather than storing it.",
 "48H DEVELOPMENTS: UKMTO confirmed a tanker hit by a projectile about 11 nm north of Khasab on 21-November, the second confirmed strike in two days, and vessels holding near the Strait rose to 58; Iran's foreign minister was reported ready for conditional talks with the US on reopening. In the US, a 750 kt Oklahoma smelter project remains under environmental review.",
 "WHAT TO WATCH: Monday's official against the $2,800-2,850 zone (a settle below about $2,803 opens a deeper leg), any US-Iran contact on Hormuz, and first Q1-2027 Japanese premium offers (none reported yet; earlier market talk was $190-200/t)."]}

d['feed']=([
 {"when":"Sat 21-Nov","impact":"Bullish","text":"HORMUZ: UKMTO reports an outbound tanker struck by a projectile ~11 nm north of Khasab; vessels holding rise to 58 (Straits brief 22-Nov)."},
 {"when":"Sun 22-Nov","impact":"Bearish","text":"HORMUZ DIPLOMACY: Iran's FM Araghchi reported ready for conditional talks with the US on reopening the Strait; no agreement (Straits brief)."},
 {"when":"Sat 21-Nov","impact":"Mixed","text":"US SUPPLY: 750 kt/yr Inola, Oklahoma smelter project (EGA/Century) still under ODEQ environmental review; fluoride concerns raised (AL Circle)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ: SECOND CONFIRMED TANKER STRIKE IN TWO DAYS (Straits Daily Brief, 22-November): UKMTO reported an outbound tanker struck by an unknown projectile about 11 nautical miles north of Khasab, Oman, on 21-November, with no casualties; a secondary report of two tankers hit is not confirmed against a UKMTO release, and Iranian claims of mine strikes remain unconfirmed. The Strait is listed as closed; AIS-visible vessels holding rose to 58 (from 48); the latest IMF PortWatch count is 2 transits on 15-November against 85/day pre-crisis."},
 {"theme":"Hormuz","horizon":"0-3 months","impact":"Bearish","url":S_ST,
  "headline":"IRAN SIGNALS CONDITIONAL TALKS ON REOPENING (Straits Daily Brief, 22-November): twelve outlets attribute to Foreign Minister Araghchi a readiness for talks with the US on reopening the Strait, with conditions; reports differ on terms and no agreement has been announced. A reopening would ease Gulf metal and alumina logistics - bearish for regional premiums if it materialises."},
 {"theme":"Supply","horizon":"Structural","impact":"Mixed","url":S_IN,
  "headline":"OKLAHOMA SMELTER UNDER ENVIRONMENTAL REVIEW (AL Circle, 21-November): the proposed up-to-750,000 t/yr Inola smelter, a joint project of EGA and Century Aluminum (Oklahoma Primary Aluminum), is under review by the Oklahoma DEQ; a Jacobs evaluation estimates 328 t/yr of fluoride releases and recommends independent off-site monitoring. No permit or construction timeline was reported."},
 {"theme":"Policy","horizon":"0-3 months","impact":"Mixed","url":S_KA,
  "headline":"US TRADE ENFORCEMENT ON ALUMINIUM FOIL (AL Circle, 21-November): a July US Commerce preliminary ruling could raise the duty on Korea Aluminium's US foil exports to 105.8% over alleged rerouting of Chinese-origin foil via South Korea - a reminder that anti-circumvention enforcement adds to the Section 232 tariff wall."},
 {"theme":"Demand","horizon":"0-3 months","impact":"Bullish (margin)","url":S_HK,
  "headline":"HIGHER ALUMINIUM COSTS SQUEEZE AUTOMAKERS (AL Circle, 20-November): aluminium prices up about 26% are weighing on Hyundai and Kia's profitability per their quarterly reporting - cost pass-through pressure on downstream users."},
 {"theme":"Supply","horizon":"Structural","impact":"Bearish","url":S_GU,
  "headline":"AL CIRCLE ANALYSIS (21-November): Guinea's 183 Mt bauxite output, China's push toward 46 Mt of aluminium and Indonesia's 2.77 bt bauxite reserves are reshaping the global raw-material and supply picture."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 20-Nov-2026 session RE-VERIFIED 22-Nov (EN and DE overviews agree; Al per-metal table newest row 20-Nov, no later row - weekend)",W])
for x in ([L_ST,S_ST],[L_IN,S_IN],[L_KA,S_KA],[L_GU,S_GU],[L_HK,S_HK]): d['sources'].append(x)
for x in ([L_ST,S_ST],[L_IN,S_IN]): d['outlook']['sources'].append(x)

# EW: count unchanged (no new session); refresh dated prefix only
for k in ('short_term','long_term'):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 21-NOVEMBER'),k
    d['ew'][k]['writeup']="REVIEWED 22-NOVEMBER (WEEKEND, NO NEW SESSION): count, targets, alternates and invalidation levels unchanged from the 21-November review below. "+w
d['ew']['updated']=RD

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-20',3184.5,2831.5,223525]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
