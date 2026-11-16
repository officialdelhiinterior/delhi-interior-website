import os, json

# Common HTML Header & Footer Builders (Livspace Style)
def get_header(active_nav="", is_light_page=False, title="", desc="", canonical="", schema=None):
    schema_script = f'''<script type="application/ld+json">
{json.dumps(schema, indent=2)}
</script>''' if schema else ''

    return f'''<!DOCTYPE html>
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
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/assets/css/style.css?v=3.0">
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
        <span class="utility-timing"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> Open 24 Hours (7 Days a Week)</span>
      </div>
      <div class="top-utility-right">
        <a href="tel:+919643817099" class="top-utility-link">
          <span class="utility-call"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> Call 24/7: +91 96438 17099</span>
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
          <span class="utility-wa"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg> WhatsApp Designer</span>
        </a>
      </div>
    </div>
  </div>

  <!-- LEVEL 2: MAIN BRAND & NAVIGATION BAR -->
  <header class="site-header" role="banner">
    <div class="container nav-container">
      <a href="/" class="site-logo" aria-label="Delhi Interior Home">
        <img src="/assets/images/logo.png" alt="Delhi Interior" width="168" height="52" class="brand-logo-img">
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
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Custom Woodwork &amp; Carpentry</strong>
                  <span>Teak Mandirs, Beds, Desks &amp; Millwork</span>
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

  <!-- Mobile Drawer Menu -->
  <div id="mobile-menu" class="mobile-menu-overlay" aria-modal="true" role="dialog">
    <div class="mobile-menu-header">
      <div class="site-logo">
        <img src="/assets/images/logo.png" alt="Delhi Interior" width="150" height="46" class="brand-logo-img">
      </div>
      <button class="mobile-menu-close" aria-label="Close menu">✕</button>
    </div>
    <div class="mobile-menu-content" style="padding: 1.5rem; overflow-y: auto;">
      <div class="mobile-menu-section-title">Navigation</div>
      <ul class="mobile-nav-links" style="list-style: none; display: flex; flex-direction: column; gap: 0.85rem; margin-bottom: 1.5rem;">
        <li><a href="/" onclick="closeMobileMenu()">Home</a></li>
        <li><a href="/about/" onclick="closeMobileMenu()">About Our Studio</a></li>
        <li><a href="/portfolio/" onclick="closeMobileMenu()">Projects &amp; Portfolio</a></li>
        <li><a href="/process/" onclick="closeMobileMenu()">How It Works</a></li>
        <li><a href="/blog/" onclick="closeMobileMenu()">Blogs &amp; Design Guides</a></li>
        <li><a href="/contact/" onclick="closeMobileMenu()">Contact Us</a></li>
      </ul>

      <div class="mobile-menu-section-title">Our Services</div>
      <ul class="mobile-nav-services">
        <li><a href="/full-home-interior-delhi/" onclick="closeMobileMenu()">Residential Interiors (2/3/4 BHK)</a></li>
        <li><a href="/modular-kitchen-delhi/" onclick="closeMobileMenu()">Modular Kitchens</a></li>
        <li><a href="/wardrobe-design-delhi/" onclick="closeMobileMenu()">Custom Wardrobes</a></li>
        <li><a href="/wall-paneling-delhi/" onclick="closeMobileMenu()">Wall Paneling &amp; Louvers</a></li>
        <li><a href="/false-ceiling-delhi/" onclick="closeMobileMenu()">False Ceiling &amp; Lighting</a></li>
        <li><a href="/doors-partitions-delhi/" onclick="closeMobileMenu()">Doors &amp; Partitions</a></li>
        <li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">Custom Woodwork &amp; Carpentry</a></li>
        <li><a href="/painting-polishing-delhi/" onclick="closeMobileMenu()">Painting &amp; PU Polish</a></li>
        <li><a href="/plumbing-electrical-delhi/" onclick="closeMobileMenu()">Plumbing &amp; Electrical MEP</a></li>
      </ul>
    </div>
    <div class="mobile-menu-footer">
      <p style="font-size: 0.85rem; color: #6B7280; margin-bottom: 1rem;">F-128/4, Mohammadpur, New Delhi 110066<br>Open 24 Hours</p>
      <a href="tel:+919643817099" class="btn btn-primary btn-block">Call +91 96438 17099</a>
    </div>
  </div>

    <!-- Floating Contact Actions (Call above WhatsApp) -->
  <div class="floating-actions-container" aria-label="Direct studio contacts">
    <!-- Call Button (Above) -->
    <a href="tel:+919643817099" class="call-float" aria-label="Call Delhi Interior 24/7">
      <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">
        <path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
      </svg>
      <span class="call-tooltip">Call +91 96438 17099 (24/7)</span>
    </a>

    <!-- WhatsApp Button (Below Call Button) -->
    <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+consultation." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp 24/7">
      <svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor">
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
      </svg>
      <span class="whatsapp-tooltip">Chat on WhatsApp (24/7)</span>
    </a>
  </div>

  <!-- Mobile Sticky Bottom CTA -->
  <aside class="sticky-mobile-cta" aria-label="Mobile quick actions">
    <div class="cta-btn-group">
      <a href="tel:+919643817099" class="cta-btn btn-call">Call Designer</a>
      <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+a+quote." class="cta-btn btn-wa" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
  </aside>'''

def get_footer():
    return '''  <!-- Modern Livspace Footer -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <a href="/" class="footer-logo-card" aria-label="Delhi Interior Home">
            <img src="/assets/images/logo.png" alt="Delhi Interior" width="165" height="52" class="brand-logo-img">
          </a>
          <p>Delhi NCR's premier interior and custom woodwork studio. Delivering precision modular kitchens, bespoke teak carpentry, and turnkey home transformations crafted by master artisans.</p>
          <div style="display: flex; gap: 0.75rem; margin-top: 1.2rem; font-size: 0.85rem;">
            <a href="https://instagram.com/delhiinterior" style="color: #9CA3AF;" aria-label="Instagram">Instagram</a> ·
            <a href="https://facebook.com/delhiinterior" style="color: #9CA3AF;" aria-label="Facebook">Facebook</a> ·
            <a href="https://youtube.com/delhiinterior" style="color: #9CA3AF;" aria-label="YouTube">YouTube</a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Our Services</h4>
          <ul class="footer-links">
            <li><a href="/modular-kitchen-delhi/">Modular Kitchens</a></li>
            <li><a href="/wardrobe-design-delhi/">Custom Wardrobes</a></li>
            <li><a href="/bedroom-furniture-delhi/">Custom Woodwork &amp; Carpentry</a></li>
            <li><a href="/wall-paneling-delhi/">Wall Paneling &amp; TV Units</a></li>
            <li><a href="/false-ceiling-delhi/">False Ceilings &amp; Lighting</a></li>
            <li><a href="/full-home-interior-delhi/">Full Home Turnkey Interiors</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Company</h4>
          <ul class="footer-links">
            <li><a href="/about/">About Us</a></li>
            <li><a href="/portfolio/">Design Portfolio</a></li>
            <li><a href="/process/">How It Works</a></li>
            <li><a href="/blog/">Interior Guides &amp; Blog</a></li>
            <li><a href="/contact/">Contact &amp; Site Visit</a></li>
            <li><a href="/sitemap/">Sitemap</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Studio Location</h4>
          <p>F-128/4, Mohammadpur,<br>New Delhi, Delhi 110066</p>
          <p><strong>Phone:</strong> <a href="tel:+919643817099" style="color: #FFFFFF;">+91 96438 17099</a></p>
          <p><strong>WhatsApp:</strong> <a href="https://wa.me/919643817099" style="color: #FFFFFF;" target="_blank" rel="noopener noreferrer">+91 96438 17099</a></p>
          <p>Open 24 Hours (7 Days a Week)</p>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span id="year">2025</span> Delhi Interior. All rights reserved.</p>
        <div class="footer-legal">
          <a href="/privacy-policy/">Privacy Policy</a>
          <a href="/terms-of-service/">Terms of Service</a>
          <a href="/sitemap/">HTML Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Floating Call Button (24/7) -->
  <a href="tel:+919643817099" class="call-float" aria-label="Call Delhi Interior">
    <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    <span class="call-tooltip">Call +91 96438 17099 (24/7)</span>
  </a>

  <!-- Floating WhatsApp (24/7) -->
  <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+consultation." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.43.1-.12.19-.48.61-.59.73-.11.12-.22.14-.41.05-.19-.09-.8-.29-1.53-.94-.57-.51-.95-1.13-1.06-1.32-.11-.19-.01-.3.08-.39.09-.08.19-.22.29-.33.09-.11.12-.19.19-.31.06-.12.03-.24-.01-.33-.05-.09-.43-1.04-.6-1.42-.16-.38-.32-.33-.44-.33h-.37c-.13 0-.34.05-.52.24-.18.19-.69.67-.69 1.64s.71 1.9 1.01 2.3c.3.4 1.92 2.93 4.65 4.11.65.28 1.16.45 1.55.58.65.21 1.25.18 1.72.11.53-.08 1.62-.66 1.85-1.3.23-.64.23-1.19.16-1.3-.06-.11-.23-.18-.42-.27z"/></svg>
    <span class="whatsapp-tooltip">Chat on WhatsApp (24/7)</span>
  </a>

  <!-- Mobile Sticky Bottom CTA -->
  <aside class="sticky-mobile-cta" aria-label="Mobile quick actions">
    <div class="cta-btn-group">
      <a href="tel:+919643817099" class="cta-btn btn-call">Call Designer</a>
      <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+a+quote." class="cta-btn btn-wa" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
  </aside>

  <script defer src="/assets/js/main.js"></script>
  <script defer src="/assets/js/form.js"></script>
</body>
</html>'''

