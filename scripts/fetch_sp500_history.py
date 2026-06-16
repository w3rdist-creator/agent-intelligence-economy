#!/usr/bin/env python3
import csv, datetime, json, math, time, urllib.request
from pathlib import Path

outdir = Path(__file__).resolve().parents[1] / 'starter-vault' / 'Market Research' / 'Data'
outdir.mkdir(parents=True, exist_ok=True)
# Yahoo's ^GSPC metadata reports a firstTradeDate before 1970. Use that
# negative Unix timestamp rather than period1=0 so the public starter keeps
# the long S&P 500 price history back to 1927 when Yahoo serves it.
url = f'https://query1.finance.yahoo.com/v8/finance/chart/%5EGSPC?period1=-1325583000&period2={int(time.time())}&interval=1d&events=history&includeAdjustedClose=true'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
res = json.loads(urllib.request.urlopen(req, timeout=60).read().decode('utf-8'))['chart']['result'][0]
quote = res['indicators']['quote'][0]
rows = []
for i, ts in enumerate(res['timestamp']):
    close = quote['close'][i]
    if close is None:
        continue
    high = quote['high'][i] or close
    low = quote['low'][i] or close
    date = datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).date().isoformat()
    rows.append({'date':date, 'year':date[:4], 'close':float(close), 'high':float(high), 'low':float(low)})
by = {}
for row in rows:
    by.setdefault(row['year'], []).append(row)
annual = []
prev_end = None
for year in sorted(by):
    rs = by[year]
    start, end = rs[0]['close'], rs[-1]['close']
    ret = '' if prev_end is None else end / prev_end - 1
    running_high = -1
    max_dd = 0
    for r in rs:
        running_high = max(running_high, r['high'])
        max_dd = min(max_dd, r['low'] / running_high - 1)
    annual.append({
        'year': year,
        'start_date': rs[0]['date'],
        'end_date': rs[-1]['date'],
        'start_close': f'{start:.4f}',
        'end_close': f'{end:.4f}',
        'annual_return': '' if ret == '' else f'{ret:.6f}',
        'max_drawdown_from_year_high': f'{max_dd:.6f}',
        'year_high': f'{max(r["high"] for r in rs):.4f}',
        'year_low': f'{min(r["low"] for r in rs):.4f}',
        'trading_days': len(rs),
        'source': 'Yahoo Finance chart API ^GSPC',
    })
    prev_end = end
with (outdir / 'sp500_annual_history.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(annual[0].keys()), lineterminator='\n')
    writer.writeheader(); writer.writerows(annual)
print(outdir / 'sp500_annual_history.csv')
