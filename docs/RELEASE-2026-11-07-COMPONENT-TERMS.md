# Technical component/tool names stay English

Expanded the terminology policy to cover technical components and tools by category, including Server, Browser, Processor, Operating System, Libraries, Framework, Namespace, File, Folder, Keyboard, Input, Output, Initialization, and Statement. Arabic prose remains explanatory; technical names remain English throughout Lessons, Subjects, captions, and Glossary.

Added scripts/technical_terms.json with checked Arabic aliases, including Server aliases, so the existing source validator catches reintroductions. Preserved all fenced teaching examples and 122 coverage references. Corrected two awkward sentences left by the earlier terminology pass without adding new topics.

Source validation passed. Java example checks, full HTML/EPUB rendering, deployment, and live verification are recorded below when complete.

## Verified release

- Local source and full 68-page HTML/EPUB checks passed; no checked Arabic component/tool aliases remained in rendered pages or EPUB. SVG labels were also scanned.
- 5 original programs and intentional failures passed; 17 additional programs passed 59 sample, boundary, and intentional-error checks.
- Workflow 42352643195 succeeded for commit 6a6cdb130decd2ca0d2b124030244d749520f333 and published the site.
- Live Lesson 00 confirmed Server, Browser, Processor, Operating System, Libraries, and Framework, with no tested translated aliases or video references. Inspected desktop at 1363px and narrow view at 454px: no page overflow and all images loaded. Restored desktop view.
