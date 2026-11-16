import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

div_classes = set(re.findall(r'<div class="([^"]+)"', text))
grid_classes = [c for c in div_classes if any(k in c for k in ['grid', 'layout', 'row', 'container', 'box', 'strip', 'hero', 'tier', 'usps', 'review', 'brief'])]
print("Structural classes found in index.html:")
for c in sorted(grid_classes):
    print(" -", c)

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("\nMissing CSS rules in style.css:")
for c in sorted(grid_classes):
    for single_class in c.split():
        if f".{single_class}" not in css:
            print(f"  MISSING: .{single_class}")
