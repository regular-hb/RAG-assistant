"""Small reusable Streamlit rendering functions for the application views."""

from __future__ import annotations

import streamlit as st

from frontend.ui_helpers import PaperRecord, format_file_size


def render_header(eyebrow: str, title: str, description: str) -> None:
    """Render the shared page heading used by each workspace view."""
    st.markdown(
        f'<header class="page-heading"><p class="eyebrow">{eyebrow}</p>'
        f'<h1>{title}</h1><p class="page-description">{description}</p></header>',
        unsafe_allow_html=True,
    )


def render_panel_heading(number: str, title: str, description: str) -> None:
    """Render a numbered section heading within the research desk."""
    st.markdown(
        f'<div class="panel-heading"><span>{number}</span><div><h2>{title}</h2>'
        f'<p>{description}</p></div></div>',
        unsafe_allow_html=True,
    )


def render_status(label: str, tone: str = "pending", sidebar: bool = False) -> None:
    """Show a concise status indicator; tone selects a CSS color token."""
    sidebar_class = " status-sidebar" if sidebar else ""
    st.markdown(
        f'<div class="status-line{sidebar_class}"><span class="status-dot status-{tone}"></span>'
        f'<span>{label}</span></div>',
        unsafe_allow_html=True,
    )


def render_paper_list(papers: list[PaperRecord], empty_message: str) -> None:
    """Render upload metadata without reading or persisting document contents."""
    if not papers:
        st.markdown(f'<div class="empty-list">{empty_message}</div>', unsafe_allow_html=True)
        return

    for paper in papers:
        st.markdown(
            '<div class="paper-row"><span class="pdf-mark">PDF</span>'
            f'<div class="paper-copy"><strong>{_escape_html(paper.name)}</strong>'
            f'<small>{format_file_size(paper.size_bytes)} · Ready for ingestion</small></div>'
            '<span class="paper-state">IN SESSION</span></div>',
            unsafe_allow_html=True,
        )


def _escape_html(value: str) -> str:
    """Escape filenames before placing them in the small HTML presentation layer."""
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#x27;")
    )