# ==============================================================================
# 1. PORTFOLIO PAGE (/portfolio/)
# ==============================================================================
portfolio_schema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Portfolio', 'item': 'https://delhiinterior.com/portfolio/'}
    ]
}

portfolio_items = [
    ('/assets/images/portfolio-kitchen.webp', 'kitchen', 'The Sterling Kitchen', 'Greater Kailash II', 'Matte acrylic shutters with Calacatta quartz island'),
    ('/assets/images/portfolio-bedroom.webp', 'bedroom', 'Master Suite Wardrobe', 'Panchsheel Park', 'Bronze glass sliding shutters with LED profile rails'),
    ('/assets/images/portfolio-tvunit.webp', 'living', 'Acoustic Charcoal TV Wall', 'Golf Course Road, Gurugram', 'Fluted charcoal slats with floating marble console'),
    ('/assets/images/portfolio-fullhome.webp', 'fullhome', 'Defence Colony Villa', 'Defence Colony, New Delhi', 'Complete 4BHK turnkey transformation with Italian marble'),
    ('/assets/images/portfolio-living.webp', 'living', 'Modern Minimalist Lounge', 'Gulmohar Park', 'Geometric veneer feature wall and magnetic track lights'),
    ('/assets/images/portfolio-dining.webp', 'living', 'Great Room & Dining Area', 'Vasant Vihar', 'Open concept dining with warm 3000K coffer ceiling'),
    ('/assets/images/portfolio-office.webp', 'office', 'Executive Study & Library', 'Noida Sector 44', 'Ergonomic L-desk with floor-to-ceiling bookshelves'),
    ('/assets/images/portfolio-bathroom.webp', 'bathroom', 'Spa Master Vanity & Bath', 'Greater Kailash I', 'Concealed thermostatic rain shower & fluted vanity'),
    ('/assets/images/portfolio-mandir.webp', 'woodwork', 'Sacred Teakwood Mandir', 'Mohammadpur, South Delhi', 'Intricate CNC backlit jali with solid brass bells'),
    ('/assets/images/portfolio-kitchen-2.webp', 'kitchen', 'Monochrome Parallel Kitchen', 'DLF Phase 5, Gurugram', 'Anti-fingerprint matte black finish with quartz tops'),
    ('/assets/images/portfolio-wardrobe-2.webp', 'bedroom', 'His & Her Walk-In Wardrobe', 'Jor Bagh, New Delhi', 'Velvet lined accessory trays with smoked glass doors'),
    ('/assets/images/portfolio-penthouse.webp', 'fullhome', 'Golf Links Luxury Penthouse', 'Golf Links, New Delhi', 'Turnkey duplex with bespoke teak carpentry throughout')
]

portfolio_cards_html = '\n'.join([
    f'''<div class="portfolio-card" data-category="{cat}">
  <picture>
    <source srcset="{img}" type="image/webp">
    <img src="{img.replace('.webp', '.jpg')}" alt="{title} by Delhi Interior in Delhi NCR" width="800" height="600" loading="lazy">
  </picture>
  <div class="portfolio-overlay">
    <h3>{title}</h3>
    <p>{loc} · {desc}</p>
    <a href="/contact/" class="blog-read-link" style="margin-top:0.8rem;">Get This Look →</a>
  </div>
</div>'''
    for img, cat, title, loc, desc in portfolio_items
])

portfolio_html = f'''{get_header(active_nav='portfolio', title='Interior Design Portfolio Delhi | 500+ Verified Homes | Delhi Interior', desc='Explore our portfolio of 500+ luxury modular kitchens, custom wardrobes, living rooms and full turnkey homes completed across Delhi NCR.', canonical='https://delhiinterior.com/portfolio/', schema=portfolio_schema)}
  <main id="main-content">
    <section class="inner-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="/">Home</a>
          <span class="separator">/</span>
          <span class="current">Design Portfolio</span>
        </nav>
        <div class="pill-badge" style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.8rem; font-weight:700; margin-bottom:1rem;">
          ✦ 500+ Homes Delivered Across Delhi NCR
        </div>
        <h1>Real Homes, Beautifully Crafted<span class="logo-dot">.</span></h1>
        <p class="hero-subtitle">Every room tells a personal story. Explore our residential transformations across South Delhi, Gurugram, and Noida — from compact modular kitchens to grand turnkey villas.</p>
      </div>
    </section>

    <section class="section-padding bg-light">
      <div class="container">
        <!-- Interactive Category Filter Bar -->
        <div class="portfolio-filter-bar" role="toolbar" aria-label="Portfolio category filter">
          <button class="portfolio-filter-btn active" data-filter="all">All Projects</button>
          <button class="portfolio-filter-btn" data-filter="kitchen">Kitchens</button>
          <button class="portfolio-filter-btn" data-filter="bedroom">Bedrooms &amp; Wardrobes</button>
          <button class="portfolio-filter-btn" data-filter="living">Living &amp; Dining</button>
          <button class="portfolio-filter-btn" data-filter="fullhome">Full Home</button>
          <button class="portfolio-filter-btn" data-filter="office">Workspaces</button>
          <button class="portfolio-filter-btn" data-filter="bathroom">Baths &amp; Vanity</button>
          <button class="portfolio-filter-btn" data-filter="woodwork">Woodwork &amp; Mandirs</button>
        </div>

        <!-- Project Grid -->
        <div class="portfolio-full-grid">
          {portfolio_cards_html}
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="/contact/" class="btn btn-primary" style="padding: 1rem 2.5rem; font-size: 1.05rem;">Book Consultation for Your Home</a>
        </div>
      </div>
    </section>

    <!-- Bottom CTA Banner -->
    <section class="cta-banner-section">
      <div class="container">
        <h2>Love What You See? Let's Design Yours<span class="logo-dot">.</span></h2>
        <p>Book a free site consultation and 3D layout session with our interior specialists today.</p>
        <div class="cta-buttons">
          <a href="/contact/" class="btn btn-primary">Book Free Consultation</a>
          <a href="https://wa.me/919643817099" class="btn btn-outline" style="color:#FFF; border-color:rgba(255,255,255,0.3);" target="_blank" rel="noopener noreferrer">Chat on WhatsApp</a>
        </div>
      </div>
    </section>
  </main>
{get_footer()}'''

