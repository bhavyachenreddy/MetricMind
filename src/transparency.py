import json


def create_transparency_record(
    question: str,
    metric: str,
    dimensions: list,
    filters: dict,
    sql: str = ""
) -> dict:
    """
    Create a transparent record showing how a business
    question was processed.
    """

    return {
        "question": question,
        "metric": metric,
        "dimensions": dimensions,
        "filters": filters,
        "sql": sql
    }


def display_transparency(record: dict):
    """Display the transparency information."""

    print("\n=== MetricMind Transparency ===")

    print("\nQuestion:")
    print(record["question"])

    print("\nMetric:")
    print(record["metric"])

    print("\nDimensions:")
    print(", ".join(record["dimensions"]))

    print("\nFilters:")
    print(json.dumps(record["filters"], indent=2))

    if record["sql"]:
        print("\nSQL:")
        print(record["sql"])
    else:
        print("\nSQL:")
        print("No SQL generated.")


if __name__ == "__main__":

    record = create_transparency_record(
        question="Show revenue by region",
        metric="Revenue",
        dimensions=["Region"],
        filters={},
        sql="""
SELECT
    region,
    SUM(revenue) AS revenue
FROM corporate_data
GROUP BY region
ORDER BY revenue DESC;
"""
    )

    display_transparency(record)