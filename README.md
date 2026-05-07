📊 Sales Forecasting System (End-to-End ML Project)
📌 Project Overview

The Sales Forecasting System is a machine learning-based web application that predicts future sales using historical patterns and engineered time-series features. The system uses a trained regression model exposed through a FastAPI backend and a simple interactive frontend dashboard built with HTML, CSS, and JavaScript.

This project demonstrates a complete end-to-end ML pipeline including data preprocessing, feature engineering, model training, API deployment, and frontend integration.

🎯 Objective

To build a predictive system that can forecast future sales based on historical lag features and statistical rolling metrics, enabling better business decision-making and demand planning.

🏗️ System Architecture
Frontend (HTML/CSS/JS)
        ↓
FastAPI Backend (app.py)
        ↓
ML Model (best_model.pkl)
        ↓
Prediction Output (Next 8 Weeks Forecast)
🧠 Machine Learning Approach

The model uses engineered time-series features:

📌 Input Features:
Lag 1 (previous day sales)
Lag 7 (weekly lag)
Lag 30 (monthly lag)
Rolling Mean (7-day average)
Rolling Standard Deviation (7-day volatility)
Day of Week
Month

📌 Output:
Forecast of next 8 weeks sales


📌 Model Used:
Trained regression-based machine learning model (e.g., XGBoost / Random Forest / similar ensemble model)


💻 Tech Stack
Backend:
FastAPI
Python
NumPy
Pandas
Scikit-learn / XGBoost
Frontend:
HTML5
CSS3
JavaScript (Fetch API)
Deployment:
Uvicorn (ASGI Server)


🚀 Features
📈 Real-time sales prediction API
🌐 Interactive web dashboard
🔁 RESTful FastAPI architecture
📊 Time-series feature engineering
⚡ Fast prediction response
🔗 Frontend-backend integration using Fetch API


📂 Project Structure
forecasting-project/
│
├── app.py                  # FastAPI backend
├── best_model.pkl          # Trained ML model
├── requirements.txt        # Dependencies
├── index.html              # Frontend UI
└── README.md               # Project documentation


📊 Results
The system successfully generates future sales forecasts based on historical patterns.
Provides quick and interactive predictions via web interface.
Backend API ensures scalable deployment for real-world usage.



🔮 Future Improvements
Integration of LSTM/Deep Learning models for better sequence forecasting
Dynamic multi-step prediction instead of constant outputs
Visualization dashboard using Chart.js or Plotly
Cloud deployment (AWS / Render / Azure)
