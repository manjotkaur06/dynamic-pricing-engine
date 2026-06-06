# 🚗 Real-Time Production Dynamic Pricing Engine

An end-to-end Machine Learning system that models and predicts ride-hailing/product surge prices using an industry-standard **XGBoost Regressor**. Features a production pipeline, analytical evaluations, and an interactive web interface.

🌐 **Live Demo:** [INSERT_YOUR_STREAMLIT_URL_HERE]

## 📈 Model Performance & Metrics
- **Data Size:** 20,000 trips with real-world noise, geospatial vectors, and seasonal cycles.
- **R-Squared Accuracy:** **99.20%**
- **Mean Absolute Error (MAE):** **₹14.08**
- **Root Mean Squared Error (RMSE):** ₹19.36

## 🛠️ Tech Stack & Architecture
- **Language:** Python 3.14
- **Core ML:** XGBoost, Scikit-Learn, Pandas, NumPy, Joblib
- **API Framework:** FastAPI, Uvicorn, Pydantic
- **Dashboard UI:** Streamlit

## 📂 Project Structure
```text
├── data/                  # Ingested real-world structured datasets
├── models/                # Trained serialised weights (.pkl)
├── src/
│   ├── download_data.py   # Automated data ingestion logic & pipelines
│   ├── train.py           # Feature Engineering & Model training pipeline
│   ├── app.py             # FastAPI backend with business validation fallback
│   └── dashboard.py       # Streamlit Live Control Web Center
├── requirements.txt       # Project dependencies
└── README.md