with open('portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(portfolio_html)
print('[SUCCESS] portfolio/index.html')

# ==============================================================================
# 2. PROCESS PAGE (/process/)
# ==============================================================================
process_schema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'How It Works', 'item': 'https://delhiinterior.com/process/'}
    ]
}

process_html = f'''{get_header(active_nav='process', title='How It Works | Structured Turnkey Home Journey | Delhi Interior', desc='Learn how Delhi Interior delivers turnkey homes with transparent milestone schedules, photorealistic 3D designs, itemized pricing, and 146 quality checks.', canonical='https://delhiinterior.com/process/', schema=process_schema)}
  <main id="main-content">
    <section class="inner-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="/">Home</a>
          <span class="separator">/</span>
          <span class="current">How It Works</span>
        </nav>
        <div class="pill-badge" style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.8rem; font-weight:700; margin-bottom:1rem;">
          ✦ Predictable, Stress-Free Execution
        </div>
        <h1>Our 5-Stage Seamless Journey<span class="logo-dot">.</span></h1>
        <p class="hero-subtitle">A transparent, milestone-driven workflow that eliminates guesswork. From laser room scans to milestone-based zero-defect key handover, discover how we build homes worth living in.</p>
      </div>
    </section>

    <section class="section-padding bg-white">
      <div class="container" style="max-width: 1000px;">
        
        <!-- Stage 1 -->
        <div class="process-step" style="display: grid; grid-template-columns: 80px 1fr 1fr; gap: 2.5rem; align-items: center; margin-bottom: 2.5rem;">
          <div class="step-circle" style="width: 60px; height: 60px; font-size: 1.5rem; margin: 0;">01</div>
          <div>
            <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.2rem 0.6rem; border-radius:999px; font-size:0.75rem; font-weight:700; margin-bottom:0.5rem;">Stage 1 · Days 1–3</div>
            <h4>Free Consultation &amp; Discovery</h4>
            <p>We begin with an in-depth conversation regarding your lifestyle, family requirements, aesthetic tastes, and budget expectations. We explain materials, timelines, and options openly without sales pressure.</p>
            <ul style="list-style: none; margin-top: 1rem; color: #4B5563; font-size: 0.88rem; line-height: 1.8;">
              <li>✓ Family lifestyle analysis &amp; storage planning</li>
              <li>✓ Realistic budget breakdown across civil and modular</li>
              <li>✓ Preliminary timeline projection</li>
            </ul>
          </div>
          <div>
            <picture>
              <source srcset="/assets/images/about-team.webp" type="image/webp">
              <img src="/assets/images/about-team.jpg" alt="Interior consultation at Delhi Interior Delhi" width="800" height="600" loading="lazy" style="border-radius: var(--radius-lg); width:100%; box-shadow:var(--shadow-md);">
            </picture>
          </div>
        </div>

        <!-- Stage 2 -->
        <div class="process-step" style="display: grid; grid-template-columns: 80px 1fr 1fr; gap: 2.5rem; align-items: center; margin-bottom: 2.5rem;">
          <div class="step-circle" style="width: 60px; height: 60px; font-size: 1.5rem; margin: 0;">02</div>
          <div>
            <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.2rem 0.6rem; border-radius:999px; font-size:0.75rem; font-weight:700; margin-bottom:0.5rem;">Stage 2 · Days 4–7</div>
            <h4>Millimetre Laser Site Audit</h4>
            <p>Our technical team visits your property equipped with Leica laser meters. We inspect plumbing pressure, electrical load distribution, wall plumbness, and civil masonry integrity to preempt any site surprises.</p>
            <ul style="list-style: none; margin-top: 1rem; color: #4B5563; font-size: 0.88rem; line-height: 1.8;">
              <li>✓ Millimetre-accurate 3D laser measurement</li>
              <li>✓ Electrical and plumbing conduit tracing</li>
              <li>✓ Comprehensive photographic and videographic site audit</li>
            </ul>
          </div>
          <div>
            <picture>
              <source srcset="/assets/images/about-workshop.webp" type="image/webp">
              <img src="/assets/images/about-workshop.jpg" alt="Site measurement and engineering by Delhi Interior" width="800" height="600" loading="lazy" style="border-radius: var(--radius-lg); width:100%; box-shadow:var(--shadow-md);">
            </picture>
          </div>
        </div>

        <!-- Stage 3 -->
        <div class="process-step" style="display: grid; grid-template-columns: 80px 1fr 1fr; gap: 2.5rem; align-items: center; margin-bottom: 2.5rem;">
          <div class="step-circle" style="width: 60px; height: 60px; font-size: 1.5rem; margin: 0;">03</div>
          <div>
            <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.2rem 0.6rem; border-radius:999px; font-size:0.75rem; font-weight:700; margin-bottom:0.5rem;">Stage 3 · Days 8–14</div>
            <h4>Architectural Working Drawings Design &amp; Materials</h4>
            <p>You see your finished home before a single nail is hammered. We develop immersive 3D renderings showcasing exact furniture proportions, lighting layers, and material textures. We revise until you are completely thrilled.</p>
            <ul style="list-style: none; margin-top: 1rem; color: #4B5563; font-size: 0.88rem; line-height: 1.8;">
              <li>✓ Architectural Working Drawings room renders and 360-degree views</li>
              <li>✓ Physical material swatches (laminates, quartz, veneers, fabrics)</li>
              <li>✓ Itemized BOQ quotation with zero hidden escalation</li>
            </ul>
          </div>
          <div>
            <picture>
              <source srcset="/assets/images/portfolio-tvunit.webp" type="image/webp">
              <img src="/assets/images/portfolio-tvunit.jpg" alt="3D design to reality execution by Delhi Interior" width="800" height="600" loading="lazy" style="border-radius: var(--radius-lg); width:100%; box-shadow:var(--shadow-md);">
            </picture>
          </div>
        </div>

        <!-- Stage 4 -->
        <div class="process-step" style="display: grid; grid-template-columns: 80px 1fr 1fr; gap: 2.5rem; align-items: center; margin-bottom: 2.5rem;">
          <div class="step-circle" style="width: 60px; height: 60px; font-size: 1.5rem; margin: 0;">04</div>
          <div>
            <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.2rem 0.6rem; border-radius:999px; font-size:0.75rem; font-weight:700; margin-bottom:0.5rem;">Stage 4 · Days 15–40</div>
            <h4>Factory Machining &amp; Turnkey Assembly</h4>
            <p>All cabinetry and modular carcasses are manufactured in our state-of-the-art facility using computerized beam saws and German edge-banders. Simultaneously, civil, plumbing, electrical, and false ceiling works proceed seamlessly on-site.</p>
            <ul style="list-style: none; margin-top: 1rem; color: #4B5563; font-size: 0.88rem; line-height: 1.8;">
              <li>✓ Zero-dust factory fabrication with certified BWP grade materials</li>
              <li>✓ Full-time on-site project manager supervising every trade</li>
              <li>✓ Daily WhatsApp photo &amp; video progress reports</li>
            </ul>
          </div>
          <div>
            <picture>
              <source srcset="/assets/images/service-kitchen.webp" type="image/webp">
              <img src="/assets/images/service-kitchen.jpg" alt="Turnkey execution by Delhi Interior craftsmen" width="800" height="600" loading="lazy" style="border-radius: var(--radius-lg); width:100%; box-shadow:var(--shadow-md);">
            </picture>
          </div>
        </div>

        <!-- Stage 5 -->
        <div class="process-step" style="display: grid; grid-template-columns: 80px 1fr 1fr; gap: 2.5rem; align-items: center;">
          <div class="step-circle" style="width: 60px; height: 60px; font-size: 1.5rem; margin: 0;">05</div>
          <div>
            <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.2rem 0.6rem; border-radius:999px; font-size:0.75rem; font-weight:700; margin-bottom:0.5rem;">Stage 5 · Final Handover</div>
            <h4>146-Point Quality Audit &amp; Move-In</h4>
            <p>Before handing you the keys, our quality control team audits 146 inspection points — checking drawer glide smoothness, silicone sealants, electrical switch polarity, and paint sheen. We complete a thorough handover accompanied by original material documentation.</p>
            <ul style="list-style: none; margin-top: 1rem; color: #4B5563; font-size: 0.88rem; line-height: 1.8;">
              <li>✓ Comprehensive 146-point quality checklist audit</li>
              <li>✓ Industrial deep cleaning of all cabinets, floors, and glass</li>
              <li>✓ Original manufacturer hardware certificates and material authenticity records</li>
            </ul>
          </div>
          <div>
            <picture>
              <source srcset="/assets/images/portfolio-fullhome.webp" type="image/webp">
              <img src="/assets/images/portfolio-fullhome.jpg" alt="Handover of finished luxury home in Delhi" width="800" height="600" loading="lazy" style="border-radius: var(--radius-lg); width:100%; box-shadow:var(--shadow-md);">
            </picture>
          </div>
        </div>

      </div>
    </section>

    <!-- CTA Banner -->
    <section class="cta-banner-section">
      <div class="container">
        <h2>Experience Hassle-Free Interior Execution<span class="logo-dot">.</span></h2>
        <p>Book your initial consultation and laser site measurement today. 100% free with zero obligations.</p>
        <div class="cta-buttons">
          <a href="/contact/" class="btn btn-primary">Book Free Consultation</a>
          <a href="https://wa.me/919643817099" class="btn btn-outline" style="color:#FFF; border-color:rgba(255,255,255,0.3);" target="_blank" rel="noopener noreferrer">Chat on WhatsApp</a>
        </div>
      </div>
    </section>
  </main>
{get_footer()}'''

