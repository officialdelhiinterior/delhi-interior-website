import re

def build_complete_blubloom_system():
    with open('scripts/full_55k_master_style.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the raw CSS string from the python script
    # It starts after css = '''/* and ends before '''
    m = re.search(r'css\s*=\s*[\x22\x27]{3}(.*?)[\x22\x27]{3}', content, re.DOTALL)
    if not m:
        print("Error: Could not extract css from scripts/full_55k_master_style.py")
        return
    css = m.group(1)

    # 1. Update :root variables
    old_root_pattern = r':root\s*\{[^}]+\}'
    new_root = ''':root {
  /* Brand Primary: Deep Dark Navy Blue (Anchored by Official Brand Identity) */
  --color-primary: #0B2540;          /* Deep Dark Navy Blue */
  --color-primary-hover: #16365C;    /* Rich Luminous Navy */
  --color-primary-subtle: #F0F4F8;   /* Subtle Navy Mist */
  --color-primary-border: #CBD5E1;   /* Slate Hairline Divider */

  /* Brand Accent: Warm Architectural Golden Brass / Sand */
  --color-accent: #B89058;           /* Warm Architectural Golden Brass */
  --color-accent-hover: #9E7A42;     /* Burnished Antique Gold */
  --color-accent-subtle: #FDFBF7;    /* Delicate Warm Ivory Glow */
  --color-accent-border: #E8D8BA;    /* Soft Brass Border */
  --color-gold: #B89058;

  /* WhatsApp Green: STRICTLY FOR WHATSAPP ACTIONS ONLY */
  --color-whatsapp: #25D366;
  --color-whatsapp-hover: #20BD5A;

  /* Architectural Depth & Neutrals (White, Warm Ivory, Midnight Slate) */
  --color-dark: #0A1626;             /* Deep Midnight Ink */
  --color-dark-surface: #060E18;     /* Obsidian Dark Navy Surface */
  --color-dark-muted: #132438;       /* Deep Navy Slate */
  --color-body: #334155;             /* Slate 700 — High-legibility Editorial Reading Measure */
  --color-muted: #64748B;            /* Slate 500 — Secondary Details */
  --color-light-muted: #94A3B8;      /* Slate 400 */

  --color-white: #FFFFFF;
  --color-ivory: #F8F6F0;            /* Warm Architectural Ivory */
  --color-bg-light: #F8FAFC;         /* Crisp Off-White Surface */
  --color-border: #E2E8F0;           /* Clean Structural Border */
  --color-border-light: #F1F5F9;     /* Hairline Divider */

  /* Typography Scale (Blu Bloom Editorial & Architectural Pairing) */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-body: 'Plus Jakarta Sans', var(--font-sans);
  --font-serif: 'Playfair Display', Georgia, 'Times New Roman', serif;
  --font-display: 'Playfair Display', Georgia, serif;

  /* Precise Architectural Radii (Clean, sharp, never bulbous AI rounded) */
  --radius-xs: 3px;
  --radius-sm: 4px;                  /* Inputs, Small Buttons */
  --radius-md: 6px;                  /* Cards, Tooltips, Icon Boxes */
  --radius-lg: 8px;                  /* Major Feature Cards, Hero Media */
  --radius-xl: 12px;                 /* Outer Showcases */
  --radius-full: 9999px;             /* Pill Badges */

  /* Architectural Ambient Elevation Shadows */
  --shadow-subtle: 0 1px 2px rgba(11, 37, 64, 0.04);
  --shadow-sm: 0 2px 6px -1px rgba(11, 37, 64, 0.05), 0 1px 2px rgba(11, 37, 64, 0.03);
  --shadow-card: 0 4px 14px -2px rgba(11, 37, 64, 0.06), 0 1px 3px rgba(11, 37, 64, 0.04);
  --shadow-hover: 0 16px 32px -6px rgba(11, 37, 64, 0.09), 0 4px 12px -2px rgba(11, 37, 64, 0.04);
  --shadow-floating: 0 20px 40px -8px rgba(11, 37, 64, 0.16);

  /* Layout & Grid Constants */
  --max-width: 1280px;
  --header-height: 76px;
  --topbar-height: 38px;
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-fast: 150ms;
  --duration-normal: 250ms;
}'''
    css = re.sub(old_root_pattern, new_root, css)

    # 2. Update typography definitions
    old_typo_pattern = r'/\* --------------------------------------------------------------------------\s*3\. TYPOGRAPHY SYSTEM.*?(?=/\* --------------------------------------------------------------------------|$)'
    new_typo = '''/* --------------------------------------------------------------------------
   3. TYPOGRAPHY SYSTEM (BLU BLOOM EDITORIAL SERIF & SANS PAIRING)
   -------------------------------------------------------------------------- */
h1, h2, h3, h4, h5, h6,
.hero-headline h1,
.brief-main-title,
.section-header-center h2,
.section-heading h2,
.process-header h2,
.why-choose-title,
.service-card-title,
.room-card-title {
  font-family: var(--font-serif);
  color: var(--color-primary);
  font-weight: 600;
  line-height: 1.22;
  letter-spacing: -0.015em;
}

h1 {
  font-size: clamp(2.4rem, 4.4vw, 3.6rem);
  font-weight: 600;
  line-height: 1.15;
}

h2 {
  font-size: clamp(1.9rem, 3.2vw, 2.7rem);
  font-weight: 600;
  line-height: 1.2;
}

h3 {
  font-size: clamp(1.3rem, 2vw, 1.7rem);
  font-weight: 600;
  line-height: 1.28;
}

h4 {
  font-size: 1.15rem;
  font-weight: 600;
  line-height: 1.35;
}

p {
  font-family: var(--font-body);
  font-size: 1rem;
  line-height: 1.7;
  color: var(--color-body);
}

/* Editorial Italic Emphasis (Blu Bloom Signature) */
h1 em, h2 em, h3 em,
.hero-headline h1 em,
.highlight, .highlight-serif {
  font-family: var(--font-serif);
  font-style: italic;
  font-weight: 400;
  color: var(--color-accent);
}

.eyebrow,
.pill-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-sans);
  font-size: 0.72rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: var(--color-accent);
  background: var(--color-accent-subtle);
  border: 1px solid var(--color-accent-border);
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-full);
}

.pill-badge-red,
.pill-badge-green,
.pill-badge-gold {
  background: var(--color-accent-subtle);
  color: var(--color-accent);
  border: 1px solid var(--color-accent-border);
}

.section-header-center {
  text-align: center;
  max-width: 760px;
  margin: 0 auto 3rem;
}
.section-header-center h2 {
  margin-bottom: 0.85rem;
}
.section-header-center p {
  font-size: 1.05rem;
  color: var(--color-muted);
  line-height: 1.7;
}

.section-title-wrap {
  margin-bottom: 2.5rem;
}
.section-title-wrap h2 {
  margin-bottom: 0.75rem;
}
.section-title-wrap p {
  font-size: 1.05rem;
  color: var(--color-muted);
  max-width: 680px;
}

/* Flex Row Section Heading (Blu Bloom Signature) */
.section-heading-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 3rem;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.text-link {
  color: var(--color-primary);
  font-weight: 600;
  font-size: 0.92rem;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: color 0.2s ease, gap 0.2s ease;
}
.text-link:hover {
  color: var(--color-accent);
  gap: 9px;
}
.text-link .arrow-icon {
  font-size: 1.05rem;
  transition: transform 0.2s ease;
}
.text-link:hover .arrow-icon {
  transform: translate(2px, -2px);
}
'''
    css = re.sub(old_typo_pattern, new_typo + '\n\n', css, flags=re.DOTALL)

    # 3. Process Section styling - Immersive Navy (Blu Bloom Signature)
    process_pattern = r'/\* --------------------------------------------------------------------------\s*14\. STRUCTURED MILESTONE EXECUTION PROCESS.*?(?=/\* --------------------------------------------------------------------------|$)'
    new_process = '''/* --------------------------------------------------------------------------
   14. STRUCTURED MILESTONE EXECUTION PROCESS (BLU BLOOM IMMERSIVE NAVY)
   -------------------------------------------------------------------------- */
.process-section {
  background-color: var(--color-primary) !important;
  color: #FFFFFF !important;
  padding: 5.5rem 0;
}
.process-section .section-header-center h2 {
  color: #FFFFFF !important;
}
.process-section .section-header-center p {
  color: #CBD5E1 !important;
}
.process-section .pill-badge {
  background: rgba(184, 144, 88, 0.18) !important;
  color: #E8D8BA !important;
  border-color: rgba(184, 144, 88, 0.35) !important;
}
.process-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  position: relative;
  margin-top: 2.5rem;
}
.process-step {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-sm);
  padding: 2.2rem 1.6rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  position: relative;
  transition: transform 0.25s ease, border-color 0.25s ease, background 0.25s ease;
}
.process-step:hover {
  transform: translateY(-4px);
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--color-accent);
}
.step-circle {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--color-accent);
  color: #FFFFFF;
  font-family: var(--font-serif);
  font-weight: 700;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
  box-shadow: 0 4px 12px rgba(184, 144, 88, 0.35);
}
.process-step h4,
.process-step h3 {
  font-family: var(--font-serif);
  color: #FFFFFF;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}
.process-step p {
  color: #CBD5E1;
  font-size: 0.88rem;
  line-height: 1.6;
}
'''
    css = re.sub(process_pattern, new_process + '\n\n', css, flags=re.DOTALL)

    # 4. Floating buttons: Call above WhatsApp
    floating_pattern = r'/\* --------------------------------------------------------------------------\s*23\. FLOATING ACTION CONTROLS.*?(?=/\* --------------------------------------------------------------------------|$)'
    new_floating = '''/* --------------------------------------------------------------------------
   23. FLOATING ACTION CONTROLS (CALL ABOVE WHATSAPP) & MOBILE STICKY BAR
   -------------------------------------------------------------------------- */
.floating-actions-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
  z-index: 995;
}
.call-float,
.whatsapp-float {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  position: relative;
  transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.25s ease, background-color 0.2s ease;
}

/* Call Button (Top / Above WhatsApp) */
.call-float {
  background-color: var(--color-primary);
  color: #FFFFFF;
  border: 1px solid rgba(184, 144, 88, 0.4);
  box-shadow: 0 4px 16px rgba(11, 37, 64, 0.4);
}
.call-float:hover {
  background-color: var(--color-primary-hover);
  transform: translateY(-2px) scale(1.06);
  box-shadow: 0 8px 24px rgba(11, 37, 64, 0.55);
}
.call-float svg {
  width: 22px;
  height: 22px;
  fill: #FFFFFF;
  transition: transform 0.2s ease;
}
.call-float:hover svg {
  transform: rotate(12deg);
}

/* WhatsApp Button (Bottom / Below Call) */
.whatsapp-float {
  background-color: #25D366;
  color: #FFFFFF;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
}
.whatsapp-float:hover {
  background-color: #20BD5A;
  transform: translateY(-2px) scale(1.06);
  box-shadow: 0 8px 24px rgba(37, 211, 102, 0.55);
}
.whatsapp-float svg {
  width: 26px;
  height: 26px;
  fill: #FFFFFF;
}

/* Tooltips */
.call-tooltip,
.whatsapp-tooltip {
  position: absolute;
  right: 64px;
  top: 50%;
  transform: translateY(-50%);
  background-color: #060E18;
  color: #FFFFFF;
  font-size: 0.78rem;
  font-weight: 600;
  white-space: nowrap;
  padding: 6px 12px;
  border-radius: 6px;
  border: 1px solid rgba(184, 144, 88, 0.3);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
  pointer-events: none;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s ease, visibility 0.2s ease, transform 0.2s ease;
}
.call-float:hover .call-tooltip,
.whatsapp-float:hover .whatsapp-tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(-4px);
}

/* Standalone fallbacks */
body > a.whatsapp-float:not(.floating-actions-container a) {
  position: fixed;
  right: 24px;
  bottom: 24px;
  z-index: 995;
}
body > a.call-float:not(.floating-actions-container a) {
  position: fixed;
  right: 24px;
  bottom: 86px;
  left: auto;
  z-index: 995;
}

/* Mobile Sticky Bottom CTA */
.sticky-mobile-cta {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: #FFFFFF;
  border-top: 1px solid var(--color-border);
  box-shadow: 0 -4px 16px rgba(11, 37, 64, 0.08);
  z-index: 995;
  padding: 0.5rem 1rem;
}
.cta-btn-group {
  display: flex;
  gap: 0.75rem;
  height: 100%;
}
.cta-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-sm);
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none;
}
.btn-call {
  background: var(--color-primary);
  color: #FFFFFF !important;
}
.btn-wa {
  background: var(--color-whatsapp);
  color: #FFFFFF !important;
}
'''
    css = re.sub(floating_pattern, new_floating + '\n\n', css, flags=re.DOTALL)

    # 5. Clean all non-WhatsApp greens from the CSS
    css = re.sub(r'--color-green:[^;]+;', '', css)
    css = re.sub(r'--color-green-subtle:[^;]+;', '', css)
    css = css.replace('#15803D', '#B89058')
    css = css.replace('#15803d', '#B89058')
    css = css.replace('#16a34a', '#B89058')
    css = css.replace('#10b981', '#B89058')
    css = css.replace('#A7F3D0', '#E8D8BA')
    css = css.replace('#ECFDF5', '#FDFBF7')

    # Ensure .mobile-menu-overlay exists and is properly styled
    if '.mobile-menu-overlay' not in css:
        mobile_menu_css = '''
/* Mobile Navigation Drawer */
.mobile-menu-overlay {
  position: fixed;
  inset: 0;
  background-color: #FFFFFF;
  z-index: 2000;
  display: none;
  flex-direction: column;
  overflow-y: auto;
}
.mobile-menu-overlay.open {
  display: flex !important;
}
.mobile-menu-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid var(--color-border);
}
.mobile-menu-close {
  font-size: 1.5rem;
  color: var(--color-primary);
  padding: 0.5rem;
  cursor: pointer;
}
.mobile-menu-content {
  padding: 1.5rem;
  flex-grow: 1;
}
.mobile-menu-section-title {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--color-accent);
  margin-bottom: 1rem;
}
.mobile-nav-links {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  margin-bottom: 1.75rem;
}
.mobile-nav-links a {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-primary);
}
'''
        css += '\n\n' + mobile_menu_css

    # 6. Write out assets/css/style.css
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Wrote updated assets/css/style.css, length:", len(css))

    # 7. Write out scripts/generate_master_style.py
    with open('scripts/generate_master_style.py', 'w', encoding='utf-8') as f:
        f.write('css = """' + css + '"""\n\ndef generate_style():\n    with open("assets/css/style.css", "w", encoding="utf-8") as f:\n        f.write(css)\n\nif __name__ == "__main__":\n    generate_style()\n')
    print("Wrote updated scripts/generate_master_style.py")

if __name__ == '__main__':
    build_complete_blubloom_system()
