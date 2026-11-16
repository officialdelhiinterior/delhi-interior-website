import glob, re

files = glob.glob('**/*.html', recursive=True)
claims = ['10,000', '10k', 'sq. ft.', 'sqft', 'sq ft', 'facility', 'factory', 'plant', 'ISO', 'award', 'acres', 'square feet']

found = []
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    for cl in claims:
        matches = re.finditer(re.escape(cl), c, re.IGNORECASE)
        for m in matches:
            start = max(0, m.start() - 60)
            end = min(len(c), m.end() + 60)
            snippet = c[start:end].replace('\n', ' ').strip()
            # If it's a rate like "₹180 per sq. ft." in a blog or service pricing table, keep track separately
            is_rate = bool(re.search(r'₹\s*\d+.*(?:per|/)\s*sq', snippet, re.IGNORECASE))
            found.append((f, cl, snippet, is_rate))

print(f"Total mentions found: {len(found)}")
print("\n--- NON-RATE CLAIMS (Facility / Size / Exaggerations) ---")
for f, cl, snippet, is_rate in found:
    if not is_rate:
        print(f"[{f}] ({cl}): {snippet}")
