# Daily data refresh - 2026-10-13 (TUESDAY, compiled ~03:30 London).
# Westmetall WebFetch NOT GRANTED (PROVENANCE_REQUIRED on EN, DE and per-metal pages); AL Circle news and straits.live also blocked.
# WebSearch fallback did NOT yield a complete 12-Oct LME official (cash+3M+stocks), so per owner rule (3) the board is KEPT on the
# 09-Oct official (one session behind) and that is stated in caveats/so_what. Reuters (via Business Recorder, 12-Oct) official
# open-outcry 3M marks are cited as REPORTED context only. Macro refreshed from Trading Economics (fetch OK).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-13'; d['report_date']=RD
S_BR="https://www.brecorder.com/news/40443822/aluminium-rebounds-from-8-month-low-copper-hits-two-week-peak"
L_BR="Business Recorder (Reuters) - Aluminium rebounds from 8-month low, copper hits two-week peak (12-Oct-2026)"
S_OP="https://oilprice.com/Latest-Energy-News/World-News/Two-More-Oil-Tankers-Attacked-Near-Strait-of-Hormuz.html"
L_OP="Oilprice.com - Two more oil tankers attacked near Strait of Hormuz (12-Oct-2026)"
S_SMMO="https://news.metal.com/newscontent/104152937-dollar-crude-oil-rise-metals-collectively-weaken-alumina-lme-zinc-lead-declines-ny-gold-falls-below-4200-overnight-market"
L_SMMO="SMM - Dollar, crude oil rise; metals collectively weaken; alumina, LME zinc, lead decline [Overnight market] (13-Oct-2026)"
S_TEA="https://tradingeconomics.com/commodity/aluminum"; L_TEA="Trading Economics - Aluminum (commentary 12-Oct-2026)"
S_TEB="https://tradingeconomics.com/commodity/brent-crude-oil"; L_TEB="Trading Economics - Brent crude (viewed 13-Oct-2026)"
S_TEG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TEG="Trading Economics - EU natural gas TTF (12-Oct-2026 close)"
S_TED="https://tradingeconomics.com/united-states/currency"; L_TED="Trading Economics - US dollar index (viewed 13-Oct-2026)"
S_TEY="https://tradingeconomics.com/united-states/government-bond-yield"; L_TEY="Trading Economics - US 10-year yield (viewed 13-Oct-2026)"

