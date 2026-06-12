"""
vector_test.py

Tests:

1. PDF loading
2. Chunking
3. Embedding generation
4. Chroma creation
5. Similarity search
"""

from app.loaders.pdf_loader import (
    load_pdf
)

from app.chunking.text_chunker import (
    create_chunks
)

from app.embeddings.embedding_model import (
    get_embedding_model
)

from app.vectorstore.chroma_store import (
    create_vector_db
)

from app.vectorstore.vector_search import (
    similarity_search
)


def run_vector_test():

    print(
        "\nLoading PDF..."
    )

    documents = load_pdf(
        "data/documents/sample.pdf"
    )

    print(
        f"Pages: {len(documents)}"
    )

    print(
        "\nChunking..."
    )

    chunks = create_chunks(
        documents
    )

    print(
        f"Chunks: {len(chunks)}"
    )

    print(
        "\nLoading Embedding Model..."
    )

    embedding_model = (
        get_embedding_model()
    )

    print(
        "\nCreating Chroma DB..."
    )

    vectordb = (
        create_vector_db(
            chunks,
            embedding_model
        )
    )

    query = (
        "What is the leave policy?"
    )

    print(
        f"\nSearching: {query}"
    )

    results = (
        similarity_search(
            vectordb,
            query
        )
    )

    print(
        f"\nResults Found: {len(results)}"
    )

    print(
        "\nTop Result:"
    )

    print(
        results[0].page_content[:500]
    )


if __name__ == "__main__":

    run_vector_test()