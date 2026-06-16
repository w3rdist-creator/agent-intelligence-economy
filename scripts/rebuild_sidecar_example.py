#!/usr/bin/env python3
import sqlite3, sys
from pathlib import Path
root=Path(sys.argv[1]); db=Path(sys.argv[2])
db.parent.mkdir(parents=True, exist_ok=True)
con=sqlite3.connect(db); con.execute('create table if not exists notes(path text primary key, title text, chars integer)')
for p in root.rglob('*.md'):
    txt=p.read_text(encoding='utf-8', errors='replace')
    con.execute('insert or replace into notes values (?,?,?)',(str(p.relative_to(root)),p.stem,len(txt)))
con.commit(); print(db)
