# Daily data refresh - 2026-11-08 (SUNDAY, ~02:40 UTC). No ring Sat/Sun: board CARRIED on the FRIDAY 06-Nov LME official.
# Westmetall cache-busted EN + DE overviews re-fetched: both show 06-Nov (Al cash 3,117 / 3M 3,050 / stock 227,600; MTLE 1.11690);
# aluminium and copper per-metal tables: newest row 06-Nov, NO later row. No board number changes this run.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-08'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-08"; L_ST="Straits Daily Brief - Strait of Hormuz, 08-Nov-2026 (AI-assisted)"
S_TR="https://www.alcircle.com/news/trimet-seeks-changes-to-alcoa-south32-deal-concerned-over-reduced-independent-alumina-supply-in-brazil-121881"; L_TR="AL Circle - Trimet asks CADE to block/remedy Alcoa-South32 alumina deal (07-Nov-2026)"
S_AN="https://www.alcircle.com/news/al-circle-analysis-alumina-prices-fall-22-ghana-advances-bauxite-projects-global-aluminium-production-rises-2-1-121875"; L_AN="AL Circle Analysis - overseas alumina 9M-2026 avg ~$321/t (-22% y/y, per Nanshan); IAI Q3 output 18.377 Mt (07-Nov-2026)"
S_DS="https://www.alcircle.com/news/downstream-aluminium-producers-operating-rates-increased-slightly-this-week-and-the-divergence-between-sectors-continues-121865"; L_DS="AL Circle/SMM - China downstream operating rates, week to 06-Nov-2026"
cash,m3,stk=3117.0,3050.0,227600
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==cash and B['LME 3-month']['cur']==m3 and B['LME warehouse stock (t)']['cur']==stk
assert d['lme_series'][-1]==["06-Nov",cash,m3,stk]

REPL=[("COMPILED SATURDAY 07-NOVEMBER-2026 ABOUT 02:35 LONDON. THERE IS NO LME RING ON SATURDAY, SO THE BOARD IS THE FRIDAY 06-NOVEMBER-2026 LME OFFICIAL - THE LAST TRADING SESSION AND THE CORRECT FIGURE TO CARRY UNTIL MONDAY. ",
       "COMPILED SUNDAY 08-NOVEMBER-2026 ABOUT 02:40 LONDON. THERE IS NO LME RING ON SATURDAY OR SUNDAY, SO THE BOARD IS THE FRIDAY 06-NOVEMBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND - THE LAST TRADING SESSION AND THE CORRECT FIGURE UNTIL MONDAY 09-NOVEMBER. RE-CHECKED 08-NOVEMBER: the cache-busted Westmetall English and German overviews still show the identical 06-November session and the aluminium and copper per-metal tables show NO row after 06-November. "),
      ("COMPILED SATURDAY 07-NOVEMBER-2026 (LME BOARD ON THE FRIDAY 06-NOVEMBER OFFICIAL, THE LAST TRADING SESSION; NO RING ON SATURDAY).",
       "COMPILED SUNDAY 08-NOVEMBER-2026 (LME BOARD CARRIED ON THE FRIDAY 06-NOVEMBER OFFICIAL, THE LAST TRADING SESSION; NO RING AT WEEKENDS)."),
      ("REVIEWED 07-NOVEMBER: no newer public disclosure","REVIEWED 08-NOVEMBER: no newer public disclosure"),
      ("REVIEWED 07-NOVEMBER. NO NEW DATED","REVIEWED 08-NOVEMBER. NO NEW DATED")]
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

# Hormuz risk + cost floor
hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 08-NOVEMBER: Straits Daily Brief (AI-assisted) - strait still listed CLOSED; latest lagged transit count 1 vessel on 01-November vs 85/day; US Central Command reportedly disabled a cargo vessel in the Gulf of Oman that tried to break the US blockade of Iran; Iranian navy mine/fire claims remain UNCONFIRMED by any maritime authority; UN counts 25 seafarers killed since 28-February; 138 vessels holding. The Guardian reports a Qatari proposal to reopen the strait as part of ending the war - no agreement announced. Trend held at UP."; r['trend']='up'; hit+=1
assert hit==1
for c in d['outlook']['catalysts']:
    if c['date']=='Daily, from Mon 09-Nov':
        c['event']="CARRIED THROUGH THE WEEKEND (re-checked 08-November, no new session). "+c['event']
