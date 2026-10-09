"""Student guide: load PDFs into page records without losing provenance.

Keep this module responsible for file validation and text extraction only.
Chunking, embedding, and indexing belong in later stages.
"""

# MVP goal: given one or more local PDF paths, return one record per page that
# contains usable text. Keep the original filename (or a stable source ID) with
# every record so later answers can cite the source accurately.
#
# Suggested boundary (students write the implementation):
#   extract_pdf(path) -> list[PageRecord]
#   extract_pdfs(paths) -> list[PageRecord]
# PageRecord may be a dataclass or TypedDict with: source, page, text, title.
# Keep the page number one-based for display, even if the PDF library is
# zero-based internally. Make this choice explicit and test it.
#
# Implementation decisions to make:
# - Select one PDF library and check whether it extracts text from ordinary
#   text PDFs. OCR for scanned papers is a useful stretch goal, not MVP scope.
# - Decide whether `source` is a filename, a path relative to the corpus root,
#   or a generated ID. Do not store machine-specific absolute paths in citations.
# - Use available metadata cautiously: PDFs often have missing or incorrect
#   titles/authors, so retain the filename as a fallback.
#
# Failure behavior: reject non-PDF inputs, report encrypted/unreadable files,
# and skip or flag pages with no extracted text. A bad file should not prevent
# the rest of a batch from being reported. Do not log full paper contents.
#
# Tests to write: a tiny redistributable PDF with two pages, a page with no text,
# a missing path, and a malformed/encrypted file. Assert page numbering and
# source metadata, not just that a non-empty list was returned.