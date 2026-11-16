"""
Update Delhi Interior website to perfectly implement the 3 screenshot specifications:
1. Image 1: "Why Choose Us / We offer perfect interior services"
   - Subtle warm interior photography backdrop (portfolio-bedroom.webp with soft ivory overlay)
   - Center-aligned header (Title: "Why Choose Us", Subtitle: "We offer perfect interior services")
   - Single unified elevated white floating card box (4 columns)
   - Line-art icons (House with Key, Handshake, Wallet with Cash, Connected Client Approach)
   - Centered titles, centered body paragraphs
   - Subtle vertical divider lines between columns
   - Complete removal of bottom tags for clean architectural elegance

2. Image 2: "An interior solution for every brief." (Blu Bloom Interior Layout)
   - Elegant left-aligned Playfair Display serif heading:
     "An interior solution for every<br>brief."
   - Subtitle: "Every property, material palette and scope is different. Choose a starting direction, then let our team prepare a project-specific BOQ and quotation."
   - Continuous seamless warm ivory/sand 5-column grid (01 Ultra Luxury, 02 Luxury, 03 Minimalist, 04 Essential, 05 Basic)
   - Golden brass numbers (01 to 05)
   - High-contrast Playfair Display serif tier titles
   - Editorial descriptions and "Request details ↗" with underline
   - Subtle vertical dividing borders between columns

3. Image 3: "✦ CERTIFIED MATERIALS / Quality You Can Feel"
   - 100% confirmed removed from index.html and all pages
   - Purged all dead CSS classes (.material-showcase-section, .materials-grid, .material-card)

4. Strict Color & Quality Rules:
   - Green is strictly & exclusively for WhatsApp (#25D366)
   - Primary is Deep Dark Navy Blue (#0B2540)
   - Accent is Warm Architectural Golden Brass (#B89058)
   - Surfaces are Crisp White (#FFFFFF) & Warm Ivory (#F8F6F0 / #F8F5EE)
   - Floating buttons: Call button (#0B2540) directly above WhatsApp (#25D366)
   - Zero mentions of warranty, guarantee, or 45 days
   - 24/7 studio timing preserved
"""

import os
import re

# ==============================================================================
# 1. UPDATE generate_master_style.py
# ==============================================================================
with open('scripts/generate_master_style.py', 'r', encoding='utf-8') as f:
    master_style_content = f.read()

# Replace why-choose styles
old_why_choose_css = r"""/* --------------------------------------------------------------------------
   16. WHY CHOOSE US (SECTION 2.5)
   -------------------------------------------------------------------------- */
.why-choose-section {
  padding: clamp(3.5rem, 6vw, 5.5rem) 0;
  background-color: var(--color-white);
  border-bottom: 1px solid var(--color-border);
}

.why-choose-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.why-choose-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2.2rem 1.6rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out), border-color 0.25s ease;
}
.why-choose-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
  border-color: var(--color-primary-border);
}

.why-choose-icon {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-md);
  background: var(--color-accent-subtle);
  border: 1px solid var(--color-accent-border);
  color: var(--color-accent);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
}

.why-choose-card h3 {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--color-dark);
  margin-bottom: 0.65rem;
}

.why-choose-card p {
  font-size: 0.9rem;
  color: var(--color-body);
  line-height: 1.65;
  margin-bottom: 1.25rem;
  flex: 1;
}"""

