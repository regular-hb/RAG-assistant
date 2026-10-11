"""Simple notes for checking if retrieval and answers are good."""

# Start with a small set of questions and known good answers.
# Keep the question, relevant passages, and expected evidence in one place.
# Use the same test set before and after changes so the comparison is fair.
#
# Retrieval check: confirm the right passages appear near the top.
# Answer check: confirm the result uses only the provided evidence and cites it.
#
# Do not rely on one random example to judge quality.
# Record the model, embeddings, and settings so any score change can be explained.
#
# Good tests include: known-good rankings, missing evidence, duplicate results,
# and citations that point to the wrong paper or page.