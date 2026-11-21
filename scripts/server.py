import http.server
import socketserver
import os

PORT = 8000

class ThreadingSimpleServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        # Concise logging
        sys_stderr = getattr(self, 'server', None)
        print(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}")

handler = NoCacheHTTPRequestHandler
handler.extensions_map.update({
    '.webp': 'image/webp',
    '.svg': 'image/svg+xml',
    '.js': 'application/javascript',
    '.css': 'text/css',
    '.html': 'text/html; charset=utf-8'
})

print(f"Starting Multi-Threaded HTTP Server on port {PORT}...")
try:
    with ThreadingSimpleServer(('127.0.0.1', PORT), handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Server stopped.")
