"""Validate actual failure modes: XML, registry, local links and rendered anchors."""
from pathlib import Path
import re,json,sys,hashlib,posixpath,zipfile,xml.etree.ElementTree as ET
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
 if x['editorial_status']=='reviewed' and (x['source_status']!='received' or not x['url']):errors.append(f'Reviewed lesson without received source/URL: {x["id"]}')
for p in B.rglob('*.qmd'):
 if '_book' in p.parts:continue
 for target in re.findall(r'\]\(([^\s)]+)',p.read_text()):
  if '://' in target or target.startswith('#'):continue
  link=unquote(target.split('#')[0])
  if link and not (p.parent/link).exists():errors.append(f'{p.relative_to(ROOT)}: missing {link}')
for text in ['{{AVAILABLE}}','{{RECEIVED}}','استلمنا نص الفيديو الأول فقط','الدرس الأول فقط يحتوي شرحًا']:
 if text in (B/'index.qmd').read_text()+(B/'roadmap.qmd').read_text():errors.append('Stale status: '+text)
for p in [*B.rglob('*.qmd'),B/'includes/shell.html']:
 if '_book' in p.parts:continue
 for attr,target in re.findall(r'(href|src|data-book-path)="([^"<>]+)"',p.read_text()):
  u=urlsplit(target)
  if u.scheme or u.netloc or not u.path or u.path.startswith('/'):continue
  dest=(B if attr=='data-book-path' else p.parent)/unquote(u.path)
  if dest.suffix=='.html':dest=dest.with_suffix('.qmd')
  if dest.suffix=='.epub':continue # Produced by Quarto, checked after rendering.
  if not dest.exists():errors.append(f'{p.relative_to(ROOT)}: missing HTML link {target}')
# Reader-facing terminology and reference contract (archives retain original provenance).
public_pages=[p for p in B.rglob('*.qmd') if '_book' not in p.parts]
term_aliases=[alias for aliases in json.loads((ROOT/'scripts/technical_terms.json').read_text()).values() for alias in aliases]
translated_name=re.compile(r'(?<![\u0621-\u064a])(?:'+'|'.join(map(re.escape,sorted(term_aliases,key=len,reverse=True)))+r')(?![\u0621-\u064a])')
for p in public_pages:
 text=p.read_text()
 if translated_name.search(text):errors.append(f'{p.relative_to(ROOT)}: component/tool name must be English')
 if re.search(r'youtu(?:be\.com|\.be)|\bvideos?\b|فيديو|تفريغ|\btranscripts?\b',text,re.I):errors.append(f'{p.relative_to(ROOT)}: video reference in public book')
 if re.search(r'(?<![\u0621-\u064a])(?:محرر|المحرر|متغير|المتغير|متغيرات|المتغيرات|مصفوفة|كائن|دالة|حلقة|الحلقة|عداد|التعبير|التعبيرات|الإسناد|المشروع|المشاريع|محرف|المحرف|محارف|المحارف)(?![\u0621-\u064a])',text):errors.append(f'{p.relative_to(ROOT)}: translated technical name')
glossary=(B/'glossary.qmd').read_text()
definitions=re.findall(r'^\*\*English definition:\*\* .+$',glossary,re.M)
blocks=re.findall(r'::: \{\.english-definition dir="ltr" lang="en"\}\n\n(\*\*English definition:\*\* [^\n]+)\n\n:::',glossary)
if not definitions or definitions!=blocks:errors.append('Glossary English definitions must have explicit LTR/lang blocks')
registry=json.loads((B/'assets/registry.json').read_text())
registered={x['file'] for x in registry}
for asset in registry:
 if not (B/asset['file']).is_file():errors.append('Missing registered asset: '+asset['file'])
for p in (B/'lessons').glob('*.qmd'):
 for target in re.findall(r'!\[[^\]]*\]\(([^\s)]+)',p.read_text()):
  if '://' not in target:
   rel=(p.parent/target).resolve().relative_to(B.resolve()).as_posix()
   if rel not in registered:errors.append(f'Unregistered image: {rel}')
