from app.loaders.pdf_loader import (
    load_pdf
)

from app.chunking.text_chunker import (
    create_chunks
)

from app.chunking.chunk_stats import (
    get_chunk_stats
)

documents = load_pdf(
    "data/documents/sample.pdf"
)

chunks = create_chunks(
    documents
)

stats = get_chunk_stats(
    chunks
)

print(
    "\nChunk Statistics"
)

print(stats)

print(
    "\nFirst Chunk Metadata"
)

print(
    chunks[0].metadata
)

print(
    "\nFirst Chunk Preview"
)

print(
    chunks[0].page_content[:300]
)