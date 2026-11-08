"""Generate public curriculum/status views from one canonical registry."""
from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'books/java'
data=json.loads((B/'curriculum.json').read_text())
lessons=data['lessons'];available=sum(x['editorial_status']=='reviewed' for x in lessons);received=sum(x['source_status']=='received' for x in lessons)
ready=[x for x in lessons if x['editorial_status']=='reviewed' and x['url']]
module_cards=['<div class="module-grid">']
for m in data['modules']:
 group=[x for x in ready if x['module']==m['id']]
 if not group:continue
 all_group=[x for x in lessons if x['module']==m['id']]
 label='Complete' if len(group)==len(all_group) else 'In progress'
 module_cards += [f'<section class="module-card"><p class="eyebrow" dir="ltr">{m["id"]} · {label} · {len(group)} / {len(all_group)} lessons</p><h3 dir="ltr"><a href="modules/{m["id"].lower()}.html">{html.escape(m["title"])}</a></h3><ul>']
 for s in data['subjects']:
  subset=[x for x in group if x['subject']==s['id']]
  if subset:module_cards += [f'<li><a href="subjects/{s["id"].lower()}.html">{s["id"]} · {html.escape(s["title"])}</a><small>{" / ".join(x["source_id"] for x in subset)}</small></li>']
 module_cards += ['</ul></section>']
module_cards+=['</div>']
next_lesson=next((x for x in lessons if x['editorial_status']!='reviewed'),None)
next_html=''
if next_lesson:
 state='Source received' if next_lesson['source_status']=='received' else 'Not yet available'
 arabic='المادة بانتظار الكتابة والمراجعة.' if next_lesson['source_status']=='received' else 'هذا الدرس مخطط له؛ صفحته ستتاح بعد الكتابة والمراجعة.'
 next_html=f'<section class="next-chapter"><span class="next-number" aria-hidden="true">{next_lesson["id"]:02}</span><div><p class="eyebrow" dir="ltr">UP NEXT</p><h2 dir="ltr">{html.escape(next_lesson["original_title"])}</h2><p>{arabic}</p></div><span class="pending-label">{state}</span></section>'
epub_contents=[]
for m in data['modules']:
 group=[x for x in ready if x['module']==m['id']]
 if not group:continue
 epub_contents += [f'## {m["id"]} · {m["title"]}','']
 for x in group:epub_contents += [f'- [{x["source_id"]} · {x.get("display_title",x["original_title"])}](lessons/lesson-{x["id"]:03}.qmd)']
 epub_contents += ['']
home=(ROOT/'scripts/home.template.qmd').read_text().replace('{{AVAILABLE}}',str(available)).replace('{{RECEIVED}}',str(received)).replace('{{MODULE_CARDS}}','\n'.join(module_cards)).replace('{{NEXT_LESSON}}',next_html).replace('{{EPUB_CONTENTS}}','\n'.join(epub_contents))
(B/'index.qmd').write_text(home)
shell=B/'includes/shell.html'
text=shell.read_text()
import re
text=re.sub(r'\d+ / 77 lessons available',f'{available} / 77 lessons available',text)
nav=['<!-- curriculum-navigation:start -->']
for m in data['modules']:
 group=[x for x in ready if x['module']==m['id']]
 if not group:continue
 nav += [f'<details class="nav-module" data-module="{m["id"]}"'+(' open' if m['id']=='M01' else '')+f'><summary><span>{m["id"]}</span>{html.escape(m["title"])}</summary><nav class="lesson-nav" aria-label="{m["id"]} lessons">']
 for s in data['subjects']:
  subset=[x for x in group if x['subject']==s['id']]
  if not subset:continue
  for x in subset:
   nav += [f'<a data-book-path="{x["url"]}"><span>{x["id"]:02}</span>{html.escape(x.get("display_title",x["original_title"]))}</a>']
  all_subset=[x for x in lessons if x['subject']==s['id']]
  caption='Review & Exam' if len(subset)==len(all_subset) else 'Partial Review'
  nav += [f'<a class="subject-review-link" data-book-path="subjects/{s["id"].lower()}.html"><span>{s["id"]}</span>{caption}</a>']
 nav += ['</nav></details>']
