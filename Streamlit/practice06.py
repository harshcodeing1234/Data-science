import streamlit as st #type:ignore
# Create a Streamlit app that checks whether a given number is even or odd. 

st.title('Even odd Num checker')

num = st.number_input('Enter a number',value=0)

if num % 2 ==0:
    st.write(f'{num} is Even number')
else:
    st.write(f'{num} is odd number')