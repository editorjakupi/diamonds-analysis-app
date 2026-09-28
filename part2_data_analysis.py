"""Guldfynd diamonds Streamlit app — entry point for Streamlit Cloud and Docker."""

from __future__ import annotations

import streamlit as st

from data_loader import load_diamonds_data
from google_translate import inject_google_translate
from i18n import hint_for_section, render_lang_toggle, t
from section_decision import render_decision_support
from section_presentation import render_presentation
from section_upload import render_upload_section
from theme import inject_custom_css, render_app_header, render_theme_toggle, section_heading

st.set_page_config(
    page_title="Diamonds Analysis — Guldfynd",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.markdown(f"### {t('translate_title')}")
    inject_google_translate(page_language="sv")
    st.markdown("---")
    st.markdown(f"### {t('lang_title')}")
    render_lang_toggle()
    st.markdown("---")
    st.markdown(f"### {t('nav_title')}")
    section = st.radio(
        t("nav_label"),
        [t("nav_presentation"), t("nav_decision"), t("nav_upload")],
        label_visibility="collapsed",
        key="diamonds_nav_radio",
    )
    st.markdown("---")
    st.markdown(f"### {t('theme_title')}")
    render_theme_toggle()
    st.markdown("---")
    st.markdown(
        f'<p class="nav-hint">{hint_for_section(section)}</p>',
        unsafe_allow_html=True,
    )

inject_custom_css()
render_app_header(kicker=t("kicker"), title_html=t("hero_title"), tagline=t("tagline"))

if section == t("nav_presentation"):
    render_presentation()
elif section == t("nav_decision"):
    render_decision_support(load_diamonds_data())
else:
    section_heading(t("section_label"), t("nav_upload"))
    render_upload_section()
