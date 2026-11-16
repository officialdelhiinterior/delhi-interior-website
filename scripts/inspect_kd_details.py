import re

with open('kd_dump.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the entire <header> and top nav
header_match = re.search(r'(<header[\s\S]*?</header>)', html, re.I)
if header_match:
    print("=== HEADER HTML ===")
    print(header_match.group(1)[:3000])

# Let's inspect the CSS links or styles
styles = re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']*)["\']', html, re.I)
print("\n=== STYLESHEETS ===")
for s in styles:
    print(s)

# Let's check the text content of the homepage sections
print("\n=== HOMEPAGE SECTION TEXT SAMPLES ===")
sections = re.findall(r'<section[\s\S]*?</section>', html, re.I)
for i, sec in enumerate(sections):
    clean = re.sub(r'<[^>]+>', ' ', sec)
    clean = re.sub(r'\s+', ' ', clean).strip()
    print(f"\n--- Section {i+1} ({len(clean)} chars) ---")
    print(clean[:350])
