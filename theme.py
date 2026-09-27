"""Luxury diamond theme: in-app light/dark switch + Plotly helpers."""

from __future__ import annotations

import streamlit as st

THEME_KEY = "diamonds_ui_theme"


def init_theme() -> str:
    if THEME_KEY not in st.session_state:
        st.session_state[THEME_KEY] = "light"
    return st.session_state[THEME_KEY]


def get_theme_base() -> str:
    return init_theme()


def get_plotly_template() -> str:
    return "plotly_dark" if get_theme_base() == "dark" else "plotly_white"


def apply_plotly_theme(fig):
    template = get_plotly_template()
    is_dark = get_theme_base() == "dark"
    fig.update_layout(
        template=template,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(18,18,20,0.55)" if is_dark else "rgba(255,252,247,0.9)",
        font=dict(family="Cormorant Garamond, Georgia, serif", color="#f5f0e8" if is_dark else "#1a1612"),
        title_font=dict(family="Cormorant Garamond, Georgia, serif", color="#C9A227" if is_dark else "#8B6914"),
        colorway=["#C9A227", "#8B7355", "#5C4A32", "#D4AF37", "#A89060", "#6B5344"],
        margin=dict(t=56, r=24, b=40, l=48),
    )
    return fig


def render_theme_toggle() -> str:
    """Sidebar light/dark control. Returns current theme ('light'|'dark')."""
    init_theme()
    choice = st.radio(
        "Appearance",
        ["Light", "Dark"],
        index=0 if st.session_state[THEME_KEY] == "light" else 1,
        horizontal=True,
        key="diamonds_theme_radio",
    )
    st.session_state[THEME_KEY] = "dark" if choice == "Dark" else "light"
    return st.session_state[THEME_KEY]


def inject_custom_css() -> None:
    theme = get_theme_base()
    if theme == "dark":
        vars_block = """
        :root, .stApp, [data-testid="stAppViewContainer"] {
            --lux-bg-1: #0c0b0a;
            --lux-bg-2: #161412;
            --lux-surface: rgba(28, 26, 24, 0.88);
            --lux-border: rgba(201, 162, 39, 0.38);
            --lux-gold: #C9A227;
            --lux-gold-soft: #a89060;
            --lux-text: #f5f0e8;
            --lux-muted: #b8b0a4;
            --lux-shadow: 0 18px 48px rgba(0,0,0,0.45);
        }
        """
    else:
        vars_block = """
        :root, .stApp, [data-testid="stAppViewContainer"] {
            --lux-bg-1: #f7f3ec;
            --lux-bg-2: #ebe4d8;
            --lux-surface: rgba(255, 252, 247, 0.92);
            --lux-border: rgba(139, 105, 20, 0.28);
            --lux-gold: #8B6914;
            --lux-gold-soft: #C9A227;
            --lux-text: #1a1612;
            --lux-muted: #5c5348;
            --lux-shadow: 0 14px 40px rgba(26, 22, 18, 0.1);
        }
        """

    st.markdown(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Source+Sans+3:wght@400;500;600&display=swap" rel="stylesheet">
        <style>
        {vars_block}

        .stApp {{
            background:
              radial-gradient(ellipse 90% 55% at 50% -15%, rgba(201,162,39,0.16), transparent 55%),
              linear-gradient(165deg, var(--lux-bg-1) 0%, var(--lux-bg-2) 48%, var(--lux-bg-1) 100%);
        }}

        .block-container {{
            padding-top: 1.25rem;
            max-width: 1180px;
        }}

        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, var(--lux-bg-2), var(--lux-bg-1));
            border-right: 1px solid var(--lux-border);
        }}

        [data-testid="stSidebar"] * {{
            font-family: 'Source Sans 3', system-ui, sans-serif !important;
        }}

        .lux-hero {{
            font-family: 'Cormorant Garamond', Georgia, serif;
            font-weight: 600;
            font-size: 2.15rem;
            letter-spacing: 0.04em;
            color: var(--lux-gold);
            margin: 0 0 0.25rem 0;
        }}

        .lux-tagline {{
            font-family: 'Source Sans 3', system-ui, sans-serif;
            color: var(--lux-muted);
            font-size: 1.05rem;
            margin: 0 0 1.25rem 0;
        }}

        .lux-hero-wrap {{
            padding: 1.35rem 1.5rem 1.5rem;
            margin-bottom: 1.35rem;
            border-radius: 4px;
            background: var(--lux-surface);
            border: 1px solid var(--lux-border);
            box-shadow: var(--lux-shadow);
            position: relative;
            overflow: hidden;
        }}

        .lux-hero-wrap::after {{
            content: "";
            position: absolute;
            left: 1.5rem;
            bottom: 0;
            width: 72px;
            height: 2px;
            background: linear-gradient(90deg, var(--lux-gold-soft), transparent);
        }}

        .lux-section {{
            font-family: 'Cormorant Garamond', Georgia, serif !important;
            font-size: 1.65rem !important;
            font-weight: 600 !important;
            color: var(--lux-text) !important;
            margin: 2rem 0 0.85rem 0 !important;
            padding-bottom: 0.55rem;
            border-bottom: 1px solid var(--lux-border);
            letter-spacing: 0.02em;
        }}

        .lux-section-label {{
            display: inline-block;
            font-family: 'Source Sans 3', system-ui, sans-serif;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--lux-gold);
            margin-bottom: 0.35rem;
        }}

        h1, h2, h3,
        [data-testid="stMarkdownContainer"] h1,
        [data-testid="stMarkdownContainer"] h2,
        [data-testid="stMarkdownContainer"] h3 {{
            font-family: 'Cormorant Garamond', Georgia, serif !important;
            color: var(--lux-text) !important;
        }}

        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li {{
            font-family: 'Source Sans 3', system-ui, sans-serif;
            color: var(--lux-text);
            line-height: 1.65;
        }}

        div[data-testid="stMetric"] {{
            background: var(--lux-surface);
            border: 1px solid var(--lux-border);
            border-radius: 4px;
            padding: 0.85rem 1rem;
            box-shadow: var(--lux-shadow);
        }}

        div[data-testid="stMetric"] label {{
            color: var(--lux-gold) !important;
            font-family: 'Source Sans 3', system-ui, sans-serif !important;
            letter-spacing: 0.04em;
        }}

        .stButton > button[kind="primary"],
        div[data-testid="stFormSubmitButton"] > button {{
            background: linear-gradient(135deg, #C9A227 0%, #8B6914 100%) !important;
            color: #0c0b0a !important;
            border: none !important;
            border-radius: 4px !important;
            font-family: 'Source Sans 3', system-ui, sans-serif !important;
            font-weight: 600 !important;
            letter-spacing: 0.03em;
        }}

        hr {{
            border-color: var(--lux-border) !important;
        }}

        .nav-hint {{
            font-size: 0.82rem;
            color: var(--lux-muted);
            line-height: 1.45;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_app_header() -> None:
    st.markdown(
        """
        <div class="lux-hero-wrap">
          <p class="lux-hero">Guldfynd · Diamonds Intelligence</p>
          <p class="lux-tagline">Datadriven analys för sortiment, prissättning och inköp.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_heading(label: str, title: str) -> None:
    st.markdown(
        f'<div class="lux-section-label">{label}</div><h2 class="lux-section">{title}</h2>',
        unsafe_allow_html=True,
    )
