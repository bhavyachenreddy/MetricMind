
import pandas as pd
import streamlit as st


# Page configuration
st.set_page_config(
    page_title="MetricMind Dashboard",
    page_icon="📊",
    layout="wide"
)


# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/corporate_data_.csv")
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df


df = load_data()


# Dashboard title
st.title("📊 MetricMind Business Dashboard")
st.write("Explore corporate sales performance and business metrics.")


# Sidebar filters
st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["category"].unique()),
    default=sorted(df["category"].unique())
)


# Apply filters
filtered_df = df[
    (df["region"].isin(regions)) &
    (df["category"].isin(categories))
]


# KPI calculations
total_revenue = filtered_df["revenue"].sum()
total_profit = filtered_df["profit"].sum()
total_quantity = filtered_df["quantity"].sum()

profit_margin = (
    (total_profit / total_revenue) * 100
    if total_revenue != 0
    else 0
)


# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{total_revenue:,.2f}")
col2.metric("Total Profit", f"₹{total_profit:,.2f}")
col3.metric("Quantity Sold", f"{total_quantity:,}")
col4.metric("Profit Margin", f"{profit_margin:.2f}%")


st.divider()


# Revenue by region
st.subheader("Revenue by Region")

region_revenue = (
    filtered_df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(region_revenue)


# Profit by category
st.subheader("Profit by Category")

category_profit = (
    filtered_df.groupby("category")["profit"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_profit)


# Revenue by sales channel
st.subheader("Revenue by Sales Channel")

channel_revenue = (
    filtered_df.groupby("sales_channel")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(channel_revenue)


# Monthly revenue trend
st.subheader("Monthly Revenue Trend")

monthly_revenue = (
    filtered_df.groupby(
        filtered_df["order_date"].dt.to_period("M")
    )["revenue"]
    .sum()
)

monthly_revenue.index = monthly_revenue.index.astype(str)

st.line_chart(monthly_revenue)


# Data preview
st.subheader("Filtered Data Preview")

st.dataframe(filtered_df.head(100), width="stretch")