"""
text_chunker.py

Responsible for:

1. Splitting documents
2. Preserving metadata
3. Creating manageable chunks
4. Improving retrieval quality

This module is critical
for RAG accuracy.
"""

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from app.config.settings import (
    settings
)


def create_chunks(
        documents
):
    """
    Creates chunks from documents.

    Input:
        List[Document]

    Output:
        List[Document]
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_documents(
        documents
    )

    # Add chunk ids

    for index, chunk in enumerate(
            chunks
    ):

        chunk.metadata[
            "chunk_id"
        ] = index

    return chunks