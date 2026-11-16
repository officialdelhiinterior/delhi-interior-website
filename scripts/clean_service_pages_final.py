import glob

service_files = [
    'bedroom-furniture-delhi/index.html',
    'doors-partitions-delhi/index.html',
    'false-ceiling-delhi/index.html',
    'full-home-interior-delhi/index.html',
    'modular-kitchen-delhi/index.html',
    'painting-polishing-delhi/index.html',
    'plumbing-electrical-delhi/index.html',
    'wall-paneling-delhi/index.html',
    'wardrobe-design-delhi/index.html',
    'scripts/build_services.py'
]

replacements = [
    (
        "Factory-engineered offsite, assembled on-site with zero dust and laser precision.",
        "Crafted in our South Delhi workshop, assembled on-site with clean joinery and lasting precision."
    ),
    (
        "Factory cut carcass, zero-dust edge banding, and flawless on-site assembly.",
        "Precision workshop-cut carcass, clean edge sealing, and flawless on-site assembly."
    ),
    (
        "In-House Factory Build",
        "In-House Workshop Crafting"
    ),
    (
        "Factory Build & Handover",
        "Workshop Crafting & Handover"
    ),
    (
        "Factory Build &amp; Handover",
        "Workshop Crafting &amp; Handover"
    ),
    (
        "Factory precision cutting, edge-banding",
        "Precision workshop fabrication, edge sealing"
    ),
    (
        "Factory precision cutting",
        "Precision workshop fabrication"
    )
]

for f in service_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    modified = c
    for o, n in replacements:
        if o in modified:
            modified = modified.replace(o, n)
    
    if modified != c:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(modified)
        print(f"[UPDATED] {f}")

print("Done updating service files!")
