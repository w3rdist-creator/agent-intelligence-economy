#!/usr/bin/env python3
import re, sys
from pathlib import Path
pat=re.compile(r'(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[A-Za-z0-9_./+=-]{12,}|sk-[A-Za-z0-9]{20,}')
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
hits=[]
for p in root.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.txt','.csv','.json','.yaml','.yml','.py'}:
        txt=p.read_text(encoding='utf-8', errors='ignore')
        for i,line in enumerate(txt.splitlines(),1):
            if pat.search(line): hits.append((p,i,line[:160]))
print(f'secret_like_hits={len(hits)}')
for p,i,l in hits[:50]: print(f'{p}:{i}: {l}')
sys.exit(1 if hits else 0)
