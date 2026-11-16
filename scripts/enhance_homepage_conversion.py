"""
Enhance homepage conversion:
Positioning Delhi Interior clearly as Turnkey Interior Designers & Master Carpenters
Maximizing lead generation, direct calls, and WhatsApp chats.
"""

with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Title and Meta Description for High-Intent Commercial Search
old_meta = '''  <title>Interior Designers in Delhi NCR | Delhi Interior — Home Styling &amp; Modular Studio</title>
  <meta name="description" content="Delhi Interior: Premier luxury interior designers &amp; modular studio in Delhi NCR. Bespoke modular kitchens, custom wardrobes, and turnkey homes with 10-year warranty. Book your free consultation.">'''

new_meta = '''  <title>Interior Designers & Master Carpenters in Delhi NCR | Delhi Interior — Direct Workshop Rates</title>
  <meta name="description" content="Delhi Interior: Turnkey Interior Designers & Master Carpenters in Delhi NCR. Modular kitchens, custom wardrobes, teak woodwork, false ceilings & full 2/3/4 BHK renovations at direct workshop rates. Free site visit & 10-yr warranty. Call 9643817099.">'''

text = text.replace(old_meta, new_meta)

# 2. Update Top Utility Bar
old_utility_left = '''      <div class="top-utility-left">
        <span class="badge-welcome">Welcome to Delhi Interior</span>
        <span>·</span>
        <span>Premier Interior Designers in Delhi NCR</span>
        <span>·</span>
        <span>Open 24 Hours</span>
      </div>'''

new_utility_left = '''      <div class="top-utility-left">
        <span class="badge-welcome">Welcome to Delhi Interior</span>
        <span>·</span>
        <span>Turnkey Interior Designers &amp; Master Carpenters</span>
        <span>·</span>
        <span>Direct Workshop Rates · Open 24 Hours</span>
      </div>'''

text = text.replace(old_utility_left, new_utility_left)

# 3. Update Hero Headline, Subhead, USPs and Form
old_hero_headline = '''        <!-- Left Column: Copy, USPs, & Consultation Booking -->
        <div class="hero-headline">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 1.2rem;">
            ✦ 10+ Years Crafting Luxury Homes · Delhi NCR
          </div>
          <h1>
            Complete Home Interiors &amp; <span class="highlight">Custom Woodwork</span><span class="logo-dot">.</span>
          </h1>
          <p class="hero-subhead">
            Factory-crafted modular kitchens, custom floor-to-ceiling wardrobes, and bespoke teak carpentry across South Delhi, Gurugram &amp; Noida. 45-day move-in guaranteed.
          </p>

          <!-- Core USPs -->
          <div class="hero-usps">
            <div class="hero-usp-item">
              <svg viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
              <span>45-Day Handover Guarantee</span>
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

          <!-- Integrated Consultation Card Left -->
          <div class="hero-consult-card-left" id="consultation-card">
            <div class="consult-title">
              <span>✦ Book Free Design Consultation</span>
            </div>
            <p class="consult-sub">Speak with our senior design director. Open 24 Hours for site queries.</p>

            <form id="quote-form" novalidate>
              <input type="text" name="honeypot" style="display:none" tabindex="-1">

              <div class="form-fields-container">
                <div class="form-row">
                  <div class="form-group">
                    <label for="client-name" class="form-label">Your Name *</label>
                    <input type="text" id="client-name" name="name" class="form-control" placeholder="Enter your full name" required>
                  </div>
                  <div class="form-group">
                    <label for="client-phone" class="form-label">Phone Number *</label>
                    <input type="tel" id="client-phone" name="phone" class="form-control" placeholder="+91 96438 17099" required>
                  </div>
                </div>

                <div class="form-row">
                  <div class="form-group">
                    <label for="service-type" class="form-label">Space Required</label>
                    <select id="service-type" name="service" class="form-control">
                      <option value="Modular Kitchen" selected>Modular Kitchen</option>
                      <option value="Wardrobes &amp; Bedrooms">Wardrobes &amp; Bedrooms</option>
                      <option value="Custom Woodwork &amp; Carpentry">Custom Woodwork &amp; Carpentry</option>
                      <option value="Full Home 2BHK">Full Home 2BHK Turnkey</option>
                      <option value="Full Home 3BHK">Full Home 3BHK Turnkey</option>
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

                <button type="submit" id="submit-quote-btn" class="btn btn-primary btn-block" style="padding: 0.95rem; font-size: 0.95rem; margin-top: 0.3rem;">
                  Book Free Consultation
                </button>

                <div class="hero-card-trust" style="margin-top: 0.6rem; font-size: 0.74rem;">
                  <span>🔒 100% Privacy Protected · Zero Spam Calls · Available 24/7</span>
                </div>
              </div>'''

