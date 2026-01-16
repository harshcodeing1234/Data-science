import streamlit as st #type:ignore
# Create a Streamlit app that takes a user’s name as input and displays apersonalized greeting. 

name = st.text_input("Enter your name:")

if name:
    st.success(f"Welcome {name}")
    st.write(f"Welcome {name}")
