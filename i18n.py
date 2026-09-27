"""Lightweight EN/SV strings for the Diamonds Streamlit app."""

from __future__ import annotations

import streamlit as st

LANG_KEY = "diamonds_ui_lang"

MESSAGES = {
    "en": {
        "nav_title": "Navigation",
        "nav_label": "Choose section",
        "theme_title": "Theme",
        "lang_title": "Language",
        "nav_presentation": "Presentation",
        "nav_decision": "Decision support",
        "nav_upload": "Upload your data",
        "nav_hint": (
            "Presentation covers background, executive summary and interactive analysis. "
            "Decision support and upload are separate sections."
        ),
        "kicker": "Guldfynd portfolio",
        "hero_title": 'Diamonds <em>Intelligence</em>',
        "tagline": "Data-driven analysis for assortment, pricing and purchasing — from the 4Cs to business decisions.",
        "section_label": "Section",
        "appearance_light": "Light",
        "appearance_dark": "Dark",
        "appearance": "Appearance",
    },
    "sv": {
        "nav_title": "Navigation",
        "nav_label": "Välj sektion",
        "theme_title": "Tema",
        "lang_title": "Språk",
        "nav_presentation": "Presentation",
        "nav_decision": "Beslutstöd",
        "nav_upload": "Ladda upp data",
        "nav_hint": (
            "Presentation inkluderar bakgrund, executive summary "
            "och interaktiv analys. Beslutstöd och uppladdning är egna sektioner."
        ),
        "kicker": "Guldfynd portfolio",
        "hero_title": 'Diamonds <em>Intelligence</em>',
        "tagline": "Datadriven analys för sortiment, prissättning och inköp — från 4C till affärsbeslut.",
        "section_label": "Sektion",
        "appearance_light": "Ljust",
        "appearance_dark": "Mörkt",
        "appearance": "Utseende",
    },
}


def init_lang() -> str:
    if LANG_KEY not in st.session_state:
        st.session_state[LANG_KEY] = "sv"
    return st.session_state[LANG_KEY]


def t(key: str) -> str:
    lang = init_lang()
    return MESSAGES.get(lang, MESSAGES["en"]).get(key, MESSAGES["en"].get(key, key))


def render_lang_toggle() -> str:
    init_lang()
    choice = st.radio(
        t("lang_title"),
        ["Svenska", "English"],
        index=0 if st.session_state[LANG_KEY] == "sv" else 1,
        horizontal=True,
        key="diamonds_lang_radio",
        label_visibility="collapsed",
    )
    st.session_state[LANG_KEY] = "sv" if choice == "Svenska" else "en"
    return st.session_state[LANG_KEY]
