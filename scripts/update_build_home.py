import re

with open('scripts/build_home.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Header Navigation in scripts/build_home.py
old_header_pattern = r'<header class="site-header" role="banner">[\s\S]*?</header>'

new_header = '''<header class="site-header" role="banner">
    <div class="container nav-container">
      <a href="/" class="site-logo" aria-label="Delhi Interior Home">
        Delhi Interior<span class="logo-dot">.</span>
      </a>

      <nav class="main-navigation" aria-label="Main navigation">
        <ul class="nav-links">
          <li class="nav-dropdown-item">
            <a href="/modular-kitchen-delhi/" class="nav-dropdown-trigger">
              Services <span class="dropdown-chevron">▼</span>
            </a>
            <div class="nav-dropdown-menu" role="menu">
              <a href="/modular-kitchen-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">🍳</span>
                <div class="dropdown-text">
                  <strong>Modular Kitchens</strong>
                  <span>L &amp; U-Shaped, Acrylic &amp; PU</span>
                </div>
              </a>
              <a href="/wardrobe-design-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">🚪</span>
                <div class="dropdown-text">
                  <strong>Custom Wardrobes</strong>
                  <span>Sliding, Walk-in &amp; Lofts</span>
                </div>
              </a>
              <a href="/full-home-interior-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">🏡</span>
                <div class="dropdown-text">
                  <strong>Full Home Interiors</strong>
                  <span>Complete 2/3/4 BHK Turnkey</span>
                </div>
              </a>
              <a href="/wall-paneling-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">📺</span>
                <div class="dropdown-text">
                  <strong>Wall Paneling &amp; TV Units</strong>
                  <span>Charcoal, Louver &amp; Fluted</span>
                </div>
              </a>
              <a href="/false-ceiling-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">💡</span>
                <div class="dropdown-text">
                  <strong>False Ceiling &amp; Lighting</strong>
                  <span>Gypsum, Cove &amp; Track Lights</span>
                </div>
              </a>
              <a href="/doors-partitions-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">🏛️</span>
                <div class="dropdown-text">
                  <strong>Doors &amp; Partitions</strong>
                  <span>Fluted Glass, Jali &amp; Flush</span>
                </div>
              </a>
              <a href="/bedroom-furniture-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">📚</span>
                <div class="dropdown-text">
                  <strong>Furniture &amp; Study</strong>
                  <span>Workstations, Mandirs &amp; Consoles</span>
                </div>
              </a>
              <a href="/commercial-interior-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">🏢</span>
                <div class="dropdown-text">
                  <strong>Commercial Interiors</strong>
                  <span>Offices, Retail &amp; Clinics</span>
                </div>
              </a>
              <a href="/plumbing-electrical-delhi/" class="dropdown-link" role="menuitem" style="grid-column: span 2;">
                <span class="dropdown-icon">🎨</span>
                <div class="dropdown-text">
                  <strong>MEP, Civil &amp; Luxury Finishes</strong>
                  <span>Concealed Plumbing, Electrical, Asian Paints Royale &amp; PU Polish</span>
                </div>
              </a>
            </div>
          </li>
          <li><a href="#estimator">Cost Calculator</a></li>
          <li><a href="/portfolio/">Designs</a></li>
          <li><a href="/process/">How It Works</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </nav>

      <div class="nav-right">
        <a href="tel:+919811000000" class="nav-phone" aria-label="Call Delhi Interior">
          <svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          +91 98110 00000
        </a>
        <a href="/contact/" class="btn btn-primary">Book Consultation</a>
        <button class="hamburger" aria-label="Open menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>'''

code = re.sub(old_header_pattern, new_header, code, count=1)

# 2. Update Mobile Menu Drawer in scripts/build_home.py
old_mobile_menu_pattern = r'<div id="mobile-menu" class="mobile-menu-overlay"[\s\S]*?</div>\s*</div>'

new_mobile_menu = '''<div id="mobile-menu" class="mobile-menu-overlay" aria-modal="true" role="dialog">
    <div class="mobile-menu-header">
      <div class="site-logo">Delhi Interior<span class="logo-dot">.</span></div>
      <button class="mobile-menu-close" aria-label="Close menu">✕</button>
    </div>
    <div class="mobile-menu-content" style="padding: 1.5rem; overflow-y: auto;">
      <div class="mobile-menu-section-title">Popular Services</div>
      <ul class="mobile-nav-services">
        <li><a href="/modular-kitchen-delhi/" onclick="closeMobileMenu()">🍳 Modular Kitchens</a></li>
        <li><a href="/wardrobe-design-delhi/" onclick="closeMobileMenu()">🚪 Custom Wardrobes</a></li>
        <li><a href="/full-home-interior-delhi/" onclick="closeMobileMenu()">🏡 Full Home Interiors</a></li>
        <li><a href="/wall-paneling-delhi/" onclick="closeMobileMenu()">📺 Wall Paneling &amp; Louvers</a></li>
        <li><a href="/false-ceiling-delhi/" onclick="closeMobileMenu()">💡 False Ceiling &amp; Lights</a></li>
        <li><a href="/doors-partitions-delhi/" onclick="closeMobileMenu()">🏛️ Doors &amp; Partitions</a></li>
        <li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">📚 Custom Furniture &amp; Study</a></li>
        <li><a href="/commercial-interior-delhi/" onclick="closeMobileMenu()">🏢 Commercial Interiors</a></li>
        <li><a href="/plumbing-electrical-delhi/" onclick="closeMobileMenu()">🎨 MEP, Civil &amp; Paints</a></li>
      </ul>

      <div class="mobile-menu-section-title" style="margin-top: 1.5rem;">Explore &amp; Tools</div>
      <ul class="mobile-nav-links" style="list-style: none; display: flex; flex-direction: column; gap: 0.85rem;">
        <li><a href="#estimator" onclick="closeMobileMenu()">📊 Cost Calculator</a></li>
        <li><a href="/portfolio/" onclick="closeMobileMenu()">🖼️ Portfolio &amp; Designs</a></li>
        <li><a href="/process/" onclick="closeMobileMenu()">⚡ How It Works (45 Days)</a></li>
        <li><a href="/about/" onclick="closeMobileMenu()">ℹ️ About Our Studio</a></li>
        <li><a href="/contact/" onclick="closeMobileMenu()">📍 Experience Centre &amp; Contact</a></li>
      </ul>
    </div>
    <div class="mobile-menu-footer">
      <p style="font-size: 0.85rem; color: #6B7280; margin-bottom: 1rem;">South Extension II, Ring Road, New Delhi<br>Mon–Sat: 9:00 AM – 7:00 PM</p>
      <a href="tel:+919811000000" class="btn btn-primary btn-block">Call +91 98110 00000</a>
    </div>
  </div>'''

code = re.sub(old_mobile_menu_pattern, new_mobile_menu, code, count=1)

# 3. Update Hero Section in scripts/build_home.py
old_hero_pattern = r'<!-- 1\. LIVSPACE-STYLE HERO SECTION -->[\s\S]*?</section>'

new_hero = '''<!-- 1. LIVSPACE-STYLE HERO SECTION -->
    <section class="hero-livspace">
      <div class="container hero-layout">
        
        <!-- Left Column: Copy & Value Proposition & Trust Stats -->
        <div class="hero-headline">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 1.2rem;">
            ✦ Delhi NCR's Certified Modular Interior Studio
          </div>
          <h1>
            Complete Home Interiors &amp; <span class="highlight">Modular Woodwork</span> in Delhi NCR<span class="logo-dot">.</span>
          </h1>
          <p class="hero-subhead">
            From modular kitchens and custom floor-to-ceiling wardrobes to full-home turnkey transformations — built in our own factory with certified BWP marine ply and German fittings. 45-day move-in guaranteed.
          </p>

          <!-- Livspace USPs -->
          <div class="hero-usps">
            <div class="hero-usp-item">
              <svg viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
              <span>45-Day Move-in Guarantee</span>
            </div>
            <div class="hero-usp-item">
              <svg viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
              <span>10-Year Comprehensive Warranty</span>
            </div>
            <div class="hero-usp-item">
              <svg viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
              <span>146 Quality Checks</span>
            </div>
          </div>

          <div style="display: flex; align-items: center; gap: 1rem; margin-top: 1.5rem; flex-wrap: wrap;">
            <a href="#consultation-card" class="btn btn-primary" style="padding: 0.9rem 2rem; font-size: 0.95rem;">Book Free 3D Consultation</a>
            <a href="#estimator" class="btn btn-outline" style="padding: 0.9rem 1.8rem; font-size: 0.95rem;">Calculate Cost</a>
          </div>

          <div style="display: flex; align-items: center; gap: 1rem; margin-top: 1.5rem;">
            <div class="pill-badge pill-badge-amber">
              ⭐ 4.9 / 5 (500+ Verified Delhi NCR Homeowners)
            </div>
          </div>

          <!-- Hero Metrics Bar -->
          <div class="hero-stats-row">
            <div class="hero-stat-box">
              <h4>500<span>+</span></h4>
              <p>Homes Delivered</p>
            </div>
            <div class="hero-stat-box">
              <h4>45<span> Days</span></h4>
              <p>Move-In Guarantee</p>
            </div>
            <div class="hero-stat-box">
              <h4>10<span> Yrs</span></h4>
              <p>Hardware Warranty</p>
            </div>
            <div class="hero-stat-box">
              <h4>0<span>%</span></h4>
              <p>EMI Available</p>
            </div>
          </div>
        </div>

        <!-- Right Column: Instant Consultation Card -->
        <div class="hero-form-card" id="consultation-card">
          <div class="form-badge">Free 3D Design Session</div>
          <h3>Book Your Consultation</h3>
          <p class="form-sub">Speak with our senior design director within 24 hours.</p>

          <form id="quote-form" novalidate>
            <input type="text" name="honeypot" style="display:none" tabindex="-1">
            
            <div class="form-fields-container">
              <div class="form-group">
                <label for="client-name" class="form-label">Full Name *</label>
                <input type="text" id="client-name" name="name" class="form-control" placeholder="Enter your full name" required>
              </div>

              <div class="form-group">
                <label for="client-phone" class="form-label">Phone Number *</label>
                <input type="tel" id="client-phone" name="phone" class="form-control" placeholder="+91 98765 43210" required>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="service-type" class="form-label">Space Required</label>
                  <select id="service-type" name="service" class="form-control">
                    <option value="Modular Kitchen" selected>Modular Kitchen</option>
                    <option value="Wardrobes &amp; Bedrooms">Wardrobes &amp; Bedrooms</option>
                    <option value="Full Home 2BHK">Full Home 2BHK</option>
                    <option value="Full Home 3BHK">Full Home 3BHK</option>
                    <option value="Full Home 4BHK+">Full Home 4BHK+ / Villa</option>
                    <option value="Wall Paneling &amp; TV Units">Wall Paneling &amp; TV Units</option>
                    <option value="Doors &amp; Partitions">Doors &amp; Partitions</option>
                    <option value="Other">Other / Commercial</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="client-area" class="form-label">Locality / City</label>
                  <input type="text" id="client-area" name="area" class="form-control" placeholder="e.g. Gurugram, GK-2">
                </div>
              </div>

              <button type="submit" id="submit-quote-btn" class="btn btn-primary btn-block" style="padding: 1rem; font-size: 1rem; margin-top: 0.5rem;">
                Book Free Consultation
              </button>

              <div class="hero-card-trust">
                <span>🔒 100% Privacy Protected · Zero Spam Calls · Callback within 2 hours</span>
              </div>

              <div class="hero-recent-preview">
                <img src="/assets/images/portfolio-kitchen.jpg" alt="Recent handover modular kitchen in GK-2" class="recent-thumb" width="52" height="52" loading="lazy">
                <div class="recent-info">
                  <span class="recent-title">📍 GK-II, South Delhi · Handed Over in 42 Days</span>
                  <span class="recent-desc">100% Factory BWP Marine Ply &amp; German Tandem Drawers</span>
                </div>
              </div>
            </div>

            <!-- Success State -->
            <div class="form-success-state" style="display: none; text-align: center; padding: 2rem 0;">
              <div style="font-size: 3rem; color: var(--color-green); margin-bottom: 0.5rem;">✓</div>
              <h3 style="color: var(--color-dark); margin-bottom: 0.5rem;">Thank you, <span class="client-name-display">there</span>!</h3>
              <p style="color: var(--color-muted); margin-bottom: 1.5rem;">Our lead designer will call you within 24 hours to schedule your free 3D design session.</p>
              <a href="#" class="btn btn-primary wa-direct-link" target="_blank" rel="noopener noreferrer">Send on WhatsApp</a>
            </div>
          </form>
        </div>

      </div>
    </section>'''

code = re.sub(old_hero_pattern, new_hero, code, count=1)

# 4. Ensure Calculator Result WhatsApp Button has id="calc-wa-btn"
old_calc_btn = 'class="btn btn-primary btn-block" style="padding: 1rem;" target="_blank" rel="noopener noreferrer">\n              Get Itemized Quotation on WhatsApp'
new_calc_btn = 'class="btn btn-primary btn-block" style="padding: 1rem;" target="_blank" rel="noopener noreferrer" id="calc-wa-btn">\n              Get Itemized Quotation on WhatsApp'

code = code.replace(old_calc_btn, new_calc_btn)

with open('scripts/build_home.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] scripts/build_home.py updated with refined Header, Mobile Drawer, Balanced Hero, and Calculator ID.')
