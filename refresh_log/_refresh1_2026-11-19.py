# Daily data refresh - 2026-11-19 (THURSDAY, ~02:45 UTC, before today's ring). BOARD CARRIED on the TUESDAY 17-Nov LME official:
# cache-busted Westmetall EN + DE overviews AND the Al and Cu per-metal tables all still show 17-Nov as the newest session; the
# Wednesday 18-Nov official had not been published there, and no search located the 18-Nov official settlement (fallback rule 3).
# Reuters (via Business Recorder 18-Nov) reports intraday 3M ~$2,869 (-2.2%) by 1100 GMT; Trading Economics CFD 2,834.9 (-3.50%) - TEXT ONLY.
import json,re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-19'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-19"; L_ST="Straits Daily Brief - Strait of Hormuz, 19-Nov-2026 (Brent figure AI-assisted)"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,834.9 (-3.50%) on 18-Nov-2026, a 51-week low of 2,819; forecast 2027 surplus 830 kt (CFD reference)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$92.1 (+0.17%), near lowest since late August; US crude stocks +3.38 mb (19-Nov-2026)"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.87; hawkish October FOMC minutes; ~90% odds of a 25bp December hike, ~10% for 50bp (19-Nov-2026)"
S_TG="https://tradingeconomics.com/commodity/eu-natural-gas"; L_TG="Trading Economics - European gas ~EUR 82.0-82.3/MWh; EU storage toward 70% vs 89% five-year average (19-Nov-2026)"
S_BRC="https://www.brecorder.com/news/40449557/copper-tumbles-to-seven-month-low-on-speculative-selling-and-inflation-fears"; L_BRC="Business Recorder (Reuters) - Copper tumbles to seven-month low; LME aluminium -2.2% to $2,869 by 1100 GMT (18-Nov-2026)"
S_CA="https://www.alcircle.com/news/canada-extends-us-tariff-relief-by-one-year-to-june-2028-but-ends-exemptions-for-certain-aluminum-products-122013"; L_CA="AL Circle - Canada extends US counter-tariff relief to June 2028 but ends exemptions for certain aluminum products (18-Nov-2026)"
S_SP="https://www.spglobal.com/energy/en/news-research/latest-news/metals/101326-japanese-q4-aluminum-premium-falls-35-to-255mt-cif-japan"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o
OV=("COMPILED WEDNESDAY 18-NOVEMBER-2026 ABOUT 02:40 LONDON, BEFORE TODAY'S RING. THE BOARD IS THE TUESDAY 17-NOVEMBER-2026 LME OFFICIAL - THE LATEST PUBLISHED SESSION AND THE CORRECT FIGURE UNTIL TODAY'S OFFICIAL PRINTS AT 13:20 LONDON. "
 "COMPLETENESS CHECKS: (1) the cache-busted Westmetall ENGLISH AND GERMAN overviews were BOTH fetched and AGREE on the full 17-November official for all metals with stocks and FX (EUR/USD MTLE 1.09930; 16-November 1.10140); (2) the aluminium per-metal daily table shows 17-November as its newest row and its 10-16 November rows match the stored series exactly. ")
NV=("COMPILED THURSDAY 19-NOVEMBER-2026 ABOUT 02:45 LONDON, BEFORE TODAY'S RING. THE BOARD IS CARRIED ON THE TUESDAY 17-NOVEMBER-2026 LME OFFICIAL: THE WEDNESDAY 18-NOVEMBER OFFICIAL HAD NOT BEEN PUBLISHED ON THE PUBLIC SOURCE AT RUN TIME - the cache-busted Westmetall ENGLISH AND GERMAN overviews and the aluminium and copper per-metal daily tables ALL still show 17-November as the newest session, and no search located the 18-November official settlement - so the board is one session behind and is NOT a fresh print. "
 "Reuters (via Business Recorder, 18-November) reports LME three-month aluminium DOWN 2.2% TO ABOUT $2,869 BY 11:00 GMT on Wednesday and the Trading Economics reference about $2,834.9 (-3.50%) - both INTRADAY/CFD marks cited in text only, not officials. ")