with open('process/index.html', 'w', encoding='utf-8') as f:
    f.write(process_html)
print('[SUCCESS] process/index.html')

# ==============================================================================
# 3. ABOUT PAGE (/about/)
# ==============================================================================
about_schema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'About Us', 'item': 'https://delhiinterior.com/about/'}
    ]
}

about_html = f'''{get_header(active_nav='about', title='About Delhi Interior | 10+ Years Luxury Interior Design Studio', desc='Learn about Delhi Interior — our founding story, in-house modular workshop, master craftsmen, and philosophy of creating spaces designed to delight every day.', canonical='https://delhiinterior.com/about/', schema=about_schema)}
  <main id="main-content">
    <section class="inner-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="/">Home</a>
          <span class="separator">/</span>
          <span class="current">About Us</span>
        </nav>
        <div class="pill-badge" style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.8rem; font-weight:700; margin-bottom:1rem;">
          ✦ Dedicated to Design Excellence Since 2014
        </div>
        <h1>Crafting Homes for Indian Lifestyles<span class="logo-dot">.</span></h1>
        <p class="hero-subtitle">We are an architectural interior design and precision modular studio based in New Delhi. No cookie-cutter templates. No subcontracted chaos. Just unyielding dedication to certified craftsmanship.</p>
      </div>
    </section>

    <!-- Our Story Section -->
    <section class="section-padding bg-white">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 4rem; align-items: center;">
          <div>
            <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Our Story</div>
            <h2 style="font-size: 2.4rem; margin-bottom: 1.2rem;">Building a Better Way to Design Homes</h2>
            <p style="font-size: 1.05rem; line-height: 1.8; color: #4B5563; margin-bottom: 1.2rem;">Founded in 2014 in the heart of Delhi, Delhi Interior began with a fundamental belief: Indian homeowners deserved a better experience than the fragmented chaos of local contractors and the rigid, overpriced catalog templates of corporate tech startups.</p>
            <p style="font-size: 1.05rem; line-height: 1.8; color: #4B5563; margin-bottom: 1.2rem;">Over the past 10+ years, we have brought civil masons, master carpenters, certified electricians, and architectural designers under one single roof. We operate our own modern 10,000 sq. ft. fabrication facility in Delhi NCR, giving us 100% control over quality, hardware authenticity, and on-time delivery.</p>
            <p style="font-size: 1.05rem; line-height: 1.8; color: #4B5563;">Today, with over 500+ completed residences across South Delhi, Gurugram, and Noida, our studio continues to design spaces that are deeply personal, built to withstand generations, and inspiring every single day.</p>
          </div>
          <div>
            <picture>
              <source srcset="/assets/images/about-team.webp" type="image/webp">
              <img src="/assets/images/about-team.jpg" alt="Interior design team at Delhi Interior" width="800" height="1000" loading="lazy" style="border-radius: var(--radius-xl); box-shadow: var(--shadow-xl); width: 100%;">
            </picture>
          </div>
        </div>
      </div>
    </section>

    <!-- Modern Stats Strip -->
    <section class="section-padding bg-light" style="padding: 4rem 0;">
      <div class="container">
        <div class="trust-strip-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem;">
          <div class="trust-strip-item" style="text-align: center; background: var(--color-white); padding: 2rem; border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
            <div class="metric-counter" data-target="500" data-suffix="+" style="font-size: 2.5rem; font-weight: 800; color: var(--color-primary); margin-bottom: 0.3rem;">500+</div>
            <div style="font-size: 0.95rem; font-weight: 700; color: var(--color-dark);">Homes Delivered</div>
            <p style="font-size: 0.8rem; color: var(--color-muted); margin-top: 0.3rem;">Across Delhi, Gurugram &amp; Noida</p>
          </div>
          <div class="trust-strip-item" style="text-align: center; background: var(--color-white); padding: 2rem; border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
            <div class="metric-counter" data-target="10" data-suffix="+" style="font-size: 2.5rem; font-weight: 800; color: var(--color-primary); margin-bottom: 0.3rem;">10+</div>
            <div style="font-size: 0.95rem; font-weight: 700; color: var(--color-dark);">Years Experience</div>
            <p style="font-size: 0.8rem; color: var(--color-muted); margin-top: 0.3rem;">Established since 2014</p>
          </div>
          <div class="trust-strip-item" style="text-align: center; background: var(--color-white); padding: 2rem; border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
            <div class="metric-counter" data-target="146" data-suffix="" style="font-size: 2.5rem; font-weight: 800; color: var(--color-primary); margin-bottom: 0.3rem;">146</div>
            <div style="font-size: 0.95rem; font-weight: 700; color: var(--color-dark);">Quality Checks</div>
            <p style="font-size: 0.8rem; color: var(--color-muted); margin-top: 0.3rem;">Rigorous pre-delivery audit</p>
          </div>
          <div class="trust-strip-item" style="text-align: center; background: var(--color-white); padding: 2rem; border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
            <div class="metric-counter" data-target="10" data-suffix=" Years" style="font-size: 2.5rem; font-weight: 800; color: var(--color-primary); margin-bottom: 0.3rem;">10<span> Years</span></div>
            <div style="font-size: 0.95rem; font-weight: 700; color: var(--color-dark);">Authentic Materials</div>
            <p style="font-size: 0.8rem; color: var(--color-muted); margin-top: 0.3rem;">Hardware &amp; cabinetry protection</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Workshop & Facility Section -->
    <section class="section-padding bg-white">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 4rem; align-items: center;">
          <div>
            <picture>
              <source srcset="/assets/images/about-workshop.webp" type="image/webp">
              <img src="/assets/images/about-workshop.jpg" alt="Delhi Interior modern manufacturing facility" width="800" height="600" loading="lazy" style="border-radius: var(--radius-xl); box-shadow: var(--shadow-xl); width: 100%;">
            </picture>
          </div>
          <div>
            <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Precision Engineering</div>
            <h2 style="font-size: 2.4rem; margin-bottom: 1.2rem;">Our 10,000 Sq. Ft. Fabrication Studio</h2>
            <p style="font-size: 1.05rem; line-height: 1.8; color: #4B5563; margin-bottom: 1.2rem;">Unlike firms that outsource manufacturing to third-party factories where quality corners are cut, we operate our own 10,000 sq. ft. dedicated manufacturing and finishing facility.</p>
            <p style="font-size: 1.05rem; line-height: 1.8; color: #4B5563; margin-bottom: 1.2rem;">Equipped with high-precision CNC panel saws, heavy-duty through-feed edge banders, and dedicated dust-free paint and PU spray booths, our workshop ensures that every carcass, hinge cavity, and edge band meets international millimeter tolerances.</p>
            <p style="font-size: 1.05rem; line-height: 1.8; color: #4B5563;">Clients are always welcome to visit our workshop to see their cabinets being assembled and inspect raw plywood sheets before they are dispatched to site.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 4 Core Pillars -->
    <section class="section-padding bg-light">
      <div class="container">
        <div class="section-title-wrap">
          <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Our Commitments</div>
          <h2>The Four Pillars of Delhi Interior</h2>
          <p>Uncompromising principles that guide every single drawing, cut, and joint we create.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem;">
          <div style="background: var(--color-white); padding: 2rem; border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
            <div class="pillar-icon-box"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg></div>
            <h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Honest Materials</h4>
            <p style="font-size: 0.9rem; color: var(--color-muted); line-height: 1.6;">We specify certified BWP 710 marine plywood and authentic German hardware. Zero counterfeit substitutes.</p>
          </div>
          <div style="background: var(--color-white); padding: 2rem; border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
            <div class="pillar-icon-box"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21.3 15.3l-6.6-6.6a2 2 0 0 0-2.8 0L2.7 17.9a1 1 0 0 0 0 1.4l2 2a1 1 0 0 0 1.4 0l9.2-9.2 1.4 1.4a1 1 0 0 0 1.4 0l3.2-3.2z"/><path d="M14 6l4 4"/><circle cx="5" cy="19" r="1"/></svg></div>
            <h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Form Follows Life</h4>
            <p style="font-size: 0.9rem; color: var(--color-muted); line-height: 1.6;">A home must function effortlessly for Indian living. We design around storage realities, domestic help access, and climate resilience.</p>
          </div>
          <div style="background: var(--color-white); padding: 2rem; border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
            <div class="pillar-icon-box"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>
            <h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Structured Timelines</h4>
            <p style="font-size: 0.9rem; color: var(--color-muted); line-height: 1.6;">Time is sacred. Our milestone schedules and proactive project management ensure steady progress toward your planned move-in date.</p>
          </div>
          <div style="background: var(--color-white); padding: 2rem; border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
            <div class="pillar-icon-box"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
            <h4 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Enduring Durability</h4>
            <p style="font-size: 0.9rem; color: var(--color-muted); line-height: 1.6;">Our relationship does not end at handover. With our dedicated after-sales care, our service team is always just a phone call away.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom CTA Banner -->
    <section class="cta-banner-section">
      <div class="container">
        <h2>Work with Delhi NCR's Trusted Interior Studio<span class="logo-dot">.</span></h2>
        <p>Schedule a complimentary design consultation and site measurement today.</p>
        <div class="cta-buttons">
          <a href="/contact/" class="btn btn-primary">Book Consultation</a>
          <a href="https://wa.me/919643817099" class="btn btn-outline" style="color:#FFF; border-color:rgba(255,255,255,0.3);" target="_blank" rel="noopener noreferrer">Chat on WhatsApp</a>
        </div>
      </div>
    </section>
  </main>
{get_footer()}'''