KPI_OLD=("COMPILED MONDAY 12-OCTOBER-2026 AT ABOUT 03:30 LONDON, BEFORE THE MONDAY RING. THE FRIDAY 09-OCTOBER-2026 OFFICIAL REMAINS THE LATEST PUBLISHED SESSION AND IS CARRIED; MONDAY'S OFFICIAL PRINTS AT 13:20 LONDON. THIS RUN COULD NOT RE-FETCH WESTMETALL (ACCESS NOT GRANTED IN TIME) AND RELIES ON THE 10- AND 11-OCTOBER RUNS' VERIFICATION, CORROBORATED BY TRADING ECONOMICS SHOWING 09-OCTOBER AS ITS LATEST ALUMINIUM PRINT.")
KPI_NEW=("COMPILED TUESDAY 13-OCTOBER-2026 AT ABOUT 03:30 LONDON. THE MONDAY 12-OCTOBER OFFICIAL HAS PRINTED BUT COULD NOT BE VERIFIED THIS RUN: access to Westmetall was not granted in time and web search did not surface a complete 12-October official (cash, three-month and stocks for every metal). THE BOARD IS THEREFORE KEPT ON THE FRIDAY 09-OCTOBER-2026 OFFICIAL - ONE SESSION BEHIND - rather than mixing sessions. Reported context only, not placed on the board: Reuters (via Business Recorder, 12-October) put aluminium three-month at $3,058 in official open-outcry trading, up 0.3%, after an intraday eight-month low of $3,023. The 09-October board was verified by the 10- and 11-October runs.")
REP=[
 (KPI_OLD,KPI_NEW),
 ("COMPILED MONDAY 12-OCTOBER-2026 (BEFORE THE MONDAY RING).","COMPILED TUESDAY 13-OCTOBER-2026 (LME BOARD KEPT ON 09-OCTOBER - SEE CAVEATS)."),
 ("COMPILED MONDAY 12-OCTOBER-2026, BEFORE THE MONDAY RING (REVIEWED;","COMPILED TUESDAY 13-OCTOBER-2026 (REVIEWED;"),
 ("REVIEWED 12-OCTOBER: no newer public disclosure","REVIEWED 13-OCTOBER: no newer public disclosure"),
 ("REVIEWED 12-OCTOBER. NO NEW DATED","REVIEWED 13-OCTOBER. NO NEW DATED"),
 ("CARRIED MONDAY 12-OCTOBER-2026 (compiled before Monday's sessions settle; Friday 09-October closes first captured on the Saturday run) to the 09-October LME fixing",
  "CARRIED TUESDAY 13-OCTOBER-2026 (the 12-October LME fixing could not be fetched this run) at the 09-October LME fixing"),
 ("HELD 12-OCTOBER (pre-ring Monday,","HELD 13-OCTOBER (board kept on 09-October because the 12-October official could not be verified; the Reuters-reported eight-month intraday low of $3,023 and Citi's 2027 surplus call add to the bear weight, but no verified new official) AND 12-OCTOBER (pre-ring Monday,"),
 ("REVIEWED 12-OCTOBER (MONDAY, BEFORE THE RING - NO NEW SESSION SINCE FRIDAY; COUNT UNCHANGED). ",
  "REVIEWED 13-OCTOBER (BOARD KEPT ON 09-OCTOBER; COUNT UNCHANGED PENDING VERIFICATION). Reuters reports the 12-October three-month at $3,058 in official open-outcry trading after an intraday low of $3,023, the lowest since 13-February; if the official is confirmed beneath 3,061.5 it is the first settled close below the July low, which fits the base-case wave (v) extending toward 2,980-3,000 and is not a re-label trigger. REVIEWED 12-OCTOBER (MONDAY, BEFORE THE RING - NO NEW SESSION SINCE FRIDAY; COUNT UNCHANGED). "),
 (" Before Monday's assessments no agency has published since Friday, so every row here is carried."," Each row is carried at its own last public assessment date; the CIF Japan spot row uses SMM's 09-October mark."),
 (" Next official Monday 12-October."," THE 12-OCTOBER OFFICIAL HAS PRINTED BUT COULD NOT BE VERIFIED ON 13-OCTOBER (Westmetall access not granted; not found via search), so the window was NOT rolled and stays one session behind."),
 ("Carried through the weekend; next official Monday 12-October 13:20 London.","Carried: the 12-October official could not be verified on the 13-October run."),
 ("FOURTH, WATCH THE CALENDAR: Monday's official decides whether 3,061.5 keeps holding;","FOURTH, WATCH THE CALENDAR: the first verified post-weekend official decides whether 3,061.5 has broken on a settled basis (Reuters reported an intraday $3,023 on 12-October);"),
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
assert all(n>0 for n in cnt.values())

# ---- macro (Trading Economics, fetched this run) ----
M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="105.32",day="-1.24% intraday 13-October after a three-session gain; -0.34% month to date (Trading Economics)",
 note="REFRESHED TUESDAY 13-OCTOBER-2026 on a public reference board (Trading Economics): Brent slipped toward $105 after three sessions of gains as traders weighed Russia's partial easing of diesel export curbs against Middle East and Ukraine tensions; Oilprice.com reported Brent above $103 on 12-October after two more tankers were attacked near Hormuz. Energy is a major smelter cash-cost line. SOURCE: "+S_TEB)
M['European gas TTF (EUR/MWh)'].update(value="84.20",day="+3.40% on Monday 12-October; +1.98% over the month (Trading Economics)",
 note="REFRESHED TUESDAY 13-OCTOBER-2026 to the Monday 12-October close (Trading Economics): TTF rose to its highest since December 2022 as Hormuz tanker attacks raised LNG supply concerns, with EU storage about 73% full and cold autumn forecasts. European power and gas costs bear on marginal European smelter economics. SOURCE: "+S_TEG)
M['US dollar index (DXY)'].update(value="102.45",day="-0.14% intraday 13-October after rising to about 102.5 on Monday; +3.08% over the month (Trading Economics)",
 note="REFRESHED TUESDAY 13-OCTOBER-2026 (Trading Economics): the dollar rose to about 102.5 on Monday, near its highest since April 2025, ahead of US inflation data and on safe-haven demand; Reuters cited the strong dollar as a weight on aluminium on 12-October. SOURCE: "+S_TED)
