"""
chunk_stats.py

Provides chunk statistics.

Useful for:

1. Debugging
2. Optimization
3. Evaluation
"""


def get_chunk_stats(
        chunks
):
    """
    Returns chunk statistics.
    """

    total_chunks = len(
        chunks
    )

    chunk_lengths = [
        len(chunk.page_content)
        for chunk in chunks
    ]

    avg_length = (
        sum(chunk_lengths)
        / total_chunks
        if total_chunks
        else 0
    )

    longest_chunk = (
        max(chunk_lengths)
        if chunk_lengths
        else 0
    )

    shortest_chunk = (
        min(chunk_lengths)
        if chunk_lengths
        else 0
    )

    return {
        "total_chunks":
            total_chunks,

        "average_length":
            round(avg_length, 2),

        "largest_chunk":
            longest_chunk,

        "smallest_chunk":
            shortest_chunk
    }