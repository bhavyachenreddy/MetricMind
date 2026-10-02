import json
from urllib.request import Request, urlopen


CUBE_API_URL = "http://localhost:4000/cubejs-api/v1/load"


def query_cube(measures, dimensions):
    """Query business metrics through the Cube semantic API."""
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


if __name__ == "__main__":
    result = query_cube(
        measures=[
            "sales.total_revenue",
            "sales.total_profit",
        ],
        dimensions=[
            "sales.region",
        ],
    )

    print(json.dumps(result, indent=2))