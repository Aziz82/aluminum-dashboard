# Daily data refresh - 2026-10-11 (SUNDAY, no LME ring). Board CARRIED at FRIDAY 09-Oct LME official, re-verified 11-Oct.
# Material catch-up: Reuters (07-Oct) reported a Q4-2026 MJP agreement at $255/t - missed by the 08-10 Oct runs, recorded now.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-11'; d['report_date']=RD
S_RTR="https://www.lse.co.uk/news/some-japanese-aluminium-buyers-agree-to-pay-q4-premiums-of-255t-35-lower-than-q3-sources-say-v64wx6vu8vtjw95.html"
L_RTR="Reuters via LSE.co.uk - Some Japanese aluminium buyers agree to pay Q4 premiums of $255/t, 35% lower than Q3 (07-Oct-2026)"
S_KED="https://in.investing.com/news/commodities-news/aluminium-falls-as-middle-east-output-recovers-and-indonesian-shipments-increase-5625216"
L_KED="Investing.com (Kedia Advisory) - Aluminium falls as Middle East output recovers and Indonesian shipments increase (09-Oct-2026)"
S_STR="https://straits.live/briefs/2026-10-09"
L_STR="straits.live - Strait of Hormuz daily brief (09-Oct-2026)"
S_SEA="https://www.seatrade-maritime.com/security/tanker-catches-fire-after-first-hormuz-attack-in-october"
L_SEA="Seatrade Maritime - Tanker catches fire after first Hormuz attack in October (02-Oct-2026)"

