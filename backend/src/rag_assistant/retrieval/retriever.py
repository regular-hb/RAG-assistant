"""Student guide: coordinate query embedding and passage search."""

# This module is the boundary between a user's question and the vector store.
# It should return evidence records, not a generated answer. Keeping that split
# lets the group test retrieval quality without involving a language model.
#
# Suggested operation: retrieve(question, top_k=..., filters=None) -> list of
# Evidence records. It should: validate the question/settings, embed the query
# using embeddings/embedder.py, call vector_store.search, then return records
# ordered best-first with source/page/text/chunk_id/score intact.
#
# Start with configurable top_k and no score threshold. Similarity values are
# model/store dependent, so choose a threshold only after inspecting results on
# sample research questions. If adding deduplication, keep the best result and
# do not remove distinct passages just because their wording is similar.
#
# A high similarity score is not proof that a passage supports the question.
# Let the answer stage inspect the text, and preserve scores so evaluation can
# explain why a passage was selected. Return an empty list when nothing is
# indexed or no result is available; do not fabricate fallback evidence.
#
# Tests to write: fake embedder + fake store, confirm the question vector is
# passed through, top_k/filters are forwarded, ranking and metadata survive,
# and empty results remain empty. Stretch goal: compare semantic retrieval with
# a keyword or hybrid baseline on a small, labeled query set.