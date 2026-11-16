import urllib.request
import re

url = "https://k2india.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req, timeout=12) as response:
        content = response.read().decode('utf-8', errors='ignore')
        print(f"Fetched {len(content)} bytes from {url}")

        with open("scripts/k2_raw.html", "w", encoding="utf-8") as f:
            f.write(content)

        # Look for animations, libraries, js files
        scripts = re.findall(r'<script[^>]*src=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE)
        print("\n--- Scripts ---")
        for s in scripts[:20]:
            print(s)

        css_files = re.findall(r'<link[^>]*href=[\'"]([^\'"]+\.css[^\'"]*)[\'"]', content, re.IGNORECASE)
        print("\n--- CSS ---")
        for c in css_files[:15]:
            print(c)

        # Search for animation terms in HTML
        anim_terms = ['gsap', 'scroll', 'swiper', 'aos', 'locomotive', 'motion', 'wow', 'animate', 'fade', 'parallax']
        print("\n--- Animation Terms in HTML ---")
        for t in anim_terms:
            matches = len(re.findall(t, content, re.IGNORECASE))
            print(f"{t}: {matches} matches")

except Exception as e:
    print(f"Error fetching {url}: {e}")
