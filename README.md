# Apex Retail: A/B Testing & Revenue Optimization Analysis

## 🎯 Project Objective
This project analyzes a 2,000-user trial of a new checkout page design. The goal was to determine if the new design improves conversion rates and to identify the impact of page load latency on total revenue.

## 🛠️ Tech Stack
- **Python:** SciPy (Hypothesis Testing), Statsmodels (OLS Regression), Pandas (Data Manipulation).
- **Excel:** Pivot Tables, Regression Visualization, Interactive Dashboards.

## 📊 Key Findings
1. **Conversion Success:** The Test group showed an **18.5% conversion rate** compared to **11.4%** in the Control group (p < 0.001).
2. **The "Price of Lag":** Regression analysis reveals that every **1 second of load delay costs $10.48** in average purchase value. 
3. **Model Accuracy:** The regression model achieved an **R-squared of 0.85**, indicating that site speed is a primary driver of spending behavior.

## 💡 Recommendation
Roll out the new design immediately, but prioritize back-end server optimization to reduce load times below 2.0 seconds to maximize average order value.

<img width="612" height="374" alt="image" src="https://github.com/user-attachments/assets/66951d39-66be-4e32-aa20-7a515293b3f4" />
<img width="608" height="355" alt="image" src="https://github.com/user-attachments/assets/c562c5cb-b2c6-4849-92f4-f73a06b71916" />