new_why_choose_css = r"""/* --------------------------------------------------------------------------
   16. WHY CHOOSE US (SECTION 2.5 - EXACT IMAGE 1 SPECIFICATION)
   -------------------------------------------------------------------------- */
.why-choose-section {
  position: relative;
  padding: clamp(4.5rem, 7vw, 6.5rem) 0;
  background-image: linear-gradient(rgba(248, 246, 240, 0.88), rgba(248, 246, 240, 0.94)), url('/assets/images/portfolio-bedroom.webp');
  background-position: center 30%;
  background-size: cover;
  background-repeat: no-repeat;
  border-bottom: 1px solid var(--color-border);
}

.why-choose-header-center {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 2.75rem auto;
}

.why-choose-main-title {
  font-family: var(--font-display);
  font-size: clamp(2.2rem, 3.8vw, 2.85rem);
  font-weight: 700;
  color: var(--color-primary);
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.why-choose-main-sub {
  font-family: var(--font-sans);
  font-size: 1.1rem;
  color: #5A6472;
  margin: 0;
  line-height: 1.5;
}

/* Floating White Card Container (Image 1 Specification) */
.why-choose-floating-box {
  background: #FFFFFF;
  border-radius: 6px;
  box-shadow: 0 20px 48px -10px rgba(11, 37, 64, 0.10), 0 4px 16px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(226, 232, 240, 0.9);
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  padding: 3.5rem 1.5rem;
}

.why-choose-col {
  padding: 0.5rem 2rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-right: 1px solid #EEF2F6;
}

.why-choose-col:last-child {
  border-right: none;
}

.why-choose-icon-box {
  width: 64px;
  height: 64px;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-primary);
  transition: transform 0.25s ease;
}

.why-choose-floating-box:hover .why-choose-col:hover .why-choose-icon-box {
  transform: translateY(-3px);
}

.why-choose-col-title {
  font-family: var(--font-sans);
  font-size: 1.18rem;
  font-weight: 700;
  color: var(--color-primary);
  margin-bottom: 0.85rem;
  line-height: 1.35;
}

.why-choose-col-desc {
  font-size: 0.88rem;
  color: #5A6472;
  line-height: 1.65;
  margin: 0;
}

@media (max-width: 1024px) {
  .why-choose-floating-box {
    grid-template-columns: repeat(2, 1fr);
    padding: 2.5rem 1rem;
    gap: 2rem 0;
  }
  .why-choose-col:nth-child(2) {
    border-right: none;
  }
  .why-choose-col:nth-child(1),
  .why-choose-col:nth-child(2) {
    border-bottom: 1px solid #EEF2F6;
    padding-bottom: 2rem;
  }
}

@media (max-width: 640px) {
  .why-choose-floating-box {
    grid-template-columns: 1fr;
    padding: 2rem 1rem;
    gap: 2rem;
  }
  .why-choose-col {
    border-right: none !important;
    border-bottom: 1px solid #EEF2F6;
    padding: 0 1rem 2rem 1rem;
  }
  .why-choose-col:last-child {
    border-bottom: none;
    padding-bottom: 0;
  }
}"""

# Replace brief-solutions styles
old_brief_css = r"""/* --------------------------------------------------------------------------
   16.1 AN INTERIOR SOLUTION FOR EVERY BRIEF (SECTION 6.5)
   -------------------------------------------------------------------------- */
.brief-solutions-section {
  padding: clamp(4rem, 6vw, 6rem) 0;
  background-color: #FFFFFF;
  border-top: 1px solid var(--color-border);
}

.brief-solutions-header {
  max-width: 820px;
  margin-bottom: 3rem;
}

.brief-main-title {
  font-family: var(--font-display);
  font-size: clamp(2.2rem, 3.8vw, 3rem);
  font-weight: 800;
  color: var(--color-dark);
  letter-spacing: -0.025em;
  margin-bottom: 1rem;
  line-height: 1.15;
}

.brief-sub-title {
  font-size: 1.05rem;
  color: var(--color-body);
  line-height: 1.7;
}

.brief-tiers-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1.25rem;
}

.brief-tier-card {
  background: #F8F6F0;
  border: 1px solid #ECE7DD;
  border-radius: var(--radius-sm);
  padding: 2.2rem 1.6rem 1.8rem;
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out), border-color 0.25s ease;
}
.brief-tier-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
  border-color: var(--color-accent);
}

.brief-tier-num {
  font-family: var(--font-display);
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-accent);
  margin-bottom: 1.75rem;
  letter-spacing: 0.05em;
}

.brief-tier-title {
  font-family: var(--font-display);
  font-size: 1.45rem;
  font-weight: 700;
  color: var(--color-dark);
  margin-bottom: 0.75rem;
  line-height: 1.2;
}

.brief-tier-desc {
  font-size: 0.88rem;
  color: var(--color-body);
  line-height: 1.6;
  margin-bottom: 2rem;
  flex: 1;
}

.brief-tier-link {
  font-family: var(--font-display);
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--color-dark);
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  text-decoration: underline;
  text-underline-offset: 4px;
  transition: color var(--duration-fast) ease;
}
.brief-tier-link:hover {
  color: var(--color-accent);
}
.brief-tier-link .arrow-icon {
  font-size: 1rem;
  line-height: 1;
  transition: transform var(--duration-fast) ease;
}"""