M['US 10-year Treasury yield (%)'].update(value="5.20",day="down about 4bp intraday 13-October; +21bp over the month (Trading Economics)",
 note="REFRESHED TUESDAY 13-OCTOBER-2026 on a public reference board (Trading Economics). Higher yields raise the cost of carrying metal and financing inventory. SOURCE: "+S_TEY)

# ---- caveats ----
C=d['caveats']
C[0]=("THE LME BOARD ON THIS PAGE IS THE FRIDAY 09-OCTOBER-2026 OFFICIAL AND IS ONE SESSION BEHIND. The Monday 12-October official printed at 13:20 London, but this Tuesday 13-October run could not verify it: Westmetall access was not granted in time and web search did not surface a complete 12-October official. Rather than mix sessions or publish an unverified figure, every board value (aluminium, copper, nickel, zinc, lead, stocks, spread, fifteen-session windows) is kept on 09-October.")
C[1]=("REPORTED, NOT ON THE BOARD: Reuters (via Business Recorder, 12-October) put three-month aluminium at $3,058 in official open-outcry trading (+0.3%) after an intraday low of $3,023, the lowest since 13-February; copper $14,657 (+0.8%), zinc $3,758 (-1.3%), nickel $15,700 (+0.5%), lead $1,884 (-0.2%). SMM's 13-October overnight report says LME aluminium edged down and LME zinc fell 1.38% in the later session. These are cited as context; cash settlements and stocks for 12-October were not available.")
C[2]=("THE 09-OCTOBER BOARD WAS VERIFIED BY THE 10- AND 11-OCTOBER RUNS (cache-busted English and German Westmetall overviews agreed exactly across all six metals, stocks and FX fixings, EUR/USD MTLE 1.12090; per-metal table showed no row after 09-October). It was not re-checked on 12- or 13-October.")

# ---- inputs summary / producers ----
d['inputs_summary']=("UPDATE 13-OCTOBER: copper is kept at the Friday 09-October LME official cash of $14,689.00 and its fifteen-session window is NOT rolled, because the 12-October official could not be verified this run (Reuters reported copper three-month at $14,657 in official trading on 12-October, a two-week high, after a fatal landslide partially suspended Codelco's El Teniente mine). No new input mark was located; every row is carried at its own dated public mark and nothing was interpolated. The mid-October carbon settlement cycle (anodes, pitch, green coke) is due around 17-18 October.")
for p in d['producer_status']: p['asof']=RD

d['so_what']={"line":"Aluminium hit an eight-month intraday low of $3,023 on Monday before recovering to about $3,058 three-month (Reuters), as a strong dollar, easing Gulf supply fears and Citi's call for a 2027 surplus weigh - the July floor is now being tested on an official basis, while Hormuz tanker attacks keep energy and freight costs high.",
 "points":[
 "WHAT MOVED: Reuters reports three-month aluminium at $3,058 in Monday's official open-outcry (+0.3%) after touching $3,023, the lowest since 13-February; prices are down 19% from June's four-year high. This page's board stays on the verified Friday 09-October official (cash $3,055.50, three-month $3,070.00, $14.50 contango, stock 238,875 t) because Monday's full official could not be verified this run.",
 "WHY: the dollar index near 102.5, its highest since April 2025, ahead of US inflation data; easing Gulf supply concerns and expected Indonesian capacity; Citi sees a 1.8 Mt surplus in 2027 versus a 941,000 t deficit this year. Low visible inventories are still cited as support.",
 "ENERGY AND LOGISTICS: two more tankers were attacked near Hormuz on Sunday (one Suezmax set on fire, two sailors missing); Brent traded above $103-105 and European gas hit its highest since December 2022 at about 84 EUR/MWh - raising smelter power-cost risk in Europe.",
 "WHAT TO WATCH: whether a verified official settles beneath 3,061.5 (opens $2,980-3,000); US inflation data this week; Alcoa's Q3 results on Thursday 15-October after the New York close; and the mid-October carbon settlements around 17-18 October."]}

