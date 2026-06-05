import streamlit as st
import gspread
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Mutasi BCA Dashboard", layout="wide")
st.title("📊 Live Mutasi BCA")

# Fungsi untuk mengambil data dari Google Sheets
def get_data():
    # Menggunakan st.secrets agar lebih aman (tidak perlu file credentials.json di GitHub)
    creds_dict = st.secrets["gcp_service_account"]
    gc = gspread.service_account_from_dict(creds_dict)
    
    # Ganti dengan nama file spreadsheet Anda
    sh = gc.open("NAMA_FILE_SPREADSHEET_ANDA") 
    worksheet = sh.sheet1
    
    # Mengambil data
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    
    # Memastikan kolom sesuai urutan
    # Pastikan nama kolom di Google Sheet sama dengan list di bawah
    cols = ["Tanggal", "Jam", "Nama", "Nominal"]
    return df[cols]

# Tampilan utama
try:
    df = get_data()
    
    # Menampilkan tabel dengan gaya yang rapi
    st.dataframe(df, use_container_width=True)
    
    # Tombol refresh manual
    if st.button('Refresh Data Terbaru'):
        st.rerun()
        
except Exception as e:
    st.error(f"Gagal memuat data: {e}")
    st.info("Pastikan nama spreadsheet sudah benar dan Service Account memiliki akses Editor.")
