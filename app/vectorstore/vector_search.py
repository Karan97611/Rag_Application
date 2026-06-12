"""
vector_search.py

Responsible for:

1. Similarity search
2. Retrieval
3. Metadata filtering
"""

from app.config.settings import (
    settings
)


def similarity_search(
        vector_db,
        query
):
    """
    Returns top matching chunks.
    """

    results = (
        vector_db.similarity_search(
            query,

            k=settings.TOP_K
        )
    )

    return results


def similarity_search_with_score(
        vector_db,
        query
):
    """
    Returns chunks
    with similarity scores.
    """

    results = (
        vector_db.similarity_search_with_score(
            query,

            k=settings.TOP_K
        )
    )

    return results