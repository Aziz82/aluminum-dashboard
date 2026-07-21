#!/usr/bin/env python3
"""AI-driven daily refresh of market_data.json — PATCH PROTOCOL (cloud / GitHub Actions).

WHY A PATCH, NOT A REWRITE
--------------------------
The previous version asked the model to return the ENTIRE market_data.json. That file
is now ~77 KB (~22k tokens) — larger than any sane max_tokens output budget — so every
run truncated and was rejected. Input context is cheap and large; OUTPUT is the scarce
resource. So: we send the full current dataset as context, and require the model to
return ONLY the top-level keys it wants to change.

This also makes the schema contract structurally safe. The model can never reshape a
container it did not touch, and every container it DOES touch is shape-checked against
the previous run before it is merged.

FAIL-SAFE
---------
Any parse failure, shape violation, unknown key, or staleness violation leaves
market_data.json completely untouched and exits non-zero, so the workflow stops and
the previously published dashboard stays live. Silence is never treated as success.

Env:
  ANTHROPIC_API_KEY      required
  CLAUDE_MODEL           default 'claude-sonnet-4-5'
  WEB_SEARCH_MAX_USES    default 20
  EXPECT_DATE            default today (UTC)
Usage: python refresh_ai.py [engine_dir]
"""
import json, os, re, sys, datetime, copy

ENG = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(ENG, "market_data.json")
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-5")
MAX_USES = int(os.environ.get("WEB_SEARCH_MAX_USES", "20"))
TODAY = os.environ.get("EXPECT_DATE") or datetime.datetime.utcnow().strftime("%Y-%m-%d")

# Keys the model is allowed to patch. Anything else is rejected outright.
PATCHABLE = {
    "report_date", "so_what", "kpi_cards", "benchmark", "premiums", "macro",
    "macro_events", "lme_series", "lme_commentary", "alumina", "alumina_notes",
    "alumina_outlook", "raw_materials", "inputs", "inputs_summary", "logistics",
    "net_read", "feed", "news", "earnings", "earnings_note", "commercial",
    "bottom_line", "sources", "caveats", "outlook", "ew", "metals_board",
    "metals_history", "premium_history", "premium_outlook", "premium_quarters",
    "premium_tariff", "premium_drivers", "premium_settlement_src",
}
# Must change every run or the refresh is not a refresh.
MUST_CHANGE = ["report_date"]


# ── shape guard ─────────────────────────────────────────────────────────────
def _keyunion(rows):
    u, i = set(), None
    for r in rows:
        if isinstance(r, dict):
            u |= set(r)
            i = set(r) if i is None else (i & set(r))
    return u, (i or set())


def check_shape(new, old, path="", errs=None):
    """Recursively assert `new` has the same container shape as `old`."""
    errs = errs if errs is not None else []

    if isinstance(old, dict):
        if not isinstance(new, dict):
            errs.append(f"{path}: expected object, got {type(new).__name__}")
            return errs
        missing, extra = set(old) - set(new), set(new) - set(old)
        if missing:
            errs.append(f"{path}: missing keys {sorted(missing)}")
        if extra:
            errs.append(f"{path}: unexpected keys {sorted(extra)}")
        for k in set(old) & set(new):
            check_shape(new[k], old[k], f"{path}.{k}" if path else k, errs)
        return errs

    if isinstance(old, list):
        if not isinstance(new, list):
            errs.append(f"{path}: expected list, got {type(new).__name__}")
            return errs
        if old and not new:
            errs.append(f"{path}: list emptied (renderer would show a blank section)")
            return errs
        if not old:
            return errs
        proto = old[0]
        if isinstance(proto, dict):
            union, inter = _keyunion(old)
            for n, row in enumerate(new):
                if not isinstance(row, dict):
                    errs.append(f"{path}[{n}]: expected object, got {type(row).__name__}")
                    continue
                bad = set(row) - union
                lack = inter - set(row)
                if bad:
                    errs.append(f"{path}[{n}]: unexpected keys {sorted(bad)}")
                if lack:
                    errs.append(f"{path}[{n}]: missing required keys {sorted(lack)}")
        elif isinstance(proto, list):
            ln = len(proto)
            for n, row in enumerate(new):
                if not isinstance(row, list):
                    errs.append(f"{path}[{n}]: expected pair-array, got {type(row).__name__}")
                elif ln == 2 and len(row) != 2:
                    errs.append(f"{path}[{n}]: expected 2 elements, got {len(row)}")
        else:
            for n, row in enumerate(new):
                if isinstance(row, (dict, list)):
                    errs.append(f"{path}[{n}]: expected scalar, got {type(row).__name__}")
        return errs

    # scalars — allow numeric widening and nullable fields, block container swaps
    if isinstance(new, (dict, list)):
        errs.append(f"{path}: expected scalar, got {type(new).__name__}")
    return errs


