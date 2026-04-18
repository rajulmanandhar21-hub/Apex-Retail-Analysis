import pandas as pd
import statsmodels.api as sm

# 1. Load data
df = pd.read_csv('apex_retail_data.csv')

# 2. We only care about people who actually bought something (amount > 0)
buyers = df[df['purchase_amount'] > 0]

# 3. Define X (Speed) and Y (Amount)
X = buyers['load_speed']
Y = buyers['purchase_amount']

# 4. Add a 'constant' (The Intercept) - Statsmodels needs this for the math to work
X = sm.add_constant(X)

# 5. Build the Model (OLS = Ordinary Least Squares)
model = sm.OLS(Y, X).fit()

# 6. Show the results
print(model.summary())
