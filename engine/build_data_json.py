#!/usr/bin/env python3
"""Merge market_data.json (+ weekly_data.json) into a single data.json for the hosted dashboard.
Usage: python3 build_data_json.py <engine_dir> <output_dir>
Writes <output_dir>/data.json
"""
import json, os, sys, datetime
eng = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
out = sys.argv[2] if len(sys.argv) > 2 else eng
D = json.load(open(os.path.join(eng, "market_data.json"), encoding="utf-8"))
wkp = os.path.join(eng, "weekly_data.json")
D["weekly"] = json.load(open(wkp, encoding="utf-8")) if os.path.exists(wkp) else None
def _tone(s):
    s = str(s).lower()
    if "bull" in s or "pos" in s: return 1
    if "bear" in s or "neg" in s: return -1
    return 0
_items = [x.get("impact", "") for x in D.get("feed", [])] + [x.get("impact", "") for x in D.get("news", [])]
_pos = sum(1 for t in _items if _tone(t) > 0); _neg = sum(1 for t in _items if _tone(t) < 0); _tot = len(_items) or 1
_net = round((_pos - _neg) / _tot * 100)
_hp = os.path.join(eng, "sentiment_history.json")
try:
    _hist = json.load(open(_hp, encoding="utf-8"))
except Exception:
    _hist = []
_rd = D.get("report_date") or datetime.date.today().isoformat()
_hist = [h for h in _hist if h.get("date") != _rd]
_hist.append({"date": _rd, "net": _net})
_hist = _hist[-30:]
json.dump(_hist, open(_hp, "w", encoding="utf-8"))
D.setdefault("outlook", {})["sentiment_history"] = _hist

# --- EW guardrail: enforce the REAL latest LME 3M price as the 'now' anchor ---
# Prevents the daily AI re-analysis from drifting the current price / inventing a 'now' point.
# Historical wave pivots are locked; anything at/after now_x is treated as projection, not history.
try:
    _ls = D.get("lme_series") or []
    _cur3m = _ls[0][2] if _ls and len(_ls[0]) > 2 else None
    if _cur3m is not None:
        for _k in ("long_term", "short_term"):
            _P = (D.get("ew") or {}).get(_k)
            if not isinstance(_P, dict):
                continue
            _nx = _P.get("now_x")
            _P["now_p"] = _cur3m  # real current price, engine-injected
            if _nx is not None:
                if isinstance(_P.get("waves"), list):
                    _P["waves"] = [w for w in _P["waves"] if w.get("t", 0) < _nx - 1e-9]
                if isinstance(_P.get("line"), list):
                    _P["line"] = [pt for pt in _P["line"] if pt and pt[0] < _nx - 1e-9]
                if isinstance(_P.get("proj"), dict):
                    for _kk, _arr in _P["proj"].items():
                        if _arr:
                            _arr[0] = [_nx, _cur3m]
            if isinstance(_P.get("annos"), list):
                _P["annos"] = [a for a in _P["annos"] if "now" not in str(a.get("text", "")).lower()]
except Exception as _e:
    print("EW guardrail skipped:", _e)

D["generated"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
path = os.path.join(out, "data.json")
json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("saved", path)
