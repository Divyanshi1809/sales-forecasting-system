from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pickle
import numpy as np
from datetime import datetime
import os

app = FastAPI(title="Sales Forecasting API")

# CORS (optional but safe)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend (THIS IS THE MAIN FIX)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Load model safely
model = pickle.load(open("best_model.pkl", "rb"))

@app.get("/predict")
def predict(
    lag_1: float,
    lag_7: float,
    lag_30: float,
    rolling_mean_7: float,
    rolling_std_7: float,
    day_of_week: int,
    month: int
):
    features = np.array([[lag_1, lag_7, lag_30, rolling_mean_7, rolling_std_7, day_of_week, month]])
    prediction = model.predict(features)

    forecast = [round(float(prediction[0]), 2) for _ in range(56)]

    return {
        "generated_at": str(datetime.now()),
        "forecast_next_8_weeks": forecast
    }