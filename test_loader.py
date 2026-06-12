from app.loaders.pdf_loader import (
    load_pdf
)

documents = load_pdf(
    "data/documents/sample.pdf"
)

print(
    f"Pages Loaded: {len(documents)}"
)

print(
    documents[0].metadata
)

print(
    documents[0].page_content[:300]
)