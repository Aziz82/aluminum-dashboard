# Daily data refresh - 2026-10-12 (MONDAY, compiled ~03:30 London BEFORE the Monday ring).
# Board CARRIED at FRIDAY 09-Oct LME official (latest published). Westmetall fetch NOT GRANTED this run
# (permission request withdrawn) -> fallback: rely on 10/11-Oct verification; Trading Economics corroborates 09-Oct as latest print.
# New: SMM 09-Oct overseas premium assessment (CIF Japan MJP spot $230/t), weekend Hormuz strikes (gCaptain 11-Oct),
# Vedanta record Q2 FY27 output (SMM 07-Oct / BSE 03-Oct), Alcoa Q3 results date 15-Oct.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-12'; d['report_date']=RD
S_SMMP="https://news.metal.com/newscontent/104148845-overseas-primary-aluminum-premiums-near-a-floor-as-selling-pressure-eases-smm-analysis"
L_SMMP="SMM - Overseas primary aluminum premiums near a floor as selling pressure eases (09-Oct-2026)"
S_GC="https://gcaptain.com/more-tankers-hit-in-hormuz-as-u-s-strikes-cargo-ship/"
L_GC="gCaptain - More tankers hit in Hormuz as U.S. strikes cargo ship (11-Oct-2026)"
S_VED="https://news.metal.com/newscontent/104144175-vedanta-sets-q2-fy2027-records-in-aluminium-alumina-oil-and-gas-output-drops"
L_VED="SMM - Vedanta sets Q2 FY2027 records in aluminium, alumina (07-Oct-2026; BSE filing 03-Oct)"
S_AA="https://newshub.medianet.com.au/2026/09/alcoa-schedules-third-quarter-2026-earnings-release-and-conference-call/171619/"
L_AA="Alcoa via Medianet - Alcoa schedules Q3-2026 earnings release and conference call (Sep-2026)"
S_SMMS="https://news.metal.com/newscontent/104145345-post-holiday-inventory-buildup-limited-market-mostly-wait-and-see-smm-south-china-spot-aluminum-daily-review"
L_SMMS="SMM - Post-holiday inventory buildup limited; market mostly wait-and-see (South China spot review, 08-Oct-2026)"
S_TE="https://tradingeconomics.com/commodity/aluminum"
L_TE="Trading Economics - Aluminum (latest print 09-Oct-2026, viewed 12-Oct)"

OLD_HDR=("COMPILED SUNDAY 11-OCTOBER-2026. THERE IS NO LONDON METAL EXCHANGE RING ON SATURDAY OR SUNDAY, SO THE FRIDAY 09-OCTOBER-2026 OFFICIAL IS THE CORRECT, LATEST PUBLISHED SESSION AND IS CARRIED THROUGH THE WEEKEND; THE NEXT OFFICIAL PRINTS MONDAY 12-OCTOBER AT 13:20 LONDON. COMPLETENESS CHECKS:")
NEW_HDR=("COMPILED MONDAY 12-OCTOBER-2026 AT ABOUT 03:30 LONDON, BEFORE THE MONDAY RING. THE FRIDAY 09-OCTOBER-2026 OFFICIAL REMAINS THE LATEST PUBLISHED SESSION AND IS CARRIED; MONDAY'S OFFICIAL PRINTS AT 13:20 LONDON. THIS RUN COULD NOT RE-FETCH WESTMETALL (ACCESS NOT GRANTED IN TIME) AND RELIES ON THE 10- AND 11-OCTOBER RUNS' VERIFICATION, CORROBORATED BY TRADING ECONOMICS SHOWING 09-OCTOBER AS ITS LATEST ALUMINIUM PRINT. COMPLETENESS CHECKS (RUN 11-OCTOBER):")
REP=[
 (OLD_HDR,NEW_HDR),
 ("COMPILED SUNDAY 11-OCTOBER-2026, NO LME RING (REVIEWED;","COMPILED MONDAY 12-OCTOBER-2026, BEFORE THE MONDAY RING (REVIEWED;"),
 ("REVIEWED 11-OCTOBER: no newer public disclosure","REVIEWED 12-OCTOBER: no newer public disclosure"),
 ("REVIEWED 11-OCTOBER. NO NEW DATED","REVIEWED 12-OCTOBER. NO NEW DATED"),
 ("COMPILED SUNDAY 11-OCTOBER-2026 (NO LME RING). PREMIUM","COMPILED MONDAY 12-OCTOBER-2026 (BEFORE THE MONDAY RING). PREMIUM"),
 ("CARRIED SUNDAY 11-OCTOBER-2026 (markets shut since Friday; Friday 09-October values first captured on the Saturday run)",
  "CARRIED MONDAY 12-OCTOBER-2026 (compiled before Monday's sessions settle; Friday 09-October closes first captured on the Saturday run)"),
 ("COMPILED SUNDAY 11-OCTOBER-2026.","COMPILED MONDAY 12-OCTOBER-2026 (BEFORE THE MONDAY RING)."),
 ("HELD 11-OCTOBER (weekend, no new session;","HELD 12-OCTOBER (pre-ring Monday, no new session since Friday; weekend Hormuz strikes and SMM's 'premiums near a floor' read roughly offset) AND 11-OCTOBER (weekend;"),
 ("REVIEWED 11-OCTOBER (WEEKEND, NO NEW SESSION; COUNT UNCHANGED). ","REVIEWED 12-OCTOBER (MONDAY, BEFORE THE RING - NO NEW SESSION SINCE FRIDAY; COUNT UNCHANGED). "),
 (" These are offers, not a settlement. THE TARIFF"," THE TARIFF"),
]
cnt={a:0 for a,_ in REP}
def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        for a,b in REP:
            if a in o: cnt[a]+=o.count(a); o=o.replace(a,b)
    return o
