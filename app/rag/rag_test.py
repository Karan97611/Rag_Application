"""
rag_test.py

Tests complete RAG pipeline.
"""

from app.embeddings.embedding_model import (
    get_embedding_model
)

from app.vectorstore.chroma_store import (
    load_vector_db
)

from app.rag.rag_pipeline import (
    ask_question
)


def run_rag_test():

    print(
        "\nLoading Vector DB..."
    )

    embedding_model = (
        get_embedding_model()
    )

    vector_db = (
        load_vector_db(
            embedding_model
        )
    )

    question = (
        "What is the leave policy?"
    )

    print(
        f"\nQuestion: {question}"
    )

    response = (
        ask_question(
            question,
            vector_db
        )
    )

    print(
        "\nAnswer:"
    )

    print(
        response["answer"]
    )

    print(
        "\nSources:"
    )

    for source in (
        response["sources"]
    ):

        print(source)


if __name__ == "__main__":

    run_rag_test()