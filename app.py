
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('unemployment_model.pkl', 'rb'))

st.title("Unemployment Rate Predictor")

year = st.number_input("Enter Year (e.g., 2025):", min_value=2025, max_value=2035)

if st.button("Predict"):
    pred = model.predict(np.array([[year]]))
    st.success(f"Predicted Unemployment Rate in {year}: {pred[0]:.2f}%")
