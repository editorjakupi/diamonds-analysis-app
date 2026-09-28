"""Luxury diamond theme: in-app light/dark + Plotly helpers.

IMPORTANT: never inject <style> via st.markdown — Streamlit strips the tag and
prints CSS as visible page text. Always use st.html.
"""

from __future__ import annotations

from typing import Optional

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
        plot_bgcolor="rgba(12,14,18,0.72)" if is_dark else "rgba(255,250,245,0.92)",
        font=dict(
            family="Fraunces, Georgia, serif",
            color="#f4efe6" if is_dark else "#1c1410",
        ),
        title_font=dict(
            family="Fraunces, Georgia, serif",
            color="#e8c547" if is_dark else "#7a5a12",
        ),
        colorway=["#C9A227", "#8B7355", "#5C4A32", "#D4AF37", "#A89060", "#6B5344"],
        margin=dict(t=56, r=28, b=44, l=52),
    )
    fig.update_layout(modebar_remove=["lasso2d", "select2d"])
    return fig


def render_theme_toggle() -> str:
    from i18n import t

    init_theme()
    choice = st.radio(
        t("appearance"),
        [t("appearance_light"), t("appearance_dark")],
        index=0 if st.session_state[THEME_KEY] == "light" else 1,
        horizontal=True,
        key="diamonds_theme_radio",
    )
    dark_label = t("appearance_dark")
    st.session_state[THEME_KEY] = "dark" if choice == dark_label else "light"
    return st.session_state[THEME_KEY]


def _inject_html(markup: str) -> None:
    """Inject HTML/CSS. Prefer st.html; never st.markdown for <style>."""
    if hasattr(st, "html"):
        st.html(markup)
        return
    st.error(
        "Streamlit ≥ 1.33 required (st.html). Upgrade so theme CSS is not shown as text."
    )


