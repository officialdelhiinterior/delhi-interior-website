import re

with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Remove <span class="logo-dot">.</span> and ?<span class="logo-dot">.</span>
code = code.replace('?<span class="logo-dot">.</span>', '?')
code = code.replace('<span class="logo-dot">.</span>', '')

# 2. Clean up mobile menu drawer: Remove emojis from navigation and services
emoji_replacements = [
    ('🏠 Home', 'Home'),
    ('ℹ️ About Our Studio', 'About Our Studio'),
    ('🖼️ Projects &amp; Portfolio', 'Projects &amp; Portfolio'),
    ('⚡ How It Works (45 Days)', 'How It Works (45 Days)'),
    ('📝 Blogs &amp; Design Guides', 'Blogs &amp; Design Guides'),
    ('📍 Contact Us', 'Contact Us'),
    ('🏡 Residential Interiors', 'Residential Interiors (2/3/4 BHK)'),
    ('🍳 Modular Kitchens', 'Modular Kitchens'),
    ('🚪 Custom Wardrobes', 'Custom Wardrobes'),
    ('📺 Wall Paneling &amp; Louvers', 'Wall Paneling &amp; Louvers'),
    ('💡 False Ceiling &amp; Lights', 'False Ceiling &amp; Lighting'),
    ('🏛️ Doors &amp; Partitions', 'Doors &amp; Partitions'),
    ('🪵 Custom Woodwork &amp; Carpentry', 'Custom Woodwork &amp; Carpentry'),
    ('🎨 Painting &amp; PU Polish', 'Painting &amp; PU Polish'),
    ('⚡ Plumbing &amp; Electrical MEP', 'Plumbing &amp; Electrical MEP')
]
for old_e, new_e in emoji_replacements:
    code = code.replace(old_e, new_e)

# 3. Replace emojis in Section 2.5 (The Craftsman Difference) with clean vector SVG icons
old_advantage_block = '''          <div style="background: #F9FAFB; border: 1.5px solid #E5E7EB; border-radius: var(--radius-lg); padding: 2.2rem 1.8rem; box-shadow: var(--shadow-sm);">
            <div style="width: 48px; height: 48px; border-radius: 12px; background: #EFF6FF; color: #2563EB; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; font-weight: 800; margin-bottom: 1.2rem;">🪵</div>
            <h3 style="font-size: 1.25rem; font-weight: 700; color: var(--color-dark); margin-bottom: 0.6rem;">Direct Workshop &amp; Carpenter Rates</h3>
            <p style="font-size: 0.92rem; color: #4B5563; line-height: 1.7; margin-bottom: 1rem;">Aggregator brands charge 35% to 50% extra for corporate marketing and sales agents. Because we manufacture and fabricate at our own Mohammadpur workshop, you save significantly on genuine CenturyPly BWP marine ply and Action TESA HDMR.</p>
            <span style="font-size: 0.82rem; font-weight: 700; color: #16A34A;">✓ Save 30% to 40% vs Aggregators</span>
          </div>

          <div style="background: #F9FAFB; border: 1.5px solid #E5E7EB; border-radius: var(--radius-lg); padding: 2.2rem 1.8rem; box-shadow: var(--shadow-sm);">
            <div style="width: 48px; height: 48px; border-radius: 12px; background: #ECFDF5; color: #10B981; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; font-weight: 800; margin-bottom: 1.2rem;">📐</div>
            <h3 style="font-size: 1.25rem; font-weight: 700; color: var(--color-dark); margin-bottom: 0.6rem;">Master Carpentry &amp; Millimeter Precision</h3>
            <p style="font-size: 0.92rem; color: #4B5563; line-height: 1.7; margin-bottom: 1rem;">We do not subcontract your home to third-party laborers. Our in-house master carpenters (karigars) custom-craft solid Burma Teak mandirs, sliding almirahs, storage beds, and TV louvers built to fit your room's exact dimensions.</p>
            <span style="font-size: 0.82rem; font-weight: 700; color: #2563EB;">✓ 10+ Years Woodworking Expertise</span>
          </div>

          <div style="background: #F9FAFB; border: 1.5px solid #E5E7EB; border-radius: var(--radius-lg); padding: 2.2rem 1.8rem; box-shadow: var(--shadow-sm);">
            <div style="width: 48px; height: 48px; border-radius: 12px; background: #FEF3C7; color: #D97706; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; font-weight: 800; margin-bottom: 1.2rem;">⚡</div>
            <h3 style="font-size: 1.25rem; font-weight: 700; color: var(--color-dark); margin-bottom: 0.6rem;">Complete Turnkey Under One Roof</h3>
            <p style="font-size: 0.92rem; color: #4B5563; line-height: 1.7; margin-bottom: 1rem;">Say goodbye to the nightmare of managing separate painters, electricians, plumbers, and carpenters. We handle civil masonry, false ceilings, Asian Paints Royale, Italian PU polish, and electrical MEP with one single accountable contact.</p>
            <span style="font-size: 0.82rem; font-weight: 700; color: #D97706;">✓ Single Point Accountability</span>
          </div>'''

new_advantage_block = '''          <div class="craftsman-card">
            <div class="craftsman-card-icon">
              <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
            </div>
            <h3>Direct Workshop &amp; Carpenter Rates</h3>
            <p>Aggregator brands charge 35% to 50% extra for corporate marketing and sales agents. Because we manufacture and fabricate at our own Mohammadpur workshop, you save significantly on genuine CenturyPly BWP marine ply and Action TESA HDMR.</p>
            <span class="craftsman-tag tag-green">✓ Save 30% to 40% vs Aggregators</span>
          </div>

          <div class="craftsman-card">
            <div class="craftsman-card-icon">
              <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21.3 15.3l-6.6-6.6a2 2 0 0 0-2.8 0L2.7 17.9a1 1 0 0 0 0 1.4l2 2a1 1 0 0 0 1.4 0l9.2-9.2 1.4 1.4a1 1 0 0 0 1.4 0l3.2-3.2z"/><path d="M14 6l4 4"/><circle cx="5" cy="19" r="1"/></svg>
            </div>
            <h3>Master Carpentry &amp; Millimeter Precision</h3>
            <p>We do not subcontract your home to third-party laborers. Our in-house master carpenters (karigars) custom-craft solid Burma Teak mandirs, sliding almirahs, storage beds, and TV louvers built to fit your room's exact dimensions.</p>
            <span class="craftsman-tag tag-blue">✓ 10+ Years Woodworking Expertise</span>
          </div>

          <div class="craftsman-card">
            <div class="craftsman-card-icon">
              <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </div>
            <h3>Complete Turnkey Under One Roof</h3>
            <p>Say goodbye to the nightmare of managing separate painters, electricians, plumbers, and carpenters. We handle civil masonry, false ceilings, Asian Paints Royale, Italian PU polish, and electrical MEP with one single accountable contact.</p>
            <span class="craftsman-tag tag-amber">✓ Single Point Accountability</span>
          </div>'''

code = code.replace(old_advantage_block, new_advantage_block)

with open('scripts/rebuild_complete_site_v3.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Applied refined markup to scripts/rebuild_complete_site_v3.py")
