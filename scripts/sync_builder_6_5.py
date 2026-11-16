import re

with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    text = f.read()

with open('scripts/update_section_6_5.py', 'r', encoding='utf-8') as f:
    script_c = f.read()

m = re.search(r'new_section_6_5_html = """([\s\S]*?)"""', script_c)
if m:
    new_sec = m.group(1)
    pattern = r'<!-- 6\.5 AN INTERIOR SOLUTION[\s\S]*?</section>'
    updated, count = re.subn(pattern, new_sec, text, count=1)
    print('Updated rebuild_complete_site_v3.py count:', count)
    with open('scripts/rebuild_complete_site_v3.py', 'w', encoding='utf-8') as f:
        f.write(updated)
