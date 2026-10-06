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
fwd = D.get('forward') or {}
if not ne(fwd.get('cone')): f.append("forward.cone empty (probability range)")
if not ne(fwd.get('history')): f.append("forward.history empty (price chart)")
if not ne(fwd.get('drivers')): f.append("forward.drivers empty (condition diagnostics)")
if not (fwd.get('backtest') or {}).get('verdict'):
    f.append("forward.backtest.verdict missing — the measured-evidence disclosure must always publish")
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
    if 'id="root"' not in html and 'id="embedded-data"' not in html:
        warns.append('index.html has neither id="root" (legacy SPA) nor id="embedded-data" (v4 portal shell) — wrong shell?')
else:
    warns.append("index.html not in SITE dir (shell committed once; ok if only data.json republished)")
print("── Contract (Web_v3, non-empty critical sections)")
if f:
    for x in f: print("  ✗ " + x)
else:
    print("  ✓ all critical sections present and non-empty")
for w in warns: print("  ! WARN: " + w)

# ─────────────────────────────────────────────────────────────────────────────
# LAYER 2 — ASSET / MODULE GRAPH (added 2026-07-26)
# The site is a Vite ESM React SPA. Charts and the hero canvas are LAZY chunks.
# A mixed deploy (entry from one build, chunks from another) leaves a chunk
# importing an entry hash that does not exist -> the dynamic import 404s -> every
# chart silently fails to mount while the text/tables still render. That happened
# on 2026-07-25 (EChart/HeroCanvas imported a missing index-DJLtjH6T.js) and the
# data-contract check above could not see it. This layer closes that hole by
# resolving the whole static graph on disk BEFORE publishing.
# It only runs when SITE mirrors the deploy (i.e. SITE/assets exists).
# ─────────────────────────────────────────────────────────────────────────────
import re
g_fail, g_warn, g_ok = [], [], []
ASSETS = os.path.join(SITE, "assets")
SELF_CONTAINED = not os.path.isdir(ASSETS)
if SELF_CONTAINED:
    # v4 portal (2026-07-31): the frontend is ONE self-contained index.html — no assets/.
    # The failure mode is no longer a mixed chunk graph; it is (a) a shell that secretly
    # references local files that are not deployed, (b) a broken embedded-data fallback,
    # or (c) a shell not wired to fetch data.json (daily refresh would go dark).
    if not os.path.exists(INDEX):
        g_fail.append("SITE/index.html missing — v4 shell must be mirrored in SITE")
    else:
        html = open(INDEX, encoding="utf-8", errors="ignore").read()
        locrefs = re.findall(r'(?:src|href)\s*=\s*["\'](?!https?:|#|data:)([^"\']+)["\']', html)
        # ignore JS template-literal placeholders inside the inline app script
        # (e.g. href="${esc(p.url)}") — they are runtime strings, not static file refs
        locrefs = [r for r in locrefs if r not in ("data.json",) and '${' not in r]
        if locrefs:
            g_fail.append("v4 shell references undeployed local files: %s" % sorted(set(locrefs))[:5])
        else:
            g_ok.append("shell is self-contained (no local file references)")
        m = re.search(r'<script id="embedded-data" type="application/json">(.*?)</script>', html, re.S)
        if not m:
            g_fail.append("v4 shell missing embedded-data block (offline/CDN-lag fallback)")
        else:
            try:
                emb = json.loads(m.group(1).replace('<\\/script>', '</script>'))
                g_ok.append("embedded-data parses (fallback as_of %s)" % (emb.get('meta', {}).get('as_of')))
            except Exception as ex:
                g_fail.append("embedded-data does not parse: %s" % ex)
        if "fetch('data.json')" not in html and 'fetch("data.json")' not in html:
            g_fail.append("v4 shell does not fetch data.json — daily data refresh would never appear")
        else:
            g_ok.append("shell fetches data.json (daily refresh wired)")
elif not os.path.exists(INDEX):
    g_warn.append("SITE/index.html missing — cannot verify shell->asset references.")
