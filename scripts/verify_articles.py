import os, re

files = [
    ('blog/modular-kitchen-cost-delhi/index.html', 'modular kitchen cost in Delhi'),
    ('blog/fluted-vs-charcoal-panel/index.html', 'fluted panel vs charcoal panel'),
    ('blog/sliding-vs-hinged-wardrobe/index.html', 'sliding vs hinged wardrobe Delhi'),
    ('blog/full-home-interior-checklist/index.html', 'full home interior checklist Delhi'),
    ('blog/interior-design-mistakes/index.html', 'interior design mistakes to avoid')
]

for path, kw in files:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    text = re.sub(r'<[^>]+>', ' ', html)
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    kw_count = len(re.findall(re.escape(kw), text, re.IGNORECASE))
    h2_count = len(re.findall(r'<h2\b', html, re.IGNORECASE))
    h3_count = len(re.findall(r'<h3\b', html, re.IGNORECASE))
    has_wa = 'wa.me' in html

    print(f'{path}:')
    print(f'  Words: {word_count} (>=1000 required)')
    print(f'  Keyword: "{kw}" count: {kw_count} (5-8 target)')
    print(f'  H2s: {h2_count}, H3s: {h3_count}')
    print(f'  Has WhatsApp CTA: {has_wa}')
