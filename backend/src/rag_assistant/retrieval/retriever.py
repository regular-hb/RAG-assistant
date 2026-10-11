"""Simple notes for searching the best passages for a question."""

# This module turns a user question into a vector search.
# It should return evidence, not an answer.
#
# Steps:
# - check the question and settings
# - turn the question into an embedding
# - ask the vector store for similar chunks
# - return the best matches in order
#
# Keep the score and metadata with each result.
# If no passages are found, return an empty result instead of making up answers.
#
# Good tests include: fake embedder + fake store, ranked results, empty results,
# and checks that filters and top_k are passed through correctly.