import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen


CUBE_API_URL = "http://localhost:4000/cubejs-api/v1/load"


def query_cube():
    payload = {
        "query": {
            "measures": [
                "sales.total_revenue",
                "sales.total_profit"
            ],
            "dimensions": [
                "sales.region"
            ]
        }
    }

    request = Request(
        CUBE_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


class BackendHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/metrics":
            try:
                result = query_cube()

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()

                self.wfile.write(
                    json.dumps(result).encode("utf-8")
                )

            except Exception as error:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                self.wfile.write(
                    json.dumps({"error": str(error)}).encode("utf-8")
                )

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), BackendHandler)

    print("Backend API running at http://localhost:8000")
    print("Metrics endpoint: http://localhost:8000/api/metrics")

    server.serve_forever()