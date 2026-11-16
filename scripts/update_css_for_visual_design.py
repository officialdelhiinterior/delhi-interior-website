import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

visual_enhancements = '''
/* ==========================================================================
   LIVSPACE HIGH-END VISUAL DESIGN SYSTEM
   ========================================================================== */

/* Hero Section Enhancements */
.hero-livspace {
  padding-top: calc(72px + 40px + 2rem);
  padding-bottom: 3rem;
  background: #FFFFFF;
  position: relative;
}
.hero-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}
.hero-headline h1 {
  font-size: 2.75rem;
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: var(--color-dark);
  margin-bottom: 1rem;
}
.hero-headline h1 span.highlight {
  color: var(--color-primary);
}
.hero-subhead {
  font-size: 1.08rem;
  color: #4B5563;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}
.hero-usps {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}
.hero-usp-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-dark);
}
.hero-usp-item svg {
  width: 18px;
  height: 18px;
  fill: var(--color-green);
  flex-shrink: 0;
}

/* Hero Visual Showcase Right */
.hero-visual-showcase {
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12);
  height: 100%;
  min-height: 540px;
  max-height: 600px;
}
.hero-visual-showcase picture,
.hero-visual-showcase img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Floating Glass Badges on Hero Photo */
.hero-glass-badge {
  position: absolute;
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.85);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  border-radius: var(--radius-md);
  padding: 0.65rem 1rem;
  z-index: 10;
}
.hero-badge-location {
  top: 1.25rem;
  right: 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}
.hero-badge-location .icon {
  font-size: 1.2rem;
}
.hero-badge-location strong {
  display: block;
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--color-dark);
}
.hero-badge-location span {
  display: block;
  font-size: 0.72rem;
  color: var(--color-muted);
}
.hero-badge-warranty {
  bottom: 1.25rem;
  left: 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}
.hero-badge-warranty .check-icon {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--color-green);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 0.85rem;
}
.hero-badge-warranty strong {
  display: block;
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--color-dark);
}
.hero-badge-warranty span {
  display: block;
  font-size: 0.72rem;
  color: var(--color-muted);
}
.hero-badge-rating {
  bottom: 1.25rem;
  right: 1.25rem;
  text-align: right;
}
.hero-badge-rating .stars {
  color: #F59E0B;
  font-size: 0.85rem;
  display: block;
  letter-spacing: 2px;
}
.hero-badge-rating strong {
  display: block;
  font-size: 0.85rem;
  font-weight: 800;
  color: var(--color-dark);
}
.hero-badge-rating span {
  display: block;
  font-size: 0.72rem;
  color: var(--color-muted);
}

/* Integrated Hero Consultation Card Left */
.hero-consult-card-left {
  background: #F9FAFB;
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 1.4rem;
  margin-top: 1.5rem;
}
.hero-consult-card-left .consult-title {
  font-size: 0.95rem;
  font-weight: 800;
  color: var(--color-dark);
  margin-bottom: 0.3rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.hero-consult-card-left .consult-sub {
  font-size: 0.8rem;
  color: var(--color-muted);
  margin-bottom: 1rem;
}

/* Visual Services Grid Section */
.services-visual-section {
  padding: 5rem 0;
  background: #F9FAFB;
}
.services-visual-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 2.5rem;
}
.service-visual-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
  transition: transform 250ms ease, box-shadow 250ms ease, border-color 250ms ease;
  display: flex;
  flex-direction: column;
}
.service-visual-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.08);
  border-color: var(--color-primary-subtle);
}
.service-visual-img {
  position: relative;
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: #E5E7EB;
}
.service-visual-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 450ms ease;
}
.service-visual-card:hover .service-visual-img img {
  transform: scale(1.06);
}
.service-visual-tag {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: rgba(17, 24, 39, 0.85);
  color: #FFFFFF;
  backdrop-filter: blur(8px);
  padding: 0.35rem 0.8rem;
  border-radius: var(--radius-sm);
  font-size: 0.75rem;
  font-weight: 700;
  z-index: 2;
}
.service-visual-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.service-visual-body h3 {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--color-dark);
  margin-bottom: 0.5rem;
}
.service-visual-body p {
  font-size: 0.88rem;
  color: var(--color-body);
  line-height: 1.55;
  margin-bottom: 1.25rem;
  flex-grow: 1;
}
.service-visual-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}
.service-visual-pill {
  font-size: 0.75rem;
  font-weight: 600;
  color: #374151;
  background: #F3F4F6;
  padding: 0.25rem 0.65rem;
  border-radius: var(--radius-sm);
}
.service-visual-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--color-border);
  padding-top: 1rem;
  margin-top: auto;
}
.service-visual-price {
  font-size: 0.85rem;
  color: var(--color-muted);
}
.service-visual-price strong {
  font-size: 1rem;
  font-weight: 800;
  color: var(--color-dark);
}
.service-visual-link {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-primary);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  transition: transform var(--trans-fast);
}
.service-visual-link:hover {
  transform: translateX(4px);
}

@media (max-width: 1024px) {
  .hero-layout {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  .hero-visual-showcase {
    min-height: 380px;
    max-height: 440px;
  }
  .services-visual-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .hero-headline h1 {
    font-size: 2.1rem;
  }
  .services-visual-grid {
    grid-template-columns: 1fr;
  }
}
'''

css += '\n' + visual_enhancements

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('[SUCCESS] assets/css/style.css updated with Livspace Visual Design System.')