new_hero_headline = '''        <!-- Left Column: Copy, USPs, & Consultation Booking -->
        <div class="hero-headline">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 1.2rem;">
            ✦ Direct Workshop Rates · Turnkey Interior Designers &amp; Master Carpenters
          </div>
          <h1>
            Interior Design &amp; <span class="highlight">Master Carpentry</span> Under One Roof<span class="logo-dot">.</span>
          </h1>
          <p class="hero-subhead">
            Looking for top-quality home interiors without aggregator middleman markups? We are turnkey interior designers &amp; hands-on master carpenters with our own Delhi workshop. From modular kitchens &amp; sliding wardrobes to bespoke teak woodwork &amp; full 2/3/4 BHK turnkey execution — get direct craftsman rates, 45-day handover, and a 10-year warranty.
          </p>

          <!-- Core USPs -->
          <div class="hero-usps">
            <div class="hero-usp-item">
              <svg viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
              <span>Direct Workshop Rates (Save 30–40%)</span>
            </div>
            <div class="hero-usp-item">
              <svg viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
              <span>In-House Master Carpenters &amp; Designers</span>
            </div>
            <div class="hero-usp-item">
              <svg viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
              <span>Free Site Visit &amp; 24-Hr Quote</span>
            </div>
            <div class="hero-usp-item">
              <svg viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
              <span>10-Year Comprehensive Warranty</span>
            </div>
          </div>

          <!-- Integrated Consultation Card Left -->
          <div class="hero-consult-card-left" id="consultation-card">
            <div class="consult-title">
              <span>✦ Book Free Site Visit &amp; Direct Estimate</span>
            </div>
            <p class="consult-sub">Our Master Designer &amp; Carpenter visits your site anywhere in Delhi NCR. Open 24 Hours.</p>

            <form id="quote-form" novalidate>
              <input type="text" name="honeypot" style="display:none" tabindex="-1">

              <div class="form-fields-container">
                <div class="form-row">
                  <div class="form-group">
                    <label for="client-name" class="form-label">Your Name *</label>
                    <input type="text" id="client-name" name="name" class="form-control" placeholder="Enter your full name" required>
                  </div>
                  <div class="form-group">
                    <label for="client-phone" class="form-label">Phone Number *</label>
                    <input type="tel" id="client-phone" name="phone" class="form-control" placeholder="+91 96438 17099" required>
                  </div>
                </div>

                <div class="form-row">
                  <div class="form-group">
                    <label for="service-type" class="form-label">Work Required *</label>
                    <select id="service-type" name="service" class="form-control">
                      <option value="Full Home 2BHK/3BHK/4BHK" selected>Full Home Turnkey (2/3/4 BHK / Villa)</option>
                      <option value="Custom Woodwork &amp; Carpentry">Custom Woodwork &amp; Carpentry (Mandir, Beds, Almirahs)</option>
                      <option value="Modular Kitchen">Modular Kitchen (Acrylic / PU / Quartz)</option>
                      <option value="Wardrobes &amp; Closets">Custom Sliding Wardrobes &amp; Walk-Ins</option>
                      <option value="Wall Paneling &amp; TV Units">Wall Paneling &amp; TV Units (Charcoal/Fluted)</option>
                      <option value="False Ceiling &amp; Lighting">False Ceiling &amp; Architectural Lighting</option>
                      <option value="Painting &amp; PU Polish">Painting &amp; PU / Duco Polish</option>
                      <option value="Doors &amp; Partitions">Doors, Partitions &amp; CNC Jalis</option>
                      <option value="Complete Renovation">Complete Renovation &amp; MEP Works</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="client-area" class="form-label">Locality / City *</label>
                    <input type="text" id="client-area" name="area" class="form-control" placeholder="e.g. South Delhi, Gurugram, Noida">
                  </div>
                </div>

                <button type="submit" id="submit-quote-btn" class="btn btn-primary btn-block" style="padding: 0.95rem; font-size: 0.95rem; margin-top: 0.3rem;">
                  Get Free Estimate &amp; Site Measurement
                </button>

                <div style="margin-top: 0.75rem; text-align: center; font-size: 0.86rem; color: #4B5563;">
                  Need an immediate estimate? <strong><a href="tel:+919643817099" style="color: #2563EB; text-decoration: none;">Call Directly: +91 96438 17099</a></strong>
                </div>

                <div class="hero-card-trust" style="margin-top: 0.5rem; font-size: 0.74rem;">
                  <span>🔒 Direct Craftsman Guarantee · Zero Spam · 100% Free Site Visit in Delhi NCR</span>
                </div>
              </div>'''

