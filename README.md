# Diamonds Analysis — Guldfynd

**Live:** [https://diamonds.editorjakupi.com](https://diamonds.editorjakupi.com)  
**Repo:** [github.com/editorjakupi/diamonds-analysis-app](https://github.com/editorjakupi/diamonds-analysis-app)  
**Hosting:** Hetzner CX23 `apps-nbg1` (`23.88.100.144`) — Streamlit in Docker behind shared Caddy + Let’s Encrypt

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

## Deploy (Hetzner)

Production path: `/opt/diamonds` on `apps-nbg1`, container `diamonds-prod-app` on Docker network `deploy_gematrior`. Caddy serves `diamonds.editorjakupi.com`.

```bash
# on VPS
cd /opt/diamonds
docker compose up -d --build
docker exec gematrior-prod-caddy caddy reload --config /etc/caddy/Caddyfile
curl -sI https://diamonds.editorjakupi.com/ | head -5
```

Compose service **must not** be named `app` (that alias collides with Gematrior on the shared network). See `docker-compose.yml`.

Streamlit Community Cloud hosting for this app has been **removed**; GitHub remains the source repo.

---

## Theme helpers

- `streamlit_parent_inject.py` — CSS into parent document  
- `streamlit_theme_widgets.py` / `streamlit_theme_force.py` — widgets + scrollbars  
- `google_translate.py` — themed “Translate page” control (`pageLanguage=en`)
