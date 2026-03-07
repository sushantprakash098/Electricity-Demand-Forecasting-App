import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("model.pkl")

# App title
st.title("⚡ Electricity Demand Forecasting App")

st.write("Enter the required values to predict electricity demand.")

# Input sliders
hour = st.slider("Hour of Day", 0, 23, 12)
dayofweek = st.slider("Day of Week (0 = Monday, 6 = Sunday)", 0, 6, 0)
month = st.slider("Month", 1, 12, 1)

# Weekend calculation
is_weekend = 1 if dayofweek >= 5 else 0

# Historical load inputs
lag_1 = st.number_input("Load in Previous Hour (MW)", value=20000.0)
lag_24 = st.number_input("Load 24 Hours Ago (MW)", value=20000.0)
lag_168 = st.number_input("Load 168 Hours Ago (MW)", value=20000.0)
rolling_mean_24 = st.number_input("24 Hour Rolling Mean Load (MW)", value=20000.0)

# Prediction button
if st.button("Predict Electricity Demand"):

    input_data = np.array([[hour, dayofweek, month, is_weekend,
                            lag_1, lag_24, lag_168, rolling_mean_24]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Electricity Load: {prediction[0]:,.2f} MW")