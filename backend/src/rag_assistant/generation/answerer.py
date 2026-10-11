"""Simple notes for writing careful answers from retrieved evidence."""

# This stage gets a question and the evidence that was already found.
# It should not search the full paper collection again.
#
# The answer should include:
# - the answer text
# - the citation IDs
# - page or source information when needed
#
# Rules:
# - only use the supplied passages
# - do not invent references
# - say when the evidence is weak or missing
# - stop early if there is no evidence to use
#
# Keep provider settings separate from the app logic.
# Validate every model response before returning it.
#
# Good tests include: normal answer generation, bad citation IDs, no evidence,
# malformed model output, and provider errors.