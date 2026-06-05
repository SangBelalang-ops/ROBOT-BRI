import streamlit as st
import pandas as pd
import io

st.title("✂️ Data Cleaner - Manual Fix")

raw_data = st.text_area("Paste data Excel/Tabel di sini:", height=200)

if raw_data:
    # Membaca data sebagai tabel (menganggap kolom dipisah oleh Tab/Spasi)
    try:
        df = pd.read_csv(io.StringIO(raw_data), sep='\t', header=None)
        st.write("Coba lihat tabel ini, kolom mana yang isinya Tiket & Nominal?")
        st.dataframe(df)
        
        # User input manual nomor kolom (index)
        col1, col2 = st.columns(2)
        tiket_idx = col1.number_input("Kolom Tiket (index ke-):", min_value=0, max_value=len(df.columns)-1, value=0)
        nominal_idx = col2.number_input("Kolom Nominal (index ke-):", min_value=0, max_value=len(df.columns)-1, value=1)
        
        if st.button("Bersihkan Sekarang"):
            df_final = df[[tiket_idx, nominal_idx]].copy()
            df_final.columns = ['TICKET', 'NOMINAL']
            
            # Membersihkan Nominal (buang titik/koma)
            df_final['NOMINAL'] = df_final['NOMINAL'].replace(r'[^\d]', '', regex=True)
            
            st.success("Tabel sudah rapi!")
            st.table(df_final)
            
            csv = df_final.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download", csv, "hasil_rapi.csv", "text/csv")
            
    except Exception as e:
        st.error(f"Gagal baca data. Pastikan di-paste dengan benar. Error: {e}")