OC=("COMPILED WEDNESDAY 18-NOVEMBER-2026 BEFORE THE RING (LME BOARD ON THE TUESDAY 17-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION; WEDNESDAY'S OFFICIAL PRINTS 13:20 LONDON).")
NC=("COMPILED THURSDAY 19-NOVEMBER-2026 BEFORE THE RING (LME BOARD CARRIED ON THE TUESDAY 17-NOVEMBER OFFICIAL - THE WEDNESDAY 18-NOVEMBER OFFICIAL HAD NOT BEEN PUBLISHED ON WESTMETALL AT RUN TIME).")
cnt={'v':0,'c':0}
def f(s):
    if OV in s: cnt['v']+=1; s=s.replace(OV,NV)
    if OC in s: cnt['c']+=1; s=s.replace(OC,NC)
    s=s.replace("REVIEWED 18-NOVEMBER: no newer public disclosure","REVIEWED 19-NOVEMBER: no newer public disclosure").replace("REVIEWED 18-NOVEMBER. NO NEW DATED","REVIEWED 19-NOVEMBER. NO NEW DATED")
    return s
for k in ('kpi_cards','benchmark','metals_detail','premiums','alumina','producer_status','inputs','logistics','raw_materials'):
    d[k]=walk(d[k],f)
assert cnt['v']==13 and cnt['c']==10, cnt

for fp in d['outlook']['forward_path']:
    fp['basis']=fp['basis'].replace("Next official Wednesday 18-November 13:20 London.","CARRIED: the Wednesday 18-November official was not yet published on Westmetall at run time; next print Thursday 19-November 13:20 London.")
assert "Next official Wednesday" not in json.dumps(d['outlook']['forward_path'])
bl=d['bottom_line']; o="Next official Wednesday 18-November 13:20 London."; assert o in bl
d['bottom_line']=bl.replace(o,"THIS RUN CARRIES THE 17-NOVEMBER BOARD: the 18-November official was not yet published on the public source; Reuters reports three-month traded down a further 2.2% to about $2,869 by 11:00 GMT Wednesday - below the 2,894-2,906 target zone intraday - so the 18-November settlement is the key check against that zone. Next print Thursday 19-November 13:20 London.")

d['lme_commentary']=("CARRIED BOARD, SELLING EXTENDED INTRADAY. This Thursday run carries the 17-November official because the Wednesday 18-November official was not yet on the public source. Reuters (via Business Recorder, 18-November) reports three-month aluminium fell 2.2% to about $2,869 by 11:00 GMT Wednesday and copper 3.5% to $12,770, a seven-month low, with tin down 7.1%; Saxo Bank's Ole Hansen called it 'the inflation scare, the risk of higher funding costs'. Trading Economics shows aluminium at a 51-week low and cites forecasts of a swing from a 1.1 Mt 2026 deficit to an 830 kt 2027 surplus. ")+d['lme_commentary']
d['net_read']=("NET: BEARISH ON THE FORWARD (UPDATED 19-NOVEMBER). Wednesday's reported intraday trade near $2,869 extends the break below the 2,994.50 October low into the 2,894-2,906 Elliott zone, pending confirmation by the 18-November official; the October FOMC minutes showed nearly all policymakers backing further hikes. ")+d['net_read']

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS CARRIED ON THE COMPLETE TUESDAY 17-NOVEMBER-2026 LME OFFICIAL. THIS THURSDAY 19-NOVEMBER RUN IS COMPILED AT ABOUT 02:45 LONDON, BEFORE TODAY'S RING. WEDNESDAY 18-NOVEMBER WAS A TRADING DAY, BUT ITS OFFICIAL HAD NOT BEEN PUBLISHED ON THE PUBLIC SOURCE (Westmetall) AT RUN TIME AND NO SEARCH LOCATED IT, so the board is ONE SESSION BEHIND and was NOT rolled - nothing was estimated. Wednesday's intraday Reuters mark (three-month about $2,869, -2.2%, by 11:00 GMT) and the Trading Economics CFD reference (about $2,834.9, -3.50%) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (19-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on the 17-November session (aluminium cash 3,060.50, three-month 2,940.00, stock 220,350; EUR/USD MTLE 1.09930) as the newest session; the aluminium and copper per-metal daily tables also show 17-November as their newest row. A search for the 18-November official settlement found only intraday reports. Because all four pages agree, this is treated as a publication lag at the source, not a single stale cached page.")
C[2]=("COMPENSATING CHECKS: the aluminium per-metal table's 23-October to 17-November rows match the stored series; lme_series, metals_series, the Copper input series and the price-history row are UNCHANGED this run because no new official session was available.")
hit=0
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $92.1), the dollar index (about 103.87) and TTF (about EUR 82.0-82.3/MWh) are Trading Economics readings for 19-November (early, pre-European session); Trading Economics prices are contract-for-difference references, not official benchmarks, and its TTF page again showed two levels in different sections, so levels are approximate. The US ten-year row is CARRIED (not re-fetched). The Straits Daily Brief (19-November) shows Brent $92.22 (AI-assisted); its incident items are flagged as media reports unless attributed to UKMTO."); hit+=1
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 19-NOVEMBER (THURSDAY, PRE-RING): no authorised fetch was blocked. Westmetall EN and DE overviews and the aluminium and copper per-metal tables, Trading Economics aluminium/Brent/TTF/dollar, AL Circle news and the Straits Daily Brief were fetched; all Westmetall pages ended on 17-November, so fallback rule 3 applied (board carried, everything else refreshed). The Reuters Wednesday metals report (via Business Recorder) was found by search and fetched. Searches for Q1-2027 Japanese premium offers and for an official US-Canada aluminium tariff deal again found neither, so both stay pending."); hit+=1
assert hit==2,hit

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="92.1",day="about $92.11 on 19-November (+0.17%, Trading Economics), near its lowest since late August; Straits Daily Brief $92.22",
 note="REFRESHED THURSDAY 19-NOVEMBER-2026 (Trading Economics): Brent is down about 20% this month on recovering Middle Eastern supply, an IEA-projected surplus of about 2 mb/d this quarter and Goldman Sachs glut warnings; US crude stocks rose 3.38 mb to 417.8 mb in the week to 13-November. Attacks in the Gulf continue to threaten tanker traffic. Levels approximate. SOURCE: "+S_BR)
