"""
embedding_test.py

Simple embedding tests.

Helps verify:

1. Model loaded
2. Vectors generated
3. Dimensions correct
"""

from app.embeddings.embedding_model import (
    get_embedding_model
)

from app.embeddings.embedding_validator import (
    validate_embedding
)


def run_embedding_test():

    model = get_embedding_model()

    text = (
        "Employees receive annual leave."
    )

    vector = (
        model.embed_query(text)
    )

    is_valid = (
        validate_embedding(
            vector
        )
    )

    print(
        "\nEmbedding Validation:"
    )

    print(
        is_valid
    )

    print(
        "\nEmbedding Dimension:"
    )

    print(
        len(vector)
    )

    print(
        "\nFirst 10 Values:"
    )

    print(
        vector[:10]
    )


if __name__ == "__main__":

    run_embedding_test()