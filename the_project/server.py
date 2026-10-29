import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>Todo Project v0.1</h1>")


def main():
    port = int(os.environ.get("PORT", 3000))
    server = HTTPServer(("0.0.0.0", port), RequestHandler)
    print(f"Server started in port {port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
