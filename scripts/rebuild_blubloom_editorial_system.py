import os
import re

def create_blubloom_master_style():
    style_content = '''/* ==========================================================================
   DELHI INTERIOR — MASTER STYLESHEET (BLU BLOOM EDITORIAL ARCHITECTURE)
   Color Palette: Primary Deep Dark Navy, Golden Brass, Crisp White & Ivory
   Green: STRICTLY AND EXCLUSIVELY FOR WHATSAPP ONLY
   Typography: Editorial Playfair Display Serif + Plus Jakarta Sans / Inter
   ========================================================================== */

/* --------------------------------------------------------------------------
   1. DESIGN TOKENS & SYSTEM VARIABLES
   -------------------------------------------------------------------------- */
:root {
  /* Brand Primary: Deep Dark Navy Blue (Anchored by Official Brand Identity) */
  --color-primary: #0B2540;          /* Deep Dark Navy Blue */
  --color-primary-hover: #16365C;    /* Rich Luminous Navy */
  --color-primary-subtle: #F0F4F8;   /* Subtle Navy Mist */
  --color-primary-border: #CBD5E1;   /* Slate Hairline Divider */

  /* Brand Accent: Warm Architectural Golden Brass / Sand */
  --color-accent: #B89058;           /* Warm Architectural Golden Brass */
  --color-accent-hover: #9E7A42;     /* Burnished Antique Gold */
  --color-accent-subtle: #FDFBF7;    /* Delicate Warm Ivory Glow */
  --color-accent-border: #E8D8BA;    /* Soft Brass Border */
  --color-gold: #B89058;

  /* WhatsApp Green: STRICTLY FOR WHATSAPP ACTIONS ONLY */
  --color-whatsapp: #25D366;
  --color-whatsapp-hover: #20BD5A;

  /* Architectural Depth & Neutrals (White, Warm Ivory, Midnight Slate) */
  --color-dark: #0A1626;             /* Deep Midnight Ink */
  --color-dark-surface: #060E18;     /* Obsidian Dark Navy Surface */
  --color-dark-muted: #132438;       /* Deep Navy Slate */
  --color-body: #334155;             /* Slate 700 — High-legibility Editorial Reading Measure */
  --color-muted: #64748B;            /* Slate 500 — Secondary Details */
  --color-light-muted: #94A3B8;      /* Slate 400 */

  --color-white: #FFFFFF;
  --color-ivory: #F8F6F0;            /* Warm Architectural Ivory */
  --color-bg-light: #F8FAFC;         /* Crisp Off-White Surface */
  --color-border: #E2E8F0;           /* Clean Structural Border */
  --color-border-light: #F1F5F9;     /* Hairline Divider */

  /* Typography Scale (Blu Bloom Editorial & Architectural Pairing) */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-body: 'Plus Jakarta Sans', var(--font-sans);
  --font-serif: 'Playfair Display', Georgia, 'Times New Roman', serif;
  --font-display: 'Playfair Display', Georgia, serif;

  /* Precise Architectural Radii (Clean, sharp, never bulbous AI rounded) */
  --radius-xs: 3px;
  --radius-sm: 4px;                  /* Inputs, Small Buttons */
  --radius-md: 6px;                  /* Cards, Tooltips, Icon Boxes */
  --radius-lg: 8px;                  /* Major Feature Cards, Hero Media */
  --radius-xl: 12px;                 /* Outer Showcases */
  --radius-full: 9999px;             /* Pill Badges */

  /* Architectural Ambient Elevation Shadows */
  --shadow-subtle: 0 1px 2px rgba(11, 37, 64, 0.04);
  --shadow-sm: 0 2px 6px -1px rgba(11, 37, 64, 0.05), 0 1px 2px rgba(11, 37, 64, 0.03);
  --shadow-card: 0 4px 14px -2px rgba(11, 37, 64, 0.06), 0 1px 3px rgba(11, 37, 64, 0.04);
  --shadow-hover: 0 16px 32px -6px rgba(11, 37, 64, 0.09), 0 4px 12px -2px rgba(11, 37, 64, 0.04);
  --shadow-floating: 0 20px 40px -8px rgba(11, 37, 64, 0.16);

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
  font-size: 16px;
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}

body {
  font-family: var(--font-body);
  color: var(--color-body);
  background-color: var(--color-white);
  line-height: 1.65;
  letter-spacing: -0.011em;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

img, picture, svg, video {
  display: block;
  max-width: 100%;
  height: auto;
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  font: inherit;
  border: none;
  background: none;
  cursor: pointer;
}

ul, ol {
  list-style: none;
}

.skip-link {
  position: absolute;
  top: -100px;
  left: 1rem;
  background: var(--color-primary);
  color: #FFFFFF;
  padding: 0.75rem 1.5rem;
  z-index: 9999;
  border-radius: var(--radius-sm);
  font-weight: 600;
  transition: top 0.2s ease;
}
.skip-link:focus {
  top: 1rem;
}

/* --------------------------------------------------------------------------
   3. TYPOGRAPHY SYSTEM (BLU BLOOM EDITORIAL SERIF & SANS PAIRING)
   -------------------------------------------------------------------------- */
h1, h2, h3, h4, h5, h6,
.hero-headline h1,
.brief-main-title,
.section-header-center h2,
.section-heading h2,
.process-header h2,
.why-choose-header h2 {
  font-family: var(--font-serif);
  color: var(--color-primary);
  font-weight: 600;
  line-height: 1.22;
  letter-spacing: -0.015em;
}

h1 {
  font-size: clamp(2.4rem, 4.4vw, 3.6rem);
  font-weight: 600;
  line-height: 1.15;
}

h2 {
  font-size: clamp(1.9rem, 3.2vw, 2.7rem);
  font-weight: 600;
  line-height: 1.2;
}

h3 {
  font-size: clamp(1.3rem, 2vw, 1.7rem);
  font-weight: 600;
  line-height: 1.28;
}

h4 {
  font-size: 1.15rem;
  font-weight: 600;
  line-height: 1.35;
}

p {
  font-size: 1rem;
  line-height: 1.7;
  color: var(--color-body);
}

/* Editorial Italic Emphasis (Blu Bloom Signature) */
h1 em, h2 em, h3 em,
.hero-headline h1 em,
.highlight, .highlight-serif {
  font-family: var(--font-serif);
  font-style: italic;
  font-weight: 400;
  color: var(--color-accent);
}

.eyebrow,
.pill-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-sans);
  font-size: 0.72rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: var(--color-accent);
  background: var(--color-accent-subtle);
  border: 1px solid var(--color-accent-border);
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-full);
}

.section-header-center {
  text-align: center;
  max-width: 760px;
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
  max-width: 680px;
}

/* Flex Row Section Heading (Blu Bloom Signature) */
.section-heading-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 3rem;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.text-link {
  color: var(--color-primary);
  font-weight: 600;
  font-size: 0.92rem;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: color 0.2s ease, gap 0.2s ease;
}
.text-link:hover {
  color: var(--color-accent);
  gap: 9px;
}
.text-link .arrow-icon {
  font-size: 1.05rem;
  transition: transform 0.2s ease;
}
.text-link:hover .arrow-icon {
  transform: translate(2px, -2px);
}

/* --------------------------------------------------------------------------
   4. CONTAINERS & LAYOUT SYSTEM
   -------------------------------------------------------------------------- */
.container {
  width: 100%;
  max-width: var(--max-width);
  margin-left: auto;
  margin-right: auto;
  padding-left: clamp(1rem, 3vw, 2rem);
  padding-right: clamp(1rem, 3vw, 2rem);
}

.container-narrow {
  max-width: 900px;
}

/* --------------------------------------------------------------------------
   5. BUTTONS & UI ELEMENTS
   -------------------------------------------------------------------------- */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-family: var(--font-body);
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1;
  padding: 0.85rem 1.65rem;
  border-radius: var(--radius-sm);
  transition: all 0.2s var(--ease-out);
  text-align: center;
  white-space: nowrap;
  border: 1px solid transparent;
}

.btn-primary {
  background-color: var(--color-primary);
  color: #FFFFFF !important;
  border-color: var(--color-primary);
}
.btn-primary:hover {
  background-color: var(--color-primary-hover);
  border-color: var(--color-primary-hover);
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(11, 37, 64, 0.25);
}

.btn-secondary, .btn-gold {
  background-color: var(--color-accent);
  color: #FFFFFF !important;
  border-color: var(--color-accent);
}
.btn-secondary:hover, .btn-gold:hover {
  background-color: var(--color-accent-hover);
  border-color: var(--color-accent-hover);
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(184, 144, 88, 0.35);
}

.btn-outline {
  background-color: transparent;
  color: var(--color-primary);
  border-color: var(--color-primary);
}
.btn-outline:hover {
  background-color: var(--color-primary);
  color: #FFFFFF !important;
  transform: translateY(-1px);
}

.btn-outline-white {
  background-color: transparent;
  color: #FFFFFF !important;
  border-color: rgba(255, 255, 255, 0.4);
}
.btn-outline-white:hover {
  background-color: #FFFFFF;
  color: var(--color-primary) !important;
  border-color: #FFFFFF;
}

/* WhatsApp Button: STRICTLY AND EXCLUSIVELY GREEN */
.btn-whatsapp,
a[href*="wa.me"].btn {
  background-color: var(--color-whatsapp) !important;
  color: #FFFFFF !important;
  border-color: var(--color-whatsapp) !important;
}
.btn-whatsapp:hover,
a[href*="wa.me"].btn:hover {
  background-color: var(--color-whatsapp-hover) !important;
  border-color: var(--color-whatsapp-hover) !important;
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(37, 211, 102, 0.35);
}

/* --------------------------------------------------------------------------
   6. LEVEL 1: TOP UTILITY BAR (MIDNIGHT NAVY)
   -------------------------------------------------------------------------- */
.top-utility-bar {
  background-color: var(--color-dark-surface);
  color: #CBD5E1;
  font-size: 0.78rem;
  font-weight: 500;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding: 0.45rem 0;
}
.top-utility-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.top-utility-left {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}
.badge-welcome {
  color: var(--color-accent);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
.utility-timing {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  color: #E2E8F0;
}
.top-utility-right {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}
.top-utility-link {
  color: #CBD5E1;
  transition: color 0.15s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}
.top-utility-link:hover {
  color: var(--color-accent);
}
.utility-wa {
  color: #25D366;
  font-weight: 600;
}
.top-utility-social {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}
.top-utility-social a {
  color: #94A3B8;
  transition: color 0.15s ease;
}
.top-utility-social a:hover {
  color: #FFFFFF;
}

/* --------------------------------------------------------------------------
   7. LEVEL 2: MAIN SITE HEADER & NAVIGATION
   -------------------------------------------------------------------------- */
.site-header {
  background-color: #FFFFFF;
  position: sticky;
  top: 0;
  z-index: 900;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  border-bottom: 1px solid var(--color-border);
}
.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: var(--header-height);
}
.site-logo {
  display: flex;
  align-items: center;
}
.brand-logo-img {
  height: 52px;
  width: auto;
  object-fit: contain;
}
.site-nav {
  display: flex;
  align-items: center;
  gap: 1.75rem;
}
.nav-link {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--color-primary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.5rem 0;
  position: relative;
  transition: color 0.15s ease;
}
.nav-link:hover,
.nav-link.active {
  color: var(--color-accent);
}
.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--color-accent);
  transition: width 0.2s ease;
}
.nav-link:hover::after,
.nav-link.active::after {
  width: 100%;
}
.nav-cta {
  display: flex;
  align-items: center;
  gap: 1rem;
}

/* Hamburger toggle for mobile */
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  padding: 6px;
  cursor: pointer;
}
.hamburger span {
  width: 24px;
  height: 2px;
  background-color: var(--color-primary);
  transition: all 0.2s ease;
}

/* --------------------------------------------------------------------------
   8. HERO SECTION (EDITORIAL BLU BLOOM PRESENTATION)
   -------------------------------------------------------------------------- */
.hero-livspace {
  padding: clamp(3rem, 6vw, 4.5rem) 0 3.5rem;
  background: linear-gradient(180deg, var(--color-bg-light) 0%, #FFFFFF 100%);
  position: relative;
  overflow: hidden;
}
.hero-layout {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: clamp(2rem, 4vw, 3.5rem);
  align-items: center;
}
.hero-headline h1 {
  margin-bottom: 1.25rem;
  letter-spacing: -0.02em;
}
.hero-subhead {
  font-size: clamp(1rem, 1.2vw, 1.12rem);
  color: var(--color-body);
  line-height: 1.7;
  max-width: 600px;
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
  color: var(--color-primary);
}
.hero-usp-item svg {
  width: 18px;
  height: 18px;
  fill: var(--color-accent);
  flex-shrink: 0;
}
.hero-cta-group {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-top: 2.2rem;
  flex-wrap: wrap;
}
.hero-visual-showcase {
  position: relative;
}
.hero-visual-showcase img {
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-hover);
  border: 1px solid rgba(184, 144, 88, 0.2);
}

/* --------------------------------------------------------------------------
   9. TRUST METRIC STRIP (BLU BLOOM NUMBERED SUMMARY)
   -------------------------------------------------------------------------- */
.trust-strip-section {
  background-color: var(--color-primary);
  color: #FFFFFF;
  padding: 2.2rem 0;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.trust-metrics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}
.trust-metric-item {
  text-align: center;
  border-right: 1px solid rgba(255, 255, 255, 0.12);
  padding: 0 1rem;
}
.trust-metric-item:last-child {
  border-right: none;
}
.trust-metric-num {
  font-family: var(--font-serif);
  font-size: clamp(2rem, 3.2vw, 2.75rem);
  font-weight: 700;
  color: var(--color-accent);
  line-height: 1;
  margin-bottom: 0.35rem;
}
.trust-metric-label {
  font-size: 0.85rem;
  font-weight: 500;
  color: #E2E8F0;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* --------------------------------------------------------------------------
   10. WHY CHOOSE US (SECTION 2.5 - SCREENSHOT 1 INTEGRATION)
   -------------------------------------------------------------------------- */
.why-choose-section {
  padding: 5rem 0;
  background-color: var(--color-white);
}
.why-choose-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}
.why-choose-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-top: 3px solid var(--color-accent);
  border-radius: var(--radius-sm);
  padding: 2.2rem 1.6rem;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.why-choose-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}
.why-choose-icon-wrap {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-sm);
  background: var(--color-accent-subtle);
  border: 1px solid var(--color-accent-border);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
  color: var(--color-accent);
}
.why-choose-icon-wrap svg {
  width: 26px;
  height: 26px;
  stroke: var(--color-accent);
}
.why-choose-title {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  color: var(--color-primary);
  margin-bottom: 0.65rem;
}
.why-choose-desc {
  font-size: 0.9rem;
  color: var(--color-muted);
  line-height: 1.65;
  margin-bottom: 1rem;
}
.why-choose-tag {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--color-accent);
}

/* --------------------------------------------------------------------------
   11. SERVICES SECTION ("DESIGNED AND DELIVERED UNDER ONE ROOF")
   -------------------------------------------------------------------------- */
.services-section {
  padding: 5rem 0;
  background-color: var(--color-bg-light);
}
.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}
.service-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.service-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
  border-color: rgba(184, 144, 88, 0.4);
}
.service-card-media {
  position: relative;
  height: 220px;
  overflow: hidden;
}
.service-card-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.service-card:hover .service-card-media img {
  transform: scale(1.05);
}
.service-card-body {
  padding: 1.6rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.service-card-title {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  color: var(--color-primary);
  margin-bottom: 0.5rem;
}
.service-card-desc {
  font-size: 0.9rem;
  color: var(--color-muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
  flex-grow: 1;
}

/* --------------------------------------------------------------------------
   12. AN INTERIOR SOLUTION FOR EVERY BRIEF (SECTION 6.5 - SCREENSHOT 2)
   -------------------------------------------------------------------------- */
.brief-solutions-section {
  padding: 5rem 0;
  background-color: var(--color-white);
}
.brief-tiers-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1.25rem;
}
.brief-tier-card {
  background-color: var(--color-ivory);
  border: 1px solid #E5E0D5;
  border-radius: var(--radius-sm);
  padding: 2rem 1.4rem;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.brief-tier-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(11, 37, 64, 0.08);
  border-color: var(--color-accent);
}
.brief-tier-num {
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-accent);
  margin-bottom: 1rem;
}
.brief-tier-title {
  font-family: var(--font-serif);
  font-size: 1.35rem;
  color: var(--color-primary);
  margin-bottom: 0.65rem;
}
.brief-tier-desc {
  font-size: 0.88rem;
  color: var(--color-muted);
  line-height: 1.6;
  margin-bottom: 1.5rem;
  flex-grow: 1;
}
.brief-tier-link {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-primary);
  text-decoration: underline;
  text-underline-offset: 4px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  transition: color 0.15s ease;
}
.brief-tier-link:hover {
  color: var(--color-accent);
}

/* --------------------------------------------------------------------------
   13. IMMERSIVE NAVY PROCESS SECTION ("FROM SITE VISIT TO HANDOVER")
   -------------------------------------------------------------------------- */
.process-section {
  background-color: var(--color-primary) !important;
  color: #FFFFFF !important;
  padding: 5.5rem 0;
}
.process-section .section-header-center h2 {
  color: #FFFFFF !important;
}
.process-section .section-header-center p {
  color: #CBD5E1 !important;
}
.process-section .pill-badge {
  background: rgba(184, 144, 88, 0.18) !important;
  color: #E8D8BA !important;
  border-color: rgba(184, 144, 88, 0.35) !important;
}
.process-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-top: 2.5rem;
}
.process-step {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-sm);
  padding: 2.2rem 1.6rem;
  transition: transform 0.25s ease, border-color 0.25s ease, background 0.25s ease;
}
.process-step:hover {
  transform: translateY(-4px);
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--color-accent);
}
.step-circle {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--color-accent);
  color: #FFFFFF;
  font-family: var(--font-serif);
  font-weight: 700;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
  box-shadow: 0 4px 12px rgba(184, 144, 88, 0.35);
}
.process-step h4,
.process-step h3 {
  font-family: var(--font-serif);
  color: #FFFFFF;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}
.process-step p {
  color: #CBD5E1;
  font-size: 0.88rem;
  line-height: 1.6;
}

/* --------------------------------------------------------------------------
   14. PORTFOLIO SHOWCASE SECTION ("SPACES WITH A POINT OF VIEW")
   -------------------------------------------------------------------------- */
.portfolio-section {
  padding: 5rem 0;
  background-color: var(--color-bg-light);
}
.room-tabs-bar {
  display: flex;
  justify-content: center;
  gap: 0.65rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}
.room-tab-btn {
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 600;
  padding: 0.55rem 1.25rem;
  border-radius: var(--radius-full);
  background: var(--color-white);
  color: var(--color-primary);
  border: 1px solid var(--color-border);
  cursor: pointer;
  transition: all 0.2s ease;
}
.room-tab-btn:hover {
  border-color: var(--color-accent);
  color: var(--color-accent);
}
.room-tab-btn.active {
  background: var(--color-primary);
  color: #FFFFFF;
  border-color: var(--color-primary);
}
.room-cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}
.room-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  overflow: hidden;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out);
}
.room-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
  border-color: rgba(184, 144, 88, 0.4);
}
.room-card-media {
  height: 240px;
  overflow: hidden;
}
.room-card-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.room-card:hover .room-card-media img {
  transform: scale(1.05);
}
.room-card-content {
  padding: 1.5rem;
}
.room-card-title {
  font-family: var(--font-serif);
  font-size: 1.2rem;
  color: var(--color-primary);
  margin-bottom: 0.35rem;
}
.room-card-meta {
  font-size: 0.82rem;
  color: var(--color-muted);
}

/* --------------------------------------------------------------------------
   15. FAQ ACCORDION
   -------------------------------------------------------------------------- */
.faq-section {
  padding: 5rem 0;
  background-color: var(--color-white);
}
.faq-list {
  max-width: 820px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.faq-item {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: var(--color-white);
  overflow: hidden;
  transition: border-color 0.2s ease;
}
.faq-item:hover,
.faq-item.active,
.faq-item.open {
  border-color: var(--color-accent);
}
.faq-question {
  width: 100%;
  text-align: left;
  padding: 1.25rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font-serif);
  font-size: 1.12rem;
  color: var(--color-primary);
  font-weight: 600;
  cursor: pointer;
}
.faq-question .chevron {
  font-size: 0.8rem;
  color: var(--color-accent);
  transition: transform 0.25s ease;
}
.faq-item.active .chevron,
.faq-item.open .chevron {
  transform: rotate(180deg);
}
.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s ease;
}
.faq-item.active .faq-answer,
.faq-item.open .faq-answer {
  max-height: 400px;
}
.faq-answer p {
  padding: 0 1.5rem 1.25rem;
  font-size: 0.95rem;
  color: var(--color-body);
  line-height: 1.7;
}

/* --------------------------------------------------------------------------
   16. FINAL HIGH-IMPACT CTA BANNER (BLU BLOOM .CONSULT-CTA)
   -------------------------------------------------------------------------- */
.final-cta-section {
  background-color: var(--color-primary) !important;
  color: #FFFFFF !important;
  padding: 6rem 0;
  text-align: center;
}
.final-cta-section h2 {
  font-family: var(--font-serif);
  font-size: clamp(2.2rem, 3.8vw, 3.4rem);
  color: #FFFFFF !important;
  margin-bottom: 1rem;
}
.final-cta-section p {
  color: #CBD5E1 !important;
  font-size: 1.05rem;
  max-width: 680px;
  margin: 0 auto 2.2rem;
}
.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* --------------------------------------------------------------------------
   17. SITE FOOTER (OBSIDIAN NAVY ARCHITECTURAL FOOTER)
   -------------------------------------------------------------------------- */
.site-footer {
  background-color: var(--color-dark-surface);
  color: #94A3B8;
  padding: 4.5rem 0 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr 1.2fr;
  gap: 2.5rem;
  margin-bottom: 3.5rem;
}
.footer-col p {
  color: #94A3B8;
  font-size: 0.88rem;
  line-height: 1.7;
}
.footer-heading {
  font-family: var(--font-sans);
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--color-accent);
  margin-bottom: 1.25rem;
}
.footer-links {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}
.footer-links a {
  font-size: 0.88rem;
  color: #CBD5E1;
  transition: color 0.15s ease;
}
.footer-links a:hover {
  color: #FFFFFF;
}
.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 2rem;
  font-size: 0.82rem;
  color: #64748B;
}
.footer-legal-links {
  display: flex;
  gap: 1.5rem;
}
.footer-legal-links a {
  color: #64748B;
  transition: color 0.15s ease;
}
.footer-legal-links a:hover {
  color: #FFFFFF;
}

/* --------------------------------------------------------------------------
   18. FLOATING ACTION CONTROLS (CALL ABOVE WHATSAPP)
   -------------------------------------------------------------------------- */
.floating-actions-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
  z-index: 995;
}
.call-float,
.whatsapp-float {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  position: relative;
  transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.25s ease, background-color 0.2s ease;
}
.call-float {
  background-color: var(--color-primary);
  color: #FFFFFF;
  border: 1px solid rgba(184, 144, 88, 0.4);
  box-shadow: 0 4px 16px rgba(11, 37, 64, 0.4);
}
.call-float:hover {
  background-color: var(--color-primary-hover);
  transform: translateY(-2px) scale(1.06);
  box-shadow: 0 8px 24px rgba(11, 37, 64, 0.55);
}
.call-float svg {
  width: 22px;
  height: 22px;
  fill: #FFFFFF;
  transition: transform 0.2s ease;
}
.call-float:hover svg {
  transform: rotate(12deg);
}

.whatsapp-float {
  background-color: #25D366;
  color: #FFFFFF;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
}
.whatsapp-float:hover {
  background-color: #20BD5A;
  transform: translateY(-2px) scale(1.06);
  box-shadow: 0 8px 24px rgba(37, 211, 102, 0.55);
}
.whatsapp-float svg {
  width: 26px;
  height: 26px;
  fill: #FFFFFF;
}

.call-tooltip,
.whatsapp-tooltip {
  position: absolute;
  right: 64px;
  top: 50%;
  transform: translateY(-50%);
  background-color: #060E18;
  color: #FFFFFF;
  font-size: 0.78rem;
  font-weight: 600;
  white-space: nowrap;
  padding: 6px 12px;
  border-radius: 6px;
  border: 1px solid rgba(184, 144, 88, 0.3);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
  pointer-events: none;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s ease, visibility 0.2s ease, transform 0.2s ease;
}
.call-float:hover .call-tooltip,
.whatsapp-float:hover .whatsapp-tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(-4px);
}

/* Standalone fallbacks */
body > a.whatsapp-float:not(.floating-actions-container a) {
  position: fixed;
  right: 24px;
  bottom: 24px;
  z-index: 995;
}
body > a.call-float:not(.floating-actions-container a) {
  position: fixed;
  right: 24px;
  bottom: 86px;
  left: auto;
  z-index: 995;
}

/* --------------------------------------------------------------------------
   19. MOBILE STICKY BOTTOM ACTIONS
   -------------------------------------------------------------------------- */
.sticky-mobile-cta {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: #FFFFFF;
  border-top: 1px solid var(--color-border);
  box-shadow: 0 -4px 16px rgba(11, 37, 64, 0.08);
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
  border-radius: var(--radius-sm);
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none;
}
.btn-call {
  background: var(--color-primary);
  color: #FFFFFF !important;
}
.btn-wa {
  background: var(--color-whatsapp);
  color: #FFFFFF !important;
}

/* --------------------------------------------------------------------------
   20. RESPONSIVE DESIGN BREAKPOINTS
   -------------------------------------------------------------------------- */
@media (max-width: 1024px) {
  .hero-layout {
    grid-template-columns: 1fr;
  }
  .services-grid,
  .room-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .brief-tiers-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  .why-choose-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .process-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .top-utility-bar {
    display: none;
  }
  .site-nav {
    display: none;
  }
  .hamburger {
    display: flex;
  }
  .sticky-mobile-cta {
    display: block;
  }
  .floating-actions-container {
    bottom: 74px;
    right: 16px;
    gap: 10px;
  }
  body > a.whatsapp-float:not(.floating-actions-container a) {
    bottom: 74px;
    right: 16px;
  }
  body > a.call-float:not(.floating-actions-container a) {
    bottom: 136px;
    right: 16px;
    left: auto;
  }
  .call-float, .whatsapp-float {
    width: 48px;
    height: 48px;
  }
  .call-float svg {
    width: 20px;
    height: 20px;
  }
  .whatsapp-float svg {
    width: 24px;
    height: 24px;
  }
  .call-tooltip, .whatsapp-tooltip {
    display: none;
  }
  body {
    padding-bottom: 60px;
  }
  .services-grid,
  .room-cards-grid,
  .why-choose-grid,
  .process-grid,
  .brief-tiers-grid {
    grid-template-columns: 1fr;
  }
  .trust-metrics-grid {
    grid-template-columns: repeat(2, 1fr);
    row-gap: 1.5rem;
  }
  .trust-metric-item:nth-child(2) {
    border-right: none;
  }
  .footer-grid {
    grid-template-columns: 1fr;
  }
  .footer-bottom {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
}
'''
    return style_content

def main():
    css = create_blubloom_master_style()
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Compiled new assets/css/style.css successfully!")

    # Also update generate_master_style.py to match
    with open('scripts/generate_master_style.py', 'w', encoding='utf-8') as f:
        f.write('css = """' + css + '"""\n\ndef generate_style():\n    with open("assets/css/style.css", "w", encoding="utf-8") as f:\n        f.write(css)\n\nif __name__ == "__main__":\n    generate_style()\n')
    print("Updated scripts/generate_master_style.py successfully!")

if __name__ == '__main__':
    main()
