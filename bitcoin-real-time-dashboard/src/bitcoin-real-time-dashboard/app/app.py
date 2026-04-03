# =========================
# FIX IMPORT PATH (WAJIB)
# =========================
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# =========================
# IMPORT LIBRARY
# =========================
import streamlit as st
import pandas as pd

from src.model import train_model
from src.feature_engineering import create_features

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(
    page_title="Bitcoin Dashboard",
    page_icon="🚀",
    layout="wide"
)

# =========================
# TITLE
# =========================
st.title("🚀 Bitcoin Real-Time Dashboard")

# =========================
# LOAD DATA
# =========================
try:
    df = pd.read_csv("data/btc_live.csv")
except FileNotFoundError:
    st.error("❌ File data tidak ditemukan. Jalankan dulu data_save.py")
    st.stop()

# =========================
# FEATURE ENGINEERING
# =========================
df = create_features(df)

if df.empty:
    st.warning("⚠️ Data masih sedikit. Kumpulkan data dulu (Day 2)")
    st.stop()

# =========================
# METRIC (PRICE)
# =========================
latest_price = df.iloc[-1]["price"]
st.metric("💰 Current BTC Price", f"{latest_price:.2f} USD")

# =========================
# CHART
# =========================
st.subheader("📈 Price & Moving Average")

st.line_chart(df[["price", "ma5", "ma10"]])

# =========================
# DATA TABLE
# =========================
st.subheader("📊 Latest Data")
st.dataframe(df.tail())

# =========================
# MODEL
# =========================
st.subheader("🤖 Price Prediction")

model = train_model()

if model is not None:
    latest = df.iloc[-1]

    prediction = model.predict([[
        latest["lag1"],
        latest["ma5"],
        latest["ma10"],
        latest["volatility"]
    ]])

    st.success(f"📌 Predicted Next Price: {prediction[0]:.2f} USD")
else:
    st.error("❌ Model belum bisa dijalankan (data kurang)")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Built with Python, Streamlit & Machine Learning 🚀")