import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor
import joblib
import os

def train_advanced_engine():
    data_path = 'data/real_pricing_data.csv'
    if not os.path.exists(data_path):
        print("❌ Dataset missing! Run download_data.py first.")
        return

    print("📊 Loading messy real-world structured data...")
    df = pd.read_csv(data_path)
    
    # ----- 1. DATA CLEANING & IMPUTATION -----
    # Real data has missing values, handling them with median imputation
    df['demand_level'] = df['demand_level'].fillna(df['demand_level'].median())
    df['traffic_density'] = df['traffic_density'].fillna(df['traffic_density'].median())
    
    # ----- 2. ADVANCED FEATURE ENGINEERING -----
    # Creating business-critical ratios that tree models love
    df['demand_supply_ratio'] = df['demand_level'] / (df['supply_level'] + 1)
    df['cost_per_km_baseline'] = df['trip_distance'] * 12.0
    
    # ----- 3. TRAIN-TEST SPLIT -----
    features = ['trip_distance', 'demand_level', 'supply_level', 'traffic_density', 
                'is_peak_hour', 'is_raining', 'demand_supply_ratio', 'cost_per_km_baseline']
    
    X = df[features]
    y = df['final_price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # ----- 4. XGBOOST MODEL TRAINING -----
    print("🚀 Training Industry-Standard XGBoost Regressor...")
    model = XGBRegressor(
        n_estimators=150,
        max_depth=6,
        learning_rate=0.08,
        subsample=0.8,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # ----- 5. RIGOROUS DATA SCIENCE EVALUATION -----
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    
    print("\n" + "="*30)
    print("📈 DATA SCIENCE MODEL METRICS")
    print("="*30)
    print(f"Mean Absolute Error (MAE): ₹{mae:.2f}")
    print(f"Root Mean Squared Error (RMSE): ₹{rmse:.2f}")
    print(f"R-Squared Score (Accuracy): {r2*100:.2f}%")
    print("="*30 + "\n")
    
    # Save model and columns list for deployment consistency
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/advanced_xgb_pricing_model.pkl')
    print("✅ Production model successfully exported to 'models/advanced_xgb_pricing_model.pkl'")

if __name__ == "__main__":
    train_advanced_engine()