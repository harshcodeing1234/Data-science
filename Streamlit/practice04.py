import streamlit as st #type:ignore
import random

# Write a program where clicking a button displays a random motivational quote.
 
st.title('Digital Motivational quotes')
st.write('click button to get motivation')
quotes = [
    "Believe in yourself!",
    "Keep pushing forward.",
    "Success is not final; failure is not fatal.",
    "Dream big and dare to fail."
]

if st.button('Motivational quotes'):
    st.success(random.choice(quotes))
    