text = text.replace(old_hero_headline, new_hero_headline)

# 4. Add the Dedicated "Master Carpenter & Designer Advantage" Section right after Trust Strip
old_after_trust = '''    <!-- 2. TRUST METRIC STRIP -->
    <section class="trust-strip">
      <div class="container trust-strip-grid">
        <div class="trust-item">
          <h4>10<span>+ Years</span></h4>
          <p>Design &amp; Execution Excellence</p>
        </div>
        <div class="trust-item">
          <h4>500<span>+</span></h4>
          <p>Delivered Homes in Delhi NCR</p>
        </div>
        <div class="trust-item">
          <h4>45<span> Days</span></h4>
          <p>Move-In Delivery Guarantee</p>
        </div>
        <div class="trust-item">
          <h4>10<span> Years</span></h4>
          <p>Comprehensive Written Warranty</p>
        </div>
      </div>
    </section>'''

new_after_trust = '''    <!-- 2. TRUST METRIC STRIP -->
    <section class="trust-strip">
      <div class="container trust-strip-grid">
        <div class="trust-item">
          <h4>10<span>+ Years</span></h4>
          <p>Design &amp; Woodwork Excellence</p>
        </div>
        <div class="trust-item">
          <h4>500<span>+</span></h4>
          <p>Delivered Homes in Delhi NCR</p>
        </div>
        <div class="trust-item">
          <h4>45<span> Days</span></h4>
          <p>Move-In Delivery Guarantee</p>
        </div>
        <div class="trust-item">
          <h4>10<span> Years</span></h4>
          <p>Comprehensive Written Warranty</p>
        </div>
      </div>
    </section>

    <!-- 2.5 THE DIRECT MASTER CARPENTER & DESIGNER ADVANTAGE -->
    <section style="padding: 4rem 0 3.5rem; background: #FFFFFF; border-bottom: 1px solid var(--color-border);">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            ✦ The Craftsman Difference
          </div>
          <h2>Why Delhi Homeowners Choose Our Direct Studio<span class="logo-dot">.</span></h2>
          <p>We combine the spatial aesthetics of a luxury design studio with the hands-on precision and honest rates of master carpenters.</p>
        </div>

        <div class="craftsman-advantage-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 2.5rem;">
          <div style="background: #F9FAFB; border: 1.5px solid #E5E7EB; border-radius: var(--radius-lg); padding: 2.2rem 1.8rem; box-shadow: var(--shadow-sm);">
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
          </div>
        </div>
      </div>
    </section>'''

text = text.replace(old_after_trust, new_after_trust)

