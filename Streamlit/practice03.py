import streamlit as st #type:ignore


# Build a Streamlit app that accepts two numbers and displays their sum, diƯerence, product, and quotient. 
st.title('Digital calculator')
st.write('You can apply Addition, Substraction, Product and Division')
num1 = st.number_input('Enter First number',value=0.0)
num2 = st.number_input('Enter second number',value=0.0)

st.write(f'Sum = {num1 + num2}')
st.write(f'Diffrence = {num1 - num2}')
st.write(f'Product = {num1 * num2}')
st.write()

if num2!=0:
    st.write(f'Devide = {num1 / num2}')
else:
    st.warning('Cannot allow division by Zero')