"""Guldfynd diamonds Streamlit app — entry point for Streamlit Cloud and Docker."""

from __future__ import annotations

import streamlit as st

from data_loader import load_diamonds_data
from google_translate import render_translate_sidebar
from section_decision import render_decision_support
from section_presentation import render_presentation
from section_upload import render_upload_section
from streamlit_theme_force import inject_theme_force
from theme import get_theme_base, inject_custom_css, render_app_header, render_theme_toggle, section_heading

# English UI source — Google Translate handles other languages (no hardcoded i18n tables).
NAV_PRESENTATION = "Presentation"
NAV_DECISION = "Decision support"
NAV_UPLOAD = "Upload data"

st.set_page_config(
    page_title="Diamonds Analysis — Guldfynd",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.markdown("### Theme")
    render_theme_toggle()
    st.markdown("---")
    render_translate_sidebar(page_language="en", theme=get_theme_base())
    st.markdown("---")
    st.markdown("### Navigation")
    section = st.radio(
        "Choose section",
        [NAV_PRESENTATION, NAV_DECISION, NAV_UPLOAD],
        label_visibility="collapsed",
        key="diamonds_nav_radio",
    )
    st.markdown("---")
    if section == NAV_DECISION:
        hint = "Decision support helps with assortment, pricing and purchasing from the data."
    elif section == NAV_UPLOAD:
        hint = "Upload your own diamond data and run the same analyses on your file."
    else:
        hint = "Presentation covers background, executive summary and interactive analysis."
    st.markdown(f'<p class="nav-hint">{hint}</p>', unsafe_allow_html=True)

# Single theme inject after sidebar (avoids double-paint flash)
inject_custom_css()
inject_theme_force(get_theme_base(), accent="#3d7eb0", accent_fg="#ffffff")

render_app_header(
    kicker="Guldfynd portfolio",
    title_html="Diamonds <em>Intelligence</em>",
    tagline="Data-driven analysis for assortment, pricing and purchasing — from the 4Cs to decisions.",
)

if section == NAV_PRESENTATION:
    render_presentation()
elif section == NAV_DECISION:
    render_decision_support(load_diamonds_data())
else:
    section_heading("Section", NAV_UPLOAD)
    render_upload_section()
