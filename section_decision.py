"""Beslutstöd: ska vi köpa diamanten? — egen sektion."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from theme import section_heading


def render_decision_support(df: pd.DataFrame) -> None:
    section_heading("Sektion", "Beslutstöd")
    st.markdown(
        "Syfte: Hjälpa styrelsen att fatta datadrivna beslut om inköp av enskilda "
        "diamanter baserat på marknadsreferensen i datasetet."
    )

    cut_order = ["Ideal", "Premium", "Very Good", "Good", "Fair"]
    color_order = ["D", "E", "F", "G", "H", "I", "J"]
    clarity_order = ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"]

    @st.cache_data
    def get_reference_stats(frame: pd.DataFrame) -> pd.DataFrame:
        ref = (
            frame.groupby(["cut", "color", "clarity"])[["price", "carat"]]
            .median()
            .reset_index()
        )
        ref["price_per_carat"] = ref["price"] / ref["carat"]
        return ref

    reference_stats = get_reference_stats(df)

    def should_buy_diamond(
        carat, cut, color, clarity, price, depth, table, x, y, z, frame, reference_stats
    ):
        if carat <= 0 or price <= 0 or x <= 0 or y <= 0 or z <= 0:
            return (
                "Nej",
                "Ogiltiga värden: carat, pris och dimensioner måste vara större än 0.",
            )
        for col, val in zip(
            ["carat", "price", "depth", "table", "x", "y", "z"],
            [carat, price, depth, table, x, y, z],
        ):
            Q1 = frame[col].quantile(0.25)
            Q3 = frame[col].quantile(0.75)
            IQR = Q3 - Q1
            if val < (Q1 - 1.5 * IQR) or val > (Q3 + 1.5 * IQR):
                return (
                    "Nej",
                    f"{col}={val} är ett extremvärde jämfört med marknaden. "
                    "Undvik köp utan manuell granskning.",
                )
        ref_row = reference_stats[
            (reference_stats["cut"] == cut)
            & (reference_stats["color"] == color)
            & (reference_stats["clarity"] == clarity)
        ]
        if not ref_row.empty:
            ref_ppc = ref_row.iloc[0]["price_per_carat"]
            ppc = price / carat
            if ppc > ref_ppc * 1.2:
                return (
                    "Nej",
                    f"Priset per carat ({ppc:.0f} USD) är mer än 20% högre än medianen "
                    f"för denna kvalitet ({ref_ppc:.0f} USD). Undvik köp.",
                )
            if ppc < ref_ppc * 0.7:
                return (
                    "Ja",
                    f"Priset per carat ({ppc:.0f} USD) är lågt jämfört med marknaden "
                    "för denna kvalitet. Möjligt fynd!",
                )
            return (
                "Ja",
                f"Priset per carat ({ppc:.0f} USD) är rimligt för denna kvalitet.",
            )
        return (
            "Nej",
            "Kombinationen av cut, color och clarity är ovanlig i marknaden. "
            "Kräver manuell granskning.",
        )

    with st.form("diamond_decision_form"):
        st.subheader("Fatta beslut om enskild diamant")
        col1, col2, col3 = st.columns(3)
        with col1:
            carat = st.number_input(
                "Vikt (carat)", min_value=0.01, max_value=5.0, value=0.5, step=0.01
            )
            price = st.number_input(
                "Pris (USD)", min_value=1, max_value=100000, value=3000, step=1
            )
            cut = st.selectbox("Slipning (cut)", cut_order)
        with col2:
            color = st.selectbox("Färg (color)", color_order)
            clarity = st.selectbox("Klarhet (clarity)", clarity_order)
            depth = st.number_input(
                "Djup (%)", min_value=40.0, max_value=80.0, value=61.0, step=0.1
            )
        with col3:
            table = st.number_input(
                "Tavla (%)", min_value=40.0, max_value=100.0, value=57.0, step=0.1
            )
            x = st.number_input(
                "Längd (x, mm)", min_value=0.1, max_value=15.0, value=5.0, step=0.01
            )
            y = st.number_input(
                "Bredd (y, mm)", min_value=0.1, max_value=15.0, value=5.0, step=0.01
            )
            z = st.number_input(
                "Höjd (z, mm)", min_value=0.1, max_value=10.0, value=3.2, step=0.01
            )
        submitted = st.form_submit_button("Få rekommendation")
        if submitted:
            beslut, motivering = should_buy_diamond(
                carat,
                cut,
                color,
                clarity,
                price,
                depth,
                table,
                x,
                y,
                z,
                df,
                reference_stats,
            )
            if beslut == "Ja":
                st.success(f"Rekommendation: {beslut}")
            else:
                st.warning(f"Rekommendation: {beslut}")
            st.info(f"Motivering: {motivering}")
