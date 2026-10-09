# Academic Research Assistant

An academic-focused retrieval-augmented generation (RAG) assistant for finding evidence in research papers and producing answers grounded in those sources.

## Project status

This repository is currently a scaffold. The Streamlit page and Python package mark the intended boundaries, but document ingestion, embeddings, retrieval, answer generation, and evaluation are not implemented yet. The provider, embedding model, vector store, and supported document formats should be selected before those components are built.

## Structure

```text
.
|-- backend/
|   |-- README.md                     # Student implementation guide
|   |-- data/
|   |   `-- papers/
|   |       |-- raw/                 # Local source papers; do not commit PDFs
|   |       |-- processed/           # Extracted and normalized paper data
|   |       `-- indeces/             # Local vector index and retrieval metadata
|   |-- notebooks/                   # Exploratory processing and retrieval work
|   |   |-- 01_document_processing.ipynb
|   |   |-- 02_embedding.ipynb
|   |   |-- 03_retrieval.ipynb
|   |   `-- rag.ipynb
|   |-- src/rag_assistant/
|   |   |-- ingestion/
|   |   |   |-- documents.py         # Loading papers and preserving metadata
|   |   |   `-- chunking.py           # Structure-aware, page-aware text chunks
|   |   |-- embeddings/
|   |   |   `-- embedder.py           # Text embedding interface
|   |   |-- retrieval/
|   |   |   |-- vector_store.py       # Persistence and similarity search
|   |   |   `-- retriever.py          # Querying and evidence selection
|   |   |-- generation/
|   |   |   `-- answerer.py            # Source-grounded answer generation
|   |   `-- evaluation/
|   |   |   `-- metrics.py             # Retrieval and answer quality measures
|   |   `-- pipeline.py                # Student guide to composing the stages
|   `-- tests/                        # Backend unit and integration tests
|-- frontend/
|   |-- streamlit_app.py              # Streamlit user interface
|   |-- README.md                     # Frontend responsibilities and editing guide
|   |-- .env.example                  # Safe template; no credentials
|   `-- tests/                        # Frontend and workflow tests
|-- .gitignore
|-- README.md
`-- requirements.txt
```

The numbered notebooks are research and prototyping artifacts. Reusable, tested logic belongs in `backend/src/rag_assistant/`; the frontend should call that package rather than duplicate pipeline logic. Backend modules are comment-guided student starters; see [backend/README.md](backend/README.md) for the suggested implementation order, shared data contract, and hints.

## Intended flow

1. Ingest permitted paper files and extract text with page, section, and bibliographic metadata.
2. Split text into chunks while retaining enough metadata to cite the original paper and page.
3. Embed and index chunks in a persistent vector store.
4. Retrieve relevant passages for a research question and generate an answer supported by those passages.
5. Present answers with inspectable citations, and evaluate retrieval quality and citation faithfulness.

For academic use, answers should distinguish retrieved evidence from model-generated interpretation. Preserve provenance (paper identity and page or section) through every stage, and evaluate citation correctness rather than relying only on answer fluency.

## Setup

Use Python 3.10 or newer and create a virtual environment. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate #for non windows users

.\.venv\Scripts\Activate.ps1 #for windows users
 
python -m pip install -r requirements.txt
```

The requirements file contains Streamlit for the interface and pytest for the frontend helper tests. Add backend dependencies when the pipeline implementations are selected.

## Run the interface

```bash
python -m streamlit run frontend/streamlit_app.py
```

Run this from the repository root with the project environment active. Do not run `python frontend/streamlit_app.py` directly; Streamlit must launch the script to provide the web server and app context. The page is an interface scaffold; it does not yet ingest papers or answer questions.

## Test the frontend

After installing the requirements, run the frontend helper tests from the repository root:

```bash
python -m pytest frontend/tests
```

These tests cover upload metadata summaries and file-size formatting. For frontend file responsibilities and editing guidance, see [frontend/README.md](frontend/README.md).

## Data and credentials

Keep source papers, extracted corpora, and generated indexes local unless their licenses and your institution's policies explicitly permit sharing. The ignore rules exclude PDF files and generated processed/index data. Never commit API keys or private credentials; put local settings in an ignored `.env` file and keep only placeholder names in `.env.example`.# RAG-assistant
