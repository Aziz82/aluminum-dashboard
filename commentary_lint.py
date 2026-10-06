#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
commentary_lint.py — enforce the Aluminium Commentary Standard on market_data.json.

Mirrors the Upstream Cockpit build-check pattern: mechanical, non-negotiable,
reported line by line.

Usage:
    python3 commentary_lint.py <ENGDIR> [--strict]

    ENGDIR   directory holding market_data.json and the *.preedit.bak.json archive
    --strict exit non-zero on any FAIL (hard gate). Default is warn-only.

Run AFTER build_data_json.py and BEFORE validate_dashboard.py.
"""
import json, os, re, sys, glob, io

# ---------------------------------------------------------------- word budgets
BUDGET = {
    'so_what.line':                 45,
    'so_what.points[]':             60,
    'kpi_cards[].delta':            40,
    'benchmark[].note':             90,
    'metals_detail[].src':          70,
    'lme_commentary':              200,
    'net_read':                    120,
    'bottom_line':                 120,
    'outlook.ai_analysis[]':        70,
    'news[].headline':              60,
    'feed[].text':                  45,
    'premiums[].src':               80,
    'inputs[].src':                 80,
    'alumina[].src':                80,
    'raw_materials[].src':          80,
    'outlook.risks[].risk':         90,
    'outlook.catalysts[].event':    90,
    'producer_status[].update':     90,
    'premium_drivers[].d':          90,
    'earnings_note':               160,
    'caveats[]':                    60,
    'commercial[]':                100,
    'inputs_summary[]':            100,
    'alumina_notes[]':             100,
    'call.items[].text':           110,
    'ew.long_term.writeup':        180,
    'ew.short_term.writeup':       180,
}
COUNT_CAP = {           # max number of entries
    'so_what.points':   4,
    'outlook.ai_analysis': 6,
    'caveats':         12,
    'call.items':       3,
}
PAGE_WORD_CAP = 9000

# ---------------------------------------------------------------- thresholds
MAX_CAPS_SHARE       = 0.05
MAX_META_SHARE       = 0.05
MAX_DUP_WORD_SHARE   = 0.01
MAX_CARRIED_SHARE    = 0.25
MIN_NUM_DENSITY      = 13.0     # numbers per 100 words

# ---------------------------------------------------------------- patterns
META = re.compile(
    r'\b(this page|this row|this run|this board|this card|this panel|this table|this series'
    r'|re-verified|verified this morning|republished|is flagged|flagged rather'
    r'|carried (?:at|unchanged|forward|here)|basis (?:check|discipline|consist)'
    r'|not (?:published|written|appended|invented|interpolated|spliced) here'
    r'|gaps? stay gaps?|deliberately not|rather than (?:a guess|an omission|hidden|papered)'
    r'|correction is made|corrects itself|stated (?:here|as such)|no newer'
    r'|could not be (?:verified|sourced|retrieved|opened)|subscription-only|paywall'
    r'|convention on this page|is the point|worth stating plainly)', re.I)

NUM = re.compile(r'(?<![\w/])(?:\$|RMB |EUR |€|£)?\d[\d,]*(?:\.\d+)?%?')
URL = re.compile(r'https?://\S+')

# house style, inherited from the cockpit — build-checked, non-negotiable
HOUSE = [
    (re.compile(r"Ma[’']aden", re.I),          "apostrophe spelling of Maaden"),
    (re.compile(r'\bhot metal\b', re.I),            "'hot metal' (use 'Smelter (Potline)')"),
    (re.compile(r'\bCock\b(?!pit)'),                "'Cock' where 'Coke' is meant"),
    (re.compile(r'confidence interval', re.I),      "'confidence interval' (the band is a spread, not a CI)"),
    (re.compile(r'\bI am pleased to report\b', re.I), "'I am pleased to report'"),
    (re.compile(r'…'),                          "ellipsis character (never pre-truncate)"),
]

# ---------------------------------------------------------------- helpers
def sentences(t):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9$])', t) if len(x.strip()) > 40]

def norm(s):
    s = re.sub(r'[\d,\.\$%]+', '#', s.lower())
    s = re.sub(r'[^a-z# ]', ' ', s)
    return ' '.join(s.split())

def all_strings(o, path='', out=None):
    """yield (dotted_path, string) for every commentary string"""
    if out is None:
        out = []
    if isinstance(o, str):
        if len(o) > 60:
            out.append((path, o))
    elif isinstance(o, dict):
        for k, v in o.items():
            all_strings(v, (path + '.' + k).lstrip('.'), out)
    elif isinstance(o, list):
        for v in o:
            all_strings(v, path + '[]', out)
    return out

def budget_key(path):
    """map a dotted path to a BUDGET key, tolerating index markers"""
    if path in BUDGET:
        return path
    # normalise e.g. 'kpi_cards[].delta'
    for k in BUDGET:
        if path == k:
            return k
    return None

# ---------------------------------------------------------------- main
def main():
    eng = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    strict = '--strict' in sys.argv
    p = os.path.join(eng, 'market_data.json')
    d = json.load(io.open(p, encoding='utf-8'))
    rd = d.get('report_date', '?')

    fails, warns = [], []
    def FAIL(m): fails.append(m)
    def WARN(m): warns.append(m)

    strings = all_strings(d)
    blob = ' '.join(s for _, s in strings)
    blob_nourl = URL.sub(' ', blob)
    total_words = len(blob_nourl.split())

    print("== commentary_lint — %s ==" % rd)
    print()

    # ---- 1. page total
    print("-- page size")
    verdict = 'OK' if total_words <= PAGE_WORD_CAP else 'FAIL'
    print("   %-38s %7d   cap %d   %s" % ('total prose words', total_words, PAGE_WORD_CAP, verdict))
    print("   %-38s %7.0f min" % ('reading time @230wpm', total_words / 230.0))
    if total_words > PAGE_WORD_CAP:
        FAIL("page is %d words over the %d cap" % (total_words - PAGE_WORD_CAP, PAGE_WORD_CAP))

    # ---- 2. per-field budgets
    print()
    print("-- word budgets (worst offenders)")
    breaches = []
    for path, s in strings:
        k = budget_key(path)
        if not k:
            continue
        n = len(s.split())
        if n > BUDGET[k]:
            breaches.append((n - BUDGET[k], n, BUDGET[k], k, s[:60]))
    breaches.sort(reverse=True)
    if not breaches:
        print("   all fields within budget")
    for over, n, cap, k, snip in breaches[:15]:
        print("   %-30s %4dw  cap %3d  (+%d)  %s..." % (k[:30], n, cap, over, snip[:44]))
    if breaches:
        FAIL("%d field(s) over word budget; worst is %s at %dw against a %dw cap"
             % (len(breaches), breaches[0][3], breaches[0][1], breaches[0][2]))

    # ---- 3. entry-count caps
    print()
    print("-- entry counts")
    for key, cap in COUNT_CAP.items():
        node = d
        try:
            for part in key.split('.'):
                node = node[part]
            n = len(node)
        except Exception:
            print("   %-30s  absent" % key)
            continue
        v = 'OK' if n <= cap else 'FAIL'
        print("   %-30s %4d   cap %d   %s" % (key, n, cap, v))
        if n > cap:
            FAIL("%s has %d entries against a cap of %d" % (key, n, cap))

    # ---- 4. prose quality metrics
    print()
    print("-- prose metrics")
    ss = []
    for _, t in strings:
        ss += sentences(t)
    nsent = max(len(ss), 1)

    meta_n = sum(1 for s in ss if META.search(s))
    meta_share = meta_n / nsent
    print("   %-38s %6.1f%%  cap %.0f%%  %s" % ('process/meta sentences', 100 * meta_share,
          100 * MAX_META_SHARE, 'OK' if meta_share <= MAX_META_SHARE else 'FAIL'))
    if meta_share > MAX_META_SHARE:
        FAIL("process/meta sentences at %.1f%% against a %.0f%% cap (%d sentences)"
             % (100 * meta_share, 100 * MAX_META_SHARE, meta_n))

    words = re.findall(r'\b[A-Za-z]{3,}\b', blob_nourl)
    caps_share = sum(1 for w in words if w.isupper()) / max(len(words), 1)
    print("   %-38s %6.1f%%  cap %.0f%%  %s" % ('ALL-CAPS words', 100 * caps_share,
          100 * MAX_CAPS_SHARE, 'OK' if caps_share <= MAX_CAPS_SHARE else 'FAIL'))
    if caps_share > MAX_CAPS_SHARE:
        FAIL("ALL-CAPS at %.1f%% against a %.0f%% cap" % (100 * caps_share, 100 * MAX_CAPS_SHARE))

    density = 100.0 * len(NUM.findall(blob_nourl)) / max(total_words, 1)
    print("   %-38s %6.1f   min %.0f    %s" % ('numbers per 100 words', density,
          MIN_NUM_DENSITY, 'OK' if density >= MIN_NUM_DENSITY else 'FAIL'))
    if density < MIN_NUM_DENSITY:
        FAIL("information density %.1f per 100 words, below the %.0f minimum" % (density, MIN_NUM_DENSITY))

    # ---- 5. within-file duplication
    print()
    print("-- duplication")
    from collections import Counter
    c = Counter(norm(s) for s in ss)
    dup_words = sum((v - 1) * len(k.split()) for k, v in c.items() if v > 1)
    dup_share = dup_words / max(sum(len(norm(s).split()) for s in ss), 1)
    print("   %-38s %6.1f%%  cap %.0f%%  %s" % ('duplicate words within this file',
          100 * dup_share, 100 * MAX_DUP_WORD_SHARE, 'OK' if dup_share <= MAX_DUP_WORD_SHARE else 'FAIL'))
    worst = [(v, k) for k, v in c.items() if v > 1]
    worst.sort(reverse=True)
    for v, k in worst[:5]:
        print("      %2dx  %s..." % (v, k[:66]))
    if dup_share > MAX_DUP_WORD_SHARE:
        FAIL("%.1f%% of words are sentences repeated inside this one file" % (100 * dup_share))

    # ---- 6. day-over-day carry
    baks = sorted(glob.glob(os.path.join(eng, 'market_data.2026-*.preedit.bak.json')))
    baks = [f for f in baks if not re.search(r'run2|run3|preedit2|eve|myrun|peerpatch|phantom|refresh', f)]
    if baks:
        prev = json.load(io.open(baks[-1], encoding='utf-8'))
        pss = set()
        for _, t in all_strings(prev):
            pss |= set(norm(x) for x in sentences(t))
        cur = set(norm(s) for s in ss)
        carried = len(cur & pss) / max(len(cur), 1)
        print("   %-38s %6.1f%%  cap %.0f%%  %s" % ('carried verbatim from prior run',
              100 * carried, 100 * MAX_CARRIED_SHARE, 'OK' if carried <= MAX_CARRIED_SHARE else 'FAIL'))
        if carried > MAX_CARRIED_SHARE:
            FAIL("%.1f%% of sentences are verbatim from the previous run" % (100 * carried))

    # ---- 7. house style
    print()
    print("-- house style (cockpit rules, non-negotiable)")
    hs_clean = True
    for rx, label in HOUSE:
        hits = rx.findall(blob)
        if hits:
            hs_clean = False
            print("   FAIL  %-52s %d occurrence(s)" % (label, len(hits)))
            FAIL("house style: %s appears %d time(s)" % (label, len(hits)))
    if hs_clean:
        print("   all house-style checks clean")

    # ---- 8. CALL / CALL_REVIEW
    print()
    print("-- accountability loop")
    call = d.get('call')
    review = d.get('call_review')
    if not call or not (call.get('items') if isinstance(call, dict) else None):
        print("   FAIL  no CALL issued this run")
        FAIL("no CALL issued — the page states no falsifiable forward view")
    else:
        items = call['items']
        print("   OK    %d call(s) issued" % len(items))
        for i, it in enumerate(items):
            miss = [k for k in ('series', 'expected', 'horizon') if not it.get(k)]
            if miss:
                print("   FAIL  call %d missing %s" % (i + 1, ', '.join(miss)))
                FAIL("call %d is not machine-scoreable (missing %s)" % (i + 1, ', '.join(miss)))
            if 'Expect' not in (it.get('text') or ''):
                print("   FAIL  call %d has no 'Expect ...' sentence" % (i + 1))
                FAIL("call %d has no 'Expect ...' sentence" % (i + 1))
    if review is None:
        print("   FAIL  no CALL_REVIEW block")
        FAIL("no CALL_REVIEW — prior calls were never scored")
    else:
        ok = {'CORRECT', 'WRONG', 'INDETERMINATE'}
        bad = [r for r in review if r.get('outcome') not in ok]
        print("   OK    %d prior call(s) reviewed" % len(review))
        if bad:
            print("   FAIL  %d review(s) with an outcome outside CORRECT/WRONG/INDETERMINATE" % len(bad))
            FAIL("%d call review(s) carry an invalid outcome" % len(bad))
        for r in review:
            if not r.get('note'):
                FAIL("a call review carries no note justifying its verdict")
        if review:
            hits = sum(1 for r in review if r.get('outcome') == 'CORRECT')
            scored = sum(1 for r in review if r.get('outcome') in ('CORRECT', 'WRONG'))
            if scored:
                print("   info  running hit rate this run: %d/%d = %.0f%%"
                      % (hits, scored, 100.0 * hits / scored))

    # ---- summary
    print()
    print("=" * 62)
    if fails:
        print("COMMENTARY LINT: %d FAIL" % len(fails))
        for f in fails:
            print("  - %s" % f)
    else:
        print("COMMENTARY LINT: PASSED")
    for w in warns:
        print("  warn: %s" % w)
    print("=" * 62)

    if fails and strict:
        return 1
    if fails:
        print("(warn-only mode — pass --strict to make this a hard gate)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
