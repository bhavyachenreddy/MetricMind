
import pandas as pd

# Load dataset
df = pd.read_csv("data/corporate_data_.csv")

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Overall business metrics
total_revenue = df["revenue"].sum()
total_cost = df["cost"].sum()
total_profit = df["profit"].sum()
total_quantity = df["quantity"].sum()

profit_margin = (total_profit / total_revenue) * 100

print("===== OVERALL BUSINESS METRICS =====")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Cost: ₹{total_cost:,.2f}")
print(f"Total Profit: ₹{total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Overall Profit Margin: {profit_margin:.2f}%")

# Revenue and profit by region
region_metrics = df.groupby("region")[["revenue", "profit"]].sum()
region_metrics = region_metrics.sort_values("revenue", ascending=False)

print("\n===== REGION-WISE PERFORMANCE =====")
print(region_metrics)

# Revenue and profit by category
category_metrics = df.groupby("category")[["revenue", "profit"]].sum()
category_metrics = category_metrics.sort_values("revenue", ascending=False)

print("\n===== CATEGORY-WISE PERFORMANCE =====")
print(category_metrics)

# Revenue by sales channel
channel_metrics = df.groupby("sales_channel")[["revenue", "profit"]].sum()
channel_metrics = channel_metrics.sort_values("revenue", ascending=False)

print("\n===== SALES CHANNEL PERFORMANCE =====")
print(channel_metrics)


# Save region-wise metrics
region_metrics.to_csv("data/region_metrics.csv")

# Save category-wise metrics
category_metrics.to_csv("data/category_metrics.csv")

# Save sales channel metrics
channel_metrics.to_csv("data/channel_metrics.csv")

print("\nMetrics saved successfully!")