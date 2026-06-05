import streamlit as st
import pandas as pd

# Masukkan link Google Sheets Anda di sini (setelah di-Publish to Web sebagai CSV)
# Caranya: File > Share > Publish to web > Pilih format CSV
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkVpVI1olnVwUmSli1Gm88rmmkWk-z0ZlzcXPALnlSJh4u5cLXHR46p4eqVHX_R4iSSkE9bb4PLn8r/pubhtml?gid=1051785416&single=true"

st.title("BRI AGAM BOT")

def load_data():
    return pd.read_csv(SHEET_URL)

try:
    df = load_data()
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.write("Belum ada data atau link salah. Coba cek link CSV Anda.")
