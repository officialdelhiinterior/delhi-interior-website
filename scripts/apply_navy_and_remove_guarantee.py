import os, re

print("Starting complete removal of warranty, guarantee, and 45-day claims, and applying Dark Navy Blue brand palette...")

# -----------------------------------------------------------------------------
# 1. UPDATE scripts/rebuild_complete_site_v3.py (Homepage Generator)
# -----------------------------------------------------------------------------
with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    home_code = f.read()

# Meta and Head
home_code = re.sub(
    r'10\+ years experience, direct workshop rates, modular kitchens, custom wardrobes, turnkey interiors and 10-year warranty\.',
    '10+ years experience, direct workshop rates, modular kitchens, custom wardrobes, and full-home turnkey interiors.',
    home_code
)
home_code = re.sub(
    r'How It Works \(45 Days\)',
    'How It Works',
    home_code
)
home_code = re.sub(
    r'Our 45-Day Process',
    'Our Execution Process',
    home_code
)

# Hero Section
home_code = home_code.replace(
    'get direct craftsman rates, 45-day handover, and a 10-year warranty.',
    'get direct craftsman rates, structured milestone delivery, and enduring structural durability.'
)
home_code = home_code.replace(
    '<span>10-Year Comprehensive Warranty</span>',
    '<span>Certified BWP 710 Marine Plywood</span>'
)
home_code = home_code.replace(
    '<strong>10-Year Warranty</strong>\n                <span>Certified BWP Marine Ply &amp; German Fittings</span>',
    '<strong>Authentic Materials</strong>\n                <span>Certified BWP Marine Ply &amp; German Fittings</span>'
)
home_code = home_code.replace(
    '<strong>10-Year Warranty</strong>',
    '<strong>Authentic Materials</strong>'
)
home_code = home_code.replace(
    '<span>Direct Craftsman Guarantee · Zero Spam · 100% Free Site Visit in Delhi NCR</span>',
    '<span>Direct Master Craftsmen · Zero Spam · 100% Free Site Visit in Delhi NCR</span>'
)

# Trust Metrics
old_trust = '''        <div class="trust-item">
          <h4 class="metric-counter" data-target="10" data-suffix="+ Years">10<span>+ Years</span></h4>
          <p>Design &amp; Woodwork Excellence</p>
        </div>
        <div class="trust-item">
          <h4 class="metric-counter" data-target="500" data-suffix="+">500<span>+</span></h4>
          <p>Delivered Homes in Delhi NCR</p>
        </div>
        <div class="trust-item">
          <h4 class="metric-counter" data-target="45" data-suffix=" Days">45<span> Days</span></h4>
          <p>Move-In Delivery Guarantee</p>
        </div>
        <div class="trust-item">
          <h4 class="metric-counter" data-target="10" data-suffix=" Years">10<span> Years</span></h4>
          <p>Comprehensive Written Warranty</p>
        </div>'''

new_trust = '''        <div class="trust-item">
          <h4 class="metric-counter" data-target="10" data-suffix="+ Years">10<span>+ Years</span></h4>
          <p>Design &amp; Woodwork Excellence</p>
        </div>
        <div class="trust-item">
          <h4 class="metric-counter" data-target="500" data-suffix="+">500<span>+</span></h4>
          <p>Delivered Homes in Delhi NCR</p>
        </div>
        <div class="trust-item">
          <h4 class="metric-counter" data-target="100" data-suffix="%">100<span>%</span></h4>
          <p>In-House Master Carpenters</p>
        </div>
        <div class="trust-item">
          <h4 class="metric-counter" data-target="100" data-suffix="%">100<span>%</span></h4>
          <p>Certified Authentic Materials</p>
        </div>'''

if old_trust in home_code:
    home_code = home_code.replace(old_trust, new_trust)
    print("Replaced Trust Metrics in rebuild_complete_site_v3.py")
else:
    # Fallback regex replace for trust items
    home_code = re.sub(
        r'<h4 class="metric-counter"[^>]*>45<span> Days</span></h4>\s*<p>Move-In Delivery Guarantee</p>',
        '<h4 class="metric-counter" data-target="100" data-suffix="%">100<span>%</span></h4>\n          <p>In-House Master Carpenters</p>',
        home_code
    )
    home_code = re.sub(
        r'<h4 class="metric-counter"[^>]*>10<span> Years</span></h4>\s*<p>Comprehensive Written Warranty</p>',
        '<h4 class="metric-counter" data-target="100" data-suffix="%">100<span>%</span></h4>\n          <p>Certified Authentic Materials</p>',
        home_code
    )

