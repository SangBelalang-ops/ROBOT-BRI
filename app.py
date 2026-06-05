import streamlit as st
import pandas as pd
import re

st.title("✂️ Data Cleaner - Anti Ribet")

# Penjelasan singkat buat Anda
st.write("Paste data berantakan (Tiket & Nominal) di bawah ini:")

raw_data = st.text_area("Data di sini:", height=200, placeholder="Contoh: Tiket 123456789 Nominal 50000...")

if st.button("Hapus Sampah & Rapikan"):
    lines = raw_data.split('\n')
    data_bersih = []
    
    for line in lines:
        if not line.strip(): continue # Skip baris kosong
        
        # LOGIKA: Ambil angka pertama sebagai TIKET, angka kedua sebagai NOMINAL
        # Ini akan mengabaikan spasi, huruf, dan simbol di antaranya
        angka_angka = re.findall(r'\d+', line.replace('.', '').replace(',', ''))
        
        if len(angka_angka) >= 2:
            data_bersih.append({
                "TICKET": angka_angka[0],
                "NOMINAL": angka_angka[1]
            })
    
    if data_bersih:
        df = pd.DataFrame(data_bersih)
        st.table(df)
        # Tombol Download kalau mau dipindah ke Excel
        st.download_button("Download jadi CSV", df.to_csv(index=False), "data_bersih.csv", "text/csv")
    else:
        st.error("Data ga kebaca! Pastikan ada dua angka di setiap baris.")