with open('about/index.html', 'w', encoding='utf-8') as f:
    f.write(about_html)
print('[SUCCESS] about/index.html')

# ==============================================================================
# 4. CONTACT PAGE (/contact/)
# ==============================================================================
contact_schema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Contact', 'item': 'https://delhiinterior.com/contact/'}
    ]
}

contact_html = f'''{get_header(active_nav='contact', title='Contact Us & Book Free Site Visit | Delhi Interior', desc='Contact Delhi Interior studio. Call +91 96438 17099 or submit your project details for a free site visit and 3D design consultation within 24 hours.', canonical='https://delhiinterior.com/contact/', schema=contact_schema)}
  <main id="main-content">
    <section class="inner-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="/">Home</a>
          <span class="separator">/</span>
          <span class="current">Contact Us</span>
        </nav>
        <div class="pill-badge" style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.8rem; font-weight:700; margin-bottom:1rem;">
          ✦ Prompt Response Within 24 Hours
        </div>
        <h1>Get in Touch with Our Designers<span class="logo-dot">.</span></h1>
        <p class="hero-subtitle">Ready to transform your home? Schedule a complimentary site visit or consultation with our principal design team.</p>
      </div>
    </section>

    <section class="section-padding bg-light">
      <div class="container">
        <div class="contact-grid">
          
          <!-- Contact Info Left Column -->
          <div class="contact-info-card">
            <h2>Studio Information</h2>
            <p style="color: var(--color-muted); margin-bottom: 2rem; font-size: 0.95rem;">Drop by our South Delhi studio or call directly to discuss your layout, materials, and itemized quotation.</p>

            <div class="contact-channel-item">
              <div class="icon-box">
                <svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
              </div>
              <div>
                <strong>Direct Phone Line</strong>
                <a href="tel:+919643817099" style="color:var(--color-primary); font-weight:700;">+91 96438 17099</a>
              </div>
            </div>

            <div class="contact-channel-item">
              <div class="icon-box" style="background:#DCFCE7; color:#16A34A;">
                <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.43.1-.12.19-.48.61-.59.73-.11.12-.22.14-.41.05-.19-.09-.8-.29-1.53-.94-.57-.51-.95-1.13-1.06-1.32-.11-.19-.01-.3.08-.39.09-.08.19-.22.29-.33.09-.11.12-.19.19-.31.06-.12.03-.24-.01-.33-.05-.09-.43-1.04-.6-1.42-.16-.38-.32-.33-.44-.33h-.37c-.13 0-.34.05-.52.24-.18.19-.69.67-.69 1.64s.71 1.9 1.01 2.3c.3.4 1.92 2.93 4.65 4.11.65.28 1.16.45 1.55.58.65.21 1.25.18 1.72.11.53-.08 1.62-.66 1.85-1.3.23-.64.23-1.19.16-1.3-.06-.11-.23-.18-.42-.27z"/></svg>
              </div>
              <div>
                <strong>WhatsApp Priority Desk</strong>
                <a href="https://wa.me/919643817099" target="_blank" rel="noopener noreferrer" style="color:#16A34A; font-weight:700;">+91 96438 17099</a>
              </div>
            </div>

            <div class="contact-channel-item">
              <div class="icon-box">
                <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
              </div>
              <div>
                <strong>Email Address</strong>
                <p>hello@delhiinterior.com</p>
              </div>
            </div>

            <div class="contact-channel-item">
              <div class="icon-box">
                <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
              </div>
              <div>
                <strong>Studio Address</strong>
                <p>F-128/4, Mohammadpur, New Delhi, Delhi, 110066</p>
              </div>
            </div>

            <div class="contact-channel-item">
              <div class="icon-box">
                <svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
              </div>
              <div>
                <strong>Working Hours</strong>
                <p>Open 24 Hours (7 Days a Week)</p>
              </div>
            </div>

            <!-- Google Map -->
            <div class="map-container">
              <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14015.405781308365!2d77.2155!3d28.5684!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390ce2697843d1a3%3A0x6b093666b6c8d45e!2sSouth%20Extension%20II%2C%20New%20Delhi!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" 
                title="Delhi Interior Studio Location"
                loading="lazy">
              </iframe>
            </div>
          </div>

          <!-- Form Card Right Column -->
          <div class="hero-form-card" style="box-shadow: var(--shadow-lg);">
            <div class="form-badge">Free Design Consultation</div>
            <h3>Book Your Consultation</h3>
            <p class="form-sub">Speak with our senior design director within 24 hours.</p>

            <form id="quote-form" novalidate>
              <input type="text" name="honeypot" style="display:none" tabindex="-1" autocomplete="off">

              <div class="form-fields-container">
                <div class="form-group">
                  <label for="client-name" class="form-label">Full Name *</label>
                  <input type="text" id="client-name" name="name" class="form-control" placeholder="e.g. Rahul Sharma" required>
                  <div class="invalid-feedback">Please enter your name</div>
                </div>

                <div class="form-group">
                  <label for="client-phone" class="form-label">Phone Number *</label>
                  <input type="tel" id="client-phone" name="phone" class="form-control" placeholder="10-digit mobile number" required>
                  <div class="invalid-feedback">Please enter a valid 10-digit phone number</div>
                </div>

                <div class="form-group">
                  <label for="service-type" class="form-label">Required Space *</label>
                  <select id="service-type" name="service" class="form-control" required>
                    <option value="" disabled selected>Select service...</option>
                    <option value="Modular Kitchen">Modular Kitchen</option>
                    <option value="Wardrobes & Bedrooms">Wardrobes &amp; Bedrooms</option>
                    <option value="Full Home 2BHK Turnkey">Full Home 2BHK Turnkey</option>
                    <option value="Full Home 3BHK Turnkey">Full Home 3BHK Turnkey</option>
                    <option value="Full Home 4BHK+ Turnkey">Full Home 4BHK+ Turnkey</option>
                    <option value="Wall Paneling & TV Units">Wall Paneling &amp; TV Units</option>
                    <option value="False Ceiling & Lighting">False Ceiling &amp; Lighting</option>
                    <option value="Other / Commercial">Other / Commercial</option>
                  </select>
                </div>

                <div class="form-group">
                  <label for="client-area" class="form-label">Locality / City *</label>
                  <input type="text" id="client-area" name="area" class="form-control" placeholder="e.g. Greater Kailash, Golf Course Rd Gurugram" required>
                </div>

                <div class="form-group">
                  <label for="client-message" class="form-label">Project Details (Optional)</label>
                  <textarea id="client-message" name="message" class="form-control" rows="3" placeholder="Possession date, room size, or special requirements..."></textarea>
                </div>

                <button type="submit" id="submit-quote-btn" class="btn btn-primary btn-block">
                  Book Free Consultation
                </button>

                <p class="privacy-note">Zero spam. Your details remain 100% confidential.</p>
              </div>

              <div class="form-success-state">
                <div class="check-icon">✓</div>
                <h3>Thank you, <span class="client-name-display">there</span>!</h3>
                <p>We've received your request. Our senior designer will call you within 24 hours.</p>
                <a href="#" class="btn btn-primary wa-direct-link" target="_blank" rel="noopener noreferrer">
                  Chat Now on WhatsApp
                </a>
              </div>
            </form>
          </div>

        </div>
      </div>
    </section>
  </main>
{get_footer()}'''

