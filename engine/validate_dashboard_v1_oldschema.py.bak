#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_dashboard.py — MANDATORY pre-publish gate for the Aluminum dashboard.

Run this AFTER build_data_json.py and BEFORE the git push. If it exits non-zero,
DO NOT PUBLISH: fix market_data.json, rebuild, re-validate.

    python3 validate_dashboard.py "$ENGDIR" "$SITE"

Two layers:

  LAYER 1 — CONTRACT (offline, pure python)
    Asserts the exact shapes index.html requires. Derived by reading the
    renderer, not by assumption. Catches the fatal class of bug directly:
    a field the renderer calls .map() on must be a LIST; a field it indexes
    as s[0]/s[1] must be a PAIR; row dicts must carry the keys the template
    interpolates.

  LAYER 2 — HEADLESS RENDER (jsdom)
    Executes the REAL index.html against the REAL data.json and fails if the
    page throws or any section comes back empty. This is the authoritative
    check and catches shape breaks the contract doesn't yet know about.

WHY THIS EXISTS (2026-07-13 incident)
    index.html wraps render() inside the fetch promise chain:
        fetch(...).then(r=>r.json()).then(D=>render(D)).catch(()=> show error)
    That single .catch() swallows BOTH network errors AND rendering exceptions,
    and always prints "Couldn't load data.json". On 13-Jul, outlook.ai_analysis
    was written as a string instead of a list; the renderer called .map() on it,
    threw, and the page showed a load error even though data.json was valid,
    served a clean 200, and had the correct report_date. Verifying the SERVED
    FILE therefore proves nothing. Only executing the renderer does.
