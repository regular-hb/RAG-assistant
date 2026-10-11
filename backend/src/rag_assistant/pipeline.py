"""Simple notes for connecting the backend stages together."""

# This module is the main app flow.
# It should call the other backend pieces, not do all the work itself.
#
# Main tasks:
# - ingest PDFs and prepare them for search
# - embed the chunks and save them to the vector store
# - answer a question using retrieval and generation
#
# Keep config outside this file when possible.
# Return helpful error messages, but do not hide real bugs.
#
# Good end-to-end tests use fake clients and a temporary index.
# That lets us test the whole flow without real network calls or papers.