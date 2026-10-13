import json,re
P='market_data.json'; d=json.load(open(P,encoding='utf-8'))
for a in d['alumina']:
    s=a['src'].replace("COMPILED TUESDAY 13-OCTOBER-2026 (LME BOARD KEPT ON 09-OCTOBER - SEE CAVEATS).","COMPILED TUESDAY 13-OCTOBER-2026 (LME BOARD ON THE 12-OCTOBER OFFICIAL).")
    m=re.search(r"THE RATIO: LME Alumina at \$360\.40/t against the 09-October aluminium three-month of \$3,070\.00 is [0-9.]+%",s)
    if m: s=s.replace(m.group(0),f"THE RATIO: LME Alumina at $360.40/t against the 12-October aluminium three-month of $3,060.00 is {360.4/3060*100:.2f}%")
    a['src']=s
d['commercial']=d['commercial'].replace("is $1,527.75 on 12-October cash","is $1,527.50 on 12-October cash")
json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
s=json.dumps(d); print(s.count('BOARD KEPT'), s.count('1,527.75'), s.count('09-October aluminium three-month'))
