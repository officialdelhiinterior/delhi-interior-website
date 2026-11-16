import re

# Update build_main_and_utility.py
with open('scripts/build_main_and_utility.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace get_header function
old_get_header_pattern = r'def get_header\(active_nav="", is_light_page=False, title="", desc="", canonical="", schema=None\):[\s\S]*?<!-- Mobile Sticky Bottom CTA -->[\s\S]*?</aside>'

new_get_header = '''def get_header(active_nav="", is_light_page=False, title="", desc="", canonical="", schema=None):
    schema_script = f\'\'\'<script type="application/ld+json">
{json.dumps(schema, indent=2)}
</script>\'\'\' if schema else ''

    return f\'\'\'<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://delhiinterior.com/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_IN">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://delhiinterior.com/og-image.jpg">

  <!-- Favicons -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon-32x32.png" type="image/png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <!-- Typography: Plus Jakarta Sans & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/assets/css/style.css">
  {schema_script}
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- LEVEL 1: TOP UTILITY BAR (Home Styling by KD Signature Topbar) -->
  <div class="top-utility-bar">
    <div class="container top-utility-container">
      <div class="top-utility-left">
        <span class="badge-welcome">Welcome to Delhi Interior</span>
        <span>·</span>
        <span>Premier Interior Designers in Delhi NCR</span>
        <span>·</span>
        <span>Mon–Sat: 9:00 AM – 7:00 PM</span>
      </div>
      <div class="top-utility-right">
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
        <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+want+to+consult+for+my+home+interior." class="top-utility-link" target="_blank" rel="noopener noreferrer">
          <span>💬 WhatsApp Designer</span>
        </a>
      </div>
    </div>
  </div>

  <!-- LEVEL 2: MAIN BRAND & NAVIGATION BAR -->
  <header class="site-header" role="banner">
    <div class="container nav-container">
      <a href="/" class="site-logo" aria-label="Delhi Interior Home">
        Delhi Interior<span class="logo-dot">.</span>
      </a>

      <nav class="main-navigation" aria-label="Main navigation">
        <ul class="nav-links">
          <li><a href="/" class="{'active' if active_nav == 'home' else ''}">Home</a></li>
          <li><a href="/about/" class="{'active' if active_nav == 'about' else ''}">About Us</a></li>
          <li><a href="/portfolio/" class="{'active' if active_nav == 'portfolio' else ''}">Projects</a></li>
          <li class="nav-dropdown-item">
            <a href="/modular-kitchen-delhi/" class="nav-dropdown-trigger {'active' if active_nav == 'services' else ''}">
              Services <span class="dropdown-chevron">▼</span>
            </a>
            <div class="nav-dropdown-menu" role="menu">
              <a href="/full-home-interior-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Residential Interior Design</strong>
                  <span>Full Home 2/3/4 BHK &amp; Villas</span>
                </div>
              </a>
              <a href="/modular-kitchen-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-8z"/><path d="M4 11V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"/><circle cx="7.5" cy="8" r="1"/><circle cx="16.5" cy="8" r="1"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Modular Kitchens</strong>
                  <span>Acrylic, PU &amp; Quartz Worktops</span>
                </div>
              </a>
              <a href="/wardrobe-design-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 3v18"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Custom Wardrobes</strong>
                  <span>Sliding, Walk-in &amp; Lofts</span>
                </div>
              </a>
              <a href="/wall-paneling-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="8" y1="3" x2="8" y2="21"/><line x1="12" y1="3" x2="12" y2="21"/><line x1="16" y1="3" x2="16" y2="21"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Wall Paneling &amp; TV Units</strong>
                  <span>Charcoal Louvers &amp; Fluted Slats</span>
                </div>
              </a>
              <a href="/false-ceiling-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><line x1="2" y1="4" x2="22" y2="4"/><path d="M7 4v4a5 5 0 0 0 10 0V4"/><line x1="12" y1="13" x2="12" y2="17"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>False Ceiling &amp; Lighting</strong>
                  <span>Gypsum, Cove &amp; Track Lights</span>
                </div>
              </a>
              <a href="/doors-partitions-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 20V6a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v14"/><path d="M2 20h20"/><circle cx="14" cy="12" r="1"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Doors &amp; Partitions</strong>
                  <span>Fluted Glass &amp; CNC Backlit Jali</span>
                </div>
              </a>
              <a href="/bedroom-furniture-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 18v3"/><path d="M20 18v3"/><path d="M19 11v7H5v-7"/><path d="M19 11a3 3 0 0 0-3-3H8a3 3 0 0 0-3 3"/><path d="M3 14h18"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Study Desks &amp; Storage</strong>
                  <span>Workstations &amp; Teak Mandirs</span>
                </div>
              </a>
              <a href="/painting-polishing-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18.37 2.63L14 7l3 3 4.37-4.37a2.12 2.12 0 1 0-3-3z"/><path d="M14 7l-9 9v4h4l9-9"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Painting &amp; PU Polish</strong>
                  <span>Asian Paints Royale, PU &amp; Duco</span>
                </div>
              </a>
              <a href="/plumbing-electrical-delhi/" class="dropdown-link" role="menuitem" style="grid-column: span 2;">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Plumbing &amp; Electrical MEP</strong>
                  <span>Concealed Piping, 4mm Fire-Proof Wiring &amp; Sanitaryware</span>
                </div>
              </a>
            </div>
          </li>
          <li><a href="/#estimator">Cost Calculator</a></li>
          <li><a href="/blog/" class="{'active' if active_nav == 'blog' else ''}">Blogs</a></li>
          <li><a href="/contact/" class="{'active' if active_nav == 'contact' else ''}">Contact Us</a></li>
        </ul>
      </nav>

      <div class="nav-right">
        <a href="/contact/" class="btn btn-primary">Book Consultation</a>
        <button class="hamburger" aria-label="Open menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- LEVEL 3: UNDER-NAV CONTACT TRUST BAR -->
  <div class="under-nav-bar">
    <div class="container under-nav-grid">
      <!-- 1. Office Address -->
      <a href="https://maps.google.com/?q=Ring+Road+South+Extension+Part+II+New+Delhi" class="under-nav-item" target="_blank" rel="noopener noreferrer">
        <div class="under-nav-icon">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        </div>
        <div class="under-nav-text">
          <h6>Office &amp; Experience Centre</h6>
          <p>Ring Road, South Extension Part II, New Delhi</p>
        </div>
      </a>

      <!-- 2. Email Us -->
      <a href="mailto:hello@delhiinterior.com" class="under-nav-item">
        <div class="under-nav-icon">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        </div>
        <div class="under-nav-text">
          <h6>Email Us Directly</h6>
          <p>hello@delhiinterior.com</p>
        </div>
      </a>

      <!-- 3. Call Us -->
      <a href="tel:+919811000000" class="under-nav-item">
        <div class="under-nav-icon">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        </div>
        <div class="under-nav-text">
          <h6>Call Us (9 AM – 7 PM)</h6>
          <p>+91 98110 00000</p>
        </div>
      </a>
    </div>
  </div>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-menu" class="mobile-menu-overlay" aria-modal="true" role="dialog">
    <div class="mobile-menu-header">
      <div class="site-logo">Delhi Interior<span class="logo-dot">.</span></div>
      <button class="mobile-menu-close" aria-label="Close menu">✕</button>
    </div>
    <div class="mobile-menu-content" style="padding: 1.5rem; overflow-y: auto;">
      <div class="mobile-menu-section-title">Navigation</div>
      <ul class="mobile-nav-links" style="list-style: none; display: flex; flex-direction: column; gap: 0.85rem; margin-bottom: 1.5rem;">
        <li><a href="/" onclick="closeMobileMenu()">🏠 Home</a></li>
        <li><a href="/about/" onclick="closeMobileMenu()">ℹ️ About Our Studio</a></li>
        <li><a href="/portfolio/" onclick="closeMobileMenu()">🖼️ Projects &amp; Portfolio</a></li>
        <li><a href="/#estimator" onclick="closeMobileMenu()">📊 Cost Calculator</a></li>
        <li><a href="/process/" onclick="closeMobileMenu()">⚡ How It Works (45 Days)</a></li>
        <li><a href="/blog/" onclick="closeMobileMenu()">📝 Blogs &amp; Design Guides</a></li>
        <li><a href="/contact/" onclick="closeMobileMenu()">📍 Contact Us</a></li>
      </ul>

      <div class="mobile-menu-section-title">Our Services</div>
      <ul class="mobile-nav-services">
        <li><a href="/full-home-interior-delhi/" onclick="closeMobileMenu()">🏡 Residential Interiors</a></li>
        <li><a href="/modular-kitchen-delhi/" onclick="closeMobileMenu()">🍳 Modular Kitchens</a></li>
        <li><a href="/wardrobe-design-delhi/" onclick="closeMobileMenu()">🚪 Custom Wardrobes</a></li>
        <li><a href="/wall-paneling-delhi/" onclick="closeMobileMenu()">📺 Wall Paneling &amp; Louvers</a></li>
        <li><a href="/false-ceiling-delhi/" onclick="closeMobileMenu()">💡 False Ceiling &amp; Lights</a></li>
        <li><a href="/doors-partitions-delhi/" onclick="closeMobileMenu()">🏛️ Doors &amp; Partitions</a></li>
        <li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">📚 Custom Furniture &amp; Study</a></li>
        <li><a href="/painting-polishing-delhi/" onclick="closeMobileMenu()">🎨 Painting &amp; PU Polish</a></li>
        <li><a href="/plumbing-electrical-delhi/" onclick="closeMobileMenu()">⚡ Plumbing &amp; Electrical MEP</a></li>
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
  </aside>\'\'\''''

text = re.sub(old_get_header_pattern, new_get_header, text, count=1)
with open('scripts/build_main_and_utility.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("[SUCCESS] Updated scripts/build_main_and_utility.py")

# Update update_build_services.py
with open('scripts/update_build_services.py', 'r', encoding='utf-8') as f:
    text_s = f.read()

old_service_header_pattern = r'<!-- Top Announcement Bar -->[\s\S]*?<!-- Mobile Sticky Bottom CTA -->[\s\S]*?</aside>'

new_service_header = '''<!-- LEVEL 1: TOP UTILITY BAR (Home Styling by KD Signature Topbar) -->
  <div class="top-utility-bar">
    <div class="container top-utility-container">
      <div class="top-utility-left">
        <span class="badge-welcome">Welcome to Delhi Interior</span>
        <span>·</span>
        <span>Premier Interior Designers in Delhi NCR</span>
        <span>·</span>
        <span>Mon–Sat: 9:00 AM – 7:00 PM</span>
      </div>
      <div class="top-utility-right">
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
        <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+want+to+consult+for+my+home+interior." class="top-utility-link" target="_blank" rel="noopener noreferrer">
          <span>💬 WhatsApp Designer</span>
        </a>
      </div>
    </div>
  </div>

  <!-- LEVEL 2: MAIN BRAND & NAVIGATION BAR -->
  <header class="site-header" role="banner">
    <div class="container nav-container">
      <a href="/" class="site-logo" aria-label="Delhi Interior Home">
        Delhi Interior<span class="logo-dot">.</span>
      </a>

      <nav class="main-navigation" aria-label="Main navigation">
        <ul class="nav-links">
          <li><a href="/">Home</a></li>
          <li><a href="/about/">About Us</a></li>
          <li><a href="/portfolio/">Projects</a></li>
          <li class="nav-dropdown-item">
            <a href="/modular-kitchen-delhi/" class="nav-dropdown-trigger active">
              Services <span class="dropdown-chevron">▼</span>
            </a>
            <div class="nav-dropdown-menu" role="menu">
              <a href="/full-home-interior-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Residential Interior Design</strong>
                  <span>Full Home 2/3/4 BHK &amp; Villas</span>
                </div>
              </a>
              <a href="/modular-kitchen-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-8z"/><path d="M4 11V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"/><circle cx="7.5" cy="8" r="1"/><circle cx="16.5" cy="8" r="1"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Modular Kitchens</strong>
                  <span>Acrylic, PU &amp; Quartz Worktops</span>
                </div>
              </a>
              <a href="/wardrobe-design-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 3v18"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Custom Wardrobes</strong>
                  <span>Sliding, Walk-in &amp; Lofts</span>
                </div>
              </a>
              <a href="/wall-paneling-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="8" y1="3" x2="8" y2="21"/><line x1="12" y1="3" x2="12" y2="21"/><line x1="16" y1="3" x2="16" y2="21"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Wall Paneling &amp; TV Units</strong>
                  <span>Charcoal Louvers &amp; Fluted Slats</span>
                </div>
              </a>
              <a href="/false-ceiling-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><line x1="2" y1="4" x2="22" y2="4"/><path d="M7 4v4a5 5 0 0 0 10 0V4"/><line x1="12" y1="13" x2="12" y2="17"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>False Ceiling &amp; Lighting</strong>
                  <span>Gypsum, Cove &amp; Track Lights</span>
                </div>
              </a>
              <a href="/doors-partitions-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 20V6a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v14"/><path d="M2 20h20"/><circle cx="14" cy="12" r="1"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Doors &amp; Partitions</strong>
                  <span>Fluted Glass &amp; CNC Backlit Jali</span>
                </div>
              </a>
              <a href="/bedroom-furniture-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 18v3"/><path d="M20 18v3"/><path d="M19 11v7H5v-7"/><path d="M19 11a3 3 0 0 0-3-3H8a3 3 0 0 0-3 3"/><path d="M3 14h18"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Study Desks &amp; Storage</strong>
                  <span>Workstations &amp; Teak Mandirs</span>
                </div>
              </a>
              <a href="/painting-polishing-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18.37 2.63L14 7l3 3 4.37-4.37a2.12 2.12 0 1 0-3-3z"/><path d="M14 7l-9 9v4h4l9-9"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Painting &amp; PU Polish</strong>
                  <span>Asian Paints Royale, PU &amp; Duco</span>
                </div>
              </a>
              <a href="/plumbing-electrical-delhi/" class="dropdown-link" role="menuitem" style="grid-column: span 2;">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Plumbing &amp; Electrical MEP</strong>
                  <span>Concealed Piping, 4mm Fire-Proof Wiring &amp; Sanitaryware</span>
                </div>
              </a>
            </div>
          </li>
          <li><a href="/#estimator">Cost Calculator</a></li>
          <li><a href="/blog/">Blogs</a></li>
          <li><a href="/contact/">Contact Us</a></li>
        </ul>
      </nav>

      <div class="nav-right">
        <a href="/contact/" class="btn btn-primary">Book Consultation</a>
        <button class="hamburger" aria-label="Open menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- LEVEL 3: UNDER-NAV CONTACT TRUST BAR -->
  <div class="under-nav-bar">
    <div class="container under-nav-grid">
      <!-- 1. Office Address -->
      <a href="https://maps.google.com/?q=Ring+Road+South+Extension+Part+II+New+Delhi" class="under-nav-item" target="_blank" rel="noopener noreferrer">
        <div class="under-nav-icon">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        </div>
        <div class="under-nav-text">
          <h6>Office &amp; Experience Centre</h6>
          <p>Ring Road, South Extension Part II, New Delhi</p>
        </div>
      </a>

      <!-- 2. Email Us -->
      <a href="mailto:hello@delhiinterior.com" class="under-nav-item">
        <div class="under-nav-icon">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        </div>
        <div class="under-nav-text">
          <h6>Email Us Directly</h6>
          <p>hello@delhiinterior.com</p>
        </div>
      </a>

      <!-- 3. Call Us -->
      <a href="tel:+919811000000" class="under-nav-item">
        <div class="under-nav-icon">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        </div>
        <div class="under-nav-text">
          <h6>Call Us (9 AM – 7 PM)</h6>
          <p>+91 98110 00000</p>
        </div>
      </a>
    </div>
  </div>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-menu" class="mobile-menu-overlay" aria-modal="true" role="dialog">
    <div class="mobile-menu-header">
      <div class="site-logo">Delhi Interior<span class="logo-dot">.</span></div>
      <button class="mobile-menu-close" aria-label="Close menu">✕</button>
    </div>
    <div class="mobile-menu-content" style="padding: 1.5rem; overflow-y: auto;">
      <div class="mobile-menu-section-title">Navigation</div>
      <ul class="mobile-nav-links" style="list-style: none; display: flex; flex-direction: column; gap: 0.85rem; margin-bottom: 1.5rem;">
        <li><a href="/" onclick="closeMobileMenu()">🏠 Home</a></li>
        <li><a href="/about/" onclick="closeMobileMenu()">ℹ️ About Our Studio</a></li>
        <li><a href="/portfolio/" onclick="closeMobileMenu()">🖼️ Projects &amp; Portfolio</a></li>
        <li><a href="/#estimator" onclick="closeMobileMenu()">📊 Cost Calculator</a></li>
        <li><a href="/process/" onclick="closeMobileMenu()">⚡ How It Works (45 Days)</a></li>
        <li><a href="/blog/" onclick="closeMobileMenu()">📝 Blogs &amp; Design Guides</a></li>
        <li><a href="/contact/" onclick="closeMobileMenu()">📍 Contact Us</a></li>
      </ul>

      <div class="mobile-menu-section-title">Our Services</div>
      <ul class="mobile-nav-services">
        <li><a href="/full-home-interior-delhi/" onclick="closeMobileMenu()">🏡 Residential Interiors</a></li>
        <li><a href="/modular-kitchen-delhi/" onclick="closeMobileMenu()">🍳 Modular Kitchens</a></li>
        <li><a href="/wardrobe-design-delhi/" onclick="closeMobileMenu()">🚪 Custom Wardrobes</a></li>
        <li><a href="/wall-paneling-delhi/" onclick="closeMobileMenu()">📺 Wall Paneling &amp; Louvers</a></li>
        <li><a href="/false-ceiling-delhi/" onclick="closeMobileMenu()">💡 False Ceiling &amp; Lights</a></li>
        <li><a href="/doors-partitions-delhi/" onclick="closeMobileMenu()">🏛️ Doors &amp; Partitions</a></li>
        <li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">📚 Custom Furniture &amp; Study</a></li>
        <li><a href="/painting-polishing-delhi/" onclick="closeMobileMenu()">🎨 Painting &amp; PU Polish</a></li>
        <li><a href="/plumbing-electrical-delhi/" onclick="closeMobileMenu()">⚡ Plumbing &amp; Electrical MEP</a></li>
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

text_s = re.sub(old_service_header_pattern, new_service_header, text_s, count=1)
with open('scripts/update_build_services.py', 'w', encoding='utf-8') as f:
    f.write(text_s)
print("[SUCCESS] Updated scripts/update_build_services.py")
