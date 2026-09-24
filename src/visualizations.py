
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Load dataset
df = pd.read_csv("data/corporate_data_.csv")

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Create output directory
output_dir = Path("reports/charts")
output_dir.mkdir(parents=True, exist_ok=True)


# 1. Revenue by Region
region_revenue = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output_dir / "revenue_by_region.png")
plt.close()


# 2. Profit by Category
category_profit = (
    df.groupby("category")["profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_dir / "profit_by_category.png")
plt.close()


# 3. Revenue by Sales Channel
channel_revenue = (
    df.groupby("sales_channel")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(7, 5))
channel_revenue.plot(kind="bar")
plt.title("Revenue by Sales Channel")
plt.xlabel("Sales Channel")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output_dir / "revenue_by_channel.png")
plt.close()


# 4. Monthly Revenue Trend
monthly_revenue = (
    df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
    .sum()
)

monthly_revenue.index = monthly_revenue.index.astype(str)

plt.figure(figsize=(12, 5))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(output_dir / "monthly_revenue_trend.png")
plt.close()


print("All visualizations generated successfully!")
print(f"Charts saved in: {output_dir}")