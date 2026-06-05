import streamlit as st
import pandas as pd
import io

st.title("✂️ Data Cleaner - Copyable")

raw_data = st.text_area("Paste data di sini:", height=200)

if st.button("Bersihkan & Siapkan Copy"):
    try:
        # Memproses data
        df_input = pd.read_csv(io.StringIO(raw_data), sep='\t', header=None)
        df_clean = df_input[df_input[0].astype(str).str.startswith('D', na=False)].copy()
        df_final = df_clean[[0, 3]].rename(columns={0: 'TICKET', 3: 'NOMINAL'})
        
        # Tampilkan
        st.table(df_final)
        
        # Opsi 1: Download File
        csv = df_final.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", csv, "data_bersih.csv", "text/csv")
        
        # Opsi 2: Teks untuk di-copy manual (Tampilkan dalam text_area agar bisa diblok)
        st.subheader("Copy Teks di Bawah Ini:")
        st.text_area("Hasil Copy:", value=df_final.to_string(index=False), height=200)
        
    except Exception as e:
        st.error("Gagal memproses. Pastikan data di-copy dengan benar dari Excel!")
