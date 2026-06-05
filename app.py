import streamlit as st
import pandas as pd
import io

st.title("📊 Pivot Data Cleaner (Dual Input)")

# Layout 2 kolom untuk input
col1, col2 = st.columns(2)

with col1:
    data_a = st.text_area("Paste Data 1 (Doc):", height=150)
with col2:
    data_b = st.text_area("Paste Data 2 (Panel):", height=150)

def proses_data(raw):
    try:
        df_input = pd.read_csv(io.StringIO(raw), sep='\t', header=None)
        # Filter hanya yang diawali 'D'
        df_clean = df_input[df_input[0].astype(str).str.startswith('D', na=False)].copy()
        return df_clean[[0, 3]].rename(columns={0: 'TICKET', 3: 'NOMINAL'})
    except:
        return pd.DataFrame(columns=['TICKET', 'NOMINAL'])

if st.button("Pivot & Gabungkan"):
    df_1 = proses_data(data_a)
    df_2 = proses_data(data_b)
    
    # Gabungkan (Pivot/Append)
    df_result = pd.concat([df_1, df_2], ignore_index=True)
    
    # Hapus duplikat (opsional)
    df_result = df_result.drop_duplicates()
    
    st.subheader("Hasil Gabungan:")
    st.dataframe(df_result, use_container_width=True)
    
    # Download
    csv = df_result.to_csv(index=False).encode('utf-8')
    st.download_button("💾 Download Gabungan (.csv)", csv, "data_pivot.csv", "text/csv")
