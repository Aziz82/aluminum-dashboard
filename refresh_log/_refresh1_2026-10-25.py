# Daily data refresh - 2026-10-25 (SUNDAY, ~02:40 UTC). Board CARRIED on the FRIDAY 23-Oct LME official (no ring Sat/Sun).
# Westmetall cache-busted EN + DE overviews re-fetched: both show 23-Oct session with identical figures (Al cash 3,043 / 3M 3,018 / stock 235,800; MTLE 1.11910);
# Al per-metal table top row = 23-Oct, NO later row. New items: SMM overnight report (25-Oct 10:09 GMT+8) - LME Al +1.03%, SHFE Al +1.62% overnight Fri,
# Brent +6.85% on the week (4th weekly gain); SMM 23-Oct: 30kt alumina traded $361/t FOB India (Nov shipment). IRGC claim of halted Hormuz shipping (Iranian state TV, unverified).
import json
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
RD='2026-10-25'; d['report_date']=RD
W="https://www.westmetall.com/en/markdaten.php"
S_ON="https://news.metal.com/newscontent/104176874-crude-oil-surges-base-metals-broadly-rise-lme-zinc-leads-the-gains-lme-copper-shfe-aluminum-and-shfe-tin-post-top-gains-gold-and-silver-plunge-on-the-weekly-chart-overnight-market"
L_ON="SMM - Overnight market: crude oil surges, base metals broadly rise (published 25-Oct-2026, covering the 23/24-Oct overnight session)"
S_AI="https://news.metal.com/newscontent/104176830-30000-mt-alumina-traded-at-361mt-fob-india-for-nov-shipment"; L_AI="SMM - 30,000 mt alumina traded at $361/mt FOB India for November shipment (23-Oct-2026)"
S_HZ="https://see.news/iranian-tv-announces-halt-to-strait-of-hormuz-shipping"; L_HZ="SEE News - Iranian TV announces halt to Strait of Hormuz shipping (Oct-2026; Iranian claim, unverified)"

def walk(o):
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    if isinstance(o,str):
        o=o.replace("COMPILED SATURDAY 24-OCTOBER-2026","COMPILED SUNDAY 25-OCTOBER-2026")
        o=o.replace("REVIEWED 24-OCTOBER: no newer public disclosure","REVIEWED 25-OCTOBER: no newer public disclosure").replace("REVIEWED 24-OCTOBER. NO NEW DATED","REVIEWED 25-OCTOBER. NO NEW DATED")
    return o
for k in ('kpi_cards','benchmark','premiums','alumina','metals_detail','producer_status'):
    d[k]=walk(d[k])
for p in d['producer_status']: p['asof']=RD

C=d['caveats']
C[0]=("THE BOARD ON THIS PAGE IS THE COMPLETE FRIDAY 23-OCTOBER-2026 LME OFFICIAL, CARRIED THROUGH THE WEEKEND BECAUSE THE MARKET IS SHUT (no ring Saturday or Sunday); this Sunday 25-October run changes no board figure. The next official prints Monday 26-October at 13:20 London. Reference and overnight prices (Trading Economics, SMM) are cited in text only and are NOT used on the board.")
C[1]=("SOURCE CHECK THIS RUN (25-OCTOBER): the cache-busted Westmetall ENGLISH AND GERMAN overviews were both RE-FETCHED and still show the 23-October session with identical prices, stocks and FX fixings (EUR/USD MTLE 1.11910), and the per-metal aluminium daily table shows NO row after 23-October (cash 3,043.00, three-month 3,018.00, stock 235,800), so the carried board is complete rather than lagging.")
for i,cv in enumerate(C):
    if cv.startswith("MACRO ROWS ARE MIXED-SESSION") and "25-OCTOBER" not in cv:
        C[i]=cv+" These are the FRIDAY 23-OCTOBER closes, carried through the weekend (no new session); they were not re-fetched individually on Sunday 25-October. SMM's overnight report (25-October) puts Brent +6.85% on the week, a fourth straight weekly gain - cited in text only."
    if cv.startswith("FETCH NOTE 24-OCTOBER"):
        C[i]=("FETCH NOTE 25-OCTOBER: no authorised fetch was blocked for the board (Westmetall EN, DE and per-metal pages all fetched). Two SMM article links on the metal.com/en host returned HTTP 500; the same articles were fetched on the news.metal.com host instead. "
              "The Iranian claim that movement of 'non-compliant' vessels through Hormuz has been halted comes from Iranian state TV as reported by news aggregators and was NOT independently confirmed - it is cited as reported, not as fact. The SMM overnight +1.03% LME aluminium move is a post-official electronic close and is NOT used on the board.")

d['so_what']={"line":"Weekend check: aluminium holds Friday's $3,018 three-month with a confirmed $25 backwardation and record-low LME stock, while a fourth straight weekly jump in oil keeps the energy-cost floor rising into Monday's open and Wednesday's Fed decision.",
 "points":[
 "WHERE IT STANDS: the board is Friday's 23-October LME official - cash $3,043.00 and three-month $3,018.00 (both +$10.00), a $25.00 backwardation (cash above three-month) for a second straight session, and LME stock at a new low of 235,800 t. Nothing trades on the LME until Monday's 13:20 London official.",
 "AFTER THE RING: aluminium kept rising in Friday's later trade - SMM's overnight report (25-October) shows LME aluminium +1.03% and Shanghai aluminium +1.62% - a hint that Monday may open higher, but that is not an official price.",
 "ENERGY: SMM reports Brent up 6.85% on the week, a fourth straight weekly gain, on Houthi attacks on Saudi oil facilities, a drone strike on Aramco's Shaybah field and an Iranian claim that shipping through Hormuz has stopped (not independently confirmed). Higher power and fuel costs raise the cost floor for smelters outside China.",
 "WHAT TO WATCH THIS WEEK: Monday's official versus Friday's close; a settled three-month above $3,061.5-3,077 (price confirming the tight curve) or below $2,994.50; the FOMC decision on 28-October; China's Fifth Plenary Session (26-29 October)."]}

