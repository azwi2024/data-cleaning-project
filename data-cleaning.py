import pandas as pd

# Load the data
file_path = 'Order_Data_meriskill.csv'  # Ensure the CSV file is in the same folder
data = pd.read_csv(file_path)

# Step 1: Remove duplicate rows
data_cleaned = data.drop_duplicates()

# Step 2: Handle missing values
# Replace missing values in 'Fraud' and 'Gender' with 'Unknown'
data_cleaned['Fraud'].fillna('Unknown', inplace=True)
data_cleaned['Gender'].fillna('Unknown', inplace=True)

# Drop rows with missing critical fields
data_cleaned = data_cleaned.dropna(subset=['Customer_Name', 'AcquisitionSource'])

# Step 3: Standardize data formats
# Strip whitespace and newline characters from 'AcquisitionSource'
data_cleaned['AcquisitionSource'] = data_cleaned['AcquisitionSource'].str.strip()

# Convert 'OrderDate' to datetime format
data_cleaned['OrderDate'] = pd.to_datetime(data_cleaned['OrderDate'], errors='coerce')

# Convert 'ProductPrice' to numeric (float), handling non-numeric values
data_cleaned['ProductPrice'] = pd.to_numeric(data_cleaned['ProductPrice'], errors='coerce')

# Optional: Check for remaining missing values
missing_values = data_cleaned.isnull().sum()

# Step 4: Save cleaned data
data_cleaned.to_csv('Cleaned_Order_Data.csv', index=False)

# Print a summary of the cleaned data
print("Data Cleaning Completed!")
print("Remaining Missing Values:\n", missing_values)
print("Cleaned data saved as 'Cleaned_Order_Data.csv'")