new_brief_css = r"""/* --------------------------------------------------------------------------
   16.1 AN INTERIOR SOLUTION FOR EVERY BRIEF (IMAGE 2 BLU BLOOM SPECIFICATION)
   -------------------------------------------------------------------------- */
.brief-solutions-section {
  padding: clamp(4.5rem, 6.5vw, 6.5rem) 0;
  background-color: #FFFFFF;
  border-top: 1px solid #ECE7DD;
}

.brief-solutions-header {
  max-width: 840px;
  margin-bottom: 3rem;
}

.brief-main-title {
  font-family: var(--font-display);
  font-size: clamp(2.4rem, 4.2vw, 3.4rem);
  font-weight: 700;
  color: var(--color-primary);
  letter-spacing: -0.025em;
  margin: 0 0 1.25rem 0;
  line-height: 1.15;
}

.brief-sub-title {
  font-family: var(--font-sans);
  font-size: 1.05rem;
  color: #5A6472;
  line-height: 1.7;
  max-width: 720px;
  margin: 0;
}

/* Seamless 5-Column Ivory Grid (Image 2 Specification) */
.brief-tiers-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  background: #F8F5EE;
  border: 1px solid #ECE6DA;
  border-radius: 4px;
  overflow: hidden;
}

.brief-tier-col {
  padding: 3rem 2rem 2.5rem;
  border-right: 1px solid #E5DFD2;
  display: flex;
  flex-direction: column;
  background: #F8F5EE;
  transition: background-color 0.25s ease;
}

.brief-tier-col:last-child {
  border-right: none;
}

.brief-tier-col:hover {
  background: #FAF7F2;
}

.brief-tier-num {
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--color-accent);
  margin-bottom: 2rem;
  letter-spacing: 0.05em;
  display: block;
}

.brief-tier-title {
  font-family: var(--font-display);
  font-size: 1.65rem;
  font-weight: 600;
  color: var(--color-primary);
  margin-bottom: 1rem;
  line-height: 1.25;
}

.brief-tier-desc {
  font-size: 0.9rem;
  color: #5A6472;
  line-height: 1.65;
  margin-bottom: 2.5rem;
  flex: 1;
}

.brief-tier-link {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--color-primary);
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  text-decoration: underline;
  text-underline-offset: 4px;
  transition: color 0.2s ease;
}

.brief-tier-link:hover {
  color: var(--color-accent);
}

.brief-tier-link .arrow-icon {
  font-size: 1rem;
  line-height: 1;
  transition: transform 0.2s ease;
}

.brief-tier-link:hover .arrow-icon {
  transform: translate(2px, -2px);
}

@media (max-width: 1100px) {
  .brief-tiers-container {
    grid-template-columns: repeat(3, 1fr);
  }
  .brief-tier-col:nth-child(3) {
    border-right: none;
  }
  .brief-tier-col:nth-child(1),
  .brief-tier-col:nth-child(2),
  .brief-tier-col:nth-child(3) {
    border-bottom: 1px solid #E5DFD2;
  }
}

@media (max-width: 768px) {
  .brief-tiers-container {
    grid-template-columns: 1fr;
  }
  .brief-tier-col {
    border-right: none !important;
    border-bottom: 1px solid #E5DFD2;
    padding: 2.2rem 1.5rem;
  }
  .brief-tier-col:last-child {
    border-bottom: none;
  }
}"""

