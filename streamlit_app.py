"""
streamlit_app.py

Enterprise RAG Platform

Features:

1. Upload PDF
2. Create Knowledge Base
3. Ask Questions
4. Show Sources
5. Session Persistence
"""

import os

import streamlit as st

from app.loaders.document_ingestor import (
    ingest_documents

)

from app.chunking.text_chunker import (
    create_chunks
)

from app.embeddings.embedding_model import (
    get_embedding_model
)

from app.vectorstore.chroma_store import (
    create_vector_db,
    load_vector_db
)

from app.rag.rag_pipeline import (
    ask_question
)

# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="Enterprise RAG Platform",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------
# Session State
# ---------------------------------
if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

if st.session_state.chat_history:

    st.subheader("History")

    for item in reversed(
            st.session_state.chat_history
    ):

        st.markdown(
            f"**Q:** {item['question']}"
        )

        st.markdown(
            f"**A:** {item['answer']}"
        )
        
if "knowledge_base_ready" not in st.session_state:

    st.session_state.knowledge_base_ready = False

# ---------------------------------
# Header
# ---------------------------------

st.title(
    "Enterprise RAG Platform"
)

st.markdown(
    """
Upload PDFs and ask questions
using Retrieval Augmented Generation.
"""
)

# ---------------------------------
# Sidebar
# ---------------------------------

with st.sidebar:

    st.header("Configuration")

    st.info(
        """
Current Setup

LLM: Ollama Llama3

Embeddings:
BAAI/bge-base-en-v1.5

Vector DB:
ChromaDB
"""
    )

# ---------------------------------
# Upload Section
# ---------------------------------

st.header("Upload PDF")

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True

)

# ---------------------------------
# Save Uploaded File
# ---------------------------------

if uploaded_files:


    os.makedirs(
        "data/documents",
        exist_ok=True
    )

    file_paths = []
    for uploaded_file in uploaded_files:
        file_path = f"data/documents/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_paths.append(file_path)
        st.success(f"Uploaded: {uploaded_file.name}")

    # ------------------------------
    # Build Knowledge Base
    # ------------------------------

    if st.button(
            "Create Knowledge Base"
    ):

        with st.spinner(
            "Processing PDF..."
        ):

            try:

                # Step 1
                # Load PDF

                documents = (
                    ingest_documents(
                        file_paths
                    )
                )

                # Step 2
                # Chunking

                chunks = (
                    create_chunks(
                        documents
                    )
                )

                # Step 3
                # Embeddings

                embedding_model = (
                    get_embedding_model()
                )

                # Step 4
                # Create Vector DB

                create_vector_db(
                    chunks,
                    embedding_model
                )

                st.session_state.knowledge_base_ready = True

                st.success(
                    "Knowledge Base Created Successfully!"
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

# ---------------------------------
# Question Section
# ---------------------------------

st.header("Ask Questions")

question = st.text_input(
    "Enter your question"
)

# ---------------------------------
# Ask Button
# ---------------------------------

if st.button(
        "Get Answer"
):

    if not question:

        st.warning(
            "Please enter a question."
        )

    elif not st.session_state.knowledge_base_ready:

        st.warning(
            "Please create knowledge base first."
        )

    else:

        try:

            with st.spinner(
                "Searching documents..."
            ):

                embedding_model = (
                    get_embedding_model()
                )

                vector_db = (
                    load_vector_db(
                        embedding_model
                    )
                )

                response = (
                    ask_question(
                        question,
                        vector_db
                    )
                )

                st.session_state.chat_history.append(
                    {
                        "question": question,
                        "answer": response["answer"]
                    }
                )

            # --------------------------
            # Answer
            # --------------------------

            st.subheader(
                "Answer"
            )

            # st.write(
            #     response["answer"]
            # )
            st.success(response["answer"])

            # --------------------------
            # Sources
            # --------------------------

            st.subheader(
                "Sources"
            )

            for source in (
                response["sources"]
            ):

                st.write(
                    f"""
File:
{source['file']}

Page:
{source['page']}

Chunk:
{source['chunk']}
"""
                )

        except Exception as e:

            st.error(
                str(e)
            )