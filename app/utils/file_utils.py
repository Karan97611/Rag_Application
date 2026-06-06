"""
file_utils.py

Utility functions related
to file operations.
"""

import os

from app.utils.constants import (
    SUPPORTED_FILE_TYPES
)

from app.exceptions.custom_exceptions import (
    InvalidFileTypeException
)


def validate_file_type(
        file_name: str
) -> bool:
    """
    Validates uploaded file.

    Example:

    policy.pdf → valid

    image.png → invalid
    """

    extension = os.path.splitext(
        file_name
    )[1].lower()

    if extension not in SUPPORTED_FILE_TYPES:
        raise InvalidFileTypeException(
            f"Unsupported file type: {extension}"
        )

    return True