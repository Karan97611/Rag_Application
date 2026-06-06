"""
embedding_validator.py

Validates embedding generation.

Useful for:

1. Debugging
2. Unit testing
3. Production monitoring
"""


def validate_embedding(
        vector
):
    """
    Validates embedding output.
    """

    if vector is None:
        return False

    if len(vector) == 0:
        return False

    return True