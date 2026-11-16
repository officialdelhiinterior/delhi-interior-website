import re

# 1. CLEAN scripts/build_services.py
with open('scripts/build_services.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace all occurrences of warranties/guarantees/45-day in package features and descriptions
replacements = [
    # Meta / descs
    (r"5yr warranty\. Call now\.", "Master craftsmanship. Call now."),
    (r"5-yr warranty\. Free design consultation\.", "Master craftsmanship. Free design consultation."),
    (r"5-yr warranty\.", "Master craftsmanship."),
    (r"10-yr warranty\.", "Master craftsmanship."),
    (r"5-yr warranty\. Call now\.", "Master craftsmanship. Call now."),
    (r"45-day delivery guarantee\.", "Structured milestone delivery."),
    (r"45–60 day delivery with written penalty commitments\.", "Structured milestone delivery with direct workshop execution."),
    (r"45–60 day delivery with written guarantees and zero surprise bills\.", "Structured milestone delivery with transparent itemized BOQ."),
    (r"to guarantee zero sagging, cracking, or surface blemishes", "to ensure zero sagging, cracking, or surface blemishes"),

    # Packages features
    (r"'1-Year Warranty'", "'Quality Audit & Handover'"),
    (r"'Profile Lighting & 5-Year Warranty'", "'Profile Lighting & Concealed Channels'"),
    (r"'Comprehensive 5-Year Studio Warranty'", "'Comprehensive Quality Assurance'"),
    (r"'5-Year Warranty'", "'Precision Joinery & Care Guide'"),
    (r"'5-Year Studio Warranty'", "'Master Craftsman Detailing'"),
    (r"'Concealed LED Channels & 5-Yr Warranty'", "'Concealed LED Channels & Millwork'"),
    (r"'Studio 5-Year Craftsmanship Guarantee'", "'Master Craftsman Detailing'"),
    (r"'5-Year Structural Warranty'", "'Reinforced Structural Joinery'"),
    (r"'Studio 5-Year Guarantee'", "'Bespoke Studio Detailing'"),
    (r"'45-Day Timeline & 5-Yr Warranty'", "'Milestone Schedule & Handover'"),
    (r"'60-Day Timeline & 5-Yr Warranty'", "'Milestone Schedule & Handover'"),
    (r"'5-Year Hardware Warranty'", "'Certified International Hardware'"),
    (r"'3-Year Warranty'", "'High-Durability Finish'"),
    (r"'5-Year Leak-Proof Warranty'", "'Hydro-Static Pressure Tested'"),

    # FAQs
    (r"all backed by official manufacturer warranties\.", "all installed to authentic manufacturer specifications."),
    (r"'Guaranteed\. We install concealed PVC conduits", "'Yes, completely. We install concealed PVC conduits"),
    (r"'What warranty do you provide on turnkey work\?'", "'What quality assurances do you provide on turnkey work?'"),
    (r"'1-year comprehensive warranty on civil, electrical, and plumbing fittings, and a 5-year structural warranty on all carpentry and hardware\.'",
     "'We conduct detailed multi-point quality audits across all civil, electrical, plumbing, and carpentry installations before handover, accompanied by original manufacturer documentation for certified hardware and materials.'"),
    (r"'How do you guarantee that newly tiled bathrooms will never leak into ceilings below\?'",
     "'How do you ensure that newly tiled bathrooms will not leak into ceilings below?'")
]

for pattern, repl in replacements:
    text = re.sub(pattern, repl, text)

with open('scripts/build_services.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Cleaned scripts/build_services.py")

# 2. CLEAN scripts/build_blog.py
with open('scripts/build_blog.py', 'r', encoding='utf-8') as f:
    btext = f.read()

btext = btext.replace("and a 5-year studio warranty.", "and authentic manufacturer hardware.")
btext = btext.replace("What specific written warranty do you provide on carpentry, civil, and hardware", "What specific quality assurances and material certificates do you provide")
btext = btext.replace("and a binding price-lock guarantee.", "and a transparent itemized Bill of Quantities (BOQ).")
btext = btext.replace("guaranteeing accountability", "ensuring accountability")
btext = btext.replace("backed by a 10-year warranty", "crafted by master artisans")

with open('scripts/build_blog.py', 'w', encoding='utf-8') as f:
    f.write(btext)
print("Cleaned scripts/build_blog.py")
