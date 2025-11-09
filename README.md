# **Animal Health and Product Sales Insights Dashboard**

---

## **Tagline**
*Bridging animal healthcare and business intelligence through data-driven insights.*

---

## **LIVE AT**
- **[View Power BI Dashboard](https://app.powerbi.com/links/DXWbVb_Ktt?ctid=f6981b0a-3915-4628-be7e-368196415f8f&pbi_source=linkShare)** (Requires Microsoft login)

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Objectives](#objectives)
4. [Dataset](#dataset)
5. [Data Preprocessing](#data-preprocessing)
6. [Data Model](#data-model)
7. [Dashboard Overview](#dashboard-overview)
8. [Key Insights](#key-insights)
9. [Technologies Used](#technologies-used)
10. [Implementation Details](#implementation-details)
11. [Results](#results)
12. [Hosting](#hosting)
13. [Future Enhancements](#future-enhancements)
14. [Contributing](#contributing)
15. [License](#license)
16. [Contact](#contact)

---

## **Introduction**
The **Animal Health and Product Sales Insights Dashboard** is a Business Intelligence project built to analyze veterinary disease trends and product sales performance across regions.  
It simulates a real-world BI case for **Elanco**, combining animal health analytics with sales data to drive strategic decisions in product planning, inventory management, and market forecasting.

The project integrates **Python** (for data preparation) and **Power BI** (for visualization and analytics), showcasing how modern BI workflows transform raw data into actionable insights.

---

## **Problem Statement**
Animal healthcare companies often struggle to:
- Understand how disease outbreaks influence product sales.
- Identify profitable regions and underperforming products.
- Predict future sales based on seasonal disease patterns.

This dashboard provides a unified analytical solution linking **veterinary health data** with **sales performance**, helping stakeholders make informed business decisions.

---

## **Objectives**
- Build a unified BI dashboard integrating **health and sales data**.
- Visualize **regional performance, disease frequency, and profit metrics**.
- Identify **high-profit products and demand patterns** by region.
- Enable **forecasting** and **interactive filtering** for decision-making.
- Demonstrate **end-to-end analytics workflow** using Python and Power BI.

---

## **Dataset**
### **Sources**
Synthetic datasets generated using **Faker**, **NumPy**, and **Pandas**.

| Dataset | Columns | Rows | Description |
|----------|----------|------|-------------|
| `health_data_raw.csv` | Region, Disease, Cases, Month, Year | 1200 | Veterinary disease records |
| `sales_data_raw.csv` | Region, Product, Units_Sold, Revenue, Month, Year, Category | 1200 | Sales and revenue data |
| `product_info_raw.csv` | Product, Category, Cost_Per_Unit | 8 | Product details |

---

## **Data Preprocessing**
Data cleaning and transformation performed in **Python** (`data_cleaning_and_merge.py`).

### **Steps:**
1. Removed duplicates and nulls.  
2. Imputed missing values using median strategy.  
3. Calculated derived metrics:
   ```python
   Profit = Revenue - (Units_Sold * Cost_Per_Unit)
   Profit_Margin = (Profit / Revenue) * 100
   Revenue_per_Case = Revenue / Cases
````

4. Standardized numeric columns and exported cleaned data to `/cleaned_data/`.

Command to run:

```bash
python scripts/data_cleaning_and_merge.py
```

---

## **Data Model**

Power BI schema follows a **Star Model** design:

```
product_info  ←→  sales_data  ←→  health_data
       ↑                   |
      (Cost_Per_Unit)      ↓
           merged_data (fact table)
```

Relationships:

* **Product** links sales and product info.
* **Region, Month, Year** link sales and health data.
* Optional **Calendar table** added for time intelligence.

---

## **Dashboard Overview**


### **KPIs Displayed**

| KPI                 | Description                              |
| ------------------- | ---------------------------------------- |
| **Total Revenue**   | ₹ 4.11 B — Total generated sales revenue |
| **Total Profit**    | ₹ 943 M — Overall profit after cost      |
| **Profit Margin %** | 22.9 % — Average profit margin           |
| **Units Sold**      | 9 M units across all categories          |
| **Total Cases**     | 1 M veterinary disease cases             |

### **Visual Components**

| Section                      | Visual Type   | Purpose                                     |
| ---------------------------- | ------------- | ------------------------------------------- |
| Revenue by Region & Category | Bar Chart     | Compare product revenue across regions      |
| Revenue by Category          | Donut Chart   | Show revenue contribution per product type  |
| Profit by Region & Product   | Treemap       | Highlight top profitable regions & products |
| Disease Frequency            | Clustered Bar | Analyze disease trends region-wise          |
| Revenue Trend (2023–2024)    | Line Chart    | Forecast sales performance over time        |
| Key Insights                 | Text Card     | Summarize actionable findings               |

### **Filters / Slicers**

* Region
* Product Category
* Year / Month

---

## **Key Insights**

* **South and East regions** contribute **45 %+** of total revenue, driven by vaccine sales.
* **PetGuard** and **HealthyPaws** products achieve **highest margins (27–30 %)**.
* **Parvovirus** and **Tick Fever** correlate directly with **medicine and vaccine sales**.
* **Revenue forecast** shows **10 % quarterly growth** led by preventive product demand.
* The **Central region** shows potential for operational cost optimization.

---

## **Technologies Used**

| Category              | Tools                                     |
| --------------------- | ----------------------------------------- |
| **Programming / ETL** | Python, Pandas, NumPy, Faker              |
| **Visualization**     | Power BI, Power Query, DAX                |
| **Storage**           | CSV, Excel                                |
| **Modeling**          | Star Schema, Calculated Columns, Measures |
| **Deployment**        | Power BI Service (Publish to Web)         |

---

## **Implementation Details**

### **Python Stage**

* Created 3 datasets (`health`, `sales`, `product_info`).
* Generated 1200+ synthetic records.
* Ensured realistic positive profit margins.
* Saved outputs into `/cleaned_data/`.

### **Power BI Stage**

* Imported cleaned data and built relationships.
* Created DAX measures for KPIs.
* Designed visuals using consistent healthcare theme.
* Added slicers for interactivity.
* Published dashboard to Power BI Service.

---

## **Results**

| Metric                    | Value        | Description                       |
| ------------------------- | ------------ | --------------------------------- |
| **Average Profit Margin** | 22.9 %       | Balanced, realistic profitability |
| **Build Time**            | ~3 hours     | End-to-end completion             |
| **Regional Leaders**      | South & East | Highest revenue contribution      |
| **Forecast Growth**       | +10 %        | Predicted next-quarter increase   |
| **Data Records**          | ~2400 merged | Across health + sales             |

---

## **Hosting**

* Published to **Power BI Service → My Workspace → Publish to Web**
* Shareable live link (replace below once available):
  🔗 [**View Dashboard**](https://app.powerbi.com/view?r=)

Offline reports stored in:

```
/reports/dashboard_screenshots/AnimalHealth_SalesInsights_Report.pdf
```

---

## **Future Enhancements**

* Connect to **live veterinary datasets** (Kaggle / OIE).
* Integrate **Python Prophet/ARIMA** for advanced forecasting.
* Add **geospatial maps** for regional disease hotspots.
* Automate data refresh using **Power Automate**.
* Extend to **drill-through pages** for product-level analysis.

---

## **Contributing**

Contributions are welcome!

**Steps to contribute:**

```bash
# Fork the repository
git clone https://github.com/yourusername/Animal-Health-Sales-Insights-Dashboard.git

# Create a new branch
git checkout -b feature-branch

# Make your updates
git commit -m "Added new visualization or feature"

# Push and open a Pull Request
git push origin feature-branch
```

Ensure code is clean, modular, and documented.

---

## **License**

```
MIT License

Copyright (c) 2025 Parasa Hari Sai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

---

## **Contact**

**Author:** Parasa Hari Sai
📧 Email: [harisaiparasa@gmail.com](mailto:harisaiparasa@gmail.com)
🔗 LinkedIn: [linkedin.com/in/parasa-hari-sai](https://www.linkedin.com/in/parasa-hari-sai)
💻 GitHub: [github.com/harisaigithub](https://github.com/harisaigithub)

---