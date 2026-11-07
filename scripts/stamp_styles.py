"""Give the shared stylesheet a content version so cached readers receive it."""
from pathlib import Path
import hashlib,re

B=Path(__file__).resolve().parents[1]/'books/java'
out=B/'_book';css=out/'styles.css'
if css.exists():
    version=hashlib.sha256(css.read_bytes()).hexdigest()[:12]
    count=0
    for page in out.rglob('*.html'):
        original=page.read_text()
        updated=re.sub(r'href="((?:\.\./|\./)*styles\.css)(?:\?v=[a-f0-9]+)?"',lambda m:f'href="{m[1]}?v={version}"',original)
        if updated!=original:
            page.write_text(updated);count+=1
    print(f'Stylesheet version {version}: updated {count} rendered pages')
