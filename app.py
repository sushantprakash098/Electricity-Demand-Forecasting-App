import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("rf_model.pkl")

st.set_page_config(page_title="Electricity Load Predictor")

st.title("⚡ Electricity Demand Forecasting App")

st.markdown("Predict hourly electricity load using Machine Learning.")

# Inputs
hour = st.slider("Hour of Day", 0, 23, 12)
dayofweek = st.slider("Day of Week (0=Monday)", 0, 6, 0)
month = st.slider("Month", 1, 12, 1)

is_weekend = 1 if dayofweek >= 5 else 0

lag_1 = st.number_input("Previous Hour Load (MW)", value=20000.0)
lag_24 = st.number_input("Load 24 Hours Ago (MW)", value=20000.0)
lag_168 = st.number_input("Load 168 Hours Ago (MW)", value=20000.0)
rolling_mean_24 = st.number_input("24 Hour Rolling Mean (MW)", value=20000.0)

if st.button("Predict Load"):
    
    input_data = np.array([[hour, dayofweek, month, is_weekend,
                            lag_1, lag_24, lag_168, rolling_mean_24]])
    
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Load: {prediction[0]:,.2f} MW")
