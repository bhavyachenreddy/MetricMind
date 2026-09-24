import pandas as pd


def load_data():
    """Load the corporate sales dataset."""
    return pd.read_csv("data/corporate_data_.csv")


def get_total_revenue(df):
    """Calculate total revenue."""
    return df["revenue"].sum()


def get_total_profit(df):
    """Calculate total profit."""
    return df["profit"].sum()


def get_total_quantity(df):
    """Calculate total quantity sold."""
    return df["quantity"].sum()


def get_region_performance(df):
    """Calculate revenue and profit by region."""
    return df.groupby("region")[["revenue", "profit"]].sum()


def get_category_performance(df):
    """Calculate revenue and profit by category."""
    return df.groupby("category")[["revenue", "profit"]].sum()


def get_channel_performance(df):
    """Calculate revenue and profit by sales channel."""
    return df.groupby("sales_channel")[["revenue", "profit"]].sum()


def get_profit_margin(df):
    """Calculate overall profit margin percentage."""
    total_revenue = df["revenue"].sum()
    total_profit = df["profit"].sum()

    if total_revenue == 0:
        return 0

    return (total_profit / total_revenue) * 100


def get_average_order_revenue(df):
    """Calculate average revenue per order."""
    return df["revenue"].mean()


def get_monthly_performance(df):
    """Calculate monthly revenue and profit."""
    df["order_date"] = pd.to_datetime(df["order_date"])

    monthly_metrics = (
        df.groupby(df["order_date"].dt.to_period("M"))[
            ["revenue", "profit"]
        ]
        .sum()
        .reset_index()
    )

    monthly_metrics["order_date"] = (
        monthly_metrics["order_date"].astype(str)
    )

    return monthly_metrics


def get_top_products(df, n=10):
    """Return top products by revenue."""
    product_metrics = (
        df.groupby("product_name")[["revenue", "profit"]]
        .sum()
        .sort_values("revenue", ascending=False)
        .head(n)
    )

    return product_metrics