M['European gas TTF (EUR/MWh)'].update(value="82.0",day="about EUR 82.0-82.3/MWh on 19-November (+1.5-1.8%, Trading Economics; sections differ)",
 note="REFRESHED THURSDAY 19-NOVEMBER-2026 (Trading Economics): prices back below EUR 85/MWh; EU storage fell toward 70% against a five-year seasonal average of 89%, Germany below 58%; Hormuz tensions and curtailed Qatari supply weigh on LNG. SOURCE: "+S_TG)
M['US dollar index (DXY)'].update(value="103.87",day="about 103.87 on 19-November (+0.06%, Trading Economics)",
 note="REFRESHED THURSDAY 19-NOVEMBER-2026 (Trading Economics): October FOMC minutes showed nearly all policymakers backing further rate increases; Governor Waller raised the possibility of a 50bp December hike; CME FedWatch about 90% odds of 25bp and 10% of 50bp in December. SOURCE: "+S_TD)

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 19-NOVEMBER: Straits Daily Brief - still effectively closed; latest transit count 2 on 15-November (vs 85/day pre-crisis); 45 AIS-visible vessels holding (from 37). The LPG tanker TARA GAS, struck 17-November, is reported still burning and adrift off Oman with a crew member missing (gCaptain/Reuters); UKMTO reported a tanker struck by an unknown projectile; an attack on an ADNOC L&S vessel is a media report only. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 19-NOVEMBER: October FOMC minutes showed nearly all policymakers backing further hikes; Waller flagged a possible 50bp December move; CME FedWatch about 90% 25bp / 10% 50bp; dollar index about 103.87 (Trading Economics). Saxo Bank's Ole Hansen attributes Wednesday's metals sell-off to 'the inflation scare, the risk of higher funding costs' (Reuters via Business Recorder). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 19-NOVEMBER: Brent about $92.1, down about 20% this month; TTF about EUR 82/MWh (Trading Economics). With three-month trading near $2,869 intraday on 18-November, the price is approaching the energy-cost floor while that floor itself softens. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('TARIFF POLICY'):
        r['risk']+=" UPDATE 19-NOVEMBER: Canada extended horizontal remission of its counter-tariffs on US goods to 30-June-2028 but ends relief for certain domestically produced aluminium wire, extrusions and paperboard products from 01-February-2027 (AL Circle, 18-November); no official US-Canada deal on the 50% Section 232 rate located. Trend unchanged."; hit+=1