# Clean material-showcase CSS
old_mat_css = r"""/* --------------------------------------------------------------------------
   17. MATERIAL SHOWCASE (SECTION 6)
   -------------------------------------------------------------------------- */
.material-showcase-section {
  padding: clamp(3.5rem, 6vw, 5.5rem) 0;
  background-color: var(--color-bg-light);
}

.materials-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.material-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2rem 1.5rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.material-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.material-icon-wrap {
  width: 50px;
  height: 50px;
  border-radius: var(--radius-md);
  background: var(--color-accent-subtle);
  border: 1px solid var(--color-accent-border);
  color: var(--color-accent);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
}

.material-card h3 {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--color-dark);
  margin-bottom: 0.65rem;
}

.material-card p {
  font-size: 0.88rem;
  color: var(--color-body);
  line-height: 1.6;
  margin-bottom: 1.25rem;
  flex: 1;
}

.material-spec-pill {
  display: inline-block;
  padding: 0.35rem 0.75rem;
  background: var(--color-accent-subtle);
  border: 1px solid var(--color-accent-border);
  border-radius: var(--radius-pill);
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--color-accent);
  align-self: flex-start;
}"""

# Purge any remaining tag-green / pill-badge-green
if old_why_choose_css in master_style_content:
    master_style_content = master_style_content.replace(old_why_choose_css, new_why_choose_css)
    print("[SUCCESS] Replaced why-choose styles in generate_master_style.py")
else:
    print("[WARN] old_why_choose_css not exact match, using regex replace")
    master_style_content = re.sub(r'/\* -+ 16\. WHY CHOOSE US[\s\S]*?(?=/\* -+ 16\.1|\Z)', new_why_choose_css + "\n\n", master_style_content)

if old_brief_css in master_style_content:
    master_style_content = master_style_content.replace(old_brief_css, new_brief_css)
    print("[SUCCESS] Replaced brief-solutions styles in generate_master_style.py")
else:
    print("[WARN] old_brief_css not exact match, using regex replace")
    master_style_content = re.sub(r'/\* -+ 16\.1 AN INTERIOR SOLUTION[\s\S]*?(?=/\* -+ 17\.|\Z)', new_brief_css + "\n\n", master_style_content)

if old_mat_css in master_style_content:
    master_style_content = master_style_content.replace(old_mat_css, "/* 17. MATERIAL SHOWCASE: PERMANENTLY REMOVED AS REQUESTED */")
    print("[SUCCESS] Removed material-showcase styles from generate_master_style.py")

# Ensure desktop mobile drawer is completely hidden
desktop_rule = "\n@media (min-width: 992px) {\n  .mobile-menu-overlay {\n    display: none !important;\n  }\n}\n"
if ".mobile-menu-overlay {" in master_style_content and desktop_rule not in master_style_content:
    master_style_content = master_style_content.replace(".mobile-menu-overlay {", desktop_rule + "\n.mobile-menu-overlay {")

with open('scripts/generate_master_style.py', 'w', encoding='utf-8') as f:
    f.write(master_style_content)

# Execute generate_master_style.py to build assets/css/style.css
import subprocess
subprocess.run(['python', 'scripts/generate_master_style.py'], check=True)
print("[SUCCESS] Regenerated assets/css/style.css")

# ==============================================================================
# 2. UPDATE rebuild_complete_site_v3.py & index.html
# ==============================================================================
with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    site_builder_content = f.read()

