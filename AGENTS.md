# Java Learning Library

Read docs/WORKFLOW.md before each action. Use books/java/curriculum.json as the source of truth for lesson receipt and readiness. Do not infer new source content from a title.

- Explain in Arabic; preserve technical terms in English throughout the product.
- Keep explanations concise but comprehensive and within Adel Nasim's supplied topics/talking points. Read multi-topic batches fully and preserve their sequence and coverage.
- Source educational imagery online first, including accurate YouTube frames; use ImageGen only when no suitable image is found. Match and verify the exact concept; label generated illustrations and never present them as genuine Screenshots. Follow docs/WORKFLOW.md for provenance and fidelity checks.
- Keep original source IDs and URLs stable in internal provenance records. Learner-facing pages link to the book’s Lesson/Subject pages and contain no video references.
- Place lessons before their Exam in the reading sequence.
- Preserve code, source examples and coverage; label additions and uncertainties.
- Genuine Screenshots require provenance. Schematics must be identified.
- Register each image in books/java/assets/registry.json. Validate SVG XML.
- Use the existing reading controls and shared styles; no appended competing design systems.
- Run scripts/sync_curriculum.py, scripts/validate_book.py, scripts/verify_java.py with a JDK, then Quarto and scripts/validate_book.py --rendered.
- Inspect desktop and mobile rendering, links, menu, text scaling, images, and search.
- A successful deployment is distinct from verified live frontend behavior.
- Update the guide and release record for meaningful changes. Do not promise automated recall or tests that do not exist.
