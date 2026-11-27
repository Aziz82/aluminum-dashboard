# Daily data refresh - 2026-11-27 (FRIDAY, ~02:45 UTC, BEFORE the Friday ring). Board CARRIED on the WEDNESDAY 25-Nov LME official:
# the Thursday 26-Nov official could NOT be located - cache-busted Westmetall EN + DE overviews and the Al, Cu and Zn per-metal tables ALL still show
# 25-Nov as newest; WebSearch found no published 26-Nov official (only LME closing-price/CFD references). Per owner fallback (3) the prior session stays on the
# board, stated in caveats + so_what; everything else (macro, Hormuz, news, producer asof, risks, catalysts, EW review) refreshed from sourced pages.
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-11-27'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ST="https://straits.live/briefs/2026-11-27"; L_ST="Straits Daily Brief - Strait of Hormuz, 27-Nov-2026 (effectively closed; 1 transit on 22-Nov per IMF PortWatch; tanker struck by projectile per UKMTO; IRGC mine claims unconfirmed; AI-assisted, flagged data gaps)"
S_BR="https://tradingeconomics.com/commodity/brent-crude-oil"; L_BR="Trading Economics - Brent ~$96.35 on 27-Nov-2026, on track for first weekly gain in four weeks after Houthi strike on Saudi Jazan refinery and a Hormuz tanker strike; down ~13.7% over the month; OPEC+ meets Sunday 29-Nov"
S_TD="https://tradingeconomics.com/united-states/currency"; L_TD="Trading Economics - Dollar index ~103.71 (27-Nov-2026), second daily decline as Treasury yields fell; 25bp December hike near-certain, another possible in January"
S_TE="https://tradingeconomics.com/commodity/aluminum"; L_TE="Trading Economics - Aluminum ~2,809.50 (+0.31%) on 26-Nov-2026 (CFD reference); 'Aluminum hovers near 13-month low' (25-Nov)"
S_BM="https://www.bigmint.co/insights/detail/lme-aluminium-stock-drawdown-widening-backwardation-heighten-supply-concerns-ahead-of-expected-recovery-in-2027-812358"; L_BM="BigMint - LME aluminium stock drawdown, widening backwardation heighten supply concerns ahead of expected recovery in 2027 (26-Nov-2026): spread peaked ~$405/t on 23-Nov (highest since 1988); 2026 deficit 1.05 Mt, 2027 near balance (~39 kt surplus)"
S_301="https://www.alcircle.com/news/us-proposes-25-tariff-on-indian-goods-under-section-301-keeps-aluminium-and-steel-duties-separate-122120"; L_301="AL Circle - US proposes 25% tariff on Indian goods under Section 301, keeps aluminium and steel duties separate (26-Nov-2026)"
S_NS="https://www.alcircle.com/news/nanshan-aluminium-acquires-20-stake-in-indonesian-jv-for-just-1-122124"; L_NS="AL Circle - Nanshan Aluminium acquires 20% stake in Indonesian JV for $1 (26-Nov-2026): 67.95% of PT Bintan Fine Chem Indonesia, caustic soda/epichlorohydrin project ~CNY 1.87bn"
S_MM="https://www.alcircle.com/news/canyon-resources-seeks-a70m-as-minim-martap-bauxite-project-faces-major-reset-122118"; L_MM="AL Circle - Canyon Resources seeks A$70m as Minim Martap bauxite project faces major reset (26-Nov-2026)"
S_SMM="https://news.metal.com/"; L_SMM="SMM news - China's aluminium ingot inventory in three regions falls on 27-November (to about 287,000 t); 6063 billet inventory in two regions flat at 56,500 t (27-Nov-2026)"
S_LMEC="https://www.lme.com/market-data/reports-and-data/lme-closing-prices"

def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o
B={b['name']:b for b in d['benchmark']}
assert B['LME Cash settlement']['cur']==2849.0 and B['LME 3-month']['cur']==2760.0 and B['LME warehouse stock (t)']['cur']==219200
m3=2760.0

