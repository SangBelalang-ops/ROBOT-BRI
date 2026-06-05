import streamlit as st
import pandas as pd

# Masukkan link CSV hasil Publish to web di sini
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTv0RRg3nakuAvSwDSWi8Vc8BCukKV6CrqSidGQ6FuDh7Vf7LqA9qxFXNPn2hOe-yuaW9kbFa7JJKJw/pub?gid=177426029&single=true&output=csv"

st.title("📊 BRI AGAM BOT")
df = pd.read_csv(CSV_URL)
st.dataframe(df, use_container_width=True)
