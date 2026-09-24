from metrics import (
    load_data,
    get_total_revenue,
    get_total_profit,
    get_total_quantity,
    get_region_performance,
    get_category_performance,
    get_channel_performance,
)

df = load_data()

print("Total Revenue:", get_total_revenue(df))
print("Total Profit:", get_total_profit(df))
print("Total Quantity:", get_total_quantity(df))

print("\nRegion Performance:")
print(get_region_performance(df))

print("\nCategory Performance:")
print(get_category_performance(df))

print("\nChannel Performance:")
print(get_channel_performance(df))


from metrics import (
    get_profit_margin,
    get_average_order_revenue,
    get_monthly_performance,
    get_top_products,
)

print("\nOverall Profit Margin:")
print(f"{get_profit_margin(df):.2f}%")

print("\nAverage Order Revenue:")
print(f"₹{get_average_order_revenue(df):,.2f}")

print("\nMonthly Performance:")
print(get_monthly_performance(df))

print("\nTop 10 Products:")
print(get_top_products(df))