OLDV=("COMPILED THURSDAY 26-NOVEMBER-2026 ABOUT 02:40 LONDON - BEFORE TODAY'S LME RING (13:20 LONDON). THE BOARD IS THE WEDNESDAY 25-NOVEMBER-2026 LME OFFICIAL, THE LATEST PUBLISHED SESSION; it ROLLED ONE SESSION this run (the previous run carried Tuesday 24-November). ")
NEWV=("COMPILED FRIDAY 27-NOVEMBER-2026 ABOUT 02:45 LONDON - BEFORE TODAY'S LME RING (13:20 LONDON). THE BOARD IS CARRIED ON THE WEDNESDAY 25-NOVEMBER-2026 LME OFFICIAL: the Thursday 26-November official COULD NOT BE LOCATED THIS RUN - the cache-busted Westmetall English and German overviews and the aluminium, copper and zinc per-metal tables all still show 25-November as their newest session, and a web search found no published 26-November official. The 25-November figures were verified by the previous run and re-confirmed this run; nothing was estimated. ")
NC2="COMPILED THURSDAY 26-NOVEMBER-2026 BEFORE THE RING (LME BOARD ROLLED TO THE WEDNESDAY 25-NOVEMBER OFFICIAL, THE LATEST PUBLISHED SESSION)."
NC3="COMPILED FRIDAY 27-NOVEMBER-2026 BEFORE THE RING (LME BOARD CARRIED ON THE WEDNESDAY 25-NOVEMBER OFFICIAL - THE THURSDAY 26-NOVEMBER OFFICIAL WAS NOT YET PUBLISHED ON THE PUBLIC SOURCE)."
REPL=[(OLDV,NEWV),(NC2,NC3),
 ("REVIEWED 26-NOVEMBER: no newer public disclosure","REVIEWED 27-NOVEMBER: no newer public disclosure"),
 ("REVIEWED 26-NOVEMBER. NO NEW DATED","REVIEWED 27-NOVEMBER. NO NEW DATED"),
 ("Next print Thursday 26-November 13:20 London.","Thursday 26-November official not yet published on the public source; next print Friday 27-November 13:20 London.")]
cnt={}
def f(s):
    for a,b in REPL:
        if a in s: cnt[a[:25]]=cnt.get(a[:25],0)+s.count(a); s=s.replace(a,b)
    return s
for k in list(d.keys()):
    if k in ('report_date','ew','sources'): continue
    d[k]=walk(d[k],f)
print(cnt)
assert cnt.get(OLDV[:25],0)>=15
blob=json.dumps(d,ensure_ascii=False)
assert "COMPILED THURSDAY 26-NOVEMBER" not in blob

d['bottom_line']=("BOTTOM LINE: the board is carried on the 25-November official because Thursday's official was not yet published on the public source - cash $2,849.00, three-month $2,760.00 inside the extended wave (v) zone, an $89.00 backwardation after the LME's lending-rule change broke the squeeze, and visible stock at a 219,200 t series low. "
 "Scenario weights hold at 10% bull / 30% base / 60% bear (no new trigger on any published official). A settled close back above 2,994.50 would mark a completed C wave; above 3,097.50 negates the count; daily invalidation 3,289. Friday 27-November's official (13:20 London) also sets the weekly close tested against 2,750; OPEC+ meets Sunday 29-November.")
for fp in d['outlook']['forward_path']:
    if fp['tenor'].startswith('Cash'):
        fp['basis']=("THE WEDNESDAY 25-NOVEMBER-2026 OFFICIAL CASH SETTLEMENT OF $2,849.00 (CARRIED: the Thursday 26-November official was not yet on the public source at compile time). Next print Friday 27-November 13:20 London.")

d['lme_commentary']=("CARRIED BOARD - THE SQUEEZE PREMIUM HAS BEEN DEFLATED; THE FORWARD SITS NEAR A 13-MONTH LOW. The latest published official remains Wednesday 25-November: cash $2,849.00 (-$271.50) and three-month $2,760.00 (-$29.00), with the backwardation collapsed to $89.00 from $331.50 as the LME's cut in the aluminium Tom-Next lending threshold (50% to 30% of on-warrant stock) took effect; visible stock fell to a 219,200 t series low. Thursday 26-November's official was not yet on the public source at compile time. "
 "BigMint (26-November) puts the traded spread peak at about $405/t on 23-November, the highest since 1988, and the post-announcement spread at $105.75/t; it sees a 1.05 Mt global deficit in 2026 narrowing to near balance (about 39 kt surplus) in 2027 as Gulf capacity recovers and Indonesian output grows - broadly in line with the Trading Economics-cited surplus view and against Emkay Global's ~400 kt deficit. "
 "Reference CFD and LME closing-price marks (about $2,751-2,810) cited in press for 26-November are not officials and are not used on the board. Macro: Brent firmed to about $96.35 on fresh Gulf attacks; the dollar index eased to about 103.71 as yields fell.")
