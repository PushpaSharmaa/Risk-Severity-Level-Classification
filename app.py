import streamlit as st
import joblib

# Load the model and vectorizer
with open('models/best_model.pkl', 'rb') as f:
    model = joblib.load(f)

with open('models/tfidf.pkl', 'rb') as f:
    tfidf = joblib.load(f)

# Streamlit UI
st.title("Severity Level Prediction")
st.write("Enter a severity summary below:")

user_input = st.text_area("Severity Summary")

if st.button("Predict"):
    input_vector = tfidf.transform([user_input])
    prediction = model.predict(input_vector)[0]
    st.success(f"Predicted Severity Level: **{prediction}**")
