import os, re
from urllib.parse import urlparse

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
    'modular-kitchen-delhi/index.html',
    'wardrobe-design-delhi/index.html',
    'wall-paneling-delhi/index.html',
    'false-ceiling-delhi/index.html',
    'full-home-interior-delhi/index.html',
    'bedroom-furniture-delhi/index.html',
    'doors-partitions-delhi/index.html',
    'painting-polishing-delhi/index.html',
    'plumbing-electrical-delhi/index.html'
]

broken = []

for p in PAGES:
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    links = re.findall(r'href=["\']([^"\']+)["\']', html)
    for link in links:
        if link.startswith('#') or link.startswith('tel:') or link.startswith('mailto:') or link.startswith('http://') or link.startswith('https://'):
            continue
        
        # Internal link check
        clean_path = link.split('?')[0].split('#')[0]
        if clean_path.startswith('/'):
            target = clean_path.lstrip('/')
        else:
            target = clean_path
        
        if target == '' or target == '/':
            target_file = 'index.html'
        elif target.endswith('/'):
            target_file = os.path.join(target, 'index.html')
        elif not os.path.splitext(target)[1]:
            target_file = os.path.join(target, 'index.html')
        else:
            target_file = target
        
        target_file = target_file.replace('/', os.sep)

        if not os.path.exists(target_file):
            broken.append(f'{p} -> {link} (Resolved: {target_file})')

print(f'Checked internal links across {len(PAGES)} pages.')
if broken:
    print(f'Found {len(broken)} broken internal links:')
    for b in broken:
        print('  [BROKEN]', b)
else:
    print('[SUCCESS] All internal links resolve to valid files on disk!')