d['feed']=([
 {"when":"Tue 13-Oct","impact":"Mixed","text":"BOARD KEPT ON THE FRIDAY 09-OCTOBER LME OFFICIAL (cash $3,055.50, three-month $3,070.00, stock 238,875 t) because the 12-October official could not be verified this run. Reported: Reuters puts Monday's official open-outcry three-month at $3,058."},
 {"when":"Mon 12-Oct","impact":"Bearish","text":"Aluminium touched $3,023, an eight-month low, on a strong dollar and easing Gulf supply fears, then recovered to $3,058 three-month in official trading (Reuters via Business Recorder). Citi sees a 1.8 Mt 2027 surplus."},
 {"when":"Mon 12-Oct","impact":"Bullish","text":"European gas (TTF) rose 3.4% to about 84.2 EUR/MWh, the highest since December 2022, on Hormuz tanker attacks (Trading Economics) - a cost headwind for European smelters."},
 {"when":"Sun 11-Oct","impact":"Bullish","text":"Two more tankers attacked near Hormuz - a Suezmax carrying Iraqi crude caught fire with two sailors missing, and a product carrier was hit by a drone (Oilprice.com)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"Price","horizon":"0-1 month","impact":"Bearish","url":S_BR,
  "headline":"ALUMINIUM REBOUNDS FROM AN EIGHT-MONTH LOW AS COPPER HITS A TWO-WEEK PEAK (Reuters via Business Recorder, 12-October): LME three-month aluminium touched $3,023, its lowest since 13-February, then traded at $3,058 in official open-outcry, up 0.3%; prices are down 19% from June's four-year high. Pressure came from a dollar near an 18-month high ahead of US inflation data, easing Gulf supply concerns and expectations of more Indonesian capacity, while low visible inventories still offer support. Citi forecasts a 1.8 million t surplus in 2027 against a 941,000 t deficit this year. Copper rose 0.8% to $14,657 after a fatal landslide partially suspended Codelco's El Teniente mine; zinc fell 1.3% as LME stocks rose to 132,850 t."},
 {"theme":"Logistics","horizon":"0-3 months","impact":"Bullish","url":S_OP,
  "headline":"TWO MORE TANKERS ATTACKED NEAR HORMUZ (Oilprice.com, 12-October): a Suezmax loaded with Iraqi crude was hit by a projectile and caught fire, with two sailors missing, and a product carrier was struck by a drone; one attack was in Hormuz and the other off Oman, where ships have been moving in dark mode along a southern corridor. Brent rose above $103. For aluminium, this keeps Gulf export freight, war-risk insurance and energy costs elevated."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish","url":S_TEG,
  "headline":"EUROPEAN GAS AT ITS HIGHEST SINCE DECEMBER 2022 (Trading Economics, 12-October): TTF rose 3.4% to about 84.2 EUR/MWh on LNG supply worries after Hormuz tanker attacks, with EU storage around 73% full and cold autumn forecasts. Higher gas lifts European power prices and the cost base of marginal European smelters, a supply-side support for premiums there."},
 {"theme":"Macro","horizon":"0-1 month","impact":"Bearish","url":S_SMMO,
  "headline":"METALS BROADLY WEAKER OVERNIGHT AS THE DOLLAR AND CRUDE RISE (SMM, 13-October): LME aluminium edged down, LME zinc fell 1.38% and lead 0.29%, while copper rose 0.56%; SHFE aluminium fell 0.4% and the most-traded alumina futures fell 1.15%; the dollar index rose 0.34% to 102.58."},
]+d['news'][:16]

d['outlook']['ai_analysis'].insert(0,"TUESDAY REVIEW, 13-OCTOBER: the July floor at 3,061.5 is being tested. Reuters reports Monday's official three-month at $3,058 after an eight-month intraday low of $3,023, which would be the first settled close beneath the July low; this page keeps its board on the verified Friday official until Monday's full official can be confirmed. The drivers are macro and supply: a dollar near its highest since April 2025, easing Gulf supply concerns, and Citi's call for a 1.8 Mt 2027 surplus. Against that, European gas at a near three-year high and fresh Hormuz tanker attacks raise smelter energy and freight costs. Bias stays bearish into US inflation data and Alcoa's 15-October results.")
R1=d['outlook']['risks'][1]
R1['risk']+=" UPDATE 13-OCTOBER: the dollar index rose to about 102.5 on 12-October, near its highest since April 2025, ahead of US inflation data, and Reuters cited it as a key weight on aluminium's slide to an eight-month intraday low; the US ten-year is near 5.20% (Trading Economics). Trend held at UP."

for s in [[L_BR,S_BR],[L_OP,S_OP],[L_SMMO,S_SMMO],[L_TEA,S_TEA],[L_TEB,S_TEB],[L_TEG,S_TEG],[L_TED,S_TED],[L_TEY,S_TEY]]:
    d['sources'].append(s)
d['outlook']['sources'].append([L_BR,S_BR])
d['ew']['updated']=RD

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-09', ph['rows'][-1]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
