import streamlit as st
import gspread
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Mutasi BCA Dashboard", layout="wide")
st.title("📊 Live Mutasi BCA")

# Fungsi untuk mengambil data dari Google Sheets
def get_data():
    creds_dict = st.secrets["gcp_service_account"]
    gc = gspread.service_account_from_dict(creds_dict)
    
    # Buka spreadsheet
    sh = gc.open("NAMA_FILE_SPREADSHEET_ANDA") 
    # Buka sheet dengan nama spesifik
    worksheet = sh.worksheet("BOT MUT")
    
    # Ambil data dari range spesifik
    # C7:D7 = Tanggal dan Waktu
    # G7:H7 = Nama dan Nominal
    data_tanggal_waktu = worksheet.get("C7:D7")[0]
    data_nama_nominal = worksheet.get("G7:H7")[0]
    
    # Gabungkan menjadi satu baris data
    row = {
        "Tanggal": data_tanggal_waktu[0],
        "Jam": data_tanggal_waktu[1],
        "Nama": data_nama_nominal[0],
        "Nominal": data_nama_nominal[1]
    }
    
    # Balikkan dalam bentuk DataFrame agar tabel rapi
    return pd.DataFrame([row])
    
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
