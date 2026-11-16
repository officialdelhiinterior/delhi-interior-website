import urllib.request
import http.server, socketserver, threading, time

class SilentHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

PORT = 8089
httpd = socketserver.TCPServer(('', PORT), SilentHandler)
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()
print('Local server started on port', PORT)

test_urls = [
    f'http://localhost:{PORT}/',
    f'http://localhost:{PORT}/modular-kitchen-delhi/',
    f'http://localhost:{PORT}/portfolio/',
    f'http://localhost:{PORT}/blog/modular-kitchen-cost-delhi/',
    f'http://localhost:{PORT}/thank-you/',
    f'http://localhost:{PORT}/sitemap.xml',
    f'http://localhost:{PORT}/robots.txt',
    f'http://localhost:{PORT}/assets/css/style.css',
    f'http://localhost:{PORT}/assets/js/main.js'
]

all_ok = True
for u in test_urls:
    try:
        with urllib.request.urlopen(u, timeout=5) as resp:
            code = resp.getcode()
            size = len(resp.read())
            print(f'{code} OK - {u} ({size} bytes)')
    except Exception as e:
        print(f'FAIL {u}: {e}')
        all_ok = False

httpd.shutdown()
if all_ok:
    print('[SUCCESS] All HTTP endpoints served with 200 OK.')
