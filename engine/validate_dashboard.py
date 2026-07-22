#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_dashboard.py — MANDATORY pre-publish gate for the Aluminum dashboard (v2).

Run AFTER build_data_json.py and BEFORE the git push. Non-zero exit = DO NOT PUBLISH.

    python3 validate_dashboard.py "$ENGDIR" "$SITE"

The site is now a built React SPA that renders from a camelCase data.json through a
defensive adapter (it never throws; a missing/malformed section hides itself). The
fatal class is therefore no longer "renderer throws" but "a critical section is
EMPTY", which would show placeholders on an executive dashboard. This gate asserts
the new contract and fails if any must-have section is missing or empty, and enforces
the same freshness rule as before (data must carry today's report date).

v1 (old snake_case + jsdom render of the client-renderer) kept as
validate_dashboard_v1_oldschema.py.bak for reference.
"""
import json, os, sys

ENGDIR = sys.argv[1] if len(sys.argv) > 1 else "."
SITE   = sys.argv[2] if len(sys.argv) > 2 else ENGDIR
DATA   = os.path.join(SITE, "data.json")
INDEX  = os.path.join(SITE, "index.html")

fails, warns = [], []
def fail(m): fails.append(m)

if not os.path.exists(DATA):
    print("FATAL: %s not found — run build_data_json.py first." % DATA); sys.exit(2)
try:
    D = json.load(open(DATA, encoding="utf-8"))
except Exception as ex:
    print("FATAL: data.json is not valid JSON — %s" % ex); sys.exit(1)

def is_list(x): return isinstance(x, list)
def nonempty_list(x): return isinstance(x, list) and len(x) > 0

# ── Contract: critical sections that MUST be present and non-empty ───────────
# (empty here = blank/placeholder section on the live exec dashboard)
meta = D.get("meta") or {}
sw   = D.get("soWhat") or {}
lme  = D.get("lme") or {}
ew   = D.get("elliottWave") or {}
outl = D.get("outlook") or {}

if not sw.get("headline"):                 fail("soWhat.headline is empty (hero brief)")
if not nonempty_list(sw.get("bullets")):   fail("soWhat.bullets is empty")
if not nonempty_list(D.get("kpis")):       fail("kpis is empty (KPI cards)")
if not nonempty_list(lme.get("series")):   fail("lme.series is empty (price/stock chart)")
bench = lme.get("benchmark") or {}
if bench.get("cash") is None and bench.get("threeMonth") is None:
    fail("lme.benchmark has neither cash nor threeMonth")
if not nonempty_list(D.get("baseMetals")): fail("baseMetals is empty (metals board)")
prem = D.get("premiums") or {}
if not nonempty_list(prem.get("regional")):fail("premiums.regional is empty")
lt = (ew.get("longTerm") or {}).get("points")
st = (ew.get("shortTerm") or {}).get("points")
if not (nonempty_list(lt) or nonempty_list(st)):
    fail("elliottWave has no points in either panel (technicals section)")
if not (nonempty_list(D.get("news")) or nonempty_list(D.get("peers"))):
    fail("news AND peers both empty")
if not (outl.get("consensus") or nonempty_list(outl.get("catalysts")) or nonempty_list(outl.get("risks"))):
    fail("outlook is empty (consensus/catalysts/risks all missing)")
if not nonempty_list(D.get("sources")):    fail("sources is empty")

# ── Type sanity where the app calls .map() ──────────────────────────────────
for k in ["kpis", "baseMetals", "news", "peers", "sources"]:
    if k in D and not is_list(D[k]):
        fail("%s must be a LIST, got %s" % (k, type(D[k]).__name__))
for path_, v in [("lme.series", lme.get("series")),
                 ("premiums.regional", prem.get("regional")),
                 ("premiums.quarterly", prem.get("quarterly")),
                 ("macro.row", (D.get("macro") or {}).get("row")),
                 ("outlook.catalysts", outl.get("catalysts")),
                 ("outlook.risks", outl.get("risks"))]:
    if v is not None and not is_list(v):
        fail("%s must be a LIST, got %s" % (path_, type(v).__name__))

# ── Freshness / anti-stale ──────────────────────────────────────────────────
exp = os.environ.get("EXPECT_DATE")
gen = meta.get("generatedAt")
if exp and gen != exp:
    fail("meta.generatedAt %r != expected %r (stale data — refresh did not update)" % (gen, exp))
elif not gen:
    warns.append("meta.generatedAt is empty — cannot verify freshness")

# ── index.html sanity (built React shell must reference its bundle) ─────────
if os.path.exists(INDEX):
    html = open(INDEX, encoding="utf-8", errors="ignore").read()
    if 'id="root"' not in html:
        warns.append('index.html has no <div id="root"> — is it the built React shell?')
    if "assets/" not in html and "<script" not in html:
        warns.append("index.html references no assets bundle — shell may be broken")
else:
    warns.append("index.html not found in SITE dir (shell is committed once; ok if only data.json is republished)")

# ── Verdict ─────────────────────────────────────────────────────────────────
print("── Contract (v2 camelCase, non-empty critical sections)")
if fails:
    for f in fails: print("  ✗ " + f)
else:
    print("  ✓ all critical sections present and non-empty")
for w in warns: print("  ! WARN: " + w)
if fails:
    print("\n=== VALIDATION FAILED — DO NOT PUBLISH (%d issue%s) ===" % (len(fails), "" if len(fails)==1 else "s"))
    sys.exit(1)
print("=== VALIDATION PASSED — safe to publish ===")
sys.exit(0)