d['feed']=([
 {"when":"Sun 25-Oct","impact":"Mixed","text":"WEEKEND CHECK: board CARRIED on the Friday 23-October LME official (cash $3,043.00, three-month $3,018.00, $25.00 backwardation, stock 235,800 t); Westmetall English and German pages re-checked - no later session. Next official Monday 26-October."},
 {"when":"Sat 24-Oct","impact":"Bullish","text":"SMM overnight report: LME aluminium +1.03% and SHFE aluminium +1.62% in Friday's later trade (not an official price); Brent +3.72% overnight and +6.85% on the week, a fourth weekly gain; US dollar index 101.75."},
]+d['feed'])[:12]

d['news']=[
 {"theme":"Market","horizon":"0-1 month","impact":"Bullish (cost)","url":S_ON,
  "headline":"OVERNIGHT: BASE METALS RISE, CRUDE SURGES (SMM, published 25-October): in Friday's overnight session LME aluminium rose 1.03% and the most-traded SHFE aluminium contract 1.62%, with cast aluminium +1.74% and alumina futures -0.51%. Brent rose 3.72% overnight and 6.85% on the week (a fourth straight weekly gain), WTI 3.99%, on Houthi attacks on Saudi oil facilities, a drone strike on Aramco's Shaybah field, an IRGC statement that Hormuz shipping had stopped and reports of two supertankers striking mines; a reported G7 strategic-reserve release did not stop the rally. Markets expect US rates higher for longer into the 28-October FOMC; University of Michigan sentiment fell to 48.0. READ: post-official moves point to a firmer Monday open, but the board stays on Friday's official."},
 {"theme":"Raw materials","horizon":"0-1 month","impact":"Bearish (cost)","url":S_AI,
  "headline":"ALUMINA SPOT TRADE AT $361/t FOB INDIA (SMM, 23-October): 30,000 t of alumina traded at $361/t FOB India for November shipment - $21/t below the $382/t FOB India trade SMM reported on 16-October. READ: ex-China alumina keeps softening, which eases smelter raw-material cost even as energy costs rise. Origin-specific trade cited as context only; not substituted into the alumina rows."},
]+d['news']
d['news']=d['news'][:20]

for r in d['outlook']['risks']:
    if 'HORMUZ' in r['risk']:
        r['risk']+=" UPDATE 25-OCTOBER: SMM (25-October) reports an IRGC statement that shipping in the strait had stopped and two supertankers striking mines; Iranian state TV says movement of 'non-compliant' vessels is halted (not independently confirmed). Brent +6.85% on the week. Trend held at UP."
        r['trend']='up'
d['outlook']['ai_analysis'].insert(0,"SUNDAY CHECK, 25-OCTOBER: no LME session since Friday's 23-October official (three-month $3,018.00, +$10.00; week +$6.00; backwardation $25.00 confirmed; stock 235,800 t), so the price read is unchanged: the curve has turned tight while price stays beneath the 3,061.5 July low. Post-official trade was firmer (SMM: LME aluminium +1.03%, SHFE +1.62% overnight) and Brent closed a fourth straight weekly gain (+6.85%), both supportive. Ex-China alumina kept softening ($361/t FOB India, down from $382/t a week earlier), a partial offset on the cost side. Monday's official is the first test of whether price follows the curve above 3,061.5.")

EWS="REVIEWED 25-OCTOBER (SUNDAY, NO NEW SESSION): count and levels unchanged from the 24-October review - wave (v) low at 2,994.50 favoured as complete but not confirmed; confirmation is a settled close above 3,077; re-count below about 2,977.5; invalidation 3,289. The firmer post-official trade on Friday is not a settled official and does not change the count. "
d['ew']['short_term']['writeup']=EWS+d['ew']['short_term']['writeup']
d['ew']['long_term']['writeup']="REVIEWED 25-OCTOBER (SUNDAY, NO NEW SESSION): the weekly close of 3,018.00 stands; corrective count towards 2,894 unchanged. "+d['ew']['long_term']['writeup']
d['ew']['updated']=RD

for s in d['outlook']['scenarios']:
    s['drivers']="HELD 25-OCTOBER at 15/45/40: no new session over the weekend; firmer post-official trade and a fourth weekly oil gain are supportive but not price confirmation. "+s['drivers']

d['inputs_summary']=("UPDATE 25-OCTOBER (SUNDAY): no new LME session, so Copper's fifteen-session window stays at 05-October to 23-October (last mark $14,415.00 cash). No new monthly carbon settlement or dated SMM fluoride, silicon or magnesium mark was published over the weekend, so no hist mark was appended. Energy: SMM (25-October) reports Brent +6.85% on the week, a fourth straight weekly gain. Ex-China alumina: SMM reports 30,000 t traded at $361/t FOB India (23-October), down from $382/t on 16-October - context only. "+d['inputs_summary'])

d['sources'].insert(0,["Westmetall - LME official prices and stocks, 23-Oct-2026 session re-checked 25-Oct (English and German overviews agree; no later row)",W])
for x in ([L_ON,S_ON],[L_AI,S_AI],[L_HZ,S_HZ]): d['sources'].append(x)
d['outlook']['sources'].append([L_ON,S_ON]); d['outlook']['sources'].append([L_HZ,S_HZ])

ph=json.load(open('price_history.json',encoding='utf-8'))
assert ph['rows'][-1][0]=='2026-10-23', ph['rows'][-1]
ph['updated']=RD
json.dump(ph,open('price_history.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
