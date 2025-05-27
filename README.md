## 🚀 Live Demo

[Öppna Diamonds Analysis App på Streamlit Cloud](https://diamonds-analysis-app-uae8lqradky68cntkehd8j.streamlit.app/)

# Diamonds Analysis App

En interaktiv Streamlit-app för analys av diamanter, utvecklad för Guldfynd.

## Installation

1. Klona repot:

```bash
git clone https://github.com/editorjakupi/diamonds-analysis-app.git
cd diamonds-analysis-app
```

2. Skapa en virtuell miljö och aktivera den:

```bash
python -m venv venv
source venv/bin/activate  # På Windows: venv\Scripts\activate
```

3. Installera beroenden:

```bash
pip install -r requirements.txt
```

## Kör appen lokalt

```bash
streamlit run part2_data_analysis.py
```

## Deployment

Appen är konfigurerad för deployment på Streamlit Cloud:

1. Gå till [Streamlit Cloud](https://streamlit.io/cloud)
2. Logga in med ditt GitHub-konto
3. Klicka på "New app"
4. Välj ditt repo: `editorjakupi/diamonds-analysis-app`
5. Ange sökväg till huvudfilen: `part2_data_analysis.py`
6. Klicka på "Deploy"

## Projektstruktur

```
diamonds-analysis-app/
├── part2_data_analysis.py     # Huvudapplikation
├── create_notebook.py         # Notebook-generator
├── requirements.txt           # Projektberoenden
├── .streamlit/               # Streamlit-konfiguration
│   └── config.toml
├── diamonds_dataset/         # Dataset
│   └── diamonds.csv
└── README.md                 # Denna fil
```

## Funktioner

- Interaktiv dataanalys av diamanter
- Visualiseringar med Plotly
- Filtrering och sökning
- Statistik och insikter
- Beslutsstöd för inköp

## Teknisk stack

- Python 3.9+
- Streamlit
- Pandas
- Plotly
- Scikit-learn
- NumPy
