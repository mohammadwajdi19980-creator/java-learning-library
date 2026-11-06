# Java Learning Library — Working Guide

Version 1.1 · 6 November 2026

The user has authorized implementation and publication of the audit fixes and appearance redesign. The earlier analysis-only limit was specific to the audit turn. Preserve original video IDs, Arabic explanations, English technical terminology, and source coverage.

Read AGENTS.md and this guide before changes. The original findings remain in AUDIT-2026-11-06.md; they are a historical snapshot.

## 4. Proposed information structure

Use a consistent content hierarchy:

Book → Module → Subject → Lesson → Topic.

“Lesson” means a teaching chapter. “Java Class” means a Java code construct. Never use them interchangeably in records.

Recommended learner-facing navigation:

- Home: clear starting point, accurate readiness, direct access to available lessons.
- Contents: Modules and Subjects containing their available lessons.
- Within a lesson: compact section navigation, Previous/Next, related terms, and practice.
- Subject Review/Exam: after its constituent lessons.
- Module Review/Exam/Project: after the Module's prerequisites.
- Glossary, Projects, Sources, and full Roadmap: supporting destinations.
- Planned lessons: visible as planned in the Roadmap without presenting them as completed reading.

Preserve original video IDs and existing public lesson URLs. Separate the original video title from an editorial title. If URLs ever change, map old destinations deliberately.

The broader 523-topic Java_Master_Topic_Index includes other uploaded university and Swing/JDBC material as well as the video course. Treat it as a separate scope layer; do not silently claim that all 523 topics belong to the 77 videos.

## 5. Terminology and direction contract

- Keep technical names in English everywhere: Class, Object, Method, Constructor, Package, Array, Inheritance, Interface, Compiler, Source Code, Bytecode, JVM, and so on.
- Explain their meaning in Arabic, without replacing their names with Arabic technical labels.
- Put a main term on its own English heading or label, followed by the Arabic explanation.
- Use LTR direction and bidirectional isolation for inline English where an inline occurrence is necessary.
- Code, commands, filenames, API names, mathematical expressions, and Output remain LTR.
- Keep capitalization and spelling exact. Class differs from the keyword class; Method differs from a method name.
- Expand abbreviations once when useful. Keep one preferred term and a record of aliases.
- The Glossary may contain Arabic explanations and concise English definitions. English terms remain the entry names.
- Apply this rule to the entire product, including diagrams, alternative text where terms occur, captions, navigation, Exams, and tooltips.

## 6. Workflow before every action

1. Read this guide and the latest task; identify whether the request authorizes analysis, content edits, design changes, or publication.
2. Inspect current repository HEAD and affected files. Check existing work before deciding what to change.
3. Read the relevant transcript/source and existing lesson, Glossary, status, and assets.
4. Define the smallest coherent change and its acceptance conditions.
5. Preserve unrelated work, stable IDs, source provenance, and existing links.
6. Use the applicable workflow below.
7. Review the affected content and rendered experience.
8. Report only what actually happened: source received, draft prepared, checked, committed, deployed, and live verified are distinct facts.

For future implementation, use a reviewable branch/PR where appropriate and avoid publishing incomplete work through an incidental push to main. Do not introduce repeated permission questions for routine work already authorized.

## 7. Workflow for every new Lesson

1. Register the video ID, original title, source link, supplied transcript reference, timestamps, and language.
2. Preserve the original transcript. Correct a working copy; mark uncertain words rather than reconstructing them as quotes.
3. Inventory distinct concepts, conditions, examples, exercises, and visual demonstrations. Map each to its place in the lesson.
4. Identify prerequisites. Explain only the necessary bridge without assuming knowledge not yet taught.
5. Draft the lesson in a stable structure: purpose/prerequisites; concept sections; relevant visual; explanation; full example and Output; trace; mistakes; practice; answers; brief review; source/addition notes.
6. Put a relevant image directly before the explanation it supports where that helps the learner. Do not gather all images at the end.
7. Preserve original examples. Label new examples and current-version updates as additions.
8. Verify uncertain technical claims using primary documentation; record versions and verification dates for installation instructions.
9. Run complete code examples in the stated environment when possible. Record inspected-only examples honestly.
10. Audit terminology, Arabic/English direction, source coverage, code, and Output.
11. Update the Glossary, relationships, navigation, status, and affected Subject/Module/Exam links together.
12. Preview, inspect, and publish only within the authorized scope. Reopen the live page before reporting it as verified.

A compact source-coverage record should map transcript location → concept/example → lesson section → status/gap. A missing or unclear source item remains explicit.

## 8. Workflow for every Java Class or code example

