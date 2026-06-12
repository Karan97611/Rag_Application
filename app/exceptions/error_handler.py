"""
error_handler.py
"""

from app.utils.logger import (
    logger
)


def handle_exception(
        exception
):

    logger.error(
        str(exception)
    )

    return {
        "status": "failed",
        "message": str(exception)
    }