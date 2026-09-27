"""Upload CSV or SQLite and run interactive EDA."""

from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from theme import apply_plotly_theme, section_heading


def _read_uploaded_dataframe(uploaded_file) -> pd.DataFrame | None:
    name = uploaded_file.name.lower()
    if name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    if name.endswith(".db") or name.endswith(".sqlite") or name.endswith(".sqlite3"):
        raw = uploaded_file.getvalue()
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
            tmp.write(raw)
            tmp_path = tmp.name
        try:
            conn = sqlite3.connect(tmp_path)
            tables = pd.read_sql(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name",
                conn,
            )
            if tables.empty:
                st.error("SQLite-filen innehåller inga tabeller.")
                conn.close()
                return None
            table_names = tables["name"].tolist()
            if len(table_names) == 1:
                chosen = table_names[0]
            else:
                chosen = st.selectbox("Välj tabell", table_names)
            df = pd.read_sql_query(f'SELECT * FROM "{chosen}"', conn)
            conn.close()
            return df
        finally:
            Path(tmp_path).unlink(missing_ok=True)
    st.error("Stödda format: CSV eller SQLite (.db, .sqlite, .sqlite3).")
    return None


def _show_plotly(fig):
    apply_plotly_theme(fig)
    st.plotly_chart(fig, use_container_width=True)


def render_upload_section() -> None:
    st.markdown(
        "Ladda upp en **CSV**-fil eller **SQLite**-databas (.db) för automatisk explorativ dataanalys."
    )

    uploaded = st.file_uploader(
        "Välj fil",
        type=["csv", "db", "sqlite", "sqlite3"],
        help="Maximal filstorlek enligt Streamlit-inställningar.",
    )

    if uploaded is None:
        st.info("Ingen fil uppladdad ännu. Välj CSV eller SQLite för att börja.")
        return

    df = _read_uploaded_dataframe(uploaded)
    if df is None or df.empty:
        st.warning("Kunde inte läsa data eller datasetet är tomt.")
        return

    st.success(f"Laddade **{len(df):,}** rader och **{len(df.columns)}** kolumner från `{uploaded.name}`.")

    st.subheader("Förhandsvisning")
    st.dataframe(df.head(100), use_container_width=True)

    st.subheader("Datatyper")
    dtype_df = pd.DataFrame(
        {"kolumn": df.dtypes.index.astype(str), "dtype": df.dtypes.astype(str).values}
    )
    st.dataframe(dtype_df, use_container_width=True, hide_index=True)

    st.subheader("Saknade värden")
    missing = df.isnull().sum()
    miss_df = pd.DataFrame({"kolumn": missing.index, "saknade": missing.values})
    st.dataframe(miss_df, use_container_width=True, hide_index=True)
    if missing.sum() == 0:
        st.caption("Inga saknade värden i datasetet.")

    st.subheader("Deskriptiv statistik (numeriska kolumner)")
    num_cols = df.select_dtypes(include="number").columns.tolist()
    if num_cols:
        st.dataframe(df[num_cols].describe().T, use_container_width=True)
    else:
        st.caption("Inga numeriska kolumner hittades.")

    st.subheader("Enkla filter")
    filter_col = st.selectbox(
        "Filtrera på kolumn (valfritt)",
        ["— ingen —"] + list(df.columns),
    )
    work = df.copy()
    if filter_col != "— ingen —":
        series = work[filter_col]
        if pd.api.types.is_numeric_dtype(series):
            lo, hi = float(series.min()), float(series.max())
            if lo == hi:
                st.caption(f"Kolumnen `{filter_col}` har ett enda värde.")
            else:
                rng = st.slider(
                    f"Intervall för `{filter_col}`",
                    min_value=lo,
                    max_value=hi,
                    value=(lo, hi),
                )
                work = work[(work[filter_col] >= rng[0]) & (work[filter_col] <= rng[1])]
        else:
            uniques = series.dropna().astype(str).unique().tolist()
            if len(uniques) > 50:
                st.caption("För många unika värden — visar de 50 common.")
                top = series.value_counts().head(50).index.astype(str).tolist()
                uniques = top
            selected = st.multiselect(f"Värden för `{filter_col}`", uniques)
            if selected:
                work = work[work[filter_col].astype(str).isin(selected)]
        st.metric("Rader efter filter", f"{len(work):,}")

    st.subheader("Visualiseringar")
    cat_cols = work.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    num_work = work.select_dtypes(include="number").columns.tolist()

    if num_work:
        st.markdown("**Histogram (numeriska kolumner)**")
        for col in num_work[:12]:
            fig = px.histogram(
                work,
                x=col,
                nbins=40,
                title=f"Fördelning: {col}",
            )
            _show_plotly(fig)
        if len(num_work) > 12:
            st.caption(f"Visar 12 av {len(num_work)} numeriska kolumner.")

    if cat_cols:
        st.markdown("**Stapeldiagram (kategoriska kolumner)**")
        for col in cat_cols[:8]:
            counts = work[col].astype(str).value_counts().head(20).reset_index()
            counts.columns = [col, "antal"]
            fig = px.bar(counts, x=col, y="antal", title=f"Frekvens: {col}")
            _show_plotly(fig)
        if len(cat_cols) > 8:
            st.caption(f"Visar 8 av {len(cat_cols)} kategoriska kolumner.")

    if len(num_work) >= 2:
        st.subheader("Korrelationsheatmap")
        corr = work[num_work].corr(numeric_only=True)
        fig = px.imshow(
            corr,
            labels=dict(color="Korrelation"),
            x=corr.columns,
            y=corr.columns,
            color_continuous_scale="RdBu_r",
            aspect="auto",
            title="Korrelation mellan numeriska variabler",
        )
        _show_plotly(fig)
