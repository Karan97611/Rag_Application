"""
chroma_store.py

Responsible for:

1. Creating Chroma DB
2. Persisting vectors
3. Loading existing vectors
4. Managing collections
"""

import os
import shutil

from langchain_chroma import Chroma

from app.config.settings import (
    settings
)


def create_vector_db(
        chunks,
        embedding_model
):
    """
    Creates a new vector database.

    Existing database will be removed.

    Useful during development.
    """

    db_path = settings.VECTOR_DB_PATH

    # Remove old DB

    if os.path.exists(db_path):

        shutil.rmtree(db_path)

    vectordb = Chroma.from_documents(
        documents=chunks,

        embedding=embedding_model,

        persist_directory=db_path
    )

    return vectordb


def load_vector_db(
        embedding_model
):
    """
    Loads existing vector DB.
    """

    vectordb = Chroma(
        persist_directory=
        settings.VECTOR_DB_PATH,

        embedding_function=
        embedding_model
    )

    return vectordb