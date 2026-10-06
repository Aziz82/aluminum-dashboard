// Aluminum Weekly Market Brief — Word engine.
// Reads weekly_data.json (same folder), writes a dated .docx to argv[2] (or same folder).
const fs = require("fs");
const path = require("path");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        Header, Footer, AlignmentType, LevelFormat, BorderStyle, WidthType,
        ShadingType, PageNumber } = require("docx");

const HERE = __dirname;
const D = JSON.parse(fs.readFileSync(path.join(HERE, "weekly_data.json"), "utf8"));
const OUTDIR = process.argv[2] || HERE;

const NAVY = "14213D", GOLD = "8E7C42", GREY = "5A5A5A", GREEN = "1E7D34", RED = "C0392B", LGOLD = "EFE9D8", BAND = "F7F4EC";
const CW = 9360; // content width DXA (US Letter, 1in margins)

const toneColor = t => t === "up" ? GREEN : (t === "down" ? RED : GREY);

function h2(text) {
  return new Paragraph({
    spacing: { before: 240, after: 100 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: GOLD, space: 2 } },
    children: [new TextRun({ text, bold: true, font: "Arial", size: 24, color: NAVY })],
  });
}
function body(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 120 }, alignment: AlignmentType.JUSTIFIED,
    children: [new TextRun({ text, font: "Arial", size: 21, color: opts.color || "000000", italics: !!opts.italics, bold: !!opts.bold })],
  });
}
function bullet(runs) {
  return new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 80 }, children: runs });
}
function tcell(text, { w, head = false, tone = null, alignRight = false, bold = false } = {}) {
  const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    borders: { top: border, bottom: border, left: border, right: border },
    shading: { fill: head ? NAVY : "FFFFFF", type: ShadingType.CLEAR },
    margins: { top: 60, bottom: 60, left: 110, right: 110 },
    children: [new Paragraph({
      alignment: alignRight ? AlignmentType.RIGHT : AlignmentType.LEFT,
      children: [new TextRun({ text, font: "Arial", size: 19, bold: head || bold,
        color: head ? "FFFFFF" : (tone ? toneColor(tone) : "000000") })],
    })],
  });
}

const cols = [2600, 1450, 1450, 1100, 2760]; // sums 9360
const priceRows = [
  new TableRow({ tableHeader: true, children: [
    tcell("Metric", { w: cols[0], head: true }), tcell("Week open", { w: cols[1], head: true, alignRight: true }),
    tcell("Latest", { w: cols[2], head: true, alignRight: true }), tcell("Δ WoW", { w: cols[3], head: true, alignRight: true }),
    tcell("Note", { w: cols[4], head: true }),
  ]}),
  ...D.price_table.map((r, i) => new TableRow({ children: [
    tcell(r.metric, { w: cols[0], bold: true }),
    tcell(r.wopen, { w: cols[1], alignRight: true }),
    tcell(r.wclose, { w: cols[2], alignRight: true }),
    tcell(r.chg, { w: cols[3], alignRight: true, tone: r.tone }),
    tcell(r.note, { w: cols[4] }),
  ]})),
];

const children = [];
// Title block
children.push(new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: "ALUMINUM — WEEKLY MARKET BRIEF", bold: true, font: "Arial", size: 34, color: NAVY })] }));
children.push(new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: "Commercial Market Intelligence  |  Primary Aluminum • Alumina • Premiums • Logistics", font: "Arial", size: 18, color: GOLD })] }));
children.push(new Paragraph({
  spacing: { after: 200 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: NAVY, space: 2 } },
  children: [new TextRun({ text: D.week_label + "   |   Classification: Restricted", bold: true, font: "Arial", size: 19, color: GREY })],
}));

children.push(h2("Executive Summary"));
D.exec_summary.forEach(p => children.push(body(p)));

children.push(h2("Price Action — Week in Review"));
children.push(new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: cols, rows: priceRows }));
children.push(new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: "USD/MT unless noted. Δ WoW = change vs prior-week close (LME official); intraweek extremes noted.", font: "Arial", size: 16, italics: true, color: GREY })] }));

children.push(h2("Key Drivers This Week"));
D.drivers.forEach(d => children.push(bullet([new TextRun({ text: d, font: "Arial", size: 21 })])));

children.push(h2("Commercial Implications — Aluminum Business"));
D.implications.forEach(it => children.push(bullet([
  new TextRun({ text: it.lead + ": ", bold: true, font: "Arial", size: 21, color: NAVY }),
  new TextRun({ text: it.text, font: "Arial", size: 21 }),
])));

children.push(h2("Outlook — Week Ahead / Watch Items"));
D.outlook.forEach(o => children.push(bullet([new TextRun({ text: o, font: "Arial", size: 21 })])));

children.push(h2("Sources & Data Quality"));
children.push(body(D.sources, { color: GREY }));
children.push(new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: D.caveat, font: "Arial", size: 16, italics: true, color: GREY })] }));

const doc = new Document({
  creator: "Aluminum Commercial Market Intelligence",
  title: "Aluminum Weekly Market Brief",
  numbering: { config: [ { reference: "bullets", levels: [
    { level: 0, format: LevelFormat.BULLET, text: "▸", alignment: AlignmentType.LEFT,
      style: { run: { color: GOLD }, paragraph: { indent: { left: 460, hanging: 260 } } } } ] } ] },
  styles: { default: { document: { run: { font: "Arial", size: 21 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, right: 1440, bottom: 1080, left: 1440 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
      children: [new TextRun({ text: "Classification: Restricted", font: "Arial", size: 15, color: GREY })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [ new TextRun({ text: "Aluminum Weekly Market Brief — " + D.week_label + "   |   Page ", font: "Arial", size: 15, color: GREY }),
        new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 15, color: GREY }),
        new TextRun({ text: " of ", font: "Arial", size: 15, color: GREY }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 15, color: GREY }) ] })] }) },
    children,
  }],
});

const iso = D.week_ending;
const out = path.join(OUTDIR, `Aluminum_Weekly_Brief_${iso}.docx`);
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(out, buf); console.log("saved", out); });
