import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import pandas as pd
import streamlit as st

from ingestion.ingest import load_excel
from preprocessing.clean import normalize_columns, clean_data, add_features
from anomaly_detection.detect import detect_anomalies
from insights.narrator import generate_insight

st.set_page_config(page_title="OpsSight Dashboard", layout="wide")

st.title(" OpsSight – Operational Intelligence Dashboard")

uploaded_file = st.file_uploader("Upload Operational Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    df = normalize_columns(df)
    df = clean_data(df)
    df = add_features(df)

    df = detect_anomalies(df)

    st.subheader("Processed Data")
    st.dataframe(df)

    anomalies = df[df["is_anomaly"] == 1]

    st.subheader("Detected Anomalies")
    if anomalies.empty:
        st.info("No significant anomalies detected.")
    else:
        st.dataframe(anomalies)

    st.subheader("AI-Generated Insights")
    if anomalies.empty:
        st.write("No insights generated.")
    else:
        for _, row in anomalies.iterrows():
            st.markdown(f"- {generate_insight(row)}")
