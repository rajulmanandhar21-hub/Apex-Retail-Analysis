import pandas as pd
from scipy import stats

# 1. Load the data
df = pd.read_csv('apex_retail_data.csv')

# 2. Separate the groups
control_group = df[df['group'] == 'Control']['converted']
test_group = df[df['group'] == 'Test']['converted']

# 3. Perform the Independent T-Test
t_stat, p_value = stats.ttest_ind(control_group, test_group)

# 4. Show the results
print(f"--- A/B Test Results ---")
print(f"Control Conversion Rate: {control_group.mean():.2%}")
print(f"Test Conversion Rate: {test_group.mean():.2%}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("\n✅ Result: Statistically Significant! The new design is a winner.")
else:
    print("\n❌ Result: Not Significant. The difference could be due to luck.")