# USPs Section
home_code = home_code.replace(
    '<h3>Itemized Scope &amp; Specification Guarantee</h3>',
    '<h3>Itemized Scope &amp; Detailed Specifications</h3>'
)
home_code = home_code.replace(
    '<h3>Guaranteed Timelines &amp; Video Progress</h3>',
    '<h3>Structured Timelines &amp; Video Progress</h3>'
)
home_code = home_code.replace(
    '<p>45-day milestone handover backed by written penalty commitments. Weekly WhatsApp photo and video logs keep you updated without taking time off work.</p>',
    '<p>Milestone-driven execution with structured stage handovers. Weekly WhatsApp photo and video logs keep you updated without taking time off work.</p>'
)

# Why Need Designers Section
home_code = home_code.replace(
    '<h4>Transparent Scope Guarantee</h4>',
    '<h4>Transparent Scope &amp; Detailed BOQ</h4>'
)
home_code = home_code.replace(
    "Our comprehensive scope guarantees every detail and material specification is committed in writing.",
    "Our comprehensive scope ensures every detail and material specification is committed in writing."
)

# Services Section
home_code = home_code.replace(
    'with 10-year warranty protection.',
    'with verified premium materials.'
)
home_code = home_code.replace(
    '<span class="service-visual-tag">Turnkey 45 Days</span>',
    '<span class="service-visual-tag">Turnkey Execution</span>'
)
home_code = home_code.replace(
    '<span class="service-visual-pill">10-Yr Warranty</span>',
    '<span class="service-visual-pill">BWP Marine Ply</span>'
)
home_code = home_code.replace(
    '<span class="service-visual-badge">✦ Turnkey 45-Day Handover</span>',
    '<span class="service-visual-badge">✦ Complete Turnkey Execution</span>'
)

# Materials Section
home_code = home_code.replace(
    'with a 10-year official warranty.',
    'built for enduring performance.'
)

# Room Explorer
home_code = home_code.replace(
    '<div class="price-chip">Delivered in <strong>45 Days</strong></div>',
    '<div class="price-chip">Scope: <strong>Turnkey Lounge</strong></div>'
)

# FAQ Section
home_code = home_code.replace(
    '<span>How does Delhi Interior guarantee a 45-day move-in timeline?</span>',
    '<span>How does Delhi Interior streamline project timelines and execution?</span>'
)
home_code = home_code.replace(
    'slashing on-site assembly time to just 10–14 days.',
    'significantly accelerating on-site installation and ensuring orderly progress.'
)
home_code = home_code.replace(
    '<span>What is covered under your 10-Year Warranty?</span>',
    '<span>What material quality standards and durability assurances do you follow?</span>'
)
home_code = home_code.replace(
    'Our comprehensive 10-year written warranty covers delamination, termite infestation, and structural integrity of all calibrated BWP 710 marine plywood and HDMR carcasses, alongside official brand warranties on Blum, Hettich, and Ebco hardware.',
    'We exclusively build using calibrated BWP 710 marine plywood, Greenpanel HDMR boards, and authentic hardware from Blum, Hettich, and Hafele. Our direct joinery techniques and moisture-resistant fabrication deliver lasting structural stability and termite resilience.'
)

# Footer Section
home_code = home_code.replace(
    'backed by a 10-year warranty.',
    'crafted by master artisans.'
)

with open('scripts/rebuild_complete_site_v3.py', 'w', encoding='utf-8') as f:
    f.write(home_code)
print("Updated rebuild_complete_site_v3.py successfully.")

# -----------------------------------------------------------------------------
# 2. UPDATE scripts/build_main_and_utility.py
# -----------------------------------------------------------------------------
with open('scripts/build_main_and_utility.py', 'r', encoding='utf-8') as f:
    main_code = f.read()

# Header & Footer Navigation
main_code = main_code.replace('How It Works (45 Days)', 'How It Works')
main_code = main_code.replace('backed by a 10-year warranty', 'crafted by master artisans')

