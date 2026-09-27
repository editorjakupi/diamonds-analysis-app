"""Luxury theme: CSS (light/dark) and Plotly template helpers."""

from __future__ import annotations

import streamlit as st


def get_theme_base() -> str:
    """Return Streamlit theme base: 'light' or 'dark'."""
    try:
        base = st.get_option("theme.base")
        if base in ("light", "dark"):
            return base
    except Exception:
        pass
    return "light"


def get_plotly_template() -> str:
    return "plotly_dark" if get_theme_base() == "dark" else "plotly_white"


def apply_plotly_theme(fig):
    """Apply Streamlit-aware Plotly template and gold-friendly defaults."""
    template = get_plotly_template()
    fig.update_layout(
        template=template,
        font=dict(family="Georgia, 'Playfair Display', serif"),
        title_font=dict(family="Georgia, 'Playfair Display', serif"),
    )
    return fig


def inject_custom_css() -> None:
    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&display=swap" rel="stylesheet">
        <style>
        :root {
            --lux-charcoal: #1c1c1e;
            --lux-ivory: #faf8f5;
            --lux-gold: #C4A35A;
            --lux-gold-muted: #8B7355;
            --lux-border: rgba(196, 163, 90, 0.35);
            --lux-card-bg: rgba(250, 248, 245, 0.92);
            --lux-text: #1c1c1e;
            --lux-text-muted: #4a4a4a;
        }
        [data-theme="dark"] {
            --lux-charcoal: #0f0f10;
            --lux-ivory: #1a1a1c;
            --lux-gold: #C4A35A;
            --lux-gold-muted: #a8906a;
            --lux-border: rgba(196, 163, 90, 0.45);
            --lux-card-bg: rgba(28, 28, 30, 0.85);
            --lux-text: #f5f3ef;
            --lux-text-muted: #c8c4bc;
        }
        .lux-hero {
            font-family: 'Playfair Display', Georgia, serif;
            font-weight: 600;
            letter-spacing: 0.02em;
            color: var(--lux-gold);
            border-bottom: 1px solid var(--lux-border);
            padding-bottom: 0.35rem;
            margin-bottom: 1rem;
        }
        h1, h2, h3, [data-testid="stMarkdownContainer"] h1,
        [data-testid="stMarkdownContainer"] h2,
        [data-testid="stMarkdownContainer"] h3 {
            font-family: 'Playfair Display', Georgia, serif !important;
            color: var(--lux-text) !important;
        }
        [data-testid="stSidebar"] {
            border-right: 1px solid var(--lux-border);
        }
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] label {
            font-family: Georgia, serif;
        }
        div[data-testid="stMetric"] {
            background: var(--lux-card-bg);
            border: 1px solid var(--lux-border);
            border-radius: 8px;
            padding: 0.75rem 1rem;
        }
        div[data-testid="stMetric"] label {
            color: var(--lux-gold-muted) !important;
        }
        .stButton > button[kind="primary"],
        div[data-testid="stFormSubmitButton"] > button {
            background: linear-gradient(135deg, var(--lux-gold) 0%, var(--lux-gold-muted) 100%) !important;
            color: var(--lux-charcoal) !important;
            border: none !important;
            font-family: Georgia, serif;
        }
        hr {
            border-color: var(--lux-border) !important;
        }
        .lux-tagline {
            color: var(--lux-text-muted);
            font-family: Georgia, serif;
            font-size: 1.05rem;
            margin-top: -0.5rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_app_header() -> None:
    st.markdown(
        '<p class="lux-hero">💎 Guldfynd · Diamonds Intelligence</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="lux-tagline">Datadriven analys för sortiment, prissättning och inköp.</p>',
        unsafe_allow_html=True,
    )
