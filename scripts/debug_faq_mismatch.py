import re

with open('modular-kitchen-delhi/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

faq_start = text.find('faq-accordion')
faq_block = text[faq_start:faq_start + 4000]
print(faq_block[:2500])
