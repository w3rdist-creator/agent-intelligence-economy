#!/usr/bin/env python3
import csv, sys, collections
rows=list(csv.DictReader(open(sys.argv[1], newline='', encoding='utf-8')))
by=collections.Counter(r.get('domain','') for r in rows)
print(f'belief revisions: {len(rows)}')
for k,v in by.items(): print(f'- {k}: {v}')
