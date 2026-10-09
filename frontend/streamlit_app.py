"""Streamlit entry point for the academic research assistant."""

from __future__ import annotations

import streamlit as st

from frontend.components import (
    render_header,
    render_paper_list,
    render_panel_heading,
    render_status,
)
from frontend.styles import APP_CSS
from frontend.ui_helpers import PaperRecord, summarize_papers


st.set_page_config(
    page_title="Fieldnotes | Research assistant",
    page_icon="G",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(APP_CSS, unsafe_allow_html=True)


def initialize_state() -> None:
    """Create the small amount of state shared across Streamlit reruns."""
    st.session_state.setdefault("uploader_generation", 0)
    st.session_state.setdefault("research_question", "")
    st.session_state.setdefault("submitted_question", "")


def render_sidebar() -> tuple[str, list[PaperRecord]]:
    """Render navigation and the session-only PDF picker."""
    st.sidebar.markdown(
        '<div class="brand-lockup"><span class="brand-mark">F</span>'
        '<span><strong>Fieldnotes</strong><small>RESEARCH DESK</small></span></div>',
        unsafe_allow_html=True,
    )
    view = st.sidebar.radio(
        "Workspace",
        ["Research desk", "Paper library", "Project notes"],
        label_visibility="collapsed",
        key="active_view",
    )

    st.sidebar.markdown('<div class="sidebar-rule"></div>', unsafe_allow_html=True)
    st.sidebar.markdown('<p class="sidebar-label">YOUR PAPERS</p>', unsafe_allow_html=True)
    uploads = st.sidebar.file_uploader(
        "Add research papers",
        type=["pdf"],
        accept_multiple_files=True,
        key=f"paper_uploads_{st.session_state.uploader_generation}",
        help="PDFs stay in this Streamlit session. They are not indexed or saved yet.",
    )
    papers = summarize_papers(uploads or [])

    total_bytes = sum(paper.size_bytes for paper in papers)
    st.sidebar.markdown(
        f'<div class="sidebar-library"><div><strong>{len(papers)}</strong>'
        f'<span>paper{"s" if len(papers) != 1 else ""} in session</span></div>'
        f'<small>{total_bytes and _format_size(total_bytes) or "No files added"}</small></div>',
        unsafe_allow_html=True,
    )
    if papers and st.sidebar.button("Clear session papers", use_container_width=True):
        st.session_state.uploader_generation += 1
        st.session_state.submitted_question = ""
        st.rerun()

    st.sidebar.markdown('<div class="sidebar-rule"></div>', unsafe_allow_html=True)
    render_status("Pipeline not connected", tone="pending", sidebar=True)
    st.sidebar.caption("Files stay in this browser session. No analysis runs yet.")
    return view, papers


def _format_size(size_bytes: int) -> str:
    """Keep the sidebar's total size compact and human-readable."""
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.0f} KB total"
    return f"{size_bytes / (1024 * 1024):.1f} MB total"


