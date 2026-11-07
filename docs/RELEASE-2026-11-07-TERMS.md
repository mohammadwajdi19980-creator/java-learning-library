# Terminology, Glossary direction, and web-book references

## Scope

- Reviewed all 14 available Lessons, all 35 Subjects, generated Module/Contents/Home pages, and the 57-entry Glossary.
- Technical names stay English, including Text Editor, Code Editor, Variable, Local Variable, Expression, Assignment, Loop, Counter, Project, and Build System. Arabic explanations remain Arabic.
- All 57 English definitions have static LTR language/direction blocks with left alignment in HTML and EPUB. English term labels are explicitly isolated; Arabic paragraphs keep RTL.
- Public references now point to existing Lesson/Subject pages. Removed video labels, video URLs, timestamps, viewing references, and transcript status from learner-facing pages. Original source IDs/provenance remain in internal records; curriculum.json is no longer a distributed resource.
- Added checks for translated technical names, video references, and missing LTR definition blocks. Preserved every fenced teaching example and all 122 source-coverage references.

## Validation

- Source validation passed.
- 5 original complete programs and intentional failures passed.
- 17 additional complete programs passed 59 sample, boundary, and intentional-error checks.
- Full 68-page HTML/EPUB build passed; rendered links/anchors and EPUB integrity passed. All public HTML/EPUB scanned: zero video references, 57 explicit LTR definitions, no LTR inheritance on Arabic sections.
- Live verification passed after successful workflow 42350978341 for commit 1f8a8dcde66dc7faaf651b0856939b5864a691e8. All 57 English definitions computed LTR/left; Arabic paragraphs computed RTL/right. Checked 1363px desktop and 454px narrow layout, no horizontal overflow, mobile menu, Text Editor search results, Lesson 01 page links, and Subject S02 English terminology. Refreshed Glossary confirmed the final Character terminology pass.
