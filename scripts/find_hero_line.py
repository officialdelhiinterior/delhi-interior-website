with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:350]):
    if 'hero' in l.lower() or 'trust' in l.lower():
        print(f"{i+1}: {l.strip()[:100]}")
