import json

home_schema = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Delhi Interior",
    "image": "https://delhiinterior.com/og-image.jpg",
    "url": "https://delhiinterior.com/",
    "telephone": "+919643817099",
    "email": "hello@delhiinterior.com",
    "priceRange": "₹₹₹",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "F-128/4, Mohammadpur",
        "addressLocality": "New Delhi",
        "addressRegion": "Delhi",
        "postalCode": "110066",
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
  <title>Interior Designers in Delhi NCR | Delhi Interior — Home Styling &amp; Modular Studio</title>
  <meta name="description" content="Delhi's premier residential &amp; commercial interior design studio. Complete turnkey execution from start to finish, 100% budget transparency, 3D designs &amp; 45-day handover.">
  <link rel="canonical" href="https://delhiinterior.com/">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Interior Designers in Delhi NCR | Delhi Interior">
  <meta property="og:description" content="Complete turnkey execution from start to finish, 100% budget transparency, 3D designs &amp; 45-day handover.">
  <meta property="og:url" content="https://delhiinterior.com/">
  <meta property="og:image" content="https://delhiinterior.com/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_IN">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Interior Designers in Delhi NCR | Delhi Interior">
  <meta name="twitter:description" content="Premier residential &amp; commercial interior design studio in Delhi NCR. 45-day handover guarantee.">
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

  <script type="application/ld+json">
{json.dumps(home_schema, indent=2)}
  </script>
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
        <span>Open 24 Hours</span>
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
        <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+consult+for+my+home+interior." class="top-utility-link" target="_blank" rel="noopener noreferrer">
          <span>💬 WhatsApp Designer</span>
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
          <li><a href="/" class="active">Home</a></li>
          <li><a href="/about/">About Us</a></li>
          <li><a href="/portfolio/">Projects</a></li>
          <li class="nav-dropdown-item">
            <a href="/modular-kitchen-delhi/" class="nav-dropdown-trigger">
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
    </section>

    <!-- 2. TRUST METRIC STRIP -->
    <section class="trust-strip">
      <div class="container trust-strip-grid">
        <div class="trust-item">
          <h4>17<span>+ Years</span></h4>
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
    </section>

    <!-- 3. DUAL SPECIALIZATION: RESIDENTIAL & COMMERCIAL DESIGN (KD Signature Feature) -->
    <section style="padding: 4.5rem 0; background: #FFFFFF;">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            ✦ Tailored Spatial Solutions
          </div>
          <h2>Residential &amp; Commercial Interior Designing<span class="logo-dot">.</span></h2>
          <p>Whether you need a classy, functional home or an innovative, brand-elevating workspace, our team has you covered.</p>
        </div>

        <div class="dual-specialty-grid">
          <!-- Card 1: Residential -->
          <div class="specialty-card">
            <picture>
              <source srcset="/assets/images/service-fullhome.webp" type="image/webp">
              <img src="/assets/images/service-fullhome.jpg" alt="Residential Interior Designing Delhi NCR" width="800" height="500" loading="lazy">
            </picture>
            <div class="specialty-overlay"></div>
            <div class="specialty-content">
              <span class="specialty-tag">Residential Interior Designing</span>
              <h3>Bespoke Luxury For Your Home</h3>
              <p>Complete turnkey home transformations: modular kitchens, custom sliding wardrobes, bespoke woodwork &amp; precision carpentry, fluted wall paneling, and teakwood pooja mandirs crafted for urban Delhi living.</p>
              <a href="/full-home-interior-delhi/" class="btn btn-primary" style="padding: 0.75rem 1.6rem; font-size: 0.9rem;">Explore Residential Interiors</a>
            </div>
          </div>

          <!-- Card 2: Commercial -->
          <div class="specialty-card">
            <picture>
              <source srcset="/assets/images/portfolio-office.webp" type="image/webp">
              <img src="/assets/images/portfolio-office.jpg" alt="Commercial Interior Designing Delhi NCR" width="800" height="500" loading="lazy">
            </picture>
            <div class="specialty-overlay"></div>
            <div class="specialty-content">
              <span class="specialty-tag" style="background-color: #2563EB;">Commercial Interior Designing</span>
              <h3>Productive &amp; Inspiring Workspaces</h3>
              <p>Modern corporate offices, collaborative workstations, executive conference rooms, retail showrooms, and clinics that enhance team productivity and reflect your brand prestige.</p>
              <a href="/portfolio/" class="btn btn-primary" style="background-color: #2563EB; padding: 0.75rem 1.6rem; font-size: 0.9rem;">Explore Commercial Projects</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. UNIQUE SELLING POINTS (KD Signature Value Proposition) -->
    <section class="usps-section-kd">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            ✦ Why Delhi Homeowners Choose Us
          </div>
          <h2>Our Core Unique Selling Points<span class="logo-dot">.</span></h2>
          <p>Unlike designers who just provide sketches and disappear, we manage the entire execution with active supervision and budget discipline.</p>
        </div>

        <div class="usps-grid-kd">
          
          <!-- USP 1 -->
          <div class="usp-card-kd">
            <div class="usp-card-icon">
              <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            </div>
            <h3>Start to Finish Execution</h3>
            <p>Unlike designers who only provide 2D/3D sketches and leave you to coordinate carpenters, we manage the complete execution as per approved designs with daily progress checks and a single point of accountability.</p>
          </div>

          <!-- USP 2 -->
          <div class="usp-card-kd">
            <div class="usp-card-icon">
              <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
            </div>
            <h3>100% Budget Transparency</h3>
            <p>We provide comprehensive itemized cost breakdowns so you know where every single rupee is going. We share editable BOQ spreadsheets so you can customize material choices and control budgets without unexpected markups.</p>
          </div>

          <!-- USP 3 -->
          <div class="usp-card-kd">
            <div class="usp-card-icon">
              <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            </div>
            <h3>Realistic 3D &amp; AutoCAD Drawings</h3>
            <p>Architectural Working Drawings visualization and millimeter-accurate 2D AutoCAD working drawings for every room before on-site work begins, ensuring what you see on screen is exactly what is delivered on site.</p>
          </div>

          <!-- USP 4 -->
          <div class="usp-card-kd">
            <div class="usp-card-icon">
              <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
            </div>
            <h3>Material Selection &amp; Value Engineering</h3>
            <p>We explain the transparent pros and cons of BWP marine ply, HDMR, acrylic, veneer, and quartz. We guide you on where premium materials can be smart-swapped with budget materials without compromising aesthetics.</p>
          </div>

          <!-- USP 5 -->
          <div class="usp-card-kd">
            <div class="usp-card-icon">
              <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </div>
            <h3>End-to-End Renovation Under One Roof</h3>
            <p>Demolition, civil modifications, modular cabinetry, concealed electrical, plumbing, gypsum ceilings, Italian PU polish, and deep-clean styling under one single roof. We also handle manufacturer warranty claims on your behalf.</p>
          </div>

          <!-- USP 6 -->
          <div class="usp-card-kd">
            <div class="usp-card-icon">
              <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            </div>
            <h3>Timeline Justification &amp; Progress Checks</h3>
            <p>We provide a milestone-tracked project schedule and weekly photographic progress reports. If we delay handover beyond our 45-day commitment, we pay a financial penalty for every day of delay.</p>
          </div>

        </div>
      </div>
    </section>

    <!-- 5. WHY DO YOU NEED INTERIOR DESIGNERS IN DELHI NCR (KD Content Synthesis) -->
    <section class="why-need-section">
      <div class="container why-need-layout">
        <div class="why-need-content">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            ✦ Value Your Money &amp; Trust
          </div>
          <h2>Why Do You Need Professional Interior Designers in Delhi NCR?</h2>
          <p>
            Trusting someone with a ₹10 Lakh to ₹50 Lakh+ investment for building your home or office is a massive responsibility. In Delhi NCR, plenty of research is required to find an interior designer who will genuinely respect your budget and hard-earned money.
          </p>
          <p>
            Dealing directly with unorganized local contractors leads to endless delays (6 to 9 months average), unexpected 40% cost escalations, and counterfeit commercial plywood disguised as marine grade. Delhi Interior provides all the values and legal guarantees an interior partner needs to protect your peace of mind.
          </p>

          <div class="why-need-points">
            <div class="why-point-box">
              <span class="why-point-icon">✓</span>
              <div>
                <strong>Strategic Planning</strong>
                <span>Optimizing every square foot in Delhi apartments with vertical lofts and smart layouts.</span>
              </div>
            </div>
            <div class="why-point-box">
              <span class="why-point-icon">✓</span>
              <div>
                <strong>Suits Your Exact Budget</strong>
                <span>Editable BOQ spreadsheets letting you decide where to invest and where to save.</span>
              </div>
            </div>
            <div class="why-point-box">
              <span class="why-point-icon">✓</span>
              <div>
                <strong>Factory Precision Machinery</strong>
                <span>CNC beam saws and PUR hot-melt edge banding for flawless, chip-free finishes.</span>
              </div>
            </div>
            <div class="why-point-box">
              <span class="why-point-icon">✓</span>
              <div>
                <strong>Single Point Accountability</strong>
                <span>One dedicated site supervisor handles civil, carpentry, electrical, plumbing, and paint.</span>
              </div>
            </div>
          </div>
        </div>

        <div>
          <picture>
            <source srcset="/assets/images/about-workshop.webp" type="image/webp">
            <img src="/assets/images/about-workshop.jpg" alt="Delhi Interior Dedicated Woodworking Workshop in South Delhi" style="width: 100%; border-radius: 20px; box-shadow: 0 16px 45px rgba(0,0,0,0.12);" width="800" height="600" loading="lazy">
          </picture>
        </div>
      </div>
    </section>

