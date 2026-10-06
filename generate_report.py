#!/usr/bin/env python3
"""Aluminum Daily Market Report — formatting engine.
Reads market_data.json (same folder) and writes a dated .xlsx.
Layout/format is FIXED here; only market_data.json changes day-to-day.
Usage: python3 generate_report.py [output_dir]
"""
import json, os, sys, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.worksheet.properties import PageSetupProperties
from openpyxl.worksheet.page import PageMargins
from openpyxl.chart import LineChart, Reference

HERE=os.path.dirname(os.path.abspath(__file__))
D=json.load(open(os.path.join(HERE,"market_data.json"),encoding="utf-8"))
REPORT_DATE=datetime.date.fromisoformat(D["report_date"])
DATESTR=REPORT_DATE.strftime("%d %B %Y"); ISO=REPORT_DATE.strftime("%Y-%m-%d")
OUTDIR=sys.argv[1] if len(sys.argv)>1 else HERE

NAVY="14213D"; GOLD="8E7C42"; LGOLD="EFE9D8"; BAND="F7F4EC"
GREY="5A5A5A"; LGREY="F2F2F2"; GREEN="1E7D34"; RED="C0392B"; WHITE="FFFFFF"; BORDER_C="D9D9D9"
FNAME="Arial"
thin=Side(style="thin",color=BORDER_C); box=Border(left=thin,right=thin,top=thin,bottom=thin)
gold_l=Side(style="medium",color=GOLD)
def Fn(sz=10,b=False,color="000000",italic=False): return Font(name=FNAME,size=sz,bold=b,color=color,italic=italic)
def fill(c): return PatternFill("solid",fgColor=c)
center=Alignment(horizontal="center",vertical="center",wrap_text=True)
left=Alignment(horizontal="left",vertical="center",wrap_text=True)
lefttop=Alignment(horizontal="left",vertical="top",wrap_text=True)
arr={"up":("▲",GREEN),"down":("▼",RED),"flat":("▬",GREY)}
ARROW='=IF({c}>{p},"▲",IF({c}<{p},"▼","▬"))'
wb=Workbook()

def title_block(ws,title,sub,span=8):
    ws.merge_cells(start_row=1,start_column=1,end_row=1,end_column=span)
    c=ws.cell(1,1,title); c.font=Fn(16,True,WHITE); c.fill=fill(NAVY); c.alignment=Alignment(horizontal="left",vertical="center",indent=1); ws.row_dimensions[1].height=32
    ws.merge_cells(start_row=2,start_column=1,end_row=2,end_column=span)
    c=ws.cell(2,1,sub); c.font=Fn(9,False,WHITE); c.fill=fill(GOLD); c.alignment=Alignment(horizontal="left",vertical="center",indent=1); ws.row_dimensions[2].height=18
def sect(ws,row,text,span=8):
    ws.merge_cells(start_row=row,start_column=1,end_row=row,end_column=span)
    c=ws.cell(row,1,text); c.font=Fn(11,True,NAVY); c.fill=fill(LGOLD); c.alignment=Alignment(horizontal="left",vertical="center",indent=1); c.border=Border(left=gold_l); ws.row_dimensions[row].height=21
def hdr(ws,row,cols,start=1):
    for i,h in enumerate(cols):
        c=ws.cell(row,start+i,h); c.font=Fn(10,True,WHITE); c.fill=fill(NAVY); c.alignment=center; c.border=box
    ws.row_dimensions[row].height=20
def band(ws,row,c1,c2,idx):
    if idx%2==1:
        for col in range(c1,c2+1):
            if ws.cell(row,col).fill.fgColor.rgb in (None,"00000000"): ws.cell(row,col).fill=fill(BAND)
def cf_posneg(ws,rng):
    ws.conditional_formatting.add(rng,CellIsRule(operator='greaterThan',formula=['0'],font=Fn(10,True,GREEN)))
    ws.conditional_formatting.add(rng,CellIsRule(operator='lessThan',formula=['0'],font=Fn(10,True,RED)))
def cf_arrow(ws,rng,delta_cell):
    ws.conditional_formatting.add(rng,FormulaRule(formula=[f'{delta_cell}>0'],font=Fn(12,True,GREEN)))
    ws.conditional_formatting.add(rng,FormulaRule(formula=[f'{delta_cell}<0'],font=Fn(12,True,RED)))
def setup_page(ws):
    ws.page_setup.orientation='landscape'; ws.sheet_properties.pageSetUpPr=PageSetupProperties(fitToPage=True)
    ws.page_setup.fitToWidth=1; ws.page_setup.fitToHeight=0
    ws.page_margins=PageMargins(left=0.3,right=0.3,top=0.45,bottom=0.45,header=0.2,footer=0.2)
    ws.print_options.horizontalCentered=True
    ws.oddFooter.center.text="Aluminum Daily Market Report — "+DATESTR+"  |  Classification: Restricted  |  Page &P of &N"
    ws.oddFooter.center.size=8; ws.oddFooter.center.font="Arial"
def icol(t): return GREEN if "ull" in t else (RED if "ear" in t else GREY)
def tbl(ws,r,headers,rows):
    hdr(ws,r,headers,2); r+=1; n=len(headers)
    for i,row in enumerate(rows):
        for j in range(n):
            v=row[j] if j<len(row) else ""
            c=ws.cell(r,2+j,v); c.border=box; c.font=Fn(9)
            c.alignment=(lefttop if j==n-1 else (Alignment(horizontal="right") if isinstance(v,(int,float)) else Alignment(horizontal="left",vertical="center",wrap_text=True)))
            if i%2==1 and c.fill.fgColor.rgb in (None,"00000000"): c.fill=fill(BAND)
        ws.row_dimensions[r].height=26; r+=1
    return r
