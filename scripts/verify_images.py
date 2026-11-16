import glob, os, re

html_files = glob.glob('**/*.html', recursive=True)
all_images = set()

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    srcesets = re.findall(r'<source[^>]+srcset=["\']([^"\']+)["\']', content)
    for s in srcs + srcesets:
        if not s.startswith('http') and not s.startswith('data:'):
            all_images.add(s)

missing = []
for img in all_images:
    clean_path = img.lstrip('/')
    if not os.path.exists(clean_path):
        missing.append((img, clean_path))

print(f"Total unique local images referenced: {len(all_images)}")
print(f"Missing images: {len(missing)}")
if missing:
    for m in missing:
        print("  Missing image:", m)
else:
    print("[SUCCESS] All referenced images exist on disk!")
