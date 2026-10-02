from http.server import BaseHTTPRequestHandler, HTTPServer


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>MetricMind Chat</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
        }

        #chat {
            border: 1px solid #ccc;
            height: 400px;
            padding: 15px;
            overflow-y: auto;
            margin-bottom: 15px;
        }

        input {
            width: 75%;
            padding: 12px;
        }

        button {
            padding: 12px 20px;
        }

        .user {
            margin: 10px 0;
            font-weight: bold;
        }

        .bot {
            margin: 10px 0;
        }
    </style>
</head>

<body>

<h1>MetricMind</h1>

<div id="chat">
    <div class="bot">MetricMind: Ask me about your business metrics.</div>
</div>

<input id="message" type="text" placeholder="Ask about revenue, profit, region...">
<button onclick="sendMessage()">Send</button>

<script>
async function sendMessage() {
    const input = document.getElementById("message");
    const chat = document.getElementById("chat");

    const message = input.value.trim();

    if (!message) {
        return;
    }

    chat.innerHTML += `<div class="user">You: ${message}</div>`;

    input.value = "";

    try {
        const response = await fetch(
            "http://localhost:8000/api/metrics"
        );

        const data = await response.json();

        const rows = data.data || [];

let message = "MetricMind:<br>";

for (const row of rows) {
    message += `Region: ${row["sales.region"]}<br>`;
    message += `Revenue: ${row["sales.total_revenue"]}<br>`;
    message += `Profit: ${row["sales.total_profit"]}<br><br>`;
}

chat.innerHTML += `<div class="bot">${message}</div>`;
    } catch (error) {
        chat.innerHTML +=
            `<div class="bot">MetricMind: Backend connection failed.</div>`;
    }

    chat.scrollTop = chat.scrollHeight;
}
</script>

</body>
</html>
"""


class ChatUIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(HTML.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), ChatUIHandler)

    print("MetricMind Chat UI running at http://localhost:8080")

    server.serve_forever()