def bullets(ws,r,items,span=6):
    for s in items:
        ws.cell(r,2,"▸").font=Fn(10,True,GOLD); ws.cell(r,2).alignment=Alignment(horizontal="center",vertical="top")
        ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=span)
        ws.cell(r,3,s).font=Fn(10); ws.cell(r,3).alignment=lefttop; ws.row_dimensions[r].height=30; r+=1
    return r

# ---------- Cover ----------
ws=wb.active; ws.title="Cover"; ws.sheet_view.showGridLines=False
for col,w in {"A":3,"B":26,"C":62,"D":18}.items(): ws.column_dimensions[col].width=w
ws.merge_cells("B2:D2"); c=ws.cell(2,2,"ALUMINUM — DAILY MARKET REPORT"); c.font=Fn(20,True,NAVY)
ws.merge_cells("B3:D3"); c=ws.cell(3,2,"Commercial Market Intelligence | Primary Aluminum • Alumina • Premiums • Logistics"); c.font=Fn(10,False,GOLD)
ws.merge_cells("B4:D4"); c=ws.cell(4,2,"Reporting date: "+REPORT_DATE.strftime("%A, %d %B %Y")); c.font=Fn(10,True,GREY)
ws.cell(6,2,"Classification:").font=Fn(10,True); ws.cell(6,3,"Restricted — Internal Commercial Use").font=Fn(10)
meta=[("Prepared for","Aluminum Business — Commercial / Marketing / Market Intelligence"),
      ("Coverage","Primary Aluminum, Marketing, Alumina Sales, Outbound Logistics, Customer Support, Market Intelligence"),
      ("Data as of","LME official settlements through latest confirmed close; latest benchmark read "+DATESTR),
      ("Primary sources","LME (via Westmetall), Trading Economics, Fastmarkets, S&P Global Platts, Argus, AlCircle, GAC China"),
      ("Currency / units","USD per metric tonne unless stated; premiums per tonne or US c/lb as noted"),
      ("Output","Excel (.xlsx), dated; auto-generated daily at 08:00")]
r=8
for k,v in meta:
    ws.cell(r,2,k).font=Fn(10,True,NAVY); ws.cell(r,2).alignment=lefttop
    ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=4)
    ws.cell(r,3,v).font=Fn(10); ws.cell(r,3).alignment=lefttop; ws.row_dimensions[r].height=30; r+=1
sect(ws,r+1,"Workbook contents",3); r+=2
toc=[("Dashboard","Headline KPIs, prices, premiums, macro, sentiment & 48-hour feed"),
     ("LME Prices & Inventory","Daily cash / 3M settlements, stock, spread, stats & trend chart"),
     ("Premiums","Regional physical premiums with trend direction"),
     ("Alumina & Raw Materials","Alumina indices, bauxite & input commentary"),
     ("Macro & FX","USD, FX, energy, rates & base-metals — with daily moves"),
     ("Market News & Sentiment","Headlines tagged by theme, impact & source"),
     ("Peer Earnings","Recent earnings-call results — aluminum & mining peers"),
     ("Commercial Implications","SME read-through for the Aluminum Business"),
     ("Sources & Data Quality","Citations, caveats & refresh guidance")]
for name,desc in toc:
    ws.cell(r,2,name).font=Fn(10,True,GOLD); ws.cell(r,2).alignment=left
    ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=4)
    ws.cell(r,3,desc).font=Fn(10); ws.cell(r,3).alignment=left; r+=1
c=ws.cell(r+1,2,"Legend:  ▲ green = positive move   ▼ red = negative move   ▬ unchanged.   Daily premium prints (Platts/Fastmarkets/Argus) are subscription feeds — figures shown are most recent public anchors; reconcile to the desk's licensed feed before pricing.")
c.font=Fn(8,False,GREY); ws.merge_cells(start_row=r+1,start_column=2,end_row=r+2,end_column=4); ws.cell(r+1,2).alignment=lefttop

