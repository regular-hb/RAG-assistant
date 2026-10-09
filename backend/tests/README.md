# Backend tests

Write tests alongside the pipeline as students implement it. Start with small,
deterministic unit tests, then add one integration test for the complete flow.
The corresponding source modules include test ideas and edge cases. Prefer tests
that assert observable behavior and metadata contracts over tests of private
implementation details.

- Ingestion: known text and page metadata, empty pages, and invalid PDFs.
- Chunking: chunk size/overlap and preservation of source and page metadata.
- Embeddings/retrieval: result count, stable metadata mapping, and empty-index behavior.
- Generation: citations refer only to supplied evidence; no-evidence questions are handled honestly.
- Evaluation: known relevant passages produce the expected ranking/grounding checks.

Use tiny, redistributable fixtures with known page-level citations. Do not commit
private or unlicensed research papers. Mock external model/vector services in
unit tests; reserve live-service tests for an explicitly configured integration
environment. Put generated indexes under a temporary test directory and verify
that a test run cannot alter a developer's local research index.