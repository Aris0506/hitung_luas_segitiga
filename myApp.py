import streamlit as st  
# import pandas as pd

st.write("""
    # Aplikasi hitung Luas Segitiga
    gaskeun sayang
    """)

alas = st.number_input("Masukan Alas", 0)
tinggi = st.number_input("Masukan Tinggi", 0)
hitung = st.button("Hitung Luas")

if hitung:
    st.success("Hello Word")
    luas = 0.5 * alas * tinggi
    # st.success(f"Luas Segitiganya adalah {luas}")
    st.balloons()
# df = pd.read_csv("my_data.csv")
# st.line_chart(df)