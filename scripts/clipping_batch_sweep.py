#!/usr/bin/env python3
import csv, hashlib, sys, datetime
from pathlib import Path

def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''):
            h.update(b)
    return h.hexdigest()

def preview(p, n=1200):
    try:
        return p.read_text(encoding='utf-8', errors='replace')[:n].replace('\n',' ').strip()
    except Exception as e:
        return f'[unreadable: {e}]'

if len(sys.argv) != 4:
    print('usage: clipping_batch_sweep.py CLIPPINGS_DIR LOG_CSV REPORTS_DIR', file=sys.stderr); sys.exit(2)
clippings=Path(sys.argv[1]); log=Path(sys.argv[2]); reports=Path(sys.argv[3])
old={}
if log.exists():
    for r in csv.DictReader(log.open(newline='', encoding='utf-8')):
        old[r['path']]=r['sha256']
rows=[]; changed=[]
for p in sorted(clippings.rglob('*')):
    if p.is_file() and not p.name.startswith('.'):
        rel=str(p.relative_to(clippings)); s=sha256(p)
        status='unchanged' if old.get(rel)==s else ('changed' if rel in old else 'new')
        rows.append({'path':rel,'sha256':s,'status':status})
        if status!='unchanged': changed.append((rel,p,s,status))
log.parent.mkdir(parents=True, exist_ok=True)
with log.open('w', newline='', encoding='utf-8') as f:
    writer=csv.DictWriter(f, fieldnames=['path','sha256','status'], lineterminator='\n'); writer.writeheader(); writer.writerows(rows)
reports.mkdir(parents=True, exist_ok=True)
date=datetime.date.today().isoformat()
out=reports/f'{date} - clipping sweep report.md'
lines=[f'# Clipping Sweep Report - {date}','',f'- Total tracked: {len(rows)}',f'- New/changed: {len(changed)}',f'- Unchanged skipped: {len(rows)-len(changed)}','','## New / changed clipping map']
for rel,p,s,status in changed:
    lines += ['',f'### {rel}',f'- Status: {status}',f'- SHA-256: `{s}`','- Suggested disposition: TBD by reviewer','',preview(p)]
lines += ['','## Skill/runbook candidates','','## Already absorbed','','## Kill/archive','','## Verification',f'- Hash log written: `{log}`']
out.write_text('\n'.join(lines)+'\n', encoding='utf-8')
print(out)
