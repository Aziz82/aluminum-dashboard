#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""forward_model.py — market-implied forward baseline + probability cone + rules-based
driver scorecard with a measured backtest, all computed from LME official prices.

INPUTS  : price_history.json (weekly LME cash / 3M / stock, sourced from Westmetall)
OUTPUT  : writes the 'forward' block into market_data.json

Design rules (deliberate, for defensibility):
  * The forward BASELINE is the LME 3-month official price — a real traded market price,
    not a model output. Beyond 3M no public longer-dated quote is sourced, so the baseline
    is held flat and that assumption is stated on the dashboard.
  * The RANGE is a random-walk cone: F * exp(±z * sigma * sqrt(t)), sigma = realized
    volatility of weekly log returns. It is a probability distribution, not a forecast.
  * The DRIVER SCORE is three transparent rules (carry, inventory, momentum), each
    +1/-1, and its historical hit rate is MEASURED here — never asserted.
Usage: python3 forward_model.py <engine_dir>
"""
import json, math, os, sys, datetime

ENG = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
H = json.load(open(os.path.join(ENG, "price_history.json"), encoding="utf-8"))
rows = H["rows"]
dates = [r[0] for r in rows]
cash = [float(r[1]) for r in rows]
m3 = [float(r[2]) for r in rows]
stock = [float(r[3]) for r in rows]
N = len(rows)

# ---------- realized volatility (weekly log returns) ----------
def logret(series):
    return [math.log(series[i] / series[i - 1]) for i in range(1, len(series))]

rets = logret(m3)

def stdev(x):
    if len(x) < 2: return 0.0
    mu = sum(x) / len(x)
    return math.sqrt(sum((v - mu) ** 2 for v in x) / (len(x) - 1))

WIN = 26  # ~6 months of weekly observations
sig_w = stdev(rets[-WIN:])            # weekly sigma
sig_ann = sig_w * math.sqrt(52.0)     # annualised
sig_w_2y = stdev(rets)                # full-sample weekly sigma (context)

# ---------- probability cone around the market forward ----------
F = m3[-1]          # LME 3-month official = market baseline
SPOT = cash[-1]
Z68, Z95 = 1.0, 1.96
HORIZONS = [("1 month", 4), ("3 months", 13), ("6 months", 26)]
cone = []
for label, wks in HORIZONS:
    s = sig_w * math.sqrt(wks)
    cone.append({
        "horizon": label,
        "weeks": wks,
        "central": round(F, 1),
        "lo68": round(F * math.exp(-Z68 * s), 1),
        "hi68": round(F * math.exp(Z68 * s), 1),
        "lo95": round(F * math.exp(-Z95 * s), 1),
        "hi95": round(F * math.exp(Z95 * s), 1),
    })

# Weekly cone path for the chart: the same maths sampled every week to 26 weeks, so the
# fan opens smoothly across a meaningful share of the plot instead of three cramped points.
_last = datetime.date.fromisoformat(dates[-1])
cone_path = []
for wk in range(1, 27):
    s = sig_w * math.sqrt(wk)
    cone_path.append({
        "date": (_last + datetime.timedelta(weeks=wk)).isoformat(),
        "weeks": wk,
        "central": round(F, 1),
        "lo68": round(F * math.exp(-Z68 * s), 1),
        "hi68": round(F * math.exp(Z68 * s), 1),
        "lo95": round(F * math.exp(-Z95 * s), 1),
        "hi95": round(F * math.exp(Z95 * s), 1),
    })

# ---------- rules-based driver signals ----------
def ma(series, n, i):
    seg = series[max(0, i - n + 1): i + 1]
    return sum(seg) / len(seg)

def signals_at(i):
    """Three transparent rules, each +1 (bullish) / -1 (bearish) / 0 (flat).
    Uses ONLY information available at week i (no look-ahead)."""
    carry = cash[i] - m3[i]                      # >0 = backwardation = prompt tightness
    s_carry = 1 if carry > 0 else (-1 if carry < 0 else 0)
    if i >= 13:
        inv_chg = (stock[i] - stock[i - 13]) / stock[i - 13]
        s_inv = 1 if inv_chg < -0.02 else (-1 if inv_chg > 0.02 else 0)
    else:
        inv_chg, s_inv = 0.0, 0
    mom_ma = ma(m3, 20, i)
    s_mom = 1 if m3[i] > mom_ma else (-1 if m3[i] < mom_ma else 0)
    return s_carry, s_inv, s_mom, carry, (inv_chg if i >= 13 else None), mom_ma

# ---------- backtest (honest: measured, overlapping windows declared) ----------
# NOTE ON THE RESULT: measured on 2024-2026 weekly data the composite driver score showed
# NO predictive edge — directional hit rate came in BELOW the naive "always up" baseline,
# and conditional forward returns ran opposite to the score (bullish readings preceded
# weaker returns, i.e. mean reversion after spikes). The sample is short, dominated by one
# uptrend, and uses overlapping windows, so the inverse relationship is NOT trustworthy
# either. We therefore publish the drivers as DIAGNOSTICS of current market condition and
# publish this evidence alongside them — we do not dress them up as a forecast.
HB = 13  # forward horizon in weeks (~1 quarter)
START = 20  # need 20 weeks of MA history
hits = tot = 0
bull_h = bull_t = bear_h = bear_t = 0
ups = 0
for i in range(START, N - HB):
    sc, si, sm, *_ = signals_at(i)
    score = sc + si + sm
    fwd = m3[i + HB] - m3[i]
    if fwd > 0: ups += 1
    if score == 0: continue
    tot += 1
    ok = (score > 0 and fwd > 0) or (score < 0 and fwd < 0)
    hits += 1 if ok else 0
    if score > 0:
        bull_t += 1; bull_h += 1 if fwd > 0 else 0
    else:
        bear_t += 1; bear_h += 1 if fwd < 0 else 0

base_n = N - HB - START
hit_rate = round(100.0 * hits / tot, 1) if tot else None
base_rate = round(100.0 * ups / base_n, 1) if base_n > 0 else None

# conditional mean forward return by score sign — the proper test under a trending sample
def _cond(sign):
    rs = [(m3[i + HB] / m3[i] - 1) * 100 for i in range(START, N - HB)
          if (sum(signals_at(i)[:3]) > 0) == (sign > 0) and sum(signals_at(i)[:3]) != 0]
    return round(sum(rs) / len(rs), 2) if rs else None
cond_bull, cond_bear = _cond(1), _cond(-1)
edge = None
if cond_bull is not None and cond_bear is not None:
    edge = round(cond_bull - cond_bear, 2)
has_edge = bool(hit_rate and base_rate and hit_rate > base_rate and (edge or 0) > 0)

# ---------- current reading ----------
i = N - 1
s_carry, s_inv, s_mom, carry_v, inv_chg_v, mom_ma_v = signals_at(i)
score = s_carry + s_inv + s_mom
LBL = {1: "Tightening", 0: "Neutral", -1: "Loosening"}
if score >= 2: stance = "Tight"
elif score == 1: stance = "Mildly tight"
elif score == 0: stance = "Balanced"
elif score == -1: stance = "Mildly loose"
else: stance = "Loose"

drivers = [
    {"name": "Curve carry (cash − 3M)",
     "value": f"{carry_v:+,.2f} $/t",
     "reading": LBL[s_carry], "score": s_carry,
     "rule": "Backwardation (cash above 3M) = prompt physical tightness = bullish; contango = bearish.",
     "basis": "LME official cash and 3-month settlement."},
    {"name": "Inventory trend (13-week)",
     "value": (f"{inv_chg_v*100:+.1f}%" if inv_chg_v is not None else "n/a"),
     "reading": LBL[s_inv], "score": s_inv,
     "rule": "LME stock falling more than 2% over 13 weeks = tightening = bullish; rising >2% = bearish.",
     "basis": "LME warehouse stock."},
    {"name": "Momentum (3M vs 20-week average)",
     "value": f"{m3[i]:,.0f} vs {mom_ma_v:,.0f}",
     "reading": LBL[s_mom], "score": s_mom,
     "rule": "Price above its 20-week average = uptrend = bullish; below = bearish.",
     "basis": "LME official 3-month."},
]

# history of the composite score (for the mini trend on the dashboard)
score_hist = []
for j in range(max(START, N - 52), N):
    a, b, c, *_ = signals_at(j)
    score_hist.append({"date": dates[j], "score": a + b + c, "price": m3[j]})

out = {
    "as_of": H.get("updated"),
    "basis": "LME official prices via Westmetall. Baseline = LME 3-month official (a traded market price). Range = random-walk cone from realized volatility. Driver score = 3 transparent rules, hit rate measured on history.",
    "source": H.get("source"),
    "spot_cash": round(SPOT, 1),
    "forward_3m": round(F, 1),
    "vol": {
        "weekly_pct": round(sig_w * 100, 2),
        "annual_pct": round(sig_ann * 100, 1),
        "window_weeks": WIN,
        "full_sample_weekly_pct": round(sig_w_2y * 100, 2),
    },
    "cone": cone,
    "cone_path": cone_path,
    "stance": stance,
    "score": score,
    "score_max": 3,
    "stance_label": "Current physical-market condition (diagnostic, not a forecast)",
    "drivers": drivers,
    "score_history": score_hist,
    "backtest": {
        "horizon_weeks": HB,
        "observations": tot,
        "hit_rate_pct": hit_rate,
        "bull_calls": bull_t, "bull_hit_pct": round(100.0*bull_h/bull_t,1) if bull_t else None,
        "bear_calls": bear_t, "bear_hit_pct": round(100.0*bear_h/bear_t,1) if bear_t else None,
        "baseline_up_pct": base_rate,
        "cond_return_bullish_pct": cond_bull,
        "cond_return_bearish_pct": cond_bear,
        "edge_pp": edge,
        "has_edge": has_edge,
        "verdict": ("These condition indicators showed NO predictive edge when tested: a %s%% directional hit "
                    "rate against a %s%% naive 'always higher' baseline over the same sample, and forward "
                    "returns after 'tightening' readings averaged %s%% versus %s%% after 'loosening' readings. "
                    "They are therefore published as a read on CURRENT market condition only — not as a price "
                    "forecast. The forward baseline and probability range above are the forward-looking view."
                    % (hit_rate, base_rate, cond_bull, cond_bear)) if not has_edge else
                   ("Measured hit rate %s%% versus a %s%% naive baseline, with a %s pp return spread."
                    % (hit_rate, base_rate, edge)),
        "sample_start": dates[START], "sample_end": dates[N-1-HB] if N-1-HB >= 0 else dates[-1],
        "caveat": ("Measured on overlapping %d-week windows of weekly LME data (%d observations, %s to %s). "
                   "Overlapping windows overstate significance and the sample spans a single, largely rising "
                   "market — evidence in either direction is weak."
                   % (HB, tot, dates[START], dates[N-1-HB] if N-1-HB >= 0 else dates[-1])),
    },
    "history": [{"date": d, "price": p} for d, p in zip(dates[-104:], m3[-104:])],
}

MD = os.path.join(ENG, "market_data.json")
D = json.load(open(MD, encoding="utf-8"))
D["forward"] = out
json.dump(D, open(MD, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print("forward model written.")
print("  spot cash %.1f | 3M forward %.1f" % (SPOT, F))
print("  realized vol: %.2f%% weekly / %.1f%% annualised (%dw window)" % (sig_w*100, sig_ann*100, WIN))
for c in cone:
    print("  %-9s 68%%: %.0f–%.0f | 95%%: %.0f–%.0f" % (c["horizon"], c["lo68"], c["hi68"], c["lo95"], c["hi95"]))
print("  stance: %s (score %+d/3)" % (stance, score))
for d in drivers:
    print("    %-34s %-16s %s" % (d["name"], d["value"], d["reading"]))
print("  backtest: %s%% hit over %d obs (%dw horizon); baseline up-rate %s%%; bull %s%% / bear %s%%"
      % (hit_rate, tot, HB, base_rate,
         out["backtest"]["bull_hit_pct"], out["backtest"]["bear_hit_pct"]))