d['net_read']=("NET: BEARISH ON THE FORWARD; PROMPT SUPPORT REDUCED BUT NOT GONE. Against: three-month at $2,760.00 (latest official) near a 13-month low, the LME lending rule cutting the cash premium, reported LME approval for Indonesian Hua Chin metal, a hawkish Fed (December hike near-certain), and forecasts (BigMint, Trading Economics) of a 2027 move to balance or surplus. "
 "Supportive: a backwardation still at $89.00, visible stock at a 219,200 t series low, Hormuz still effectively closed with fresh attacks on Saudi energy infrastructure lifting Brent to about $96, and Emkay Global's view of a ~400 kt deficit through 2028.")

for s in d['outlook']['scenarios']:
    assert s['prob']=={'Bull':'10%','Base':'30%','Bear':'60%'}[s['case']]
    s['drivers']=("HELD 27-NOVEMBER AT 10/30/60: no new official was published since the 25-November print (three-month $2,760.00, inside the 2,700-2,790 extended-(v) zone), so no pre-registered trigger could fire. ")+s['drivers']

hit=0
for r in d['outlook']['risks']:
    if r['risk'].startswith('STRAIT OF HORMUZ'):
        r['risk']+=" UPDATE 27-NOVEMBER: Straits Daily Brief - still effectively closed (1 transit on 22-November vs 85/day pre-crisis); UKMTO reports a tanker struck by a projectile while transiting; a crew member from the 17-November attack on an ADNOC L&S vessel was found dead; IRGC mine-strike claims remain uncorroborated. Trading Economics reports a Houthi strike on Saudi Arabia's Jazan refinery. Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('THE COST FLOOR'):
        r['risk']+=" UPDATE 27-NOVEMBER: Brent about $96.35, on track for its first weekly gain in four weeks but still about 13.7% lower over the month (Trading Economics); OPEC+ meets 29-November. Trend held at DOWN."; r['trend']='down'; hit+=1
    elif r['risk'].startswith('THE FEDERAL RESERVE PATH'):
        r['risk']+=" UPDATE 27-NOVEMBER: the dollar index eased to about 103.71 as Treasury yields fell on safe-haven buying; a 25bp December hike remains near-certain with another possible in January (Trading Economics). Trend held at UP."; r['trend']='up'; hit+=1
    elif r['risk'].startswith('TARIFF POLICY'):
        r['risk']+=" UPDATE 27-NOVEMBER: AL Circle (26-November) reports the proposed Section 301 duty on India is up to 25% (17% with a deal) and would NOT stack on Section 232 aluminium and steel tariffs; not final."; hit+=1
assert hit==4,hit
hc=0
for cat in d['outlook']['catalysts']:
    if cat['date']=='Daily, from Thu 26-Nov':
        hc+=1; cat['date']='Daily, from Fri 27-Nov'
        cat['event']=("LATEST PUBLISHED OFFICIAL STILL WEDNESDAY 25-NOVEMBER (cash $2,849.00; three-month $2,760.00; backwardation $89.00; stock 219,200 t) - the Thursday 26-November official was not on the public source at compile time. NEXT: Friday 27-November official (13:20 London), which also sets the weekly close tested against 2,750; 2,750 and 2,700 remain the wave (v) objectives; whether the backwardation holds above $15.00 under the new lending rule; a settled close back above 2,994.50 marks a completed C wave; above 3,097.50 negates the count; invalidation 3,289. OPEC+ meeting Sunday 29-November; the December Fed meeting (25bp priced); first Q1-2027 Japanese premium offers (none located; S&P Global cites expectations near $190-200/t CIF Japan).")
assert hc==1
d['outlook']['ai_analysis'].insert(0,"FRIDAY 27-NOVEMBER (BOARD CARRIED ON THE 25-NOVEMBER OFFICIAL): Thursday's official was not yet on the public source, so nothing on the board moved. The structural read is unchanged - the LME's lending-rule change deflated the prompt premium (backwardation $89.00) while three-month sits at $2,760.00 near a 13-month low and visible stock at a 219,200 t series low. New this run: BigMint sees the 2026 deficit (1.05 Mt) narrowing to near balance in 2027; Brent firmed to about $96 on Gulf attacks; S&P Global-cited expectations for Q1-2027 Japanese premiums sit near $190-200/t, below Q4's $255. Weights hold at 10/30/60.")

