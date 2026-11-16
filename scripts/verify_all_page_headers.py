import re, glob

html_files = glob.glob('**/*.html', recursive=True)
html_files = [f for f in html_files if not f.startswith('brain')]

errors = []

print(f'Verifying header dropdown and structure across {len(html_files)} HTML files...')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()

    # Skip 404 or Thank-you if minimal
    if f in ['404.html', 'thank-you\\index.html']:
        continue

    nav_links = re.findall(r'<ul class="nav-links">([\s\S]*?)</ul>', html)
    if not nav_links:
        errors.append(f'{f}: Missing .nav-links')
        continue

    top_items = re.findall(r'<li\b[^>]*>', nav_links[0])
    if len(top_items) != 6:
        errors.append(f'{f}: Expected 6 top-level nav items, found {len(top_items)}')

    dropdown_links = re.findall(r'class="dropdown-link"', nav_links[0])
    if len(dropdown_links) != 9:
        errors.append(f'{f}: Expected 9 service links in dropdown, found {len(dropdown_links)}')

if errors:
    print(f'[FAIL] Found {len(errors)} header errors:')
    for e in errors:
        print(' -', e)
else:
    print(f'[PASS] All {len(html_files)} pages have the exact 6-item nav and 9-service dropdown!')
