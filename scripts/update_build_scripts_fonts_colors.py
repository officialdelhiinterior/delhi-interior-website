import glob
import re

def update_build_scripts():
    scripts = [
        'scripts/rebuild_complete_site_v3.py',
        'scripts/build_main_and_utility.py',
        'scripts/update_build_services.py',
        'scripts/update_build_blog.py'
    ]
    new_font = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'

    for f in scripts:
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                c = fp.read()
            c = re.sub(
                r'<link\s+href=[\x22\x27]https://fonts\.googleapis\.com/css2\?[^\x22\x27]+[\x22\x27]\s+rel=[\x22\x27]stylesheet[\x22\x27]>',
                new_font,
                c
            )
            for g in ['#15803D', '#15803d', '#16a34a', '#10b981', '#059669']:
                c = c.replace(g, '#B89058')
            c = c.replace('badge-green', 'pill-badge')
            c = c.replace('pill-badge-red', 'pill-badge')
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(c)
            print(f"Updated: {f}")
        except Exception as e:
            print(f"Error updating {f}: {e}")

if __name__ == '__main__':
    update_build_scripts()
