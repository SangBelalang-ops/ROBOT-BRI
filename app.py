import streamlit as st
import pandas as pd
import re

st.title("⚡ Data Cleaner - BRI AGAM")

# Kotak Input
raw_data = st.text_area("Paste data berantakan di sini:", height=200)

if st.button("Bersihkan Data"):
    # Logika untuk mencari ID Tiket dan Nominal
    # Asumsi: ID Tiket adalah angka, Nominal adalah angka di akhir atau setelah ID
    # Kita pakai regex untuk mengambil pola (bisa disesuaikan nanti)
    lines = raw_data.split('\n')
    cleaned_data = []
    
    for line in lines:
        if line.strip():
            # Cari angka (contoh: ID tiket 10 digit, nominal angka panjang)
            # Ini contoh regex, nanti tinggal kita sesuaikan dengan format tiket Anda
            matches = re.findall(r'\d+', line)
            if len(matches) >= 2:
                cleaned_data.append({
                    "Tiket ID": matches[0],
                    "Nominal": matches[1]
                })
    
    # Tampilkan Tabel
    if cleaned_data:
        df = pd.DataFrame(cleaned_data)
        st.table(df)
        st.success("Data berhasil dibersihkan!")
    else:
        st.error("Data tidak dikenali. Coba paste ulang!")