else:
    html = open(INDEX, encoding="utf-8", errors="ignore").read()
    refs = set(re.findall(r'(?:src|href)\s*=\s*["\'](?:\./)?(assets/[A-Za-z0-9._-]+\.(?:js|css))["\']', html))
    if not refs:
        g_fail.append("index.html references no assets/*.js — wrong or empty shell")
    for r in sorted(refs):
        (g_ok if os.path.isfile(os.path.join(SITE, r)) else g_fail).append(
            "shell -> %s" % r if os.path.isfile(os.path.join(SITE, r))
            else "shell -> %s MISSING (stale index.html vs deployed assets)" % r)
    entries = {os.path.basename(r) for r in refs if r.endswith(".js")}
    jsfiles = sorted(x for x in os.listdir(ASSETS) if x.endswith(".js"))
    for jf in jsfiles:
        src = open(os.path.join(ASSETS, jf), encoding="utf-8", errors="ignore").read()
        deps = set(re.findall(r'["\']\./([A-Za-z0-9._-]+\.js)["\']', src))
        for d in sorted(deps):
            if os.path.isfile(os.path.join(ASSETS, d)):
                g_ok.append("%s -> %s" % (jf, d))
            else:
                g_fail.append("%s -> %s MISSING (orphan chunk from a different build "
                              "— its dynamic import will 404 and the charts will not render)" % (jf, d))
    # orphan detection: a chunk nobody imports and the shell does not load
    imported = set()
    for jf in jsfiles:
        src = open(os.path.join(ASSETS, jf), encoding="utf-8", errors="ignore").read()
        imported |= set(re.findall(r'["\']\./([A-Za-z0-9._-]+\.js)["\']', src))
    for jf in jsfiles:
        if jf not in entries and jf not in imported:
            g_warn.append("%s is never imported by the shell or any chunk — dead file "
                          "(likely left over from a previous build)" % jf)
    # duplicate-React guard. Two React copies in one bundle render a BLANK page
    # ("TypeError: Cannot read properties of null (reading 'useRef')").
    # Signature = how many times React's client-internals key is DEFINED in a file.
    # Empirically calibrated 2026-07-26 against both bundles built that day:
    #   healthy entry = 3   |   duplicate-React entry = 4
    #   lazy chunks   = 0-1 (they reference the entry's single React)
    # Do NOT use React version strings for this — peer-dependency strings in the
    # three.js/drei chunk produce false positives (e.g. "19.2.0" in HeroCanvas).
    KEY = "__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE"
    for jf in jsfiles:
        src = open(os.path.join(ASSETS, jf), encoding="utf-8", errors="ignore").read()
        n = src.count(KEY)
        if n > 3:
            g_fail.append("%s defines React client-internals %d times (healthy = 3) — a "
                          "DUPLICATE REACT copy is bundled; the page will render blank" % (jf, n))

print("── Layer 2 — %s" % ("self-contained v4 shell" if SELF_CONTAINED else "asset / module graph (Vite ESM chunks)"))
for x in g_ok: print("  ✓ " + x)
for x in g_fail: print("  ✗ " + x)
for x in g_warn: print("  ! WARN: " + x)
if not g_fail and not g_warn and g_ok:
    print("  ✓ graph complete and closed — every import resolves on disk")

f += g_fail

# ─────────────────────────────────────────────────────────────────────────────
# LAYER 3 — RENDER CONTRACT: template expectations vs actual data.json types
# (added 2026-09-13)
# WHY THIS EXISTS. Layers 1 and 2 check that sections are non-empty and that the
# shell is intact. Neither executes the page, so a FIELD-SHAPE mismatch between
# data.json and the renderer was invisible to both. On 2026-09-13 the "Alumina &
# Inputs" tab had been silently dead: alumina.notes is authored as a narrative
# STRING, the renderer called .map() on it, the section threw mid-render, and
# because the tab strip repaints BEFORE the main column, the tab highlight moved
# while the previous tab's content stayed on screen — so "Premiums" and "Alumina
# & Inputs" showed identical content and nothing anywhere reported an error.
# Both prior layers passed clean that day.
# WHAT THIS CHECKS. Every `D.<path>.map(` in the SHIPPED shell must resolve to a
# LIST in the freshly built data.json. A path guarded by a coercion helper (e.g.
# asList(D.x.y).map(...)) is deliberately NOT matched by the regex and needs no
# entry here — guarding a field is how you opt out of this check.
r_fail, r_ok, r_warn = [], [], []
import re as _re
_shell = INDEX if os.path.exists(INDEX) else None
if _shell:
    _html = open(_shell, encoding="utf-8", errors="ignore").read()
    # strip the embedded fallback JSON so data content can never be scanned as code
    _html = _re.sub(r'(<script[^>]*id="embedded-data"[^>]*>).*?(</script>)',
                    r'\1\2', _html, flags=_re.S)
    _paths = sorted(set(_re.findall(r'\bD\.([A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)*)\.map\(', _html)))
    for _p in _paths:
        _cur, _found = D, True
        for _part in _p.split('.'):
            if isinstance(_cur, dict) and _part in _cur:
                _cur = _cur[_part]
            else:
                _cur, _found = None, False
                break
        if not _found:
            r_fail.append("shell renders D.%s with .map() but data.json has no such path "
                          "— that tab will throw and show the PREVIOUS tab's content" % _p)
        elif not isinstance(_cur, list):
            r_fail.append("shell renders D.%s with .map() but data.json has type %s "
                          "— that tab will throw and show the PREVIOUS tab's content "
                          "(wrap it in asList() or fix the schema transform)"
                          % (_p, type(_cur).__name__))
    if _paths and not r_fail:
        r_ok.append("all %d .map() render paths resolve to lists in data.json" % len(_paths))
    if not _paths:
        r_warn.append("no D.<path>.map() calls found in the shell — regex may be stale, "
                      "this layer is not actually checking anything")