with open('contact/index.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)
print('[SUCCESS] contact/index.html')

# ==============================================================================
# 5. THANK YOU PAGE (/thank-you/)
# ==============================================================================
thank_you_html = f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Thank You | Enquiry Received | Delhi Interior</title>
  <meta name="description" content="Thank you for contacting Delhi Interior. Our team will review your requirements and call you within 24 hours to schedule your free site consultation.">
  <meta name="robots" content="noindex, follow">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/assets/css/style.css?v=3.0">

  <script>
    window.addEventListener('DOMContentLoaded', function() {{
      if (typeof window.gtag === 'function') {{
        window.gtag('event', 'conversion', {{
          'send_to': 'G-XXXXXXXXXX',
          'event_category': 'lead',
          'event_label': 'thank_you_page_view'
        }});
      }}
    }});
  </script>
</head>
<body style="background-color: #FAFAFA; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; align-items: center; text-align: center; padding: 2rem 1rem;">
  
  <div style="max-width: 620px; width: 100%; background: var(--color-white); border-radius: var(--radius-xl); border: 1px solid var(--color-border); padding: 3.5rem 2.5rem; box-shadow: var(--shadow-xl);">
    <div style="margin-bottom: 2rem;">
      <a href="/" aria-label="Delhi Interior Home">
        <img src="/assets/images/logo.png" alt="Delhi Interior" width="168" height="52" class="brand-logo-img">
      </a>
    </div>
    
    <div style="width: 72px; height: 72px; border-radius: 50%; background: #DCFCE7; color: #16A34A; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2.2rem; font-weight: 800;">
      ✓
    </div>

    <div class="pill-pill-badge" style="display:inline-flex; align-items:center; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.8rem; font-weight:700; margin-bottom:1rem;">
      Enquiry Received Successfully
    </div>

    <h1 style="font-size: 2.3rem; font-weight: 800; color: var(--color-dark); margin-bottom: 0.8rem;">
      You're One Step Closer to Your Dream Home<span class="logo-dot">.</span>
    </h1>
    <p style="color: var(--color-muted); font-size: 1.05rem; margin-bottom: 2.5rem; line-height: 1.6;">
      Our senior design director will review your requirements and call you within 24 hours to schedule your complimentary 3D design consultation.
    </p>

    <!-- Next Steps Box -->
    <div style="background: #F9FAFB; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 1.8rem; text-align: left; margin-bottom: 2.5rem;">
      <h4 style="font-size: 0.95rem; font-weight: 800; color: var(--color-dark); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">What Happens Next</h4>
      
      <div style="display: flex; gap: 0.85rem; margin-bottom: 0.85rem; align-items: baseline;">
        <span style="color: var(--color-primary); font-weight: 800; font-size: 1rem;">1.</span>
        <p style="color: #4B5563; font-size: 0.9rem; margin: 0;">We review your floor plan dimensions and material preferences.</p>
      </div>

      <div style="display: flex; gap: 0.85rem; margin-bottom: 0.85rem; align-items: baseline;">
        <span style="color: var(--color-primary); font-weight: 800; font-size: 1rem;">2.</span>
        <p style="color: #4B5563; font-size: 0.9rem; margin: 0;">A senior designer calls to schedule your free laser site measurement.</p>
      </div>

      <div style="display: flex; gap: 0.85rem; align-items: baseline;">
        <span style="color: var(--color-primary); font-weight: 800; font-size: 1rem;">3.</span>
        <p style="color: #4B5563; font-size: 0.9rem; margin: 0;">You receive architectural layouts and an itemized specification quotation.</p>
      </div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 1rem;">
      <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+just+submitted+an+enquiry+on+your+website." class="btn btn-primary" target="_blank" rel="noopener noreferrer">
        Need Faster Response? Chat on WhatsApp
      </a>
      <a href="/portfolio/" class="btn btn-outline">
        Browse Design Portfolio
      </a>
      <a href="/" style="color: var(--color-muted); font-size: 0.85rem; text-decoration: underline; margin-top: 0.5rem;">
        Return to Homepage
      </a>
    </div>

  </div>

</body>
</html>'''

with open('thank-you/index.html', 'w', encoding='utf-8') as f:
    f.write(thank_you_html)
print('[SUCCESS] thank-you/index.html')

# ==============================================================================
# 6. 404 PAGE (/404.html)
# ==============================================================================
page_404_html = f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>404 — Page Not Found | Delhi Interior</title>
  <meta name="description" content="The page you are looking for has moved or does not exist. Return to Delhi Interior homepage.">
  <meta name="robots" content="noindex, follow">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/assets/css/style.css?v=3.0">
</head>
<body style="background-color: #FAFAFA; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; align-items: center; text-align: center; padding: 2rem 1rem;">
  
  <div style="max-width: 540px; background: var(--color-white); border-radius: var(--radius-xl); border: 1px solid var(--color-border); padding: 3.5rem 2rem; box-shadow: var(--shadow-xl);">
    <div style="font-size: 4.5rem; font-weight: 800; color: var(--color-primary); line-height: 1; margin-bottom: 1rem;">
      404
    </div>
    <h1 style="font-size: 2rem; font-weight: 800; color: var(--color-dark); margin-bottom: 0.8rem;">
      Page Not Found<span class="logo-dot">.</span>
    </h1>
    <p style="color: var(--color-muted); font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.6;">
      The page you're looking for might have been moved, renamed, or is temporarily unavailable.
    </p>

    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <a href="/" class="btn btn-primary">Go to Homepage</a>
      <a href="/portfolio/" class="btn btn-outline">Explore Designs</a>
      <a href="/contact/" class="btn btn-outline">Contact Us</a>
    </div>
  </div>

</body>
</html>'''

with open('404.html', 'w', encoding='utf-8') as f:
    f.write(page_404_html)
print('[SUCCESS] 404.html')

# ==============================================================================
# 7. PRIVACY POLICY PAGE (/privacy-policy/)
# ==============================================================================
privacy_schema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Privacy Policy', 'item': 'https://delhiinterior.com/privacy-policy/'}
    ]
}