assert hit==4,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Wed 18-Nov':
        hc+=1; cat['date']='Daily, from Thu 19-Nov'
        cat['event']=("BOARD CARRIED ON THE 17-NOVEMBER OFFICIAL (three-month $2,940.00, cash $3,060.50, backwardation $120.50): the 18-November official was not yet published on the public source at run time. Reuters reports three-month traded near $2,869 intraday on 18-November, inside/below the 2,894-2,906 zone. NEXT: the 18-November and 19-November officials (13:20 London) against the 2,894-2,906 zone (weekly 61.8% and re-counted wave (v) target); a settled close back above 2,994.50 would signal a failed break; above 3,097.50 negates the re-count; invalidation 3,289. Friday's weekly close; the December Fed meeting (25bp about 90%, 50bp about 10% priced); any official US-Canada tariff announcement; first Q1-2027 Japanese premium offers.")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"THURSDAY 19-NOVEMBER (BOARD CARRIED ON THE 17-NOVEMBER OFFICIAL): the Wednesday 18-November official was not yet on the public source, so no new settlement is used. The reported trade points lower: Reuters has three-month aluminium down a further 2.2% to about $2,869 by 11:00 GMT Wednesday amid a broad metals sell-off (copper -3.5% to a seven-month low, tin -7.1%) driven by inflation and funding-cost fears, after the October FOMC minutes showed near-unanimous support for further hikes. Trading Economics cites forecasts of a 2027 surplus of 830 kt as Chinese output nears 46 Mt and Gulf supply recovers. Scenario weights stay at 10/40/50 until the officials confirm whether the 2,894-2,906 Elliott zone holds.")

for s in d['outlook']['scenarios']:
    s['drivers']="REVIEWED 19-NOVEMBER: weights held at 10/40/50 - no new official this run (18-November not yet published); a settled three-month close below 2,894 would add bear weight, back above 2,994.50 return it. "+s['drivers']

