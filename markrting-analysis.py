import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the cleaned dataset
file_path = 'Cleaned_Order_Data.csv'  # Ensure this file exists in your directory
data = pd.read_csv(file_path)

# Task 1: Profitability Calculation
# Calculate total profit and profit per user for each campaign
data['total_profit'] = data['revenue'] - data['cost']
data['profit_per_user'] = data['total_profit'] / data['num_users']

# Profitability metrics for all campaigns
profitability_data = data[['campaign_id', 'total_profit', 'profit_per_user']]

# Display profitability data
print("\nProfitability Data:")
print(profitability_data)

# Task 2: Campaign Comparison
# Identify the most profitable campaign
best_campaign = profitability_data.loc[profitability_data['profit_per_user'].idxmax()]
print("\nMost Profitable Campaign:")
print(best_campaign)

# Task 3: Conversion Rate and CAC Analysis
# Segment data by acquisition source for conversion rate and CAC analysis
# Assuming 'acquisition_source' column exists
conversion_data = data.groupby('acquisition_source').agg(
    total_conversions=('num_users', 'sum'),
    total_cost=('cost', 'sum')
)

# Calculate Conversion Rate and CAC
conversion_data['conversion_rate'] = conversion_data['total_conversions'] / data['num_users'].sum()
conversion_data['CAC'] = conversion_data['total_cost'] / conversion_data['total_conversions']

# Display Conversion Rate and CAC
print("\nConversion Rate and CAC for Each Acquisition Source:")
print(conversion_data)

# Task 4: Prediction and Visualization
# Predict customer acquisition based on the budget
# Assuming you have 'budget' column in your dataset to predict customer acquisition

# Step 1: Budget and CAC Analysis
budget_data = data[['budget', 'CAC']]  # Assuming 'budget' column exists

# Step 2: Use Linear Regression to predict customer acquisition
X = budget_data[['budget']]  # Independent variable (budget)
y = budget_data['CAC']  # Dependent variable (Customer Acquisition Cost)

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict customer acquisition
predicted_acquisition = model.predict(X)

# Step 3: Visualize Predictions
plt.figure(figsize=(10, 6))
plt.scatter(budget_data['budget'], predicted_acquisition, color='blue', label='Predicted Acquisition')
plt.plot(budget_data['budget'], predicted_acquisition, color='red', label='Fitted Line')
plt.title('Predicted Customer Acquisition vs Budget')
plt.xlabel('Budget')
plt.ylabel('Predicted Customer Acquisition')
plt.legend()
plt.show()

# Save the output to CSV
profitability_data.to_csv('Profitability_Calculations.csv', index=False)
conversion_data.to_csv('Conversion_CAC_Analysis.csv', index=False)
print("\nProfitability and Conversion/CAC Analysis saved as CSV files.")
