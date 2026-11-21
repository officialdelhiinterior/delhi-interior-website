import os, re, json
from PIL import Image

errors = []
warnings = []

PAGES = [
    'index.html',
    '404.html',
    'about/index.html',
    'portfolio/index.html',
    'process/index.html',
    'contact/index.html',
    'thank-you/index.html',
    'privacy-policy/index.html',
    'terms-of-service/index.html',
    'sitemap/index.html',
    'blog/index.html',
    'blog/modular-kitchen-cost-delhi/index.html',
    'blog/fluted-vs-charcoal-panel/index.html',
    'blog/sliding-vs-hinged-wardrobe/index.html',
    'blog/full-home-interior-checklist/index.html',
    'blog/interior-design-mistakes/index.html',
    'blog/main-door-design-guide-delhi/index.html',
    'blog/interior-design-cost-delhi/index.html',
    'modular-kitchen-delhi/index.html',
    'wardrobe-design-delhi/index.html',
    'wall-paneling-delhi/index.html',
    'false-ceiling-delhi/index.html',
    'full-home-interior-delhi/index.html',
    'bedroom-furniture-delhi/index.html',
    'doors-partitions-delhi/index.html',
    'aluminium-glass-work-delhi/index.html',
    'painting-polishing-delhi/index.html',
    'plumbing-electrical-delhi/index.html'
]

print(f'Auditing {len(PAGES)} total HTML pages...')

titles = {}
descriptions = {}

for p in PAGES:
    if not os.path.exists(p):
        errors.append(f'Missing page: {p}')
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Title tag check
    m_title = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
    if not m_title:
        errors.append(f'{p}: Missing <title>')
    else:
        title = m_title.group(1).strip()
        if title in titles and p != 'thank-you/index.html':
            errors.append(f'{p}: Duplicate title with {titles[title]}: "{title}"')
        titles[title] = p

    # 2. Meta description check
    m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.DOTALL | re.IGNORECASE)
    if not m_desc:
        if p != '404.html':
            errors.append(f'{p}: Missing meta description')
    else:
        desc = m_desc.group(1).strip()
        if desc in descriptions and p != 'thank-you/index.html':
            errors.append(f'{p}: Duplicate meta description with {descriptions[desc]}')
        descriptions[desc] = p

    # 3. Exactly one H1 check
    h1s = re.findall(r'<h1\b[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    if len(h1s) != 1:
        errors.append(f'{p}: Expected exactly 1 <h1>, found {len(h1s)}')

    # 4. Image alt text check
    imgs = re.findall(r'<img\b([^>]*)>', html, re.IGNORECASE)
    for img in imgs:
        m_alt = re.search(r'alt=["\'](.*?)["\']', img)
        if not m_alt:
            errors.append(f'{p}: Image missing alt attribute: {img[:60]}')
        else:
            alt = m_alt.group(1).strip()
            if not alt:
                errors.append(f'{p}: Empty image alt attribute: {img[:60]}')
            elif alt.lower() in ['image', 'photo', 'interior', 'img']:
                errors.append(f'{p}: Generic image alt text: "{alt}"')

    # 5. WhatsApp link format check
    wa_links = re.findall(r'href=["\'](https?://wa\.me/[^"\']*)["\']', html)
    for wa in wa_links:
        if 'wa.me/+91' in wa:
            errors.append(f'{p}: Forbidden "+" in WhatsApp link: {wa}')
        if 'wa.me/0' in wa:
            errors.append(f'{p}: Forbidden leading zero in WhatsApp link: {wa}')
        if not wa.startswith('https://wa.me/919643817099') and not wa.startswith('https://wa.me/?text='):
            warnings.append(f'{p}: Unexpected WhatsApp phone link format: {wa}')

    # 6. JSON-LD schema validity check
    schemas = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', html, re.DOTALL)
    for s in schemas:
        try:
            json.loads(s.strip())
        except Exception as e:
            errors.append(f'{p}: JSON-LD syntax error: {e}')

    # 7. Check for forbidden arrow "->" in button text
    buttons = re.findall(r'<(?:button|a)[^>]*class=["\'][^"\']*\bbtn\b[^"\']*["\'][^>]*>(.*?)</(?:button|a)>', html, re.DOTALL)
    for b in buttons:
        clean_btn = re.sub(r'<[^>]+>', '', b).strip()
        if '→' in clean_btn or '->' in clean_btn or '&rarr;' in clean_btn:
            errors.append(f'{p}: Button contains forbidden arrow: "{clean_btn}"')

# 8. Check CSS for forbidden colors & border-radius
css_path = 'assets/css/style.css'
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    if '#111111' in css or '#0b0b0b' in css.lower():
        errors.append('style.css contains forbidden dark colors (#111111 or #0B0B0B)')
    if '#ffd700' in css.lower():
        errors.append('style.css contains forbidden yellow (#FFD700)')

# 9. Verify OG image dimensions
if os.path.exists('og-image.jpg'):
    img = Image.open('og-image.jpg')
    if img.size != (1200, 630):
        errors.append(f'og-image.jpg size is {img.size}, expected (1200, 630)')
else:
    errors.append('Missing og-image.jpg')

# 10. Verify robots.txt and sitemap.xml
if not os.path.exists('robots.txt'):
    errors.append('Missing robots.txt')
if not os.path.exists('sitemap.xml'):
    errors.append('Missing sitemap.xml')

# Summary
print('=' * 60)
print(f'AUDIT COMPLETE. Errors: {len(errors)}, Warnings: {len(warnings)}')
print('=' * 60)
if errors:
    print('ERRORS:')
    for e in errors:
        safe_e = str(e).encode('ascii', 'replace').decode('ascii')
        print('  [FAIL]', safe_e)
else:
    print('[SUCCESS] ALL STRICT CRITERIA PASSED WITHOUT ERRORS!')

if warnings:
    print('WARNINGS:')
    for w in warnings:
        safe_w = str(w).encode('ascii', 'replace').decode('ascii')
        print('  [WARN]', safe_w)