EWP=("REVIEWED 19-NOVEMBER - COUNT UNCHANGED, NO NEW OFFICIAL: the 18-November official was not yet published on the public source, so no pivot is added. Reuters reports three-month near $2,869 intraday on 18-November, which would put wave (v) inside or slightly beyond the 2,894-2,906 target zone; an official settlement there would satisfy the base-case target, while a settled close below about 2,850 would favour the extended-(v) alternate toward 2,830-2,850. Invalidation unchanged: above 3,097.50 (re-count), 3,289 (C-wave count). ")
EWL=("REVIEWED 19-NOVEMBER - NO NEW OFFICIAL: weekly count unchanged; intraday trade near $2,869 on 18-November (Reuters) tests the 2,894 61.8% retracement, but only a weekly close below 2,894 would open the 78.6% near 2,633. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 18-NOVEMBER'),k
    d['ew'][k]['writeup']=pfx+w
d['ew']['updated']=RD

d['so_what']={"line":"LME aluminium selling extended on Wednesday: Reuters reports three-month fell a further 2.2% to about $2,869 intraday as a broad metals sell-off deepened on Fed-hike and inflation fears; the board carries the 17-November official ($2,940 three-month, $120.50 backwardation) because the 18-November official was not yet published.",
 "points":[
 "WHAT MOVED: the last published official (17-November) has three-month at $2,940.00 and cash at $3,060.50; on Wednesday Reuters reports three-month near $2,869 by 11:00 GMT, with copper -3.5% to a seven-month low and tin -7.1%. These are intraday marks, not officials.",
 "WHY: the October FOMC minutes showed nearly all Fed policymakers backing more hikes (about 90% odds of 25bp in December, 10% of 50bp) and the dollar sits near 103.9; forecasts cited by Trading Economics see a 1.1 Mt deficit in 2026 turning into an 830 kt surplus in 2027.",
 "SUPPORT: Hormuz stays effectively closed with 45 vessels holding and another LPG tanker still burning off Oman, and visible LME stock was at a record-low 220,350 t on 17-November.",
 "WHAT TO WATCH: whether the 18- and 19-November officials settle three-month inside the $2,894-2,906 zone or below it; Canada ends counter-tariff relief on some aluminium products from 01-February-2027; Friday's weekly close."]}

d['feed']=([
 {"when":"Wed 18-Nov","impact":"Bearish","text":"REUTERS: LME three-month aluminium -2.2% to about $2,869 by 11:00 GMT; copper -3.5% to $12,770 (seven-month low), tin -7.1% (intraday; via Business Recorder)."},
 {"when":"Wed 18-Nov","impact":"Bearish","text":"FED: October FOMC minutes show nearly all policymakers backing further hikes; December 25bp about 90% priced (Trading Economics)."},
 {"when":"Wed 18-Nov","impact":"Mixed","text":"CANADA: counter-tariff relief on US goods extended to June 2028, but ends for some aluminium wire, extrusions and paperboard products from 01-Feb-2027 (AL Circle)."},
 {"when":"Thu 19-Nov","impact":"Bullish","text":"HORMUZ: effectively closed; 45 vessels holding; LPG tanker TARA GAS still burning off Oman (Straits brief)."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Bearish","url":S_BRC,
  "headline":"REUTERS: METALS SELL-OFF DEEPENS (via Business Recorder, 18-November): LME three-month aluminium fell 2.2% to about $2,869 by 11:00 GMT after touching its lowest in almost a year the prior session; copper fell 3.5% to $12,770, its fifth straight loss and lowest since 13-April; zinc -1.4% to $3,623, nickel -2.5% to $16,055, tin -7.1% to $41,840. Saxo Bank's Ole Hansen: 'It's the inflation scare, the risk of higher funding costs that's weighing on risk sentiment.' Intraday marks, not officials."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Bearish","url":S_TD,
  "headline":"HAWKISH FOMC MINUTES (Trading Economics, 19-November): minutes of the October meeting showed nearly all policymakers supporting further rate increases; Governor Waller raised the possibility of a 50bp December hike; CME FedWatch about 90% odds of 25bp and 10% of 50bp; dollar index about 103.87."},
 {"theme":"Supply","horizon":"Structural","impact":"Bearish","url":S_TE,
  "headline":"AT A 51-WEEK LOW, FORECASTS POINT TO A 2027 SURPLUS (Trading Economics, 18-November): the aluminium reference fell about 3.5% to $2,834.9 (low $2,819); China's output is on track for a record above 46 Mt, Chinese producers plan at least 15 Mt/yr of overseas smelters, and Middle East output is recovering - expected to swing the market from a 1.1 Mt deficit in 2026 to an 830 kt surplus in 2027. CFD reference."},
 {"theme":"Trade policy","horizon":"0-6 months","impact":"Mixed","url":S_CA,
  "headline":"CANADA EXTENDS US COUNTER-TARIFF RELIEF TO JUNE 2028 (AL Circle, 18-November): horizontal remission of 15-50% counter-tariffs extended by one year to 30-June-2028, but relief ends for certain domestically produced aluminium wire, extrusions and paperboard products on 01-February-2027 and for certain trailers on 01-December-2026."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL EFFECTIVELY CLOSED (Straits Daily Brief, 19-November): latest IMF PortWatch count 2 transits on 15-November vs 85/day pre-crisis; 45 AIS-visible vessels holding. LPG tanker TARA GAS, struck 17-November, still burning and adrift off Oman with a crew member missing (gCaptain/Reuters); UKMTO reported a tanker struck by an unknown projectile; an ADNOC L&S vessel attack is a media report only."},
 {"theme":"Energy","horizon":"0-1 month","impact":"Bearish","url":S_BR,
  "headline":"BRENT NEAR LOWEST SINCE LATE AUGUST (Trading Economics, 19-November): about $92.1, down about 20% this month on recovering Middle Eastern supply and an IEA-projected 2 mb/d surplus this quarter; US crude stocks +3.38 mb to 417.8 mb. European gas about EUR 82/MWh with storage toward 70%."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])

hit=0
for p in d['producer_status']:
    p['asof']=RD
    if p['name'].startswith('US / Canada'):
        o="REVIEWED 18-NOVEMBER: still no official confirmation"; assert o in p['update']
        p['update']=("UPDATED 19-NOVEMBER: Canada extended its horizontal remission of counter-tariffs on US goods to 30-June-2028 but ends relief for certain domestically produced aluminium wire, extrusions and paperboard products from 01-February-2027 (AL Circle, 18-November). Still no official confirmation of the reported US-Canada deal; 50% Section 232 rate unchanged. ")+p['update']
        p['src']=[L_CA,S_CA]; hit+=1
assert hit==1

s=d['inputs_summary']
d['inputs_summary']=("UPDATE 19-NOVEMBER: no new LME official was published at run time, so the Copper series stays on the 17-November window (28-October to 17-November); no new carbon, fluoride, silicon or magnesium mark was located (gaps stay gaps). Energy softer: Brent about $92.1 and European gas about EUR 82/MWh, storage toward 70% (Trading Economics, 19-November). "+s)

d['sources'].insert(0,["Westmetall - LME official prices and stocks; newest published session 17-Nov-2026 at 19-Nov run time (EN/DE overviews and Al/Cu per-metal tables agree); board carried",W])
for x in ([L_ST,S_ST],[L_TE,S_TE],[L_BR,S_BR],[L_TD,S_TD],[L_TG,S_TG],[L_BRC,S_BRC],[L_CA,S_CA]): d['sources'].append(x)
for x in ([L_BRC,S_BRC],[L_TE,S_TE],[L_CA,S_CA],[L_ST,S_ST]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-17',3060.5,2940.0,220350]
ph['updated']=RD   # no new session: row unchanged
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',cnt)
