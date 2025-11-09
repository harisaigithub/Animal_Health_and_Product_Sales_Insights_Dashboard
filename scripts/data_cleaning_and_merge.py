# ============================================
# Animal Health and Product Sales Insights Dashboard
# Data Generation, Cleaning, and Merging Script (Positive Profit Version)
# ============================================

import pandas as pd
import numpy as np
import random
import os
from faker import Faker

# -------------------------------
# 1. Setup & Folder Preparation
# -------------------------------
fake = Faker()
random.seed(42)
np.random.seed(42)

base_dir = os.path.dirname(os.path.abspath(__file__))
raw_dir = os.path.join(base_dir, "../raw_data")
clean_dir = os.path.join(base_dir, "../cleaned_data")

os.makedirs(raw_dir, exist_ok=True)
os.makedirs(clean_dir, exist_ok=True)

# -------------------------------
# 2. Define Reference Data
# -------------------------------
regions = ["North", "South", "East", "West", "Central"]
diseases = ["Parvovirus", "Rabies", "Tick Fever", "Ringworm", "Distemper", "Leptospirosis"]
products = ["VetCare Plus", "PetGuard", "HealthyPaws", "FurWell", "MediPet", "PawShield", "FurryVax", "CanineCare"]
categories = ["Medicine", "Vaccine", "Supplement", "Antibiotic"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
years = [2023, 2024]

# -------------------------------
# 3. Generate Raw Datasets
# -------------------------------

# Health dataset (disease trends)
health_data = pd.DataFrame({
    "Region": np.random.choice(regions, 1200),
    "Disease": np.random.choice(diseases, 1200),
    "Cases": np.random.randint(5, 120, 1200),
    "Month": np.random.choice(months, 1200),
    "Year": np.random.choice(years, 1200)
})
health_path = os.path.join(raw_dir, "health_data_raw.csv")
health_data.to_csv(health_path, index=False)

# Product information dataset (cost per unit)
product_info = pd.DataFrame({
    "Product": products,
    "Category": np.random.choice(categories, len(products)),
    "Cost_Per_Unit": np.random.randint(100, 500, len(products))
})
product_path = os.path.join(raw_dir, "product_info_raw.csv")
product_info.to_csv(product_path, index=False)

# Sales dataset (product sales performance)
sales_rows = []
for _ in range(1200):
    region = random.choice(regions)
    product = random.choice(products)
    units_sold = random.randint(50, 1000)
    year = random.choice(years)
    month = random.choice(months)
    category = random.choice(categories)
    # Get cost for this product
    cost_per_unit = product_info.loc[product_info["Product"] == product, "Cost_Per_Unit"].values[0]
    # Add random markup 10%–50%
    markup = random.uniform(1.1, 1.5)
    revenue = units_sold * cost_per_unit * markup
    sales_rows.append([region, product, units_sold, revenue, month, year, category])

sales_data = pd.DataFrame(sales_rows, columns=["Region", "Product", "Units_Sold", "Revenue", "Month", "Year", "Category"])
sales_path = os.path.join(raw_dir, "sales_data_raw.csv")
sales_data.to_csv(sales_path, index=False)

print("✅ Raw CSVs created successfully in /raw_data folder.")

# -------------------------------
# 4. Data Cleaning
# -------------------------------
health = pd.read_csv(health_path)
sales = pd.read_csv(sales_path)
product_info = pd.read_csv(product_path)

# Remove duplicates
health.drop_duplicates(inplace=True)
sales.drop_duplicates(inplace=True)

# Handle missing values (if any)
health.fillna({"Cases": health["Cases"].median()}, inplace=True)
sales.fillna({"Revenue": sales["Revenue"].median(), "Units_Sold": sales["Units_Sold"].median()}, inplace=True)

# Convert data types
health["Cases"] = health["Cases"].astype(int)
sales["Revenue"] = sales["Revenue"].astype(float)
sales["Units_Sold"] = sales["Units_Sold"].astype(int)

# -------------------------------
# 5. Merge and Feature Engineering
# -------------------------------
sales_merged = pd.merge(sales, product_info, on="Product", how="left")
merged = pd.merge(sales_merged, health, on=["Region", "Month", "Year"], how="left", suffixes=("_sales", "_health"))

# Derived Metrics
merged["Profit"] = merged["Revenue"] - (merged["Units_Sold"] * merged["Cost_Per_Unit"])
merged["Profit_Margin"] = np.where(merged["Revenue"] > 0, (merged["Profit"] / merged["Revenue"]) * 100, 0)
merged["Revenue_per_Case"] = np.where(merged["Cases"] > 0, merged["Revenue"] / merged["Cases"], merged["Revenue"])

# Small anomaly injection for realism
for _ in range(10):
    merged.loc[random.randint(0, len(merged)-1), "Revenue"] = np.nan
    merged.loc[random.randint(0, len(merged)-1), "Cases"] = np.nan

# Handle anomalies
merged["Revenue"].fillna(merged["Revenue"].median(), inplace=True)
merged["Cases"].fillna(merged["Cases"].median(), inplace=True)

# Round for neatness
merged["Profit_Margin"] = merged["Profit_Margin"].round(2)
merged["Revenue_per_Case"] = merged["Revenue_per_Case"].round(2)

# -------------------------------
# 6. Save Cleaned Outputs
# -------------------------------
health.to_csv(os.path.join(clean_dir, "health_data_cleaned.csv"), index=False)
sales_merged.to_csv(os.path.join(clean_dir, "sales_data_cleaned.csv"), index=False)
merged.to_csv(os.path.join(clean_dir, "merged_data.csv"), index=False)

# Summary
print("✅ Data cleaned, merged, and saved in /cleaned_data folder.")
print(f"Health records: {len(health)}, Sales records: {len(sales)}, Final merged: {len(merged)}")
print(f"Average Profit Margin: {merged['Profit_Margin'].mean():.2f}%")
