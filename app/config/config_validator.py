"""
config_validator.py

Validates settings.
"""

from app.config.settings import (
    settings
)


def validate_settings():

    if settings.CHUNK_SIZE <= 0:

        raise ValueError(
            "CHUNK_SIZE must be > 0"
        )

    if settings.TOP_K <= 0:

        raise ValueError(
            "TOP_K must be > 0"
        )

    return True