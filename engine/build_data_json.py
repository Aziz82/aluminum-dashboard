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
D["generated"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
path = os.path.join(out, "data.json")
json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("saved", path)
