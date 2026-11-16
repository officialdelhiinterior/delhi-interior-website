import glob
import re
import os

def update_google_fonts():
    old_font_pattern = r'<link\s+href=[\x22\x27]https://fonts\.googleapis\.com/css2\?family=Inter:[^\x22\x27]+[\x22\x27]\s+rel=[\x22\x27]stylesheet[\x22\x27]>'
    new_font_tag = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'

    for html_file in glob.glob('**/*.html', recursive=True):
        if 'k2_raw' in html_file or 'blubloom' in html_file:
            continue
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        if re.search(old_font_pattern, content):
            content = re.sub(old_font_pattern, new_font_tag, content)
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated Google Fonts in: {html_file}")
        elif 'Playfair+Display' not in content and 'fonts.googleapis.com' in content:
            # Replace whatever google font link with the new one
            content = re.sub(r'<link\s+href=[\x22\x27]https://fonts\.googleapis\.com/css2\?[^\x22\x27]+[\x22\x27]\s+rel=[\x22\x27]stylesheet[\x22\x27]>', new_font_tag, content)
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated alternate Google Fonts in: {html_file}")

def cleanse_non_whatsapp_green():
    # Only green allowed: WhatsApp button #25D366 / #20BD5A
    # Any other green: #15803D, #16a34a, #10b981, #059669 -> Replace with golden brass #B89058 or dark navy #0B2540
    for html_file in glob.glob('**/*.html', recursive=True):
        if 'k2_raw' in html_file or 'blubloom' in html_file:
            continue
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False
        # Replace badge-green with pill-badge
        if 'badge-green' in content:
            content = content.replace('badge-green', 'pill-badge')
            changed = True
        if 'pill-badge-red' in content:
            content = content.replace('pill-badge-red', 'pill-badge')
            changed = True

        # Replace non-whatsapp inline greens
        for green_hex in ['#15803D', '#15803d', '#16a34a', '#10b981', '#059669']:
            if green_hex in content:
                # check if it's near whatsapp, otherwise replace with #B89058
                content = content.replace(green_hex, '#B89058')
                changed = True

        if changed:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Cleansed non-WhatsApp greens in: {html_file}")

if __name__ == '__main__':
    update_google_fonts()
    cleanse_non_whatsapp_green()
    print("Font & Green cleansing completed!")
