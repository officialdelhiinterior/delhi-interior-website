with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Replace Section 2.5 with the 4-card "Why Choose Us" section
old_section_2_5_start = code.find('<!-- 2.5 THE DIRECT MASTER CARPENTER')
old_section_2_5_end = code.find('<!-- 3. DUAL SPECIALIZATION')

if old_section_2_5_start != -1 and old_section_2_5_end != -1:
    new_why_choose = '''<!-- 2.5 WHY CHOOSE US (WE OFFER COMPLETE INTERIOR & CARPENTRY SOLUTIONS) -->
    <section class="why-choose-section">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            ✦ The Craftsman Difference
          </div>
          <h2>Why Choose Us</h2>
          <p>We combine the spatial artistry of a luxury design studio with the hands-on precision and honest rates of in-house master carpenters.</p>
        </div>

        <div class="why-choose-grid">
          <!-- Card 1: Years of Experience -->
          <div class="why-choose-card">
            <div class="why-choose-icon">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/><circle cx="12" cy="12" r="2"/></svg>
            </div>
            <h3>Years of Experience</h3>
            <p>A trusted name in Delhi NCR, offering complete interior, architectural woodwork, and custom furniture solutions with craftsmanship excellence.</p>
            <span class="craftsman-tag tag-blue">✓ 10+ Years Woodworking Heritage</span>
          </div>

          <!-- Card 2: Creative Interior Designers -->
          <div class="why-choose-card">
            <div class="why-choose-icon">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
            </div>
            <h3>Creative Interior Designers</h3>
            <p>Our expert designers combine artistry with functionality to transform ordinary spaces into elegant, timeless, and inspiring interiors.</p>
            <span class="craftsman-tag tag-amber">✓ Bespoke Spatial Planning</span>
          </div>

          <!-- Card 3: Skilled Craftsmanship -->
          <div class="why-choose-card">
            <div class="why-choose-icon">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
            </div>
            <h3>Skilled Craftsmanship</h3>
            <p>Our talented in-house carpenter team breathes new life into furniture and joinery through custom fabrication, restoration, and quality repair work.</p>
            <span class="craftsman-tag tag-green">✓ In-House Master Karigars</span>
          </div>

          <!-- Card 4: Client-Focused Approach -->
          <div class="why-choose-card">
            <div class="why-choose-icon">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </div>
            <h3>Client-Focused Approach</h3>
            <p>We work closely with every client to understand their lifestyle and vision, ensuring each project reflects their personality with full transparency.</p>
            <span class="craftsman-tag tag-blue">✓ Dedicated Single Contact</span>
          </div>
        </div>
      </div>
    </section>

    '''
    code = code[:old_section_2_5_start] + new_why_choose + code[old_section_2_5_end:]
    print("Replaced Section 2.5 with Why Choose Us (4 Cards)")

# 2. Add Section 6.5 "An interior solution for every brief" after Section 7 (Services)
services_end = code.find('<!-- 8. MATERIAL SHOWCASE')
if services_end != -1:
    new_brief_section = '''<!-- 6.5 AN INTERIOR SOLUTION FOR EVERY BRIEF -->
    <section class="brief-solutions-section">
      <div class="container">
        <div class="brief-solutions-header">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.85rem;">
            ✦ Tailored Scope
          </div>
          <h2 class="brief-main-title">An interior solution for every brief.</h2>
          <p class="brief-sub-title">
            Every property, material palette and scope is different. Choose a starting direction, then let our team prepare a project-specific BOQ and quotation.
          </p>
        </div>

        <div class="brief-tiers-grid">
          <!-- 01 Ultra Luxury -->
          <div class="brief-tier-card" data-tier="Ultra Luxury">
            <span class="brief-tier-num">01</span>
            <h3 class="brief-tier-title">Ultra Luxury</h3>
            <p class="brief-tier-desc">Bespoke detailing and an elevated material palette.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 02 Luxury -->
          <div class="brief-tier-card" data-tier="Luxury">
            <span class="brief-tier-num">02</span>
            <h3 class="brief-tier-title">Luxury</h3>
            <p class="brief-tier-desc">Premium finishes with complete design and execution support.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 03 Minimalist -->
          <div class="brief-tier-card" data-tier="Minimalist">
            <span class="brief-tier-num">03</span>
            <h3 class="brief-tier-title">Minimalist</h3>
            <p class="brief-tier-desc">Calm, functional spaces with disciplined material choices.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 04 Essential -->
          <div class="brief-tier-card" data-tier="Essential">
            <span class="brief-tier-num">04</span>
            <h3 class="brief-tier-title">Essential</h3>
            <p class="brief-tier-desc">A focused interior scope built around everyday priorities.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Complete Renovation">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 05 Basic -->
          <div class="brief-tier-card" data-tier="Basic">
            <span class="brief-tier-num">05</span>
            <h3 class="brief-tier-title">Basic</h3>
            <p class="brief-tier-desc">Practical solutions for a clearly defined project scope.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Custom Woodwork &amp; Carpentry">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    '''
    code = code[:services_end] + new_brief_section + code[services_end:]
    print("Added Section 6.5 (An interior solution for every brief)")

# 3. Clean remaining room cards chips
code = code.replace('Delivered in <strong>21 Days</strong>', 'Scope: <strong>Bespoke Mandir</strong>')
code = code.replace('Delivered in <strong>42 Days</strong>', 'Scope: <strong>Modular Kitchen</strong>')
code = code.replace('Delivered in <strong>38 Days</strong>', 'Scope: <strong>Master Suite</strong>')

with open('scripts/rebuild_complete_site_v3.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated scripts/rebuild_complete_site_v3.py with new sections and cleaned room chips.")
