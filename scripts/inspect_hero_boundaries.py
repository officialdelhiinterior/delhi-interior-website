import re

with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    content = f.read()

hero_start_idx = content.find('<section class="hero-section"')
trust_strip_idx = content.find('<!-- 2. TRUST METRIC STRIP')

print(f"Hero section indices: {hero_start_idx} to {trust_strip_idx}")
old_hero = content[hero_start_idx:trust_strip_idx]
print(f"Current hero length: {len(old_hero)}")
print("First 300 chars of hero:\n", old_hero[:300])
print("Last 300 chars of hero:\n", old_hero[-300:])
