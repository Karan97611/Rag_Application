"""
retriever_service.py

Responsible for:

1. Retrieving relevant chunks
2. Formatting context
3. Source extraction
"""

from app.config.settings import (
    settings
)


def retrieve_documents(
        vector_db,
        question
):
    """
    Retrieve top K chunks.
    """

    retriever = (
        vector_db.as_retriever(
            search_kwargs={
                "k":
                settings.TOP_K
            }
        )
    )

    documents = (
        retriever.invoke(
            question
        )
    )

    return documents


def build_context(
        documents
):
    """
    Convert retrieved documents
    into LLM context.
    """

    context = "\n\n".join(

        doc.page_content

        for doc in documents
    )

    return context


def extract_sources(
        documents
):
    """
    Extract source references.
    """

    sources = []

    for doc in documents:

        source = (
            doc.metadata.get(
                "file_name",
                "Unknown"
            )
        )

        page = (
            doc.metadata.get(
                "page",
                "Unknown"
            )
        )

        chunk_id = (
            doc.metadata.get(
                "chunk_id",
                "Unknown"
            )
        )

        sources.append({

            "file":
                source,

            "page":
                page,

            "chunk":
                chunk_id
        })

    return sources