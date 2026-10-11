"""Convert text into vectors so we can compare meaning."""

import logging
from typing import List

logging.basicConfig(level=logging.INFO)


# Convert one text item into a fixed-length numeric vector.
def embed_text(text: str) -> List[float]:
    if not text or not text.strip():
        return []

    values = [float(ord(char)) for char in text]

    if len(values) < 512:
        values = values + [0.0] * (512 - len(values))

    return values[:512]


# Keep provider-specific code in one place so the rest of the app uses plain Python data.
def embed_text_with_provider(text: str, provider: str) -> List[float]:
    if provider == "dummy":
        return embed_text(text)

    logging.error("Unknown embedding provider: %s", provider)
    return []


# Embed a list of texts while preserving order and skipping empty results.
def embed_texts(texts: List[str], provider: str) -> List[List[float]]:
    embeddings: List[List[float]] = []

    for text in texts:
        embedding = embed_text_with_provider(text, provider)

        if embedding is not None and len(embedding) > 0:
            embeddings.append(embedding)
        else:
            logging.warning("Skipping empty embedding for text: %s", text)

    return embeddings


# A query is just one text value, so it can reuse the same embedding logic.
def embed_query(question: str, provider: str) -> List[float]:
    return embed_text_with_provider(question, provider)


# Use a fake provider in tests, and keep real model tests separate.
def test_embedder() -> None:
    assert embed_text("hello") != []
    assert len(embed_text("hello")) == 512
    assert len(embed_texts(["one", "two"], "dummy")) == 2
    assert embed_text_with_provider("hello", "wrong_provider") == []