d['outlook']['ai_analysis'].insert(0,"SUNDAY 08-NOVEMBER, BOARD CARRIED ON THE FRIDAY 06-NOVEMBER OFFICIAL (no ring at weekends; Westmetall re-checked): three-month $3,050.00, cash $3,117.00, a $67.00 backwardation, LME stock 227,600 t; weights unchanged at 15/45/40. Weekend developments are structural rather than price-moving: Trimet has asked Brazil's competition authority CADE to block or remedy Alcoa's acquisition of South32's alumina and bauxite assets, arguing the combined group would hold about 52.7% of the Western merchant alumina market (AL Circle, 07-November); overseas alumina averaged about $321/t in January-September, down about 22% y/y (Nanshan, via AL Circle); IAI Q3 primary output rose 2.1% q/q to 18.377 Mt. Hormuz remains closed with a Qatari reopening proposal reported but no agreement. Monday's test is unchanged: 3,077 above, 3,042 then 3,024.50 below.")
pre="REVIEWED 08-NOVEMBER (WEEKEND, NO NEW SESSION): the count is unchanged from the 07-November review because there has been no official since Friday's 3,050.00; no pivot is added or re-labelled and no invalidation level is touched. "
d['ew']['short_term']['writeup']=pre+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']=pre+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('Alcoa'):
        p['update']="UPDATED 08-NOVEMBER (AL Circle, 07-November): Germany's Trimet has asked Brazil's competition authority CADE to block Alcoa's acquisition of South32's Alumar, MRN and Worsley interests or impose remedies (divesting integrated bauxite/alumina assets in Brazil or Western Australia, changes to Alumar/MRN ownership links, independent monitoring of alumina price reporting), saying the combined group would hold about 51.8% of Brazil's merchant alumina sales and 52.66% of the Western merchant market, and could redirect about 3 Mt/y of South32's third-party alumina to Alcoa smelters ("+S_TR+"). "+p['update']
    elif p['name'].startswith('EGA'):
        p['update']="REVIEWED 08-NOVEMBER: no newer EGA release located; latest company figure remains 631 of 1,262 cells (21-October), full output targeted Q1-2027. "+p['update']
    elif p['name'].startswith('China operators'):
        p['update']="REVIEWED 08-NOVEMBER: no new SMM social-inventory print on news.metal.com (weekend); SMM (06-November, via AL Circle) shows downstream operating rates broadly stable, +0.1 pp overall - primary alloy 61.4% (+0.6), wire and cable 64.8% (+0.4), extrusion 52.5% (flat), plate/sheet/strip 68.8% (-0.4), foil 71.0% (-0.1) ("+S_DS+"). "+p['update']
    elif p['name'].startswith('Rio Tinto'):
        p['update']="REVIEWED 08-NOVEMBER: no newer public disclosure located beyond the 06-November workforce review. "+p['update']

d['news']=[
 {"theme":"Alumina","horizon":"0-12 months","impact":"Bullish","url":S_TR,
  "headline":"TRIMET CHALLENGES THE ALCOA-SOUTH32 ALUMINA DEAL (AL Circle, 07-November): the German smelter has asked Brazil's competition authority CADE to block Alcoa's purchase of South32's Alumar, MRN and Worsley interests or require remedies, saying independent Brazilian smelter-grade alumina sellers would fall from three to two, the combined group would hold about 52.66% of the Western merchant alumina market (potentially 61%), and about 3 Mt/y of South32's third-party alumina could be redirected to Alcoa's own smelters. READ: a regulatory risk to the June-2027 deal timeline and a flag on future merchant-alumina availability and price-reporting for non-integrated smelters."},
 {"theme":"Alumina","horizon":"0-6 months","impact":"Bullish (margin)","url":S_AN,
  "headline":"ALUMINA 22% CHEAPER THIS YEAR (AL Circle Analysis, 07-November): overseas alumina averaged about $321/t in January-September 2026, down about 22% y/y, per Nanshan Aluminium International, with a Q3 recovery after a weak first half; IAI data show Q3 global primary aluminium output 18.377 Mt, +2.1% q/q, still below Q3-2025, on GCC restoration and gains in Europe, Oceania and Asia. Ghana is advancing bauxite projects (a proposed RUSAL partnership for up to 5 Mt/y bauxite and a 1.2 Mt/y refinery)."},
 {"theme":"China","horizon":"0-1 month","impact":"Mixed","url":S_DS,
  "headline":"CHINA DOWNSTREAM STEADY (SMM via AL Circle, 06-November): overall downstream operating rate +0.1 pp week on week - primary alloy 61.4% (+0.6), wire and cable 64.8% (+0.4), secondary aluminium 53.9% (+0.6), extrusion 52.5% (flat), plate/sheet/strip 68.8% (-0.4), foil 71.0% (-0.1); finished-goods destocking short of expectations. READ: no demand acceleration into the seasonal slowdown."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Mixed","url":S_ST,
  "headline":"HORMUZ STILL CLOSED; QATARI REOPENING PROPOSAL REPORTED (Straits Daily Brief, 08-November, AI-assisted): latest lagged transit count 1 vessel on 01-November vs an 85/day baseline; US Central Command reportedly disabled a cargo vessel in the Gulf of Oman that tried to break the US blockade of Iran; Iran's mine claims remain UNCONFIRMED; 138 vessels holding; the UN counts 25 seafarers killed since 28-February. The Guardian reports Qatar has proposed reopening the strait as part of an end to the US-Iran war - no agreement announced. Brent closed Friday at $98.32."},
]+d['news']
d['news']=d['news'][:20]
d['feed']=([
 {"when":"Sun 08-Nov","impact":"Mixed","text":"BOARD CARRIED ON THE FRIDAY 06-NOVEMBER OFFICIAL (no ring at weekends; Westmetall re-checked): three-month $3,050.00, cash $3,117.00, backwardation $67.00, stock 227,600 t."},
 {"when":"Sat 07-Nov","impact":"Bullish","text":"TRIMET ASKS BRAZIL'S CADE TO BLOCK OR REMEDY ALCOA'S PURCHASE OF SOUTH32 ALUMINA ASSETS - combined ~52.7% of Western merchant alumina (AL Circle)."},
 {"when":"Sat 07-Nov","impact":"Bullish (margin)","text":"ALUMINA: overseas price averaged ~$321/t in 9M-2026, -22% y/y (Nanshan via AL Circle); IAI Q3 primary output 18.377 Mt (+2.1% q/q)."},
 {"when":"Sun 08-Nov","impact":"Mixed","text":"HORMUZ: still closed (1 transit on 01-Nov, lagged); Qatari reopening proposal reported, no agreement; Iranian mine claims UNCONFIRMED (Straits brief)."},
]+d['feed'])[:12]

