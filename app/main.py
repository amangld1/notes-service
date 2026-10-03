"""A tiny notes service using only the Python standard library."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

NOTES = [
    {"id": 1, "text": "Buy milk"},
    {"id": 2, "text": "Finish INF 345 week 3 lab"},
    {"id": 3, "text": "Read about containers"},
]


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body, content_type="application/json"):
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/":
            self._send(200, "Hello from the notes service!\n", "text/plain; charset=utf-8")
        elif path == "/healthz":
            self._send(200, "ok\n", "text/plain; charset=utf-8")
        elif path == "/notes":
            self._send(200, json.dumps(NOTES))
        else:
            self._send(404, json.dumps({"error": "not found"}))

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


def make_server(port, host="0.0.0.0"):
    return ThreadingHTTPServer((host, port), Handler)


def main():
    port = int(os.environ.get("PORT", "8080"))
    server = make_server(port)
    print(f"Listening on port {port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
