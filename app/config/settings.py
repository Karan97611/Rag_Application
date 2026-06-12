"""
settings.py

Loads all environment variables from .env

Purpose:
Central configuration management.

Instead of calling os.getenv()
throughout the project,
we do it once here.
"""

import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings:
    """
    Holds all application settings.

    Think of this as a central
    configuration object.
    """

    # Ollama model name
    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "llama3"
    )

    # Embedding model
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-base-en-v1.5"
    )

    # Chunk size
    CHUNK_SIZE = int(
        os.getenv(
            "CHUNK_SIZE",
            1000
        )
    )

    # Chunk overlap
    CHUNK_OVERLAP = int(
        os.getenv(
            "CHUNK_OVERLAP",
            200
        )
    )

    # Retrieval count
    TOP_K = int(
        os.getenv(
            "TOP_K",
            5
        )
    )

    # Chroma location
    VECTOR_DB_PATH = os.getenv(
        "VECTOR_DB_PATH",
        "chroma_db"
    )


settings = Settings()