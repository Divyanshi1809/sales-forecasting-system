from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np
import pandas as pd
from datetime import datetime

app = FastAPI(title="Sales Forecasting API")

# Enable frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
model = pickle.load(open("best_model.pkl", "rb"))

@app.get("/")
def home():
    return {
        "message": "Sales Forecasting API Running Successfully"
    }

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

    features = np.array([[
        lag_1,
        lag_7,
        lag_30,
        rolling_mean_7,
        rolling_std_7,
        day_of_week,
        month
    ]])
    prediction = model.predict(features)

    next_8_weeks = []

    for i in range(56):
        next_8_weeks.append(round(float(prediction[0]), 2))

    return {
        "generated_at": str(datetime.now()),
        "forecast_next_8_weeks": next_8_weeks
    }