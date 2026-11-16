css_additions = '''
/* ==========================================================================
   Services Marquee Ticker
   ========================================================================== */
.services-marquee-wrap {
  background: #F3F4F6;
  border-top: 1px solid var(--color-border);
  border-bottom: 1px solid var(--color-border);
  overflow: hidden;
  white-space: nowrap;
  position: relative;
  padding: 0.9rem 0;
}
.marquee-track {
  display: inline-flex;
  gap: 2.5rem;
  animation: marquee-scroll 35s linear infinite;
}
.services-marquee-wrap:hover .marquee-track {
  animation-play-state: paused;
}
.marquee-item {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 0.9rem;
  font-weight: 700;
  color: #374151;
  text-transform: capitalize;
  letter-spacing: 0.02em;
}
.marquee-item .dot {
  color: var(--color-primary);
  font-size: 1.1rem;
}
@keyframes marquee-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* ==========================================================================
   Hero Visual Enhancement
   ========================================================================== */
.hero-visual-card {
  position: relative;
  border-radius: var(--radius-xl);
  overflow: hidden;
  box-shadow: var(--shadow-xl);
  border: 1px solid var(--color-border);
  aspect-ratio: 16 / 11;
  margin-bottom: 1.5rem;
}
.hero-visual-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.hero-badge-top {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(17, 24, 39, 0.85);
  color: var(--color-white);
  backdrop-filter: blur(8px);
  padding: 0.4rem 0.9rem;
  border-radius: var(--radius-sm);
  font-size: 0.8rem;
  font-weight: 600;
}
.hero-badge-bottom {
  position: absolute;
  bottom: 1rem;
  left: 1rem;
  background: rgba(255, 255, 255, 0.95);
  color: var(--color-dark);
  backdrop-filter: blur(8px);
  padding: 0.5rem 1rem;
  border-radius: var(--radius-md);
  font-size: 0.82rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  box-shadow: var(--shadow-md);
}
.hero-badge-bottom .check {
  color: var(--color-green);
  font-weight: 900;
}

/* ==========================================================================
   What We Do — Services Showcase Accordion
   ========================================================================== */
.what-we-do-section {
  padding: 5.5rem 0;
  background-color: var(--color-white);
}
.what-we-do-grid {
  display: grid;
  grid-template-columns: 360px 1fr;
  gap: 4.5rem;
  align-items: flex-start;
}
.what-we-do-sidebar {
  position: sticky;
  top: 6.5rem;
}
.what-we-do-sidebar h2 {
  font-size: 2.4rem;
  font-weight: 800;
  color: var(--color-dark);
  line-height: 1.2;
  margin-bottom: 1rem;
}
.what-we-do-sidebar p {
  font-size: 1rem;
  color: var(--color-muted);
  line-height: 1.7;
  margin-bottom: 2rem;
}
.services-accordion-list {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}
.service-acc-card {
  background: #FAFAFA;
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all var(--trans-smooth);
}
.service-acc-card:hover {
  border-color: var(--color-primary-subtle);
  box-shadow: var(--shadow-md);
}
.service-acc-card.open {
  background: var(--color-white);
  border-color: var(--color-primary);
  box-shadow: 0 10px 25px rgba(224, 53, 70, 0.08);
}
.service-acc-header {
  width: 100%;
  padding: 1.4rem 1.6rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
}
.service-acc-title-group {
  display: flex;
  align-items: center;
  gap: 1.2rem;
}
.service-acc-icon {
  width: 46px;
  height: 46px;
  border-radius: var(--radius-md);
  background: var(--color-primary-light);
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.35rem;
  flex-shrink: 0;
  transition: all var(--trans-fast);
}
.service-acc-card.open .service-acc-icon {
  background: var(--color-primary);
  color: var(--color-white);
}
.service-acc-title-group h3 {
  font-size: 1.22rem;
  font-weight: 700;
  color: var(--color-dark);
  margin: 0;
}
.service-acc-toggle {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: var(--color-white);
  border: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  color: var(--color-dark);
  transition: transform var(--trans-fast), background var(--trans-fast), color var(--trans-fast);
}
.service-acc-card.open .service-acc-toggle {
  transform: rotate(45deg);
  background: var(--color-primary);
  color: var(--color-white);
  border-color: var(--color-primary);
}
.service-acc-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 400ms ease;
}
.service-acc-card.open .service-acc-content {
  max-height: 600px;
}
.service-acc-body {
  padding: 0 1.6rem 1.6rem;
  border-top: 1px solid var(--color-border);
  padding-top: 1.2rem;
}
.service-acc-body p {
  font-size: 0.95rem;
  color: #4B5563;
  line-height: 1.65;
  margin-bottom: 1.2rem;
}
.service-tags-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.4rem;
}
.service-tag {
  padding: 0.3rem 0.75rem;
  background: #F3F4F6;
  border: 1px solid #E5E7EB;
  border-radius: var(--radius-pill);
  font-size: 0.78rem;
  font-weight: 600;
  color: #374151;
}
.service-page-link {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--color-primary);
  text-decoration: none;
}
.service-page-link:hover {
  text-decoration: underline;
}

/* ==========================================================================
   Material Showcase ("Quality You Can Feel")
   ========================================================================== */
.material-showcase-section {
  padding: 5.5rem 0;
  background-color: #F8F9FA;
  border-top: 1px solid var(--color-border);
  border-bottom: 1px solid var(--color-border);
}
.materials-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1.5rem;
}
.material-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2rem 1.5rem;
  box-shadow: var(--shadow-sm);
  transition: all var(--trans-smooth);
  display: flex;
  flex-direction: column;
}
.material-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-hover);
  border-color: var(--color-primary-subtle);
}
.material-icon-wrap {
  font-size: 2.2rem;
  margin-bottom: 1.2rem;
}
.material-card h3 {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--color-dark);
  margin-bottom: 0.5rem;
}
.material-card p {
  font-size: 0.88rem;
  color: var(--color-muted);
  line-height: 1.6;
  margin-bottom: 1.2rem;
}
.material-spec-pill {
  margin-top: auto;
  display: inline-block;
  padding: 0.25rem 0.65rem;
  background: var(--color-green-light);
  color: var(--color-green);
  border-radius: var(--radius-pill);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

@media (max-width: 1024px) {
  .what-we-do-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  .what-we-do-sidebar {
    position: static;
  }
  .materials-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .materials-grid {
    grid-template-columns: 1fr;
  }
}
'''

with open('assets/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)

print('[SUCCESS] style.css updated with Marquee, What We Do, and Material Showcase!')