d=walk(d)
for a,n in cnt.items(): print(n,'x',a[:70])

# ---- CIF Japan spot: new public assessment (SMM 09-Oct) ----
NOTE_CIF=("CIF JAPAN SPOT REFRESHED THIS RUN TO SMM'S 09-OCTOBER ASSESSMENT: CIF Japan MJP spot $230/t (warehouse-warrant $269/t; FCA South Korea $223/t, CIF South Korea $216/t, CIF Thailand P1020A $249/t), down from the $370/t last public spot carried since Q3. SMM's read is that overseas premiums are 'near a floor' with the outlook 'less bearish', though a stronger rebound needs better downstream orders. The prior $370/t mark and the new $230/t mark are not guaranteed to share one assessor, so the size of the step is indicative. ")
for p in d['premiums']:
    p['src']=p['src'].replace("NO NEW ASSESSMENT ON ANY ROW'S OWN BASIS WAS LOCATED FOR THIS WINDOW, so every row is CARRIED UNCHANGED.",
      NOTE_CIF+"EVERY OTHER ROW IS CARRIED UNCHANGED at its own last public assessment. SMM also cites the US Midwest duty-paid premium at 105 US cents/lb (about $2,315/t) on 09-October - context from a different source, not substituted into the US rows.")
    if p['name'].startswith('CIF Japan'):
        p['prev']=p['cur']; p['cur']=230
        p['src']=p['src']+" | SOURCE: "+L_SMMP+" "+S_SMMP
ph_=d['premium_history']; ph_['labels_reg'][3]="Q4-26 sett. / spot 09-Oct"; ph_['mjp'][3]=255; ph_['cif'][3]=230
d['premium_drivers'].insert(1,{'t':"Spot premiums have fallen below the new quarterly benchmark - but sellers' pressure is easing",
 'd':"SMM's 09-October assessment puts CIF Japan MJP spot at $230/t, $25 beneath the $255/t Q4 quarterly settlement, with Korea at $216-223/t and Thailand at $249/t. SMM concludes the outlook for overseas premiums 'has become less bearish' and premiums may stabilise or recover modestly near term, but a stronger rebound needs clearer improvement in downstream orders and restocking. WHY IT MATTERS: with spot below the quarterly benchmark, remaining Japanese buyers have little reason to settle above $255/t, and the Q1-2027 talks start from a lower spot base.",
 'src':[L_SMMP,S_SMMP]})
d['premium_drivers']=d['premium_drivers'][:4]
d['premium_outlook']=("UPDATE 12-OCTOBER: SPOT HAS SLIPPED BENEATH THE NEW BENCHMARK. SMM (09-October) assesses CIF Japan MJP spot at $230/t against the $255/t Q4 settlement, and calls overseas premiums 'near a floor' as selling pressure eases. Watch whether remaining Japanese buyers settle at $255/t or below, and where Q1-2027 offers open from late November. "+d['premium_outlook'])
C=d['caveats']
C[6]=C[6].replace("PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY, AND NO NEW ASSESSMENT ON ANY ROW'S OWN BASIS WAS LOCATED FOR THIS WINDOW; every premium row is carried at its own assessment date.",
 "PREMIUM ASSESSMENTS ARE PERIODIC, NOT DAILY. ON 12-OCTOBER THE CIF JAPAN SPOT ROW WAS REFRESHED TO SMM'S 09-OCTOBER CIF JAPAN MJP SPOT OF $230/T (from $370/t); the step may partly reflect a change of assessor, so it is indicative. Every other premium row is carried at its own assessment date.")
