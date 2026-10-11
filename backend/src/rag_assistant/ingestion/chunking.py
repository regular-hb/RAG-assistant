"""Split page text into smaller chunks for embedding and retrieval."""

import hashlib
import re
from typing import Any, Dict, List


# Input: a page record with source, page, text, and title.
# Output: a list of chunk records with chunk_id, source, page, text, and title.
# Rules:
# - chunk_size must be greater than 0
# - overlap must be smaller than chunk_size
# - do not create empty chunks
# - keep source and page metadata with every chunk
# - use a stable chunk ID so repeated runs do not create duplicates


# Normalize whitespace so the text is easier to split safely.
def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


# Split a text string into overlapping chunks of a fixed character length.
def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    if not text or not text.strip():
        return []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    text = clean_text(text)
    chunks: List[str] = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(text):
            break

        start = end - overlap

    return chunks


# Create a stable chunk ID from the source, page, and chunk position.
def generate_chunk_id(source: str, page_number: int, chunk_index: int) -> str:
    return hashlib.md5(f"{source}_{page_number}_{chunk_index}".encode("utf-8")).hexdigest()


# Turn one page record into multiple chunk records with metadata attached.
def chunk_page(page_record: Dict[str, Any], chunk_size: int, overlap: int) -> List[Dict[str, Any]]:
    text = page_record.get("text", "")
    source = page_record.get("source", "")
    page_number = page_record.get("page", 1)
    title = page_record.get("title", "")

    if not text or not text.strip():
        return []

    chunks = chunk_text(text, chunk_size, overlap)
    chunk_records: List[Dict[str, Any]] = []

    for index, chunk in enumerate(chunks):
        chunk_id = generate_chunk_id(source, page_number, index)
        chunk_records.append(
            {
                "chunk_id": chunk_id,
                "source": source,
                "page": page_number,
                "text": chunk,
                "title": title,
            }
        )

    return chunk_records


# Open a PDF, extract page records, and split each page into chunks.
def chunk_document(file_path: str, chunk_size: int, overlap: int) -> List[Dict[str, Any]]:
    from rag_assistant.ingestion.documents import extract_pdf

    page_records = extract_pdf(file_path)
    all_chunks: List[Dict[str, Any]] = []

    for page_record in page_records:
        all_chunks.extend(chunk_page(page_record, chunk_size, overlap))

    return all_chunks


# Return the default chunk size and overlap values used by the project.
def get_chunking_config() -> Dict[str, int]:
    return {"chunk_size": 500, "overlap": 50}


# Run a few quick checks for empty input, short text, and invalid settings.
def test_chunking() -> None:
    text = "This is a test document. It has multiple sentences. We will split it into chunks."

    chunks = chunk_text(text, chunk_size=20, overlap=5)
    assert len(chunks) > 0, "Normal text should generate chunks."

    empty_chunks = chunk_text("", chunk_size=20, overlap=5)
    assert len(empty_chunks) == 0, "Empty text should produce no chunks."

    short_chunks = chunk_text("Short text.", chunk_size=20, overlap=5)
    assert len(short_chunks) == 1, "Short text should become one chunk."

    try:
        chunk_text(text, chunk_size=0, overlap=5)
        raise AssertionError("chunk_size <= 0 should raise ValueError")
    except ValueError:
        pass

    try:
        chunk_text(text, chunk_size=20, overlap=20)
        raise AssertionError("overlap >= chunk_size should raise ValueError")
    except ValueError:
        pass
