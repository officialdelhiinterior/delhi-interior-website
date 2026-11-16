import urllib.request

test_urls = [
    'http://localhost:8000/',
    'http://localhost:8000/modular-kitchen-delhi/',
    'http://localhost:8000/wardrobe-design-delhi/',
    'http://localhost:8000/full-home-interior-delhi/',
    'http://localhost:8000/portfolio/',
    'http://localhost:8000/process/',
    'http://localhost:8000/about/',
    'http://localhost:8000/contact/',
    'http://localhost:8000/blog/',
    'http://localhost:8000/blog/modular-kitchen-cost-delhi/',
    'http://localhost:8000/thank-you/',
    'http://localhost:8000/assets/css/style.css',
    'http://localhost:8000/assets/js/main.js'
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

if all_ok:
    print('[SUCCESS] All local server endpoints served with 200 OK on port 8000.')
