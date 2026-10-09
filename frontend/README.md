# Frontend

The frontend is a responsive Streamlit research workspace. It currently supports selecting PDFs into the current browser session, drafting a research question, switching between the research desk, paper library, and project notes, and previewing the intended evidence presentation. It does not extract PDF text, persist files, call a model, or generate answers until the backend is implemented and connected.

## Run

From the repository root with the project virtual environment active:

```bash
python -m pip install -r requirements.txt
python -m streamlit run frontend/streamlit_app.py


if it fails, run this instead:
     ./.venv/bin/python -m streamlit run frontend/streamlit_app.py #replace the env name with your env's name
```

Run the command from the repository root. Do not execute `streamlit_app.py` with plain Python; Streamlit needs to launch it to provide the web server and app context. The interface is designed to reflow for mobile and desktop browser widths. Streamlit handles the responsive columns; `styles.py` contains the narrow-screen adjustments.

## Files

| File | Responsibility |
| --- | --- |
| `streamlit_app.py` | App setup, session state, sidebar, and page/view composition. |
| `components.py` | Reusable headings, status labels, and paper-list presentation. |
| `ui_helpers.py` | Pure functions and typed records for upload metadata. |
| `styles.py` | CSS color/type tokens and responsive presentation rules. |
| `tests/test_ui_helpers.py` | Fast tests for upload summaries and size formatting. |
| `.env.example` | Safe placeholder for future configuration names. |

## Editing guide

- Change the overall palette, typography, spacing, and breakpoints in `styles.py`.
- Change navigation, session state, and page layout in `streamlit_app.py`.
- Add repeated presentation elements to `components.py` rather than duplicating markup.
- Keep business and document-processing logic in `backend/src/rag_assistant/`; the UI should call backend functions through a small integration boundary once those functions exist.
- Use `ui_helpers.py` for logic that does not need Streamlit. Keep it deterministic and cover it in `tests/`.

The HTML snippets in components are limited to visual presentation. Escape user-controlled filenames before including them in those snippets. Prefer native Streamlit widgets for inputs and actions so keyboard and screen-reader behavior remains available.

## File handling and privacy

Uploads are held by Streamlit for the active session and are not written to the repository by this frontend. The current app only reads upload names and sizes. Before connecting ingestion, define retention, access control, deletion, licensing, and institution-specific privacy requirements for academic documents.

## Test

```bash
python -m pytest frontend/tests
```