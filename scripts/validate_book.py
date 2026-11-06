"""Validate actual failure modes: XML, registry, local links and rendered anchors."""
from pathlib import Path
import re,json,sys,xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'books/java';errors=[]
for p in (B/'assets').rglob('*.svg'):
 try:ET.parse(p)
 except ET.ParseError as e:errors.append(f'{p}: {e}')
data=json.loads((B/'curriculum.json').read_text());lessons=data['lessons']
if sorted(x['id'] for x in lessons)!=list(range(77)):errors.append('Curriculum IDs missing or duplicated')
for x in lessons:
 if x['url'] and not (B/x['url'].replace('.html','.qmd')).is_file():errors.append(f'Missing lesson: {x}')
for p in B.rglob('*.qmd'):
 if '_book' in p.parts:continue
 for target in re.findall(r'\]\(([^\s)]+)',p.read_text()):
  if '://' in target or target.startswith('#'):continue
  link=unquote(target.split('#')[0])
  if link and not (p.parent/link).exists():errors.append(f'{p.relative_to(ROOT)}: missing {link}')
for text in ['{{AVAILABLE}}','{{RECEIVED}}','استلمنا نص الفيديو الأول فقط','الدرس الأول فقط يحتوي شرحًا']:
 if text in (B/'index.qmd').read_text()+(B/'roadmap.qmd').read_text():errors.append('Stale status: '+text)
class Page(HTMLParser):
 def __init__(self,text):self.ids=set();self.links=[];super().__init__();self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  if tag in ['a','img','link','script']:
   target=a.get('href') if tag in ['a','link'] else a.get('src')
   if target:self.links.append(target)
out=B/'_book'
if '--rendered' in sys.argv:
 pages={p:Page(p.read_text()) for p in out.rglob('*.html')}
 for p,page in pages.items():
  for target in page.links:
   u=urlsplit(target)
   if u.scheme or u.netloc or target.startswith('data:') or u.path.startswith('/'):continue
   dest=(p.parent/unquote(u.path)).resolve() if u.path else p
   if dest.is_dir():dest=dest/'index.html'
   if not dest.exists():errors.append(f'{p.relative_to(out)}: missing {target}')
   elif u.fragment and dest in pages and unquote(u.fragment) not in pages[dest].ids:errors.append(f'{p.relative_to(out)}: missing anchor {target}')
  for link in page.links:
   if 'github.com/mohammadwajdi19980-creator/java-learning-library/blob/main/' in link and '/books/java/' not in link:errors.append('Incorrect source link: '+link)
 if not (out/'Java-Learning-Library.epub').exists():errors.append('EPUB not generated')
 if not pages:errors.append('No rendered pages')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('PASS: SVG XML, curriculum IDs, source links, status'+(', rendered links/anchors and EPUB' if '--rendered' in sys.argv else ''))
