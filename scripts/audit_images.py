import glob
import re
from collections import defaultdict
import os

html_files = glob.glob('**/*.html', recursive=True)
images_used = defaultdict(list)

for f in html_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    # Find all image links
    matches = re.findall(r'/assets/images/[a-zA-Z0-9_\-\.]+', c)
    for m in set(matches):
        images_used[m].append(f)

print(f"Total distinct image URLs referenced: {len(images_used)}")
for img, pages in sorted(images_used.items()):
    exists = os.path.exists('.' + img)
    size = os.path.getsize('.' + img) if exists else 0
    print(f"{img} (exists={exists}, size={size//1024}KB) : used in {len(pages)} files")
