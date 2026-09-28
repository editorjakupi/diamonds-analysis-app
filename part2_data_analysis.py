"""Guldfynd diamonds Streamlit app — entry point for Streamlit Cloud and Docker."""

from __future__ import annotations

import streamlit as st

from data_loader import load_diamonds_data
from google_translate import inject_google_translate
from section_decision import render_decision_support
from section_presentation import render_presentation
from section_upload import render_upload_section
from theme import inject_custom_css, render_app_header, render_theme_toggle, section_heading

# Fixed Swedish UI labels — Google Translate handles other languages.
NAV_PRESENTATION = "Presentation"
NAV_DECISION = "Beslutstöd"
NAV_UPLOAD = "Ladda upp data"

st.set_page_config(
    page_title="Diamonds Analysis — Guldfynd",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.markdown("### Översätt")
    inject_google_translate(page_language="sv")
    st.markdown("---")
    st.markdown("### Navigation")
    section = st.radio(
        "Välj sektion",
        [NAV_PRESENTATION, NAV_DECISION, NAV_UPLOAD],
        label_visibility="collapsed",
        key="diamonds_nav_radio",
    )
    st.markdown("---")
    st.markdown("### Tema")
    render_theme_toggle()
    st.markdown("---")
    if section == NAV_DECISION:
        hint = "Beslutstöd hjälper till med sortiment, prissättning och inköp utifrån datan."
    elif section == NAV_UPLOAD:
        hint = "Ladda upp egen diamantedata och kör samma analyser på din fil."
    else:
        hint = "Presentation inkluderar bakgrund, executive summary och interaktiv analys."
    st.markdown(f'<p class="nav-hint">{hint}</p>', unsafe_allow_html=True)

inject_custom_css()
render_app_header(
    kicker="Guldfynd portfolio",
    title_html="Diamonds <em>Intelligence</em>",
    tagline="Datadriven analys för sortiment, prissättning och inköp — från 4C till affärsbeslut.",
)

if section == NAV_PRESENTATION:
    render_presentation()
elif section == NAV_DECISION:
    render_decision_support(load_diamonds_data())
else:
    section_heading("Sektion", NAV_UPLOAD)
    render_upload_section()