manifest=ROOT/'docs/sources/batch-002-013.json'
if manifest.exists():
 for source in json.loads(manifest.read_text()):
  path=ROOT/source['archive']
  if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=source['sha256']:errors.append('Transcript archive changed: '+source['archive'])
 ledger=json.loads((ROOT/'docs/sources/coverage-002-013.json').read_text())
 for unit in ledger['units']:
  path,heading=unit['output_ref'].split(' > ',1)
  if not (ROOT/path).is_file() or not re.search(r'^#{1,6} '+re.escape(heading)+r'\s*$',(ROOT/path).read_text(),re.M):errors.append('Broken coverage reference: '+unit['id'])
 print(f'Coverage references checked: {len(ledger["units"])}; {sum(u["status"]=="unclear" for u in ledger["units"])} source-detail gaps remain explicitly disclosed.')
class Page(HTMLParser):
 def __init__(self,text):self.ids=set();self.links=[];self.text=[];self.skip=0;super().__init__();self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('script','style'):self.skip+=1
  if a.get('id'):self.ids.add(a['id'])
  if tag in ['a','img','link','script']:
   target=a.get('href') if tag in ['a','link'] else a.get('src')
   if target:self.links.append(target)
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.skip-=1
 def handle_data(self,text):
  if not self.skip:self.text.append(text)
out=B/'_book'
if '--rendered' in sys.argv:
 pages={p:Page(p.read_text()) for p in out.rglob('*.html')}
 for p,page in pages.items():
  if re.search(r'youtu(?:be\.com|\.be)|\bvideos?\b|فيديو|تفريغ|\btranscripts?\b',' '.join(page.text+page.links),re.I):errors.append(f'{p.relative_to(out)}: rendered video reference')
  for target in page.links:
   u=urlsplit(target)
   if u.scheme or u.netloc or target.startswith('data:') or u.path.startswith('/'):continue
   dest=(p.parent/unquote(u.path)).resolve() if u.path else p
   if dest.is_dir():dest=dest/'index.html'
   if not dest.exists():errors.append(f'{p.relative_to(out)}: missing {target}')
   elif u.fragment and dest in pages and unquote(u.fragment) not in pages[dest].ids:errors.append(f'{p.relative_to(out)}: missing anchor {target}')
  for link in page.links:
   if 'github.com/mohammadwajdi19980-creator/java-learning-library/blob/main/' in link and link.endswith('.qmd') and '/books/java/' not in link:errors.append('Incorrect source link: '+link)
 epub=out/'Java-Learning-Library.epub'
 if not epub.exists():errors.append('EPUB not generated')
 else:
  with zipfile.ZipFile(epub) as z:
   if z.testzip():errors.append('EPUB archive corruption')
   names=set(z.namelist());epub_pages={}
   for name in names:
    if name.endswith('.xhtml'):
     try:
      epub_pages[name]=ET.fromstring(z.read(name))
      if re.search(r'youtu(?:be\.com|\.be)|\bvideos?\b|فيديو|تفريغ|\btranscripts?\b',z.read(name).decode(),re.I):errors.append(f'EPUB {name}: video reference')
     except ET.ParseError as e:errors.append(f'EPUB {name}: {e}')
   epub_ids={n:{e.attrib['id'] for e in root.iter() if 'id' in e.attrib} for n,root in epub_pages.items()}
   for name,root in epub_pages.items():
    for el in root.iter():
     for attr in ['href','src']:
      target=el.attrib.get(attr)
      if not target:continue
      u=urlsplit(target)
      if u.scheme or u.netloc:continue
      dest=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(u.path))) if u.path else name
      if dest not in names:errors.append(f'EPUB {name}: missing {target}')
      elif u.fragment and dest in epub_ids and unquote(u.fragment) not in epub_ids[dest]:errors.append(f'EPUB {name}: missing anchor {target}')
 g=(out/'glossary.html').read_text() if (out/'glossary.html').exists() else ''
 if len(re.findall(r'class="english-definition" dir="ltr" lang="en"',g))!=len(definitions):errors.append('Rendered glossary LTR definitions missing')
 if re.search(r'<section[^>]*dir="ltr"',g):errors.append('Arabic glossary section inherits LTR')
 if (out/'curriculum.json').exists():errors.append('Internal provenance distributed as public book data')
 if not pages:errors.append('No rendered pages')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('PASS: SVG XML, curriculum IDs, source links, status'+(', rendered links/anchors and EPUB' if '--rendered' in sys.argv else ''))
