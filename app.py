import streamlit as st
import pandas as pd
import requests

# Masukkan URL yang Anda copy dari langkah 2 di sini
API_URL = "https://script.google.com/macros/s/AKfycbyR4ar-u8TwY1fVThk65yEiJkn4RMm9hbjXmiJA2k6PEG4JuEUxDMEgxs6TE0Z-E-DXlA/exec"

st.title("BRI AGAM BOT")

try:
    response = requests.get(API_URL).json()
    df = pd.DataFrame([response])
    st.table(df)
except:
    st.error("Gagal ambil data. Pastikan URL sudah benar.")
