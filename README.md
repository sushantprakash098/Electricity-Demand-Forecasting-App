# ⚡ Electricity Demand Forecasting App

A web app that predicts short-term electricity demand (load in MW) using historical load patterns and time-based features. Built with [Streamlit](https://streamlit.io/) for an interactive, no-code interface.

## Overview

Electricity demand varies by time of day, day of week, and season, and is strongly correlated with recent load history. This app uses a trained machine learning model to forecast the next hour's electricity demand based on:

- **Time features:** hour of day, day of week, month, weekend indicator
- **Lag features:** load 1 hour ago, 24 hours ago, and 168 hours (1 week) ago
- **Rolling feature:** 24-hour rolling mean load

Users enter these values through simple sliders and input fields and get an instant demand prediction.

## Features

- Interactive UI built with Streamlit — no setup beyond running one command
- Instant predictions using a pre-trained model (`model.pkl`)
- Automatic weekend detection from the selected day of week
- Lightweight and easy to deploy (e.g. Streamlit Community Cloud)

## Tech Stack

- **Python**
- **Streamlit** — web app interface
- **NumPy** — input array handling
- **joblib** — model loading
- **Jupyter Notebook** (`Electricity_Demand_Prediction.ipynb`) — model training and experimentation

## Project Structure

```
├── app.py                              # Streamlit app
├── Electricity_Demand_Prediction.ipynb # Model training notebook
├── model.pkl                           # Trained model
├── requirements.txt                    # Python dependencies
└── .devcontainer/                      # Dev container config
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sushantprakash098/Electricity-Demand-Forecasting-App.git
cd Electricity-Demand-Forecasting-App
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Usage

1. Set the hour of day, day of week, and month using the sliders.
2. Enter the load values for the previous hour, 24 hours ago, and 168 hours ago (in MW).
3. Enter the 24-hour rolling mean load.
4. Click **Predict Electricity Demand** to see the forecasted load.

## Model

The prediction model was trained in `Electricity_Demand_Prediction.ipynb` using historical electricity load data, time-based features, and lagged load values, then exported as `model.pkl` for use in the app.

## Future Improvements

- Add data visualization of historical vs. predicted load trends
- Support batch predictions via file upload
- Deploy a live demo link
- Add model performance metrics (e.g., MAE, RMSE) to the README

## Author

**Sushant Prakash**
