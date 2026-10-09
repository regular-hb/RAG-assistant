"""Student guide: encode chunks and questions in one compatible vector space."""

# Embeddings are numeric representations used for similarity search; they are
# not answers and should not replace the source text. Use the same model and
# preprocessing for paper chunks and research questions.
#
# Suggested boundary: embed_texts(texts) -> list[Vector] and embed_query(text)
# -> Vector. The first operation should batch document chunks when the chosen
# provider allows it. Keep provider-specific SDK calls inside this module so
# retrieval code can work with plain Python data.
#
# Before choosing a model, record its vector dimension, maximum input length,
# batching/rate limits, cost, supported languages, license, and whether paper
# text leaves the machine. Make the model name/configuration visible to the
# indexing stage: changing models usually requires rebuilding the whole index.
#
# Validate the provider response: one vector per input, non-empty vectors,
# consistent dimensions, and no reordering of chunk IDs. Decide how provider
# timeouts/rate limits are surfaced; avoid logging paper text or credentials.
# For the first version, skip caching. Add it only if repeated calls are costly
# and the key includes model/version plus exact input text (or a safe hash).
#
# Tests to write: use a fake embedder with known vectors to test ordering,
# dimensions, empty input, and provider errors without network access. A live
# provider test should be separate and require explicit configuration.