privacy_html = f'''{get_header(active_nav='', title='Privacy Policy | Delhi Interior', desc='Read the Privacy Policy of Delhi Interior. Learn how we handle your contact details, cookies, and personal data with total security and transparency.', canonical='https://delhiinterior.com/privacy-policy/', schema=privacy_schema)}
  <main id="main-content">
    <div class="article-container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="/">Home</a>
        <span class="separator">/</span>
        <span class="current">Privacy Policy</span>
      </nav>

      <div class="article-header">
        <h1>Privacy Policy<span class="logo-dot">.</span></h1>
        <p style="font-size: 0.88rem; color: var(--color-muted);">Last Updated: November 2026</p>
      </div>

      <div class="article-body">
        <p>At Delhi Interior, accessible from https://delhiinterior.com, one of our main priorities is the privacy of our visitors. This Privacy Policy document outlines the types of information that is collected and recorded by Delhi Interior and how we use it, in compliance with applicable Indian data protection laws and the Digital Personal Data Protection (DPDP) Act.</p>

        <h2>1. Information We Collect</h2>
        <p>When you contact us, request a free quotation, or schedule a site visit, we may collect the following personal information:</p>
        <ul>
          <li><strong>Contact Data:</strong> Your full name, telephone / WhatsApp number, email address, and residential project locality.</li>
          <li><strong>Project Specifications:</strong> Room floor plans, carpet area, aesthetic preferences, and budget ranges you submit.</li>
          <li><strong>Technical Data:</strong> IP address, browser type, operating system, and pages visited, collected through anonymous analytics cookies.</li>
        </ul>

        <h2>2. How We Use Your Information</h2>
        <p>We use the collected information exclusively for legitimate interior design service purposes:</p>
        <ul>
          <li>To schedule complimentary laser site visits and consultations.</li>
          <li>To prepare customized photorealistic 3D renderings and itemized quotations.</li>
          <li>To communicate project milestones via phone, email, or WhatsApp.</li>
          <li>To improve website performance and user experience through aggregated analytics data.</li>
        </ul>

        <h2>3. We Never Sell Your Data</h2>
        <p><strong>Under no circumstances do we sell, rent, trade, or distribute your personal contact information to any third-party marketing companies, telemarketers, or loan providers.</strong> Your details remain strictly confidential within our in-house team.</p>

        <h2>4. Cookies &amp; Tracking Technologies</h2>
        <p>We use cookies to maintain website settings and understand how visitors interact with our portfolio pages. You have full control over cookie preferences via our Cookie Consent banner upon first visit. You can decline analytical tracking cookies at any time.</p>

        <h2>5. Data Security</h2>
        <p>We implement industry-standard encryption and administrative safeguards to protect your personal information from unauthorized access, alteration, or disclosure.</p>

        <h2>6. Contact Us Regarding Your Data</h2>
        <p>If you have any questions about this Privacy Policy or wish to request the deletion or correction of your contact details, please reach out to our privacy officer at:</p>
        <p><strong>Email:</strong> privacy@delhiinterior.com<br><strong>Studio Address:</strong> F-128/4, Mohammadpur, New Delhi, Delhi, 110066, Delhi 110066<br><strong>Phone:</strong> +91 96438 17099</p>
      </div>
    </div>
  </main>
{get_footer()}'''

with open('privacy-policy/index.html', 'w', encoding='utf-8') as f:
    f.write(privacy_html)
print('[SUCCESS] privacy-policy/index.html')

# ==============================================================================
# 8. TERMS OF SERVICE PAGE (/terms-of-service/)
# ==============================================================================
terms_schema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Terms of Service', 'item': 'https://delhiinterior.com/terms-of-service/'}
    ]
}

terms_html = f'''{get_header(active_nav='', title='Terms of Service & Studio Policies | Delhi Interior', desc='Review the official terms of service, payment milestones, scope of work, and craftsmanship policies of Delhi Interior design studio.', canonical='https://delhiinterior.com/terms-of-service/', schema=terms_schema)}
  <main id="main-content">
    <div class="article-container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="/">Home</a>
        <span class="separator">/</span>
        <span class="current">Terms of Service</span>
      </nav>

      <div class="article-header">
        <h1>Terms of Service<span class="logo-dot">.</span></h1>
        <p style="font-size: 0.88rem; color: var(--color-muted);">Last Updated: November 2026</p>
      </div>

      <div class="article-body">
        <p>Welcome to Delhi Interior. These Terms of Service govern your relationship with Delhi Interior regarding architectural design, modular woodwork manufacturing, and turnkey home execution services.</p>

        <h2>1. Scope of Work &amp; Itemized Quotation</h2>
        <p>All work undertaken by Delhi Interior is strictly defined in a signed Bill of Quantities (BOQ) and 3D design agreement. Any client-requested alterations or additions after sign-off will be quoted separately in writing before commencement. We commit to transparent, itemized pricing with zero hidden surcharges.</p>

        <h2>2. Payment Milestone Schedule</h2>
        <p>To ensure steady procurement of high-grade raw materials and uninterrupted manufacturing, projects follow a transparent milestone schedule:</p>
        <ul>
          <li><strong>Booking Advance (10%):</strong> Site measurement, space planning, and 3D architectural rendering.</li>
          <li><strong>Design Sign-Off (40%):</strong> Material finalization, beam saw procurement, and factory carcass cutting.</li>
          <li><strong>On-Site Civil &amp; Framing Completion (40%):</strong> Civil masonry, false ceiling, and modular assembly on site.</li>
          <li><strong>Zero-Snag Handover (10%):</strong> Final quality audit, snag fix, deep cleaning, and key handover.</li>
        </ul>

        <h2>3. Quality Standards &amp; Material Specifications Policy</h2>
        <p>Delhi Interior builds exclusively with genuine, certified materials including IS:710 boiling waterproof marine plywood, Action TESA HDMR boards, and authentic hardware from Blum, Hettich, and Hafele. Manufacturer test certificates and authenticity records are provided upon handover.</p>
        <p><em>Care Guidelines:</em> To preserve finish longevity, clients receive clear maintenance guidelines covering moisture protection, hardware care, and surface cleaning protocols.</p>

        <h2>4. Project Timelines &amp; Stage Milestones</h2>
        <p>We operate on agreed project schedules structured around clear stage milestones (civil preparation, workshop fabrication, on-site joinery, and finishing). Timelines commence after architectural drawing sign-off and site readiness.</p>

        <h2>5. Dispute Resolution &amp; Jurisdiction</h2>
        <p>Any disputes arising out of or related to our services will first be addressed through mutual good-faith mediation. If unresolved, the dispute shall be subject to the exclusive jurisdiction of the civil courts in New Delhi, India.</p>

        <h2>6. Contact Us</h2>
        <p>For any contractual or service queries, contact us at:</p>
        <p><strong>Email:</strong> legal@delhiinterior.com<br><strong>Phone:</strong> +91 96438 17099<br><strong>Studio:</strong> F-128/4, Mohammadpur, New Delhi, Delhi, 110066</p>
      </div>
    </div>
  </main>
{get_footer()}'''

