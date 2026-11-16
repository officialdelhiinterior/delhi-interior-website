"""
Clean up remaining industrial/factory claims across service pages and process/index.html.
"""

import os
import glob

replacements = [
    (
        "All cabinetry and modular carcasses are handcrafted in our dedicated South Delhi carpentry workshop by our master karigars using precision joinery and calibrated BWP materials. Simultaneously, civil, plumbing, electrical, and false ceiling works proceed seamlessly on-site.",
        "All cabinetry and modular carcasses are handcrafted in our dedicated South Delhi carpentry workshop by our master karigars using precision joinery and calibrated BWP materials. Simultaneously, civil, plumbing, electrical, and false ceiling works proceed seamlessly on-site."
    ),
    (
        "Handcrafted in our South Delhi workshop, assembled on-site with clean joinery and lasting precision.",
        "Handcrafted in our South Delhi workshop, assembled on-site with clean joinery and lasting precision."
    ),
    (
        "Workshop-crafted carcass, clean edge sealing, and flawless on-site assembly.",
        "Workshop-crafted carcass, clean edge sealing, and flawless on-site assembly."
    ),
    (
        "We source directly from authorized distributors of CenturyPly and Greenpanel.",
        "We source directly from authorized distributors of CenturyPly and Greenpanel."
    ),
    (
        "<!-- Workshop & Studio Section -->",
        "<!-- Workshop & Studio Section -->"
    ),
    (
        "Clean Workshop Pre-Fitting",
        "Clean Workshop Pre-Fitting"
    ),
]

all_files = glob.glob('**/*.html', recursive=True) + glob.glob('scripts/**/*.py', recursive=True)

count = 0
for f in all_files:
    if not os.path.isfile(f) or 'k2_raw.html' in f or 'blubloom_raw.html' in f:
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    modified = c
    for old_s, new_s in replacements:
        if old_s in modified:
            modified = modified.replace(old_s, new_s)
            count += 1
    
    if modified != c:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(modified)
        print(f"[CLEANED] {f}")

print(f"Total replacements made: {count}")
