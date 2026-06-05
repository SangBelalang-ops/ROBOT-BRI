import streamlit as st
import pandas as pd
import io

st.title("✂️ Data Cleaner - Anti Sampah")

raw_data = st.text_area("Paste data dari Excel di sini:", height=200)

if st.button("Proses Data"):
    # Membaca data sebagai file CSV/Tab Separated
    df_input = pd.read_csv(io.StringIO(raw_data), sep='\t', header=None)
    
    # Ambil kolom yang relevan (misal kolom 0 untuk Tiket, kolom 3 untuk Nominal)
    # Kita filter supaya cuma baris yang ID-nya diawali 'D' yang masuk
    df_clean = df_input[df_input[0].astype(str).str.startswith('D', na=False)].copy()
    
    # Ambil kolom 0 (Tiket) dan kolom 3 (Nominal)
    df_final = df_clean[[0, 3]].rename(columns={0: 'TICKET', 3: 'NOMINAL'})
    
    # Tampilkan
    st.table(df_final)
    
    # Download
    csv = df_final.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "data_bersih.csv", "text/csv")
