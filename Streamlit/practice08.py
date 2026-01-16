import streamlit as st #type:ignore

st.title('Temperature converter')

choice = st.radio('Convert',["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

temp = st.number_input('Enter Temperature:')

if choice == 'Celcius to fehrenhiet':
    st.write('Result',(temp * 9/5) + 32)
else:
    st.write('Result',(temp - 32) * 5/9)