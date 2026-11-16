import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section\b([^>]*)>', html)
print(f'Total <section> tags: {len(sections)}')
for i, s in enumerate(sections):
    m_cls = re.search(r'class=["\']([^"\']*)["\']', s)
    m_id = re.search(r'id=["\']([^"\']*)["\']', s)
    cls = m_cls.group(1) if m_cls else 'NO_CLASS'
    sid = m_id.group(1) if m_id else 'NO_ID'
    print(f'  {i+1}. class="{cls}" id="{sid}"')
