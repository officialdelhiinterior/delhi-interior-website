import re

def remove_material_section():
    # 1. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match the material showcase section
    pattern = r'\s*<!-- 8\. MATERIAL SHOWCASE \("QUALITY YOU CAN FEEL"\) -->\s*<section class="material-showcase-section">.*?</section>'
    
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        print("Found material section in index.html, removing...")
        new_content = content[:match.start()] + "\n\n" + content[match.end():]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully removed from index.html!")
    else:
        print("Warning: regex pattern did not match in index.html!")

    # 2. Update scripts/rebuild_complete_site_v3.py
    with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
        rebuild_script = f.read()

    match_script = re.search(pattern, rebuild_script, flags=re.DOTALL)
    if match_script:
        print("Found material section in scripts/rebuild_complete_site_v3.py, removing...")
        new_script = rebuild_script[:match_script.start()] + "\n\n" + rebuild_script[match_script.end():]
        with open('scripts/rebuild_complete_site_v3.py', 'w', encoding='utf-8') as f:
            f.write(new_script)
        print("Successfully removed from scripts/rebuild_complete_site_v3.py!")
    else:
        print("Warning: regex pattern did not match in scripts/rebuild_complete_site_v3.py!")

if __name__ == '__main__':
    remove_material_section()
