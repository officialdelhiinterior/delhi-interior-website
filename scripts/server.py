import http.server
import socketserver
import sys

PORT = 8000

class ThreadingSimpleServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

handler = NoCacheHTTPRequestHandler
handler.extensions_map.update({
    '.webp': 'image/webp',
    '.svg': 'image/svg+xml',
    '.js': 'application/javascript',
    '.css': 'text/css',
    '.html': 'text/html; charset=utf-8'
})

print(f"Starting Multi-Threaded HTTP Server on port {PORT}...")
with ThreadingSimpleServer(('', PORT), handler) as httpd:
    httpd.serve_forever()
