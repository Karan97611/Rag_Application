"""
constants.py

Stores reusable constants.

Purpose:

Avoid magic strings
and duplicated values.
"""

SUPPORTED_FILE_TYPES = [
    ".pdf"
]

SYSTEM_PROMPT = """
You are an enterprise AI assistant.

Rules:

1. Answer only from provided context.

2. If answer is unavailable,
say:

Information not found
in uploaded documents.

3. Never fabricate information.

4. Always remain factual.
"""