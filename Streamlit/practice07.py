import streamlit as st #type:ignore
import random
# Create a simple number guessing game using Streamlit where the user guesses a randomly generated number. 
st.title('Number guessing game')
st.sidebar.title('Game Rules:')
st.sidebar.markdown("""
- Computer choose  secret number  
- User need to correct guess 
- if user not guess right number game restart
""")

if 'target' not in st.session_state:
    st.session_target = random.randint(1,10)

guess = st.number_input('Guess number (1-10)',step=1)
st.write(f'You choose {guess}')

if st.button('Check'):
    if guess == st.session_target:
        st.success(f'Correct You Win')
    else:
        st.error(f'You choose Wrong number\nCorrect number{st.session_target}')

