## Live demo

[Open Diamonds Analysis on Streamlit Cloud](https://diamonds-analysis-app-uae8lqradky68cntkehd8j.streamlit.app/)

After deploying to Render, add your always-on URL here.

# Diamonds Analysis — Guldfynd

Interaktiv Streamlit-app för diamantanalys (kunskapskontroll, NBI Handlesakademin). Svensk analystext och affärsinsikter bevaras från originalprojektet.

## Tre sektioner (sidopanel)

1. **Presentation** — bakgrund, de 4 C:na och executive summary / data storytelling.
2. **Interactive Diamonds Analysis** — full analys (sektion 3–12): statistik, Plotly-diagram, interaktiv filtrering och beslutsstöd *Ska vi köpa diamanten?*
3. **Upload Your Data** — ladda upp CSV eller SQLite (`.db`) och få automatisk EDA: förhandsvisning, datatyper, saknade värden, `describe`, histogram, stapeldiagram och korrelationsheatmap.

## Kör lokalt

```bash
git clone https://github.com/editorjakupi/diamonds-analysis-app.git
cd diamonds-analysis-app
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
streamlit run part2_data_analysis.py
```

## Deploy

### Streamlit Cloud

1. [Streamlit Cloud](https://streamlit.io/cloud) → **New app**
2. Repo: `editorjakupi/diamonds-analysis-app`
3. Main file: `part2_data_analysis.py`
4. Deploy

### Render (always-on Web Service)

1. Skapa ny **Web Service** och koppla repot, eller använd `render.yaml` (Docker).
2. Render sätter `PORT`; Dockerfile kör Streamlit på `0.0.0.0`.
3. Free tier kan spinna down vid inaktivitet; uppgradera för strikt always-on.

### Docker lokalt

```bash
docker build -t diamonds-analysis .
docker run -p 8501:8501 -e PORT=8501 diamonds-analysis
```

Öppna http://localhost:8501

## Projektstruktur

```
├── part2_data_analysis.py   # Entry (Streamlit Cloud / Docker)
├── theme.py                 # CSS + Plotly-tema
├── data_loader.py
├── section_presentation.py
├── section_analysis.py
├── section_upload.py
├── diamonds_dataset/diamonds.csv
├── kunskapskontroll.ipynb
├── .streamlit/config.toml
├── Dockerfile
├── render.yaml
└── requirements.txt
```

## Stack

- Python 3.9+
- Streamlit
- Pandas, NumPy, SciPy
- Plotly

Committa aldrig `.env` eller andra hemligheter.

## Always-on

- **Streamlit Cloud** hosts the live demo and auto-redeploys from `main`.
- GitHub Action **Keep Streamlit Awake** pings the app every 10 minutes so the free tier stays reachable.
- For dedicated always-on containers, use `Dockerfile` / `render.yaml` on Render or Railway.