"""
import json, os, subprocess, sys

ENGDIR = sys.argv[1] if len(sys.argv) > 1 else "."
SITE   = sys.argv[2] if len(sys.argv) > 2 else ENGDIR
DATA   = os.path.join(SITE, "data.json")
INDEX  = os.path.join(ENGDIR, "index.html")
HERE   = os.path.dirname(os.path.abspath(__file__))

fails, warns = [], []


def fail(msg):
    fails.append(msg)


# ── LAYER 1: CONTRACT ────────────────────────────────────────────────────────
# Fields the renderer calls .map()/rows() on → MUST be lists.
MUST_BE_LIST = [
    "kpi_cards", "benchmark", "premiums", "macro", "macro_events", "lme_series",
    "alumina", "alumina_notes", "alumina_explainer", "alumina_outlook",
    "raw_materials", "inputs", "inputs_summary", "logistics", "feed", "news",
    "earnings", "commercial", "caveats", "sources", "premium_explainer",
    "premium_outlook", "premium_quarters", "premium_drivers", "metals_board",
    "chart_price_axis", "chart_stock_axis",
]
OUTLOOK_MUST_BE_LIST = [
    "forward_path", "consensus", "balance", "capacity_pipeline",
    "scenarios", "risks", "catalysts",
    "ai_analysis",   # ← the 13-Jul fatal: a string is truthy, so `O.ai_analysis||[]`
                     #   does NOT fall back, and "".map is not a function.
    "sources",
]
# Lists whose ROWS are indexed as s[0]/s[1] → each row MUST be a [label, value] pair.
LIST_OF_PAIRS = ["sources"]
# Fields that are THEMSELVES a flat [label, url] pair (not a list of rows).
FLAT_PAIRS = ["premium_settlement_src"]
# Row dicts → required keys the template interpolates.
ROW_KEYS = {
    "kpi_cards":         {"label", "value", "delta"},
    "benchmark":         {"name", "cur", "prev", "note"},
    "premiums":          {"name", "cur", "prev", "avg", "src"},
    "macro":             {"name", "value", "note"},
    "metals_board":      {"name", "price", "day", "ytd"},
    "logistics":         {"name", "val", "note"},
    "news":              {"theme", "impact", "headline", "source"},
    "feed":              {"when", "impact", "text"},
    "earnings":          {"company", "period", "headline", "readthrough"},
    "premium_drivers":   {"t", "d", "src"},
    "premium_explainer": {"term", "desc"},
    "premium_quarters":  {"q", "v"},
}
OUTLOOK_ROW_KEYS = {
    "forward_path":      {"tenor", "price", "basis"},
    "consensus":         {"source", "y2026", "note"},
    "balance":           {"year", "value", "label"},
    "capacity_pipeline": {"asset", "change", "timing"},
    "risks":             {"risk", "likelihood", "impact", "trend"},   # ← broke 13-Jul
    "catalysts":         {"date", "event", "impact"},
}

if not os.path.exists(DATA):
    print("FATAL: %s not found — run build_data_json.py first." % DATA); sys.exit(2)
if not os.path.exists(INDEX):
    print("FATAL: %s not found." % INDEX); sys.exit(2)

try:
    D = json.load(open(DATA, encoding="utf-8"))
except Exception as ex:
    print("FATAL: data.json is not valid JSON — %s" % ex); sys.exit(1)

O = D.get("outlook", {})

for k in MUST_BE_LIST:
    if k not in D:
        fail("missing key: %s" % k)
    elif not isinstance(D[k], list):
        fail("%s must be a LIST, got %s  → renderer calls .map() on it and will throw"
             % (k, type(D[k]).__name__))

for k in OUTLOOK_MUST_BE_LIST:
    if k not in O:
        fail("missing key: outlook.%s" % k)
    elif not isinstance(O[k], list):
        fail("outlook.%s must be a LIST, got %s  → renderer calls .map() on it and will throw"
             % (k, type(O[k]).__name__))

for k in LIST_OF_PAIRS:
    for i, row in enumerate(D.get(k, []) or []):
        if not (isinstance(row, list) and len(row) >= 2):
            fail("%s[%d] must be a [label, value] PAIR, got %s  → renderer indexes s[0]/s[1]"
                 % (k, i, type(row).__name__))
            break

for k in FLAT_PAIRS:
    v = D.get(k)
    if v is not None and not (isinstance(v, list) and len(v) >= 2
                              and all(isinstance(x, str) for x in v[:2])):
        fail("%s must be a flat [label, url] pair of strings, got %r" % (k, v))
for i, row in enumerate(O.get("sources", []) or []):
    if not (isinstance(row, list) and len(row) >= 2):
        fail("outlook.sources[%d] must be a [label, url] PAIR, got %s  → renderer indexes s[0]/s[1]"
             % (i, type(row).__name__))
        break

for k, req in ROW_KEYS.items():
    for i, row in enumerate(D.get(k, []) or []):
        if not isinstance(row, dict):
            fail("%s[%d] must be an object, got %s" % (k, i, type(row).__name__)); break
        missing = req - set(row)
        if missing:
            fail("%s[%d] missing key(s): %s" % (k, i, ", ".join(sorted(missing)))); break

for k, req in OUTLOOK_ROW_KEYS.items():
    for i, row in enumerate(O.get(k, []) or []):
        if not isinstance(row, dict):
            fail("outlook.%s[%d] must be an object, got %s" % (k, i, type(row).__name__)); break
        missing = req - set(row)
        if missing:
            fail("outlook.%s[%d] missing key(s): %s" % (k, i, ", ".join(sorted(missing)))); break

if not all(isinstance(x, str) for x in (O.get("ai_analysis") or []) if True):
    fail("outlook.ai_analysis must be a list of STRINGS")

sw = D.get("so_what") or {}
if not isinstance(sw, dict) or "line" not in sw or not isinstance(sw.get("points"), list):
    fail("so_what must be {line: str, points: [str, ...]}")

# Freshness / anti-stale checks
if D.get("report_date") != os.environ.get("EXPECT_DATE", D.get("report_date")):
    fail("report_date %r != expected %r" % (D.get("report_date"), os.environ.get("EXPECT_DATE")))
if D.get("ew", {}).get("updated") != D.get("report_date"):
    warns.append("ew.updated (%s) != report_date (%s) — EW should be refreshed every run"
                 % (D.get("ew", {}).get("updated"), D.get("report_date")))

print("── Layer 1: contract")
if fails:
    for f in fails:
        print("  ✗ " + f)
else:
    print("  ✓ all shapes match the renderer contract")

# ── LAYER 2: HEADLESS RENDER ────────────────────────────────────────────────
print("── Layer 2: headless render (jsdom)")
js = os.path.join(HERE, "validate_dashboard.js")
if not os.path.exists(js):
    js = os.path.join(ENGDIR, "validate_dashboard.js")

render_ok = None
if not os.path.exists(js):
    warns.append("validate_dashboard.js not found — render check SKIPPED")
else:
    try:
        subprocess.run(["node", "-e", "require('jsdom')"], check=True,
                       capture_output=True, cwd="/tmp",
                       env={**os.environ, "NODE_PATH": "/tmp/node_modules"})
    except Exception:
        print("  … installing jsdom")
        subprocess.run(["npm", "install", "--prefix", "/tmp", "jsdom", "--silent"],
                       capture_output=True)
    r = subprocess.run(["node", js, INDEX, DATA], capture_output=True, text=True,
                       env={**os.environ, "NODE_PATH": "/tmp/node_modules"})
    out = (r.stdout or "") + (r.stderr or "")
    print(out.rstrip() or "  (no output)")
    if r.returncode == 2:
        warns.append("render check could not run (jsdom unavailable) — contract check only")
        render_ok = None
    else:
        render_ok = (r.returncode == 0)
        if not render_ok:
            fail("headless render FAILED — the dashboard would show an error card")

# ── VERDICT ─────────────────────────────────────────────────────────────────
print()
for w in warns:
    print("  ! WARN: " + w)
if fails:
    print("\n=== VALIDATION FAILED — DO NOT PUBLISH (%d issue%s) ==="
          % (len(fails), "" if len(fails) == 1 else "s"))
    sys.exit(1)
print("=== VALIDATION PASSED — safe to publish ===")
sys.exit(0)
