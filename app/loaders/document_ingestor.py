"""
document_ingestor.py

Handles multiple PDFs.
"""

from app.loaders.pdf_loader import (
    load_pdf
)


def ingest_documents(
        file_paths
):

    all_documents = []

    for file_path in file_paths:

        documents = load_pdf(
            file_path
        )

        all_documents.extend(
            documents
        )

    return all_documents