<!-- 7. OUR AWESOME INTERIOR DESIGNING SERVICES (WHAT WE DO 3X3 VISUAL GRID) -->
    <section class="services-visual-section" id="what-we-do">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            ✦ Complete Range Of Interior Services
          </div>
          <h2>Our Awesome Interior Designing Services<span class="logo-dot">.</span></h2>
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

          <!-- 7. Custom Woodwork & Precision Carpentry -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-furniture.webp" type="image/webp">
                <img src="/assets/images/service-furniture.jpg" alt="Custom Woodwork & Carpentry Services in Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">Master Carpenters</span>
            </div>
            <div class="service-visual-body">
              <h3>Custom Woodwork &amp; Carpentry</h3>
              <p>Handcrafted solid Burma Teak mandirs with CNC jalis, hydraulic storage beds, ergonomic study desks, crockery consoles, and precision architectural millwork.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">Teak Pooja Mandirs</span>
                <span class="service-visual-pill">Hydraulic Beds</span>
                <span class="service-visual-pill">Precision Carpentry</span>
              </div>
              <div class="service-visual-footer">
                <div class="service-visual-price">Starting At <strong>₹35K</strong></div>
                <a href="/bedroom-furniture-delhi/" class="service-visual-link">Explore Woodwork →</a>
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

    <!-- 8. MATERIAL SHOWCASE ("QUALITY YOU CAN FEEL") -->
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