with open('terms-of-service/index.html', 'w', encoding='utf-8') as f:
    f.write(terms_html)
print('[SUCCESS] terms-of-service/index.html')

# ==============================================================================
# 9. HTML SITEMAP PAGE (/sitemap/)
# ==============================================================================
sitemap_schema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'HTML Sitemap', 'item': 'https://delhiinterior.com/sitemap/'}
    ]
}

sitemap_html = f'''{get_header(active_nav='', title='HTML Sitemap | Delhi Interior Architecture Directory', desc='Browse the complete site directory of Delhi Interior — explore services, portfolio, blog articles, process, and contact resources.', canonical='https://delhiinterior.com/sitemap/', schema=sitemap_schema)}
  <main id="main-content">
    <div class="article-container" style="max-width: 950px;">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="/">Home</a>
        <span class="separator">/</span>
        <span class="current">Sitemap</span>
      </nav>

      <div class="article-header">
        <h1>Website Directory<span class="logo-dot">.</span></h1>
        <p style="color: var(--color-muted); font-size: 1rem;">Complete directory of all pages, interior services, guides, and resources available on delhiinterior.com.</p>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-top: 2rem;">
        
        <div>
          <h2 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1.2rem; color: var(--color-dark);">Main Pages</h2>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.95rem;">
            <li><a href="/" style="color: var(--color-primary); font-weight: 600;">Homepage (/)</a></li>
            <li><a href="/about/" style="color: var(--color-dark); font-weight: 500;">About Us (/about/)</a></li>
            <li><a href="/portfolio/" style="color: var(--color-dark); font-weight: 500;">Design Portfolio (/portfolio/)</a></li>
            <li><a href="/process/" style="color: var(--color-dark); font-weight: 500;">How It Works (/process/)</a></li>
            <li><a href="/contact/" style="color: var(--color-dark); font-weight: 500;">Contact &amp; Book Consultation (/contact/)</a></li>
            <li><a href="/blog/" style="color: var(--color-dark); font-weight: 500;">Interior Design Guides &amp; Blog (/blog/)</a></li>
          </ul>

          <h2 style="font-size: 1.5rem; font-weight: 800; margin: 2.5rem 0 1.2rem; color: var(--color-dark);">Legal &amp; Utilities</h2>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.95rem;">
            <li><a href="/privacy-policy/" style="color: var(--color-dark); font-weight: 500;">Privacy Policy (/privacy-policy/)</a></li>
            <li><a href="/terms-of-service/" style="color: var(--color-dark); font-weight: 500;">Terms of Service (/terms-of-service/)</a></li>
            <li><a href="/sitemap/" style="color: var(--color-primary); font-weight: 600;">HTML Sitemap (/sitemap/)</a></li>
            <li><a href="/sitemap.xml" style="color: var(--color-dark); font-weight: 500;" target="_blank">XML Sitemap (/sitemap.xml)</a></li>
            <li><a href="/robots.txt" style="color: var(--color-dark); font-weight: 500;" target="_blank">Robots.txt (/robots.txt)</a></li>
          </ul>
        </div>

        <div>
          <h2 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1.2rem; color: var(--color-dark);">Modular Services</h2>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.95rem;">
            <li><a href="/modular-kitchen-delhi/" style="color: var(--color-dark); font-weight: 500;">Modular Kitchen Design in Delhi</a></li>
            <li><a href="/wardrobe-design-delhi/" style="color: var(--color-dark); font-weight: 500;">Custom Wardrobe &amp; Closets in Delhi</a></li>
            <li><a href="/wall-paneling-delhi/" style="color: var(--color-dark); font-weight: 500;">Charcoal &amp; Fluted Wall Paneling</a></li>
            <li><a href="/false-ceiling-delhi/" style="color: var(--color-dark); font-weight: 500;">Gypsum False Ceiling &amp; Lighting</a></li>
            <li><a href="/full-home-interior-delhi/" style="color: var(--color-dark); font-weight: 500;">Full Home Turnkey Interiors</a></li>
            <li><a href="/bedroom-furniture-delhi/" style="color: var(--color-dark); font-weight: 500;">Bedroom Furniture &amp; Study Desks</a></li>
            <li><a href="/doors-partitions-delhi/" style="color: var(--color-dark); font-weight: 500;">Doors &amp; Architectural Partitions</a></li>
            <li><a href="/painting-polishing-delhi/" style="color: var(--color-dark); font-weight: 500;">Paints, PU Polish &amp; Duco Finishes</a></li>
            <li><a href="/plumbing-electrical-delhi/" style="color: var(--color-dark); font-weight: 500;">Concealed Plumbing &amp; Electrical MEP</a></li>
          </ul>

          <h2 style="font-size: 1.5rem; font-weight: 800; margin: 2.5rem 0 1.2rem; color: var(--color-dark);">Featured Editorial Guides</h2>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.95rem;">
            <li><a href="/blog/modular-kitchen-cost-delhi/" style="color: var(--color-dark); font-weight: 500;">Modular Kitchen Cost in Delhi 2025 Breakdown</a></li>
            <li><a href="/blog/fluted-vs-charcoal-panel/" style="color: var(--color-dark); font-weight: 500;">Fluted vs Charcoal Panels Comparison</a></li>
            <li><a href="/blog/sliding-vs-hinged-wardrobe/" style="color: var(--color-dark); font-weight: 500;">Sliding vs Hinged Wardrobe Decision Guide</a></li>
            <li><a href="/blog/full-home-interior-checklist/" style="color: var(--color-dark); font-weight: 500;">Full Home Interior Checklist 2025</a></li>
            <li><a href="/blog/interior-design-mistakes/" style="color: var(--color-dark); font-weight: 500;">7 Interior Design Mistakes That Cost Lakhs</a></li>
          </ul>
        </div>

      </div>
    </div>
  </main>
{get_footer()}'''

with open('sitemap/index.html', 'w', encoding='utf-8') as f:
    f.write(sitemap_html)
print('[SUCCESS] sitemap/index.html')

print('All main and utility pages regenerated successfully.')
