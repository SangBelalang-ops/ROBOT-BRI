import streamlit as st
import pandas as pd
import re
import io

st.title("🧹 Pembersih Data Tiket & Nominal")

# Instruksi buat user
st.write("Silakan paste data mentah Anda di kotak bawah ini:")
raw_data = st.text_area("Paste Data Di Sini:", height=300, placeholder="Paste data berantakan di sini...")

if st.button("Bersihkan & Download CSV"):
    if raw_data:
        rows = []
        # Memproses baris demi baris
        lines = raw_data.split('\n')
        for line in lines:
            # 1. Cari Tiket: Pola huruf 'D' diikuti deretan angka
            tiket_match = re.search(r'D\d+', line)
            
            # 2. Cari Nominal: Cari angka yang formatnya ribuan (misal 50.000 atau 50000)
            # Kita cari angka yang paling kanan di baris tersebut
            nominals = re.findall(r'[\d\.,]+', line)
            
            if tiket_match and nominals:
                # Mengambil nominal yang paling mungkin benar (angka terbesar atau angka di posisi akhir)
                nominal_clean = nominals[-1].replace('.', '').replace(',', '')
                
                # Pastikan nominalnya murni angka
                if nominal_clean.isdigit():
                    rows.append({
                        "TICKET": tiket_match.group(0),
                        "NOMINAL": nominal_clean
                    })
        
        if rows:
            df = pd.DataFrame(rows)
            st.success(f"Berhasil membersihkan {len(df)} data!")
            st.table(df)
            
            # Konversi ke CSV untuk Download
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Klik di sini untuk Download CSV",
                data=csv,
                file_name='data_bersih.csv',
                mime='text/csv'
            )
        else:
            st.warning("Data tidak ditemukan! Pastikan format data mengandung ID yang diawali 'D'.")
    else:
        st.error("Kotak masih kosong! Masukkan data terlebih dahulu.")