# Exact Image 1 Section 2.5 HTML
new_section_2_5_html = """    <!-- 2.5 WHY CHOOSE US (EXACT IMAGE 1 SPECIFICATION) -->
    <section class="why-choose-section">
      <div class="container">
        <div class="why-choose-header-center">
          <h2 class="why-choose-main-title">Why Choose Us</h2>
          <p class="why-choose-main-sub">We offer perfect interior services</p>
        </div>

        <div class="why-choose-floating-box">
          <!-- Card 1: Years of Experience -->
          <div class="why-choose-col">
            <div class="why-choose-icon-box">
              <svg viewBox="0 0 64 64" width="52" height="52" fill="none" stroke="#0B2540" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="18" cy="18" r="7"/>
                <circle cx="18" cy="18" r="3"/>
                <path d="M25 18h24v6M39 18v6M45 18v6"/>
                <path d="M10 38l22-16 22 16"/>
                <path d="M14 36v20a2 2 0 0 0 2 2h32a2 2 0 0 0 2-2V36"/>
                <path d="M26 58V42a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16"/>
                <circle cx="36" cy="48" r="1.5" fill="#0B2540"/>
              </svg>
            </div>
            <h3 class="why-choose-col-title">Years of Experience</h3>
            <p class="why-choose-col-desc">Since 2000, Delhi Interior has been a trusted name in Delhi, offering complete interior and furniture solutions with excellence.</p>
          </div>

          <!-- Card 2: Creative Interior Designers -->
          <div class="why-choose-col">
            <div class="why-choose-icon-box">
              <svg viewBox="0 0 64 64" width="52" height="52" fill="none" stroke="#0B2540" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M10 26l12-10 12 12-8 8-16-10z"/>
                <path d="M54 26L42 16 30 28l8 8 16-10z"/>
                <path d="M26 38l6 6 8-8"/>
                <path d="M30 46l6 6 8-8"/>
                <path d="M34 52l4 4 6-6"/>
                <path d="M16 22L8 30l12 12"/>
                <path d="M48 22l8 8-12 12"/>
              </svg>
            </div>
            <h3 class="why-choose-col-title">Creative Interior Designers</h3>
            <p class="why-choose-col-desc">Our expert designers combine artistry with functionality to transform ordinary spaces into elegant and inspiring interiors.</p>
          </div>

          <!-- Card 3: Skilled Craftsmanship -->
          <div class="why-choose-col">
            <div class="why-choose-icon-box">
              <svg viewBox="0 0 64 64" width="52" height="52" fill="none" stroke="#0B2540" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 22V14a2 2 0 0 1 2-2h26a2 2 0 0 1 2 2v8"/>
                <path d="M28 12l20 10"/>
                <rect x="10" y="22" width="44" height="30" rx="4"/>
                <path d="M40 31h14v12H40a4 4 0 0 1-4-4v-4a4 4 0 0 1 4-4z"/>
                <circle cx="44" cy="37" r="2.5" fill="#0B2540"/>
              </svg>
            </div>
            <h3 class="why-choose-col-title">Skilled Craftsmanship</h3>
            <p class="why-choose-col-desc">Our talented carpenter team breathes new life into furniture through customization, restoration, and quality repair work.</p>
          </div>

          <!-- Card 4: Client-Focused Approach -->
          <div class="why-choose-col">
            <div class="why-choose-icon-box">
              <svg viewBox="0 0 64 64" width="52" height="52" fill="none" stroke="#0B2540" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="22" y="16" width="20" height="32" rx="3"/>
                <circle cx="32" cy="43" r="1.5" fill="#0B2540"/>
                <line x1="28" y1="20" x2="36" y2="20"/>
                <rect x="24" y="6" width="16" height="8" rx="2"/>
                <circle cx="12" cy="24" r="5"/>
                <path d="M12 21v3l2 1"/>
                <rect x="47" y="19" width="10" height="10" rx="2"/>
                <line x1="47" y1="23" x2="57" y2="23"/>
                <circle cx="13" cy="41" r="3"/>
                <path d="M13 44c-2 2-3 4-3 5h6c0-1-1-3-3-5z"/>
                <circle cx="51" cy="41" r="4"/>
                <path d="M51 39v2M51 43v.5"/>
              </svg>
            </div>
            <h3 class="why-choose-col-title">Client-Focused Approach</h3>
            <p class="why-choose-col-desc">We work closely with every client to understand their lifestyle and vision, ensuring each project reflects their personality.</p>
          </div>
        </div>
      </div>
    </section>"""