d['so_what']={"line":"Weekend check: LME aluminium holds Friday's $3,050 three-month close with prompt metal still tight (a $67 backwardation and record-low 227,600 t LME stock), while a smelter's legal challenge to the Alcoa-South32 alumina deal and a reported Qatari Hormuz proposal are the news to carry into Monday.",
 "points":[
 "WHERE IT STANDS: no LME trading at weekends, so the board is Friday 06-November's official - three-month $3,050.00 (down $30.00 on the week), cash $3,117.00, a $67.00 backwardation (cash above three-month) and LME stock at a new low of 227,600 t. Scenario weights unchanged at 15/45/40.",
 "ALUMINA: Trimet has asked Brazil's competition authority to block or remedy Alcoa's purchase of South32's alumina and bauxite assets, saying the combined group would control about 52.7% of Western merchant alumina (AL Circle, 07-November). Meanwhile overseas alumina averaged about $321/t in January-September, down about 22% y/y, keeping smelter margins wide.",
 "SUPPLY AND DEMAND: IAI shows Q3 global primary output up 2.1% q/q to 18.377 Mt as Gulf capacity returns; Chinese downstream operating rates were broadly flat in the week to 06-November (SMM). Hormuz remains closed to commercial traffic; a Qatari reopening proposal is reported but nothing is agreed.",
 "WHAT TO WATCH: Monday's 09-November official versus $3,077 resistance and $3,042 / $3,024.50 support; whether the backwardation stays above $15; any confirmed Hormuz deal (which would pressure energy and the cost floor further); first Q1-2027 Japanese premium offers (still none public)."]}

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 06-NOVEMBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND BECAUSE THE MARKET IS SHUT (no ring Saturday or Sunday); this Sunday 08-November run changes no board price, stock or FX figure. The next official prints Monday 09-November at 13:20 London. The Thursday 05-November official (cash 3,160.00, three-month 3,097.50, stock 228,475) is recorded in the series. Trading Economics aluminium ($3,065.60 for 06-November) is a reference cited in text only.")
C[1]=("SOURCE CHECK THIS RUN (08-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and still AGREE on the identical 06-November session (aluminium cash 3,117.00, three-month 3,050.00, stock 227,600; EUR/USD MTLE 1.11690), and the aluminium and copper per-metal daily tables show NO row after 06-November, so the board is complete and correctly carried rather than lagging.")
hit=0
for i,cv in enumerate(C):
    if cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 08-NOVEMBER: Westmetall EN and DE overviews, the aluminium and copper per-metal tables, AL Circle, news.metal.com and the Straits Daily Brief were fetched. mining.com returned HTTP 403 and was NOT retried by any other client; a web search was used instead and found no additional dated smelter news. Trading Economics macro pages were not re-fetched because no market traded since Friday - macro rows carry the 06-November readings. news.metal.com showed no SHFE settlement or social-inventory print for the weekend. A search for Q1-2027 Japanese premium offers again found none, so Q1 stays unpriced. The Straits brief is labelled AI-assisted by its publisher and its transit count lags (01-November); Iranian mine claims and the Qatari reopening proposal are cited as reported/UNCONFIRMED."); hit+=1
    elif cv.startswith("PEER EARNINGS:"):
        C[i]=("PEER EARNINGS: NO NEW PEER RESULT AND NO earnings_history BACK-FILL THIS RUN (08-NOVEMBER, weekend). Century Aluminum Q3-2026 and Novelis Q2 FY27 were added on 07-November. "+cv.split(" - CENTURY",1)[0][:0]); hit+=1
    elif cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=cv+" CARRIED THROUGH THE WEEKEND (08-November): no session since Friday; the Straits Daily Brief (08-November) shows Brent's Friday close at $98.32 (+0.03%)."; hit+=1
assert hit==3,hit

for x in ([L_ST,S_ST],[L_TR,S_TR],[L_AN,S_AN],[L_DS,S_DS]): d['sources'].append(x)
d['sources'].insert(0,["Westmetall - LME official prices and stocks, 06-Nov-2026 session re-checked 08-Nov (EN and DE overviews agree; Al and Cu per-metal tables show no later row)",W])
for x in ([L_TR,S_TR],[L_ST,S_ST]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-06',cash,m3,stk]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