- State the task, required behavior, file names, Package, and relevant JDK.
- Show the full runnable example first when teaching a complete solution.
- Then explain the important lines and execution steps in relation to the question.
- Keep UML and code identifiers consistent, including visibility, types, parameters, and relationships.
- Specify inputs, expected Output, and the reason for each non-obvious step.
- Compile and run meaningful normal cases and relevant boundary/error cases.
- Label intentionally invalid examples and the type of error expected.
- Do not claim every fragment is independently runnable or that a successful Build proves correct logic.
- Record whether verification occurred in a CLI, NetBeans, or by inspection. These are different claims.
- Keep exam questions and all their conditions intact; provide complete solutions and reasons.

## 9. Workflow for every image

1. Define the learning purpose and exact lesson section.
2. Choose the format: genuine Screenshot for software UI; precise SVG/Mermaid/UML for exact relationships; image generation for an illustration when useful.
3. Use English technical labels and exact code. Generated code/text must be checked.
4. For Screenshots, record origin, application/version, and step. Annotate actual controls without inventing UI.
5. Give the asset a stable lesson-scoped identifier and filename.
6. Record type, source/rights basis, caption, alternative text, owner lesson, and validation status.
7. Validate SVG XML and file references; inspect for clipped text, incorrect arrows, tiny labels, and low contrast.
8. Inspect the image at its actual desktop and mobile display sizes. Split dense images instead of shrinking them.
9. Place it with the explanation and provide a text equivalent for the essential information.
10. Confirm that it loads on the published site and, when exported, in EPUB.

No placeholder or broken visual may be counted as a delivered explanatory image.

## 10. Workflow for design, navigation, or structure changes

- State the reading problem and concrete success condition.
- Use shared typography, spacing, colors, and components.
- Keep a comfortable reading column with a collapsible main navigation and compact local navigation.
- Avoid duplicate headings, tiny status decorations, unnecessary panels, and long wrapped sidebar labels.
- Test Arabic prose, standalone English terms, inline identifiers, code, tables, and diagrams.
- Inspect representative widths around 390, 768, and 1366 pixels, plus enlarged text/zoom and keyboard focus.
- Check overflow, menu behavior, heading visibility, reading sequence, Previous/Next, search, source links, and downloads.
- Review affected existing lessons, not only the new component.
- Do not call a redesign complete based only on source code or a Build log.

## 11. Status and release rules

Maintain independent fields for source receipt, editorial readiness, publication, visual verification, and learner mastery.

Suggested editorial states: Awaiting Source → Source Received → Draft → Reviewed → Ready to Publish.

Track deployment separately: Not Deployed / Deployment Running / Deployment Failed / Published. Add the commit, URL, and time of live verification.

Reading a lesson does not establish mastery. A Published lesson can still require corrections.

A future canonical curriculum registry should include:

- lesson ID; original title; editorial title; Module/Subject
- transcript/source reference; timestamps; uncertainties
- editorial status; prerequisites; Glossary entries
- asset IDs; exercise/Exam links; code verification
- published URL; commit; live-check result

Generate counts and summaries from this registry instead of hardcoding them on several pages.

Release check:

- Source coverage and terminology checked.
- Relevant code verified or clearly marked inspected-only.
- Images valid and rendered.
- Navigation and internal/source links resolve.
- Progress statements agree.
- HTML builds; EPUB is checked when part of the release.
- Desktop/mobile reading checked as appropriate.
- Deployment succeeds for the intended commit.
- Published pages are reopened and inspected.

Do not report “everything works” when only deployment succeeded.

## 12. Proposed repository maintenance records

These are recommendations, not files added to GitHub in this analysis.

- A short contributor/agent entrypoint linking to this working guide.
- A lesson template.
- A canonical curriculum/source registry.
- An asset registry.
- A source-to-lesson coverage record.
- A reusable release checklist.

Keep user-facing pages focused on learning; contributor details belong in maintenance documentation.


## Current implementation

- curriculum.json drives public receipt and readiness summaries.
- sync_curriculum.py generates Home and Contents from that registry.
- assets/registry.json records visual provenance.
- templates/lesson.qmd is the starting structure for future lessons.
- validate_book.py checks SVG, IDs, source references, rendered links and anchors.
- verify_java.py compiles and runs complete examples and intentional error cases.
- HTML includes a compact custom navigation, local Contents, text scaling, search and mobile diagrams.
- Genuine official NetBeans Screenshots are identified as historical Maven tutorial images; the lesson uses Ant.
- GitHub Actions validates before deployment. Browser inspection remains a separate release step.

Use RELEASE-CHECKLIST.md. Update this guide when requirements or workflow change. Future sessions must read repository instructions; automatic cross-chat memory is not guaranteed.
