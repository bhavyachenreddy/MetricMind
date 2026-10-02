def generate_business_explanation(question: str, metric_result: str) -> str:
    """
    Generate a simple business explanation locally
    from the supplied metric result.
    """

    question_lower = question.lower()

    lines = [
        line.strip()
        for line in metric_result.strip().splitlines()
        if line.strip()
    ]

    if not lines:
        return "No metric data is available to explain."

    explanation = []

    # Revenue explanation
    if "revenue" in question_lower:
        explanation.append(
            "The result shows the revenue performance across the requested business segments."
        )

    # Profit explanation
    if "profit" in question_lower:
        explanation.append(
            "The result also shows how profit is distributed across the requested segments."
        )

    # Region/category/channel comparison
    if len(lines) > 1:
        explanation.append(
            f"The analysis contains {len(lines)} reported results, "
            "which can be compared to identify higher and lower performing segments."
        )

    # Include actual data
    explanation.append("Reported metric values:")

    for line in lines[:5]:
        explanation.append(f"- {line}")

    return "\n".join(explanation)


if __name__ == "__main__":

    question = "What is our revenue by region?"

    metric_result = """
North: ₹13,570,772
South: ₹13,002,574
West: ₹12,277,614
East: ₹12,227,316
"""

    print("Business Explanation:")
    print(generate_business_explanation(question, metric_result))