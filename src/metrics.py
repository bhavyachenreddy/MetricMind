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