import re

with open('assets/css/style.css.bak', 'r', encoding='utf-8') as f:
    text = f.read()

subpage_classes = [
    'article-body', 'blog-grid', 'portfolio-full-grid', 'contact-grid', 
    'pricing-grid', 'price-tier-card', 'dual-specialty-grid', 'room-cards-grid',
    'materials-grid', 'reviews-grid', 'faq-accordion', 'sticky-mobile-cta',
    'call-float', 'whatsapp-float'
]

for c in subpage_classes:
    matches = re.findall(rf'(\.{c}\b[^{{]*\{{[^}}]*\}})', text)
    print(f"=== {c} ({len(matches)} matches) ===")
    for m in matches[:2]:
        print(m.strip()[:150] + '...')
