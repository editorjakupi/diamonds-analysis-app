"""Guldfynd diamonds Streamlit app — entry point for Streamlit Cloud and Docker."""

from __future__ import annotations

import streamlit as st

from data_loader import load_diamonds_data
from section_analysis import render_diamonds_analysis
from section_presentation import render_presentation
from section_upload import render_upload_section
from theme import inject_custom_css, render_app_header

NAV_PRESENTATION = "Presentation"
NAV_ANALYSIS = "Interactive Diamonds Analysis"
NAV_UPLOAD = "Upload Your Data"

st.set_page_config(
    page_title="Diamonds Analysis — Guldfynd",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_custom_css()

with st.sidebar:
    st.markdown("### Navigation")
    section = st.radio(
        "Välj sektion",
        [NAV_PRESENTATION, NAV_ANALYSIS, NAV_UPLOAD],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption(
        "Tema: ljus som standard i `.streamlit/config.toml`. "
        "Byt till mörkt läge via **Settings → Theme** i Streamlit."
    )

render_app_header()

if section == NAV_PRESENTATION:
    render_presentation()
elif section == NAV_ANALYSIS:
    render_diamonds_analysis(load_diamonds_data())
else:
    render_upload_section()
