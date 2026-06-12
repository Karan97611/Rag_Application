"""
llm_service.py

Responsible for:

1. Loading Ollama model
2. Managing LLM lifecycle
3. Reusing model instance
"""

from langchain_ollama import (
    OllamaLLM
)

from app.config.settings import (
    settings
)

_llm = None


def get_llm():

    """
    Singleton pattern.

    Load once.
    Reuse everywhere.
    """

    global _llm

    if _llm is None:

        _llm = OllamaLLM(
            model=settings.OLLAMA_MODEL
        )

    return _llm