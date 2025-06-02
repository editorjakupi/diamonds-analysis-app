## 🚀 Live Demo

[Open Diamonds Analysis App on Streamlit Cloud](https://diamonds-analysis-app-uae8lqradky68cntkehd8j.streamlit.app/)

# Diamonds Analysis App

An interactive Streamlit app for diamond analysis, developed for Guldfynd.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/editorjakupi/diamonds-analysis-app.git
cd diamonds-analysis-app
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App Locally

```bash
streamlit run part2_data_analysis.py
```

## Deployment

The app is configured for deployment on Streamlit Cloud:

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Log in with your GitHub account
3. Click on "New app"
4. Select your repository: `editorjakupi/diamonds-analysis-app`
5. Specify the path to the main file: `part2_data_analysis.py`
6. Click on "Deploy"

## Project Structure

```
diamonds-analysis-app/
├── part2_data_analysis.py     # Main application
├── create_notebook.py         # Notebook generator
├── requirements.txt           # Project dependencies
├── .streamlit/               # Streamlit configuration
│   └── config.toml
├── diamonds_dataset/         # Dataset
│   └── diamonds.csv
└── README.md                 # This file
```

## Features

- Interactive diamond data analysis
- Visualizations with Plotly
- Filtering and search
- Statistics and insights
- Decision support for purchasing

## Technical Stack

- Python 3.9+
- Streamlit
- Pandas
- Plotly
- Scikit-learn
- NumPy
