import json
from urllib.request import Request, urlopen


CUBE_API_URL = "http://localhost:4000/cubejs-api/v1/load"


def query_cube(measures, dimensions):
    query = {
        "query": {
            "measures": measures,
            "dimensions": dimensions,
        }
    }

    request = Request(
        CUBE_API_URL,
        data=json.dumps(query).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def test_governed_metrics_are_available():
    result = query_cube(
        ["sales.total_revenue", "sales.total_profit"],
        ["sales.region"],
    )

    assert "data" in result
    assert len(result["data"]) == 4

    for row in result["data"]:
        assert "sales.total_revenue" in row
        assert "sales.total_profit" in row
        assert "sales.region" in row


def test_governed_revenue_total():
    result = query_cube(
        ["sales.total_revenue"],
        [],
    )

    total_revenue = float(result["data"][0]["sales.total_revenue"])

    assert round(total_revenue, 2) == 51078276.55