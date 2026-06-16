#!/usr/bin/env python3
import csv, sys
from pathlib import Path
p=Path(sys.argv[1])
rows=list(csv.DictReader(p.open(newline='', encoding='utf-8')))
print('| Loop | Verdict | Impact | Signal | Burden | Next action |')
print('|---|---|---:|---:|---:|---|')
for r in rows:
    print(f"| {r.get('name','')} | {r.get('verdict','')} | {r.get('decision_impact_1_5','')} | {r.get('signal_quality_1_5','')} | {r.get('review_burden_1_5','')} | {r.get('next_action','')} |")
