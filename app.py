import streamlit as st
import pandas as pd
import io

st.title("🚀 Data Combiner & Pivot")

# Inisialisasi state untuk menampung data gabungan
if 'combined_data' not in st.session_state:
    st.session_state.combined_data = pd.DataFrame(columns=['TICKET', 'NOMINAL'])

# Input berkali-kali
raw_data = st.text_area("Tempel data di sini (bisa dilakukan berkali-kali):", height=150)

if st.button("Gabung ke Tabel"):
    try:
        # Memproses data (Filter ID diawali 'D')
        df_input = pd.read_csv(io.StringIO(raw_data), sep='\t', header=None)
        df_clean = df_input[df_input[0].astype(str).str.startswith('D', na=False)].copy()
        df_new = df_clean[[0, 3]].rename(columns={0: 'TICKET', 3: 'NOMINAL'})
        
        # Gabungkan dengan data lama (Pivot/Append)
        st.session_state.combined_data = pd.concat([st.session_state.combined_data, df_new], ignore_index=True)
        st.success("Data berhasil ditambah!")
    except:
        st.error("Gagal! Pastikan format data saat dipaste benar.")

# Tombol Reset
if st.button("Hapus Semua Data"):
    st.session_state.combined_data = pd.DataFrame(columns=['TICKET', 'NOMINAL'])

# Tampilkan tabel yang sudah digabung
if not st.session_state.combined_data.empty:
    st.subheader("Data Gabungan (Siap Copy):")
    st.dataframe(st.session_state.combined_data, use_container_width=True)
    
    # Fitur download
    csv = st.session_state.combined_data.to_csv(index=False).encode('utf-8')
    st.download_button("💾 Download Gabungan (.csv)", csv, "data_gabungan.csv", "text/csv")