st=d['ew']['short_term']; lt=d['ew']['long_term']
EWP=("REVIEWED 27-NOVEMBER - NO NEW OFFICIAL, COUNT HELD: the latest published three-month official is still 2,760.00 (25-November), inside the 2,700-2,790 extended wave (v) zone; Thursday's official was not on the public source at compile time, and reference CFD marks are not used for the count. No pivot is added. BASE CASE (about 55%): wave (v) completes in 2,700-2,760 before a corrective rebound toward 2,994.50-3,097.50. ALTERNATE (about 45%): a larger-degree leg toward 2,633. INVALIDATION: above 3,097.50 (count); 3,289 (bearish C-wave count). Confidence low. ")
EWL=("REVIEWED 27-NOVEMBER (FRIDAY, PRE-RING): today's official sets the weekly close. The base case (about 65%) - a correction of the 2,300-3,855 advance completing in the 2,700-2,850 zone - is held; the alternate toward the 78.6% retracement near 2,633 (about 35%) rises to about 45% on a weekly close below 2,750. A weekly close back above 2,994.50 would favour a completed correction; loses preference only on a weekly close above 3,110. Confidence moderate. ")
for k,pfx in (('short_term',EWP),('long_term',EWL)):
    w=d['ew'][k]['writeup']; assert w.startswith('REVIEWED 26-NOVEMBER'),k
    d['ew'][k]['writeup']=pfx+w
d['ew']['updated']=RD

M={m['name']:m for m in d['macro']}
M['Brent crude ($/bbl)'].update(value="96.4",day="about $96.35 on 27-November (-0.04%, Trading Economics); on track for first weekly gain in four weeks; Straits brief showed $91.67 late 26-November (timestamps differ)",
 note="REFRESHED FRIDAY 27-NOVEMBER-2026 (Trading Economics): Brent rose above $96 on attacks on Middle Eastern energy sites and tankers - Houthi militants hit Saudi Arabia's Jazan refinery and a tanker was struck in the Strait of Hormuz; still down about 13.7% over the month as Gulf shipments resume and the IEA sees a Q4 surplus; OPEC+ meets Sunday 29-November on 2027 policy. Levels approximate. SOURCE: "+S_BR)
M['US dollar index (DXY)'].update(value="103.71",day="about 103.71 on 27-November (-0.06%, Trading Economics), a second daily decline",
 note="REFRESHED FRIDAY 27-NOVEMBER-2026 (Trading Economics): the dollar slipped as Treasury yields fell on safe-haven demand, AI-investment worries and new US tariff plans; core PCE 3.3% y/y and Q3 GDP 4.3% keep a 25bp December hike near-certain with another possible in January. SOURCE: "+S_TD)

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS CARRIED ON THE COMPLETE WEDNESDAY 25-NOVEMBER-2026 LME OFFICIAL. THIS FRIDAY 27-NOVEMBER RUN IS COMPILED AT ABOUT 02:45 LONDON, BEFORE TODAY'S RING. THURSDAY 26-NOVEMBER WAS A TRADING DAY, BUT ITS OFFICIAL COULD NOT BE LOCATED ON THE PUBLIC SOURCE: the cache-busted Westmetall English and German overviews and the aluminium, copper and zinc per-metal tables all still show 25-November as their newest row, and a web search found no published 26-November official. Per the owner's fallback rule the prior session is kept rather than estimated; the board will roll two sessions once the source updates. "
 "Press marks for 26-November (LME closing-price table about $2,751 three-month; Trading Economics CFD about $2,809.50) are references, not officials, and are cited in text only.")
