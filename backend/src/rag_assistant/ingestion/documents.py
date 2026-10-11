"""Read PDF files and return one page record per page."""

import logging
import os
from typing import Any, Dict, List

import fitz


# Open a PDF file and return page records with metadata and extracted text.
def extract_pdf(file_path: str) -> List[Dict[str, Any]]:
    if not file_path or not os.path.exists(file_path):
        logging.error("File not found: %s", file_path)
        return []

    if not file_path.lower().endswith(".pdf"):
        logging.error("Not a PDF file: %s", file_path)
        return []

    try:
        doc = fitz.open(file_path)
    except Exception as exc:
        logging.error("Could not open PDF %s: %s", file_path, exc)
        return []

    page_records: List[Dict[str, Any]] = []

    try:
        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            text = page.get_text("text").strip()
            title = doc.metadata.get("title", "") or os.path.basename(file_path)

            page_record = {
                "source": os.path.basename(file_path),
                "page": page_number + 1,
                "page_number": page_number + 1,
                "text": text,
                "title": title,
            }
            page_records.append(page_record)
    finally:
        doc.close()

    return page_records


# Return page records for a PDF file using the same extraction logic.
def extract_pdf_pages(file_path: str) -> List[Dict[str, Any]]:
    return extract_pdf(file_path)


# Quick sanity check for a normal PDF and a missing file.
def test_extract_pdf() -> None:
    import tempfile

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
        doc = fitz.open()
        page = doc.new_page()
        page.insert_text((72, 72), "Hello from a test PDF.")
        doc.save(temp_pdf.name)
        doc.close()

        pages = extract_pdf(temp_pdf.name)
        assert len(pages) == 1, "A one-page PDF should return one page record."
        assert pages[0]["page"] == 1, "Page numbers should be one-based."
        assert "Hello" in pages[0]["text"], "Extracted text should include the PDF content."

        missing_pages = extract_pdf("does_not_exist.pdf")
        assert missing_pages == [], "Missing files should return an empty list."

        os.unlink(temp_pdf.name)


