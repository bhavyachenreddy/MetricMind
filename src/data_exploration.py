import pandas as pd

# Load the dataset
df = pd.read_csv("data/corporate_data_.csv")

# Display dataset information
print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Check date range
print("\nMinimum Order Date:", df["order_date"].min())
print("Maximum Order Date:", df["order_date"].max())

# Check numerical summary
print("\nNumerical Summary:")
print(df[["quantity", "revenue", "cost", "profit"]].describe())