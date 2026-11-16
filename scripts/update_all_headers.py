import re

# 1. Update scripts/build_main_and_utility.py
with open('scripts/build_main_and_utility.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_header_main = r'<header class="site-header" role="banner">[\s\S]*?</aside>'

new_header_main = '''<header class="site-header" role="banner">
    <div class="container nav-container">
      <a href="/" class="site-logo" aria-label="Delhi Interior Home">
        Delhi Interior<span class="logo-dot">.</span>
      </a>

      <nav class="main-navigation" aria-label="Main navigation">
        <ul class="nav-links">
          <li class="nav-dropdown-item">
            <a href="/modular-kitchen-delhi/" class="nav-dropdown-trigger {'active' if active_nav == 'services' else ''}">
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
          <li><a href="/#estimator">Cost Calculator</a></li>
          <li><a href="/portfolio/" class="{'active' if active_nav == 'portfolio' else ''}">Designs</a></li>
          <li><a href="/process/" class="{'active' if active_nav == 'process' else ''}">How It Works</a></li>
          <li><a href="/about/" class="{'active' if active_nav == 'about' else ''}">About</a></li>
          <li><a href="/contact/" class="{'active' if active_nav == 'contact' else ''}">Contact</a></li>
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
  </header>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-menu" class="mobile-menu-overlay" aria-modal="true" role="dialog">
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
        <li><a href="/#estimator" onclick="closeMobileMenu()">📊 Cost Calculator</a></li>
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
  </div>

  <!-- Floating WhatsApp -->
  <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+consultation." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.43.1-.12.19-.48.61-.59.73-.11.12-.22.14-.41.05-.19-.09-.8-.29-1.53-.94-.57-.51-.95-1.13-1.06-1.32-.11-.19-.01-.3.08-.39.09-.08.19-.22.29-.33.09-.11.12-.19.19-.31.06-.12.03-.24-.01-.33-.05-.09-.43-1.04-.6-1.42-.16-.38-.32-.33-.44-.33h-.37c-.13 0-.34.05-.52.24-.18.19-.69.67-.69 1.64s.71 1.9 1.01 2.3c.3.4 1.92 2.93 4.65 4.11.65.28 1.16.45 1.55.58.65.21 1.25.18 1.72.11.53-.08 1.62-.66 1.85-1.3.23-.64.23-1.19.16-1.3-.06-.11-.23-.18-.42-.27z"/></svg>
    <span class="whatsapp-tooltip">Chat with a Designer</span>
  </a>

  <!-- Mobile Sticky Bottom CTA -->
  <aside class="sticky-mobile-cta" aria-label="Mobile quick actions">
    <div class="cta-btn-group">
      <a href="tel:+919811000000" class="cta-btn btn-call">Call Designer</a>
      <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+want+a+quote." class="cta-btn btn-wa" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
  </aside>'''

text = re.sub(old_header_main, new_header_main, text, count=1)
with open('scripts/build_main_and_utility.py', 'w', encoding='utf-8') as f:
    f.write(text)
print('[SUCCESS] scripts/build_main_and_utility.py updated with Services Dropdown and Categorized Mobile Drawer.')

# 2. Update scripts/update_build_services.py
with open('scripts/update_build_services.py', 'r', encoding='utf-8') as f:
    text_s = f.read()

old_header_svc = r'<header class="site-header" role="banner">[\s\S]*?</aside>'

new_header_svc = '''<header class="site-header" role="banner">
    <div class="container nav-container">
      <a href="/" class="site-logo" aria-label="Delhi Interior Home">
        Delhi Interior<span class="logo-dot">.</span>
      </a>

      <nav class="main-navigation" aria-label="Main navigation">
        <ul class="nav-links">
          <li class="nav-dropdown-item">
            <a href="/modular-kitchen-delhi/" class="nav-dropdown-trigger active">
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
          <li><a href="/#estimator">Cost Calculator</a></li>
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
  </header>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-menu" class="mobile-menu-overlay" aria-modal="true" role="dialog">
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
        <li><a href="/#estimator" onclick="closeMobileMenu()">📊 Cost Calculator</a></li>
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
  </div>

  <!-- Floating WhatsApp -->
  <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+want+to+enquire+about+{s['slug']}." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.43.1-.12.19-.48.61-.59.73-.11.12-.22.14-.41.05-.19-.09-.8-.29-1.53-.94-.57-.51-.95-1.13-1.06-1.32-.11-.19-.01-.3.08-.39.09-.08.19-.22.29-.33.09-.11.12-.19.19-.31.06-.12.03-.24-.01-.33-.05-.09-.43-1.04-.6-1.42-.16-.38-.32-.33-.44-.33h-.37c-.13 0-.34.05-.52.24-.18.19-.69.67-.69 1.64s.71 1.9 1.01 2.3c.3.4 1.92 2.93 4.65 4.11.65.28 1.16.45 1.55.58.65.21 1.25.18 1.72.11.53-.08 1.62-.66 1.85-1.3.23-.64.23-1.19.16-1.3-.06-.11-.23-.18-.42-.27z"/></svg>
    <span class="whatsapp-tooltip">Chat with a Designer</span>
  </a>

  <!-- Mobile Sticky Bottom CTA -->
  <aside class="sticky-mobile-cta" aria-label="Mobile quick actions">
    <div class="cta-btn-group">
      <a href="tel:+919811000000" class="cta-btn btn-call">Call Designer</a>
      <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+want+a+quote+for+{s['slug']}." class="cta-btn btn-wa" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
  </aside>'''

text_s = re.sub(old_header_svc, new_header_svc, text_s, count=1)
with open('scripts/update_build_services.py', 'w', encoding='utf-8') as f:
    f.write(text_s)
print('[SUCCESS] scripts/update_build_services.py updated with Services Dropdown and Categorized Mobile Drawer.')