<!-- 10. SOME OF OUR AWESOME INTERIOR DESIGNING PROJECTS (KD Signature Projects Gallery) -->
    <section class="room-explorer-section">
      <div class="container">
        <div class="section-header-center">
          <div class="pill-badge pill-badge-red" style="margin-bottom: 0.8rem;">
            ✦ Real Handover Gallery
          </div>
          <h2>Some Of Our Awesome Interior Designing Projects<span class="logo-dot">.</span></h2>
          <p>Explore real apartments, builder floors, and villas delivered across Delhi NCR with full Architectural working layouts and AutoCAD precision.</p>
        </div>

        <!-- Room Tabs -->
        <div class="room-tabs-bar" role="tablist">
          <button class="room-tab-btn active" data-room-target="all">All Projects</button>
          <button class="room-tab-btn" data-room-target="kitchen">Modular Kitchens</button>
          <button class="room-tab-btn" data-room-target="bedroom">Master Bedrooms</button>
          <button class="room-tab-btn" data-room-target="living">Living &amp; Dining</button>
          <button class="room-tab-btn" data-room-target="wardrobe">Custom Wardrobes</button>
          <button class="room-tab-btn" data-room-target="woodwork">Woodwork &amp; Mandirs</button>
        </div>

        <!-- Room Cards Grid -->
        <div class="room-cards-grid">
          <div class="room-card" data-room="woodwork">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-mandir.webp" type="image/webp">
                <img src="/assets/images/portfolio-mandir.jpg" alt="Sacred Teakwood Mandir & Custom Woodwork in South Extension Delhi" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">South Extension II</span>
            </div>
            <div class="room-card-body">
              <h3>Bespoke Teakwood Mandir &amp; Jali</h3>
              <p>Solid Burma Teak with intricate backlit CNC jaali, brass temple bells, and concealed samagri storage.</p>
              <div class="room-card-footer">
                <div class="price-chip">Delivered in <strong>21 Days</strong></div>
                <a href="/bedroom-furniture-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">View Woodwork Details</a>
              </div>
            </div>
          </div>
          
          <div class="room-card" data-room="kitchen">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-kitchen.webp" type="image/webp">
                <img src="/assets/images/portfolio-kitchen.jpg" alt="L-Shaped Acrylic Kitchen in Greater Kailash" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Greater Kailash II</span>
            </div>
            <div class="room-card-body">
              <h3>Matte Acrylic Modular Kitchen</h3>
              <p>Calacatta quartz countertop with German soft-close tandem drawers and tall pantry.</p>
              <div class="room-card-footer">
                <div class="price-chip">Delivered in <strong>Delivered On Schedule</strong></div>
                <a href="/modular-kitchen-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">View Project Details</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="bedroom">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-bedroom.webp" type="image/webp">
                <img src="/assets/images/portfolio-bedroom.jpg" alt="Master Suite with Sliding Wardrobe in Panchsheel Park" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Panchsheel Park</span>
            </div>
            <div class="room-card-body">
              <h3>Contemporary Master Suite</h3>
              <p>Floor-to-ceiling tinted glass sliding wardrobe with sensor profile lighting &amp; hydraulic bed.</p>
              <div class="room-card-footer">
                <div class="price-chip">Delivered in <strong>38 Days</strong></div>
                <a href="/wardrobe-design-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">View Project Details</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="living">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-tvunit.webp" type="image/webp">
                <img src="/assets/images/portfolio-tvunit.jpg" alt="Fluted Charcoal TV Wall in Gurugram" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">DLF Phase 5, Gurugram</span>
            </div>
            <div class="room-card-body">
              <h3>Fluted Charcoal Media Wall</h3>
              <p>Acoustic louvers with floating marble console, concealed wiring, and warm backlighting.</p>
              <div class="room-card-footer">
                <div class="price-chip">Delivered in <strong>21 Days</strong></div>
                <a href="/wall-paneling-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">View Project Details</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="kitchen">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-kitchen-2.webp" type="image/webp">
                <img src="/assets/images/portfolio-kitchen-2.jpg" alt="Parallel Modular Kitchen in Gurugram" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Dwarka Sector 4</span>
            </div>
            <div class="room-card-body">
              <h3>Monochrome Parallel Kitchen</h3>
              <p>Anti-fingerprint matte black finish with quartz worktops and breakfast counter seating.</p>
              <div class="room-card-footer">
                <div class="price-chip">Delivered in <strong>40 Days</strong></div>
                <a href="/modular-kitchen-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">View Project Details</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="wardrobe">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-wardrobe-2.webp" type="image/webp">
                <img src="/assets/images/portfolio-wardrobe-2.jpg" alt="Walk-in Wardrobe in Jor Bagh" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Jor Bagh</span>
            </div>
            <div class="room-card-body">
              <h3>His &amp; Her Luxury Walk-In</h3>
              <p>Velvet-lined jewellery drawers, sensor lighting, and smoked glass architectural shutters.</p>
              <div class="room-card-footer">
                <div class="price-chip">Delivered in <strong>35 Days</strong></div>
                <a href="/wardrobe-design-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">View Project Details</a>
              </div>
            </div>
          </div>

          <div class="room-card" data-room="living">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-dining.webp" type="image/webp">
                <img src="/assets/images/portfolio-dining.jpg" alt="Open Concept Dining & Living in Vasant Vihar" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">Vasant Vihar</span>
            </div>
            <div class="room-card-body">
              <h3>Open Concept Living &amp; Dining</h3>
              <p>Warm coffer ceiling with architectural track lighting, smoked veneer cladding, and CNC jali.</p>
              <div class="room-card-footer">
                <div class="price-chip">Delivered in <strong>44 Days</strong></div>
                <a href="/full-home-interior-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">View Project Details</a>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

