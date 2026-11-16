import re

with open("scripts/k2_raw.html", "r", encoding="utf-8") as f:
    html = f.read()

# Look for data-framer attributes, styles, keyframes, transitions
print("Length of k2_raw.html:", len(html))

# Look for keyframes or transform styles
keyframes = re.findall(r'@keyframes[^{]+{[^}]+}', html)
print(f"Keyframes found: {len(keyframes)}")
for k in keyframes[:5]:
    print(k[:150])

# Look for inline style transforms, transitions, opacity
transforms = re.findall(r'transform:[^;]+', html)
print(f"Transform styles: {len(transforms)}")
for t in transforms[:10]:
    print(t)

# Look for text sections / headers
headers = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html)
print(f"\nHeaders found: {len(headers)}")
for h in headers[:10]:
    print(re.sub('<[^<]+?>', '', h).strip())
