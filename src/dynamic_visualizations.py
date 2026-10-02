import os
import pandas as pd
import matplotlib.pyplot as plt


DATA_PATH = "data/corporate_data_.csv"
OUTPUT_DIR = "reports/charts"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_revenue_by_region_chart():
    """Create a bar chart showing revenue by region."""

    df = pd.read_csv(DATA_PATH)

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

    plt.tight_layout()

    output_path = os.path.join(
        OUTPUT_DIR,
        "dynamic_revenue_by_region.png"
    )

    plt.savefig(output_path)
    plt.close()

    return output_path


def create_revenue_trend_chart():
    """Create a line chart showing revenue over time."""

    df = pd.read_csv(DATA_PATH)

    df["order_date"] = pd.to_datetime(df["order_date"])

    monthly_revenue = (
        df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
        .sum()
    )

    monthly_revenue.index = monthly_revenue.index.astype(str)

    plt.figure(figsize=(10, 5))

    plt.plot(
        monthly_revenue.index,
        monthly_revenue.values,
        marker="o"
    )

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    plt.tight_layout()

    output_path = os.path.join(
        OUTPUT_DIR,
        "dynamic_monthly_revenue.png"
    )

    plt.savefig(output_path)
    plt.close()

    return output_path


def generate_visualization(chart_type: str):
    """
    Generate a chart based on the requested visualization type.
    """

    if chart_type == "region":
        return create_revenue_by_region_chart()

    if chart_type == "time":
        return create_revenue_trend_chart()

    raise ValueError(
        "Unsupported chart type. Use 'region' or 'time'."
    )


if __name__ == "__main__":

    print("MetricMind - Dynamic Visualizations")
    print("-----------------------------------")

    region_chart = generate_visualization("region")

    print(f"Region chart created: {region_chart}")

    time_chart = generate_visualization("time")

    print(f"Time-series chart created: {time_chart}")