def inject_custom_css() -> None:
    theme = get_theme_base()
    if theme == "dark":
        vars_block = """
        :root, .stApp, [data-testid="stAppViewContainer"] {
            --lux-bg-1: #0a0908;
            --lux-bg-2: #14110f;
            --lux-bg-3: #1c1814;
            --lux-surface: rgba(32, 28, 24, 0.92);
            --lux-border: rgba(232, 197, 71, 0.32);
            --lux-gold: #e8c547;
            --lux-gold-soft: #c9a227;
            --lux-text: #f4efe6;
            --lux-muted: #b5aa9a;
            --lux-shadow: 0 22px 56px rgba(0,0,0,0.55);
            --lux-facet: rgba(232,197,71,0.08);
        }
        """
    else:
        vars_block = """
        :root, .stApp, [data-testid="stAppViewContainer"] {
            --lux-bg-1: #f8f4ee;
            --lux-bg-2: #efe7da;
            --lux-bg-3: #e4d8c6;
            --lux-surface: rgba(255, 252, 247, 0.94);
            --lux-border: rgba(122, 90, 18, 0.26);
            --lux-gold: #7a5a12;
            --lux-gold-soft: #c9a227;
            --lux-text: #1c1410;
            --lux-muted: #5e5348;
            --lux-shadow: 0 18px 48px rgba(28, 20, 16, 0.12);
            --lux-facet: rgba(201,162,39,0.1);
        }
        """

    _inject_html(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
        <style>
        {vars_block}

        .stApp {{
            background:
              radial-gradient(ellipse 70% 45% at 12% 8%, var(--lux-facet), transparent 55%),
              radial-gradient(ellipse 55% 40% at 88% 12%, rgba(201,162,39,0.12), transparent 50%),
              linear-gradient(168deg, var(--lux-bg-1) 0%, var(--lux-bg-2) 42%, var(--lux-bg-3) 100%);
            color: var(--lux-text);
        }}

        .block-container {{
            padding-top: 1.1rem !important;
            padding-bottom: 3rem !important;
            max-width: min(1320px, 96vw) !important;
        }}

        [data-testid="stSidebar"] {{
            background:
              linear-gradient(185deg, var(--lux-bg-3) 0%, var(--lux-bg-1) 100%);
            border-right: 1px solid var(--lux-border);
        }}

        [data-testid="stSidebar"] * {{
            font-family: 'Outfit', system-ui, sans-serif !important;
        }}

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {{
            font-family: 'Outfit', system-ui, sans-serif !important;
            font-size: 0.72rem !important;
            letter-spacing: 0.16em !important;
            text-transform: uppercase !important;
            color: var(--lux-gold) !important;
            font-weight: 600 !important;
        }}

        .lux-hero-wrap {{
            position: relative;
            overflow: hidden;
            padding: 2rem 2.1rem 2.15rem;
            margin: 0 0 1.75rem 0;
            border-radius: 2px;
            background:
              linear-gradient(135deg, var(--lux-surface) 0%, transparent 70%),
              var(--lux-bg-2);
            border: 1px solid var(--lux-border);
            box-shadow: var(--lux-shadow);
        }}

        .lux-hero-wrap::before {{
            content: "";
            position: absolute;
            inset: 0 auto 0 0;
            width: 4px;
            background: linear-gradient(180deg, var(--lux-gold-soft), transparent 85%);
        }}

        .lux-hero-wrap::after {{
            content: "";
            position: absolute;
            right: -40px;
            top: -40px;
            width: 180px;
            height: 180px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(201,162,39,0.18), transparent 68%);
            pointer-events: none;
        }}

        .lux-kicker {{
            font-family: 'Outfit', system-ui, sans-serif;
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            color: var(--lux-gold);
            margin: 0 0 0.65rem 0;
        }}

        .lux-hero {{
            font-family: 'Fraunces', Georgia, serif;
            font-weight: 600;
            font-size: clamp(2.2rem, 4vw, 3.1rem);
            letter-spacing: -0.02em;
            line-height: 1.1;
            color: var(--lux-text);
            margin: 0 0 0.55rem 0;
        }}

        .lux-hero em {{
            font-style: italic;
            color: var(--lux-gold);
            font-weight: 500;
        }}

        .lux-tagline {{
            font-family: 'Outfit', system-ui, sans-serif;
            color: var(--lux-muted);
            font-size: 1.08rem;
            max-width: 42rem;
            line-height: 1.55;
            margin: 0;
        }}

        .lux-section-label {{
            display: inline-block;
            font-family: 'Outfit', system-ui, sans-serif;
            font-size: 0.68rem;
            font-weight: 600;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: var(--lux-gold);
            margin: 0.5rem 0 0.25rem 0;
        }}

        .lux-section {{
            font-family: 'Fraunces', Georgia, serif !important;
            font-size: clamp(1.55rem, 2.4vw, 1.95rem) !important;
            font-weight: 600 !important;
            color: var(--lux-text) !important;
            margin: 0.15rem 0 1rem 0 !important;
            padding-bottom: 0.65rem;
            border-bottom: 1px solid var(--lux-border);
            letter-spacing: -0.01em;
        }}

        h1, h2, h3,
        [data-testid="stMarkdownContainer"] h1,
        [data-testid="stMarkdownContainer"] h2,
        [data-testid="stMarkdownContainer"] h3 {{
            font-family: 'Fraunces', Georgia, serif !important;
            color: var(--lux-text) !important;
            letter-spacing: -0.015em;
        }}

        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li {{
            font-family: 'Outfit', system-ui, sans-serif;
            color: var(--lux-text);
            font-size: 1.02rem;
            line-height: 1.7;
            max-width: 68ch;
        }}

        div[data-testid="stMetric"] {{
            background: var(--lux-surface);
            border: 1px solid var(--lux-border);
            border-radius: 2px;
            padding: 1rem 1.15rem;
            box-shadow: var(--lux-shadow);
        }}

        div[data-testid="stMetric"] label {{
            color: var(--lux-gold) !important;
            font-family: 'Outfit', system-ui, sans-serif !important;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            font-size: 0.72rem !important;
        }}

        .stButton > button[kind="primary"],
        div[data-testid="stFormSubmitButton"] > button {{
            background: linear-gradient(135deg, #d4af37 0%, #8B6914 100%) !important;
            color: #0c0b0a !important;
            border: none !important;
            border-radius: 2px !important;
            font-family: 'Outfit', system-ui, sans-serif !important;
            font-weight: 600 !important;
            letter-spacing: 0.04em;
        }}

        hr {{ border-color: var(--lux-border) !important; }}

        .nav-hint {{
            font-size: 0.84rem;
            color: var(--lux-muted);
            line-height: 1.5;
            font-family: 'Outfit', system-ui, sans-serif;
        }}

        /* Make analysis insight blocks breathe */
        [data-testid="stVerticalBlockBorderWrapper"] {{
            background: var(--lux-surface);
            border: 1px solid var(--lux-border) !important;
            border-radius: 2px;
            box-shadow: var(--lux-shadow);
        }}

        /* Dark / light: form widgets, expanders, tabs, dataframes */
        .stTextInput input, .stNumberInput input, .stTextArea textarea,
        [data-baseweb="select"] > div, [data-baseweb="input"] input,
        .stSelectbox div[data-baseweb="select"] > div,
        .stMultiSelect div[data-baseweb="select"] > div {{
            background-color: var(--lux-surface) !important;
            color: var(--lux-text) !important;
            border-color: var(--lux-border) !important;
        }}
        label, .stMarkdown, .stCaption, [data-testid="stWidgetLabel"] p,
        [data-testid="stRadio"] label, [data-testid="stCheckbox"] label {{
            color: var(--lux-text) !important;
        }}
        [data-testid="stExpander"] details,
        [data-testid="stExpander"] summary {{
            background: var(--lux-surface) !important;
            color: var(--lux-text) !important;
            border-color: var(--lux-border) !important;
        }}
        [data-testid="stDataFrame"], [data-testid="stTable"] {{
            background: var(--lux-surface) !important;
            color: var(--lux-text) !important;
        }}
        .stTabs [data-baseweb="tab-list"] {{
            background: transparent !important;
            gap: 0.35rem;
        }}
        .stTabs [data-baseweb="tab"] {{
            color: var(--lux-muted) !important;
            background: var(--lux-surface) !important;
            border-radius: 2px !important;
        }}
        .stTabs [aria-selected="true"] {{
            color: var(--lux-gold) !important;
            border-bottom: 2px solid var(--lux-gold) !important;
        }}
        div[data-testid="stSidebar"] .stRadio label span {{
            color: var(--lux-text) !important;
        }}
        [data-testid="stFileUploader"] section {{
            background: var(--lux-surface) !important;
            border-color: var(--lux-border) !important;
            color: var(--lux-text) !important;
        }}
        .stSlider [data-baseweb="slider"] {{
            color: var(--lux-text) !important;
        }}

        /* Force BaseWeb / Streamlit internals in dark mode */
        .stApp, [data-testid="stAppViewContainer"],
        [data-testid="stHeader"], section[data-testid="stSidebar"] {{
            color: var(--lux-text) !important;
            color-scheme: { "dark" if theme == "dark" else "light" };
        }}
        div[data-baseweb="base-input"],
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"],
        .stNumberInput div[data-baseweb="input"] > div,
        input, textarea, select {{
            background-color: var(--lux-surface) !important;
            color: var(--lux-text) !important;
            -webkit-text-fill-color: var(--lux-text) !important;
            caret-color: var(--lux-text) !important;
            border-color: var(--lux-border) !important;
        }}
        [data-baseweb="popover"] ul,
        [data-baseweb="menu"],
        [role="listbox"],
        [data-baseweb="popover"] li {{
            background-color: var(--lux-bg-2) !important;
            color: var(--lux-text) !important;
        }}
        .stAlert, [data-testid="stNotification"],
        [data-testid="stMetricValue"],
        [data-testid="stMetricDelta"] {{
            color: var(--lux-text) !important;
        }}
        /* Google Translate chrome */
        .goog-te-banner-frame, .skiptranslate iframe.goog-te-banner-frame {{ display: none !important; }}
        body {{ top: 0 !important; }}
        .goog-logo-link, .goog-te-gadget span {{ display: none !important; }}
        .goog-te-gadget {{ font-size: 0 !important; }}
        #google_translate_element select {{
            font-size: 0.85rem !important;
            min-height: 36px;
            padding: 0.25rem 0.5rem;
        }}

        @media (max-width: 768px) {{
            .block-container {{
                padding-left: 0.85rem !important;
                padding-right: 0.85rem !important;
                max-width: 100% !important;
            }}
            .lux-hero-wrap {{
                padding: 1.25rem 1.1rem 1.35rem;
                margin-bottom: 1.1rem;
            }}
            .lux-hero {{
                font-size: clamp(1.7rem, 8vw, 2.3rem);
            }}
            .lux-tagline {{
                font-size: 0.95rem;
            }}
            [data-testid="stSidebar"] {{
                min-width: min(100vw, 18rem);
            }}
            div[data-testid="stHorizontalBlock"] {{
                flex-wrap: wrap !important;
            }}
            .stButton > button {{
                min-height: 44px !important;
                width: 100%;
            }}
        }}
        </style>
        """
    )


def render_app_header(
    kicker: Optional[str] = None,
    title_html: Optional[str] = None,
    tagline: Optional[str] = None,
) -> None:
    kicker = kicker or "Guldfynd portfolio"
    title_html = title_html or 'Diamonds <em>Intelligence</em>'
    tagline = tagline or "Datadriven analys för sortiment, prissättning och inköp — från 4C till affärsbeslut."
    _inject_html(
        f"""
        <div class="lux-hero-wrap">
          <p class="lux-kicker">{kicker}</p>
          <p class="lux-hero">{title_html}</p>
          <p class="lux-tagline">{tagline}</p>
        </div>
        """
    )


def section_heading(label: str, title: str) -> None:
    _inject_html(
        f'<div class="lux-section-label">{label}</div><h2 class="lux-section">{title}</h2>'
    )
