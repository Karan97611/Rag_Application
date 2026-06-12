"""
health_check.py

Vector DB validation.
"""


def vector_db_health_check(
        vector_db
):

    try:

        collection = (
            vector_db._collection
        )

        count = collection.count()

        return {
            "healthy": True,
            "document_count": count
        }

    except Exception as e:

        return {
            "healthy": False,
            "error": str(e)
        }