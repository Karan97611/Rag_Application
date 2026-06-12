"""
custom_exceptions.py

Central place for all
custom exceptions.

Benefits:

1. Cleaner code
2. Better debugging
3. Enterprise standard
"""


class InvalidFileTypeException(Exception):
    """
    Raised when unsupported
    file is uploaded.
    """
    pass


class EmptyPDFException(Exception):
    """
    Raised when PDF contains
    no readable content.
    """
    pass