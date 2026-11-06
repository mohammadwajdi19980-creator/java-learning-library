# Java Learning Library

A visual, Arabic-first Java textbook based progressively on 77 Adel Nasim videos. Technical terms stay in English. The same source builds the online book and EPUB.

[Read the book](https://mohammadwajdi19980-creator.github.io/java-learning-library/)

## Current scope

Two lessons are available (#00 and #01); three transcripts have been received (#00–#02). Lesson #02 has not been written. All 77 original video titles are mapped. Receipt, editorial readiness, publication, and learner mastery are separate states.

## Editing

Read [AGENTS.md](AGENTS.md), [the working guide](docs/WORKFLOW.md), and [release checklist](docs/RELEASE-CHECKLIST.md) before changes.

- `books/java/curriculum.json`: canonical video mapping and source/readiness state.
- `scripts/sync_curriculum.py`: generates Home and Contents and synchronizes navigation counts.
- `books/java/lessons/`: teaching chapters, preserving original IDs and public URLs.
- `books/java/subjects/`: Subject overviews and assessments; S01 Exam follows both lessons.
- `books/java/assets/registry.json`: image types, attribution and provenance.
- `templates/lesson.qmd`: reusable lesson template.
- `docs/AUDIT-2026-11-06.md`: historical audit, before the redesign.

## Verify and build

Use Quarto 1.11.9 and JDK 25 (Temurin in CI). The Java examples use conventional syntax supported by earlier modern JDKs too.

```bash
python3 scripts/sync_curriculum.py
python3 scripts/validate_book.py
python3 scripts/verify_java.py
quarto render books/java
python3 scripts/validate_book.py --rendered
```

Generated HTML and EPUB live in `books/java/_book/`, which is ignored by Git. GitHub Actions validates source, Java examples, rendered links/anchors, SVG files and EPUB availability before publishing main.

## Reading design

Warm background, self-hosted Arabic fonts, dark text, a short navigation, expandable local contents, English direction isolation, persistent text-size controls, book search and mobile-specific concept diagrams. Images open at full size. The default Quarto navigation remains as a fallback without JavaScript.

Authentic NetBeans Screenshots are attributed to the official tutorial and clearly identified as historical Maven examples. The lesson's step-by-step exercise uses Ant. They are not presented as Screenshots from NetBeans 31.

## Publication

The existing GitHub Pages deployment is retained. Check the live website after a successful workflow; build success alone is not proof of visual correctness. PDF is not currently offered.
