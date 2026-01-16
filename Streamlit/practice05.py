import streamlit as st #type:ignore

# Create an app that takes text input from the user and displays the total number of characters and words. 

words = st.text_input('Enter Something')

if words:
    st.write('You write:',words)
    st.write('length of word:',len(words))
