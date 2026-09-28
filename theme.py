"""Luxury diamond theme: in-app light/dark + Plotly helpers.

IMPORTANT: never inject <style> via st.markdown — Streamlit strips the tag and
prints CSS as visible page text. Always use st.html.
"""

from __future__ import annotations

from typing import Optional

import streamlit as st

from streamlit_parent_inject import inject_parent_css
from streamlit_theme_widgets import inject_widget_theme, streamlit_widget_theme_css

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


def _inject_html(markup: str) -> None:
    """Inject small HTML snippets (heroes/headings) into the app."""
    if hasattr(st, "html"):
        st.html(markup)
        return
    st.markdown(markup, unsafe_allow_html=True)


def inject_custom_css() -> None:
    """Luxury theme CSS via parent DOM injection (st.html sandboxes styles)."""
    theme = get_theme_base()
    if theme == "dark":
        vars_block = """
:root, .stApp, [data-testid="stAppViewContainer"] {
  --lux-bg-1: #0a0908; --lux-bg-2: #14110f; --lux-bg-3: #1c1814;
  --lux-surface: rgba(32, 28, 24, 0.92); --lux-border: rgba(232, 197, 71, 0.32);
  --lux-gold: #e8c547; --lux-gold-soft: #c9a227; --lux-text: #f4efe6;
  --lux-muted: #b5aa9a; --lux-shadow: 0 22px 56px rgba(0,0,0,0.55); --lux-facet: rgba(232,197,71,0.08);
}
"""
    else:
        vars_block = """
:root, .stApp, [data-testid="stAppViewContainer"] {
  --lux-bg-1: #f8f4ee; --lux-bg-2: #efe7da; --lux-bg-3: #e4d8c6;
  --lux-surface: rgba(255, 252, 247, 0.94); --lux-border: rgba(122, 90, 18, 0.26);
  --lux-gold: #7a5a12; --lux-gold-soft: #c9a227; --lux-text: #1c1410;
  --lux-muted: #5e5348; --lux-shadow: 0 18px 48px rgba(28, 20, 16, 0.12); --lux-facet: rgba(201,162,39,0.1);
}
"""
    base = """
.stApp {
  background:
    radial-gradient(ellipse 70% 45% at 12% 8%, var(--lux-facet), transparent 55%),
    radial-gradient(ellipse 55% 40% at 88% 12%, rgba(201,162,39,0.12), transparent 50%),
    linear-gradient(168deg, var(--lux-bg-1) 0%, var(--lux-bg-2) 42%, var(--lux-bg-3) 100%);
  color: var(--lux-text) !important;
}
.block-container { padding-top: 1.1rem !important; padding-bottom: 3rem !important; max-width: min(1320px, 96vw) !important; }
[data-testid="stSidebar"] {
  background: linear-gradient(185deg, var(--lux-bg-3) 0%, var(--lux-bg-1) 100%);
  border-right: 1px solid var(--lux-border);
}
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
  color: var(--lux-text) !important;
  -webkit-text-fill-color: var(--lux-text) !important;
  opacity: 1 !important;
  font-family: 'Outfit', system-ui, sans-serif !important;
}
.lux-hero-wrap {
  position: relative; overflow: hidden; padding: 2rem 2.1rem 2.15rem; margin: 0 0 1.75rem 0;
  border-radius: 2px; background: linear-gradient(135deg, var(--lux-surface) 0%, transparent 70%), var(--lux-bg-2);
  border: 1px solid var(--lux-border); box-shadow: var(--lux-shadow);
}
.lux-kicker { font-family: 'Outfit', system-ui, sans-serif; font-size: 0.7rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: var(--lux-gold); margin: 0 0 0.65rem 0; }
.lux-hero { font-family: 'Fraunces', Georgia, serif; font-weight: 600; font-size: clamp(2.2rem, 4vw, 3.1rem); color: var(--lux-text); margin: 0 0 0.55rem 0; }
.lux-hero em { font-style: italic; color: var(--lux-gold); font-weight: 500; }
.lux-tagline { font-family: 'Outfit', system-ui, sans-serif; color: var(--lux-muted); font-size: 1.08rem; max-width: 42rem; line-height: 1.55; margin: 0; }
.lux-section-label { display: inline-block; font-family: 'Outfit', system-ui, sans-serif; font-size: 0.68rem; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: var(--lux-gold); margin: 0.5rem 0 0.25rem 0; }
.lux-section { font-family: 'Fraunces', Georgia, serif !important; font-size: clamp(1.55rem, 2.4vw, 1.95rem) !important; font-weight: 600 !important; color: var(--lux-text) !important; margin: 0.15rem 0 1rem 0 !important; padding-bottom: 0.65rem; border-bottom: 1px solid var(--lux-border); }
h1, h2, h3, [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2, [data-testid="stMarkdownContainer"] h3 {
  font-family: 'Fraunces', Georgia, serif !important; color: var(--lux-text) !important;
}
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {
  font-family: 'Outfit', system-ui, sans-serif; color: var(--lux-text) !important; font-size: 1.02rem; line-height: 1.7;
}
div[data-testid="stMetric"] { background: var(--lux-surface); border: 1px solid var(--lux-border); border-radius: 2px; padding: 1rem 1.15rem; box-shadow: var(--lux-shadow); }
.nav-hint { font-size: 0.84rem; color: var(--lux-muted) !important; line-height: 1.5; }
[data-testid="stVerticalBlockBorderWrapper"] { background: var(--lux-surface); border: 1px solid var(--lux-border) !important; border-radius: 2px; box-shadow: var(--lux-shadow); }
@media (max-width: 768px) {
  .block-container { padding-left: 0.85rem !important; padding-right: 0.85rem !important; max-width: 100% !important; }
  .lux-hero-wrap { padding: 1.25rem 1.1rem 1.35rem; }
  .lux-hero { font-size: clamp(1.7rem, 8vw, 2.3rem); }
  .stButton > button { min-height: 44px !important; width: 100%; }
}
"""
    inject_parent_css(
        "@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Outfit:wght@400;500;600&display=swap');\n"
        + vars_block
        + base
        + streamlit_widget_theme_css(theme, prefix="diamonds"),
        style_id="diamonds-theme-css",
    )
    inject_widget_theme(theme, prefix="diamonds")



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
