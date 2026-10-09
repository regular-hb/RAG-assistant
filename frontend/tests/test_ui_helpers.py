"""Tests for pure upload metadata helpers."""

from dataclasses import dataclass

import pytest

from frontend.ui_helpers import format_file_size, summarize_papers


@dataclass
class FakeUpload:
    name: str
    size: int


def test_summarize_papers_keeps_names_and_sizes() -> None:
    papers = summarize_papers([FakeUpload("study.pdf", 2048)])

    assert [(paper.name, paper.size_bytes) for paper in papers] == [("study.pdf", 2048)]


@pytest.mark.parametrize(
    ("size_bytes", "expected"),
    [(0, "0 B"), (1023, "1023 B"), (1024, "1 KB"), (1024 * 1024, "1.0 MB")],
)
def test_format_file_size(size_bytes: int, expected: str) -> None:
    assert format_file_size(size_bytes) == expected


def test_format_file_size_rejects_negative_size() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        format_file_size(-1)