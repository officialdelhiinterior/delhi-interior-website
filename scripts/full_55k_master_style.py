# Master Architectural Stylesheet Generator for Delhi Interior
# Creative Direction: Minimalist, Editorial, Sophisticated, Contemporary & Timeless
# Zero forbidden colors (#111111, #0b0b0b, #ffd700), Zero redundant duplicates, Zero AI tropes.

css = '''/* ==========================================================================
   DELHI INTERIOR — ARCHITECTURAL DESIGN SYSTEM & STYLESHEET
   Version: 4.0 (Architectural Editorial Edition)
   Creative Direction: Sophisticated, Modern, Minimalist, Master Craftsmanship
   ========================================================================== */

/* --------------------------------------------------------------------------
   1. DESIGN TOKENS & SYSTEM VARIABLES
   -------------------------------------------------------------------------- */
:root {
  /* Brand & Neutral Palette */
  --color-primary: #D97706;          /* Warm Architectural Amber / Bronze */
  --color-primary-hover: #B45309;    /* Deep Burnished Amber */
  --color-primary-subtle: #FFFBEB;   /* Delicate Cream Highlight */
  --color-primary-border: #FDE68A;   /* Soft Gold Hairline */

  --color-dark: #0F172A;             /* Slate 900 — Deep Architectural Ink */
  --color-dark-surface: #0A0E17;     /* Obsidian Footer / Hero Depth */
  --color-dark-muted: #1E293B;       /* Slate 800 */
  --color-body: #334155;             /* Slate 700 — Optimal Editorial Reading */
  --color-muted: #64748B;            /* Slate 500 — Secondary Details */
  --color-light-muted: #94A3B8;      /* Slate 400 */

  --color-border: #E2E8F0;           /* Slate 200 — Crisp Structural Border */
  --color-border-light: #F1F5F9;     /* Slate 100 — Hairline Divider */
  --color-bg-light: #F8FAFC;         /* Slate 50 — Architectural Off-White */
  --color-white: #FFFFFF;

  --color-green: #16A34A;            /* Emerald 600 — Verified Accents */
  --color-green-subtle: #ECFDF5;
  --color-blue: #2563EB;             /* Royal 600 — Informational Focus */
  --color-blue-subtle: #EFF6FF;

  --color-badge-red: #FEF2F2;
  --color-badge-red-text: #DC2626;

  /* Typography Scale */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-display: 'Plus Jakarta Sans', var(--font-sans);

  /* Precise Architectural Radii (Clean, never bulbous) */
  --radius-xs: 4px;
  --radius-sm: 6px;                  /* Inputs, Small Buttons */
  --radius-md: 8px;                  /* Cards, Tooltips, Icon Boxes */
  --radius-lg: 12px;                 /* Major Feature Cards, Hero Media */
  --radius-xl: 16px;                 /* Outer Showcases */
  --radius-full: 9999px;             /* Pill Badges */

  /* Architectural Ambient Elevation Shadows */
  --shadow-subtle: 0 1px 2px rgba(15, 23, 42, 0.04);
  --shadow-sm: 0 2px 6px -1px rgba(15, 23, 42, 0.05), 0 1px 2px rgba(15, 23, 42, 0.03);
  --shadow-card: 0 4px 14px -2px rgba(15, 23, 42, 0.06), 0 1px 3px rgba(15, 23, 42, 0.04);
  --shadow-hover: 0 16px 32px -6px rgba(15, 23, 42, 0.09), 0 4px 12px -2px rgba(15, 23, 42, 0.04);
  --shadow-floating: 0 20px 40px -8px rgba(15, 23, 42, 0.16);

  /* Layout & Grid Constants */
  --max-width: 1280px;
  --header-height: 76px;
  --topbar-height: 38px;
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-fast: 150ms;
  --duration-normal: 250ms;
}

/* --------------------------------------------------------------------------
   2. RESETS, BOX-SIZING & ACCESSIBILITY
   -------------------------------------------------------------------------- */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: var(--font-sans);
  font-size: 16px;
  color: var(--color-body);
  background-color: var(--color-white);
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}

body {
  line-height: 1.65;
  overflow-x: hidden;
  min-height: 100vh;
}

img, picture, svg {
  display: block;
  max-width: 100%;
}

a {
  color: inherit;
  text-decoration: none;
  transition: color var(--duration-fast) ease;
}

ul, ol {
  list-style: none;
}

button, input, select, textarea {
  font: inherit;
  color: inherit;
  border: none;
  background: none;
}

button {
  cursor: pointer;
}

.skip-link {
  position: absolute;
  top: -100px;
  left: 1rem;
  background: var(--color-dark);
  color: #FFFFFF;
  padding: 0.75rem 1.25rem;
  z-index: 9999;
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  font-weight: 600;
  transition: top 0.2s ease;
}
.skip-link:focus {
  top: 1rem;
}

/* --------------------------------------------------------------------------
   3. TYPOGRAPHY SYSTEM
   -------------------------------------------------------------------------- */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-display);
  color: var(--color-dark);
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.025em;
}

h1 {
  font-size: clamp(2.2rem, 4vw, 3.25rem);
  font-weight: 800;
  line-height: 1.15;
}

h2 {
  font-size: clamp(1.8rem, 2.8vw, 2.4rem);
  font-weight: 800;
  line-height: 1.2;
}

h3 {
  font-size: clamp(1.25rem, 1.8vw, 1.5rem);
  font-weight: 700;
  line-height: 1.3;
}

h4 {
  font-size: 1.12rem;
  font-weight: 700;
  line-height: 1.4;
}

p {
  font-size: 1rem;
  line-height: 1.7;
  color: var(--color-body);
}

.highlight {
  color: var(--color-primary);
  position: relative;
  display: inline-block;
}

.section-header-center {
  text-align: center;
  max-width: 720px;
  margin: 0 auto 3rem;
}
.section-header-center h2 {
  margin-bottom: 0.85rem;
}
.section-header-center p {
  font-size: 1.05rem;
  color: var(--color-muted);
  line-height: 1.7;
}

.section-title-wrap {
  margin-bottom: 2.5rem;
}
.section-title-wrap h2 {
  margin-bottom: 0.75rem;
}
.section-title-wrap p {
  font-size: 1.05rem;
  color: var(--color-muted);
  line-height: 1.7;
}

/* --------------------------------------------------------------------------
   4. CONTAINERS & LAYOUT SYSTEM
   -------------------------------------------------------------------------- */
.container {
  max-width: var(--max-width);
  margin-left: auto;
  margin-right: auto;
  padding-left: clamp(1.25rem, 4vw, 2.5rem);
  padding-right: clamp(1.25rem, 4vw, 2.5rem);
  width: 100%;
}

.section-padding {
  padding: clamp(3.5rem, 6vw, 5.5rem) 0;
}

.bg-white {
  background-color: var(--color-white);
}

.bg-light {
  background-color: var(--color-bg-light);
}

/* --------------------------------------------------------------------------
   5. BUTTONS, PILL BADGES & UI ELEMENTS
   -------------------------------------------------------------------------- */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 0.92rem;
  line-height: 1;
  padding: 0.75rem 1.6rem;
  border-radius: var(--radius-sm);
  transition: all var(--duration-fast) var(--ease-out);
  text-align: center;
  white-space: nowrap;
}

.btn-primary {
  background-color: var(--color-primary);
  color: #FFFFFF;
  border: 1px solid var(--color-primary);
  box-shadow: 0 1px 2px rgba(217, 119, 6, 0.2);
}
.btn-primary:hover {
  background-color: var(--color-primary-hover);
  border-color: var(--color-primary-hover);
  color: #FFFFFF;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(217, 119, 6, 0.25);
}

.btn-outline {
  background-color: transparent;
  color: var(--color-dark);
  border: 1.5px solid var(--color-border);
}
.btn-outline:hover {
  background-color: var(--color-bg-light);
  border-color: var(--color-dark);
  color: var(--color-dark);
}

.btn-secondary {
  background-color: #F1F5F9;
  color: var(--color-dark);
  border: 1px solid var(--color-border);
}
.btn-secondary:hover {
  background-color: #E2E8F0;
  color: var(--color-dark);
}

.btn-block {
  width: 100%;
}

/* Editorial Pill Badges */
.pill-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-family: var(--font-display);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-full);
}

.pill-badge-red {
  background-color: var(--color-badge-red);
  color: var(--color-badge-red-text);
  border: 1px solid #FECACA;
}

.pill-badge-green {
  background-color: var(--color-green-subtle);
  color: var(--color-green);
  border: 1px solid #A7F3D0;
}

/* --------------------------------------------------------------------------
   6. FORM CONTROLS & ARCHITECTURAL INPUTS
   -------------------------------------------------------------------------- */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  text-align: left;
}

.form-label {
  font-family: var(--font-display);
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--color-dark);
}

.form-control {
  width: 100%;
  height: 44px;
  padding: 0 0.85rem;
  background-color: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  color: var(--color-dark);
  transition: border-color var(--duration-fast) ease, box-shadow var(--duration-fast) ease;
}

.form-control::placeholder {
  color: #94A3B8;
  font-size: 0.86rem;
}

.form-control:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.12);
}

select.form-control {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23475569' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  padding-right: 2rem;
  cursor: pointer;
}

/* --------------------------------------------------------------------------
   7. LEVEL 1: TOP UTILITY BAR
   -------------------------------------------------------------------------- */
.top-utility-bar {
  background-color: var(--color-dark-surface);
  color: #94A3B8;
  font-size: 0.78rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  min-height: var(--topbar-height);
  display: flex;
  align-items: center;
}

.top-utility-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.top-utility-left {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.top-utility-left .badge-welcome {
  background: rgba(255, 255, 255, 0.08);
  color: #F1F5F9;
  font-weight: 600;
  padding: 0.15rem 0.5rem;
  border-radius: var(--radius-xs);
  font-size: 0.74rem;
}

.top-utility-left .utility-timing {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  color: #CBD5E1;
}

.top-utility-left .utility-sep {
  color: #475569;
}

.top-utility-right {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.top-utility-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  color: #CBD5E1;
  font-weight: 500;
}
.top-utility-link:hover {
  color: #FFFFFF;
}

.top-utility-social {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0 0.5rem;
  border-left: 1px solid rgba(255, 255, 255, 0.12);
  border-right: 1px solid rgba(255, 255, 255, 0.12);
}
.top-utility-social a {
  color: #94A3B8;
  display: flex;
  align-items: center;
}
.top-utility-social a:hover {
  color: #FFFFFF;
}

/* --------------------------------------------------------------------------
   8. LEVEL 2: MAIN SITE HEADER & NAVIGATION
   -------------------------------------------------------------------------- */
.site-header {
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--color-border);
  position: sticky;
  top: 0;
  z-index: 1000;
  transition: all var(--duration-normal) ease;
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: var(--header-height);
}

.site-logo {
  display: flex;
  align-items: center;
  flex-shrink: 0;
}

.site-logo img.brand-logo-img {
  height: 48px;
  width: auto;
  max-width: 175px;
  object-fit: contain;
}

.main-navigation {
  display: flex;
  align-items: center;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.75rem;
}

.nav-links > li > a {
  font-family: var(--font-display);
  font-size: 0.94rem;
  font-weight: 600;
  color: #1E293B;
  padding: 0.5rem 0;
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}

.nav-links > li > a:hover,
.nav-links > li > a.active {
  color: var(--color-primary);
}

.nav-links > li > a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--color-primary);
  transition: width var(--duration-fast) var(--ease-out);
}
.nav-links > li > a:hover::after,
.nav-links > li > a.active::after {
  width: 100%;
}

/* Services Dropdown Mega Menu */
.nav-dropdown-item {
  position: relative;
}

.dropdown-chevron {
  font-size: 0.65rem;
  transition: transform var(--duration-fast) ease;
}
.nav-dropdown-item:hover .dropdown-chevron {
  transform: rotate(180deg);
}

.nav-dropdown-menu {
  position: absolute;
  top: 100%;
  left: -120px;
  width: 580px;
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-hover);
  padding: 1.25rem;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.65rem;
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: all var(--duration-normal) var(--ease-out);
  pointer-events: none;
  z-index: 1010;
}

.nav-dropdown-item:hover .nav-dropdown-menu,
.nav-dropdown-item:focus-within .nav-dropdown-menu {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
  pointer-events: auto;
}

.dropdown-link {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.65rem 0.75rem;
  border-radius: var(--radius-sm);
  transition: background-color var(--duration-fast) ease;
}
.dropdown-link:hover {
  background-color: var(--color-bg-light);
}

.dropdown-icon {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-xs);
  background: var(--color-bg-light);
  border: 1px solid var(--color-border-light);
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.dropdown-text strong {
  display: block;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-dark);
  line-height: 1.3;
}
.dropdown-text span {
  display: block;
  font-size: 0.76rem;
  color: var(--color-muted);
  line-height: 1.3;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.hamburger {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 24px;
  height: 18px;
  background: transparent;
  border: none;
  padding: 0;
}
.hamburger span {
  display: block;
  height: 2px;
  width: 100%;
  background-color: var(--color-dark);
  border-radius: 1px;
  transition: all var(--duration-fast) ease;
}

/* --------------------------------------------------------------------------
   9. MOBILE MENU DRAWER OVERLAY
   -------------------------------------------------------------------------- */
.mobile-menu-overlay {
  position: fixed;
  top: 0;
  right: -100%;
  width: 100%;
  max-width: 380px;
  height: 100vh;
  background: #FFFFFF;
  box-shadow: -8px 0 24px rgba(15, 23, 42, 0.15);
  z-index: 2000;
  transition: right 0.35s var(--ease-out);
  display: flex;
  flex-direction: column;
}
.mobile-menu-overlay.open {
  right: 0;
}

.mobile-menu-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid var(--color-border);
}

.mobile-menu-close {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background: var(--color-bg-light);
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-dark);
}

.mobile-menu-content {
  flex: 1;
  padding: 1.5rem;
  overflow-y: auto;
}

.mobile-menu-section-title {
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-muted);
  margin-bottom: 0.85rem;
}

.mobile-nav-links, .mobile-nav-services {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 2rem;
}

.mobile-nav-links a, .mobile-nav-services a {
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--color-dark);
  padding: 0.4rem 0;
  display: block;
}

.mobile-menu-footer {
  padding: 1.25rem 1.5rem;
  border-top: 1px solid var(--color-border);
  background: var(--color-bg-light);
}

/* --------------------------------------------------------------------------
   10. HERO SECTION & DOCKED HORIZONTAL CONSULTATION RIBBON
   -------------------------------------------------------------------------- */
.hero-livspace {
  padding: clamp(2.5rem, 5vw, 4rem) 0 3.5rem;
  background: linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 100%);
  position: relative;
  overflow: hidden;
}

.hero-layout {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: clamp(2rem, 4vw, 3.5rem);
  align-items: center;
}

.hero-headline h1 {
  margin-bottom: 1.2rem;
}

.hero-subhead {
  font-size: clamp(1rem, 1.2vw, 1.1rem);
  color: var(--color-body);
  line-height: 1.7;
  max-width: 580px;
}

.hero-usps {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.85rem;
  margin-top: 1.8rem;
}

.hero-usp-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.88rem;
  font-weight: 600;
  color: #1E293B;
}
.hero-usp-item svg {
  width: 18px;
  height: 18px;
  fill: var(--color-primary);
  flex-shrink: 0;
}

.hero-cta-group {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-top: 2rem;
}

/* Right Photography Showcase */
.hero-visual-showcase {
  position: relative;
}

.hero-main-photo {
  width: 100%;
  height: clamp(380px, 42vw, 490px);
  object-fit: cover;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-card);
}

.hero-glass-badge {
  position: absolute;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(226, 232, 240, 0.9);
  border-radius: var(--radius-md);
  padding: 0.65rem 0.95rem;
  box-shadow: var(--shadow-sm);
  display: flex;
  align-items: center;
  gap: 0.65rem;
  z-index: 5;
}

.hero-glass-badge strong {
  display: block;
  font-family: var(--font-display);
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--color-dark);
}
.hero-glass-badge span {
  display: block;
  font-size: 0.72rem;
  color: var(--color-muted);
}

.hero-badge-location {
  top: 1.25rem;
  left: 1.25rem;
}

.hero-badge-warranty {
  bottom: 1.25rem;
  left: 1.25rem;
}
.hero-badge-warranty .check-icon {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--color-green-subtle);
  color: var(--color-green);
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
}

.hero-badge-rating {
  bottom: 1.25rem;
  right: 1.25rem;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.2rem;
}
.hero-badge-rating .stars {
  color: #F59E0B;
  font-size: 0.78rem;
  letter-spacing: 0.1em;
}

/* Docked Consultation Card (Architectural Ribbon) */
.hero-consult-card-dock {
  margin-top: clamp(2.5rem, 5vw, 3.5rem);
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: clamp(1.5rem, 3vw, 2.25rem);
  box-shadow: var(--shadow-card);
}

.consult-dock-header {
  margin-bottom: 1.5rem;
}
.consult-title {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--color-dark);
  margin-bottom: 0.25rem;
}
.consult-sub {
  font-size: 0.88rem;
  color: var(--color-muted);
}

.consult-form-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr) 1.2fr;
  gap: 1rem;
  align-items: flex-end;
}

.form-submit-col .label-spacer {
  visibility: hidden;
  display: block;
  height: 1.35rem;
}

.consult-dock-footer {
  margin-top: 1.25rem;
  padding-top: 1rem;
  border-top: 1px solid var(--color-border-light);
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.82rem;
  color: var(--color-muted);
  flex-wrap: wrap;
  gap: 0.5rem;
}

.consult-direct-call a {
  color: var(--color-primary);
  font-weight: 700;
}

/* --------------------------------------------------------------------------
   11. TRUST METRIC STRIP
   -------------------------------------------------------------------------- */
.trust-strip {
  background-color: var(--color-dark);
  color: #FFFFFF;
  padding: 2.5rem 0;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.trust-strip-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  text-align: center;
}

.trust-item {
  position: relative;
}
.trust-item:not(:last-child)::after {
  content: '';
  position: absolute;
  right: -1rem;
  top: 15%;
  height: 70%;
  width: 1px;
  background-color: rgba(255, 255, 255, 0.12);
}

.metric-counter {
  font-family: var(--font-display);
  font-size: clamp(2rem, 3.5vw, 2.75rem);
  font-weight: 800;
  line-height: 1.1;
  color: #FFFFFF;
  margin-bottom: 0.35rem;
}

.trust-item p {
  font-size: 0.85rem;
  color: #94A3B8;
  font-weight: 500;
  letter-spacing: 0.01em;
}

/* --------------------------------------------------------------------------
   12. CRAFTSMAN ADVANTAGE CARDS (SECTION 2.5)
   -------------------------------------------------------------------------- */
.craftsman-advantage-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}

.craftsman-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2.2rem 2rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.craftsman-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.craftsman-card-icon {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-md);
  background: var(--color-bg-light);
  border: 1px solid var(--color-border);
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
}

.craftsman-card h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-dark);
  margin-bottom: 0.75rem;
}

.craftsman-card p {
  font-size: 0.92rem;
  color: var(--color-body);
  line-height: 1.7;
  margin-bottom: 1.5rem;
  flex: 1;
}

.craftsman-tag {
  font-family: var(--font-display);
  font-size: 0.8rem;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}
.tag-green { color: var(--color-green); }
.tag-blue { color: var(--color-blue); }
.tag-amber { color: var(--color-primary); }

/* --------------------------------------------------------------------------
   13. DUAL SPECIALIZATION CARDS (SECTION 3)
   -------------------------------------------------------------------------- */
.dual-specialty-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-top: 2rem;
}

.specialty-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-card);
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.specialty-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.specialty-card img {
  width: 100%;
  height: 280px;
  object-fit: cover;
  transition: transform 0.5s var(--ease-out);
}
.specialty-card:hover img {
  transform: scale(1.03);
}

.specialty-content {
  padding: 2.25rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.specialty-content h3 {
  font-size: 1.5rem;
  margin-bottom: 0.85rem;
}

.specialty-content p {
  font-size: 0.94rem;
  color: var(--color-body);
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.specialty-checklist {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  margin-bottom: 2rem;
  flex: 1;
}

.specialty-checklist li {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.88rem;
  color: #1E293B;
  font-weight: 500;
}
.specialty-checklist svg {
  width: 16px;
  height: 16px;
  fill: var(--color-green);
  flex-shrink: 0;
}

/* --------------------------------------------------------------------------
   14. 45-DAY HANDOVER PROCESS (SECTION 4)
   -------------------------------------------------------------------------- */
.process-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  position: relative;
  margin-top: 2.5rem;
}

.process-step {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2rem 1.5rem;
  box-shadow: var(--shadow-subtle);
  position: relative;
}

.step-circle {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--color-dark);
  color: #FFFFFF;
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
}

.process-step h4 {
  font-size: 1.15rem;
  margin-bottom: 0.65rem;
}

.process-step p {
  font-size: 0.88rem;
  color: var(--color-muted);
  line-height: 1.6;
}

/* --------------------------------------------------------------------------
   15. SECTION 5: LOCAL EXPERTISE & WHY SPECIALIZED DESIGNERS (BUG FIX)
   -------------------------------------------------------------------------- */
.why-need-section {
  padding: clamp(3.5rem, 6vw, 5.5rem) 0;
  background-color: var(--color-bg-light);
  border-top: 1px solid var(--color-border);
  border-bottom: 1px solid var(--color-border);
}

.why-need-layout {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 3.5rem;
  align-items: center;
}

.why-need-points {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.25rem;
  margin-top: 2rem;
}

.why-point-box {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 1.4rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform var(--duration-fast) ease, box-shadow var(--duration-fast) ease;
}
.why-point-box:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-card);
}

.why-point-box h4 {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--color-dark);
  margin-bottom: 0.5rem;
  width: 100%;
}

.why-point-box p {
  font-size: 0.88rem;
  color: var(--color-body);
  line-height: 1.65;
  margin: 0;
}

/* --------------------------------------------------------------------------
   16. SERVICES VISUAL GRID (SECTION 6)
   -------------------------------------------------------------------------- */
.services-visual-section {
  padding: clamp(3.5rem, 6vw, 5.5rem) 0;
  background-color: var(--color-white);
}

.services-visual-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.service-visual-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.service-visual-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-hover);
}

.service-visual-img {
  position: relative;
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background-color: #E2E8F0;
}
.service-visual-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s var(--ease-out);
}
.service-visual-card:hover .service-visual-img img {
  transform: scale(1.04);
}

.service-visual-body {
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.service-visual-body h3 {
  font-size: 1.25rem;
  margin-bottom: 0.65rem;
}
.service-visual-body h3 a {
  color: var(--color-dark);
}
.service-visual-body h3 a:hover {
  color: var(--color-primary);
}

.service-visual-body p {
  font-size: 0.9rem;
  color: var(--color-body);
  line-height: 1.65;
  margin-bottom: 1.25rem;
  flex: 1;
}

.service-visual-footer {
  padding: 1rem 1.75rem;
  border-top: 1px solid var(--color-border-light);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--color-bg-light);
}

.service-visual-tag {
  font-size: 0.76rem;
  font-weight: 700;
  color: var(--color-primary);
}

.service-visual-link {
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--color-dark);
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}
.service-visual-link:hover {
  color: var(--color-primary);
}

/* --------------------------------------------------------------------------
   17. ROOM DESIGN EXPLORER (SECTION 7)
   -------------------------------------------------------------------------- */
.room-tabs-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 2.5rem;
}

.room-tab-btn {
  font-family: var(--font-display);
  font-size: 0.9rem;
  font-weight: 600;
  padding: 0.6rem 1.4rem;
  border-radius: var(--radius-full);
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  color: var(--color-dark);
  transition: all var(--duration-fast) ease;
}
.room-tab-btn:hover {
  border-color: var(--color-dark);
}
.room-tab-btn.active {
  background: var(--color-dark);
  border-color: var(--color-dark);
  color: #FFFFFF;
}

.room-cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.8rem;
}

.room-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-subtle);
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.room-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.room-card-img {
  aspect-ratio: 4 / 3;
  overflow: hidden;
  background-color: #E2E8F0;
}
.room-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s var(--ease-out);
}
.room-card:hover .room-card-img img {
  transform: scale(1.04);
}

.room-card-body {
  padding: 1.5rem;
}
.room-card-body h4 {
  font-size: 1.15rem;
  margin-bottom: 0.4rem;
}
.room-card-body p {
  font-size: 0.88rem;
  color: var(--color-muted);
  line-height: 1.6;
}

.room-card-footer {
  padding: 0.85rem 1.5rem;
  border-top: 1px solid var(--color-border-light);
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--color-primary);
  background: var(--color-bg-light);
}

/* --------------------------------------------------------------------------
   18. GENUINE MATERIALS & HARDWARE SHOWCASE (SECTION 8)
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
  padding: 2rem 1.6rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform var(--duration-fast) ease, box-shadow var(--duration-fast) ease;
}
.material-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-hover);
}

.material-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-md);
  background: var(--color-bg-light);
  border: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-primary);
  margin-bottom: 1.25rem;
}

.material-card h3 {
  font-size: 1.15rem;
  margin-bottom: 0.5rem;
}
.material-card p {
  font-size: 0.88rem;
  color: var(--color-body);
  line-height: 1.6;
  margin-bottom: 1.25rem;
  flex: 1;
}

.material-spec-pill {
  font-size: 0.76rem;
  font-weight: 700;
  color: var(--color-green);
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

/* --------------------------------------------------------------------------
   19. CLIENT TESTIMONIALS (SECTION 9)
   -------------------------------------------------------------------------- */
.reviews-livspace-section {
  padding: clamp(3.5rem, 6vw, 5.5rem) 0;
  background-color: var(--color-white);
}

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.review-card-livspace {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2.25rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.review-card-livspace:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.review-card-livspace .stars {
  color: #F59E0B;
  font-size: 0.95rem;
  letter-spacing: 0.1em;
  margin-bottom: 1rem;
}

.review-card-livspace p {
  font-size: 0.94rem;
  color: var(--color-body);
  line-height: 1.7;
  margin-bottom: 1.5rem;
  flex: 1;
}

.client-meta {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--color-border-light);
}

.client-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--color-primary);
  color: #FFFFFF;
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 0.92rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.client-meta strong {
  display: block;
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--color-dark);
}
.client-meta span {
  display: block;
  font-size: 0.78rem;
  color: var(--color-muted);
}

/* --------------------------------------------------------------------------
   20. FAQ ACCORDION (SECTION 10)
   -------------------------------------------------------------------------- */
.faq-section {
  padding: clamp(3.5rem, 6vw, 5.5rem) 0;
  background-color: var(--color-bg-light);
  border-top: 1px solid var(--color-border);
}

.faq-accordion {
  max-width: 820px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.faq-item {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: border-color var(--duration-fast) ease, box-shadow var(--duration-fast) ease;
}
.faq-item.active {
  border-color: var(--color-dark);
  box-shadow: var(--shadow-sm);
}

.faq-question {
  width: 100%;
  padding: 1.4rem 1.6rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--color-dark);
  text-align: left;
  gap: 1rem;
}

.faq-icon {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--color-bg-light);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  color: var(--color-dark);
  transition: transform var(--duration-fast) ease;
  flex-shrink: 0;
}
.faq-item.active .faq-icon {
  transform: rotate(45deg);
}

.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s var(--ease-out);
}
.faq-item.active .faq-answer {
  max-height: 500px;
}

.faq-answer-inner {
  padding: 0 1.6rem 1.4rem;
  font-size: 0.94rem;
  color: var(--color-body);
  line-height: 1.7;
  border-top: 1px solid var(--color-border-light);
  padding-top: 1rem;
}

/* --------------------------------------------------------------------------
   21. FINAL CALL TO ACTION & SITE FOOTER
   -------------------------------------------------------------------------- */
.cta-banner-section, .final-cta-section {
  padding: clamp(4rem, 7vw, 6rem) 0;
  background-color: var(--color-dark);
  color: #FFFFFF;
  text-align: center;
  position: relative;
}

.cta-banner-section h2, .final-cta-section h2 {
  color: #FFFFFF;
  margin-bottom: 1rem;
}

.cta-banner-section p, .final-cta-section p {
  font-size: 1.1rem;
  color: #CBD5E1;
  max-width: 680px;
  margin: 0 auto 2.5rem;
  line-height: 1.7;
}

.cta-buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.25rem;
  flex-wrap: wrap;
}

/* Master Site Footer */
.site-footer {
  background-color: var(--color-dark-surface);
  color: #94A3B8;
  padding: 4.5rem 0 2.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.6fr 1fr 1fr 1.2fr;
  gap: 3.5rem;
}

.footer-col .footer-logo-card img {
  height: 48px;
  width: auto;
  max-width: 175px;
  margin-bottom: 1.25rem;
}

.footer-col p {
  font-size: 0.88rem;
  line-height: 1.7;
  color: #94A3B8;
}

.footer-col h4 {
  font-family: var(--font-display);
  font-size: 0.92rem;
  font-weight: 700;
  color: #FFFFFF;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 1.25rem;
}

.footer-links {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.footer-links a {
  font-size: 0.88rem;
  color: #94A3B8;
  transition: color var(--duration-fast) ease;
}
.footer-links a:hover {
  color: #FFFFFF;
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 0 0;
  margin-top: 3.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.82rem;
  color: #64748B;
}

.footer-legal-links {
  display: flex;
  gap: 1.5rem;
}
.footer-legal-links a {
  color: #64748B;
}
.footer-legal-links a:hover {
  color: #CBD5E1;
}

/* --------------------------------------------------------------------------
   22. SUBPAGE SPECIFIC MODULES (PORTFOLIO, BLOG, ABOUT, SERVICES)
   -------------------------------------------------------------------------- */
/* Inner Page Hero */
.inner-hero {
  padding: clamp(3rem, 5vw, 4.5rem) 0;
  background: var(--color-bg-light);
  border-bottom: 1px solid var(--color-border);
  text-align: center;
}
.inner-hero h1 {
  margin-bottom: 0.85rem;
}
.inner-hero p {
  font-size: 1.1rem;
  color: var(--color-muted);
  max-width: 700px;
  margin: 0 auto;
}

/* Breadcrumbs */
.breadcrumbs {
  font-size: 0.82rem;
  color: var(--color-muted);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  margin-bottom: 1rem;
}
.breadcrumbs a {
  color: var(--color-muted);
}
.breadcrumbs a:hover {
  color: var(--color-dark);
}

/* Four Pillars (About Page) */
.pillar-icon-box {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-md);
  background: var(--color-bg-light);
  border: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-primary);
  margin-bottom: 1.25rem;
}

/* Portfolio Grid & Filters */
.portfolio-filter-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 3rem;
}

.portfolio-filter-btn {
  font-family: var(--font-display);
  font-size: 0.88rem;
  font-weight: 600;
  padding: 0.55rem 1.25rem;
  border-radius: var(--radius-full);
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  color: var(--color-dark);
  transition: all var(--duration-fast) ease;
}
.portfolio-filter-btn:hover {
  border-color: var(--color-dark);
}
.portfolio-filter-btn.active {
  background: var(--color-dark);
  border-color: var(--color-dark);
  color: #FFFFFF;
}

.portfolio-full-grid, .portfolio-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.portfolio-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-subtle);
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.portfolio-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.portfolio-card img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  transition: transform 0.4s var(--ease-out);
}
.portfolio-card:hover img {
  transform: scale(1.04);
}

/* Blog Articles & Typography */
.blog-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.blog-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.blog-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.blog-card-img {
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background-color: #E2E8F0;
}
.blog-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s var(--ease-out);
}
.blog-card:hover .blog-card-img img {
  transform: scale(1.04);
}

.blog-card-body {
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.blog-card-meta {
  font-size: 0.78rem;
  color: var(--color-muted);
  margin-bottom: 0.65rem;
}

.blog-card-body h3 {
  font-size: 1.25rem;
  line-height: 1.35;
  margin-bottom: 0.75rem;
}
.blog-card-body h3 a {
  color: var(--color-dark);
}
.blog-card-body h3 a:hover {
  color: var(--color-primary);
}

.blog-card-body p {
  font-size: 0.9rem;
  color: var(--color-body);
  line-height: 1.65;
  margin-bottom: 1.25rem;
  flex: 1;
}

.blog-read-link {
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--color-primary);
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

/* Single Blog Post Reading Container */
.article-container {
  max-width: 780px;
  margin: 0 auto;
  padding: 3rem clamp(1.25rem, 4vw, 2.5rem);
}

.article-header {
  margin-bottom: 2rem;
}
.article-header h1 {
  margin-bottom: 1rem;
}

.article-meta-bar {
  display: flex;
  align-items: center;
  gap: 1rem;
  font-size: 0.85rem;
  color: var(--color-muted);
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--color-border);
}

.article-featured-img {
  width: 100%;
  border-radius: var(--radius-lg);
  margin-bottom: 2.5rem;
  box-shadow: var(--shadow-card);
}

.article-body {
  font-size: 1.05rem;
  line-height: 1.8;
  color: #334155;
}
.article-body h2 {
  font-size: 1.65rem;
  margin: 2.5rem 0 1rem;
}
.article-body h3 {
  font-size: 1.3rem;
  margin: 2rem 0 0.85rem;
}
.article-body p {
  margin-bottom: 1.4rem;
}
.article-body ul, .article-body ol {
  margin-bottom: 1.5rem;
  padding-left: 1.5rem;
}
.article-body li {
  margin-bottom: 0.5rem;
  list-style: disc;
}

.article-inline-cta {
  background: var(--color-bg-light);
  border: 1px solid var(--color-border);
  border-left: 4px solid var(--color-primary);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  margin: 2.5rem 0;
}

/* Service Specifications & Material Packages */
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.price-tier-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2.5rem 2rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.price-tier-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}
.price-tier-card.featured {
  border: 2px solid var(--color-primary);
  position: relative;
}

.price-tier-badge {
  position: absolute;
  top: -12px;
  right: 1.5rem;
  background: var(--color-primary);
  color: #FFFFFF;
  font-size: 0.74rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.25rem 0.75rem;
  border-radius: var(--radius-full);
}

.checklist-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin: 2rem 0;
}
.checklist-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
}

/* Contact Page Grid */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 3.5rem;
  align-items: flex-start;
}

.contact-info-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  box-shadow: var(--shadow-subtle);
}

.contact-channel-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 1.5rem;
}
.contact-channel-item svg {
  width: 22px;
  height: 22px;
  color: var(--color-primary);
  flex-shrink: 0;
  margin-top: 0.15rem;
}

/* --------------------------------------------------------------------------
   23. FLOATING ACTION CONTROLS & MOBILE STICKY BAR
   -------------------------------------------------------------------------- */
.call-float {
  position: fixed;
  bottom: 24px;
  left: 24px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: var(--color-blue);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
  z-index: 990;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.call-float:hover {
  transform: scale(1.08);
  box-shadow: 0 6px 18px rgba(37, 99, 235, 0.5);
}
.call-float svg {
  width: 22px;
  height: 22px;
  fill: #FFFFFF;
}

.whatsapp-float {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background-color: #25D366;
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 14px rgba(37, 211, 102, 0.4);
  z-index: 990;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.whatsapp-float:hover {
  transform: scale(1.08);
  box-shadow: 0 6px 18px rgba(37, 211, 102, 0.5);
}
.whatsapp-float svg {
  width: 26px;
  height: 26px;
  fill: #FFFFFF;
}

.call-tooltip, .whatsapp-tooltip {
  position: absolute;
  background: var(--color-dark);
  color: #FFFFFF;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.35rem 0.65rem;
  border-radius: var(--radius-xs);
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s ease;
}
.call-float:hover .call-tooltip {
  opacity: 1;
  left: 60px;
}
.whatsapp-float:hover .whatsapp-tooltip {
  opacity: 1;
  right: 64px;
}

/* Mobile Sticky Bottom CTA */
.sticky-mobile-cta {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: #FFFFFF;
  border-top: 1px solid var(--color-border);
  box-shadow: 0 -4px 16px rgba(15, 23, 42, 0.08);
  z-index: 995;
  padding: 0.5rem 1rem;
}
.cta-btn-group {
  display: flex;
  gap: 0.75rem;
  height: 100%;
}
.cta-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-display);
  font-size: 0.88rem;
  font-weight: 700;
  border-radius: var(--radius-sm);
  color: #FFFFFF;
}
.btn-call {
  background-color: var(--color-blue);
}
.btn-wa {
  background-color: #25D366;
}

/* --------------------------------------------------------------------------
   24. RESPONSIVE DESIGN SYSTEM
   -------------------------------------------------------------------------- */
/* Tablet & Laptop (< 1024px) */
@media (max-width: 1024px) {
  .hero-layout {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  .hero-visual-showcase {
    order: -1;
  }
  .hero-main-photo {
    height: 380px;
  }
  .consult-form-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .form-submit-col {
    grid-column: span 2;
  }
  .form-submit-col .label-spacer {
    display: none;
  }
  .craftsman-advantage-grid,
  .services-visual-grid,
  .room-cards-grid,
  .reviews-grid,
  .portfolio-full-grid,
  .pricing-grid,
  .blog-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .materials-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .process-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .why-need-layout {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 2.5rem;
  }
}

/* Tablet (< 768px) */
@media (max-width: 768px) {
  .top-utility-bar {
    display: none;
  }
  .main-navigation {
    display: none;
  }
  .hamburger {
    display: flex;
  }
  .site-header {
    --header-height: 64px;
  }
  .site-logo img.brand-logo-img {
    height: 40px;
  }
  .nav-right .btn-primary {
    padding: 0.55rem 1rem;
    font-size: 0.82rem;
  }
  .trust-strip-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }
  .trust-item:not(:last-child)::after {
    display: none;
  }
  .dual-specialty-grid {
    grid-template-columns: 1fr;
  }
  .contact-grid {
    grid-template-columns: 1fr;
  }
  .sticky-mobile-cta {
    display: block;
  }
  .call-float, .whatsapp-float {
    bottom: 74px;
  }
  body {
    padding-bottom: 60px;
  }
}

/* Mobile (< 640px) */
@media (max-width: 640px) {
  .consult-form-grid {
    grid-template-columns: 1fr;
  }
  .form-submit-col {
    grid-column: span 1;
  }
  .craftsman-advantage-grid,
  .services-visual-grid,
  .room-cards-grid,
  .reviews-grid,
  .portfolio-full-grid,
  .pricing-grid,
  .blog-grid,
  .materials-grid,
  .process-grid,
  .why-need-points {
    grid-template-columns: 1fr;
  }
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .footer-bottom {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  .hero-glass-badge {
    position: static;
    margin-top: 0.75rem;
    width: 100%;
  }
  .hero-badge-location, .hero-badge-warranty, .hero-badge-rating {
    position: static;
  }
}

/* Ultra-Compact Mobile (< 380px) */
@media (max-width: 380px) {
  .site-logo img.brand-logo-img {
    height: 34px;
    max-width: 130px;
  }
  .nav-right .btn-primary {
    display: none;
  }
}
'''

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Generated clean architectural master stylesheet assets/css/style.css")