assert "SMM'S 09-OCTOBER" in C[6]

# ---- caveats 0-2 ----
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 09-OCTOBER-2026 LME OFFICIAL, AND THAT IS STILL THE LATEST PUBLISHED SESSION. This page compiled on MONDAY 12-October at about 03:30 London, before the Monday ring; the 12-October official prints at 13:20 London. Every board value is therefore identical to the weekend runs by design, not stale.")
C[1]=("THIS RUN COULD NOT RE-FETCH WESTMETALL: access to the Westmetall pages was not granted in time, so the board relies on the prior runs' verification (11-October: aluminium per-metal daily table showed 09-October as the newest row with NO ROW AFTER IT). Trading Economics, viewed 12-October, independently shows 09-October as its latest aluminium print. No market session has occurred since then, so no newer official can exist.")
C[2]=("THE ENGLISH AND GERMAN WESTMETALL OVERVIEWS WERE LAST RE-REQUESTED CACHE-BUSTED ON 11-OCTOBER AND AGREED EXACTLY on 09-October across all six metals, stocks and FX fixings (EUR/USD MTLE 1.12090). They were not re-checked on 12-October (see above).")

# ---- inputs summary / producers ----
d['inputs_summary']=("UPDATE 12-OCTOBER (MONDAY, BEFORE THE RING): copper is carried at the Friday 09-October LME official cash of $14,689.00, its fifteen-session window unchanged until Monday's official prints. No new input mark was located since Friday; every row is carried at its own dated public mark and nothing was interpolated. The mid-October carbon settlement cycle (anodes, pitch, green coke) is due around 17-18 October.")
for p in d['producer_status']: p['asof']=RD

# ---- so what ----
d['so_what']={"line":"Aluminium enters Monday on its early-July floor near $3,060, and spot Japanese premiums have already slipped beneath the new $255/t quarterly benchmark - the physical market is still confirming weakness, while weekend Hormuz strikes keep Gulf logistics risk live.",
 "points":[
 "WHAT MOVED: no LME session since Friday. The 09-October official settled cash $3,055.50 and three-month $3,070.00 ($14.50 contango), stock 238,875 t; three-month fell 1.67% on the week. Monday's official prints at 13:20 London.",
 "PREMIUMS: SMM (09-October) puts CIF Japan MJP spot at $230/t, $25 under the $255/t Q4 settlement, with Korea at $216-223/t; SMM sees premiums 'near a floor' as selling pressure eases.",
 "SUPPLY AND RISK: Vedanta reported record quarterly aluminium output of 649,000 t (+5% y/y) and alumina of 895,000 t (+37%) for July-September, adding to the recovery narrative. Against that, two more outbound tankers were struck in Hormuz on 10-11 October and US forces disabled a cargo ship in the Gulf of Oman (gCaptain).",
 "WHAT TO WATCH: Monday's official against $3,061.5 - a settled break opens $2,980-3,000; China's first full post-holiday inventory prints; Alcoa's Q3 results on Thursday 15-October after the New York close, which open the producer reporting season; and the mid-October carbon settlements."]}

