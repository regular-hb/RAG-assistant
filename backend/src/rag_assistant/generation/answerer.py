"""Student guide: produce a cautious synthesis from retrieved evidence."""

# Input should be a research question plus the Evidence records from retriever.py.
# This stage must not query the corpus itself. That separation makes it possible
# to inspect retrieval independently and prevents hidden, uncited evidence from
# entering a response.
#
# Suggested result: an Answer record containing answer_text, citations, and
# optionally a short limitation/abstention reason. Each citation should resolve
# to a supplied chunk_id and carry source/page for display. Agree on this result
# shape with the frontend before implementing provider-specific code.
#
# Prompt design hints:
# - Give each passage a short stable ID, paper/title, page, and quoted text.


# - Instruct the model to use only supplied passages, cite IDs for factual
#   claims, distinguish evidence from interpretation, and say when evidence is
#   insufficient or conflicting.
# - Keep context within the selected model's token limit. Prefer fewer relevant
#   passages to silently truncating citations or sending an entire paper.
#
# Parse/validate the model response before returning it. Reject or flag citation
# IDs that were not supplied; never invent bibliographic details. Handle zero
# retrieved passages without calling the model. Keep API credentials in local
# environment configuration, never source control or logs.
#
# Tests to write: mock the model client, inspect the prompt inputs, test a valid
# cited answer, an unknown citation ID, malformed provider output, no evidence,
# and a provider error. Keep live-model tests separate from unit tests.