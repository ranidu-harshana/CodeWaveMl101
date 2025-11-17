import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

st.title("Sales Prediction App")
st.write("Predict sales using advertising budgets (trained ML model).")

# Input fields
tv = st.number_input("TV Budget (1000$)", min_value=0.0, value=100.0)
radio = st.number_input("Radio Budget (1000$)", min_value=0.0, value=20.0)
newspaper = st.number_input("Newspaper Budget (1000$)", min_value=0.0, value=30.0)

if st.button("Predict Sales"):
    X = np.array([[tv, radio, newspaper]])
    prediction = model.predict(X)[0]

    st.success(f"Predicted Sales: **{prediction:.2f} Million $**")
