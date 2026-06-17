#!/usr/bin/env python3
"""AI-driven daily refresh of market_data.json (cloud / GitHub Actions).

Calls the Anthropic API with the web_search server tool. Claude searches trusted
public sources, then returns an updated market_data.json that keeps the exact
schema of the current file. Fail-safe: if the model output does not parse or is
missing required keys, the existing market_data.json is left untouched and the
script exits non-zero so the run is visibly failed (no silent data corruption).

Env:
  ANTHROPIC_API_KEY      required
  CLAUDE_MODEL           default 'claude-sonnet-4-6'
  WEB_SEARCH_MAX_USES    default 18
Usage: python refresh_ai.py [engine_dir]
"""
import json, os, re, sys, datetime

ENG = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(ENG, "market_data.json")
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-6")
MAX_USES = int(os.environ.get("WEB_SEARCH_MAX_USES", "18"))
TODAY = datetime.datetime.utcnow().strftime("%Y-%m-%d")

# ---- required structure (fail-safe validation) -----------------------------
REQUIRED_KEYS = [
    "report_date", "kpi_cards", "benchmark", "premiums", "macro", "lme_series",
    "alumina", "net_read", "news", "earnings", "sources", "caveats", "outlook",
    "premium_history", "raw_materials", "inputs", "logistics",
]
NONEMPTY_LISTS = ["benchmark", "premiums", "macro", "news", "earnings", "inputs"]


def extract_json(text):
    """Pull the JSON object out of the model's final text."""
    t = text.strip()
    # strip ```json ... ``` fences if present
    m = re.search(r"```(?:json)?\s*(.*?)```", t, re.S)
    if m:
        t = m.group(1).strip()
    # take from first { to last }
    i, j = t.find("{"), t.rfind("}")
    if i == -1 or j == -1 or j <= i:
        raise ValueError("no JSON object found in model output")
    return json.loads(t[i:j + 1])


def validate(new, old):
    missing = [k for k in REQUIRED_KEYS if k not in new]
    if missing:
        raise ValueError(f"missing required keys: {missing}")
    for k in NONEMPTY_LISTS:
        if not isinstance(new.get(k), list) or len(new[k]) == 0:
            raise ValueError(f"key '{k}' must be a non-empty list")
    # guard against catastrophic shrinkage (model dropped most of the file)
    if len(json.dumps(new)) < 0.5 * len(json.dumps(old)):
        raise ValueError("output is <50% the size of the source; rejecting")
    return True


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        return 2
    try:
        import anthropic
    except ImportError:
        print("ERROR: anthropic SDK not installed (pip install anthropic)", file=sys.stderr)
        return 2

    old = json.load(open(MD_PATH, encoding="utf-8"))

    system = (
        "You are a senior commercial market-intelligence analyst covering the primary "
        "aluminium and alumina markets for Maaden (Saudi Arabian Mining Company). "
        "Your job is to refresh a daily market dataset using ONLY current, real figures "
        "from trusted public sources via web search. Trusted sources include: LME / "
        "Westmetall (official settlements), Trading Economics, Reuters, S&P Global / "
        "Platts public notes, Fastmarkets/Argus public commentary, SHFE, the World Bank "
        "pink sheet, and company investor-relations releases for earnings. "
        "Rules:\n"
        "- Search for the LATEST available values (LME cash & 3M, inventory, SHFE, "
        "alumina, regional premiums MJP/CIF/EDU/US Midwest, FX/DXY, Brent, US 10Y, "
        "freight/Hormuz status, peer earnings, headlines).\n"
        "- Keep premium and price units in USD per tonne ($/t).\n"
        "- Daily premium prints (Platts/Fastmarkets/Argus) are subscription feeds: use the "
        "most recent PUBLIC anchor and keep the existing 'verify PRA feed' style caveats.\n"
        "- When a value moves, set the new figure as 'cur' and shift the old 'cur' into "
        "'prev' so day-over-day deltas are real, not duplicated.\n"
        "- Preserve the EXACT JSON schema you are given: same keys, same nesting, same field "
        "names. Do not add or remove top-level keys.\n"
        f"- Set 'report_date' to {TODAY}.\n"
        "- Return ONLY the JSON object. No prose, no markdown, no code fence."
    )
    user = (
        "Here is the current dataset. Update every figure to the latest available market "
        "data, keeping the identical structure, then return ONLY the updated JSON object.\n\n"
        + json.dumps(old, ensure_ascii=False)
    )

    client = anthropic.Anthropic()
    tools = [{"type": "web_search_20250305", "name": "web_search", "max_uses": MAX_USES}]
    messages = [{"role": "user", "content": user}]

    searches = 0
    for _ in range(10):  # pause_turn safety loop
        resp = client.messages.create(
            model=MODEL, max_tokens=16000, system=system, messages=messages, tools=tools,
        )
        try:
            searches = resp.usage.server_tool_use.web_search_requests or searches
        except Exception:
            pass
        if resp.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": resp.content})
            continue
        break

    text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    if not text.strip():
        print("ERROR: model returned no text content", file=sys.stderr)
        return 1

    try:
        new = extract_json(text)
        validate(new, old)
    except Exception as e:
        print(f"ERROR: refresh rejected, keeping existing data ({e})", file=sys.stderr)
        return 1

    new["report_date"] = TODAY
    json.dump(new, open(MD_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"OK: market_data.json refreshed for {TODAY} (web searches: {searches})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
