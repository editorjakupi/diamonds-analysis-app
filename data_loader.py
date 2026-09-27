"""Dataset loading utilities."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def load_diamonds_data() -> pd.DataFrame:
    """Load diamonds CSV, drop index junk, remove impossible zero dimensions."""
    data_path = Path(__file__).parent / "diamonds_dataset" / "diamonds.csv"
    df = pd.read_csv(data_path)
    df = df.loc[:, ~df.columns.str.match(r"^Unnamed")]
    zero_mask = (df[["x", "y", "z"]] == 0).any(axis=1)
    return df.loc[~zero_mask].copy()
