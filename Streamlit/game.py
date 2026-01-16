import streamlit as st #type:ignore
import random
import os

# Page title
st.title("Snake Water Gun Game")

st.sidebar.title("Game Rules")

st.sidebar.markdown("""
- Snake beats Water  
- Water beats Gun  
- Gun beats Snake  

**Same choice = Draw**

Win → +1 point  
High score is saved
""")


# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0

if "started" not in st.session_state:
    st.session_state.started = False

# Start game button
if not st.session_state.started:
    if st.button("Start Game"):
        st.session_state.started = True
        st.session_state.score = 0

# Game logic
if st.session_state.started:
    st.subheader("Choose your option")

    options = {
        1: "Snake",
        2: "Water",
        3: "Gun"
    }

    user_option = st.radio(
        "Your Choice:",
        options=list(options.keys()),
        format_func=lambda x: options[x]
    )

    if st.button("Play"):
        computer_option = random.randint(1, 3)

        st.write(f"**Your choice:** {options[user_option]}")
        st.write(f"**Computer choice:** {options[computer_option]}")

        # Draw
        if user_option == computer_option:
            st.info("Game Draw")

        # Win conditions
        elif (
            (user_option == 1 and computer_option == 2) or
            (user_option == 2 and computer_option == 3) or
            (user_option == 3 and computer_option == 1)
        ):
            st.success("You Win")
            st.session_state.score += 1

        # Loss
        else:
            st.error("You Lose")

        st.write(f"### Current Score: {st.session_state.score}")

        # High score handling
        if not os.path.exists("hiscore.txt"):
            with open("hiscore.txt", "w") as f:
                f.write("0")

        with open("hiscore.txt", "r") as f:
            hiscore = int(f.read())

        if st.session_state.score >= hiscore:
            with open("hiscore.txt", "w") as f:
                f.write(str(st.session_state.score))
            hiscore = st.session_state.score

        st.write(f"🏆 **High Score:** {hiscore}")

    # Restart button
    if st.button("Restart Game"):
        st.session_state.score = 0
        st.session_state.started = False
