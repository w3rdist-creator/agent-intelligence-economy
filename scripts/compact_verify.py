#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
md=list(root.rglob('*.md')); csvs=list(root.rglob('*.csv')); jsons=list(root.rglob('*.json'))
errors=[]
for p in csvs:
    try:
        list(csv.reader(p.open(newline='', encoding='utf-8')))
    except Exception as e: errors.append(f'CSV {p}: {e}')
for p in jsons:
    try:
        json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'JSON {p}: {e}')
for p in md:
    txt=p.read_text(encoding='utf-8', errors='replace')
    if '\t' in txt: errors.append(f'TAB {p}')
print(f'markdown={len(md)} csv={len(csvs)} json={len(jsons)} errors={len(errors)}')
for e in errors[:100]: print('ERROR', e)
sys.exit(1 if errors else 0)
