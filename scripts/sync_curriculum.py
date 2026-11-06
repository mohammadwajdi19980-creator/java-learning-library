"""Generate public curriculum/status views from one canonical registry."""
from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'books/java'
data=json.loads((B/'curriculum.json').read_text())
lessons=data['lessons'];available=sum(x['editorial_status']=='reviewed' for x in lessons);received=sum(x['source_status']=='received' for x in lessons)
home=(ROOT/'scripts/home.template.qmd').read_text().replace('{{AVAILABLE}}',str(available)).replace('{{RECEIVED}}',str(received))
(B/'index.qmd').write_text(home)
shell=B/'includes/shell.html'
text=shell.read_text()
import re
text=re.sub(r'\d+ / 77 lessons available',f'{available} / 77 lessons available',text)
shell.write_text(text)
out=['---','title: "Contents"','subtitle: "كل الفيديوهات، وحالة كل درس"','format:', '  html:', '    toc: false','---','','<p class="roadmap-intro">هذا فهرس الفيديوهات الأصلية، وليس ادعاءً بأن الكتاب اكتمل. افتح أي Module لرؤية مواضيعه. أسماء المصدر محفوظة كما وردت؛ الشرح يُضاف بعد استلام النص ومراجعته.</p>',f'<p class="book-state">{available} lessons available · {received} transcripts received · 77 videos mapped</p>','']
for m in data['modules']:
 group=[x for x in lessons if x['module']==m['id']]
 out+=['<details class="roadmap-module"'+(' open' if m['id']=='M01' else '')+'>','<summary>'+html.escape(m['id']+' / '+m['title'])+'</summary>','<div class="module-content">']
 for s in data['subjects']:
  subset=[x for x in group if x['subject']==s['id']]
  if not subset:continue
  out+=['<h3><a href="subjects/'+s['id'].lower()+'.html">'+html.escape(s['id']+' · '+s['title'])+'</a></h3>','<ul>']
  for x in subset:
   label=html.escape(x['source_id']+' — '+x['original_title'])
   if x['url']:label='<a href="'+x['url']+'">'+label+'</a>'
   state='Available' if x['url'] else ('Source received · Lesson not written' if x['source_status']=='received' else 'Awaiting transcript')
   out+=['<li>'+label+'<span class="source-state">'+state+'</span></li>']
  out+=['</ul>']
 out+=['</div>','</details>','']
(B/'roadmap.qmd').write_text('\n'.join(out)+'\n')
print(f'Curriculum: {available} available, {received} transcripts, {len(lessons)} mapped.')
