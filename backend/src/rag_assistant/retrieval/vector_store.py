"""Simple notes for storing vectors and returning matching evidence."""

# This module saves chunk vectors and later searches them.
# It should keep the chunk text, source, and metadata together with the vector.



#
# Main actions:
# - add chunks and their vectors
# - search for the closest results
# - clear the index when needed for testing or rebuilds
#
# Important rules:
# - keep each vector matched to the correct chunk
# - store source, page, title, and chunk ID with the result
# - reject mismatched vector lengths
# - handle empty indexes and duplicate IDs clearly
#
# Good tests include: add/search round trip, empty search, top-k ordering,
# metadata retention, and dimension mismatch checks.