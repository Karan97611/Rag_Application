"""
rag_pipeline.py

Core RAG workflow.

Question
   ↓
Retrieve
   ↓
Build Context
   ↓
Create Prompt
   ↓
LLM
   ↓
Answer
"""

from app.rag.prompt_template import (
    RAG_PROMPT
)

from app.rag.llm_service import (
    get_llm
)

from app.rag.retriever_service import (
    retrieve_documents,
    build_context,
    extract_sources
)


def ask_question(
        question,
        vector_db
):
    """
    Complete RAG pipeline.
    """

    # Step 1
    # Retrieve documents

    documents = (
        retrieve_documents(
            vector_db,
            question
        )
    )

    # Step 2
    # Build context

    context = (
        build_context(
            documents
        )
    )

    # Step 3
    # Create prompt

    prompt = (
        RAG_PROMPT.format(
            context=context,
            question=question
        )
    )

    # Step 4
    # Call LLM

    llm = get_llm()

    answer = (
        llm.invoke(
            prompt
        )
    )

    # Step 5
    # Extract sources

    sources = (
        extract_sources(
            documents
        )
    )

    return {
        "question":
            question,

        "answer":
            answer,

        "sources":
            sources
    }