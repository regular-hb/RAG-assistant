"""Student guide: compose the backend stages into one application workflow."""

# This is the application-level boundary the Streamlit frontend will call. It
# should coordinate modules, not contain PDF parsing, vector math, prompts, or
# provider-specific logic itself.
#
# Suggested public operations:
# - ingest_papers(paths): documents -> chunks -> embeddings -> vector store.
# - answer_question(question, top_k=...): retrieve -> generate -> Answer record.
# Agree on exact arguments/return types with the frontend before implementation.
#
# Ingestion workflow responsibilities:
# 1. Validate the uploaded paths and call ingestion/documents.py.
# 2. Pass extracted page records to ingestion/chunking.py.
# 3. Embed the chunks and add text, vectors, and metadata to vector_store.py.
# 4. Return a small summary (papers/pages/chunks indexed and any per-file errors)
#    so the UI can tell the researcher what happened.
# Make reruns safe: stable chunk IDs should update existing records rather than
# add duplicates. Do not report success if indexing failed partway through.
#
# Question workflow responsibilities:
# 1. Validate that the question is non-empty and the index is available.
# 2. Ask retrieval/retriever.py for evidence, with configurable top_k.
# 3. If no evidence is found, return a clear no-evidence result without calling
#    a language model. Otherwise call generation/answerer.py.
# 4. Return answer text, citations, and enough retrieval metadata for the UI to
#    display and debug the result.
#
# Keep configuration (model names, index path, provider credentials) outside
# this module and inject dependencies where practical. Convert expected errors
# into useful messages at the application boundary, but do not hide unexpected
# programming errors during development. Never pass secrets to the frontend.
#
# Integration tests should use a temporary index and fake model/embedder clients
# to exercise both workflows end to end without network access or real papers.