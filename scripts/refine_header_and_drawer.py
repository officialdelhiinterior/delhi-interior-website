import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Clean Top Utility Bar timing, call, and whatsapp emojis
    code = re.sub(
        r'<span>🕒 Timing:\s*Open 24 Hours \(7 Days a Week\)</span>',
        r'<span class="utility-timing"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> Open 24 Hours (7 Days a Week)</span>',
        code
    )
    code = re.sub(
        r'<span>📞 Call 24/7:\s*\+91 96438 17099</span>',
        r'<span class="utility-call"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> Call 24/7: +91 96438 17099</span>',
        code
    )
    code = re.sub(
        r'<span>💬 WhatsApp Designer</span>',
        r'<span class="utility-wa"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg> WhatsApp Designer</span>',
        code
    )

    # 2. Clean Mobile Menu Drawer emojis
    emoji_replacements = [
        ('>🏠 Home<', '>Home<'),
        ('>ℹ️ About Our Studio<', '>About Our Studio<'),
        ('>🖼️ Projects &amp; Portfolio<', '>Projects &amp; Portfolio<'),
        ('>⚡ How It Works (45 Days)<', '>How It Works (45 Days)<'),
        ('>📝 Blogs &amp; Design Guides<', '>Blogs &amp; Design Guides<'),
        ('>📍 Contact Us<', '>Contact Us<'),
        ('>🏡 Residential Interiors<', '>Residential Interiors (2/3/4 BHK)<'),
        ('>🍳 Modular Kitchens<', '>Modular Kitchens<'),
        ('>🚪 Custom Wardrobes<', '>Custom Wardrobes<'),
        ('>📺 Wall Paneling &amp; Louvers<', '>Wall Paneling &amp; Louvers<'),
        ('>💡 False Ceiling &amp; Lights<', '>False Ceiling &amp; Lighting<'),
        ('>🏛️ Doors &amp; Partitions<', '>Doors &amp; Partitions<'),
        ('>🪵 Custom Woodwork &amp; Carpentry<', '>Custom Woodwork &amp; Carpentry<'),
        ('>🎨 Painting &amp; PU Polish<', '>Painting &amp; PU Polish<'),
        ('>⚡ Plumbing &amp; Electrical MEP<', '>Plumbing &amp; Electrical MEP<'),
        ('>📞 Call +91 96438 17099<', '>Call +91 96438 17099<'),
        ('>💬 WhatsApp +91 96438 17099<', '>WhatsApp +91 96438 17099<')
    ]
    for old_val, new_val in emoji_replacements:
        code = code.replace(old_val, new_val)

    # 3. Clean Four Pillars in About page (build_main_and_utility.py)
    code = code.replace(
        '<div style="font-size: 2.2rem; margin-bottom: 1rem;">🪵</div>',
        '<div class="pillar-icon-box"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg></div>'
    )
    code = code.replace(
        '<div style="font-size: 2.2rem; margin-bottom: 1rem;">📐</div>',
        '<div class="pillar-icon-box"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21.3 15.3l-6.6-6.6a2 2 0 0 0-2.8 0L2.7 17.9a1 1 0 0 0 0 1.4l2 2a1 1 0 0 0 1.4 0l9.2-9.2 1.4 1.4a1 1 0 0 0 1.4 0l3.2-3.2z"/><path d="M14 6l4 4"/><circle cx="5" cy="19" r="1"/></svg></div>'
    )
    code = code.replace(
        '<div style="font-size: 2.2rem; margin-bottom: 1rem;">📅</div>',
        '<div class="pillar-icon-box"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>'
    )
    code = code.replace(
        '<div style="font-size: 2.2rem; margin-bottom: 1rem;">🛡️</div>',
        '<div class="pillar-icon-box"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>'
    )
    code = code.replace(
        '🔒 Zero spam. Your details remain 100% confidential.',
        'Zero spam guarantee. Your details remain 100% confidential.'
    )
    code = code.replace(
        '🔒 Direct Craftsman Guarantee · Zero Spam · 100% Free Site Visit in Delhi NCR',
        'Direct Craftsman Guarantee · Zero Spam · 100% Free Site Visit in Delhi NCR'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Refined {filepath}")

update_file('scripts/rebuild_complete_site_v3.py')
update_file('scripts/build_main_and_utility.py')