# ---------- Dashboard ----------
ws=wb.create_sheet("Dashboard"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":30,"C":14,"D":14,"E":12,"F":8,"G":40}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"ALUMINUM MARKET DASHBOARD — "+DATESTR,"Headline KPIs • prices • premiums • macro • sentiment | Classification: Restricted",7)
r=4
cstart=[2,4,6]
for card,cs in zip(D["kpi_cards"],cstart):
    ce=cs+1
    for rr in (r,r+1,r+2): ws.merge_cells(start_row=rr,start_column=cs,end_row=rr,end_column=ce)
    a=ws.cell(r,cs,card["label"]); a.font=Fn(9,True,WHITE); a.fill=fill(NAVY); a.alignment=center
    b=ws.cell(r+1,cs,card["value"]); b.font=Fn(20,True,NAVY); b.fill=fill(BAND); b.alignment=center
    dd=ws.cell(r+2,cs,card["delta"]); dd.font=Fn(10,True,GREEN if card["pos"] else RED); dd.fill=fill(BAND); dd.alignment=center
    for rr in (r,r+1,r+2):
        for cc in range(cs,ce+1): ws.cell(rr,cc).border=box
ws.row_dimensions[r].height=16; ws.row_dimensions[r+1].height=30; ws.row_dimensions[r+2].height=16
r+=4
sect(ws,r,"MARKET PRICES (USD/MT unless noted)",7); r+=1
hdr(ws,r,["Indicator","Current","Previous","Δ %","Trend","Note"],2); r+=1
cf_first=r
for i,b in enumerate(D["benchmark"]):
    ws.cell(r,2,b["name"]).font=Fn(10,True); ws.cell(r,2).alignment=left; ws.cell(r,2).border=box
    cc=ws.cell(r,3,b["cur"]); cc.font=Fn(10); cc.alignment=Alignment(horizontal="right"); cc.border=box
    cp=ws.cell(r,4,b["prev"]); cp.font=Fn(10); cp.alignment=Alignment(horizontal="right"); cp.border=box
    fmt='#,##0' if b.get("int") else '#,##0.0'; cc.number_format=fmt; cp.number_format=fmt
    d=ws.cell(r,5,f"=IF(D{r}=0,0,(C{r}-D{r})/D{r})"); d.number_format='0.0%;-0.0%;0.0%'; d.font=Fn(10); d.alignment=Alignment(horizontal="right"); d.border=box
    t=ws.cell(r,6,ARROW.format(c=f"C{r}",p=f"D{r}")); t.alignment=center; t.font=Fn(12,True); t.border=box
    _bn=(("Avg last-mo "+format(b["avg"],",.1f")+" · ") if b.get("avg") is not None else "")+b["note"]
    ws.cell(r,7,_bn).font=Fn(9,False,GREY); ws.cell(r,7).alignment=left; ws.cell(r,7).border=box
    band(ws,r,2,7,i); r+=1
cf_posneg(ws,f"E{cf_first}:E{r-1}"); cf_arrow(ws,f"F{cf_first}:F{r-1}",f"E{cf_first}")
r+=1; sect(ws,r,"REGIONAL PHYSICAL PREMIUMS",7); r+=1
hdr(ws,r,["Premium ($/t)","Current","Previous","Δ %","Trend","Source / note"],2); r+=1
pf=r
for i,p in enumerate(D["premiums"]):
    ws.cell(r,2,p["name"]).font=Fn(10,True); ws.cell(r,2).alignment=left; ws.cell(r,2).border=box
    cc=ws.cell(r,3,p["cur"]); cc.number_format='#,##0.0'; cc.font=Fn(10); cc.alignment=Alignment(horizontal="right"); cc.border=box
    cp=ws.cell(r,4,p["prev"]); cp.number_format='#,##0.0'; cp.font=Fn(10); cp.alignment=Alignment(horizontal="right"); cp.border=box
    dd=ws.cell(r,5,f"=IF(D{r}=0,0,(C{r}-D{r})/D{r})"); dd.number_format='0.0%;-0.0%;0.0%'; dd.font=Fn(10); dd.alignment=Alignment(horizontal="right"); dd.border=box
    tt=ws.cell(r,6,ARROW.format(c=f"C{r}",p=f"D{r}")); tt.font=Fn(12,True); tt.alignment=center; tt.border=box
    _ps=(("Avg last-mo "+format(p["avg"],",.1f")+" · ") if p.get("avg") is not None else "")+p["src"]
    ws.cell(r,7,_ps).font=Fn(9,False,GREY); ws.cell(r,7).alignment=left; ws.cell(r,7).border=box
    band(ws,r,2,7,i); r+=1
cf_posneg(ws,f"E{pf}:E{r-1}"); cf_arrow(ws,f"F{pf}:F{r-1}",f"E{pf}")
r+=1; sect(ws,r,"MACRO & CROSS-ASSET (Trading Economics, "+DATESTR+")",7); r+=1
hdr(ws,r,["Indicator","Value","Day %","Tr","Indicator / note"],2); r+=1
mfirst=r
for i,m in enumerate(D["macro"]):
    ws.cell(r,2,m["name"]).font=Fn(10,True); ws.cell(r,2).alignment=left; ws.cell(r,2).border=box
    ws.cell(r,3,m["value"]).font=Fn(10); ws.cell(r,3).alignment=Alignment(horizontal="right"); ws.cell(r,3).border=box
    d=ws.cell(r,4,m["day"]/100); d.number_format='0.00%;-0.00%;0.00%'; d.font=Fn(10); d.alignment=Alignment(horizontal="right"); d.border=box
    t=ws.cell(r,5,f'=IF(D{r}>0,"▲",IF(D{r}<0,"▼","▬"))'); t.font=Fn(12,True); t.alignment=center; t.border=box
    ws.cell(r,6,m["note"]).font=Fn(9,False,GREY); ws.cell(r,6).alignment=left; ws.cell(r,6).border=box
    ws.merge_cells(start_row=r,start_column=6,end_row=r,end_column=7); band(ws,r,2,7,i); r+=1
cf_posneg(ws,f"D{mfirst}:D{r-1}"); cf_arrow(ws,f"E{mfirst}:E{r-1}",f"D{mfirst}")
r+=1; sect(ws,r,"NET MARKET READ",7); r+=1
ws.merge_cells(start_row=r,start_column=2,end_row=r+3,end_column=7)
cc=ws.cell(r,2,D["net_read"]); cc.font=Fn(10); cc.alignment=lefttop; cc.fill=fill(LGREY)
for rr in range(r,r+4):
    for col in range(2,8): ws.cell(rr,col).border=box
r+=4
r+=1; sect(ws,r,"MARKET FEED — LAST 48 HOURS (rolling, newest first)",7); r+=1
ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=6)
for col,t in [(2,"When"),(3,"Update"),(7,"Impact")]:
    c=ws.cell(r,col,t); c.font=Fn(10,True,WHITE); c.fill=fill(NAVY); c.alignment=center; c.border=box
for col in (4,5,6): ws.cell(r,col).fill=fill(NAVY); ws.cell(r,col).border=box
ws.row_dimensions[r].height=20; r+=1
for i,f in enumerate(D["feed"]):
    ws.cell(r,2,f["when"]).font=Fn(9,True,NAVY); ws.cell(r,2).alignment=center; ws.cell(r,2).border=box
    ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=6)
    tc=ws.cell(r,3,f["text"]); tc.font=Fn(9); tc.alignment=lefttop; tc.border=box
    for col in range(4,7): ws.cell(r,col).border=box
    ic=ws.cell(r,7,f["impact"]); ic.font=Fn(9,True,icol(f["impact"])); ic.alignment=center; ic.border=box
    band(ws,r,2,7,i); ws.row_dimensions[r].height=32; r+=1
