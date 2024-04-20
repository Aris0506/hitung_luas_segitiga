import streamlit as st
import pandas as pd
import numpy as np

# sidebar, (home, dataframe, chart)
option = st.sidebar.selectbox (
    "Silahkan Pilih",
    ("Home", "DataFrame", 'Chart')
)

if option == "Home" or option == "":
    st.write("""# Halaman Utama""")  #displays the main page
elif option == "DataFrame":
    st.write("""## Dataframe""") # displays the title of the dataframe page
    
    # create a dataframe with pandas consisting of 4 rows 2 columns
    df = pd.DataFrame ({
        'Coloumn 1': [1,2,3,4],
        'Coloumn 2': [10,12,14,16]
    })
    df #displays dataframe
elif option == "Chart":
    st.write("""## Draw Charts""") #Displays the title page chart
    
    # create a data variable that contains data from the dataframe
    # data berupa angka acak yang di generate menggunakan numpy/data in the form of random numbers generated using numpy.
    # data terdiri dari 2 kolom dan 20 baris
    chart_data = pd.DataFrame (
        np.random.randn(20, 2),
        columns = ["a", "b"]
    )
    # displays the data in chart form
    st.line_chart(chart_data)
    #data dalam bentuk tabel
    chart_data
    
    
    
    # referensi https://informatics.uii.ac.id/2021/03/15/streamlit-membuat-aplikasi-web-sains-data/