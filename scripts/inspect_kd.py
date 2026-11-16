import re
from html.parser import HTMLParser

with open('kd_dump.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header / nav
header_match = re.search(r'<header[\s\S]*?</header>', html, re.I)
if not header_match:
    header_match = re.search(r'<nav[\s\S]*?</nav>', html, re.I)

print("--- HEADER FOUND ---" if header_match else "--- NO HEADER TAG ---")
if header_match:
    nav_text = header_match.group(0)
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>([\s\S]*?)</a>', nav_text, re.I)
    for href, raw_text in links:
        clean = re.sub(r'<[^>]+>', '', raw_text).strip()
        if clean:
            print(f"Nav Link: {clean} -> {href}")

# Find all <a> tags with text across page
print("\n--- ALL UNIQUE INTERNAL LINKS ---")
all_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>([\s\S]*?)</a>', html, re.I)
seen = set()
for href, raw_text in all_links:
    clean = re.sub(r'<[^>]+>', '', raw_text).strip()
    if href not in seen and clean and not href.startswith('#') and not href.startswith('javascript'):
        seen.add(href)
        print(f"{clean} -> {href}")

print("\n--- ALL H1, H2, H3 HEADINGS ---")
headings = re.findall(r'<(h[1-3])\b[^>]*>([\s\S]*?)</\1>', html, re.I)
for tag, text in headings:
    clean = re.sub(r'<[^>]+>', '', text).strip()
    clean = re.sub(r'\s+', ' ', clean)
    if clean:
        print(f"[{tag.upper()}] {clean[:120]}")
