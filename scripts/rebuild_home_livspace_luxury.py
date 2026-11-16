import os, json

home_schema = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Delhi Interior",
    "image": "https://delhiinterior.com/og-image.jpg",
    "url": "https://delhiinterior.com/",
    "telephone": "+919811000000",
    "priceRange": "₹₹₹",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Ring Road, South Extension Part II",
        "addressLocality": "New Delhi",
        "addressRegion": "Delhi",
        "postalCode": "110049",
        "addressCountry": "IN"
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": "28.5684",
        "longitude": "77.2185"
    },
    "openingHoursSpecification": [
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:00",
            "closes": "19:00"
        }
    ],
    "areaServed": ["Delhi", "Gurugram", "Noida", "Faridabad", "Ghaziabad"]
}

html_content = f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Delhi Interior | Modular Kitchens &amp; Complete Home Interiors in Delhi NCR</title>
  <meta name="description" content="Delhi's premier modular interior studio. Custom modular kitchens, wardrobes, wall paneling, and full turnkey homes. 45-day move-in guarantee &amp; 10-year warranty.">
  <link rel="canonical" href="https://delhiinterior.com/">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Delhi Interior | Modular Kitchens &amp; Complete Home Interiors in Delhi NCR">
  <meta property="og:description" content="Delhi's premier modular interior studio. Custom modular kitchens, wardrobes, wall paneling, and full turnkey homes. 45-day move-in guarantee &amp; 10-year warranty.">
  <meta property="og:url" content="https://delhiinterior.com/">
  <meta property="og:image" content="https://delhiinterior.com/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_IN">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Delhi Interior | Modular Kitchens &amp; Complete Home Interiors">
  <meta name="twitter:description" content="Delhi's premier modular interior studio. 45-day move-in guarantee &amp; 10-year warranty.">
  <meta name="twitter:image" content="https://delhiinterior.com/og-image.jpg">

  <!-- Favicons -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon-32x32.png" type="image/png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <!-- Livspace Typography: Plus Jakarta Sans & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/assets/css/style.css">

  <script type="application/ld+json">
{json.dumps(home_schema, indent=2)}
  </script>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Top Announcement Bar -->
  <aside id="announcement-bar" aria-label="Announcement">
    <div class="bar-content">
      <span class="offer-tag">Limited Offer</span>
      <span>Free 3D Design + Up to 10% Off on Modular Kitchens · Call +91 98110 00000</span>
    </div>
    <button class="close-btn" aria-label="Dismiss banner">✕</button>
  </aside>

  <!-- Modern Livspace Header -->
  <header class="site-header" role="banner">
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
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-8z"/><path d="M4 11V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"/><circle cx="7.5" cy="8" r="1"/><circle cx="16.5" cy="8" r="1"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Modular Kitchens</strong>
                  <span>L &amp; U-Shaped, Acrylic &amp; PU</span>
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
              <a href="/full-home-interior-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Full Home Interiors</strong>
                  <span>Complete 2/3/4 BHK Turnkey</span>
                </div>
              </a>
              <a href="/wall-paneling-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="8" y1="3" x2="8" y2="21"/><line x1="12" y1="3" x2="12" y2="21"/><line x1="16" y1="3" x2="16" y2="21"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Wall Paneling &amp; TV Units</strong>
                  <span>Charcoal, Louver &amp; Fluted</span>
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
                  <span>Fluted Glass, Jali &amp; Flush</span>
                </div>
              </a>
              <a href="/bedroom-furniture-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 18v3"/><path d="M20 18v3"/><path d="M19 11v7H5v-7"/><path d="M19 11a3 3 0 0 0-3-3H8a3 3 0 0 0-3 3"/><path d="M3 14h18"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Furniture &amp; Study</strong>
                  <span>Workstations, Mandirs &amp; Consoles</span>
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
          <li><a href="#estimator">Cost Calculator</a></li>
          <li><a href="/portfolio/">Designs</a></li>
          <li><a href="/process/">How It Works</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </nav>

      <div class="nav-right">
        <a href="tel:+919811000000" class="nav-phone" aria-label="Call Delhi Interior">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
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
        <li><a href="/painting-polishing-delhi/" onclick="closeMobileMenu()">🎨 Painting &amp; PU Polish</a></li>
        <li><a href="/plumbing-electrical-delhi/" onclick="closeMobileMenu()">⚡ Plumbing &amp; Electrical MEP</a></li>
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
  </div>

  <!-- Floating WhatsApp -->
  <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+design+consultation." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.43.1-.12.19-.48.61-.59.73-.11.12-.22.14-.41.05-.19-.09-.8-.29-1.53-.94-.57-.51-.95-1.13-1.06-1.32-.11-.19-.01-.3.08-.39.09-.08.19-.22.29-.33.09-.11.12-.19.19-.31.06-.12.03-.24-.01-.33-.05-.09-.43-1.04-.6-1.42-.16-.38-.32-.33-.44-.33h-.37c-.13 0-.34.05-.52.24-.18.19-.69.67-.69 1.64s.71 1.9 1.01 2.3c.3.4 1.92 2.93 4.65 4.11.65.28 1.16.45 1.55.58.65.21 1.25.18 1.72.11.53-.08 1.62-.66 1.85-1.3.23-.64.23-1.19.16-1.3-.06-.11-.23-.18-.42-.27z"/></svg>
    <span class="whatsapp-tooltip">Chat with a Designer</span>
  </a>

  <!-- Mobile Sticky Bottom CTA -->
  <aside class="sticky-mobile-cta" aria-label="Mobile quick actions">
    <div class="cta-btn-group">
      <a href="tel:+919811000000" class="cta-btn btn-call">Call Designer</a>
      <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+consultation." class="cta-btn btn-wa" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
  </aside>

  <!-- Main Content -->
  <main id="main-content">

    <!-- 1. LIVSPACE SPLIT HERO: EDITORIAL TEXT & CONSULTATION LEFT + JAW-DROPPING PHOTOGRAPHY RIGHT -->
    <section class="hero-livspace">
      <div class="container hero-layout">
        
        <!-- Left Column: Copy, USPs, & Integrated Lead Capture -->
        <div class="hero-headline">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 1.2rem;">
            ✦ Certified Modular Interior Studio · Delhi NCR
          </div>
          <h1>
            Complete Home Interiors &amp; <span class="highlight">Modular Woodwork</span><span class="logo-dot">.</span>
          </h1>
          <p class="hero-subhead">
            Factory-crafted modular kitchens, custom floor-to-ceiling wardrobes, and turnkey home interiors across South Delhi, Gurugram &amp; Noida. 45-day move-in guaranteed.
          </p>

          <!-- Livspace USPs -->
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
              <span>✦ Book Free 3D Design Session</span>
            </div>
            <p class="consult-sub">Speak with our senior design director within 2 hours. Zero commitment.</p>

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
                    <input type="tel" id="client-phone" name="phone" class="form-control" placeholder="+91 98765 43210" required>
                  </div>
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

                <button type="submit" id="submit-quote-btn" class="btn btn-primary btn-block" style="padding: 0.95rem; font-size: 0.95rem; margin-top: 0.3rem;">
                  Book Free 3D Design Session
                </button>

                <div class="hero-card-trust" style="margin-top: 0.6rem; font-size: 0.74rem;">
                  <span>🔒 100% Privacy Protected · Zero Spam Calls · Callback within 2 hours</span>
                </div>
              </div>

              <!-- Success State -->
              <div class="form-success-state" style="display: none; text-align: center; padding: 1.5rem 0;">
                <div style="font-size: 2.5rem; color: var(--color-green); margin-bottom: 0.4rem;">✓</div>
                <h3 style="color: var(--color-dark); margin-bottom: 0.3rem;">Thank you, <span class="client-name-display">there</span>!</h3>
                <p style="color: var(--color-muted); font-size: 0.88rem; margin-bottom: 1rem;">Our lead designer will connect with you within 2 hours to confirm your 3D session.</p>
                <a href="#" class="btn btn-primary wa-direct-link" target="_blank" rel="noopener noreferrer">Send Details on WhatsApp</a>
              </div>
            </form>
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
            <span class="icon">📍</span>
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
    </section>

    <!-- 2. TRUST METRIC STRIP -->
    <section class="trust-strip">
      <div class="container trust-strip-grid">
        <div class="trust-item">
          <h4>500<span>+</span></h4>
          <p>Homes Delivered in Delhi NCR</p>
        </div>
        <div class="trust-item">
          <h4>45<span> Days</span></h4>
          <p>Move-In Delivery Guarantee</p>
        </div>
        <div class="trust-item">
          <h4>10<span> Years</span></h4>
          <p>Material &amp; Hardware Warranty</p>
        </div>
        <div class="trust-item">
          <h4>0<span>%</span></h4>
          <p>No-Cost EMI Options Available</p>
        </div>
      </div>
    </section>

    <!-- 3. SERVICES SCROLLING MARQUEE TICKER (Continuous Loop) -->
    <div class="services-marquee-wrap" aria-hidden="true">
      <div class="marquee-track">
        <span class="marquee-item"><span class="dot">✦</span> Modular Kitchen</span>
        <span class="marquee-item"><span class="dot">✦</span> Custom Wardrobes</span>
        <span class="marquee-item"><span class="dot">✦</span> Wall Paneling &amp; TV Units</span>
        <span class="marquee-item"><span class="dot">✦</span> Fluted Charcoal Panels</span>
        <span class="marquee-item"><span class="dot">✦</span> Designer Doors &amp; Partitions</span>
        <span class="marquee-item"><span class="dot">✦</span> Gypsum False Ceiling</span>
        <span class="marquee-item"><span class="dot">✦</span> Concealed Electrical &amp; Plumbing</span>
        <span class="marquee-item"><span class="dot">✦</span> PU &amp; Duco Paints</span>
        <span class="marquee-item"><span class="dot">✦</span> Bespoke Teak Mandir</span>
        <span class="marquee-item"><span class="dot">✦</span> Full Home Turnkey Interiors</span>
        <span class="marquee-item"><span class="dot">✦</span> Study Desks &amp; Storage</span>

        <!-- Duplicated for continuous smooth loop -->
        <span class="marquee-item"><span class="dot">✦</span> Modular Kitchen</span>
        <span class="marquee-item"><span class="dot">✦</span> Custom Wardrobes</span>
        <span class="marquee-item"><span class="dot">✦</span> Wall Paneling &amp; TV Units</span>
        <span class="marquee-item"><span class="dot">✦</span> Fluted Charcoal Panels</span>
        <span class="marquee-item"><span class="dot">✦</span> Designer Doors &amp; Partitions</span>
        <span class="marquee-item"><span class="dot">✦</span> Gypsum False Ceiling</span>
        <span class="marquee-item"><span class="dot">✦</span> Concealed Electrical &amp; Plumbing</span>
        <span class="marquee-item"><span class="dot">✦</span> PU &amp; Duco Paints</span>
        <span class="marquee-item"><span class="dot">✦</span> Bespoke Teak Mandir</span>
        <span class="marquee-item"><span class="dot">✦</span> Full Home Turnkey Interiors</span>
        <span class="marquee-item"><span class="dot">✦</span> Study Desks &amp; Storage</span>
      </div>
    </div>

    <!-- 4. VISUAL SERVICES SHOWCASE GRID (WHAT WE DO) -->
    <section class="services-visual-section" id="what-we-do">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            ✦ Everything Your Home Needs
          </div>
          <h2>Our Core Interior &amp; Modular Services<span class="logo-dot">.</span></h2>
          <p>Every element built with certified materials in our own South Delhi factory. Zero sub-contractor shortcuts.</p>
        </div>

        <div class="services-visual-grid">
          
          <!-- 1. Modular Kitchens -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-kitchen.webp" type="image/webp">
                <img src="/assets/images/service-kitchen.jpg" alt="Modular Kitchen Design in Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Starting ₹1.8 Lakh</span>
            </div>
            <div class="service-visual-body">
              <h3>Modular Kitchens</h3>
              <p>L-shaped, parallel, and island layouts built in 100% BWP marine plywood with quartz countertops and German soft-close tandem drawers.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">BWP 710 Marine Ply</span>
                <span class="service-visual-pill">Hettich Tandem Box</span>
                <span class="service-visual-pill">Quartz Slabs</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>₹1.8L</strong></div>
                <a href="/modular-kitchen-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>

          <!-- 2. Custom Wardrobes -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-wardrobe.webp" type="image/webp">
                <img src="/assets/images/service-wardrobe.jpg" alt="Custom Wardrobe Designs in Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Starting ₹75,000</span>
            </div>
            <div class="service-visual-body">
              <h3>Custom Wardrobes &amp; Closets</h3>
              <p>Floor-to-ceiling top-hung sliding wardrobes, walk-in closets, and hinged almirahs with sensor profile lighting and hydraulic storage beds.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">Top-Hung Sliding</span>
                <span class="service-visual-pill">Walk-in Closets</span>
                <span class="service-visual-pill">Sensor Lights</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>₹75K</strong></div>
                <a href="/wardrobe-design-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>

          <!-- 3. Full Home Interiors -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-fullhome.webp" type="image/webp">
                <img src="/assets/images/service-fullhome.jpg" alt="Full Home Turnkey Interiors Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Starting ₹5.5 Lakh</span>
            </div>
            <div class="service-visual-body">
              <h3>Full Home Turnkey Interiors</h3>
              <p>Complete 2, 3, 4 BHK and villa transformations. Turnkey management from 3D renders to modular woodwork, civil, electrical, and handover.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">45-Day Handover</span>
                <span class="service-visual-pill">10-Year Warranty</span>
                <span class="service-visual-pill">Dedicated Manager</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>₹5.5L</strong></div>
                <a href="/full-home-interior-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>

          <!-- 4. Wall Paneling & TV Units -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-paneling.webp" type="image/webp">
                <img src="/assets/images/service-paneling.jpg" alt="Wall Paneling and TV Units Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Starting ₹45,000</span>
            </div>
            <div class="service-visual-body">
              <h3>Wall Paneling &amp; TV Units</h3>
              <p>Architectural charcoal louvers, acoustic fluted slats, PVC/WPC cladding, natural smoked veneers, and floating TV consoles with warm LED backlighting.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">Charcoal Louvers</span>
                <span class="service-visual-pill">Fluted Slats</span>
                <span class="service-visual-pill">Floating Consoles</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>₹45K</strong></div>
                <a href="/wall-paneling-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>

          <!-- 5. False Ceilings & Lighting -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-ceiling.webp" type="image/webp">
                <img src="/assets/images/service-ceiling.jpg" alt="False Ceiling and Lighting Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Starting ₹95/sq.ft</span>
            </div>
            <div class="service-visual-body">
              <h3>False Ceilings &amp; Lighting</h3>
              <p>Saint-Gobain gypsum false ceilings, perimeter warm cove lighting (3000K), magnetic architectural track lights, and dimmable COB spotlight channels.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">Saint-Gobain Gypsum</span>
                <span class="service-visual-pill">Warm Cove 3000K</span>
                <span class="service-visual-pill">Magnetic Tracks</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>₹95/sq.ft</strong></div>
                <a href="/false-ceiling-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>

          <!-- 6. Doors & Partitions -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-doors.webp" type="image/webp">
                <img src="/assets/images/service-doors.jpg" alt="Doors and Partitions Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Starting ₹28,000</span>
            </div>
            <div class="service-visual-body">
              <h3>Doors &amp; Architectural Partitions</h3>
              <p>Heavy solid wood entry doors, sliding fluted glass dividers, pocket doors, and CNC-cut backlit wooden jali room partitions with concealed hardware.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">Fluted Glass Dividers</span>
                <span class="service-visual-pill">CNC Backlit Jali</span>
                <span class="service-visual-pill">Heavy Hinges</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>₹28K</strong></div>
                <a href="/doors-partitions-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>

          <!-- 7. Bespoke Furniture & Study -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-furniture.webp" type="image/webp">
                <img src="/assets/images/service-furniture.jpg" alt="Study Desks and Custom Furniture Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Starting ₹35,000</span>
            </div>
            <div class="service-visual-body">
              <h3>Bespoke Furniture &amp; Study Desks</h3>
              <p>Ergonomic built-in study tables, L-shaped workstations, floor-to-ceiling bookshelves, crockery units, shoe consoles, and bespoke teak pooja mandirs.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">Ergonomic Desks</span>
                <span class="service-visual-pill">Bookshelves</span>
                <span class="service-visual-pill">Teak Pooja Mandirs</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>₹35K</strong></div>
                <a href="/bedroom-furniture-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>

          <!-- 8. Painting & Luxury Polish -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-painting.webp" type="image/webp">
                <img src="/assets/images/service-painting.jpg" alt="Painting and PU Polishing Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Starting ₹25/sq.ft</span>
            </div>
            <div class="service-visual-body">
              <h3>Painting &amp; PU Polish</h3>
              <p>Asian Paints Royale luxury emulsion, Italian polyurethane (PU) wood finishes, satin Duco spray lacquers, and damp-proof wall treatments.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">Asian Paints Royale</span>
                <span class="service-visual-pill">Italian PU Polish</span>
                <span class="service-visual-pill">Duco Lacquers</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>₹25/sq.ft</strong></div>
                <a href="/painting-polishing-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>

          <!-- 9. Plumbing & Electrical MEP -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-electrical.webp" type="image/webp">
                <img src="/assets/images/service-electrical.jpg" alt="Plumbing and Electrical MEP Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Turnkey Included</span>
            </div>
            <div class="service-visual-body">
              <h3>Plumbing &amp; Electrical MEP</h3>
              <p>Concealed fire-retardant 4 sq mm copper wiring, modular switchboards, leak-proof CPVC plumbing lines, sanitaryware fitting, and waterproofing.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">4mm Fire-Proof Wiring</span>
                <span class="service-visual-pill">CPVC Piping</span>
                <span class="service-visual-pill">Luxury Sanitaryware</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>Turnkey</strong></div>
                <a href="/plumbing-electrical-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 5. MATERIAL SHOWCASE ("QUALITY YOU CAN FEEL") -->
    <section class="material-showcase-section">
      <div class="container">
        <div class="section-title-wrap">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.75rem;">
            ✦ Certified Materials
          </div>
          <h2>Quality You Can Feel<span class="logo-dot">.</span></h2>
          <p>Every single board, hinge, and countertop we specify is chosen for longevity, finish quality, and suitability to the Indian climate. Zero cheap substitutions.</p>
        </div>

        <div class="materials-grid">
          
          <div class="material-card">
            <div class="material-icon-wrap">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
            </div>
            <h3>BWP 710 Marine Plywood</h3>
            <p>Boiling Water Proof marine ply bonded with synthetic phenolic resins. Withstands 72 hours of boiling water without delamination.</p>
            <span class="material-spec-pill">Wet Area Certified</span>
          </div>

          <div class="material-card">
            <div class="material-icon-wrap">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <h3>HDMR &amp; WPC Boards</h3>
            <p>Termite-proof, high-density moisture-resistant boards ideal for bathroom vanities, CNC jalis, and high-humidity rooms.</p>
            <span class="material-spec-pill">100% Termite Proof</span>
          </div>

          <div class="material-card">
            <div class="material-icon-wrap">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
            </div>
            <h3>Hettich &amp; Blum Hardware</h3>
            <p>German-engineered soft-close hinges, tandem box drawer runners, and hydraulic lift systems with a 10-year official warranty.</p>
            <span class="material-spec-pill">German Engineering</span>
          </div>

          <div class="material-card">
            <div class="material-icon-wrap">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </div>
            <h3>Merino &amp; Greenlam Laminates</h3>
            <p>Premium 1.0mm/1.5mm anti-scratch laminates and high-gloss acrylic shutters available in over 500+ textures.</p>
            <span class="material-spec-pill">Scratch-Resistant</span>
          </div>

          <div class="material-card">
            <div class="material-icon-wrap">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 3h12l4 6-10 12L2 9z"/></svg>
            </div>
            <h3>Stain-Proof Quartz Countertops</h3>
            <p>Non-porous, antibacterial Calacatta and engineered quartz slabs impervious to turmeric stains, heat, and heavy use.</p>
            <span class="material-spec-pill">Stain &amp; Acid Proof</span>
          </div>

        </div>
      </div>
    </section>

    <!-- 6. INTERACTIVE COST CALCULATOR (LIVSPACE ESTIMATOR WIDGET) -->
    <section class="calculator-livspace-section" id="estimator">
      <div class="container">
        
        <div class="calc-header-box">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            Instant Estimate
          </div>
          <h2>Interactive Interior Cost Calculator<span class="logo-dot">.</span></h2>
          <p>Get a realistic price estimate for your home in Delhi NCR based on room size, scope, and finish package.</p>
        </div>

        <div class="calculator-grid" id="livspace-calculator">
          
          <!-- Controls Left -->
          <div class="calc-controls-card">
            
            <!-- Step 1: BHK Selector -->
            <div class="calc-group">
              <label class="calc-label">1. Select Apartment BHK Size</label>
              <div class="pill-toggle-group">
                <button type="button" class="calc-pill-btn" data-type="bhk" data-val="1 BHK">1 BHK</button>
                <button type="button" class="calc-pill-btn active" data-type="bhk" data-val="2 BHK">2 BHK</button>
                <button type="button" class="calc-pill-btn" data-type="bhk" data-val="3 BHK">3 BHK</button>
                <button type="button" class="calc-pill-btn" data-type="bhk" data-val="4 BHK+">4 BHK+ / Villa</button>
              </div>
            </div>

            <!-- Step 2: Scope Selector -->
            <div class="calc-group">
              <label class="calc-label">2. Select Scope of Work</label>
              <div class="pill-toggle-group">
                <button type="button" class="calc-pill-btn active" data-type="scope" data-val="Full Home">Full Home</button>
                <button type="button" class="calc-pill-btn" data-type="scope" data-val="Kitchen Only">Kitchen Only</button>
                <button type="button" class="calc-pill-btn" data-type="scope" data-val="Wardrobes Only">Wardrobes Only</button>
                <button type="button" class="calc-pill-btn" data-type="scope" data-val="Living Room">Living Room</button>
              </div>
            </div>

            <!-- Step 3: Package Tier -->
            <div class="calc-group">
              <label class="calc-label">3. Select Material Package</label>
              <div class="pill-toggle-group">
                <button type="button" class="calc-pill-btn" data-type="package" data-val="Essential">Essential (Smart / Rental)</button>
                <button type="button" class="calc-pill-btn active" data-type="package" data-val="Premium">Premium (Most Popular)</button>
                <button type="button" class="calc-pill-btn" data-type="package" data-val="Luxe">Luxe (Architectural)</button>
              </div>
            </div>

          </div>

          <!-- Dynamic Result Box Right -->
          <div class="calc-result-box">
            <div class="estimate-label">Estimated Cost Range</div>
            <div class="estimate-price" id="calc-price-display">₹7.2L – ₹10.5L</div>
            <p class="note" id="calc-note-display">*Includes ISI Marine BWP ply, anti-scratch acrylic / PU, Hettich soft-close tandem drawers, 3D designs, GST &amp; 10-yr warranty.</p>

            <div style="background: rgba(255, 241, 242, 0.6); border: 1px dashed var(--color-primary-subtle); border-radius: var(--radius-md); padding: 0.85rem; margin-bottom: 1.5rem; text-align: center;">
              <span style="font-size: 0.85rem; font-weight: 700; color: var(--color-primary);">💳 EMI starting from ₹11,200/month with 0% interest options</span>
            </div>

            <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+calculated+an+estimate+for+my+home+and+want+a+detailed+breakdown." class="btn btn-primary btn-block" style="padding: 1rem;" target="_blank" rel="noopener noreferrer" id="calc-wa-btn">
              Get Itemized Quotation on WhatsApp
            </a>
            <a href="/contact/" class="btn btn-outline btn-block" style="margin-top: 0.75rem; padding: 0.85rem;">
              Book Free Site Measurement
            </a>
          </div>

        </div>

      </div>
    </section>

    <!-- 7. ROOM DESIGN EXPLORER (TABBED FILTER) -->
    <section class="room-explorer-section">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            Design Ideas
          </div>
          <h2>Explore Designs Room-by-Room<span class="logo-dot">.</span></h2>
          <p>Get inspired by our verified modular layouts crafted for urban Delhi NCR homes.</p>
        </div>

        <!-- Room Tabs -->
        <div class="room-tabs-bar" role="tablist">
          <button class="room-tab-btn active" data-room-target="all">All Designs</button>
          <button class="room-tab-btn" data-room-target="kitchen">Modular Kitchens</button>
          <button class="room-tab-btn" data-room-target="bedroom">Master Bedrooms</button>
          <button class="room-tab-btn" data-room-target="living">Living &amp; Dining</button>
          <button class="room-tab-btn" data-room-target="wardrobe">Custom Wardrobes</button>
        </div>

        <!-- Room Cards Grid -->
        <div class="room-cards-grid">
          
          <div class="room-card" data-room="kitchen">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-kitchen.webp" type="image/webp">
                <img src="/assets/images/portfolio-kitchen.jpg" alt="L-Shaped Acrylic Kitchen in Greater Kailash" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Kitchen</span>
            </div>
            <div class="room-card-body">
              <h3>Matte Acrylic Modular Kitchen</h3>
              <p>Calacatta quartz countertop with German soft-close tandem drawers.</p>
              <div class="room-card-footer">
                <div class="price-chip">Starting At <strong>₹2.8 Lakh</strong></div>
                <a href="/modular-kitchen-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">Get This Look</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="bedroom">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-bedroom.webp" type="image/webp">
                <img src="/assets/images/portfolio-bedroom.jpg" alt="Master Suite with Sliding Wardrobe in Panchsheel Park" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Bedroom</span>
            </div>
            <div class="room-card-body">
              <h3>Contemporary Master Suite</h3>
              <p>Floor-to-ceiling tinted glass sliding wardrobe with hydraulic storage bed.</p>
              <div class="room-card-footer">
                <div class="price-chip">Starting At <strong>₹1.5 Lakh</strong></div>
                <a href="/wardrobe-design-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">Get This Look</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="living">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-tvunit.webp" type="image/webp">
                <img src="/assets/images/portfolio-tvunit.jpg" alt="Fluted Charcoal TV Wall in Gurugram" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Living Room</span>
            </div>
            <div class="room-card-body">
              <h3>Fluted Charcoal Media Wall</h3>
              <p>Acoustic louvers with floating marble console and warm profile lights.</p>
              <div class="room-card-footer">
                <div class="price-chip">Starting At <strong>₹75,000</strong></div>
                <a href="/wall-paneling-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">Get This Look</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="kitchen">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-kitchen-2.webp" type="image/webp">
                <img src="/assets/images/portfolio-kitchen-2.jpg" alt="Parallel Modular Kitchen in Gurugram" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Kitchen</span>
            </div>
            <div class="room-card-body">
              <h3>Monochrome Parallel Kitchen</h3>
              <p>Anti-fingerprint matte black finish with quartz worktops and tall pantry.</p>
              <div class="room-card-footer">
                <div class="price-chip">Starting At <strong>₹3.2 Lakh</strong></div>
                <a href="/modular-kitchen-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">Get This Look</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="wardrobe">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-wardrobe-2.webp" type="image/webp">
                <img src="/assets/images/portfolio-wardrobe-2.jpg" alt="Walk-in Wardrobe in Jor Bagh" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Wardrobe</span>
            </div>
            <div class="room-card-body">
              <h3>His &amp; Her Luxury Walk-In</h3>
              <p>Velvet-lined jewellery drawers, sensor lighting, and smoked glass shutters.</p>
              <div class="room-card-footer">
                <div class="price-chip">Starting At <strong>₹1.8 Lakh</strong></div>
                <a href="/wardrobe-design-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">Get This Look</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="living">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-dining.webp" type="image/webp">
                <img src="/assets/images/portfolio-dining.jpg" alt="Open Concept Dining &amp; Living in Vasant Vihar" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Dining</span>
            </div>
            <div class="room-card-body">
              <h3>Open Concept Living &amp; Dining</h3>
              <p>Warm coffer ceiling with architectural track lighting and veneer cladding.</p>
              <div class="room-card-footer">
                <div class="price-chip">Starting At <strong>₹2.2 Lakh</strong></div>
                <a href="/full-home-interior-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">Get This Look</a>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- 8. WHY DELHI INTERIOR VS LOCAL CONTRACTORS -->
    <section class="comparison-livspace-section">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            Clear Advantage
          </div>
          <h2>Why 500+ Homeowners Pick Us Over Local Contractors<span class="logo-dot">.</span></h2>
          <p>No sudden budget surprises, no infinite delays, and zero counterfeit materials.</p>
        </div>

        <div style="overflow-x: auto;">
          <table class="comparison-table-livspace">
            <thead>
              <tr>
                <th>Parameters</th>
                <th class="brand-col">Delhi Interior</th>
                <th class="contractor-col">Local Contractors</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Cabinetry Finish</strong></td>
                <td class="brand-col">Factory CNC Beam Saw &amp; Edge Banding</td>
                <td class="contractor-col">Manual Hand Saw (Chipped Edges)</td>
              </tr>
              <tr>
                <td><strong>Pricing Transparency</strong></td>
                <td class="brand-col">100% Fixed in Writing (Zero Escalation)</td>
                <td class="contractor-col">Surprise 30% to 50% Cost Escalations</td>
              </tr>
              <tr>
                <td><strong>Warranty &amp; Service</strong></td>
                <td class="brand-col">10-Year Comprehensive Written Warranty</td>
                <td class="contractor-col">Disappears After Final Payment</td>
              </tr>
              <tr>
                <td><strong>Handover Timeline</strong></td>
                <td class="brand-col">45-Day Guaranteed Handover (With Penalty)</td>
                <td class="contractor-col">Endless Delays (6 to 9 Months Average)</td>
              </tr>
              <tr>
                <td><strong>Material Authenticity</strong></td>
                <td class="brand-col">Certified 710 BWP Marine Ply &amp; German Hardware</td>
                <td class="contractor-col">Cheap Commercial Grade MR Plywood</td>
              </tr>
              <tr>
                <td><strong>3D Design Visualization</strong></td>
                <td class="brand-col">Photorealistic 3D Renders Before Build</td>
                <td class="contractor-col">Rough Hand Pencil Sketches</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- 9. HOW IT WORKS (3-STEP SIMPLE PROCESS) -->
    <section class="how-it-works-section">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            Smooth Execution
          </div>
          <h2>Your Dream Home in 3 Simple Steps<span class="logo-dot">.</span></h2>
          <p>We've eliminated the stress from home interiors with an automated, milestone-tracked process.</p>
        </div>

        <div class="process-steps-grid">
          
          <div class="process-step-card">
            <div class="step-number">01</div>
            <h3>Free Consultation &amp; 3D Design</h3>
            <p>Meet our senior interior designer, share your floor plan, and receive custom 3D views and an itemized BOQ.</p>
            <span class="step-time">Days 1 – 7</span>
          </div>

          <div class="process-step-card">
            <div class="step-number">02</div>
            <h3>Factory Modular Fabrication</h3>
            <p>Your modular cabinetry is precision-cut and edge-banded in our factory with German machinery while civil MEP runs on-site.</p>
            <span class="step-time">Days 8 – 35</span>
          </div>

          <div class="process-step-card">
            <div class="step-number">03</div>
            <h3>Installation &amp; 45-Day Handover</h3>
            <p>Pre-finished modules are installed on-site, undergo 146 quality checks, deep cleaning, and your official 10-year warranty is issued.</p>
            <span class="step-time">Days 36 – 45</span>
          </div>

        </div>
      </div>
    </section>

    <!-- 10. REAL HOMES DELIVERED (CLIENT TESTIMONIALS) -->
    <section class="testimonials-livspace">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            Verified Homeowners
          </div>
          <h2>Hear From Delhi NCR Families Who Love Their Homes<span class="logo-dot">.</span></h2>
          <p>Over 500+ apartments, builder floors, and villas handed over on time.</p>
        </div>

        <div class="testimonials-grid">
          
          <div class="testimonial-card">
            <div class="rating-stars">★★★★★</div>
            <p class="quote">"Delhi Interior transformed our 3 BHK in GK-2 completely within 42 days. The kitchen finish is indistinguishable from German imported kitchens at one-third the price."</p>
            <div class="client-meta">
              <strong>Vikram &amp; Ritu Mehra</strong>
              <span>Greater Kailash II · 3 BHK Full Home Interior</span>
            </div>
          </div>

          <div class="testimonial-card">
            <div class="rating-stars">★★★★★</div>
            <p class="quote">"The fluted charcoal wall paneling and floor-to-ceiling tinted glass wardrobes in our master bedroom get compliments from everyone. Zero hidden costs."</p>
            <div class="client-meta">
              <strong>Ananya Sharma</strong>
              <span>DLF Phase 5, Gurugram · 4 BHK Penthouse</span>
            </div>
          </div>

          <div class="testimonial-card">
            <div class="rating-stars">★★★★★</div>
            <p class="quote">"Having one point of contact for carpentry, false ceiling, plumbing, and Asian Paints Royale polish made this whole renovation completely hassle-free."</p>
            <div class="client-meta">
              <strong>Rajesh Singhal</strong>
              <span>Vasant Vihar · Complete Turnkey Renovation</span>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 11. FAQ ACCORDION -->
    <section class="faq-section">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            Got Questions?
          </div>
          <h2>Frequently Asked Questions<span class="logo-dot">.</span></h2>
          <p>Everything you need to know about our modular interior design service in Delhi NCR.</p>
        </div>

        <div class="faq-accordion-list">
          
          <div class="faq-item">
            <button class="faq-question" type="button">
              <span>What is included in the 45-day move-in guarantee?</span>
              <span class="toggle-icon">+</span>
            </button>
            <div class="faq-answer">
              <p>Our 45-day guarantee starts from the day 3D designs and floor plans are approved and the site is handed over. If we delay handover beyond 45 days, we pay a financial penalty for every day of delay. Standard terms apply.</p>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" type="button">
              <span>What plywood brands and grades do you use?</span>
              <span class="toggle-icon">+</span>
            </button>
            <div class="faq-answer">
              <p>We strictly use certified IS:710 Boiling Water Proof (BWP) marine grade plywood for all wet areas (kitchens and bathroom vanities) and IS:303 MR grade for dry areas, sourced from top manufacturers like CenturyPly and Greenply.</p>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" type="button">
              <span>How does your 10-year warranty work?</span>
              <span class="toggle-icon">+</span>
            </button>
            <div class="faq-answer">
              <p>Our 10-year warranty covers all factory modular woodwork against delamination, borer, and termite attacks, along with manufacturer warranties on Hettich and Blum soft-close tandem drawers and hinges.</p>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" type="button">
              <span>Do you handle electrical, plumbing, and civil work too?</span>
              <span class="toggle-icon">+</span>
            </button>
            <div class="faq-answer">
              <p>Yes. We provide complete turnkey MEP execution — including concealed 4mm fire-retardant wiring, switchboards, CPVC piping, bathroom sanitaryware, and Asian Paints Royale painting.</p>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" type="button">
              <span>Can I visit your Experience Centre in South Delhi?</span>
              <span class="toggle-icon">+</span>
            </button>
            <div class="faq-answer">
              <p>Yes! Our South Extension Part II Experience Centre is open Monday to Saturday from 9:00 AM to 7:00 PM. You can explore full-scale modular kitchens, wardrobe mechanisms, and 500+ material swatches in person.</p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 12. HIGH-IMPACT FINAL CTA BANNER -->
    <section class="cta-banner-section">
      <div class="container cta-banner-box">
        <h2>Bring Home Interiors That Inspire You Every Day<span class="logo-dot">.</span></h2>
        <p>Book your free 3D design consultation with Delhi's top modular interior studio. Get a complete itemized BOQ with 0% EMI options.</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.5rem;">
          <a href="/contact/" class="btn btn-primary" style="background-color: #FFFFFF; color: var(--color-primary); font-weight: 700; padding: 1rem 2.2rem;">
            Book Free Consultation
          </a>
          <a href="https://wa.me/919811000000?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+design+consultation." class="btn btn-outline" style="border-color: #FFFFFF; color: #FFFFFF; padding: 1rem 2.2rem;" target="_blank" rel="noopener noreferrer">
            Chat on WhatsApp
          </a>
        </div>
      </div>
    </section>

  </main>

  <!-- Modern Livspace Footer -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="site-logo" style="margin-bottom: 1rem;">
            Delhi Interior<span class="logo-dot">.</span>
          </div>
          <p>Delhi NCR's trusted modular interior brand. Delivering precision kitchens, wardrobes, and full-home turnkey transformations backed by a 10-year warranty.</p>
          <div style="display: flex; gap: 0.75rem; margin-top: 1.2rem; font-size: 0.85rem;">
            <a href="https://instagram.com/delhiinterior" style="color: #9CA3AF;" aria-label="Instagram">Instagram</a> ·
            <a href="https://facebook.com/delhiinterior" style="color: #9CA3AF;" aria-label="Facebook">Facebook</a> ·
            <a href="https://youtube.com/delhiinterior" style="color: #9CA3AF;" aria-label="YouTube">YouTube</a>
          </div>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Our Services</h4>
          <ul class="footer-links">
            <li><a href="/modular-kitchen-delhi/">Modular Kitchens</a></li>
            <li><a href="/wardrobe-design-delhi/">Custom Wardrobes</a></li>
            <li><a href="/full-home-interior-delhi/">Full Home Turnkey</a></li>
            <li><a href="/wall-paneling-delhi/">Wall Paneling &amp; TV Units</a></li>
            <li><a href="/false-ceiling-delhi/">False Ceiling &amp; Lights</a></li>
            <li><a href="/doors-partitions-delhi/">Doors &amp; Partitions</a></li>
            <li><a href="/bedroom-furniture-delhi/">Study Desks &amp; Storage</a></li>
            <li><a href="/painting-polishing-delhi/">Painting &amp; PU Polish</a></li>
            <li><a href="/plumbing-electrical-delhi/">Plumbing &amp; Electrical MEP</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Explore</h4>
          <ul class="footer-links">
            <li><a href="/#estimator">Cost Calculator</a></li>
            <li><a href="/portfolio/">Design Gallery</a></li>
            <li><a href="/process/">Our 45-Day Process</a></li>
            <li><a href="/about/">About Our Studio</a></li>
            <li><a href="/blog/">Interior Design Guides</a></li>
            <li><a href="/sitemap/">HTML Sitemap</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Experience Centre</h4>
          <p style="margin-bottom: 0.5rem; color: #D1D5DB;">Ring Road, South Extension Part II<br>New Delhi, Delhi 110049</p>
          <p style="margin-bottom: 0.5rem; color: #D1D5DB;">Mon–Sat: 9:00 AM – 7:00 PM</p>
          <p style="margin-bottom: 1rem;"><a href="tel:+919811000000" style="color: #FFFFFF; font-weight: 700; text-decoration: none;">+91 98110 00000</a></p>
          <a href="/contact/" class="btn btn-outline" style="border-color: #4B5563; color: #FFFFFF; font-size: 0.85rem; padding: 0.6rem 1.2rem;">Visit Experience Centre</a>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> Delhi Interior. All rights reserved. GST Registered.</p>
        <div class="footer-legal-links">
          <a href="/privacy-policy/">Privacy Policy</a>
          <a href="/terms-of-service/">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Cookie Banner -->
  <aside id="cookie-banner" class="cookie-banner" aria-label="Cookie consent">
    <div class="cookie-content">
      <p>We use essential cookies to personalize design estimates and enhance your browsing experience. By using our website, you agree to our <a href="/privacy-policy/">Privacy Policy</a>.</p>
      <div class="cookie-actions">
        <button id="cookie-accept" class="btn btn-primary" style="padding: 0.5rem 1.2rem; font-size: 0.82rem;">Accept</button>
        <button id="cookie-decline" class="btn btn-outline" style="padding: 0.5rem 1.2rem; font-size: 0.82rem;">Decline</button>
      </div>
    </div>
  </aside>

  <script src="/assets/js/main.js" defer></script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# Also update scripts/build_home.py so future regenerations preserve this
with open('scripts/build_home.py', 'w', encoding='utf-8') as f:
    f.write(f'''import os, json

home_schema = {json.dumps(home_schema, indent=4)}

html_content = \'\'\'{html_content}\'\'\'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("[SUCCESS] index.html rebuilt with real interior visual, Marquee, What We Do, Material Showcase, and Livspace layout!")
''')

print('[SUCCESS] Rebuilt index.html with Livspace-standard split hero, giant architectural photo, and 3x3 visual services grid.')
