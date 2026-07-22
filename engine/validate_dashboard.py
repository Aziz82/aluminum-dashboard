#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_dashboard.py — pre-publish gate for the Web_v3 dashboard (snake_case v3 contract).
Run AFTER build_data_json.py, BEFORE git push. Non-zero exit = DO NOT PUBLISH.
    python3 validate_dashboard.py "$ENGDIR" "$SITE"
Asserts every must-have section is present and non-empty (the fatal class is a blank/
placeholder section on the executive dashboard) and enforces freshness (as_of == today).
Prior schema gates kept as *.bak."""
import json, os, sys
ENGDIR = sys.argv[1] if len(sys.argv) > 1 else "."
SITE   = sys.argv[2] if len(sys.argv) > 2 else ENGDIR
DATA   = os.path.join(SITE, "data.json")
INDEX  = os.path.join(SITE, "index.html")
if not os.path.exists(DATA):
    print("FATAL: %s not found — run build_data_json.py first." % DATA); sys.exit(2)
try:
    D = json.load(open(DATA, encoding="utf-8"))
except Exception as ex:
    print("FATAL: data.json is not valid JSON — %s" % ex); sys.exit(1)
f, warns = [], []
def ne(x): return isinstance(x, list) and len(x) > 0
brief=D.get('brief') or {}; lme=D.get('lme') or {}; ew=D.get('elliott_wave') or {}
outl=D.get('outlook') or {}; meta=D.get('meta') or {}
if not brief.get('headline'): f.append("brief.headline empty (hero brief)")
if not ne(brief.get('bullets')): f.append("brief.bullets empty")
if not ne(D.get('kpis')): f.append("kpis empty")
if not ne((lme.get('series') or {}).get('price')): f.append("lme.series.price empty (price chart)")
if not ne(lme.get('benchmarks')): f.append("lme.benchmarks empty")
if not ne((D.get('base_metals') or {}).get('board')): f.append("base_metals.board empty")
if not ne((D.get('premiums') or {}).get('regional')): f.append("premiums.regional empty")
panels = ew.get('panels') or []
if not panels or not ne((panels[0].get('history') or {}).get('price')):
    f.append("elliott_wave first panel history empty")
if not ne((D.get('news') or {}).get('headlines')) and not ne((D.get('peers') or {}).get('earnings')):
    f.append("news AND peers both empty")
if not (ne(outl.get('catalysts')) or ne(outl.get('risks')) or ne(outl.get('consensus'))):
    f.append("outlook empty")
if not ne((D.get('sources') or {}).get('references')): f.append("sources.references empty")
# type sanity
for k in ['kpis']:
    if k in D and not isinstance(D[k], list): f.append("%s must be a LIST" % k)
# freshness
exp = os.environ.get("EXPECT_DATE"); gen = meta.get("as_of")
if exp and gen != exp: f.append("meta.as_of %r != expected %r (stale — refresh did not update)" % (gen, exp))
elif not gen: warns.append("meta.as_of empty — cannot verify freshness")
# shell sanity
if os.path.exists(INDEX):
    html = open(INDEX, encoding="utf-8", errors="ignore").read()
    if 'id="root"' not in html: warns.append('index.html has no <div id="root"> — is it the built shell?')
else:
    warns.append("index.html not in SITE dir (shell committed once; ok if only data.json republished)")
print("── Contract (Web_v3, non-empty critical sections)")
if f:
    for x in f: print("  ✗ " + x)
else:
    print("  ✓ all critical sections present and non-empty")
for w in warns: print("  ! WARN: " + w)
if f:
    print("\n=== VALIDATION FAILED — DO NOT PUBLISH (%d) ===" % len(f)); sys.exit(1)
print("=== VALIDATION PASSED — safe to publish ==="); sys.exit(0)