# ── explicit contract assertions (the shapes index.html hard-depends on) ────
def contract_assertions(d):
    e = []
    O = d.get("outlook", {})
    ai = O.get("ai_analysis")
    if not isinstance(ai, list) or not all(isinstance(x, str) for x in ai):
        e.append("outlook.ai_analysis must be a LIST of strings (a bare string blanks the page)")
    for key, src in (("sources", d.get("sources")), ("outlook.sources", O.get("sources"))):
        if not isinstance(src, list) or not all(
                isinstance(s, list) and len(s) == 2 for s in src):
            e.append(f"{key} must be a list of 2-element [label, url] pairs")
    for r in O.get("risks", []) or []:
        if set(r) != {"risk", "likelihood", "impact", "trend"}:
            e.append(f"outlook.risks row keys wrong: {sorted(r)}")
            break
        if r["trend"] not in ("up", "down", "flat"):
            e.append(f"outlook.risks trend must be up|down|flat, got {r['trend']!r}")
            break
    for c in O.get("catalysts", []) or []:
        if set(c) != {"date", "event", "impact"}:
            e.append(f"outlook.catalysts row keys wrong: {sorted(c)}")
            break
    for b in d.get("benchmark", []) or []:
        if "int" in b:
            e.append("benchmark rows must NOT carry an 'int' key (it drops the decimal place)")
            break
    ps = d.get("premium_settlement_src")
    if not (isinstance(ps, list) and len(ps) == 2 and all(isinstance(x, str) for x in ps)):
        e.append("premium_settlement_src must be a flat [label, url] pair")
    for pd_ in d.get("premium_drivers", []) or []:
        s = pd_.get("src")
        if not (isinstance(s, list) and len(s) == 2):
            e.append("premium_drivers[].src must be a [label, url] pair")
            break
    for panel in ("long_term", "short_term"):
        P = (d.get("ew") or {}).get(panel, {})
        for a in P.get("annos", []) or []:
            if "now" in str(a.get("text", "")).lower():
                e.append(f"ew.{panel}.annos must not author a 'now' annotation (engine injects it)")
                break
    return e


# ── freshness guard ─────────────────────────────────────────────────────────
def freshness(new, old):
    """Catch the silent-stale-reuse failure mode."""
    e = []
    if new.get("report_date") != TODAY:
        e.append(f"report_date is {new.get('report_date')!r}, expected {TODAY!r}")
    bench_same = json.dumps(
        [(r.get("name"), r.get("cur")) for r in new.get("benchmark", [])], sort_keys=True
    ) == json.dumps(
        [(r.get("name"), r.get("cur")) for r in old.get("benchmark", [])], sort_keys=True
    )
    if bench_same:
        # Permitted ONLY if the model explicitly explains the non-move in the caveats,
        # e.g. the exchange had not yet published the latest official at refresh time.
        blob = " ".join(new.get("caveats", [])).lower()
        if not any(k in blob for k in ("not yet publish", "latest published", "no session",
                                       "publication-timing", "had not posted")):
            e.append("benchmark values identical to the previous run with no explanatory "
                     "caveat — refusing to republish a stale tape")
    return e


def extract_json(text):
    t = text.strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", t, re.S)
    if m:
        t = m.group(1).strip()
    i, j = t.find("{"), t.rfind("}")
    if i == -1 or j == -1 or j <= i:
        raise ValueError("no JSON object found in model output")
    return json.loads(t[i:j + 1])


