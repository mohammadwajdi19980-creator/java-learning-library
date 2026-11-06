"""Compile and execute the complete teaching examples; check intentional errors."""
from pathlib import Path
import re,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'books/java'
expected={'Main':'Java\n','WelcomeApp':'My name is Sara\nI am learning Java\n5\n','StartApp':'Welcome\n'}
count=0
with tempfile.TemporaryDirectory() as tmp:
 for name in ['lessons/lesson-000.qmd','lessons/lesson-001.qmd','subjects/s01.qmd']:
  for code in re.findall(r'```java\n(.*?)```',(B/name).read_text(),re.S):
   m=re.search(r'public class (\w+)',code)
   if not m or 'public static void main' not in code or 'system.out' in code:continue
   cls=m[1];file=Path(tmp)/(cls+'.java');file.write_text(code)
   subprocess.run(['javac','-d',tmp,str(file)],check=True,capture_output=True)
   pkg=re.search(r'package (\w+);',code);full=(pkg[1]+'.' if pkg else '')+cls
   out=subprocess.run(['java','-cp',tmp,full],check=True,capture_output=True,text=True).stdout
   want=expected.get(cls)
   if cls=='FirstProgram':want='I am learning Java.\nMy first project works!\n3\n' if 'My first project' in code else 'Hello, Java!\n'
   assert out==want,(cls,out,want)
   count+=1
 file=Path(tmp)/'Failure.java';file.write_text('class Failure { public static void main(String[] args) { int number=0; System.out.println(10/number); }}')
 subprocess.run(['javac',str(file)],check=True)
 r=subprocess.run(['java','-cp',tmp,'Failure'],capture_output=True,text=True);assert r.returncode and 'ArithmeticException' in r.stderr
 file.write_text('class Failure { public static void main(String[] args) { System.Out.println("Hello"); }}')
 assert subprocess.run(['javac',str(file)],capture_output=True).returncode
print(f'PASS: {count} full programs and intentional compile/runtime failures')