def render_research_desk(papers: list[PaperRecord]) -> None:
    render_header(
        eyebrow="RESEARCH WORKSPACE",
        title="Read across the literature.",
        description=(
            "Gather papers, frame a research question, and keep every finding tied "
            "to its source."
        ),
    )

    metric_columns = st.columns([1, 1, 1.5], gap="medium")
    metric_columns[0].markdown(
        f'<div class="metric-strip"><span>IN THIS SESSION</span>'
        f'<strong>{len(papers):02d}</strong><small>papers added</small></div>',
        unsafe_allow_html=True,
    )
    metric_columns[1].markdown(
        '<div class="metric-strip"><span>SUPPORTED FILE</span>'
        '<strong>PDF</strong><small>document format</small></div>',
        unsafe_allow_html=True,
    )
    metric_columns[2].markdown(
        '<div class="metric-strip metric-status"><span>RESEARCH PIPELINE</span>'
        '<strong>Awaiting connection</strong><small>Questions are not sent or answered yet</small></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)
    query_column, evidence_column = st.columns([1.35, 0.85], gap="large")

    with query_column:
        render_panel_heading("01", "Frame your question", "A focused question makes evidence easier to assess.")
        st.text_area(
            "Research question",
            placeholder="e.g. How do recent studies measure long-term memory retention?",
            height=122,
            key="research_question",
            label_visibility="collapsed",
        )
        st.markdown('<p class="field-label">START WITH A QUESTION LIKE</p>', unsafe_allow_html=True)
        examples = st.columns(3, gap="small")
        prompts = [
            "Compare methods",
            "Find limitations",
            "Trace key findings",
        ]
        prompt_text = [
            "How do these papers differ in their research methods?",
            "What limitations do the authors identify across these studies?",
            "Which findings are consistent across the selected papers?",
        ]
        for column, label, prompt in zip(examples, prompts, prompt_text):
            if column.button(label, key=f"prompt_{label}", use_container_width=True):
                st.session_state.research_question = prompt
                st.session_state.submitted_question = ""
                st.rerun()

        can_submit = bool(papers and st.session_state.research_question.strip())
        if st.button(
            "Prepare evidence review",
            type="primary",
            disabled=not can_submit,
            use_container_width=True,
        ):
            st.session_state.submitted_question = st.session_state.research_question.strip()

        if not papers:
            st.caption("Add one or more PDFs in the sidebar to prepare a question.")
        elif not st.session_state.research_question.strip():
            st.caption("Write a question above or choose a starting prompt.")

        if st.session_state.submitted_question:
            st.warning(
                "The backend is not connected. No answer was generated and no paper "
                "content was processed. Your question remains in this session."
            )

    with evidence_column:
        render_panel_heading("02", "Evidence preview", "Source passages will appear here after retrieval is connected.")
        st.markdown(
            '<div class="evidence-empty"><div class="evidence-index">NO SOURCES YET</div>'
            '<h3>Evidence stays close to the answer.</h3>'
            '<p>The connected research pipeline will show quoted passages with paper '
            'titles and page references, so claims can be checked in context.</p>'
            '<div class="citation-sample"><span>EXPECTED CITATION</span>'
            '<strong>Paper title · p. 12</strong></div></div>',
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)
    render_panel_heading("YOUR READING LIST", "Papers in this session", "Uploads are temporary and are not stored on disk.")
    render_paper_list(papers, empty_message="Your reading list is empty. Add papers from the sidebar to begin.")


def render_library(papers: list[PaperRecord]) -> None:
    render_header(
        eyebrow="SOURCE LIBRARY",
        title="Your reading list.",
        description="PDFs selected in this session. They are not yet parsed, indexed, or persisted.",
    )
    render_paper_list(papers, empty_message="No papers in this session yet. Add PDFs using the sidebar.")
    st.info("Paper metadata and extracted text will be available here after ingestion is implemented.")


def render_project_notes() -> None:
    render_header(
        eyebrow="PROJECT NOTES",
        title="Evidence before answers.",
        description="The interface is ready to connect to a research pipeline; the pipeline itself is still under construction.",
    )
    st.markdown(
        '<div class="notes-grid">'
        '<article><span>01 / INGEST</span><h3>Preserve the paper</h3>'
        '<p>Extract text while retaining title, authors, page numbers, and section context.</p></article>'
        '<article><span>02 / RETRIEVE</span><h3>Find relevant passages</h3>'
        '<p>Rank evidence for the question and keep passage provenance attached.</p></article>'
        '<article><span>03 / RESPOND</span><h3>Make claims checkable</h3>'
        '<p>Present a synthesis with citations that point back to the source and page.</p></article>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.caption("For setup, file responsibilities, and integration notes, see frontend/README.md.")


initialize_state()
active_view, uploaded_papers = render_sidebar()

if active_view == "Research desk":
    render_research_desk(uploaded_papers)
elif active_view == "Paper library":
    render_library(uploaded_papers)
else:
    render_project_notes()