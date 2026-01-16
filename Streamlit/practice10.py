import streamlit as st #type:ignore
import pandas as pd #type:ignore

st.title('Sales Info')
csv_file = st.file_uploader('Upload a csv file',type='csv')

if csv_file is not None:
    df = pd.read_csv(csv_file,encoding="latin1")
    st.write(df.head(10))
    st.write("Mean")
    st.write(df.mean(numeric_only=True))
    st.write("Median")
    st.write(df.median(numeric_only=True))
    st.write("Standard Deviation")
    st.write(df.std(numeric_only=True))
