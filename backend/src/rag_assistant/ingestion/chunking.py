"""Student guide: split page records into searchable, citable passages."""

# Input: the PageRecord values from documents.py. Output: Chunk records with at


# least chunk_id, text, source, page, title, and chunk_index. Keep the original
# page record fields; the answer stage must be able to cite the paper and page.
# Suggested boundary: chunk_pages(pages, chunk_size, overlap) -> list[Chunk].
#
# MVP design: chunk one page at a time, using a configurable character window
# and overlap. This keeps page citations simple. Later, compare token-based or
# section-aware splitting and decide whether joining adjacent pages is worth the
# extra multi-page citation logic. There is no universally best chunk size:
# inspect examples and tune it for the chosen embedding model and papers.
#
# Important invariants:
# - Require chunk_size > 0 and 0 <= overlap < chunk_size.
# - Never emit empty/whitespace-only chunks.
# - Each chunk must point back to its original source and page.
# - Use a stable ID derived from source/page/chunk position (or another
#   documented scheme) so re-indexing can update records instead of duplicating.
# - Normalize whitespace carefully; do not remove meaningful symbols/equations
#   just to make text look tidy.
#
# Tests to write: empty page, page shorter than the chunk size, page requiring
# several overlapping chunks, invalid settings, and metadata/ID stability.
# Print sample chunks during development and manually check that each passage
# still expresses a coherent idea rather than ending mid-sentence every time.