"""Student guide: evaluate retrieval and answer grounding as separate tasks."""

# Build a small hand-labeled evaluation set before tuning. Each case should
# contain a research question, the IDs of passages judged relevant, and (for
# answer checks) expected evidence/citation facts. Use papers the team is
# permitted to process and keep labels separate from prompt examples.
#
# Retrieval evaluation: first implement a simple Hit@k check (did any known
# relevant passage appear in the first k results?). Then consider Precision@k
# (fraction of the first k that are relevant) or Recall@k (fraction of known
# relevant passages found). State how cases with no relevant passage are scored.
# A metric is only meaningful when relevance labels and k are documented.
#
# Answer/citation evaluation: check that every citation resolves to a passage
# actually retrieved and that the source/page metadata matches. Review whether
# factual claims are supported, whether important evidence is omitted, and how
# conflicting studies are represented. A fluent answer can still be wrong.
# Start with a human-readable checklist; automated faithfulness metrics are an
# optional stretch goal and should not be treated as ground truth.
#
# Compare a baseline (for example, keyword search or top-k without reranking)
# with later changes on the same cases. Keep evaluation data out of prompt tuning
# where possible. Record model/embedding versions and retrieval settings so a
# score change can be reproduced. Never claim a quality improvement from one
# anecdotal question.
#
# Tests to write: tiny cases with known rankings and citations, k smaller/larger
# than the result set, no relevant passages, duplicate results, and citation IDs
# that are missing or point to the wrong source/page.