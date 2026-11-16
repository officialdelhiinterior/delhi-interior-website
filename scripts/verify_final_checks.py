with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = {
    'F-128/4, Mohammadpur': 'F-128/4, Mohammadpur' in text,
    '+91 96438 17099': '+91 96438 17099' in text,
    'Open 24 Hours or 24/7': 'Open 24 Hours' in text or '24/7' in text,
    'why-choose-floating-box': 'why-choose-floating-box' in text,
    'brief-tiers-container': 'brief-tiers-container' in text,
    'Call button present': 'class="call-float"' in text,
    'WhatsApp button present': 'class="whatsapp-float"' in text,
    'Call above WhatsApp in HTML': text.find('class="call-float"') < text.find('class="whatsapp-float"') and text.find('class="call-float"') != -1,
    'Quality You Can Feel absent': 'Quality You Can Feel' not in text,
    'CERTIFIED MATERIALS absent': 'CERTIFIED MATERIALS' not in text,
    '45 Days absent': '45 Days' not in text and '45-Day' not in text and '45 days' not in text,
}

for k, v in checks.items():
    print(f'[{ "PASS" if v else "FAIL" }] {k}')
