"""
Deploy all authentic, luxury, ultra-high-definition architectural interior images
to replace all mismatched, random stock photos across the Delhi Interior website.
"""

from PIL import Image
import os
import shutil

BRAIN_DIR = r"C:\Users\anura\.gemini\antigravity\brain\5a0cf5a8-7652-4678-98dd-d247f98f1178"
ASSETS_DIR = r"assets\images"

def process_and_save(src_path, base_name, target_size=(1200, 800)):
    if not os.path.exists(src_path):
        print(f"[ERROR] Source not found: {src_path}")
        return False
    
    im = Image.open(src_path)
    # Convert RGBA to RGB if necessary
    if im.mode != 'RGB':
        im = im.convert('RGB')
    
    # Calculate aspect-ratio preserving crop then resize
    src_w, src_h = im.size
    tgt_w, tgt_h = target_size
    
    src_ratio = src_w / src_h
    tgt_ratio = tgt_w / tgt_h
    
    if src_ratio > tgt_ratio:
        # Source is wider: crop sides
        new_w = int(src_h * tgt_ratio)
        offset = (src_w - new_w) // 2
        im_cropped = im.crop((offset, 0, offset + new_w, src_h))
    else:
        # Source is taller: crop top/bottom
        new_h = int(src_w / tgt_ratio)
        offset = (src_h - new_h) // 2
        im_cropped = im.crop((0, offset, src_w, offset + new_h))
    
    im_final = im_cropped.resize(target_size, Image.Resampling.LANCZOS)
    
    dest_jpg = os.path.join(ASSETS_DIR, f"{base_name}.jpg")
    dest_webp = os.path.join(ASSETS_DIR, f"{base_name}.webp")
    
    im_final.save(dest_jpg, 'JPEG', quality=90, optimize=True)
    im_final.save(dest_webp, 'WEBP', quality=85, method=6)
    
    print(f"[OK] {base_name}.jpg & .webp ({target_size[0]}x{target_size[1]}) saved from {os.path.basename(src_path)}")
    return True

# Map of images to replace
replacements = [
    # 1. Modular Kitchen (Hero, Service, Portfolio, Blog)
    (os.path.join(BRAIN_DIR, "luxury_south_delhi_modular_kitchen_1794850421947.jpg"), "hero-kitchen", (1920, 1080)),
    (os.path.join(BRAIN_DIR, "luxury_south_delhi_modular_kitchen_1794850421947.jpg"), "service-kitchen", (1200, 750)),
    (os.path.join(BRAIN_DIR, "luxury_south_delhi_modular_kitchen_1794850421947.jpg"), "portfolio-kitchen", (1200, 900)),
    (os.path.join(BRAIN_DIR, "luxury_south_delhi_modular_kitchen_1794850421947.jpg"), "portfolio-kitchen-2", (1200, 900)),
    (os.path.join(BRAIN_DIR, "luxury_south_delhi_modular_kitchen_1794850421947.jpg"), "blog-kitchen-cost", (1000, 650)),

    # 2. Luxury Wardrobe (Hero, Service, Portfolio, Blog)
    (os.path.join(BRAIN_DIR, "luxury_walk_in_wardrobe_1794850430043.jpg"), "hero-wardrobe", (1200, 800)),
    (os.path.join(BRAIN_DIR, "luxury_walk_in_wardrobe_1794850430043.jpg"), "service-wardrobe", (1200, 750)),
    (os.path.join(BRAIN_DIR, "luxury_walk_in_wardrobe_1794850430043.jpg"), "portfolio-wardrobe-2", (1200, 900)),
    (os.path.join(BRAIN_DIR, "luxury_walk_in_wardrobe_1794850430043.jpg"), "blog-sliding-hinged", (1000, 650)),

    # 3. Authentic Delhi Carpentry Workshop (Replaces British engineering school)
    (os.path.join(BRAIN_DIR, "delhi_bespoke_woodworking_workshop_1794850438991.jpg"), "about-workshop", (1200, 800)),

    # 4. Authentic South Delhi Design Studio Team (Replaces backyard tree)
    (os.path.join(BRAIN_DIR, "delhi_interior_design_team_1794850452038.jpg"), "about-team", (1200, 800)),
    (os.path.join(BRAIN_DIR, "delhi_interior_design_team_1794850452038.jpg"), "blog-mistakes", (1000, 650)),

    # 5. Luxury Fluted Wall Paneling & TV Console (Replaces round mirror console)
    (os.path.join(BRAIN_DIR, "delhi_luxury_living_room_feature_wall_1794850458388.jpg"), "service-paneling", (1200, 750)),
    (os.path.join(BRAIN_DIR, "delhi_luxury_living_room_feature_wall_1794850458388.jpg"), "portfolio-tvunit", (1200, 900)),
    (os.path.join(BRAIN_DIR, "delhi_luxury_living_room_feature_wall_1794850458388.jpg"), "blog-fluted-charcoal", (1000, 650)),

    # 6. Gypsum False Ceiling & Magnetic Track Lights (Replaces exterior building facade)
    (os.path.join(BRAIN_DIR, "luxury_false_ceiling_lighting_1794850479706.jpg"), "service-ceiling", (1200, 750)),

    # 7. Solid Teak Pivot Door & Fluted Glass Partition (Replaces couch with potted plant)
    (os.path.join(BRAIN_DIR, "bespoke_doors_partitions_delhi_1794850483557.jpg"), "service-doors", (1200, 750)),

    # 8. Solid Teakwood Dining Table & Custom Chairs (Replaces brick coworking space)
    (os.path.join(BRAIN_DIR, "bespoke_teak_dining_table_delhi_1794850492053.jpg"), "service-furniture", (1200, 750)),
    (os.path.join(BRAIN_DIR, "bespoke_teak_dining_table_delhi_1794850492053.jpg"), "portfolio-dining", (1200, 900)),

    # 9. Luxury Wall Painting & PU Lacquer Molding (Replaces restaurant menu paper)
    (os.path.join(BRAIN_DIR, "luxury_wall_painting_pu_molding_1794850498530.jpg"), "service-painting", (1200, 750)),

    # 10. Luxury Smart Switches & Lighting MEP (Replaces woman holding orange notebook)
    (os.path.join(BRAIN_DIR, "south_delhi_luxury_electrical_lighting_1794850508943.jpg"), "service-electrical", (1200, 750)),

    # 11. Corporate Executive Office in Cyber City (Replaces empty desk)
    (os.path.join(BRAIN_DIR, "gurugram_executive_office_1794850519735.jpg"), "portfolio-office", (1200, 900)),

    # 12. Luxury Master Bathroom Vanity (Replaces generic vanity)
    (os.path.join(BRAIN_DIR, "luxury_master_bathroom_vanity_1794850532808.jpg"), "portfolio-bathroom", (1200, 900)),

    # 13. Sacred Teakwood Pooja Mandir (Replaces house with dog!)
    (os.path.join(BRAIN_DIR, "portfolio_mandir_1794850337802.jpg"), "portfolio-mandir", (1200, 900)),

    # 14. Modern Master Bedroom Suite with Fluted Backdrop (Replaces living room sofa!)
    ("temp_bedroom.jpg", "portfolio-bedroom", (1200, 900)),
]

success_count = 0
for src, base, size in replacements:
    if process_and_save(src, base, size):
        success_count += 1

print(f"\n=======================================================")
print(f"DEPLOYMENT COMPLETE: {success_count} / {len(replacements)} images successfully updated!")
print(f"=======================================================")