<!-- 12. REAL HOMES DELIVERED (CLIENT TESTIMONIALS) -->
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
            <p class="quote">"Delhi Interior transformed our 3 BHK in GK-2 completely within 42 days. Their budget transparency was incredible — the editable spreadsheet meant zero surprise charges at the end."</p>
            <div class="client-meta">
              <strong>Vikram &amp; Ritu Mehra</strong>
              <span>Greater Kailash II · 3 BHK Full Home Interior</span>
            </div>
          </div>

          <div class="testimonial-card">
            <div class="rating-stars">★★★★★</div>
            <p class="quote">"The fluted charcoal wall paneling and floor-to-ceiling tinted glass wardrobes in our master bedroom get compliments from everyone. Complete turnkey execution without running after contractors."</p>
            <div class="client-meta">
              <strong>Ananya Sharma</strong>
              <span>DLF Phase 5, Gurugram · 4 BHK Penthouse</span>
            </div>
          </div>

          <div class="testimonial-card">
            <div class="rating-stars">★★★★★</div>
            <p class="quote">"Having one point of contact for civil, modular kitchen, false ceiling, plumbing, and Asian Paints Royale polish made this whole renovation completely hassle-free."</p>
            <div class="client-meta">
              <strong>Rajesh Singhal</strong>
              <span>Vasant Vihar · Complete Turnkey Renovation</span>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 13. FAQ ACCORDION -->
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
              <span>How does your budget transparency and open BOQ work?</span>
              <span class="toggle-icon">+</span>
            </button>
            <div class="faq-answer">
              <p>We provide detailed itemized cost breakdowns line by line so you know where every single penny is going. We share editable BOQ spreadsheets so you can customize material finishes according to your budget with zero hidden markups.</p>
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

    <!-- 14. HIGH-IMPACT FINAL CTA BANNER -->
    <section class="cta-banner-section">
      <div class="container cta-banner-box">
        <h2>Bring Home Interiors That Inspire You Every Day<span class="logo-dot">.</span></h2>
        <p>Book your free 3D design consultation with Delhi's top modular interior studio. Get a complete itemized BOQ with 0% EMI options.</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.5rem;">
          <a href="/contact/" class="btn btn-primary" style="background-color: #FFFFFF; color: var(--color-primary); font-weight: 700; padding: 1rem 2.2rem;">
            Book Free Consultation
          </a>
          <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+design+consultation." class="btn btn-outline" style="border-color: #FFFFFF; color: #FFFFFF; padding: 1rem 2.2rem;" target="_blank" rel="noopener noreferrer">
            Chat on WhatsApp
          </a>
        </div>
      </div>
    </section>

  </main>

  <!-- Modern Footer -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="site-logo" style="margin-bottom: 1.25rem;">
            <img src="/assets/images/logo.png" alt="Delhi Interior" width="160" height="50" class="brand-logo-img">
          </div>
          <p>Delhi NCR's trusted residential and commercial interior design brand. Delivering precision modular kitchens, wardrobes, and turnkey homes backed by a 10-year warranty.</p>
          <div style="display: flex; gap: 0.75rem; margin-top: 1.2rem; font-size: 0.85rem;">
            <a href="https://instagram.com/delhiinterior" style="color: #9CA3AF;" aria-label="Instagram">Instagram</a> ·
            <a href="https://facebook.com/delhiinterior" style="color: #9CA3AF;" aria-label="Facebook">Facebook</a> ·
            <a href="https://youtube.com/delhiinterior" style="color: #9CA3AF;" aria-label="YouTube">YouTube</a>
          </div>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Our Services</h4>
          <ul class="footer-links">
            <li><a href="/full-home-interior-delhi/">Residential Interiors</a></li>
            <li><a href="/modular-kitchen-delhi/">Modular Kitchens</a></li>
            <li><a href="/wardrobe-design-delhi/">Custom Wardrobes</a></li>
            <li><a href="/wall-paneling-delhi/">Wall Paneling &amp; TV Units</a></li>
            <li><a href="/false-ceiling-delhi/">False Ceiling &amp; Lights</a></li>
            <li><a href="/doors-partitions-delhi/">Doors &amp; Partitions</a></li>
            <li><a href="/bedroom-furniture-delhi/">Study Desks &amp; Storage</a></li>
            <li><a href="/painting-polishing-delhi/">Painting &amp; PU Polish</a></li>
            <li><a href="/plumbing-electrical-delhi/">Plumbing &amp; Electrical MEP</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Quick Links</h4>
          <ul class="footer-links">
            <li><a href="/">Home</a></li>
            <li><a href="/about/">About Us</a></li>
            <li><a href="/portfolio/">Projects Gallery</a></li>
              <li><a href="/process/">Our 45-Day Process</a></li>
            <li><a href="/blog/">Blogs &amp; Guides</a></li>
            <li><a href="/contact/">Contact Us</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Experience Centre</h4>
          <p style="margin-bottom: 0.5rem; color: #D1D5DB;">F-128/4, Mohammadpur<br>New Delhi, Delhi 110066</p>
          <p style="margin-bottom: 0.5rem; color: #D1D5DB;">Open 24 Hours</p>
          <p style="margin-bottom: 1rem;"><a href="tel:+919643817099" style="color: #FFFFFF; font-weight: 700; text-decoration: none;">+91 96438 17099</a></p>
          <a href="/contact/" class="btn btn-outline" style="border-color: #4B5563; color: #FFFFFF; font-size: 0.85rem; padding: 0.6rem 1.2rem;">Visit Experience Centre</a>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> Delhi Interior. All rights reserved. GST Registered.</p>
        <div class="footer-legal-links">
          <a href="/privacy-policy/">Privacy Policy</a>
          <a href="/terms-of-service/">Terms of Service</a>
          <a href="/sitemap/">Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

<script src="/assets/js/main.js" defer></script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('scripts/build_home.py', 'w', encoding='utf-8') as f:
    f.write(f'''import os, json

home_schema = {json.dumps(home_schema, indent=4)}

html_content = \'\'\'{html_content}\'\'\'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("[SUCCESS] index.html rebuilt with Home Styling by KD menu bar, topbar, under-nav bar, and high-value content sections!")
''')

print("[SUCCESS] Generated index.html and scripts/build_home.py successfully!")
