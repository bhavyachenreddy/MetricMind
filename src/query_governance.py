ALLOWED_METRICS = {
    "revenue",
    "profit",
    "quantity",
    "profit_margin"
}

ALLOWED_DIMENSIONS = {
    "region",
    "category",
    "sales_channel",
    "order_date"
}


def validate_query(metric: str, dimensions: list) -> dict:
    """
    Validate whether a MetricMind query uses
    approved metrics and dimensions.
    """

    metric = metric.lower().strip()

    dimensions = [
        dimension.lower().strip()
        for dimension in dimensions
    ]

    if metric not in ALLOWED_METRICS:
        return {
            "allowed": False,
            "reason": f"Metric '{metric}' is not approved."
        }

    unsupported_dimensions = [
        dimension
        for dimension in dimensions
        if dimension not in ALLOWED_DIMENSIONS
    ]

    if unsupported_dimensions:
        return {
            "allowed": False,
            "reason": (
                "Unsupported dimension(s): "
                + ", ".join(unsupported_dimensions)
            )
        }

    return {
        "allowed": True,
        "reason": "Query uses approved metrics and dimensions."
    }


def check_query(metric: str, dimensions: list):
    """Print the governance decision."""

    result = validate_query(metric, dimensions)

    print("\n=== MetricMind Query Governance ===")

    print(f"Metric: {metric}")
    print(f"Dimensions: {dimensions}")

    if result["allowed"]:
        print("Status: ALLOWED")
    else:
        print("Status: REJECTED")

    print(f"Reason: {result['reason']}")


if __name__ == "__main__":

    # Approved query
    check_query(
        "revenue",
        ["region"]
    )

    # Rejected query
    check_query(
        "customer_salary",
        ["region"]
    )

    # Rejected dimension
    check_query(
        "profit",
        ["customer_age"]
    )