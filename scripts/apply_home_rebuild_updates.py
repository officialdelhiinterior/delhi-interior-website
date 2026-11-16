import re

with open('scripts/rebuild_complete_site_v3.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update top utility bar in rebuild_complete_site_v3.py
old_top_bar = '''  <!-- LEVEL 1: TOP UTILITY BAR (Home Styling by KD Signature Topbar) -->
  <div class="top-utility-bar">
    <div class="container top-utility-container">
      <div class="top-utility-left">
        <span class="badge-welcome">Welcome to Delhi Interior</span>
        <span>·</span>
        <span>Premier Interior Designers in Delhi NCR</span>
        <span>·</span>
        <span>🕒 Timing: Open 24 Hours (7 Days a Week)</span>
      </div>
      <div class="top-utility-right">
        <a href="tel:+919643817099" class="top-utility-link">
          <span>📞 Call 24/7: +91 96438 17099</span>
        </a>
        <div class="top-utility-social">
          <a href="https://instagram.com/delhiinterior" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
          </a>
          <a href="https://facebook.com/delhiinterior" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
          </a>
          <a href="https://youtube.com/delhiinterior" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg>
          </a>
        </div>
        <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+consult+for+my+home+interior." class="top-utility-link" target="_blank" rel="noopener noreferrer">
          <span>💬 WhatsApp Designer</span>
        </a>
      </div>
    </div>
  </div>'''

new_top_bar = '''  <!-- LEVEL 1: TOP UTILITY BAR -->
  <div class="top-utility-bar">
    <div class="container top-utility-container">
      <div class="top-utility-left">
        <span class="badge-welcome">Welcome to Delhi Interior</span>
        <span class="utility-sep">·</span>
        <span>Premier Interior Designers in Delhi NCR</span>
        <span class="utility-sep">·</span>
        <span class="utility-timing">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          Open 24 Hours (7 Days a Week)
        </span>
      </div>
      <div class="top-utility-right">
        <a href="tel:+919643817099" class="top-utility-link">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>Call 24/7: +91 96438 17099</span>
        </a>
        <div class="top-utility-social">
          <a href="https://instagram.com/delhiinterior" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
          </a>
          <a href="https://facebook.com/delhiinterior" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
          </a>
          <a href="https://youtube.com/delhiinterior" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg>
          </a>
        </div>
        <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+consult+for+my+home+interior." class="top-utility-link" target="_blank" rel="noopener noreferrer">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
          <span>WhatsApp Designer</span>
        </a>
      </div>
    </div>
  </div>'''

if old_top_bar in code:
    code = code.replace(old_top_bar, new_top_bar)
    print("Replaced top utility bar in rebuild_complete_site_v3.py")
else:
    print("Warning: old_top_bar not found in rebuild_complete_site_v3.py")

# 2. Update the Hero Section
# Look for the hero block
hero_pattern = re.compile(r'<!-- 1\. EDITORIAL SPLIT HERO -->\s*<section class="hero-livspace">.*?</section>', re.DOTALL)

new_hero_section = '''<!-- 1. EDITORIAL SPLIT HERO -->
    <section class="hero-livspace">
      <div class="container">
        <!-- Top 2-Column Showcase -->
        <div class="hero-layout">
          <!-- Left Column: Copy, USPs, & Direct Actions -->
          <div class="hero-headline">
            <div class="pill-badge pill-badge-red" style="margin-bottom: 1.2rem;">
              ✦ Direct Workshop Rates · Turnkey Interior Designers &amp; Master Carpenters
            </div>
            <h1>
              Interior Design &amp; <span class="highlight">Master Carpentry</span> Under One Roof
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

            <!-- Direct Action Buttons -->
            <div class="hero-cta-group">
              <a href="#consultation-card" class="btn btn-primary">Book Free Site Visit</a>
              <a href="/portfolio/" class="btn btn-outline">Explore Projects</a>
            </div>
          </div>

          <!-- Right Column: Breathtaking Architectural Photography Showcase -->
          <div class="hero-visual-showcase">
            <picture>
              <source srcset="/assets/images/hero-kitchen.webp" type="image/webp">
              <img src="/assets/images/hero-kitchen.jpg" alt="Luxury Modular Kitchen &amp; Living Room in Greater Kailash II by Delhi Interior" class="hero-main-photo" width="1200" height="825" loading="eager" fetchpriority="high">
            </picture>

            <!-- Floating Glassmorphic Badges -->
            <div class="hero-glass-badge hero-badge-location">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="color: #2563EB; flex-shrink: 0;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              <div>
                <strong>Greater Kailash II, South Delhi</strong>
                <span>4-BHK Turnkey Delivered in 42 Days</span>
              </div>
            </div>

            <div class="hero-glass-badge hero-badge-warranty">
              <span class="check-icon">✓</span>
              <div>
                <strong>10-Year Warranty</strong>
                <span>Certified BWP Marine Ply &amp; German Fittings</span>
              </div>
            </div>

            <div class="hero-glass-badge hero-badge-rating">
              <span class="stars">★★★★★</span>
              <strong>4.9 / 5 Rating</strong>
              <span>500+ Verified Delhi NCR Homes</span>
            </div>
          </div>
        </div>

        <!-- Docked Consultation Card (Sleek Horizontal Architectural Ribbon) -->
        <div class="hero-consult-card-dock" id="consultation-card">
          <div class="consult-dock-header">
            <div class="consult-title">
              <span>✦ Book Free Site Visit &amp; Direct Estimate</span>
            </div>
            <p class="consult-sub">Our Master Designer &amp; Carpenter visits your site anywhere in Delhi NCR. Open 24 Hours.</p>
          </div>

          <form id="quote-form" novalidate>
            <input type="text" name="honeypot" style="display:none" tabindex="-1">

            <div class="form-fields-container">
              <div class="consult-form-grid">
                <div class="form-group">
                  <label for="client-name" class="form-label">Your Name *</label>
                  <input type="text" id="client-name" name="name" class="form-control" placeholder="Enter your full name" required>
                </div>
                <div class="form-group">
                  <label for="client-phone" class="form-label">Phone Number *</label>
                  <input type="tel" id="client-phone" name="phone" class="form-control" placeholder="+91 96438 17099" required>
                </div>
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
                <div class="form-group form-submit-col">
                  <label class="form-label label-spacer">&nbsp;</label>
                  <button type="submit" id="submit-quote-btn" class="btn btn-primary btn-block">
                    Get Free Estimate
                  </button>
                </div>
              </div>

              <div class="consult-dock-footer">
                <div class="consult-direct-call">
                  Need an immediate estimate? <strong><a href="tel:+919643817099">Call Directly: +91 96438 17099</a></strong>
                </div>
                <div class="hero-card-trust">
                  <span>Direct Craftsman Guarantee · Zero Spam · 100% Free Site Visit in Delhi NCR</span>
                </div>
              </div>
            </div>

            <!-- Success State -->
            <div class="form-success-state" style="display: none; text-align: center; padding: 2rem 0;">
              <div style="font-size: 2.5rem; color: var(--color-green); margin-bottom: 0.4rem;">✓</div>
              <h3 style="color: var(--color-dark); margin-bottom: 0.3rem;">Thank you, <span class="client-name-display">there</span>!</h3>
              <p style="color: var(--color-muted); font-size: 0.95rem; margin-bottom: 1.2rem;">Our lead designer will connect with you within 2 hours to confirm your consultation.</p>
              <a href="#" class="btn btn-primary wa-direct-link" target="_blank" rel="noopener noreferrer">Send Details on WhatsApp</a>
            </div>
          </form>
        </div>

      </div>
    </section>'''

if hero_pattern.search(code):
    code = hero_pattern.sub(new_hero_section, code)
    print("Successfully replaced hero section in rebuild_complete_site_v3.py")
else:
    print("Warning: hero_pattern not matched in rebuild_complete_site_v3.py")

# 3. Clean up CTA section buttons (remove 📞 and 💬 emojis)
code = code.replace('>📞 Call +91 96438 17099<', '>Call +91 96438 17099<')
code = code.replace('>💬 WhatsApp +91 96438 17099<', '>WhatsApp +91 96438 17099<')

with open('scripts/rebuild_complete_site_v3.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated rebuild_complete_site_v3.py")
