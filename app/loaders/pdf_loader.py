"""
pdf_loader.py

Responsible for:

1. Loading PDF
2. Extracting pages
3. Adding metadata
4. Validation

This is the first step
of our RAG pipeline.
"""

from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader
)

from app.utils.file_utils import (
    validate_file_type
)

from app.exceptions.custom_exceptions import (
    EmptyPDFException
)


def load_pdf(
        pdf_path: str
):
    """
    Loads PDF file.

    Returns:
        List[Document]
    """

    validate_file_type(
        Path(pdf_path).name
    )

    loader = PyPDFLoader(
        pdf_path
    )

    documents = loader.load()

    if not documents:
        raise EmptyPDFException(
            "PDF contains no content."
        )

    # Add custom metadata

    for document in documents:

        document.metadata[
            "file_name"
        ] = Path(pdf_path).name

        document.metadata[
            "source_type"
        ] = "pdf"

    return documents