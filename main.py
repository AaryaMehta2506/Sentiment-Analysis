import streamlit as st
import pandas as pd
import requests

# Flask endpoint for prediction
prediction_endpoint = "http://127.0.0.1:5000/predict"

st.title("Text Sentiment Predictor")

# Text input for sentiment prediction
user_input = st.text_input("Enter text", "")

# Slider for rating input
rating = st.slider("Rate the sentiment (1 to 5)", min_value=1, max_value=5, step=1)

# Prediction on single sentence
if st.button("Predict"):
    # Send request to Flask server with user input and rating
    response = requests.post(prediction_endpoint, json={"text": user_input, "rating": rating})
    
    # Check if the request was successful
    if response.status_code == 200:
        response_json = response.json()
        st.write(f"Predicted sentiment: {response_json['prediction']}")
    else:
        st.write("Error occurred during prediction.")