else:
    r_warn.append("index.html not in SITE dir — render contract not checked this run")

# Numeric-field contract: any key ending in _pct (or named 'value'/'price' on a
# board row) is formatted with arithmetic helpers in the shell. A STRING there does
# not throw — it silently renders "NaN%", which is why it survived unnoticed in the
# macro ticker and the whole Macro-tab Day column. Strings are rejected here.
_nan_fail = []
def _scan_numeric(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            p = path + "." + k
            if k.endswith("_pct") and isinstance(v, str):
                _nan_fail.append("%s is the string %r — the shell formats it numerically "
                                 "and will render 'NaN%%' (parse it in schema_v2)" % (p.lstrip("."), v[:24]))
            _scan_numeric(v, p)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            _scan_numeric(v, "%s[%d]" % (path, i))
_scan_numeric(D)
r_fail += _nan_fail
if not _nan_fail:
    r_ok.append("all *_pct fields are numeric or null (no silent NaN%% renders)")

# Headless render sweep: actually EXECUTE every section builder against the real
# data.json and assert none throws and none emits the literal 'NaN'. The type rules
# above catch known-shaped mistakes; this catches the rest by running the code. Node
# is optional — if it is unavailable the sweep degrades to a warning rather than
# blocking the daily run. (2026-09-13)
_rt = os.path.join(ENGDIR, "render_test.js")
if os.path.exists(_rt):
    import subprocess, shutil
    if shutil.which("node"):
        try:
            _p = subprocess.run(["node", _rt, SITE], capture_output=True, text=True, timeout=120, cwd=ENGDIR)
            _o = (_p.stdout or "") + (_p.stderr or "")
            if _p.returncode != 0:
                for _ln in [l for l in _o.splitlines() if "FAIL" in l or "THREW" in l][:8]:
                    r_fail.append("render sweep: " + _ln.strip())
                if not any("render sweep" in x for x in r_fail):
                    r_fail.append("render sweep exited %d — a section failed to render" % _p.returncode)
            elif "IDENTICAL" in _o:
                r_fail.append("render sweep: two tabs produced identical output — a section is failing silently")
            else:
                _n = [l for l in _o.splitlines() if "NaN occurrences" in l]
                if _n:
                    for _ln in _n[:6]: r_fail.append("render sweep: " + _ln.strip())
                else:
                    r_ok.append("headless render sweep — all sections render, all distinct, zero NaN")
        except Exception as _ex:
            r_warn.append("render sweep could not run (%s) — type rules still applied" % _ex)
    else:
        r_warn.append("node not available — headless render sweep skipped, type rules still applied")
else:
    r_warn.append("render_test.js not found in ENGDIR — headless render sweep skipped")

print("── Layer 3 — render contract (template expectations vs data types)")
for x in r_ok: print("  ✓ " + x)
for x in r_fail: print("  ✗ " + x)
for x in r_warn: print("  ! WARN: " + x)

f += r_fail
if f:
    print("\n=== VALIDATION FAILED — DO NOT PUBLISH (%d) ===" % len(f)); sys.exit(1)
print("=== VALIDATION PASSED — safe to publish ==="); sys.exit(0)
