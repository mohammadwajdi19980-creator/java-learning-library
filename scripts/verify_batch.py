"""Check published complete programs against independent sample and edge cases."""
from pathlib import Path
import json,re,subprocess,tempfile

ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'books/java'

def verify():
    specs=json.loads((ROOT/'docs/sources/code-cases-002-013.json').read_text())
    programs={}
    for p in sorted((B/'lessons').glob('lesson-*.qmd')):
        if int(p.stem.split('-')[-1])<2:
            continue
        for code in re.findall(r'```java\n(.*?)```',p.read_text(),re.S):
            m=re.search(r'public class (\w+)',code)
            if m:
                assert m[1] not in programs, f'Duplicate complete example {m[1]}'
                programs[m[1]]=(p,code)
    assert set(programs)==set(specs['programs']), 'Every complete program needs verification cases'
    count=0
    with tempfile.TemporaryDirectory() as tmp:
        for cls,(p,code) in programs.items():
            f=Path(tmp)/(cls+'.java');f.write_text(code)
            r=subprocess.run(['javac','-d',tmp,str(f)],capture_output=True,text=True,timeout=30)
            assert not r.returncode,(p,r.stderr)
            for case in specs['programs'][cls]:
                r=subprocess.run(['java','-Duser.language=en','-Duser.country=US','-cp',tmp,cls],input=case.get('input',''),capture_output=True,text=True,timeout=5)
                assert r.returncode==0,(cls,case,r.stderr)
                assert r.stdout==case['output'],(cls,case,repr(r.stdout))
                count+=1
        for case in specs['invalid_examples']:
            f=Path(tmp)/'Invalid.java';f.write_text(case['code'])
            r=subprocess.run(['javac','-d',tmp,str(f)],capture_output=True,text=True,timeout=30)
            if case['stage']=='compile':
                assert r.returncode,(case['name'],'unexpectedly compiled')
            else:
                assert r.returncode==0,(case['name'],r.stderr)
                r=subprocess.run(['java','-Duser.language=en','-Duser.country=US','-cp',tmp,'Invalid'],input=case.get('input',''),capture_output=True,text=True,timeout=5)
                assert r.returncode and case['exception'] in r.stderr,(case['name'],r.stderr)
            count+=1
    print(f'PASS: {len(programs)} new complete programs; {count} sample, boundary and intentional-error checks')

if __name__=='__main__':
    verify()
