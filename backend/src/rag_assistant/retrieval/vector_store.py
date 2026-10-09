"""Student guide: persist chunk vectors and return their source evidence."""

# Choose one vector store for the MVP. A local store is easy to demonstrate and
# recreate; a hosted store adds deployment, credentials, and network failure
# concerns. Document installation, where its index files live, and how students
# can rebuild a corrupted or stale index. Do not commit generated index files.
#
# Suggested operations (students define the exact signatures):
# - add_chunks(chunks, vectors): insert or update by stable chunk_id.
# - search(vector, top_k): return ranked records with text, metadata, and score.
# - clear_index(): remove generated records for a clean rebuild/test.
# Keep the vector-store library behind this module; callers should not depend on
# a vendor SDK's result object or SQL/schema conventions.
#
# Data invariant: each vector remains paired with the exact chunk text and
# metadata that produced it. Persist source, page, title, and chunk_id as fields
# that can be filtered/displayed. Store the embedding-model identity and
# dimension with the index so incompatible vectors are not mixed accidentally.
#
# Handle a not-yet-created or empty index, duplicate IDs, wrong vector lengths,
# and failed writes explicitly. Similarity scores may be distances (lower is
# better) or similarities (higher is better); normalize/document that convention
# before the retriever sorts or applies a threshold.
#
# Tests to write: add/search round trip, stable ID updates, empty search, top-k
# ordering, metadata retention, and dimension mismatch. Use a temporary index
# directory so tests never touch a student's real paper collection.