import re

with open('kd_dump.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's extract all major text blocks and headings
lines = html.splitlines()
cleaned_blocks = []
current_block = []

for line in lines:
    text = re.sub(r'<[^>]+>', ' ', line)
    text = re.sub(r'\s+', ' ', text).strip()
    if text:
        cleaned_blocks.append(text)

full_text = '\n'.join(cleaned_blocks)

with open('kd_content_summary.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print("Saved kd_content_summary.txt, total chars:", len(full_text))

# Let's search for key sections
for keyword in ['Years Experience', 'Unique Selling Points', 'Budget Transparency', 'Realistic 3D', 'Material Selection', 'End-to-End', 'Why Do You Need', 'Awesome Interior', 'Testimonial', 'Process']:
    idx = full_text.find(keyword)
    if idx != -1:
        print(f"\n=== KEYWORD: {keyword} ===")
        print(full_text[idx:idx+400])