# 5. Add Direct Estimate Banner before Testimonials
old_before_reviews = '''    <!-- 12. REAL HOMES DELIVERED (CLIENT TESTIMONIALS) -->
    <section class="reviews-livspace-section">'''

new_before_reviews = '''    <!-- DIRECT ESTIMATE BANNER -->
    <section style="background: #111827; color: #FFFFFF; padding: 3.5rem 0; border-top: 3px solid #2563EB;">
      <div class="container" style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 2rem;">
        <div style="max-width: 650px;">
          <div class="pill-badge-red" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">✦ Instant Consultation</div>
          <h3 style="color: #FFFFFF; font-size: 1.8rem; font-weight: 800; margin-bottom: 0.6rem;">Planning an Interior or Carpentry Project in Delhi NCR?</h3>
          <p style="color: #D1D5DB; font-size: 1rem; line-height: 1.7; margin: 0;">Send us your room dimensions or floor plan on WhatsApp, or speak directly with our Master Contractor. We visit your site anywhere in Delhi NCR — 100% Free.</p>
        </div>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
          <a href="tel:+919643817099" class="btn btn-primary" style="padding: 0.9rem 1.8rem; font-size: 0.95rem;">📞 Call +91 96438 17099</a>
          <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+a+direct+estimate+for+my+home+interior+and+carpentry." class="btn btn-outline" style="border-color: #25D366; color: #25D366; padding: 0.9rem 1.8rem; font-size: 0.95rem;" target="_blank" rel="noopener noreferrer">💬 WhatsApp Floor Plan</a>
        </div>
      </div>
    </section>

    <!-- 12. REAL HOMES DELIVERED (CLIENT TESTIMONIALS) -->
    <section class="reviews-livspace-section">'''

text = text.replace(old_before_reviews, new_before_reviews)

# 6. Enhance Final CTA Banner
old_final_cta = '''    <!-- 14. HIGH-IMPACT FINAL CTA BANNER -->
    <section class="final-cta-section">
      <div class="container">
        <h2>Bring Home Interiors That Inspire You Every Day<span class="logo-dot">.</span></h2>
        <p>Book a free consultation and site layout review with our senior design team today.</p>
        <div class="cta-buttons">
          <a href="/contact/" class="btn btn-primary" style="padding: 1rem 2.5rem; font-size: 1.05rem;">
            Book Free Consultation
          </a>
          <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+design+consultation." class="btn btn-outline" style="border-color: #FFFFFF; color: #FFFFFF; padding: 1rem 2.2rem;" target="_blank" rel="noopener noreferrer">
            Chat on WhatsApp
          </a>
        </div>
      </div>
    </section>'''

new_final_cta = '''    <!-- 14. HIGH-IMPACT FINAL CTA BANNER -->
    <section class="final-cta-section">
      <div class="container">
        <h2>Ready to Start Your Interior or Carpentry Project?<span class="logo-dot">.</span></h2>
        <p>Book a free on-site measurement and direct consultation with our Master Designer &amp; Carpenter today. Zero obligation, honest craftsman rates.</p>
        <div class="cta-buttons" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="/contact/" class="btn btn-primary" style="padding: 1rem 2.5rem; font-size: 1.05rem;">
            Book Free Site Visit
          </a>
          <a href="tel:+919643817099" class="btn btn-secondary" style="background: #FFFFFF; color: #2563EB; font-weight: 700; padding: 1rem 2.2rem; text-decoration: none;">
            📞 Call +91 96438 17099
          </a>
          <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+design+and+carpentry+consultation." class="btn btn-outline" style="border-color: #FFFFFF; color: #FFFFFF; padding: 1rem 2.2rem;" target="_blank" rel="noopener noreferrer">
            Chat on WhatsApp
          </a>
        </div>
      </div>
    </section>'''

text = text.replace(old_final_cta, new_final_cta)

with open('scripts/rebuild_complete_site_v3.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("[SUCCESS] Enhanced scripts/rebuild_complete_site_v3.py for maximum lead generation and business conversion!")
