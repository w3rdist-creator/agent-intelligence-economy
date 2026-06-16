#!/usr/bin/env python3
import re, sys
from pathlib import Path
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
stems={p.stem for p in root.rglob('*.md')}
missing=[]
for p in root.rglob('*.md'):
    text=p.read_text(encoding='utf-8', errors='replace')
    for m in re.findall(r'\[\[([^\]|#]+)', text):
        if Path(m).name not in stems and m not in stems:
            missing.append((str(p),m))
print(f'missing_wikilinks={len(missing)}')
for p,m in missing[:100]: print(f'{p}: [[{m}]]')
sys.exit(1 if missing else 0)
