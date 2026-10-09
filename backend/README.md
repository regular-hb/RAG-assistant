# Backend Student Guide

The backend is a set of guided placeholders, not a finished RAG pipeline. The comments in each starter file describe the local task, design choices, expected behavior, and useful tests. This guide explains how the pieces fit together and what a reasonable first application should do. Students write the implementations; the scaffold intentionally does not choose a model provider or vector database for the group.

## Build in this order

1. **Ingestion** (`src/rag_assistant/ingestion/`): read papers and emit text records with stable source and page metadata.
2. **Chunking** (`ingestion/chunking.py`): split those records while retaining citation metadata on every chunk.
3. **Embeddings** (`embeddings/embedder.py`): embed chunks and questions with the same model.
4. **Storage and retrieval** (`retrieval/`): index vectors, retrieve the most relevant passages, and return text plus metadata and scores.
5. **Generation** (`generation/answerer.py`): answer using retrieved passages only and return structured citations.
6. **Evaluation** (`evaluation/metrics.py`): test retrieval and citation grounding separately from answer fluency.
7. **Application flow** (`pipeline.py`): connect ingestion and question-answering into calls the frontend can use.

## Shared data contract

Agree on a small record format before splitting work across the group. A paper page can start with `text`, `source`, `page`, and `title`. A chunk should add a stable `chunk_id` and retain the paper fields. A retrieved result should add a similarity `score`. An answer should include answer text and citations that map back to retrieved chunk IDs. Students may choose dataclasses or typed dictionaries, but use one format consistently across modules.

Use one-based page numbers in user-facing citations. Preserve the same source and chunk IDs from ingestion through retrieval and generation. Document whether a vector-store score is a distance (smaller is better) or a similarity (larger is better); do not mix those conventions.

## First application scope

Aim for a small vertical slice, not a production platform. A researcher should be able to index a few text-based PDFs, ask one question, see a concise answer with source/page citations, and get an honest no-evidence message when retrieval finds nothing. Keep uploads and the index local for the first demonstration. Scanned-paper OCR, hosted deployment, authentication, reranking, hybrid search, and sophisticated evaluation can be later extensions.

The frontend calls `pipeline.ingest_papers(...)` when documents are added and `pipeline.answer_question(...)` when a question is submitted. Those names are suggested integration boundaries, not implemented functions. Keep the UI out of extraction, embedding, prompts, and vector-store details.

## Definition of a working slice

- A small sample corpus can be ingested more than once without creating duplicate chunks.
- The group can inspect extracted text and a few chunks before embedding them.
- A question retrieves readable passages with source and page metadata.
- An answer cites only passages returned by retrieval; empty evidence produces no model-generated guess.
- A temporary-index integration test connects all stages with fake external services.
- The demo explains model/store choices, where data is stored, and the main limitations.

## Practical hints

- Start with a few short, legally shareable PDFs and print/inspect extracted text and chunks before adding a model.
- Keep page numbering consistent end to end; citations are only useful when a reader can find the page.
- Make model, embedding, and vector-store choices configurable. Keep credentials out of source files and notebooks.
- Handle empty, malformed, and no-relevant-evidence cases explicitly.
- Test each stage with deterministic inputs. Mock network services in unit tests and use a separate integration test for real providers.
- Change one stage at a time and verify its output contract before connecting the next stage.
- Start with local, text-based PDFs and one simple retrieval strategy. Add complexity only when a measured limitation motivates it.

## Student completion check

- [ ] A paper can be ingested with source and page metadata intact.
- [ ] Chunks retain enough context and provenance to cite the source.
- [ ] Query and document embeddings use compatible settings.
- [ ] Retrieval returns inspectable passages, not just scores or generated summaries.
- [ ] Answers cite retrieved evidence and acknowledge missing or conflicting evidence.
- [ ] Tests cover normal inputs and at least one failure/empty case per stage.