"""Pure helpers for frontend upload metadata and presentation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class UploadedFile(Protocol):
    """The small part of Streamlit's UploadedFile used by this interface."""

    name: str
    size: int


@dataclass(frozen=True)
class PaperRecord:
    """Display-safe metadata for one PDF selected in the current session."""

    name: str
    size_bytes: int


def summarize_papers(uploads: list[UploadedFile]) -> list[PaperRecord]:
    """Convert uploaded PDFs to stable display records without consuming content."""
    return [PaperRecord(name=upload.name, size_bytes=upload.size) for upload in uploads]


def format_file_size(size_bytes: int) -> str:
    """Format file sizes as bytes, KB, or MB for compact reading-list rows."""
    if size_bytes < 0:
        raise ValueError("size_bytes must not be negative")
    if size_bytes < 1024:
        return f"{size_bytes} B"
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.0f} KB"
    return f"{size_bytes / (1024 * 1024):.1f} MB"