import re

# 1. Update rebuild_complete_site_v3.py
with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace(
    '10+ years experience, 500+ homes delivered, 45-day guaranteed handover, 10-year warranty.',
    '10+ years experience, 500+ homes delivered, direct workshop rates, and turnkey master craftsmanship.'
)
code = code.replace('hero-badge-warranty', 'hero-badge-quality')

with open('scripts/rebuild_complete_site_v3.py', 'w', encoding='utf-8') as f:
    f.write(code)
print("Cleaned rebuild_complete_site_v3.py")

# 2. Update build_main_and_utility.py
with open('scripts/build_main_and_utility.py', 'r', encoding='utf-8') as f:
    mcode = f.read()

mcode = mcode.replace(
    "desc='Learn how Delhi Interior delivers turnkey homes in 45 days with 10-year warranty, photorealistic 3D designs, fixed price guarantee, and 146 quality checks.'",
    "desc='Learn how Delhi Interior delivers turnkey homes with transparent milestone schedules, photorealistic 3D designs, itemized pricing, and 146 quality checks.'"
)
mcode = mcode.replace(
    'From laser room scans to 45-day zero-defect key handover, discover how we build homes worth living in.',
    'From laser room scans to milestone-based zero-defect key handover, discover how we build homes worth living in.'
)
mcode = mcode.replace(
    'Stage 5 · Days 41–45',
    'Stage 5 · Final Handover'
)
mcode = mcode.replace(
    'We deliver on time with our 10-year written warranty.',
    'We complete a thorough handover accompanied by original material documentation.'
)
mcode = mcode.replace(
    "desc='Learn about Delhi Interior — our founding story, in-house modular workshop, 10-year warranty, and philosophy of creating spaces designed to delight every day.'",
    "desc='Learn about Delhi Interior — our founding story, in-house modular workshop, master craftsmen, and philosophy of creating spaces designed to delight every day.'"
)
mcode = mcode.replace(
    "desc='Review the official terms of service, payment milestones, scope of work, and 10-year warranty policy of Delhi Interior design studio.'",
    "desc='Review the official terms of service, payment milestones, scope of work, and craftsmanship policies of Delhi Interior design studio.'"
)
mcode = mcode.replace(
    'We guarantee fixed pricing with zero hidden surcharges.',
    'We commit to transparent, itemized pricing with zero hidden surcharges.'
)
mcode = mcode.replace(
    '<h2>3. 10-Year Comprehensive Warranty Policy</h2>\n        <p>Delhi Interior provides a 10-year structural warranty on all factory-manufactured carpentry (carcasses, shutters, edge-banding) and hardware channels against manufacturing defects. Hardware accessories (Hettich, Ebco, Blum) carry their respective official manufacturer warranties. A 1-year comprehensive warranty covers civil tiling, electrical joints, and plumbing connections.</p>\n        <p><em>Exclusions:</em> The warranty does not cover damages caused by external seepage originating from third-party flats above, physical abuse, fire, or intentional impact.</p>',
    '<h2>3. Quality Standards &amp; Material Specifications Policy</h2>\n        <p>Delhi Interior builds exclusively with genuine, certified materials including IS:710 boiling waterproof marine plywood, Action TESA HDMR boards, and authentic hardware from Blum, Hettich, and Hafele. Manufacturer test certificates and authenticity records are provided upon handover.</p>\n        <p><em>Care Guidelines:</em> To preserve finish longevity, clients receive clear maintenance guidelines covering moisture protection, hardware care, and surface cleaning protocols.</p>'
)
mcode = mcode.replace(
    '<h2>4. 45-Day Delivery Timeline Guarantee</h2>\n        <p>We commit to written timelines (typically 45 days for modular setups and 60–75 days for full home turnkeys). Timelines commence after 3D design sign-off and site readiness. In the unlikely event of studio-caused delays, compensation terms outlined in the client contract apply.</p>',
    '<h2>4. Project Timelines &amp; Stage Milestones</h2>\n        <p>We operate on agreed project schedules structured around clear stage milestones (civil preparation, workshop fabrication, on-site joinery, and finishing). Timelines commence after architectural drawing sign-off and site readiness.</p>'
)

with open('scripts/build_main_and_utility.py', 'w', encoding='utf-8') as f:
    f.write(mcode)
print("Cleaned build_main_and_utility.py")

# 3. Update build_services.py
with open('scripts/build_services.py', 'r', encoding='utf-8') as f:
    scode = f.read()

scode = scode.replace("'5-Year Studio Guarantee'", "'Italian PU Buff & Inspection'")

with open('scripts/build_services.py', 'w', encoding='utf-8') as f:
    f.write(scode)
print("Cleaned build_services.py")
