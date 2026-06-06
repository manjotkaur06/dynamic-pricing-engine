from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI(title="Production Dynamic Pricing Engine")

MODEL_PATH = 'models/advanced_xgb_pricing_model.pkl'
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

class ProductionPricingRequest(BaseModel):
    trip_distance: float
    demand_level: int
    supply_level: int
    traffic_density: float
    is_peak_hour: int
    is_raining: int

@app.post("/predict-price")
def predict_price(request: ProductionPricingRequest):
    if not model:
        return {"error": "Production model not found. Train the model first."}
        
    # --- 1. LIVE FEATURE ENGINEERING (Sourcing exactly like training) ---
    demand_supply_ratio = request.demand_level / (request.supply_level + 1)
    cost_per_km_baseline = request.trip_distance * 12.0
    
    # --- 2. BUSINESS COLD START / FALLBACK LOGIC ---
    # Agar supply zero ya negative ho, ya input galat ho, toh safer fallback price calculated
    if request.trip_distance <= 0:
        return {"suggested_dynamic_price": 0.0, "status": "Invalid Distance"}
        
    # --- 3. ML MODEL PREDICTION ---
    features = [[
        request.trip_distance, request.demand_level, request.supply_level, 
        request.traffic_density, request.is_peak_hour, request.is_raining,
        demand_supply_ratio, cost_per_km_baseline
    ]]
    
    predicted_price = model.predict(features)[0]
    
    # Safeguard: Price baseline se kam nahi honi chahiye
    final_price = max(float(predicted_price), 50.0 + cost_per_km_baseline)
    
    return {
        "baseline_fare": round(50.0 + cost_per_km_baseline, 2),
        "suggested_dynamic_price": round(final_price, 2)
    }