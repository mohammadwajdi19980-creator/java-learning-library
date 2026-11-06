# Java Learning Library

An Arabic-first, illustrated, **living Java textbook** created incrementally from 77 original Adel Nasim video transcripts.

**Current verified state:** 77 topic titles mapped · 13 modules · 35 subjects · 2 transcripts received (#00–#01) · 2 teaching chapters in draft/review.

## Read online

https://mohammadwajdi19980-creator.github.io/java-learning-library/

The website is generated via GitHub Actions; GitHub Pages needs to be configured with **GitHub Actions** as its publishing source. Deployment may take a short time after commits.

## Structure

- `books/java/_quarto.yml`: Quarto book navigation and publishing setup.
- `books/java/index.qmd`: visual book landing page.
- `books/java/roadmap.qmd`: complete original source lesson registry.
- `books/java/modules/`: 13 module overviews.
- `books/java/subjects/`: 35 subject overviews, **not falsely marked complete**.
- `books/java/lessons/lesson-000.qmd`: introduction lesson.
- `books/java/lessons/lesson-001.qmd`: JDK, NetBeans, first runnable project, annotated diagrams and error types.
- `books/java/subjects/s01.qmd`: completed subject-level exam with worked answers.
- `books/java/glossary.qmd`: bilingual technical glossary.
- `books/java/projects.qmd`: staged practice projects.
- `books/java/exams.qmd`: subject, module and book exam structure.

## Build locally

Install [Quarto](https://quarto.org/docs/get-started/), then run:

```bash
quarto render books/java
```

This builds HTML and EPUB under `books/java/_book/`. PDF requires a later Arabic-aware PDF render profile and fonts and is not yet advertised as available.

## Editorial rules

1. Keep original IDs (`#00`–`#076`) and source title mappings.
2. Natural spoken-style Arabic explanation; put technical English terms in separate text blocks or code spans.
3. Explain WHY → WHAT → HOW → verified example → visual → exercises → exam/project.
4. Label supplemental explanations separately; never invent unseen video material.
5. True NetBeans screenshots only, never fabricated screenshots described as real.
6. Write readable accessible visual diagrams as inline or linked SVG assets.
7. Keep the glossary cumulative and bilingual.

This project is free/open-source and runs on GitHub Pages. 
