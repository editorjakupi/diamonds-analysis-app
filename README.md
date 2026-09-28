# Diamonds Analysis — Guldfynd

**Live:** [Streamlit Cloud](https://diamonds-analysis-app-uae8lqradky68cntkehd8j.streamlit.app/)

Interactive Streamlit app for diamond assortment / pricing analysis (NBI course project).

---

## Current version

- **English UI chrome** as Google Translate source language (default **English**, then switch languages — no hardcoded EN/SV toggle)
- **Light / Dark** theme with parent-DOM CSS (readable labels, upload Browse button, scrollbars)
- **Translate picker** themed for light and dark (not a black select in light mode)
- **Sections:** Presentation · Decision support · Upload data (CSV / SQLite EDA)
- **Mobile:** responsive padding, 44px buttons

Deep presentation/decision copy may still include Swedish analyst prose in places; use Translate to read in another language.

---

## Run locally

```bash
git clone https://github.com/editorjakupi/diamonds-analysis-app.git
cd diamonds-analysis-app
python -m venv venv
# Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run part2_data_analysis.py
```

---

## Deploy

**Streamlit Cloud:** main file `part2_data_analysis.py`  
**Render:** see `render.yaml` / Docker

---

## Theme helpers

- `streamlit_parent_inject.py` — CSS into parent document  
- `streamlit_theme_widgets.py` / `streamlit_theme_force.py` — widgets + scrollbars  
- `google_translate.py` — themed “Translate page” control (`pageLanguage=en`)
