"""
Systematically purge and replace all false, exaggerated claims like "10,000 sq. ft. factory",
"automated plant", "40+ carpenters", etc., replacing them with authentic representations
of Delhi Interior's dedicated in-house woodworking workshop in Mohammadpur, South Delhi.
"""

import os
import glob
import re

replacements = [
    # 10,000 sq ft & facility claims
    (
        "We operate our own dedicated in-house carpentry workshop in Mohammadpur, South Delhi. While on-site civil and electrical conduit preparation is underway, all your kitchen cabinets, wardrobe carcasses, and paneling are handcrafted and pre-assembled in our workshop to ensure minimal dust and disturbance at your home.",
        "We operate our own dedicated in-house carpentry workshop in Mohammadpur, South Delhi. While on-site civil and electrical conduit preparation is underway, all your kitchen cabinets, wardrobe carcasses, and paneling are handcrafted and pre-assembled in our workshop to ensure minimal dust and disturbance at your home."
    ),
    (
        "We operate our own dedicated in-house carpentry workshop in Mohammadpur, South Delhi.",
        "We operate our own dedicated in-house carpentry workshop in Mohammadpur, South Delhi."
    ),
    (
        "We operate our own dedicated in-house carpentry workshop in Mohammadpur, South Delhi, giving us complete, hands-on control over timber quality, joinery precision, and finish excellence.",
        "We operate our own dedicated in-house carpentry workshop in Mohammadpur, South Delhi, giving us complete, hands-on control over timber quality, joinery precision, and finish excellence."
    ),
    (
        "Our Dedicated Woodworking Workshop in South Delhi",
        "Our Dedicated Woodworking Workshop in South Delhi"
    ),
    (
        "where quality corners are cut, we operate our own dedicated in-house woodworking and furniture workshop in Mohammadpur, South Delhi.",
        "where quality corners are cut, we operate our own dedicated in-house woodworking and furniture workshop in Mohammadpur, South Delhi."
    ),
    (
        "our in-house master carpenters (karigars) operate from our dedicated South Delhi carpentry workshop, crafting bespoke woodwork",
        "our in-house master carpenters (karigars) operate from our dedicated South Delhi carpentry workshop, crafting bespoke woodwork"
    ),
    (
        "our in-house master carpenters",
        "our in-house master carpenters"
    ),
    (
        "Delhi Interior Dedicated Carpentry Workshop in South Delhi",
        "Delhi Interior Dedicated Carpentry Workshop in South Delhi"
    ),
    (
        "Delhi Interior Dedicated Woodworking Workshop in South Delhi",
        "Delhi Interior Dedicated Woodworking Workshop in South Delhi"
    ),
    (
        "Certified BWP Marine Ply &amp; German Fittings",
        "Certified BWP Marine Ply &amp; German Fittings"
    ),
    (
        "Certified BWP Marine Ply & German Fittings",
        "Certified BWP Marine Ply & German Fittings"
    ),
    (
        "direct workshop rates",
        "direct workshop rates"
    ),
    (
        "Direct Workshop Rates",
        "Direct Workshop Rates"
    ),
    # Process page claims
    (
        "Workshop Crafting &amp; Turnkey Assembly",
        "Workshop Crafting &amp; Turnkey Assembly"
    ),
    (
        "Workshop Crafting & Turnkey Assembly",
        "Workshop Crafting & Turnkey Assembly"
    ),
    (
        "All modular carcasses and bespoke woodwork are crafted in our dedicated South Delhi workshop by our master karigars using precision joinery and certified materials.",
        "All modular carcasses and bespoke woodwork are crafted in our dedicated South Delhi workshop by our master karigars using precision joinery and certified materials."
    ),
    (
        "Clean workshop fabrication with certified BWP grade materials",
        "Clean workshop fabrication with certified BWP grade materials"
    ),
    (
        "Clean Workshop Pre-Fitting & On-Site Assembly by Master Carpenters",
        "Clean Workshop Pre-Fitting & On-Site Assembly by Master Carpenters"
    ),
    (
        "In-House Workshop Crafting",
        "In-House Workshop Crafting"
    ),
    (
        "Workshop Crafting & Assembly",
        "Workshop Crafting & Assembly"
    ),
    (
        "Workshop Crafting &amp; Assembly",
        "Workshop Crafting &amp; Assembly"
    ),
    (
        "Precision workshop fabrication, edge sealing, and seamless on-site assembly.",
        "Precision workshop fabrication, edge sealing, and seamless on-site assembly."
    ),
    (
        "Precision workshop fabrication, edge sealing",
        "Precision workshop fabrication, edge sealing"
    ),
    (
        "Crafted in our workshop, assembled on-site with clean joinery and lasting precision.",
        "Crafted in our workshop, assembled on-site with clean joinery and lasting precision."
    ),
    (
        "material procurement, and workshop carcass fabrication",
        "material procurement, and workshop carcass fabrication"
    ),
    (
        "workshop production commencement",
        "workshop production commencement"
    ),
    (
        "Fabrication takes approximately 20–25 days in our dedicated workshop.",
        "Fabrication takes approximately 20–25 days in our dedicated workshop."
    ),
]

all_files = glob.glob('**/*.html', recursive=True) + glob.glob('scripts/**/*.py', recursive=True) + ['AI.md', 'CHECKPOINT.md']

total_replacements = 0
for f in all_files:
    if not os.path.isfile(f):
        continue
    # skip raw archives if any
    if 'k2_raw.html' in f or 'blubloom_raw.html' in f:
        continue
    
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    modified = content
    file_changes = 0
    for old_str, new_str in replacements:
        if old_str in modified:
            count = modified.count(old_str)
            modified = modified.replace(old_str, new_str)
            file_changes += count
            total_replacements += count
    
    if file_changes > 0:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(modified)
        print(f"[UPDATED] {f}: {file_changes} replacements")

print(f"\n=======================================================")
print(f"Total false claims removed and replaced: {total_replacements}")
print(f"=======================================================")
