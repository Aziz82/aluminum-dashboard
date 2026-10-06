#!/usr/bin/env node
/* render_test.js — headless render sweep for the Web_v4 portal shell.
 * Usage: node render_test.js <site_dir>        (defaults to ../Aluminum_Dashboard_Site)
 *
 * WHY THIS EXISTS. validate_dashboard.py Layers 1 and 2 never execute the page, so a
 * field-shape mismatch between data.json and the renderer was invisible to both. On
 * 2026-09-13 "Alumina & Inputs" had been silently dead for weeks: alumina.notes is a
 * narrative STRING, the renderer called .map() on it, the section threw mid-render,
 * and because the tab strip repaints BEFORE the main column, the tab highlight moved
 * while the PREVIOUS tab's content stayed on screen. Premiums and Alumina & Inputs
 * showed identical content and nothing reported an error.
 *
 * WHAT IT DOES. Extracts the application script from the SHIPPED index.html, runs it
 * against the real data.json under a minimal DOM shim (the SECTIONS builders are pure
 * string functions), then asserts:
 *   1. every section renders without throwing
 *   2. every section renders DISTINCT output (identical output = silent failure)
 *   3. no section emits the literal "NaN" (a string where a number was expected)
 * Exit 0 = clean. Non-zero = do not publish.
 */
const fs = require('fs'), path = require('path'), crypto = require('crypto');

const SITE = process.argv[2] || path.join(__dirname, '..', 'Aluminum_Dashboard_Site');
const INDEX = path.join(SITE, 'index.html');
const DATAP = path.join(SITE, 'data.json');
for (const p of [INDEX, DATAP]) {
  if (!fs.existsSync(p)) { console.log('FATAL: missing ' + p); process.exit(2); }
}
const DATA = JSON.parse(fs.readFileSync(DATAP, 'utf8'));

/* pull the application script (the largest non-JSON <script>) out of the shipped shell */
const html = fs.readFileSync(INDEX, 'utf8');
const scripts = [...html.matchAll(/<script(?![^>]*application\/json)[^>]*>([\s\S]*?)<\/script>/g)].map(m => m[1]);
if (!scripts.length) { console.log('FATAL: no application script found in index.html'); process.exit(2); }
const app = scripts.reduce((a, b) => (b.length > a.length ? b : a));

/* minimal DOM shim — SECTIONS are pure string builders, everything else is stubbed */
const el = () => ({
  set innerHTML(v) {}, get innerHTML() { return ''; }, style: {},
  classList: { add() {}, remove() {}, toggle() {} }, dataset: {},
  addEventListener() {}, appendChild() {}, querySelectorAll: () => [],
  getContext: () => null, set onclick(v) {}, textContent: JSON.stringify(DATA),
  getBoundingClientRect: () => ({ width: 900, height: 400 })
});
global.document = {
  getElementById: () => el(), querySelector: () => el(), querySelectorAll: () => [],
  createElement: () => el(), body: el(), addEventListener() {},
  documentElement: { style: {}, classList: { add() {}, remove() {}, toggle() {} }, setAttribute() {} }
};
global.window = {
  addEventListener() {}, matchMedia: () => ({ matches: false, addEventListener() {} }),
  scrollTo() {}, devicePixelRatio: 1, localStorage: { getItem: () => null, setItem() {} }
};
global.localStorage = global.window.localStorage;
global.fetch = () => Promise.reject(new Error('offline render test'));
global.requestAnimationFrame = () => {};
global.setTimeout = () => 0;

try { (0, eval)(app + '\n;globalThis.__S = SECTIONS;'); }
catch (e) { /* boot code may touch the DOM; SECTIONS is what matters */ }

const S = globalThis.__S;
if (!S || !S.length) { console.log('FATAL: SECTIONS not exposed — shell structure changed?'); process.exit(2); }

const NAMES = ['Overview', 'Markets', 'Premiums', 'Alumina & Inputs', 'Macro', 'Outlook', 'Earning', 'Sources'];
const res = S.map((fn, i) => {
  const name = NAMES[i] || ('section ' + i);
  try {
    const h = fn();
    return { i, name, ok: true, len: h.length, nan: (h.match(/NaN/g) || []).length,
             hash: crypto.createHash('md5').update(h).digest('hex').slice(0, 10) };
  } catch (e) { return { i, name, ok: false, err: e.message }; }
});

console.log('=== SECTION RENDER SWEEP ===');
for (const r of res) {
  console.log(r.ok
    ? `  OK   [${r.i}] ${r.name.padEnd(18)} ${String(r.len).padStart(7)} bytes  md5:${r.hash}${r.nan ? '  <<< ' + r.nan + ' NaN' : ''}`
    : `  FAIL [${r.i}] ${r.name.padEnd(18)} THREW: ${r.err}`);
}

const failed = res.filter(r => !r.ok);
const rendered = res.filter(r => r.ok);
const hashes = rendered.map(r => r.hash);
const dupes = hashes.filter((h, i) => hashes.indexOf(h) !== i);
const nanTotal = rendered.reduce((a, r) => a + r.nan, 0);

for (const r of rendered) if (r.nan) console.log(`  ${r.name}: ${r.nan} NaN occurrences`);
if (dupes.length) {
  const names = rendered.filter(r => dupes.includes(r.hash)).map(r => r.name).join(' == ');
  console.log(`  IDENTICAL output across tabs: ${names} — a section is failing silently`);
}
console.log(`  distinct: ${new Set(hashes).size}/${rendered.length} · threw: ${failed.length} · NaN: ${nanTotal}`);
if (!failed.length && !dupes.length && !nanTotal) console.log('  ✓ all sections render, all distinct, zero NaN');
process.exit(failed.length || dupes.length || nanTotal ? 1 : 0);
