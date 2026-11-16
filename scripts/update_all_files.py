import os, re

# ==============================================================================
# Helper replacement function for phone, address, hours, years, 3d, budget, logo
# ==============================================================================

def clean_template(text):
    # 1. Phone numbers
    text = text.replace('9811000000', '9643817099')
    text = text.replace('+91 98110 00000', '+91 96438 17099')
    text = text.replace('98110 00000', '96438 17099')
    text = text.replace('+919811000000', '+919643817099')

    # 2. Address
    text = text.replace('Ring Road, South Extension Part II, New Delhi 110049', 'F-128/4, Mohammadpur, New Delhi, Delhi, 110066')
    text = text.replace('Ring Road, South Extension Part II, New Delhi', 'F-128/4, Mohammadpur, New Delhi, Delhi, 110066')
    text = text.replace('South Extension II, Ring Road, New Delhi', 'F-128/4, Mohammadpur, New Delhi 110066')
    text = text.replace('Ring Road, South Extension Part II', 'F-128/4, Mohammadpur')
    text = text.replace('110049', '110066')
    text = text.replace('Ring+Road+South+Extension+Part+II+New+Delhi', 'F-128%2F4+Mohammadpur+New+Delhi+Delhi+110066')

    # 3. Hours (24 Hours Open)
    text = text.replace('Mon–Sat: 9:00 AM – 7:00 PM', 'Open 24 Hours')
    text = text.replace('Mon–Sat: 9 AM – 7 PM', 'Open 24 Hours')
    text = text.replace('Monday – Saturday: 9:00 AM – 7:00 PM', 'Open 24 Hours (7 Days a Week)')
    text = text.replace('9:00 AM – 7:00 PM', 'Open 24 Hours')
    text = text.replace('9 AM – 7 PM', 'Open 24 Hours')

    # 4. Years (10-Year Type)
    text = text.replace('17+ Years Experience', '10+ Years Experience')
    text = text.replace('17+ Years', '10+ Years')
    text = text.replace('12+ Years Experience', '10+ Years Experience')
    text = text.replace('12+ Years Luxury Interior Design Studio', '10+ Years Luxury Interior Design Studio')
    text = text.replace('12+ Years', '10+ Years')
    text = text.replace('Dedicated to Design Excellence Since 2012', 'Dedicated to Design Excellence Since 2014')
    text = text.replace('Founded in 2012', 'Founded in 2014')
    text = text.replace('Established since 2012', 'Established since 2014')
    text = text.replace('Over the past 12 years', 'Over the past 10+ years')
    text = text.replace('past 12 years', 'past 10+ years')

    # 5. Remove 3D design and budget fluff
    text = text.replace('Free 3D Design Session', 'Free Design Consultation')
    text = text.replace('Free 3D Design &amp; Layout Session', 'Free Site Consultation')
    text = text.replace('Free 3D design &amp; site visit', 'Free design consultation &amp; site visit')
    text = text.replace('Free 3D design', 'Free design consultation')
    text = text.replace('Free 3D Design', 'Free Design Consultation')
    text = text.replace('3D visualizations and AutoCAD precision', 'Architectural working layouts and AutoCAD precision')
    text = text.replace('full 3D visualizations', 'complete architectural drawings')
    text = text.replace('Photorealistic 3D &amp; AutoCAD Working Drawings', 'Architectural Layouts &amp; Working Drawings')
    text = text.replace('Photorealistic 3D & AutoCAD Working Drawings', 'Architectural Layouts & AutoCAD Working Drawings')
    text = text.replace('Photorealistic 3D', 'Architectural Working Drawings')
    text = text.replace('100% Transparent Budget &amp; Editable BOQ', 'Itemized Scope &amp; Fixed Price Guarantee')
    text = text.replace('Budget Transparency &amp; Editable BOQ', 'Itemized Scope &amp; Fixed Price Guarantee')
    text = text.replace('Budget Transparency & Editable BOQ', 'Itemized Scope & Fixed Price Guarantee')
    text = text.replace('No sudden budget surprises', 'No hidden charges')

    # 6. Replace text logo with image logo
    old_logo_html = '<a href="/" class="site-logo" aria-label="Delhi Interior Home">\n        Delhi Interior<span class="logo-dot">.</span>\n      </a>'
    new_logo_html = '<a href="/" class="site-logo" aria-label="Delhi Interior Home">\n        <img src="/assets/images/logo.png" alt="Delhi Interior" width="168" height="52" class="brand-logo-img">\n      </a>'
    text = text.replace(old_logo_html, new_logo_html)

    text = text.replace(
        '<div class="site-logo">Delhi Interior<span class="logo-dot">.</span></div>',
        '<div class="site-logo"><img src="/assets/images/logo.png" alt="Delhi Interior" width="150" height="46" class="brand-logo-img"></div>'
    )
    text = text.replace(
        '<div class="site-logo" style="margin-bottom: 1rem;">\n            Delhi Interior<span class="logo-dot">.</span>\n          </div>',
        '<div class="site-logo" style="margin-bottom: 1.25rem;">\n            <img src="/assets/images/logo.png" alt="Delhi Interior" width="160" height="50" class="brand-logo-img">\n          </div>'
    )
    text = text.replace(
        '<div class="site-logo" style="margin-bottom: 1rem;">Delhi Interior<span class="logo-dot">.</span></div>',
        '<div class="site-logo" style="margin-bottom: 1.25rem;"><img src="/assets/images/logo.png" alt="Delhi Interior" width="160" height="50" class="brand-logo-img"></div>'
    )

    # 7. Remove Under-Nav Bar (Image 1 requested removal)
    under_nav_pattern = r'\s*<!-- LEVEL 3: UNDER-NAV CONTACT TRUST BAR.*?</div>\s*</div>\s*</div>'
    text = re.sub(under_nav_pattern, '', text, flags=re.DOTALL)

    # 8. Add Floating Call Button if not present
    call_float_html = '''  <!-- Floating Call Button (24/7) -->
  <a href="tel:+919643817099" class="call-float" aria-label="Call Delhi Interior">
    <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    <span class="call-tooltip">Call +91 96438 17099 (24/7)</span>
  </a>

  <!-- Floating WhatsApp (24/7) -->'''

    if 'class="call-float"' not in text:
        text = text.replace('  <!-- Floating WhatsApp -->', call_float_html)

    return text

print("=== Updating scripts/build_kd_delhi_home.py ===")
with open('scripts/build_kd_delhi_home.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = clean_template(c)
with open('scripts/build_kd_delhi_home.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("=== Updating scripts/build_main_and_utility.py ===")
with open('scripts/build_main_and_utility.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = clean_template(c)
with open('scripts/build_main_and_utility.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("=== Updating scripts/update_build_services.py ===")
with open('scripts/update_build_services.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = clean_template(c)
with open('scripts/update_build_services.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("=== Updating scripts/build_services.py ===")
with open('scripts/build_services.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = clean_template(c)
with open('scripts/build_services.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done preparing all primary generator scripts!")
