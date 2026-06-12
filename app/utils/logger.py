"""
logger.py

Central logging utility.
"""

import logging
import os

os.makedirs(
    "logs",
    exist_ok=True
)

logging.basicConfig(
    filename="logs/rag.log",

    level=logging.INFO,

    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)

logger = logging.getLogger(
    "enterprise_rag"
)