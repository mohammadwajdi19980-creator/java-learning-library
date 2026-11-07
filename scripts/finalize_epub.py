"""Resolve source-relative links left behind by Quarto's EPUB writer.

The source order is checked against the actual EPUB chapter titles before any
rewrite. HTML and already-resolved EPUB links are left untouched.
"""
from pathlib import Path
import html,posixpath,re,zipfile,xml.etree.ElementTree as ET
from urllib.parse import urlsplit,unquote

ROOT=Path(__file__).resolve().parents[1];B=ROOT/'books/java'
epub=B/'_book/Java-Learning-Library.epub'

def finish():
    if not epub.exists():
        return
    config=(B/'_quarto.yml').read_text()
    source_paths=re.findall(r'^\s+- ((?:[\w-]+/)?[\w-]+\.qmd)\s*$',config,re.M)
    ns={'h':'http://www.w3.org/1999/xhtml'}
    with zipfile.ZipFile(epub) as z:
        entries={i.filename:(i,z.read(i)) for i in z.infolist()}
    chapters=sorted(n for n in entries if re.fullmatch(r'EPUB/text/ch\d+\.xhtml',n))
    assert len(source_paths)==len(chapters),(len(source_paths),len(chapters))
    mapping={};ids={}
    for source,name in zip(source_paths,chapters):
        root=ET.fromstring(entries[name][1])
        h1=root.find('.//h:h1',ns)
        assert h1 is not None, name
        actual=re.sub(r'^(?:\d+\s*|Appendix [A-Z] —\s*)','', ''.join(h1.itertext())).strip()
        text=(B/source).read_text()
        match=re.search(r'^title:\s*"([^"]+)"',text,re.M) or re.search(r'^# (.+)$',text,re.M)
        assert match,source
        expected=html.unescape(match[1]).strip()
        assert actual==expected,('EPUB source/chapter order mismatch',source,actual,expected)
        mapping[source]=name
        ids[name]={e.attrib['id'] for e in root.iter() if 'id' in e.attrib}
    changed=0
    for source,name in mapping.items():
        content=entries[name][1].decode()
        def replace(m):
            nonlocal changed
            target=html.unescape(m[1]);u=urlsplit(target)
            if u.scheme or not u.path.endswith('.qmd'):
                return m[0]
            dest=posixpath.normpath(posixpath.join(posixpath.dirname(source),unquote(u.path)))
            assert dest in mapping,('Unknown EPUB source target',source,target)
            target_name=mapping[dest]
            fragment=unquote(u.fragment)
            if fragment and fragment not in ids[target_name]:
                matches=[i for i in ids[target_name] if re.fullmatch(re.escape(fragment)+r'-\d+',i)]
                assert len(matches)==1,('Unknown EPUB anchor',dest,fragment,matches)
                fragment=matches[0]
            href=posixpath.relpath(target_name,posixpath.dirname(name))
            if fragment:href+='#'+fragment
            changed+=1
            return 'href="'+html.escape(href,quote=True)+'"'
        content=re.sub(r'href="([^"]+)"',replace,content)
        info,_=entries[name];entries[name]=(info,content.encode())
    if changed:
        temp=epub.with_suffix('.epub.tmp')
        with zipfile.ZipFile(temp,'w') as z:
            for info,data in entries.values():z.writestr(info,data)
        temp.replace(epub)
    print(f'EPUB: validated chapter mapping; resolved {changed} source-relative links')

if __name__=='__main__':
    finish()