d['feed']=([
 {"when":"Mon 12-Oct","impact":"Mixed","text":"PRE-RING MONDAY - BOARD CARRIED AT THE FRIDAY 09-OCTOBER LME OFFICIAL (cash $3,055.50, three-month $3,070.00, contango $14.50, stock 238,875 t), still the latest published session; Monday's official prints 13:20 London."},
 {"when":"Sun 11-Oct","impact":"Bullish","text":"HORMUZ: two outbound tankers struck on 10 and 11 October (one caught fire; crews safe), and US forces disabled the cargo ship Ocean Molica in the Gulf of Oman - the fourth commercial vessel disabled since the blockade resumed on 14-July (gCaptain)."},
 {"when":"Fri 09-Oct","impact":"Bearish","text":"SMM: CIF Japan MJP spot $230/t, beneath the $255/t Q4 settlement; Korea $216-223/t; premiums seen 'near a floor' as selling pressure eases."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"Logistics","horizon":"0-3 months","impact":"Bullish","url":S_GC,
  "headline":"MORE TANKERS HIT IN HORMUZ AS US STRIKES A CARGO SHIP (gCaptain, 11-October): two outbound tankers were struck in the strait - one at about 19:20 UTC on 10-October, which caught fire, and another on 11-October - with all crew reported safe; the crude carrier GEM NO.2 was hit off the UAE on Friday. US forces disabled the cargo vessel Ocean Molica in the Gulf of Oman, the fourth commercial vessel disabled since the blockade of Iranian ports resumed on 14-July, alongside 135 ships turned around. For aluminium this keeps Gulf export logistics, freight and war-risk costs elevated even as Gulf smelter output recovers."},
 {"theme":"Premiums","horizon":"0-3 months","impact":"Bearish","url":S_SMMP,
  "headline":"SPOT ASIAN PREMIUMS SLIP BELOW THE NEW BENCHMARK, BUT SMM SEES A FLOOR (SMM, 09-October): CIF Japan MJP spot $230/t and warehouse-warrant $269/t against the $255/t Q4 settlement; FCA South Korea $223/t, CIF South Korea $216/t, CIF Thailand $249/t; US Midwest duty-paid 105 cents/lb. SMM says the outlook 'has become less bearish' but a stronger rebound needs better downstream orders and restocking."},
 {"theme":"Supply","horizon":"1-6 months","impact":"Bearish","url":S_VED,
  "headline":"VEDANTA POSTS RECORD QUARTERLY ALUMINIUM AND ALUMINA OUTPUT (SMM, 07-October; BSE filing 03-October): Q2 FY2027 aluminium 649,000 t, up 5% year on year and the highest in company history; alumina 895,000 t, up 37%; first-half aluminium 1.281 Mt (+5%) and alumina 1.721 Mt (+39%). Rising ex-China output adds to the supply-recovery story weighing on prices and premiums."},
 {"theme":"China","horizon":"0-1 month","impact":"Mixed","url":S_SMMS,
  "headline":"CHINA'S POST-HOLIDAY STOCK BUILD LIMITED, DEMAND WAIT-AND-SEE (SMM South China spot review, 08-October): post-National Day arrivals produced only a limited inventory build; spot traded at a 230-270 yuan/t premium to SHFE 2610 as sellers cut offers, with weak intermediate demand and a widening SHFE backwardation."},
]+d['news'][:16]

d['outlook']['ai_analysis'].insert(0,"MONDAY PRE-RING REVIEW, 12-OCTOBER: no session since Friday's $3,070.00 three-month weekly close on the 3,061.5 July floor. New public evidence leans bearish on the physical side - SMM's CIF Japan spot at $230/t sits below the $255/t Q4 benchmark and Vedanta reported record output - while weekend tanker strikes in Hormuz keep the logistics risk premium alive. The bias stays bearish into Monday's test of the July low; Alcoa's Q3 results on 15-October are the first producer read of how Q3 prices and premiums flowed through.")

# ---- catalysts / earnings note ----
cats=d['outlook']['catalysts']
assert cats[2]['date'].startswith('Passed Mon 05-Oct')
cats[2]={'date':'Thu 15-Oct (after NYSE close)','impact':'Medium','event':"ALCOA Q3-2026 RESULTS OPEN THE PRODUCER REPORTING SEASON: release after the New York close on 15-October, call at 17:00 EDT (Alcoa via Medianet). The first public read of how Q3's record $395/t Japanese premium, the tariff-inflated US Midwest premium and the cut 9.5-9.6 Mt alumina guidance flowed into producer results."}
d['earnings_note']=("SEASON DATE CONFIRMED: Alcoa reports Q3-2026 on Thursday 15-October after the New York close (Alcoa via Medianet), opening the producer reporting season. Vedanta's Q2 FY27 production release (03-October) showed record aluminium of 649,000 t and alumina of 895,000 t; financials follow later. "+d['earnings_note'])

for s in [[L_SMMP,S_SMMP],[L_GC,S_GC],[L_VED,S_VED],[L_AA,S_AA],[L_SMMS,S_SMMS],[L_TE,S_TE]]:
    d['sources'].append(s)
d['outlook']['sources'].append([L_SMMP,S_SMMP]); d['outlook']['sources'].append([L_AA,S_AA])
d['ew']['updated']=RD

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-09', ph['rows'][-1]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
