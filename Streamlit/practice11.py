# Build a Streamlit app that generates a line chart from user-provided numeric data. 
import streamlit as st #type:ignore
import pandas as pd #type:ignore

chart_data = {
    'product':['Watch','Earbuds','Laptop','Phone'],
    'Price':[1200,4500,56000,56789]

}
df = pd.DataFrame(chart_data)
df = df.set_index('product')
st.line_chart(df)