SYSTEM = f"""You are a commercial market-intelligence analyst covering the PRIMARY ALUMINIUM and ALUMINA markets. You refresh a daily public market dashboard.

PUBLIC-ONLY MANDATE (absolute):
- Publish ONLY public information. Never anything confidential, internal or company-specific: no realised prices, net-backs, shipping lanes, volumes, costs or internal commentary.
- Never frame the content as any specific company's tool or position. No "our", "we", or house view. This is generic situational awareness, not advice.
- The ONLY company-specific content permitted is public listed-company information in the peer-earnings table.
- EVERY figure must trace to a public source. If a number cannot be publicly sourced, DO NOT publish it — leave the previous value and explain why in `caveats`.

DATA RULES:
- Today is {TODAY}. Set report_date to exactly {TODAY}.
- LME cash/3M/stock officials come from Westmetall. This job runs BEFORE the London ring (officials print 13:20 London), so the latest PUBLISHED official is normally the PRIOR session's. NEVER invent an intraday "official". If Westmetall has not yet posted the latest session, say so plainly in `caveats` and keep the prior official — that is a publication-timing fact, not stale reuse.
- Never duplicate a figure to fill a gap. When a value moves, put the new figure in `cur` and shift the old `cur` into `prev` so day-over-day deltas are real.
- SPREAD CONVENTION: cash > 3M (positive cash-3M) = BACKWARDATION; cash < 3M = CONTANGO.
- Premiums are all $/t. US premiums are tariff-inflated — keep the real high values.
- metals_board order: Aluminium, Copper, Nickel, Zinc, Lead.

ELLIOTT WAVE: act as an EW analyst. Provide CONFIRMED historical pivots only (waves[] ending at the last confirmed swing) plus forward projections. Do NOT author a "now" price point or any annotation containing the word "now" — the build engine injects the real current price. Validate impulses against the three cardinal rules. Keep counts consistent day to day; re-label only on a stated invalidation break. Technical context, NOT advice. Set ew.updated to {TODAY}.

OUTPUT PROTOCOL — READ CAREFULLY:
Return a JSON PATCH: an object containing ONLY the top-level keys you are changing. Do NOT return the whole dataset. Do NOT invent new top-level keys.
For any key you include, return the COMPLETE new value for that key with EXACTLY the same structure as the current one — same nesting, same field names, same container types.
Shapes that must never change:
  - outlook.ai_analysis = LIST of strings (never a single string)
  - sources and outlook.sources = lists of 2-element [label, url] pairs
  - outlook.risks rows = {{risk, likelihood, impact, trend}} with trend in up|down|flat
  - outlook.catalysts rows = {{date, event, impact}}
  - premium_settlement_src = a flat [label, url] pair
  - benchmark rows = {{name, cur, prev, avg, note}} — never add an "int" key
Always include at minimum: report_date, so_what, benchmark, kpi_cards, metals_board, lme_commentary, net_read, bottom_line, feed, news, caveats, sources, outlook, ew.
Return ONLY the JSON object. No prose, no markdown, no code fence."""


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        return 2
    try:
        import anthropic
    except ImportError:
        print("ERROR: anthropic SDK not installed", file=sys.stderr)
        return 2

    old = json.load(open(MD_PATH, encoding="utf-8"))

    user = (
        "Below is the CURRENT dataset (yesterday's published state) as JSON context.\n"
        "Research today's market with web search, then return a JSON PATCH containing only "
        "the top-level keys you are changing, per the output protocol.\n\n"
        "Research checklist: LME Al cash/3M/stock (Westmetall) and whether the latest "
        "session's official has actually been published yet; base metals board (Cu, Ni, Zn, "
        "Pb); regional premiums (MJP, CIF Japan, EDU Rotterdam, US Midwest duty-paid, "
        "billets); alumina and raw materials; smelter input basket and logistics; macro/FX/"
        "energy; Strait of Hormuz status; last-48h headlines; peer earnings; and the outlook "
        "and Elliott Wave read.\n\n"
        "=== CURRENT DATASET ===\n" + json.dumps(old, ensure_ascii=False)
    )

    client = anthropic.Anthropic()
    tools = [{"type": "web_search_20250305", "name": "web_search", "max_uses": MAX_USES}]
    messages = [{"role": "user", "content": user}]

    searches, resp = 0, None
    for _ in range(12):  # pause_turn safety loop
        resp = client.messages.create(
            model=MODEL, max_tokens=16000, system=SYSTEM, messages=messages, tools=tools,
        )
        try:
            searches = resp.usage.server_tool_use.web_search_requests or searches
        except Exception:
            pass
        if resp.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": resp.content})
            continue
        break

    if resp is None:
        print("ERROR: no response from model", file=sys.stderr)
        return 1
    if resp.stop_reason == "max_tokens":
        print("ERROR: model hit max_tokens — patch would be truncated; rejecting", file=sys.stderr)
        return 1

    text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    if not text.strip():
        print("ERROR: model returned no text content", file=sys.stderr)
        return 1

    # ── parse ───────────────────────────────────────────────────────────────
    try:
        patch = extract_json(text)
    except Exception as ex:
        print(f"ERROR: patch did not parse ({ex}) — data left untouched", file=sys.stderr)
        return 1

    if not isinstance(patch, dict) or not patch:
        print("ERROR: patch is empty or not an object — data left untouched", file=sys.stderr)
        return 1

    unknown = set(patch) - PATCHABLE
    if unknown:
        print(f"ERROR: patch contains non-patchable keys {sorted(unknown)}", file=sys.stderr)
        return 1

    # ── shape-check every patched container against the previous run ────────
    errs = []
    for k, v in patch.items():
        if k not in old:
            errs.append(f"{k}: key does not exist in the current dataset")
            continue
        check_shape(v, old[k], k, errs)
    if errs:
        print("ERROR: patch REJECTED on shape violations — data left untouched:", file=sys.stderr)
        for e in errs[:25]:
            print("  ✗ " + e, file=sys.stderr)
        return 1

    # ── merge into a candidate, then assert the full contract ───────────────
    cand = copy.deepcopy(old)
    cand.update(patch)
    cand["report_date"] = TODAY

    errs = contract_assertions(cand) + freshness(cand, old)
    if errs:
        print("ERROR: patch REJECTED on contract/freshness — data left untouched:", file=sys.stderr)
        for e in errs[:25]:
            print("  ✗ " + e, file=sys.stderr)
        return 1

    for k in MUST_CHANGE:
        if json.dumps(cand.get(k), sort_keys=True) == json.dumps(old.get(k), sort_keys=True):
            print(f"ERROR: '{k}' did not change — refusing to republish", file=sys.stderr)
            return 1

    json.dump(cand, open(MD_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"OK: market_data.json patched for {TODAY} "
          f"({len(patch)} keys: {', '.join(sorted(patch))}; web searches: {searches})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
