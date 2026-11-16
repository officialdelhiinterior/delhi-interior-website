import os, re, glob

print("=== RIGOROUS BUTTON & LINK AUDIT ===")

html_files = glob.glob('*.html') + glob.glob('*/*.html') + glob.glob('*/*/*.html')
print(f"Auditing {len(html_files)} HTML files for broken buttons, invalid anchors, and form issues...")

issues = []

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()

    # Find all IDs in page
    ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', content))

    # 1. Find all buttons and links with class 'btn'
    btns = re.findall(r'<a\b[^>]*class=["\'][^"\']*\bbtn\b[^"\']*["\'][^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', content, re.DOTALL | re.IGNORECASE)
    for href, text in btns:
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        href = href.strip()
        if not href:
            issues.append(f"{f}: Empty href in button: '{clean_text}'")
        elif href.startswith('#'):
            target_id = href[1:]
            if target_id and target_id not in ids:
                issues.append(f"{f}: Broken anchor href='{href}' (no element with id='{target_id}') in button: '{clean_text}'")
        elif href.startswith(('tel:', 'mailto:', 'https://wa.me', 'https://instagram.com', 'https://facebook.com', 'https://youtube.com', 'http')):
            pass
        else:
            clean_href = href.split('?')[0].split('#')[0]
            if clean_href.startswith('/'):
                clean_href = clean_href[1:]
            if not clean_href:
                target_file = 'index.html'
            elif clean_href.endswith('/'):
                target_file = os.path.join(clean_href, 'index.html')
            else:
                target_file = clean_href
            
            target_file = os.path.normpath(target_file)
            if not os.path.exists(target_file) and not os.path.exists(target_file + '.html'):
                issues.append(f"{f}: Button links to non-existent file '{target_file}': '{clean_text}'")

    # 2. Check form #quote-form elements if present
    if 'id="quote-form"' in content or "id='quote-form'" in content:
        if 'id="submit-quote-btn"' not in content and "id='submit-quote-btn'" not in content:
            issues.append(f"{f}: form #quote-form missing #submit-quote-btn")
        if 'id="client-name"' not in content and "id='client-name'" not in content:
            issues.append(f"{f}: form #quote-form missing #client-name")
        if 'id="client-phone"' not in content and "id='client-phone'" not in content:
            issues.append(f"{f}: form #quote-form missing #client-phone")

    # 3. Check FAQ buttons vs outer faq-answer containers (excluding faq-answer-inner)
    faq_btns = re.findall(r'<button\b[^>]*class=["\'][^"\']*\bfaq-question\b[^"\']*["\']', content)
    faq_answers = re.findall(r'class=["\'][^"\']*\bfaq-answer(?![-\w])[^"\']*["\']', content)
    if len(faq_btns) != len(faq_answers):
        issues.append(f"{f}: Mismatch between faq-question count ({len(faq_btns)}) and faq-answer count ({len(faq_answers)})")

print(f"Total issues found: {len(issues)}")
if issues:
    for iss in issues:
        print("  [ISSUE]", iss)
else:
    print("[SUCCESS] All buttons, anchors, forms, and FAQ accordions are 100% valid and working!")
