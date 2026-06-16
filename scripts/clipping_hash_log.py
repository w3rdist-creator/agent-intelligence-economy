#!/usr/bin/env python3
import csv, hashlib, sys
from pathlib import Path

def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''):
            h.update(b)
    return h.hexdigest()

if len(sys.argv) != 3:
    print('usage: clipping_hash_log.py CLIPPINGS_DIR LOG_CSV', file=sys.stderr); sys.exit(2)
root=Path(sys.argv[1]); log=Path(sys.argv[2])
old={}
if log.exists():
    for r in csv.DictReader(log.open(newline='', encoding='utf-8')):
        old[r['path']]=r['sha256']
rows=[]; changed=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and not p.name.startswith('.'):
        s=sha256(p); rel=str(p.relative_to(root))
        status='unchanged' if old.get(rel)==s else ('changed' if rel in old else 'new')
        rows.append({'path':rel,'sha256':s,'status':status})
        if status!='unchanged': changed.append(rel)
log.parent.mkdir(parents=True, exist_ok=True)
with log.open('w', newline='', encoding='utf-8') as f:
    w=csv.DictWriter(f, fieldnames=['path','sha256','status'], lineterminator='\n'); w.writeheader(); w.writerows(rows)
print(f'{len(rows)} files tracked; {len(changed)} new/changed')
for c in changed[:50]: print(c)
