import streamlit as st
import pandas as pd
import requests
from datetime import datetime

API_URL = "https://script.google.com/macros/s/AKfycbyoVS3WDvZ2iNXaFH7WmgIK8wCK1o9MOY82btyd3LAXkUrqTMH3H2_5nQufQBze2QPdVQ/exec"

st.title("📊 BRI AGAM BOT - Dashboard")

# 1. Bagian Input Deposit
with st.expander("➕ Input Deposit Baru"):
    with st.form("input_form"):
        nama = st.text_input("Nama Member")
        nominal = st.number_input("Nominal", min_value=0)
        submitted = st.form_submit_button("Kirim Deposit")
        
        if submitted:
            payload = {
                "tanggal": datetime.now().strftime("%Y-%m-%d"),
                "jam": datetime.now().strftime("%H:%M:%S"),
                "nama": nama,
                "nominal": nominal
            }
            requests.post(API_URL, json=payload)
            st.success("Data terkirim! Refresh halaman untuk melihat.")

# 2. Bagian Tampilkan Data
st.subheader("Data Mutasi")
try:
    response = requests.get(API_URL).json()
    df = pd.DataFrame(response)
    st.dataframe(df, use_container_width=True)
except:
    st.info("Menunggu data...")
