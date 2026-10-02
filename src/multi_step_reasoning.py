import pandas as pd


DATA_PATH = "data/corporate_data_.csv"


def analyze_region_margin(region: str) -> dict:
    """
    Perform multi-step business analysis for a region.

    Steps:
    1. Filter the requested region.
    2. Calculate revenue.
    3. Calculate cost.
    4. Calculate profit.
    5. Calculate profit margin.
    6. Identify the main result.
    """

    df = pd.read_csv(DATA_PATH)

    region_data = df[
        df["region"].str.lower() == region.lower()
    ]

    if region_data.empty:
        return {
            "error": f"No data found for region: {region}"
        }

    revenue = region_data["revenue"].sum()
    cost = region_data["cost"].sum()
    profit = region_data["profit"].sum()

    if revenue == 0:
        margin = 0
    else:
        margin = (profit / revenue) * 100

    return {
        "region": region,
        "revenue": round(revenue, 2),
        "cost": round(cost, 2),
        "profit": round(profit, 2),
        "profit_margin_pct": round(margin, 2),
        "records_analyzed": len(region_data)
    }


def explain_region_margin(region: str) -> str:
    """
    Convert the multi-step analysis into a business explanation.
    """

    result = analyze_region_margin(region)

    if "error" in result:
        return result["error"]

    return (
        f"Multi-step analysis for {result['region']}:\n"
        f"- Revenue: ₹{result['revenue']:,.2f}\n"
        f"- Cost: ₹{result['cost']:,.2f}\n"
        f"- Profit: ₹{result['profit']:,.2f}\n"
        f"- Profit Margin: {result['profit_margin_pct']:.2f}%\n"
        f"- Records analyzed: {result['records_analyzed']}\n\n"
        f"The analysis calculates revenue, cost and profit first, "
        f"and then derives the profit margin from profit divided by revenue."
    )


if __name__ == "__main__":

    region = "North"

    print("MetricMind - Multi-Step Reasoning")
    print("----------------------------------")
    print(explain_region_margin(region))