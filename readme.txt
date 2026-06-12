 ================================================================================
                          ENTERPRISE RAG PLATFORM
================================================================================

## Setup

pip install -r requirements.txt

## Run

streamlit run streamlit_app.py

## Docker

docker build -t enterprise-rag .

docker run -p 8501:8501 enterprise-rag

Overview
--------
This project is a Retrieval-Augmented Generation (RAG) application that allows 
users to upload PDF documents, chunk and embed the text locally, and ask 
questions against the document context using a local LLM.

Tech Stack
----------
* Frontend UI: Streamlit
* Local LLM: Ollama (Llama3)
* Embeddings: BAAI/bge-base-en-v1.5 (via LangChain)
* Vector Database: ChromaDB (Local persistent storage)
* Frameworks: LangChain, PyPDF, Streamlit

================================================================================
                              BLOCK DIAGRAM
================================================================================

 [PDF Upload] -> (pdf_loader) -> (text_chunker) -> (embedding_model)
                                                          |
                                                          v
                                                   [Chroma Vector DB]
                                                          |
 [User Query] -> (embedding_model) -> (retriever) --------+
                                           |
                                           v
 [Context + Prompt] -> (llm_service) -> [Answer Output] -> UI

================================================================================
                      FILE CONNECTIVITY & FUNCTION MAP
================================================================================

ROOT
|
|-- streamlit_app.py  (Main Entry Point)
|      Uses: load_pdf(), create_chunks(), get_embedding_model(), 
|            create_vector_db(), load_vector_db(), ask_question()
|
|-- reset_and_ingest.py (Utility Script)
|      Uses: clear_old_db(), ingest_sample()
|
|-- app/
    |
    |-- loaders/
    |   |-- pdf_loader.py
    |       * load_pdf(file_path): Reads PDF and returns Document objects.
    |
    |-- chunking/
    |   |-- text_chunker.py
    |       * create_chunks(documents): Splits documents into smaller text chunks.
    |   |-- chunk_stats.py
    |       * get_chunk_stats(chunks): Helper to analyze chunk sizes.
    |
    |-- embeddings/
    |   |-- embedding_model.py
    |       * get_embedding_model(): Loads BAAI/bge-base-en-v1.5 via LangChain.
    |
    |-- vectorstore/
    |   |-- chroma_store.py
    |       * create_vector_db(chunks, embedding_model): Clears old DB and saves new chunks.
    |       * load_vector_db(embedding_model): Connects to existing ChromaDB.
    |   |-- vector_search.py
    |       * similarity_search(vector_db, query): Fetches raw matching chunks.
    |
    |-- rag/
        |-- rag_pipeline.py
        |   * ask_question(question, vector_db): Orchestrates the entire query workflow.
        |
        |-- retriever_service.py
        |   * retrieve_documents(vector_db, question): Executes similarity search.
        |   * build_context(documents): Joins chunk text into LLM context block.
        |   * extract_sources(documents): Formats metadata (file, page, chunk id).
        |
        |-- llm_service.py
        |   * get_llm(): Loads the Ollama Llama3 model using a Singleton pattern.
        |
        |-- prompt_template.py
            * RAG_PROMPT: Defines the system instructions and constraints for the LLM.

================================================================================
                            THINGS TO KEEP IN MIND
================================================================================

1. Background Services:
   - Ollama MUST be running in the background for embeddings and RAG generations 
     to work. Ensure you have pulled the models locally (`ollama run llama3`).

2. GPU Memory (VRAM) Management:
   - Processing large PDFs and generating LLM responses requires sufficient VRAM. 
   - If you encounter a "CUDA error" or "Stack-based buffer overrun", it means 
     the GPU ran out of memory. 
   - Fix: Completely close and restart the background Ollama application.

3. Vector DB State / Stale Data:
   - ChromaDB saves chunks persistently to a local folder (e.g., `chroma_db/`).
   - If you want to change documents entirely without old context lingering, use 
     the `Create Knowledge Base` button in the UI or run `reset_and_ingest.py` 
     to wipe the old database directory before embedding the new one.

4. Modularity:
   - This project uses "Separation of Concerns". If you want to change the LLM 
     provider (e.g., to OpenAI), you ONLY need to edit `llm_service.py`. If you 
     want to change chunk sizes, you ONLY edit `text_chunker.py`.
