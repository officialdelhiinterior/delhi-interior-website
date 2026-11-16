import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find all img tags
img_tags = re.findall(r'<img[^>]+>', text)
print(f"Total <img> tags in index.html: {len(img_tags)}")
for i, tag in enumerate(img_tags):
    src = re.search(r'src=["\']([^"\']+)["\']', tag)
    alt = re.search(r'alt=["\']([^"\']+)["\']', tag)
    src_val = src.group(1) if src else "NO_SRC"
    alt_val = alt.group(1) if alt else "NO_ALT"
    print(f"{i+1:2d}. src={src_val:<35} | alt={alt_val}")

print("\n--- Background images in CSS / HTML ---")
bg_imgs = re.findall(r'url\([\"\']?([^\"\'\)]+)[\"\']?\)', text)
for bg in set(bg_imgs):
    print("HTML inline background:", bg)
