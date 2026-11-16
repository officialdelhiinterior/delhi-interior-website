import glob, re

all_classes = set()
for fpath in glob.glob('**/*.html', recursive=True):
    if 'k2_raw.html' in fpath or '.user_uploaded' in fpath:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    classes = re.findall(r'class=["\']([^"\']+)["\']', html)
    for c_str in classes:
        for c in c_str.split():
            all_classes.add(c)

print(f'Total unique classes across all HTML pages: {len(all_classes)}')
with open('scripts/all_used_classes.txt', 'w', encoding='utf-8') as out:
    for c in sorted(all_classes):
        out.write(c + '\n')
print('Saved all used classes to scripts/all_used_classes.txt')
