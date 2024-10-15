import streamlit as st
import random

# Title of the app
st.title("Random Number Generator")

# Display some text
st.write("Click the button to generate a random number between 1 and 100!")

# Button to generate a random number
if st.button("Generate Random Number"):
    random_number = random.randint(1, 100)
    st.success(f"Random Number: {random_number}")

# Run the app with: streamlit run your_script.py

