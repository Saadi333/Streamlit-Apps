import streamlit as st

# Title for your app
st.title("Hello World! This is my first Streamlit App")

# Display some text
st.write("This is some text displayed on the app.")

# Get user input with a text box
user_name = st.text_input("Enter your name:")

# Display a greeting based on the user input
if user_name:
    st.write("Hello, ", user_name)
    st.write("Glad you could make it!")
