import streamlit as st #type:ignore

with st.form('User_info'):
    name = st.text_input('Enter Name:')
    age = st.number_input('Enter age:',min_value=1)
    email = st.text_input('Enter Email:')
    submit = st.form_submit_button("Submit")

if submit:
    st.write(f'Name:{name}\nAge:{age}\nEmail:{email}')