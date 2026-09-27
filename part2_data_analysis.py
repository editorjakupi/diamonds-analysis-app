"""Guldfynd diamonds Streamlit app — entry point for Streamlit Cloud and Docker."""

from __future__ import annotations

import streamlit as st

from data_loader import load_diamonds_data
from section_decision import render_decision_support
from section_presentation import render_presentation
from section_upload import render_upload_section
from theme import inject_custom_css, render_app_header, render_theme_toggle, section_heading

NAV_PRESENTATION = "Presentation"
NAV_DECISION = "Beslutstöd"
NAV_UPLOAD = "Upload Your Data"

st.set_page_config(
    page_title="Diamonds Analysis — Guldfynd",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.markdown("### Navigation")
    section = st.radio(
        "Välj sektion",
        [NAV_PRESENTATION, NAV_DECISION, NAV_UPLOAD],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("### Theme")
    render_theme_toggle()
    st.markdown("---")
    st.markdown(
        '<p class="nav-hint">Presentation inkluderar bakgrund, executive summary '
        "och interaktiv analys. Beslutstöd och uppladdning är egna sektioner.</p>",
        unsafe_allow_html=True,
    )

inject_custom_css()
render_app_header()

if section == NAV_PRESENTATION:
    render_presentation()
elif section == NAV_DECISION:
    render_decision_support(load_diamonds_data())
else:
    section_heading("Sektion", "Upload Your Data")
    render_upload_section()