ws.cell(r,2,"Feed compiled "+ISO+" from Trading Economics, LME/Westmetall, ING, LSEG, Discovery Alert & Argus. Times report-date relative.").font=Fn(8,False,GREY)
ws.merge_cells(start_row=r,start_column=2,end_row=r,end_column=7); ws.cell(r,2).alignment=left

# ---------- LME ----------
ws=wb.create_sheet("LME Prices & Inventory"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":15,"C":14,"D":14,"E":14,"F":13,"G":15,"H":7}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"LME ALUMINUM — DAILY SETTLEMENTS & INVENTORY","Official cash & 3-month settlements (USD/MT) and warehouse stock | Source: LME via Westmetall",8)
r=4; sect(ws,r,"DAILY SETTLEMENT SERIES",8); r+=1
hdr(ws,r,["Date","Cash ($/t)","3-Month ($/t)","Stock (t)","Cash Δ d/d","Cash–3M spread","Tr"],2); r+=1
lme=D["lme_series"]; first=r
for i,(dt,cash,m3,stk) in enumerate(lme):
    ws.cell(r,2,dt).font=Fn(10); ws.cell(r,2).alignment=center; ws.cell(r,2).border=box
    a=ws.cell(r,3,cash); a.number_format='#,##0.0'; a.font=Fn(10); a.alignment=Alignment(horizontal="right"); a.border=box
    b=ws.cell(r,4,m3); b.number_format='#,##0.0'; b.font=Fn(10); b.alignment=Alignment(horizontal="right"); b.border=box
    s=ws.cell(r,5,stk); s.number_format='#,##0'; s.font=Fn(10); s.alignment=Alignment(horizontal="right"); s.border=box
    d=ws.cell(r,6,f"=IF(C{r+1}=0,0,(C{r}-C{r+1})/C{r+1})") if i<len(lme)-1 else ws.cell(r,6,0)
    d.number_format='0.0%;-0.0%;0.0%'; d.font=Fn(10); d.alignment=Alignment(horizontal="right"); d.border=box
    sp=ws.cell(r,7,f"=C{r}-D{r}"); sp.number_format='#,##0.0'; sp.font=Fn(10); sp.alignment=Alignment(horizontal="right"); sp.border=box
    t=ws.cell(r,8,f'=IF(F{r}>0,"▲",IF(F{r}<0,"▼","▬"))'); t.font=Fn(12,True); t.alignment=center; t.border=box
    band(ws,r,2,8,i); r+=1
last=r-1
cf_posneg(ws,f"F{first}:F{last}"); cf_arrow(ws,f"H{first}:H{last}",f"F{first}")
r+=1; sect(ws,r,"PERIOD STATISTICS (window above)",8); r+=1
stats=[("Average cash",f"=AVERAGE(C{first}:C{last})",'#,##0.0'),("High cash",f"=MAX(C{first}:C{last})",'#,##0.0'),
       ("Low cash",f"=MIN(C{first}:C{last})",'#,##0.0'),("Average 3M",f"=AVERAGE(D{first}:D{last})",'#,##0.0'),
       ("Inventory change over window (Δ t)",f"=E{first}-E{last}",'#,##0'),("Average stock",f"=AVERAGE(E{first}:E{last})",'#,##0'),
       ("Avg cash–3M spread",f"=AVERAGE(G{first}:G{last})",'#,##0.0')]
for i,(name,formula,fmt) in enumerate(stats):
    ws.cell(r,2,name).font=Fn(10,True); ws.cell(r,2).alignment=left; ws.cell(r,2).border=box
    ws.merge_cells(start_row=r,start_column=2,end_row=r,end_column=5)
    cc=ws.cell(r,6,formula); cc.number_format=fmt; cc.font=Fn(10); cc.alignment=Alignment(horizontal="right"); cc.border=box
    ws.merge_cells(start_row=r,start_column=6,end_row=r,end_column=8)
    for col in range(2,9):
        if i%2==1 and ws.cell(r,col).fill.fgColor.rgb in (None,"00000000"): ws.cell(r,col).fill=fill(BAND)
        ws.cell(r,col).border=box
    r+=1
r+=1
ws.cell(r,2,D.get("lme_commentary","")).font=Fn(9,False,GREY)
ws.merge_cells(start_row=r,start_column=2,end_row=r+1,end_column=8); ws.cell(r,2).alignment=lefttop
r+=3; sect(ws,r,"PRICE TREND — LME CASH vs 3-MONTH vs INVENTORY",8); chart_anchor=r+1
hs=chart_anchor+26
ws.cell(hs,2,"Chart data (chronological)").font=Fn(8,True,GREY)
for j,h in enumerate(["Date","Cash ($/t)","3-Month ($/t)","Stock (t)"]):
    c=ws.cell(hs+1,2+j,h); c.font=Fn(8,True,WHITE); c.fill=fill(NAVY); c.alignment=center; c.border=box
rr=hs+2
for dt,cash,m3,stk in reversed(lme):
    ws.cell(rr,2,dt).font=Fn(8); ws.cell(rr,2).alignment=center
    for j,val in enumerate([cash,m3,stk]):
        cc=ws.cell(rr,3+j,val); cc.font=Fn(8); cc.alignment=Alignment(horizontal="right"); cc.number_format='#,##0.0' if j<2 else '#,##0'
    rr+=1
hd_last=rr-1
cats=Reference(ws,min_col=2,min_row=hs+2,max_row=hd_last)
ch=LineChart(); ch.title="LME Cash vs 3-Month ($/t)  &  Inventory (t, RH axis)"; ch.style=2
ch.y_axis.title="USD / tonne"; ch.x_axis.title=None; ch.x_axis.delete=False; ch.y_axis.delete=False
ch.height=11; ch.width=22.5
ch.add_data(Reference(ws,min_col=3,min_row=hs+1,max_row=hd_last),titles_from_data=True)
ch.add_data(Reference(ws,min_col=4,min_row=hs+1,max_row=hd_last),titles_from_data=True)
ch.set_categories(cats)
pr=D.get("chart_price_axis",[3500,3900]); sr=D.get("chart_stock_axis",[325000,348000])
ch.y_axis.scaling.min=pr[0]; ch.y_axis.scaling.max=pr[1]; ch.y_axis.majorUnit=50; ch.y_axis.majorGridlines=None
ch.series[0].graphicalProperties.line.solidFill=NAVY; ch.series[0].graphicalProperties.line.width=34000
ch.series[1].graphicalProperties.line.solidFill=GOLD; ch.series[1].graphicalProperties.line.width=34000
ch2=LineChart()
ch2.add_data(Reference(ws,min_col=5,min_row=hs+1,max_row=hd_last),titles_from_data=True)
ch2.set_categories(cats)
ch2.y_axis.axId=200; ch2.y_axis.title="Stock (t)"; ch2.y_axis.crosses="max"; ch2.y_axis.delete=False; ch2.x_axis.delete=True
ch2.y_axis.scaling.min=sr[0]; ch2.y_axis.scaling.max=sr[1]; ch2.y_axis.majorUnit=5000
ch2.series[0].graphicalProperties.line.solidFill="9AA0A6"; ch2.series[0].graphicalProperties.line.width=24000
ch2.series[0].graphicalProperties.line.dashStyle="dash"
ch += ch2
ws.add_chart(ch,f"B{chart_anchor}"); ws.print_area=f"A1:K{hd_last+1}"

# ---------- Premiums ----------
ws=wb.create_sheet("Premiums"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":30,"C":16,"D":10,"E":14,"F":8,"G":44}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"REGIONAL PHYSICAL PREMIUMS","Duty-paid / duty-unpaid premiums over LME by region | Verify against licensed PRA feed",7)
r=4; sect(ws,r,"PREMIUM ASSESSMENTS & TRAJECTORY",7); r+=1
hdr(ws,r,["Premium ($/t)","Current","Previous","Δ %","Trend","Source / note"],2); r+=1
pf=r
for i,p in enumerate(D["premiums"]):
    ws.cell(r,2,p["name"]).font=Fn(10,True); ws.cell(r,2).alignment=left; ws.cell(r,2).border=box
    cc=ws.cell(r,3,p["cur"]); cc.number_format='#,##0.0'; cc.font=Fn(10); cc.alignment=Alignment(horizontal="right"); cc.border=box
    cp=ws.cell(r,4,p["prev"]); cp.number_format='#,##0.0'; cp.font=Fn(10); cp.alignment=Alignment(horizontal="right"); cp.border=box
    dd=ws.cell(r,5,f"=IF(D{r}=0,0,(C{r}-D{r})/D{r})"); dd.number_format='0.0%;-0.0%;0.0%'; dd.font=Fn(10); dd.alignment=Alignment(horizontal="right"); dd.border=box
    tt=ws.cell(r,6,ARROW.format(c=f"C{r}",p=f"D{r}")); tt.font=Fn(12,True); tt.alignment=center; tt.border=box
    _ps=(("Avg last-mo "+format(p["avg"],",.1f")+" · ") if p.get("avg") is not None else "")+p["src"]
    ws.cell(r,7,_ps).font=Fn(9,False,GREY); ws.cell(r,7).alignment=left; ws.cell(r,7).border=box
    band(ws,r,2,7,i); r+=1
cf_posneg(ws,f"E{pf}:E{r-1}"); cf_arrow(ws,f"F{pf}:F{r-1}",f"E{pf}")
r+=1
ws.cell(r,2,D.get("premium_readthrough","")).font=Fn(9,False,NAVY)
ws.merge_cells(start_row=r,start_column=2,end_row=r+1,end_column=7); ws.cell(r,2).alignment=lefttop
r+=3
if D.get("premium_explainer"):
    sect(ws,r,"UNDERSTANDING THE PREMIUMS",7); r+=1
    r=tbl(ws,r,["Term","Definition"],[[x.get("term"),x.get("desc")] for x in D["premium_explainer"]])
ph=D.get("premium_history",{})
if ph.get("labels_reg"):
    r+=1; sect(ws,r,"PREMIUM HISTORY ($/t, indicative · last = Q3 expectation)",7); r+=1
    r=tbl(ws,r,["Series"]+ph["labels_reg"],[["MJP (Japan)"]+ph.get("mjp",[]),["CIF Japan"]+ph.get("cif",[]),["EU duty-unpaid"]+ph.get("edu",[]),["MW US Transaction"]+ph.get("usmw_usd",[])])
if D.get("premium_outlook"):
    r+=1; sect(ws,r,"FORWARD EXPECTATIONS (H2-26)",7); r+=1; r=bullets(ws,r,D["premium_outlook"],7)

# ---------- Alumina ----------
ws=wb.create_sheet("Alumina & Raw Materials"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":34,"C":14,"D":10,"E":12,"F":8,"G":46}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"ALUMINA & RAW MATERIALS","Alumina indices, bauxite & input cost commentary",7)
r=4; sect(ws,r,"ALUMINA PRICE INDICES",7); r+=1
hdr(ws,r,["Index","Value","Unit","As of","Tr","Source / note"],2); r+=1
for i,a in enumerate(D["alumina"]):
    ws.cell(r,2,a["name"]).font=Fn(10,True); ws.cell(r,2).alignment=left; ws.cell(r,2).border=box
    cv=ws.cell(r,3,a["val"]); cv.number_format='#,##0.00'; cv.font=Fn(10); cv.alignment=Alignment(horizontal="right"); cv.border=box
    ws.cell(r,4,a["unit"]).font=Fn(9); ws.cell(r,4).alignment=center; ws.cell(r,4).border=box
    ws.cell(r,5,a["asof"]).font=Fn(9); ws.cell(r,5).alignment=center; ws.cell(r,5).border=box
    gl,gc=arr[a["trend"]]; x=ws.cell(r,6,gl); x.font=Fn(12,True,gc); x.alignment=center; x.border=box
    ws.cell(r,7,a["src"]).font=Fn(9,False,GREY); ws.cell(r,7).alignment=left; ws.cell(r,7).border=box
    band(ws,r,2,7,i); r+=1
r+=1; sect(ws,r,"BAYER-PROCESS RAW MATERIALS (caustic soda · lime · bauxite)",7); r+=1
hdr(ws,r,["Input","Latest","Unit","As of","Tr","Source / note"],2); r+=1
for i,m in enumerate(D.get("raw_materials",[])):
    ws.cell(r,2,m["name"]).font=Fn(10,True); ws.cell(r,2).alignment=left; ws.cell(r,2).border=box
    ws.cell(r,3,str(m["val"])).font=Fn(10); ws.cell(r,3).alignment=Alignment(horizontal="right"); ws.cell(r,3).border=box
    ws.cell(r,4,m["unit"]).font=Fn(9); ws.cell(r,4).alignment=center; ws.cell(r,4).border=box
    ws.cell(r,5,m["asof"]).font=Fn(9); ws.cell(r,5).alignment=center; ws.cell(r,5).border=box
    gl,gc=arr.get(m["trend"],("▬",GREY)); x=ws.cell(r,6,gl); x.font=Fn(12,True,gc); x.alignment=center; x.border=box
    ws.cell(r,7,m["src"]).font=Fn(9,False,GREY); ws.cell(r,7).alignment=left; ws.cell(r,7).border=box
    band(ws,r,2,7,i); r+=1
r+=1; sect(ws,r,"RAW MATERIALS & SUPPLY COMMENTARY",7); r+=1
for n in (D["alumina_notes"]+D.get("alumina_outlook",[])):
    ws.cell(r,2,"▸").font=Fn(10,True,GOLD); ws.cell(r,2).alignment=Alignment(horizontal="center",vertical="top")
    ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=7)
    ws.cell(r,3,n).font=Fn(10); ws.cell(r,3).alignment=lefttop; ws.row_dimensions[r].height=28; r+=1
r+=1
if D.get("alumina_explainer"):
    sect(ws,r,"UNDERSTANDING ALUMINA & RAW MATERIALS",7); r+=1
    r=tbl(ws,r,["Term","Definition"],[[x.get("term"),x.get("desc")] for x in D["alumina_explainer"]])
ah=D.get("alumina_history",{})
if ah.get("labels"):
    r+=1; sect(ws,r,"ALUMINA PRICE HISTORY ($/t, indicative · last = Q3 expectation)",7); r+=1
    r=tbl(ws,r,["Series"]+ah["labels"],[["FOB Australia"]+ah.get("fob",[]),["API / Platts"]+ah.get("api",[])])

# ---------- Macro & FX ----------
ws=wb.create_sheet("Macro & FX"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":28,"C":14,"D":12,"E":8,"F":48}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"MACRO & CROSS-ASSET","USD, FX, rates, energy & base-metals | Source: Trading Economics, "+DATESTR,6)
r=4; sect(ws,r,"KEY INDICATORS",6); r+=1
hdr(ws,r,["Indicator","Value","Day %","Tr","Relevance to aluminum"],2); r+=1
mf=r
for i,m in enumerate(D["macro"]):
    ws.cell(r,2,m["name"]).font=Fn(10,True); ws.cell(r,2).alignment=left; ws.cell(r,2).border=box
    ws.cell(r,3,m["value"]).font=Fn(10); ws.cell(r,3).alignment=Alignment(horizontal="right"); ws.cell(r,3).border=box
    dd=ws.cell(r,4,m["day"]/100); dd.number_format='0.00%;-0.00%;0.00%'; dd.font=Fn(10); dd.alignment=Alignment(horizontal="right"); dd.border=box
    t=ws.cell(r,5,f'=IF(D{r}>0,"▲",IF(D{r}<0,"▼","▬"))'); t.font=Fn(12,True); t.alignment=center; t.border=box
    ws.cell(r,6,m["note"]).font=Fn(9,False,GREY); ws.cell(r,6).alignment=left; ws.cell(r,6).border=box
    band(ws,r,2,6,i); r+=1
cf_posneg(ws,f"D{mf}:D{r-1}"); cf_arrow(ws,f"E{mf}:E{r-1}",f"D{mf}")
r+=1; sect(ws,r,"MACRO EVENTS & DATA",6); r+=1
for n in D["macro_events"]:
    ws.cell(r,2,"▸").font=Fn(10,True,GOLD); ws.cell(r,2).alignment=Alignment(horizontal="center",vertical="top")
    ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=6)
    ws.cell(r,3,n).font=Fn(10); ws.cell(r,3).alignment=lefttop; ws.row_dimensions[r].height=30; r+=1

# ---------- News ----------
ws=wb.create_sheet("Market News & Sentiment"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":22,"C":54,"D":16,"E":16,"F":20}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"MARKET NEWS & SENTIMENT — "+DATESTR,"Headlines tagged by theme, LME impact & source",6)
r=4; hdr(ws,r,["Theme","Headline / detail","LME impact","Horizon","Source"],2); r+=1
for i,n in enumerate(D["news"]):
    ws.cell(r,2,n["theme"]).font=Fn(10,True,NAVY); ws.cell(r,2).alignment=lefttop; ws.cell(r,2).border=box
    ws.cell(r,3,n["headline"]).font=Fn(10); ws.cell(r,3).alignment=lefttop; ws.cell(r,3).border=box
    ic=ws.cell(r,4,n["impact"]); ic.font=Fn(10,True,icol(n["impact"])); ic.alignment=center; ic.border=box
    ws.cell(r,5,n["horizon"]).font=Fn(9); ws.cell(r,5).alignment=center; ws.cell(r,5).border=box
    ws.cell(r,6,n["source"]).font=Fn(9,False,GREY); ws.cell(r,6).alignment=lefttop; ws.cell(r,6).border=box
    band(ws,r,2,6,i); ws.row_dimensions[r].height=44; r+=1

# ---------- Peer Earnings ----------
def scol(s): return GREEN if "Pos" in s else (RED if "Neg" in s else GREY)
ws=wb.create_sheet("Peer Earnings"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":20,"C":16,"D":11,"E":11,"F":40,"G":40,"H":12}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"PEER EARNINGS — ALUMINUM & MINING INDUSTRY","Most recent reported results & guidance | Quarterly/episodic — refreshed as companies report",8)
r=4; hdr(ws,r,["Company","Group","Period","Reported","Headline result","Read-through / guidance","Sentiment"],2); r+=1
for i,e in enumerate(D.get("earnings",[])):
    ws.cell(r,2,e["company"]).font=Fn(10,True,NAVY); ws.cell(r,2).alignment=lefttop; ws.cell(r,2).border=box
    ws.cell(r,3,e["group"]).font=Fn(9); ws.cell(r,3).alignment=lefttop; ws.cell(r,3).border=box
    ws.cell(r,4,e["period"]).font=Fn(9); ws.cell(r,4).alignment=center; ws.cell(r,4).border=box
    ws.cell(r,5,e["reported"]).font=Fn(9); ws.cell(r,5).alignment=center; ws.cell(r,5).border=box
    ws.cell(r,6,e["headline"]).font=Fn(9); ws.cell(r,6).alignment=lefttop; ws.cell(r,6).border=box
    ws.cell(r,7,e["readthrough"]).font=Fn(9); ws.cell(r,7).alignment=lefttop; ws.cell(r,7).border=box
    sc=ws.cell(r,8,e["sentiment"]); sc.font=Fn(10,True,scol(e["sentiment"])); sc.alignment=center; sc.border=box
    band(ws,r,2,8,i); ws.row_dimensions[r].height=54; r+=1
r+=1
ws.cell(r,2,D.get("earnings_note","Earnings are quarterly/episodic; entries show each peer's most recent reported results. Sources: company releases, SEC/exchange filings, Alcircle, Discovery Alert, Investing.com, Zawya, TradeArabia.")).font=Fn(8,False,GREY)
ws.merge_cells(start_row=r,start_column=2,end_row=r+1,end_column=8); ws.cell(r,2).alignment=lefttop

# ---------- Commercial ----------
ws=wb.create_sheet("Commercial Implications"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":26,"C":64,"D":16}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"COMMERCIAL IMPLICATIONS — ALUMINUM BUSINESS","SME read-through across the commercial value chain | Classification: Restricted",4)
r=4; hdr(ws,r,["Function","Read-through & recommended action","Priority"],2); r+=1
for i,c in enumerate(D["commercial"]):
    ws.cell(r,2,c["function"]).font=Fn(10,True,NAVY); ws.cell(r,2).alignment=lefttop; ws.cell(r,2).border=box
    ws.cell(r,3,c["text"]).font=Fn(10); ws.cell(r,3).alignment=lefttop; ws.cell(r,3).border=box
    pc=ws.cell(r,4,c["priority"]); pc.font=Fn(10,True,RED if c["priority"]=="High" else GOLD); pc.alignment=center; pc.border=box
    band(ws,r,2,4,i); ws.row_dimensions[r].height=72; r+=1
r+=1
ws.cell(r,2,"Bottom line:").font=Fn(10,True,NAVY)
ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=4)
ws.cell(r,3,D.get("bottom_line","")).font=Fn(10,False,GREEN); ws.cell(r,3).alignment=lefttop; ws.row_dimensions[r].height=40

# ---------- Sources ----------
ws=wb.create_sheet("Sources & Data Quality"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":34,"C":72}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"SOURCES & DATA QUALITY","Citations, caveats & refresh guidance",3)
r=4; sect(ws,r,"SOURCES",3); r+=1
hdr(ws,r,["Data set","Source"],2); r+=1
for i,(a,b) in enumerate(D["sources"]):
    ws.cell(r,2,a).font=Fn(10,True); ws.cell(r,2).alignment=lefttop; ws.cell(r,2).border=box
    ws.cell(r,3,b).font=Fn(10); ws.cell(r,3).alignment=lefttop; ws.cell(r,3).border=box
    band(ws,r,2,3,i); ws.row_dimensions[r].height=26; r+=1
r+=1; sect(ws,r,"DATA-QUALITY CAVEATS",3); r+=1
for n in D["caveats"]:
    ws.cell(r,2,"▸").font=Fn(10,True,GOLD); ws.cell(r,2).alignment=Alignment(horizontal="center",vertical="top")
    ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=3)
    ws.cell(r,3,n).font=Fn(9); ws.cell(r,3).alignment=lefttop; ws.row_dimensions[r].height=40; r+=1

# ---------- Inputs & Logistics ----------
ws=wb.create_sheet("Inputs & Logistics"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":28,"C":16,"D":12,"E":8,"F":11,"G":12,"H":10,"I":11,"J":40}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"INPUT BASKET & LOGISTICS — FEASIBILITY","Cost stack to make 1 t of primary aluminium + logistics | Indicative public anchors, not advice",10)
r=4; sect(ws,r,"INPUT COST BASKET",10); r+=1
hdr(ws,r,["Input","Category","Price","Unit","~ /t Al","Cost share","Index","Supply risk","Source / note"],2); r+=1
for i,x in enumerate(D.get("inputs",[])):
    vals=[x.get("name"),x.get("cat"),x.get("val"),x.get("unit"),x.get("ratio"),x.get("share"),x.get("index"),x.get("risk"),x.get("src")]
    for j,v in enumerate(vals):
        c=ws.cell(r,2+j,v); c.border=box; c.font=Fn(9,j==0)
        c.alignment=(lefttop if j in (0,8) else center)
    band(ws,r,2,10,i); ws.row_dimensions[r].height=32; r+=1
r+=1; sect(ws,r,"LOGISTICS",10); r+=1
hdr(ws,r,["Item","Latest / status","Note"],2); r+=1
for i,x in enumerate(D.get("logistics",[])):
    ws.cell(r,2,x.get("name")).font=Fn(10,True); ws.cell(r,2).border=box; ws.cell(r,2).alignment=left
    ws.cell(r,3,x.get("val")).font=Fn(10); ws.cell(r,3).border=box; ws.cell(r,3).alignment=center
    ws.merge_cells(start_row=r,start_column=4,end_row=r,end_column=10); ws.cell(r,4,x.get("note")).font=Fn(9,False,GREY); ws.cell(r,4).border=box; ws.cell(r,4).alignment=lefttop
    for col in (5,6,7,8,9,10): ws.cell(r,col).border=box
    ws.row_dimensions[r].height=28; r+=1
r+=1; sect(ws,r,"FEASIBILITY READ — WHAT TO MONITOR / SOURCE",10); r+=1; r=bullets(ws,r,D.get("inputs_summary",[]),10)

# ---------- Outlook (reference) ----------
O=D.get("outlook",{})
ws=wb.create_sheet("Outlook"); ws.sheet_view.showGridLines=False
for c_,w in {"A":2,"B":34,"C":18,"D":18,"E":18,"F":34}.items(): ws.column_dimensions[c_].width=w
title_block(ws,"OUTLOOK & FORECAST","Forward curve · consensus · balance · scenarios · risks · catalysts | Indicative, not advice",6)
r=4; sect(ws,r,"AI TREND ANALYSIS (auto-generated)",6); r+=1; r=bullets(ws,r,O.get("ai_analysis",[]))
r+=1; sect(ws,r,"FORWARD PRICE PATH ($/t)",6); r+=1; r=tbl(ws,r,["Tenor / horizon","Level","Basis"],[[x.get("tenor"),x.get("price"),x.get("basis")] for x in O.get("forward_path",[])])
r+=1; sect(ws,r,"ANALYST & AGENCY CONSENSUS",6); r+=1; r=tbl(ws,r,["Source","2026","2027","Note"],[[x.get("source"),x.get("y2026"),x.get("y2027"),x.get("note")] for x in O.get("consensus",[])])
r+=1; sect(ws,r,"SUPPLY–DEMAND BALANCE",6); r+=1; r=tbl(ws,r,["Year","Balance","Note"],[[x.get("year"),x.get("value"),x.get("label")] for x in O.get("balance",[])])
r+=1; sect(ws,r,"CAPACITY PIPELINE",6); r+=1; r=tbl(ws,r,["Asset / region","Change","Timing"],[[x.get("asset"),x.get("change"),x.get("timing")] for x in O.get("capacity_pipeline",[])])
r+=1; sect(ws,r,"SCENARIOS — 12-MONTH",6); r+=1; r=tbl(ws,r,["Case","Prob.","Target ($/t)","Key drivers"],[[x.get("case"),x.get("prob"),x.get("target"),x.get("drivers")] for x in O.get("scenarios",[])])
for sc in O.get("scenarios",[]):
    if sc.get("drivers_list"):
        ws.cell(r,2,sc.get("case")+" — drivers").font=Fn(10,True,NAVY); r+=1; r=bullets(ws,r,sc["drivers_list"])
r+=1; sect(ws,r,"RISK HEATMAP",6); r+=1; r=tbl(ws,r,["Risk","Likelihood","Impact","Trend"],[[x.get("risk"),x.get("likelihood"),x.get("impact"),x.get("trend")] for x in O.get("risks",[])])
r+=1; sect(ws,r,"CATALYST CALENDAR",6); r+=1; r=tbl(ws,r,["Date","Event","Likely impact"],[[x.get("date"),x.get("event"),x.get("impact")] for x in O.get("catalysts",[])])
r+=1; sect(ws,r,"SOURCES (further reading)",6); r+=1; r=tbl(ws,r,["Source","Link"],[[s[0],s[1]] for s in O.get("sources",[])])

_order=["Cover","Dashboard","LME Prices & Inventory","Premiums","Alumina & Raw Materials","Inputs & Logistics","Macro & FX","Market News & Sentiment","Peer Earnings","Outlook","Commercial Implications","Sources & Data Quality"]
wb._sheets.sort(key=lambda s:_order.index(s.title) if s.title in _order else 99)

for nm in wb.sheetnames:
    if nm!="Cover": wb[nm].freeze_panes="A4"
    setup_page(wb[nm])
out=os.path.join(OUTDIR,f"Aluminum_Daily_Market_Report_{ISO}.xlsx")
wb.save(out); print("saved",out)
