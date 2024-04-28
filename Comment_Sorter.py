import streamlit as st
from textblob import TextBlob

# Set page title
st.title("Positive-Negitive-Comment-Sorter")

# Text input for user to enter their comment
user_input = st.text_input("Enter your comment:")

# Function to perform sentiment analysis
def analyze_sentiment(comment):
    analysis = TextBlob(comment)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Perform sentiment analysis when user submits their comment
if st.button("Analyze"):
    if user_input:
        sentiment = analyze_sentiment(user_input)
        st.write(f"Sentiment: {sentiment}")
    else:
        st.error("Please enter a comment.")