C[1]=("SOURCE CHECK THIS RUN (27-NOVEMBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both fetched and AGREE on the full 25-November session (aluminium cash 2,849.00, three-month 2,760.00, stock 219,200; copper 11,703.00/11,758.00; nickel 15,035.00/15,210.00; zinc 3,520.50/3,394.00; lead 1,792.00/1,827.00; EUR/USD MTLE 1.09430) - identical to the stored board; the aluminium, copper and zinc per-metal tables show 25-November as their newest row. The LME's own closing-prices page returned HTTP 403.")
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION"):
        C[i]=("MACRO ROWS ARE MIXED-SESSION AND LABELLED: Brent (about $96.35) and the dollar index (about 103.71) are Trading Economics readings for 27-November; TTF and the US ten-year row are CARRIED from earlier sessions (the ten-year page returned internally inconsistent readings this run, so it was not updated; US bond markets were shut 26-November for Thanksgiving). Trading Economics prices are contract-for-difference references, not official benchmarks. The Straits Daily Brief (27-November) is AI-assisted and flags AIS undercounting, duplicate headlines and uncorroborated claims (NewsNation tanker strike; IRGC mine claims).")
    elif cv.startswith("FETCH NOTE"):
        C[i]=("FETCH NOTE 27-NOVEMBER (FRIDAY, PRE-RING): no authorised fetch was blocked, but the LME's closing-prices page (found via search) returned HTTP 403. Westmetall EN and DE overviews plus the Al, Cu and Zn per-metal tables, Trading Economics aluminium/Brent/dollar/ten-year, AL Circle news, SMM news and the Straits Daily Brief (27-November) were fetched; BigMint was read via WebSearch. FALLBACK USED: rule (3) - on a trading day the new LME official was not found by fetch or search, so the 25-November session is carried. A search for Q1-2027 Japanese premium offers again located none. No earnings_history company was back-filled and no inputs hist mark was appended this run.")
d['inputs_summary']=("UPDATE 27-NOVEMBER: the LME board is carried on 25-November, so the Copper series is unchanged (window 05- to 25-November). No new carbon, fluoride, silicon or magnesium mark was located (gaps stay gaps). Energy: Brent about $96.35 on 27-November on Gulf attacks (Trading Economics). Raw materials: AL Circle reports Canyon Resources seeking A$70m as Cameroon's Minim Martap bauxite project faces a reset. "+d['inputs_summary'])

d['so_what']={"line":"No new LME official this run - Thursday's print was not yet public, so the board stays on 25-November (cash $2,849, three-month $2,760 near a 13-month low, an $89 backwardation after the LME's lending change, stock at a 219,200 t low) while Gulf attacks lifted Brent to about $96.",
 "points":[
 "WHAT MOVED: nothing on the LME board - the Thursday 26-November official could not be found on the public source at compile time, so the Wednesday 25-November official is carried. Reference marks quoted in press for 26-November (about $2,751-2,810) are not officials.",
 "WHY IT MATTERS: the LME's lower lending threshold has already taken most of the squeeze premium out of cash (backwardation $89 from a record-era ~$405 traded peak on 23-November, per BigMint), while three-month sits near a 13-month low on expected Indonesian supply and a hawkish Fed.",
 "48H DEVELOPMENTS: Brent rose to about $96 after a Houthi strike on a Saudi refinery and a tanker hit in Hormuz, which stays effectively closed; the US Section 301 proposal on India (up to 25%) would not stack on aluminium Section 232 duties; China's three-region ingot stocks fell again to about 287,000 t (SMM).",
 "WHAT TO WATCH: Friday's official and weekly close against $2,750 (the board rolls two sessions once the source updates), whether the backwardation holds above $15, OPEC+ on Sunday 29-November, and first Q1-2027 Japanese premium offers (expectations near $190-200/t, below Q4's $255)."]}