REP=[
 ("COMPILED SATURDAY 10-OCTOBER-2026","COMPILED SUNDAY 11-OCTOBER-2026"),
 ("REFRESHED SATURDAY 10-OCTOBER-2026","CARRIED SUNDAY 11-OCTOBER-2026 (markets shut since Friday; Friday 09-October values first captured on the Saturday run)"),
 ("REVIEWED 10-OCTOBER","REVIEWED 11-OCTOBER"),
 ("No Q4 settlement had been publicly reported when this page compiled.",
  "Q4 SETTLEMENT NOW PUBLIC: Reuters (07-October) reported that some Japanese buyers agreed Q4 premiums of $255/t with global producers including Rio Tinto and South32, down 35% from $395/t in Q3 and below initial offers of $310-325/t; talks with other buyers were ongoing. This page first recorded it on 11-October."),
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
for a,n in cnt.items(): print(n,'x',a[:60])

# ---- MJP Q4 settlement ----
m=d['premiums'][0]; assert m['name'].startswith('MJP Q3')
m['name']='MJP Q4 (Main Japanese Port)'; m['cur']=255; m['prev']=395
for q in d['premium_quarters']:
    if q['q']=='Q4-26': q.clear(); q.update({'q':'Q4-26','v':255})
d['premium_settlement_src']=[L_RTR,S_RTR]
d['premium_drivers'][0]={'t':"The Q4 Japanese premium has settled 35% lower, at $255/t",
 'd':"SETTLED: Reuters (07-October) reported that some Japanese buyers agreed to pay $255/t over LME cash for October-December shipments, down 35% from $395/t in Q3 and below producers' initial offers of $310-325/t; producers named in the talks included Rio Tinto and South32, and talks with other buyers were ongoing. A Japanese trading-house source cited recovering Middle East output after the March attacks on Gulf smelters and rising Indonesian shipments. Negotiations ran longer than usual because of a wide gap between the two sides. The settlement sits inside the $245-260/t offer range AL Circle reported on 06-October, and above CRU's $202/t Asia CIF assessment. WHY IT MATTERS: the quarterly MJP is the reference for much Asian physical business, so the regional premium level resets about $140/t lower for the quarter.",
 'src':[L_RTR,S_RTR]}
d['premium_outlook']=("UPDATE 11-OCTOBER: THE Q4-2026 JAPANESE QUARTERLY PREMIUM HAS SETTLED AT $255/T, DOWN 35% FROM THE $395/T Q3 RECORD (Reuters, 07-October; some buyers, with talks continuing for others). The chart's pending band is replaced by the settled value. The settlement landed at the low end of the offer range and above CRU's $202/t Asia CIF spot assessment, so spot still sits beneath the benchmark: the next test is whether Q1-2027 talks open lower again. Drivers cited publicly are recovering Gulf output and rising Indonesian shipments. "+d['premium_outlook'])
cats=d['outlook']['catalysts']
cats[1]={'date':'Settled (reported 07-Oct)','impact':'High','event':"Q4-2026 JAPANESE QUARTERLY PREMIUM (MJP) SETTLED AT $255/T for some buyers, down 35% from $395/t in Q3 and below initial offers of $310-325/t (Reuters, 07-October); talks with other buyers ongoing. Next: Q1-2027 negotiations, typically from late November."}
cats[4]['date']='Settled 07-Oct'; cats[4]['event']="Q4-2026 JAPANESE QUARTERLY PREMIUM SETTLED AT $255/T (Reuters, 07-October) - below the $280/t offer SMM cited on 30-September, as the market had expected."
cats[13]['date']='Settled 07-Oct'; cats[13]['event']="THE Q4-2026 JAPANESE QUARTERLY PREMIUM SETTLED AT $255/T (Reuters, 07-October), a 35% fall from the $395/t Q3 record and beneath the earlier $280-310/t negotiating range. The buyer's case - recovering ex-China capacity and Chinese spot discounts - prevailed over the narrower exchange contango."
r=d['outlook']['risks'][8]
r['risk']=("RESOLVED 11-OCTOBER - THE Q4-2026 JAPANESE PREMIUM SETTLED AT $255/T, DOWN 35% (Reuters, 07-October; some buyers, others still negotiating). The arrow stays DOWN: the reset to a lower regional premium is now a print, not a risk, and the residual question is only whether remaining buyers settle at the same level. PRIOR RECORD: "+r['risk'])
d['caveats'][6]=d['caveats'][6].replace("No Q4-2026 Japanese quarterly settlement had been publicly reported when this page compiled on 10-October; the chart's pending band is the span of reported OFFERS ($245-280/t). Offers are not settlements.",
 "THE Q4-2026 JAPANESE QUARTERLY PREMIUM IS NOW CARRIED AS SETTLED AT $255/T: Reuters reported the agreement on 07-October (some buyers; talks with others ongoing). Earlier runs on 08-10 October still described Q4 as pending - that was a miss, corrected on 11-October.")
d['commercial']=d['commercial'].replace("public reporting has Q4 MJP offers at $245-260/t (AL Circle, 06-October) and CRU's Asia CIF at $202/t, against $395/t in Q3; no settlement is yet reported.",
 "the Q4 MJP settled at $255/t for some Japanese buyers (Reuters, 07-October), down 35% from $395/t in Q3, and CRU's Asia CIF spot is lower still at $202/t.").replace("a Q4 Japanese premium settlement could come any day; ","whether remaining Japanese buyers settle at $255/t; ")
d['net_read']=d['net_read'].replace("Asian premium offers sit at $245-260/t versus $395/t in Q3","the Q4 Japanese premium settled at $255/t, down 35% from $395/t in Q3") if isinstance(d['net_read'],str) else d['net_read']

# ---- weekend status ----
d['inputs_summary']=("UPDATE 11-OCTOBER (WEEKEND, NO RING): copper is carried at the Friday 09-October LME official cash of $14,689.00, its fifteen-session window unchanged (it rolled on 10-October). No other input mark printed over the weekend; every other row is carried at its own dated public mark and no value was interpolated. The mid-October carbon settlement cycle (anodes, pitch, green coke) is due around 17-18 October.")
for p in d['producer_status']:
    p['asof']=RD

d['so_what']={"line":"Aluminium starts the new week sitting on its early-July floor near $3,060 after a 1.7% weekly fall, and the Q4 Japanese premium has settled 35% lower at $255/t - the physical market has confirmed the price weakness rather than resisted it.",
 "points":[
 "WHAT MOVED: nothing since Friday - markets are shut for the weekend. The last LME official (09-October) settled cash at $3,055.50 and three-month at $3,070.00, a $14.50 contango, with LME stock 238,875 t; three-month fell 1.67% on the week while copper, zinc, nickel and lead rose.",
 "PREMIUMS RESET: some Japanese buyers agreed Q4 premiums of $255/t, down 35% from $395/t in Q3 and below initial offers of $310-325/t (Reuters, 07-October), citing recovering Middle East output and rising Indonesian shipments. Spot Asia CIF is lower still at $202/t (CRU via AL Circle).",
 "WHY: a strong dollar at its highest since April 2025, analysts' 2026 deficit view cut to 820,000 t with a 2027 surplus in view, and EGA restarting part of Al Taweelah (Macquarie and EGA via Investing.com) outweigh still-low LME stock. Hormuz remains disrupted, with near-daily attacks and only 4 transits recorded on 04-October against a pre-crisis 85 a day (straits.live).",
 "WHAT TO WATCH: Monday's LME official against $3,061.5 - a settled break opens $2,980-3,000; whether remaining Japanese buyers settle at $255/t; China's post-holiday inventory prints; the mid-October carbon settlements; and the Q3 producer earnings season from mid-month."]}

d['feed']=([
 {"when":"Sun 11-Oct","impact":"Mixed","text":"WEEKEND - BOARD CARRIED AT THE FRIDAY 09-OCTOBER LME OFFICIAL (cash $3,055.50, three-month $3,070.00, contango $14.50, stock 238,875 t), re-verified on 11-October on cache-busted English and German Westmetall overviews in exact agreement and the aluminium per-metal table with no later row. Next official Monday 12-October 13:20 London."},
 {"when":"Wed 07-Oct","impact":"Bearish","text":"Q4 JAPANESE PREMIUM SETTLES AT $255/T, DOWN 35% (Reuters): some buyers agreed with producers including Rio Tinto and South32, below initial offers of $310-325/t; talks with other buyers ongoing. (First recorded on this page 11-October.)"},
]+d['feed'])[:12]

d['news']=[
 {"theme":"Premiums","horizon":"0-3 months","impact":"Bearish","url":S_RTR,
  "headline":"Q4 JAPANESE ALUMINIUM PREMIUM SETTLES 35% LOWER AT $255/T (Reuters, 07-October): some Japanese buyers agreed to pay $255/t over LME cash for October-December shipments, down from $395/t in Q3 - the first quarterly drop in four quarters - and below producers' initial offers of $310-325/t. A trading-house source cited recovering Middle East output after the March attacks and rising Indonesian shipments; talks ran longer than usual and continue with other buyers."},
 {"theme":"Supply","horizon":"1-3 months","impact":"Bearish","url":S_KED,
  "headline":"SUPPLY RECOVERY AND RISING INDONESIAN SHIPMENTS WEIGH (Investing.com / Kedia Advisory, 09-October): Macquarie cut its 2026 deficit forecast by 120,000 t to 820,000 t and sees a 410,000 t surplus in 2027; EGA has restarted a quarter of Al Taweelah. The International Aluminium Institute put August global output down 1.5% year on year, with China at a record 3.87 Mt (+3%) and GCC output down 43% to 299,000 t; Alcoa cut 2026 alumina guidance to 9.5-9.6 Mt."},
 {"theme":"Logistics","horizon":"0-3 months","impact":"Mixed","url":S_STR,
  "headline":"HORMUZ ATTACKS CONTINUE (straits.live, 09-October brief): near-daily attacks on commercial shipping, with nine ships struck in the strait or off Oman since 01-October (USNI News, as cited); IMF PortWatch recorded 4 transits on 04-October against a pre-crisis 85 a day, and 129 AIS-visible vessels were holding position in the Gulf watch box. Brent was $104.43 at Friday's close. Disruption keeps Gulf export logistics and freight costs elevated even as smelter output recovers."},
]+d['news'][:17]

d['outlook']['ai_analysis'].insert(0,"WEEKEND REVIEW, 11-OCTOBER: no new session since Friday's weekly close at $3,070.00 three-month. The material catch-up is physical: the Q4 Japanese premium settled at $255/t, down 35% from Q3 (Reuters, 07-October), confirming that the regional market is pricing supply recovery rather than disruption. Combined with the 820,000 t trimmed deficit view and continuing Hormuz disruption that hits logistics more than output, the weekend leaves the bearish bias intact into Monday's test of the July low.")

for s in d['outlook']['scenarios']:
    s['drivers']=s['drivers'].replace("MOVED 10-OCTOBER (from 12/45/43","HELD 11-OCTOBER (weekend, no new session; the Q4 MJP settlement at $255/t is consistent with the existing bear weight); LAST MOVED 10-OCTOBER (from 12/45/43",1)

ew=d['ew']; ew['updated']=RD
for k in ('short_term','long_term'):
    ew[k]['writeup']="REVIEWED 11-OCTOBER (WEEKEND, NO NEW SESSION; COUNT UNCHANGED). "+ew[k]['writeup']

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 09-OCTOBER-2026 LME OFFICIAL, CARRIED BECAUSE THE MARKET IS SHUT. This page compiled on SUNDAY 11-October; there is no LME ring on Saturday or Sunday, so Friday's official - also the weekly close - is the correct current figure until Monday 12-October 13:20 London. Every board value is therefore identical to the Saturday run by design, not stale.")
C[1]=("THE COMPLETENESS TEST PASSES, RE-RUN ON 11-OCTOBER: the aluminium per-metal daily table shows 09-October as the newest row with NO ROW AFTER IT and 08-October unchanged as the prior row; the other metals reconcile through the cache-busted overviews.")
C[2]=("THE ENGLISH AND GERMAN OVERVIEWS WERE BOTH RE-REQUESTED CACHE-BUSTED ON 11-OCTOBER AND AGREE EXACTLY on 09-October across all six metals, stocks and FX fixings (EUR/USD MTLE 1.12090).")

for s in [[L_RTR,S_RTR],[L_KED,S_KED],[L_STR,S_STR],[L_SEA,S_SEA]]:
    d['sources'].append(s)
d['outlook']['sources'].append([L_RTR,S_RTR])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-09', ph['rows'][-1]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
