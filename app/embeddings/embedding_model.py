"""
embedding_model.py

Responsible for:

1. Loading embedding model
2. Configuring embeddings
3. Returning singleton model

Embeddings convert text
into numerical vectors.
"""

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

from app.config.settings import (
    settings
)

# Global cache

_embedding_model = None


def get_embedding_model():
    """
    Loads embedding model once.

    Why?

    Embedding models are large.

    Loading repeatedly wastes memory
    and increases response time.
    """

    global _embedding_model

    if _embedding_model is None:

        _embedding_model = (
            HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL,

                model_kwargs={
                    "device": "cpu"
                },

                encode_kwargs={
                    "normalize_embeddings": True
                }
            )
        )

    return _embedding_model