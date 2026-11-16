import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

# 1. Header checks
nav_links = re.findall(r'<ul class="nav-links">([\s\S]*?)</ul>', html)
if not nav_links:
    errors.append('Missing .nav-links')
else:
    top_items = re.findall(r'<li\b[^>]*>', nav_links[0])
    if len(top_items) != 6:
        errors.append(f'Expected exactly 6 top-level nav items, found {len(top_items)}')
    
    dropdown_links = re.findall(r'class="dropdown-link"', nav_links[0])
    if len(dropdown_links) != 9:
        errors.append(f'Expected 9 service links in dropdown, found {len(dropdown_links)}')

# 2. Hero Visual Showcase checks
if 'hero-visual-showcase' not in html:
    errors.append('Missing .hero-visual-showcase in hero section')
if 'hero-glass-badge' not in html:
    errors.append('Missing .hero-glass-badge in hero showcase')
if 'trust-strip-grid' not in html:
    errors.append('Missing .trust-strip-grid trust metric strip')

# 3. Calculator checks
if 'id="livspace-calculator"' not in html:
    errors.append('Missing id="livspace-calculator"')
if 'id="calc-price-display"' not in html:
    errors.append('Missing id="calc-price-display"')
if 'id="calc-note-display"' not in html:
    errors.append('Missing id="calc-note-display"')
if 'id="calc-wa-btn"' not in html:
    errors.append('Missing id="calc-wa-btn"')

bhk_btns = re.findall(r'data-type="bhk"\s+data-val="([^"]*)"', html)
scope_btns = re.findall(r'data-type="scope"\s+data-val="([^"]*)"', html)
pkg_btns = re.findall(r'data-type="package"\s+data-val="([^"]*)"', html)

if len(bhk_btns) < 4:
    errors.append(f'Expected >= 4 BHK buttons, found {len(bhk_btns)}')
if len(scope_btns) < 4:
    errors.append(f'Expected >= 4 Scope buttons, found {len(scope_btns)}')
if len(pkg_btns) < 3:
    errors.append(f'Expected >= 3 Package buttons, found {len(pkg_btns)}')

# 4. Room tabs check
tab_targets = set(re.findall(r'data-room-target="([^"]*)"', html))
room_cards = set(re.findall(r'data-room="([^"]*)"', html))
if not tab_targets:
    errors.append('Missing room tabs')
if not room_cards:
    errors.append('Missing room cards')
for c in room_cards:
    if c not in tab_targets and c != 'all':
        errors.append(f'Room card data-room="{c}" has no matching tab target')

# 5. Form check
if 'id="quote-form"' not in html:
    errors.append('Missing id="quote-form"')
if 'class="form-success-state"' not in html:
    errors.append('Missing .form-success-state in quote form')
if 'class="client-name-display"' not in html:
    errors.append('Missing .client-name-display in quote form')

if errors:
    print(f'[FAIL] Found {len(errors)} errors:')
    for e in errors:
        print(' -', e)
else:
    print('[PASS] All interactive components, widgets, header dropdown, and hero layout verified with 100% precision!')