d['feed']=([
 {"when":"Fri 27-Nov","impact":"Mixed","text":"LME BOARD CARRIED: 26-Nov official not yet on the public source; board stays on 25-Nov (cash $2,849, 3M $2,760, backwardation $89, stock 219,200 t)."},
 {"when":"Fri 27-Nov","impact":"Bullish (cost)","text":"ENERGY: Brent ~$96.35 after Houthi strike on Saudi Jazan refinery and a Hormuz tanker strike; OPEC+ meets 29-Nov (Trading Economics)."},
 {"when":"Fri 27-Nov","impact":"Bullish","text":"HORMUZ: effectively closed (1 transit on 22-Nov); UKMTO tanker projectile report; IRGC mine claims unconfirmed (Straits brief 27-Nov)."},
 {"when":"Thu 26-Nov","impact":"Mixed","text":"OUTLOOK: BigMint sees a 1.05 Mt 2026 deficit narrowing to near balance (~39 kt surplus) in 2027; spread peaked ~$405/t on 23-Nov."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"LME","horizon":"Immediate","impact":"Mixed","url":W,
  "headline":"LME BOARD CARRIED - THURSDAY OFFICIAL NOT YET PUBLISHED ON THE PUBLIC SOURCE. At compile time on Friday 27-November the Westmetall English and German overviews and per-metal tables still showed Wednesday 25-November as the latest official (aluminium cash $2,849.00, three-month $2,760.00, stock 219,200 t). Press reference marks for 26-November ranged about $2,751-2,810 for three-month aluminium; they are not officials."},
 {"theme":"Market structure","horizon":"0-12 months","impact":"Mixed","url":S_BM,
  "headline":"SPREAD PEAKED NEAR $405/t, HIGHEST SINCE 1988 (BigMint, 26-November): LME stocks fell 56.5% from 509,250 t on 2-January to 221,400 t on 23-November; the traded spread eased to $105.75/t on 25-November after the LME's lending-rule change. BigMint sees a 1.05 Mt global deficit in 2026 and near balance (about 39 kt surplus) in 2027 as Gulf capacity recovers and Indonesian output grows."},
 {"theme":"Energy","horizon":"0-3 months","impact":"Bullish (cost)","url":S_BR,
  "headline":"BRENT ABOVE $96 ON GULF ATTACKS (Trading Economics, 27-November): Houthi militants hit Saudi Arabia's Jazan refinery and a tanker was struck in Hormuz; Brent is on track for its first weekly gain in four weeks but still down about 13.7% on the month; OPEC+ meets Sunday 29-November."},
 {"theme":"Hormuz","horizon":"Immediate","impact":"Bullish","url":S_ST,
  "headline":"HORMUZ STILL EFFECTIVELY CLOSED (Straits Daily Brief, 27-November): 1 transit on 22-November vs 85/day pre-crisis; UKMTO reports a tanker struck by a projectile while transiting; a crew member missing since the 17-November attack on an ADNOC L&S vessel has been found dead; IRGC mine-strike claims remain uncorroborated."},
 {"theme":"Trade policy","horizon":"3-12 months","impact":"Mixed","url":S_301,
  "headline":"SECTION 301 PROPOSAL ON INDIA WOULD NOT STACK ON ALUMINIUM 232 DUTIES (AL Circle, 26-November): USTR proposed up to 25% on Indian goods (17% with a trade deal) within a probe of 14 partners; Section 232 aluminium and steel tariffs stay separate; no effective date given."},
 {"theme":"Macro","horizon":"0-3 months","impact":"Mixed","url":S_TD,
  "headline":"DOLLAR EASES AS YIELDS FALL (Trading Economics, 27-November): the dollar index slipped to about 103.71 for a second session on safe-haven bond buying; a 25bp December Fed hike remains near-certain after core PCE rose to 3.3% y/y."},
 {"theme":"China","horizon":"Immediate","impact":"Bullish","url":S_SMM,
  "headline":"CHINA INGOT STOCKS DRAW AGAIN (SMM, 27-November): three-region aluminium ingot inventory fell to about 287,000 t (from 295,500 t on 26-November), with Wuxi and Gongyi lower; 6063 billet inventory flat at 56,500 t."},
 {"theme":"Raw materials","horizon":"3-12 months","impact":"Mixed","url":S_MM,
  "headline":"CAMEROON BAUXITE PROJECT RESET (AL Circle, 26-November): Canyon Resources is seeking A$70m as its Minim Martap bauxite project faces a major reset."},
]+d['news']
d['news']=d['news'][:20]
assert all(n.get('impact') for n in d['news'])
for p in d['producer_status']: p['asof']=RD

d['sources'].insert(0,["Westmetall - LME official prices and stocks, latest published session 25-Nov-2026 (EN and DE overviews and Al/Cu/Zn per-metal tables re-checked 27-Nov; no 26-Nov row yet)",W])
for x in ([L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_TE,S_TE],[L_BM,S_BM],[L_301,S_301],[L_NS,S_NS],[L_MM,S_MM],[L_SMM,S_SMM]): d['sources'].append(x)
for x in ([L_ST,S_ST],[L_BR,S_BR],[L_TD,S_TD],[L_BM,S_BM],[L_301,S_301]): d['outlook']['sources'].append(x)

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1]==['2026-11-25',2849.0,2760.0,219200]
ph['updated']=RD   # board carried; same week row unchanged
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
