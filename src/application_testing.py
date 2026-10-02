from query_governance import validate_query
from multi_step_reasoning import analyze_region_margin
from dynamic_visualizations import generate_visualization
from business_explanations import generate_business_explanation


def test_revenue_query():
    result = validate_query(
        "revenue",
        ["region"]
    )

    assert result["allowed"] is True
    print("PASS: Revenue by region")


def test_profit_query():
    result = validate_query(
        "profit",
        ["category"]
    )

    assert result["allowed"] is True
    print("PASS: Profit by category")


def test_invalid_metric():
    result = validate_query(
        "customer_salary",
        ["region"]
    )

    assert result["allowed"] is False
    print("PASS: Invalid metric rejected")


def test_invalid_dimension():
    result = validate_query(
        "revenue",
        ["customer_age"]
    )

    assert result["allowed"] is False
    print("PASS: Invalid dimension rejected")


def test_region_analysis():
    result = analyze_region_margin("North")

    assert "revenue" in result
    assert "profit" in result
    assert "profit_margin_pct" in result

    print("PASS: Region margin analysis")


def test_business_explanation():
    explanation = generate_business_explanation(
        "What is revenue by region?",
        "North: ₹13,570,772\nSouth: ₹13,002,574"
    )

    assert len(explanation) > 0

    print("PASS: Business explanation")


def test_dynamic_visualization():
    path = generate_visualization("region")

    assert path.endswith(".png")

    print("PASS: Dynamic visualization")


if __name__ == "__main__":

    print("\n=== MetricMind Application Testing ===\n")

    test_revenue_query()
    test_profit_query()
    test_invalid_metric()
    test_invalid_dimension()
    test_region_analysis()
    test_business_explanation()
    test_dynamic_visualization()

    print("\nAll MetricMind application tests passed.")