nav+=['<!-- curriculum-navigation:end -->']
if '<!-- curriculum-navigation:start -->' in text:
 text=re.sub(r'<!-- curriculum-navigation:start -->.*?<!-- curriculum-navigation:end -->','\n'.join(nav),text,flags=re.S)
else:
 text=re.sub(r'<div class="nav-section-label">M01.*?</nav>','\n'.join(nav),text,flags=re.S,count=1)
shell.write_text(text)
out=['---','title: "Contents"','subtitle: "كل الدروس، وحالة كل صفحة"','format:', '  html:', '    toc: false','---','','<p class="roadmap-intro">هذا فهرس دروس الكتاب. افتح أي Module لرؤية مواضيعه وصفحات الدروس المتاحة؛ الدروس المخططة لم تكتمل بعد.</p>',f'<p class="book-state">{available} lessons available · 77 lessons planned</p>','','::: {.content-visible unless-format="epub"}','']
for m in data['modules']:
 group=[x for x in lessons if x['module']==m['id']]
 out+=['<details class="roadmap-module"'+(' open=""' if m['id']=='M01' else '')+'>','<summary>'+html.escape(m['id']+' / '+m['title'])+'</summary>','<div class="module-content">']
 for s in data['subjects']:
  subset=[x for x in group if x['subject']==s['id']]
  if not subset:continue
  out+=['<h3><a href="subjects/'+s['id'].lower()+'.html">'+html.escape(s['id']+' · '+s['title'])+'</a></h3>','<ul>']
  for x in subset:
   label=html.escape(x['source_id']+' — '+x['original_title'])
   if x['url']:label='<a href="'+x['url']+'">'+label+'</a>'
   state='Available' if x['url'] else ('Source received · Lesson not written' if x['source_status']=='received' else 'Not yet available')
   out+=['<li>'+label+'<span class="source-state">'+state+'</span></li>']
  out+=['</ul>']
 out+=['</div>','</details>','']
out+=[':::','','::: {.content-visible when-format="epub"}','',*epub_contents,'','بقية الدروس غير متاحة بعد؛ هذا الفهرس يسرد الصفحات المتاحة فقط.','',':::']
(B/'roadmap.qmd').write_text('\n'.join(out)+'\n')
for m in data['modules']:
 group=[x for x in lessons if x['module']==m['id']]
 done=[x for x in group if x['editorial_status']=='reviewed' and x['url']]
 count_received=sum(x['source_status']=='received' for x in group)
 state='Complete' if len(done)==len(group) else ('In progress' if done else 'Planned')
 lines=['---',f'title: "{m["id"]} · {m["title"]}"','---','',f'<div class="lesson-meta"><span>{state}</span><span>{len(done)} / {len(group)} lessons available</span><span>{len(group) - len(done)} lessons remaining</span></div>','', '## Subjects','']
 for s in data['subjects']:
  subset=[x for x in group if x['subject']==s['id']]
  if not subset:continue
  ready_sub=[x for x in subset if x in done]
  lines += [f'### {s["id"]} · {s["title"]}', '', f'[Open Subject](../subjects/{s["id"].lower()}.qmd)','']
  for x in subset:
   label=f'{x["source_id"]} · {x.get("display_title",x["original_title"])}'
   if x in done:lines += [f'- [{label}](../lessons/lesson-{x["id"]:03}.qmd)']
   else:lines += [f'- {label} — '+('Source received · Not yet reviewed' if x['source_status']=='received' else 'Not yet available')]
  lines += ['', 'Review & Exam متاح بعد الدروس المذكورة.' if len(ready_sub)==len(subset) else 'هذا Subject لم يكتمل بعد؛ المراجعة تقتصر على الدروس المتاحة.', '']
 if done:
  lines+=['## Reading Path','',f'ابدأ من [{done[0]["source_id"]}](../lessons/lesson-{done[0]["id"]:03}.qmd)، وراجع كل Subject بعد دروسه. اتبع Previous / Next للتقدّم بالترتيب.','']
 if m['id']=='M05' and len(done)==len(group):
  lines+=['## Module Assessment', '', '[M05 Exam & Math Utilities Project](../assessments/m05.qmd)', '']
 (B/'modules'/f'{m["id"].lower()}.qmd').write_text('\n'.join(lines))
print(f'Curriculum: {available} available, {received} transcripts, {len(lessons)} mapped.')
