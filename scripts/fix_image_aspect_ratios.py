import os
import re
from PIL import Image

image_cache = {}

# Preload image sizes
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.endswith(('.jpg', '.png', '.webp')):
            p = os.path.join(root, f).replace('\\', '/')
            try:
                im = Image.open(p)
                image_cache[p] = (im.width, im.height)
                # also key without assets/ if needed
                image_cache['/' + p] = (im.width, im.height)
            except Exception:
                pass

fixed_count = 0

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'scripts' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as fp:
                content = fp.read()
            
            new_content = content
            
            # Specific targeted fix for about-team.jpg in about/index.html
            if 'about-team.jpg' in content:
                new_content = re.sub(
                    r'<img\s+src=["\']/assets/images/about-team\.jpg["\']\s+alt=["\']([^"\']*)["\']\s+width=["\']\d+["\']\s+height=["\']\d+["\']([^>]*)>',
                    r'<img src="/assets/images/about-team.jpg" alt="\1" width="1200" height="800"\2 style="border-radius: var(--radius-xl); box-shadow: var(--shadow-xl); width: 100%; height: auto; object-fit: cover; aspect-ratio: 3/2;">',
                    new_content
                )
            
            # Fix any other large image attribute mismatches
            def replace_img(match):
                global fixed_count
                tag = match.group(0)
                attrs = match.group(1)
                
                src_m = re.search(r'src=["\']([^"\']+)["\']', attrs)
                w_m = re.search(r'width=["\'](\d+)["\']', attrs)
                h_m = re.search(r'height=["\'](\d+)["\']', attrs)
                
                if src_m and w_m and h_m:
                    src = src_m.group(1).lstrip('/')
                    w = int(w_m.group(1))
                    h = int(h_m.group(1))
                    
                    if 'logo' in src:
                        return tag
                    
                    if src in image_cache:
                        act_w, act_h = image_cache[src]
                        attr_ratio = w / h
                        actual_ratio = act_w / act_h
                        diff = abs(attr_ratio - actual_ratio)
                        
                        if diff > 0.3:
                            # Recalculate height to match actual ratio while keeping width close
                            new_h = int(round(w / actual_ratio))
                            new_tag = re.sub(r'height=["\']\d+["\']', f'height="{new_h}"', tag)
                            fixed_count += 1
                            print(f"Fixed {src} in {filepath}: {w}x{h} -> {w}x{new_h}")
                            return new_tag
                return tag

            new_content = re.sub(r'<img\s+([^>]+)>', replace_img, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as fp:
                    fp.write(new_content)
                print(f"Updated HTML file: {filepath}")

print(f"Total img tags adjusted: {fixed_count}")