# Process Page
main_code = main_code.replace(
    "title='How It Works | 45-Day Turnkey Home Journey | Delhi Interior'",
    "title='How It Works | Structured Turnkey Home Journey | Delhi Interior'"
)
main_code = main_code.replace(
    "desc='A transparent, milestone-driven workflow that eliminates guesswork. From laser room scan to final handover.'",
    "desc='A transparent, milestone-driven workflow that eliminates guesswork. From laser room scan to structured handover.'"
)
main_code = main_code.replace(
    'Stamped 10-year studio warranty and hardware certificates',
    'Original manufacturer hardware certificates and material authenticity records'
)

# About Page
main_code = main_code.replace(
    'title=\'About Delhi Interior | 10+ Years Luxury Interior Design & Woodwork Studio\'',
    'title=\'About Delhi Interior | 10+ Years Luxury Interior Design & Woodwork Studio\''
)
main_code = main_code.replace(
    '<div style="font-size: 0.95rem; font-weight: 700; color: var(--color-dark);">Flat Warranty</div>',
    '<div style="font-size: 0.95rem; font-weight: 700; color: var(--color-dark);">Authentic Materials</div>'
)
main_code = main_code.replace(
    '<h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">45-Day Handover</h4>\n            <p style="font-size: 0.9rem; color: var(--color-muted); line-height: 1.6;">Time is sacred. When we commit to 45 days, our milestone calendars ensure your home is ready on that exact date.</p>',
    '<h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Structured Timelines</h4>\n            <p style="font-size: 0.9rem; color: var(--color-muted); line-height: 1.6;">Time is sacred. Our milestone schedules and proactive project management ensure steady progress toward your planned move-in date.</p>'
)
main_code = main_code.replace(
    '<h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">10-Year Warranty</h4>\n            <p style="font-size: 0.9rem; color: var(--color-muted); line-height: 1.6;">Our relationship does not end at handover. With our 10-year written warranty, our service team is just a phone call away.</p>',
    '<h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Enduring Durability</h4>\n            <p style="font-size: 0.9rem; color: var(--color-muted); line-height: 1.6;">Our relationship does not end at handover. With our dedicated after-sales care, our service team is always just a phone call away.</p>'
)

# Contact Page
main_code = main_code.replace(
    '✦ Quick Response Guaranteed Within 24 Hours',
    '✦ Prompt Response Within 24 Hours'
)
main_code = main_code.replace(
    'Zero spam guarantee.',
    'Zero spam.'
)

# Terms of Service Page
main_code = main_code.replace(
    "title='Terms of Service & Warranty Terms | Delhi Interior'",
    "title='Terms of Service & Studio Policies | Delhi Interior'"
)
main_code = main_code.replace(
    "desc='Terms of service and 10-year warranty policy for Delhi Interior.'",
    "desc='Terms of service and craftsmanship policies for Delhi Interior.'"
)
main_code = main_code.replace(
    '<h2>3. 10-Year Comprehensive Warranty Policy</h2>\n      <p>Delhi Interior provides a 10-year structural warranty on all factory-manufactured carpentry (carcasses, shutters, and internal framework). This covers delamination, structural warping under normal environmental conditions, and termite damage on certified BWP marine plywood.</p>\n      <p><em>Exclusions:</em> The warranty does not cover damages caused by external seepage originating from third-party building plumbing, natural disasters, deliberate vandalism, or unauthorized alterations by third-party carpenters.</p>',
    '<h2>3. Quality Standards &amp; Material Specifications Policy</h2>\n      <p>Delhi Interior builds exclusively with genuine, certified materials including IS:710 boiling waterproof marine plywood, Action TESA HDMR boards, and authentic hardware from Blum, Hettich, and Hafele. Manufacturer test certificates and authenticity QR codes are provided upon handover.</p>\n      <p><em>Maintenance:</em> To preserve finish longevity, clients receive clear care guidelines covering moisture protection, hinge lubrication, and surface cleaning protocols.</p>'
)
main_code = main_code.replace(
    '<h2>4. 45-Day Delivery Timeline Guarantee</h2>\n      <p>We commit to written timelines (typically 45 days for modular setups and 60–75 days for full home turnkeys) starting from the date of final design approval, site clearance, and initial mobilization advance payment.</p>',
    '<h2>4. Project Timelines &amp; Stage Milestones</h2>\n      <p>We operate on agreed project schedules structured around clear stage milestones (civil preparation, workshop fabrication, on-site joinery, and finishing). Timelines commence upon final architectural drawing sign-off and site readiness.</p>'
)
main_code = main_code.replace(
    'For any contractual or warranty queries',
    'For any contractual or service queries'
)

