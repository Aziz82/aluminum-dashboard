/* validate_dashboard.js — headless render gate for the Aluminum dashboard.
 *
 * Executes the REAL index.html against the REAL data.json in jsdom and fails
 * if the dashboard cannot render. This is the authoritative check: it catches
 * ANY data-shape break generically, because it runs the actual renderer rather
 * than a hand-maintained schema.
 *
 * Why it exists: index.html wraps render() inside the fetch promise chain, so a
 * single .catch() swallows BOTH network errors and rendering exceptions and
 * always prints "Couldn't load data.json". A rendering bug is therefore
 * invisible from the served file alone — data.json can be perfectly valid JSON,
 * serve a 200, and still produce a blank dashboard.
 *
 * Usage: node validate_dashboard.js <index.html> <data.json>
 * Exit 0 = renders clean. Exit 1 = DO NOT PUBLISH.
 */
const fs = require("fs");
const path = require("path");

const [, , IDX, DATA] = process.argv;
if (!IDX || !DATA) { console.error("usage: node validate_dashboard.js <index.html> <data.json>"); process.exit(2); }

let JSDOM;
try { ({ JSDOM } = require("jsdom")); }
catch (e) { console.error("FATAL: jsdom not installed. Run: npm install --prefix /tmp jsdom"); process.exit(2); }

const html = fs.readFileSync(IDX, "utf8");
const raw = fs.readFileSync(DATA, "utf8");

let parsed;
try { parsed = JSON.parse(raw); }
catch (e) { console.error("FAIL: data.json is not valid JSON — " + e.message); process.exit(1); }

const errors = [];

// Surface the exception that index.html's .catch() would otherwise swallow.
const instrumented = html.replace(
  '.catch(()=>{document.getElementById("main").innerHTML=',
  '.catch((__e)=>{__RENDER_ERROR__(__e);document.getElementById("main").innerHTML='
);
if (instrumented === html) {
  console.warn("WARN: could not instrument the .catch() — relying on DOM inspection only.");
}

const dom = new JSDOM(instrumented, {
  runScripts: "dangerously",
  pretendToBeVisual: true,
  beforeParse(w) {
    // Serve the local data.json to the page's fetch().
    w.fetch = () => Promise.resolve({ ok: true, json: () => Promise.resolve(JSON.parse(raw)) });
    w.__RENDER_ERROR__ = (e) => errors.push("RENDER EXCEPTION: " + ((e && (e.stack || e.message)) || String(e)));
    w.addEventListener("error", (ev) => errors.push("UNCAUGHT: " + ev.message));
    // Chart.js is loaded from CDN and is absent offline; stub it so its absence
    // is not mistaken for a data fault.
    w.Chart = function () { return { destroy() {}, update() {} }; };
    w.Chart.register = () => {};
  },
});

setTimeout(() => {
  const doc = dom.window.document;
  const main = doc.getElementById("main");
  const txt = (doc.body && doc.body.textContent) || "";

  // The real failure signal: the .load error card injected into #main.
  // (Do NOT string-match the body — the literal "Couldn't load data.json"
  //  also appears in the inline <script> source, which lives inside <body>.)
  if (main && main.querySelector(".load")) {
    errors.push('ERROR CARD RENDERED: #main contains the "Couldn\'t load data.json" fallback.');
  }
  if (!main || main.innerHTML.trim().length < 500) {
    errors.push("EMPTY RENDER: #main is missing or essentially empty.");
  }

  // Content sentinels — proves the sections that broke today actually populated.
  const D = parsed, O = (parsed.outlook || {});
  const sentinels = [
    ["report date in header", () => new RegExp(String(D.report_date.slice(0, 4))).test(txt)],
    ["so_what headline", () => D.so_what && D.so_what.line && txt.includes(D.so_what.line.slice(0, 40))],
    ["benchmark row", () => D.benchmark && D.benchmark[0] && txt.includes(D.benchmark[0].name)],
    ["sources table", () => D.sources && D.sources[0] && txt.includes(String(D.sources[0][0]).slice(0, 25))],
    ["outlook ai_analysis", () => O.ai_analysis && O.ai_analysis[0] && txt.includes(String(O.ai_analysis[0]).slice(0, 40))],
    ["outlook risks", () => O.risks && O.risks[0] && txt.includes(String(O.risks[0].risk).slice(0, 25))],
    ["outlook catalysts", () => O.catalysts && O.catalysts[0] && txt.includes(String(O.catalysts[0].event).slice(0, 25))],
    ["news", () => D.news && D.news[0] && txt.includes(String(D.news[0].headline).slice(0, 30))],
    ["premiums", () => D.premiums && D.premiums[0] && txt.includes(String(D.premiums[0].name).slice(0, 12))],
    ["elliott wave writeup", () => D.ew && D.ew.long_term && txt.includes(String(D.ew.long_term.writeup).slice(0, 40))],
  ];
  const failed = [];
  for (const [name, fn] of sentinels) {
    let ok = false;
    try { ok = !!fn(); } catch (e) { ok = false; }
    if (!ok) failed.push(name);
  }
  if (failed.length) errors.push("SECTION DID NOT RENDER: " + failed.join(", "));

  if (errors.length) {
    console.error("\n=== DASHBOARD VALIDATION FAILED — DO NOT PUBLISH ===");
    errors.forEach((e) => console.error("  ✗ " + e));
    console.error("");
    process.exit(1);
  }
  console.log("  ✓ renders clean (no exceptions, all " + sentinels.length + " sections populated)");
  process.exit(0);
}, 3000);
