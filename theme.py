"""Diamond theme: bluish light / deep dark + Plotly helpers.

IMPORTANT: never inject <style> via st.html alone — it sandboxes. Use parent inject.
"""

from __future__ import annotations

from typing import Optional
from urllib.parse import quote

import streamlit as st

from streamlit_parent_inject import inject_parent_css
from streamlit_theme_widgets import inject_widget_theme, streamlit_widget_theme_css

THEME_KEY = "diamonds_ui_theme"

DIAMOND_SVG = """
<svg class="lux-diamond" viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <linearGradient id="luxFacetA" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e8f4ff"/>
      <stop offset="45%" stop-color="#7eb8e8"/>
      <stop offset="100%" stop-color="#1e5a8a"/>
    </linearGradient>
    <linearGradient id="luxFacetB" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
      <stop offset="50%" stop-color="#9ec9f0" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#2a6fa3" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="luxFacetC" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" stop-color="#cfe8fc"/>
      <stop offset="100%" stop-color="#0f3d66"/>
    </linearGradient>
    <filter id="luxGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <polygon points="100,8 168,58 100,208 32,58" fill="url(#luxFacetC)" filter="url(#luxGlow)" opacity="0.95"/>
  <polygon points="100,8 168,58 100,78" fill="url(#luxFacetA)" opacity="0.92"/>
  <polygon points="100,8 32,58 100,78" fill="url(#luxFacetB)" opacity="0.88"/>
  <polygon points="32,58 100,78 100,208" fill="#3d7eb0" opacity="0.55"/>
  <polygon points="168,58 100,78 100,208" fill="#1a4d78" opacity="0.65"/>
  <polygon points="32,58 100,8 168,58 140,52 100,28 60,52" fill="#fff" opacity="0.35"/>
  <line x1="100" y1="8" x2="100" y2="208" stroke="#fff" stroke-opacity="0.25" stroke-width="1"/>
  <line x1="32" y1="58" x2="168" y2="58" stroke="#fff" stroke-opacity="0.35" stroke-width="1.2"/>
  <line x1="60" y1="52" x2="100" y2="208" stroke="#fff" stroke-opacity="0.15" stroke-width="1"/>
  <line x1="140" y1="52" x2="100" y2="208" stroke="#fff" stroke-opacity="0.15" stroke-width="1"/>
</svg>
"""


def _diamond_data_uri() -> str:
    """SVG diamond as a CSS-safe data URI (no HTML sanitizer involved)."""
    svg = DIAMOND_SVG.replace('class="lux-diamond" ', "").strip()
    return "data:image/svg+xml;utf8," + quote(svg, safe="")


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
        plot_bgcolor="rgba(10,18,32,0.78)" if is_dark else "rgba(232,242,252,0.92)",
        font=dict(
            family="Fraunces, Georgia, serif",
            color="#e8f0fa" if is_dark else "#0c1a2e",
        ),
        title_font=dict(
            family="Fraunces, Georgia, serif",
            color="#7eb8e8" if is_dark else "#1a4d78",
        ),
        colorway=["#3d7eb0", "#7eb8e8", "#1a4d78", "#c9a227", "#5a8fb8", "#0f3d66"],
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
    if hasattr(st, "html"):
        st.html(markup)
        return
    st.markdown(markup, unsafe_allow_html=True)


