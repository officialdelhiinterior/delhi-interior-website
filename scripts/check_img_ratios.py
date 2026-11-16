import os
import re
from PIL import Image

image_cache = {}
large_mismatches = []

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'scripts' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as fp:
                content = fp.read()
            
            for match in re.finditer(r'<img\s+([^>]+)>', content):
                attrs = match.group(1)
                src_m = re.search(r'src=["\']([^"\']+)["\']', attrs)
                w_m = re.search(r'width=["\'](\d+)["\']', attrs)
                h_m = re.search(r'height=["\'](\d+)["\']', attrs)
                
                if src_m and w_m and h_m:
                    src = src_m.group(1).lstrip('/')
                    w = int(w_m.group(1))
                    h = int(h_m.group(1))
                    
                    if 'logo' in src:
                        continue
                    
                    if os.path.exists(src):
                        if src not in image_cache:
                            try:
                                im = Image.open(src)
                                image_cache[src] = (im.width, im.height)
                            except Exception:
                                continue
                        actual_w, actual_h = image_cache[src]
                        attr_ratio = w / h
                        actual_ratio = actual_w / actual_h
                        diff = abs(attr_ratio - actual_ratio)
                        if diff > 0.3:
                            large_mismatches.append((filepath, src, w, h, actual_w, actual_h, diff, match.group(0)))

print(f"Total large mismatches: {len(large_mismatches)}")
for item in large_mismatches:
    print(f"{item[0]}: {item[1]} (attr: {item[2]}x{item[3]} -> ratio {item[2]/item[3]:.2f} vs actual: {item[4]}x{item[5]} -> ratio {item[4]/item[5]:.2f})")
