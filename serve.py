#!/usr/bin/env python3
"""Simple HTTP server for Canada 2026 site — auto-redirect to carnet-voyage.html"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_GET(self):
        # Redirect / → /carnet-voyage.html
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', '/carnet-voyage.html')
            self.end_headers()
            return
        super().do_GET()

if __name__ == '__main__':
    os.chdir(DIR)
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f"Serving Canada 2026 site at http://0.0.0.0:{PORT}")
    print(f"Local: http://192.168.1.70:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
