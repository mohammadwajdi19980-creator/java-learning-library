# Lesson #00 — Machine Language and introductory clarity

Base HEAD: ce9819f004f22684ba30c924f0eb94059b715521.

## Changes

- Restored the missing Binary/Machine Language bridge: Computer and Processor, instructions, Binary data versus executable encodings, High-Level Languages, Source Code, javac, Bytecode, JVM, and native Machine Code.
- Binary `00000101` is explicitly an unsigned integer data example representing 5, not a CPU print instruction or a translation of Main.java.
- Clarified that Main.class is a File containing Bytecode and metadata. Interpreter and optional JIT roles are brief and differentiated; not every instruction is asserted to require JIT.
- Repaired desktop and mobile execution figures. Main.java/Main.class and Output Java agree with the complete runnable example. Removed the arbitrary bit string and a shadow filter that hid card backgrounds in the EPUB-oriented rasterization check.
- Added precise Binary/Machine Language desktop/mobile diagrams. Online source imagery was researched first; the Oracle security diagram includes unrelated class loading/verification details and does not match this example. Existing and new SVGs use the exact-diagram exception; none are genuine IDE Screenshots.
- Restored the Security/Encryption use case, defined the names Library/Framework and UI tools briefly, retained qualified Java platform uses and compatibility, and replaced mixed-language headings with English headings.
- All inline English technical names in this Lesson use code isolation or separate English labels. Arabic explanations retain the shared RTL layout.
- Added 16 bilingual English-LTR Glossary entries (139 total); updated S01 assessment questions within the same 20 marks. Added 23 explicit source coverage units; the archive is an editorial inventory, not a verbatim transcript.
- Lesson readiness remains 27/77. Scope is the first Lesson and its immediate references and assessment.

## Validation

- Source validation passed: terminology, source archive hashes, registered SVG XML, and all coverage headings.
- All four revised/new diagram variants rasterized and visually inspected. Machine Code is attached to Processor; Bytecode to JVM. Output matches Java.
- Java checks passed with JDK 25: five original full programs and intentional failures, plus 45 complete batch programs and 173 sample/boundary/error checks. Main.java still prints exactly `Java` plus a newline.
- Quarto HTML and EPUB generated; rendered validation passed for all links/anchors, EPUB chapter/resource integrity and 139 English LTR definition blocks.
- Published desktop browser review completed; observations follow below.

## Publication

Content commit: `d62d358143272b46374c352368bca7404915d236`. GitHub Actions run `42490067279` completed successfully, including source/Java checks, full HTML/EPUB Build, rendered validation and Pages deployment.

Live browser verification completed 2026-11-08T17:37:06+03:00:

- The published introduction now contains Binary, Machine Language, Programming Languages, Interpreter/JIT and Processor sections, plus the restored Security/Encryption paragraph.
- Machine Language explanation was visually inspected in the actual lesson. All section headings in Lesson #00 are English.
- Both the Binary illustration and repaired execution illustration were opened through their published zoom links and visually inspected. The execution figure shows Main.java, Main.class, Processor/Machine Code, and Output Java.
- The Related Terms link opens the Machine Language Glossary entry; the English definition is visually LTR and left aligned.
- S01 displays the revised High-Level Languages/Binary/Machine Language question and the native Processor execution question. Marks stay 20.
- Final verified URL: https://mohammadwajdi19980-creator.github.io/java-learning-library/lessons/lesson-000.html#machine-language

Limit: desktop browser inspection plus rasterized desktop/mobile SVG variants; no new true mobile viewport test is claimed. Shared responsive CSS and JS were unchanged.