# Exact Image 2 Section 6.5 HTML
new_section_6_5_html = """    <!-- 6.5 AN INTERIOR SOLUTION FOR EVERY BRIEF (EXACT IMAGE 2 BLU BLOOM SPECIFICATION) -->
    <section class="brief-solutions-section">
      <div class="container">
        <div class="brief-solutions-header">
          <h2 class="brief-main-title">An interior solution for every<br>brief.</h2>
          <p class="brief-sub-title">
            Every property, material palette and scope is different. Choose a starting direction, then let our team prepare a project-specific BOQ and quotation.
          </p>
        </div>

        <div class="brief-tiers-container">
          <!-- 01 Ultra Luxury -->
          <div class="brief-tier-col" data-tier="Ultra Luxury">
            <span class="brief-tier-num">01</span>
            <h3 class="brief-tier-title">Ultra Luxury</h3>
            <p class="brief-tier-desc">Bespoke detailing and an elevated material palette.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 02 Luxury -->
          <div class="brief-tier-col" data-tier="Luxury">
            <span class="brief-tier-num">02</span>
            <h3 class="brief-tier-title">Luxury</h3>
            <p class="brief-tier-desc">Premium finishes with complete design and execution support.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 03 Minimalist -->
          <div class="brief-tier-col" data-tier="Minimalist">
            <span class="brief-tier-num">03</span>
            <h3 class="brief-tier-title">Minimalist</h3>
            <p class="brief-tier-desc">Calm, functional spaces with disciplined material choices.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 04 Essential -->
          <div class="brief-tier-col" data-tier="Essential">
            <span class="brief-tier-num">04</span>
            <h3 class="brief-tier-title">Essential</h3>
            <p class="brief-tier-desc">A focused interior scope built around everyday priorities.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 05 Basic -->
          <div class="brief-tier-col" data-tier="Basic">
            <span class="brief-tier-num">05</span>
            <h3 class="brief-tier-title">Basic</h3>
            <p class="brief-tier-desc">Practical solutions for a clearly defined project scope.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>
        </div>
      </div>
    </section>"""

# Replace in site_builder_content
site_builder_content = re.sub(
    r'<!-- 2\.5 WHY CHOOSE US[\s\S]*?(?=<!-- 3\. DUAL SPECIALIZATION)',
    new_section_2_5_html + "\n\n    ",
    site_builder_content
)

site_builder_content = re.sub(
    r'<!-- 6\.5 AN INTERIOR SOLUTION FOR EVERY BRIEF[\s\S]*?(?=<!-- 8\. SIGNATURE INTERIOR PROCESS)',
    new_section_6_5_html + "\n\n    ",
    site_builder_content
)

with open('scripts/rebuild_complete_site_v3.py', 'w', encoding='utf-8') as f:
    f.write(site_builder_content)

# Execute rebuild_complete_site_v3.py to write index.html
subprocess.run(['python', 'scripts/rebuild_complete_site_v3.py'], check=True)
print("[SUCCESS] Regenerated index.html with exact screenshot specifications")

# Also update index.html directly to ensure 100% sync
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = re.sub(
    r'<!-- 2\.5 WHY CHOOSE US[\s\S]*?(?=<!-- 3\. DUAL SPECIALIZATION)',
    new_section_2_5_html + "\n\n    ",
    index_html
)

index_html = re.sub(
    r'<!-- 6\.5 AN INTERIOR SOLUTION FOR EVERY BRIEF[\s\S]*?(?=<!-- 8\. SIGNATURE INTERIOR PROCESS)',
    new_section_6_5_html + "\n\n    ",
    index_html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print("[SUCCESS] Direct sync of index.html complete")
