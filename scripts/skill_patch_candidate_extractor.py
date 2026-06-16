#!/usr/bin/env python3
import sys
from pathlib import Path
for p in map(Path, sys.argv[1:]):
    text=p.read_text(encoding='utf-8', errors='replace')
    if any(k in text.lower() for k in ['workflow','checklist','procedure','runbook','skill']):
        print(f'candidate: {p}')