with open('scripts/build_main_and_utility.py', 'w', encoding='utf-8') as f:
    f.write(main_code)
print("Updated build_main_and_utility.py successfully.")

# -----------------------------------------------------------------------------
# 3. UPDATE scripts/build_services.py & scripts/update_build_services.py
# -----------------------------------------------------------------------------
with open('scripts/build_services.py', 'r', encoding='utf-8') as f:
    serv_code = f.read()

serv_code = serv_code.replace(
    '45-day delivery guarantee.',
    'Structured milestone delivery.'
)
serv_code = serv_code.replace(
    '45–60 day delivery with written penalty commitments.',
    'Structured milestone delivery with direct workshop execution.'
)
serv_code = serv_code.replace(
    "('What warranty do you provide on turnkey work?', '1-year comprehensive warranty on civil, electrical, and plumbing works, plus manufacturer warranties on materials.')",
    "('How do you support clients after turnkey handover?', 'We provide dedicated post-handover support for civil, electrical, and plumbing checks, alongside original manufacturer documentation for all certified hardware and materials.')"
)
serv_code = serv_code.replace(
    "('Will all wires behind the TV unit truly be hidden?', 'Guaranteed. We install concealed PVC conduits inside the wall or backing box so no power cords or HDMI cables ever dangle.')",
    "('Will all wires behind the TV unit truly be hidden?', 'Yes, completely. We install concealed PVC conduits inside the wall or backing box so no power cords or HDMI cables ever dangle.')"
)
serv_code = serv_code.replace(
    "'overview_h2': 'Architectural Ceilings with Zero Sagging Guarantee.'",
    "'overview_h2': 'Architectural False Ceilings with Heavy-Duty G.I. Framing.'"
)
serv_code = serv_code.replace(
    "('How do you guarantee that newly tiled bathrooms will never leak into ceilings below?', 'We apply a double-layer chemical waterproofing membrane (Fosroc Brushbond) over base concrete, followed by a mandatory 48-hour standing water pond test before tile laying.')",
    "('How do you ensure that newly tiled bathrooms will not leak into ceilings below?', 'We apply a double-layer chemical waterproofing membrane (Fosroc Brushbond) over base concrete, followed by a mandatory 48-hour standing water pond test before tile laying.')"
)

with open('scripts/build_services.py', 'w', encoding='utf-8') as f:
    f.write(serv_code)
print("Updated build_services.py successfully.")

with open('scripts/update_build_services.py', 'r', encoding='utf-8') as f:
    up_serv_code = f.read()

up_serv_code = up_serv_code.replace(
    'genuine materials, German hardware, and a 10-year warranty.',
    'genuine materials, authentic German hardware, and lasting craftsmanship.'
)
up_serv_code = up_serv_code.replace(
    'Everything you need to know about materials, timelines, warranties, and payment terms.',
    'Everything you need to know about materials, timelines, craftsmanship standards, and payment terms.'
)

with open('scripts/update_build_services.py', 'w', encoding='utf-8') as f:
    f.write(up_serv_code)
print("Updated update_build_services.py successfully.")

# -----------------------------------------------------------------------------
# 4. UPDATE scripts/build_blog.py
# -----------------------------------------------------------------------------
with open('scripts/build_blog.py', 'r', encoding='utf-8') as f:
    blog_code = f.read()

blog_code = blog_code.replace(
    'and a 5-year studio warranty.',
    'and authentic manufacturer hardware.'
)
blog_code = blog_code.replace(
    'What specific written warranty do you provide on carpentry, civil, and hardware',
    'What specific quality assurances and material certificates do you provide'
)
blog_code = blog_code.replace(
    'and a binding price-lock guarantee.',
    'and a transparent itemized Bill of Quantities (BOQ).'
)
blog_code = blog_code.replace(
    'guaranteeing accountability, quality control, and on-time completion.',
    'ensuring accountability, quality control, and milestone completion.'
)

with open('scripts/build_blog.py', 'w', encoding='utf-8') as f:
    f.write(blog_code)
print("Updated build_blog.py successfully.")
