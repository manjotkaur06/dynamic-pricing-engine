import os
import pandas as pd
import random

def generate_advanced_data(num_rows=2000):
    print("⏳ Generating advanced synthetic pricing data...")
    data = []
    
    for _ in range(num_rows):
        demand = random.randint(10, 100)
        supply = random.randint(5, 50)
        base_price = round(random.uniform(50.0, 200.0), 2)
        
        # New Features!
        is_peak_hour = random.choice([0, 1])  # 1 = Office timing/Night, 0 = Normal
        is_raining = random.choice([0, 1])    # 1 = Raining, 0 = Clear
        
        # Advanced Multiplier Logic
        multiplier = 1.0 + (demand / (supply + 1)) * 0.1
        if is_peak_hour: multiplier += 0.3
        if is_raining: multiplier += 0.4
        
        # Extreme Surge Cap
        multiplier = min(max(multiplier, 0.8), 3.5) 
        final_price = round(base_price * multiplier, 2)
        
        data.append([demand, supply, base_price, is_peak_hour, is_raining, final_price])
        
    df = pd.DataFrame(data, columns=['demand', 'supply', 'base_price', 'is_peak_hour', 'is_raining', 'final_price'])
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/pricing_dataset.csv', index=False)
    print("✅ Advanced Data saved to 'data/pricing_dataset.csv'")

if __name__ == "__main__":
    generate_advanced_data()