def inject_custom_css() -> None:
    """Theme CSS via parent DOM injection (st.html sandboxes styles)."""
    theme = get_theme_base()
    if theme == "dark":
        vars_block = """
:root, .stApp, [data-testid="stAppViewContainer"] {
  --lux-bg-1: #070b14; --lux-bg-2: #0e1626; --lux-bg-3: #152238;
  --lux-surface: rgba(22, 34, 56, 0.94); --lux-border: rgba(126, 184, 232, 0.28);
  --lux-gold: #7eb8e8; --lux-gold-soft: #3d7eb0; --lux-text: #e8f0fa;
  --lux-muted: #a8b8cc; --lux-shadow: 0 22px 56px rgba(0,0,0,0.55); --lux-facet: rgba(126,184,232,0.1);
}
"""
    else:
        # Bluish light mode
        vars_block = """
:root, .stApp, [data-testid="stAppViewContainer"] {
  --lux-bg-1: #e8f2fc; --lux-bg-2: #d4e6f7; --lux-bg-3: #c0d8f0;
  --lux-surface: rgba(255, 255, 255, 0.88); --lux-border: rgba(26, 77, 120, 0.22);
  --lux-gold: #1a4d78; --lux-gold-soft: #3d7eb0; --lux-text: #0c1a2e;
  --lux-muted: #3d5674; --lux-shadow: 0 18px 48px rgba(12, 40, 72, 0.14); --lux-facet: rgba(61,126,176,0.14);
}
"""
    base = """
.stApp {
  background:
    radial-gradient(ellipse 70% 45% at 12% 8%, var(--lux-facet), transparent 55%),
    radial-gradient(ellipse 55% 40% at 92% 6%, rgba(126,184,232,0.22), transparent 50%),
    linear-gradient(168deg, var(--lux-bg-1) 0%, var(--lux-bg-2) 42%, var(--lux-bg-3) 100%);
  color: var(--lux-text) !important;
}
.block-container { padding-top: 1.1rem !important; padding-bottom: 3rem !important; max-width: min(1320px, 96vw) !important; }
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stHeader"] button, [data-testid="stHeader"] span,
[data-testid="stSidebarCollapsedControl"] button, [data-testid="stSidebarCollapsedControl"] span,
[data-testid="stSidebarCollapseButton"] button, [data-testid="stSidebarCollapseButton"] span {
  color: var(--lux-text) !important; -webkit-text-fill-color: var(--lux-text) !important;
}
[data-testid="stSidebar"] {
  background: linear-gradient(185deg, var(--lux-bg-3) 0%, var(--lux-bg-1) 100%);
  border-right: 1px solid var(--lux-border);
}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] li,
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
  color: var(--lux-text) !important;
  -webkit-text-fill-color: var(--lux-text) !important;
  opacity: 1 !important;
  font-family: 'Outfit', system-ui, sans-serif;
}
/* Never override Streamlit's icon font (shows "keyboard_double_arrow_left" as text otherwise) */
[data-testid="stIconMaterial"],
[data-testid="stSidebar"] [data-testid="stIconMaterial"],
.material-symbols-rounded,
span[class*="material-symbols"],
[data-testid="stSidebarCollapseButton"] *,
[data-testid="stExpanderToggleIcon"],
[data-testid="stSidebarCollapsedControl"] * {
  font-family: 'Material Symbols Rounded' !important;
  font-weight: normal !important;
  font-style: normal !important;
  letter-spacing: normal !important;
  text-transform: none !important;
  -webkit-font-feature-settings: 'liga' !important;
  font-feature-settings: 'liga' !important;
  -webkit-font-smoothing: antialiased;
}
.lux-hero-wrap {
  position: relative; overflow: hidden; padding: 2rem 2.1rem 2.15rem; margin: 0 0 1.75rem 0;
  border-radius: 4px; background: linear-gradient(135deg, var(--lux-surface) 0%, transparent 70%), var(--lux-bg-2);
  border: 1px solid var(--lux-border); box-shadow: var(--lux-shadow);
  min-height: 12rem;
}
.lux-hero-inner { position: relative; z-index: 2; max-width: min(36rem, 68%); }
/* Big diamond — CSS background so no HTML sanitizer can strip it */
.lux-hero-wrap::after {
  content: ""; position: absolute; z-index: 1; pointer-events: none;
  right: 1.25rem; top: 50%; transform: translateY(-50%);
  width: clamp(150px, 20vw, 240px); height: clamp(165px, 22vw, 264px);
  background: url("__DIAMOND_URI__") no-repeat center / contain;
  filter: drop-shadow(0 16px 32px rgba(15, 61, 102, 0.38));
}
/* Faint giant diamond watermark bottom-right of the app */
.stApp { isolation: isolate; }
.stApp::before {
  content: ""; position: fixed; z-index: -1; pointer-events: none;
  right: -6vw; bottom: -8vh; width: 44vw; height: 48vw; max-width: 620px; max-height: 680px;
  background: url("__DIAMOND_URI__") no-repeat center / contain;
  opacity: 0.18;
}
.lux-diamond { display: none; }
.lux-kicker { font-family: 'Outfit', system-ui, sans-serif; font-size: 0.7rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; color: var(--lux-gold); margin: 0 0 0.65rem 0; }
.lux-hero { font-family: 'Fraunces', Georgia, serif; font-weight: 600; font-size: clamp(2.2rem, 4vw, 3.1rem); color: var(--lux-text); margin: 0 0 0.55rem 0; }
.lux-hero em { font-style: italic; color: var(--lux-gold); font-weight: 500; }
.lux-tagline { font-family: 'Outfit', system-ui, sans-serif; color: var(--lux-muted); font-size: 1.08rem; max-width: 42rem; line-height: 1.55; margin: 0; }
.lux-section-label { display: inline-block; font-family: 'Outfit', system-ui, sans-serif; font-size: 0.68rem; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: var(--lux-gold); margin: 0.5rem 0 0.25rem 0; }
.lux-section { font-family: 'Fraunces', Georgia, serif !important; font-size: clamp(1.55rem, 2.4vw, 1.95rem) !important; font-weight: 600 !important; color: var(--lux-text) !important; margin: 0.15rem 0 1rem 0 !important; padding-bottom: 0.65rem; border-bottom: 1px solid var(--lux-border); }
h1, h2, h3, [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2, [data-testid="stMarkdownContainer"] h3 {
  font-family: 'Fraunces', Georgia, serif !important; color: var(--lux-text) !important;
  -webkit-text-fill-color: var(--lux-text) !important;
}
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {
  font-family: 'Outfit', system-ui, sans-serif; color: var(--lux-text) !important;
  -webkit-text-fill-color: var(--lux-text) !important; font-size: 1.02rem; line-height: 1.7;
  opacity: 1 !important;
}
div[data-testid="stMetric"] { background: var(--lux-surface); border: 1px solid var(--lux-border); border-radius: 4px; padding: 1rem 1.15rem; box-shadow: var(--lux-shadow); }
div[data-testid="stMetric"] label,
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stMetricDelta"] {
  color: var(--lux-text) !important;
  -webkit-text-fill-color: var(--lux-text) !important;
  opacity: 1 !important;
}
.nav-hint { font-size: 0.84rem; color: var(--lux-muted) !important; -webkit-text-fill-color: var(--lux-muted) !important; line-height: 1.5; }
[data-testid="stVerticalBlockBorderWrapper"] { background: var(--lux-surface); border: 1px solid var(--lux-border) !important; border-radius: 4px; box-shadow: var(--lux-shadow); color: var(--lux-text) !important; }
@media (max-width: 768px) {
  .block-container { padding-left: 0.85rem !important; padding-right: 0.85rem !important; max-width: 100% !important; }
  .lux-hero-wrap { padding: 1.25rem 1.1rem 1.35rem; min-height: 9rem; }
  .lux-hero-inner { max-width: 62%; }
  .lux-diamond { width: clamp(100px, 34vw, 150px); right: -0.75rem; }
  .lux-hero { font-size: clamp(1.7rem, 8vw, 2.3rem); }
  .stButton > button { min-height: 44px !important; width: 100%; }
}
"""
    base = base.replace("__DIAMOND_URI__", _diamond_data_uri())
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
    title_html = title_html or "Diamonds <em>Intelligence</em>"
    tagline = (
        tagline
        or "Data-driven analysis for assortment, pricing and purchasing — from the 4Cs to decisions."
    )
    _inject_html(
        f"""
        <div class="lux-hero-wrap">
          <div class="lux-hero-inner">
            <p class="lux-kicker">{kicker}</p>
            <p class="lux-hero">{title_html}</p>
            <p class="lux-tagline">{tagline}</p>
          </div>
        </div>
        """
    )


def section_heading(label: str, title: str) -> None:
    _inject_html(
        f'<div class="lux-section-label">{label}</div><h2 class="lux-section">{title}</h2>'
    )
