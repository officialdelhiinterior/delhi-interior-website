with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

kd_styles = '''
/* ==========================================================================
   HOMESTYLING BY KD HEADER & TRUST ARCHITECTURE
   ========================================================================== */

/* 1. Top Utility Bar */
.top-utility-bar {
  background-color: #0F172A;
  color: #94A3B8;
  font-size: 0.8rem;
  padding: 0.45rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.top-utility-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.top-utility-left {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}
.top-utility-left span.badge-welcome {
  color: #F8FAFC;
  font-weight: 600;
}
.top-utility-right {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}
.top-utility-social {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.top-utility-social a {
  color: #94A3B8;
  display: flex;
  align-items: center;
  transition: color var(--trans-fast);
}
.top-utility-social a:hover {
  color: #FFFFFF;
}
.top-utility-link {
  color: #CBD5E1;
  text-decoration: none;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  transition: color var(--trans-fast);
}
.top-utility-link:hover {
  color: var(--color-primary);
}

/* 2. Main Site Header (Sticky Tier) */
.site-header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  background: #FFFFFF;
  z-index: 990;
  border-bottom: 1px solid var(--color-border);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
  transition: all var(--trans-fast);
}
.site-header.scrolled {
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
}
.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
}

/* 3. Under-Nav Contact Trust Bar (KD Signature Component) */
.under-nav-bar {
  background-color: #FFFFFF;
  border-bottom: 1px solid var(--color-border);
  padding: 0.85rem 0;
  position: relative;
  z-index: 10;
}
.under-nav-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr;
  gap: 1.5rem;
  align-items: center;
}
.under-nav-item {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
  color: inherit;
  transition: transform var(--trans-fast);
}
.under-nav-item:hover {
  transform: translateY(-1px);
}
.under-nav-icon {
  width: 42px;
  height: 42px;
  border-radius: var(--radius-md);
  background: var(--color-primary-light);
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.under-nav-text {
  display: flex;
  flex-direction: column;
}
.under-nav-text h6 {
  font-size: 0.76rem;
  font-weight: 800;
  color: var(--color-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin: 0 0 0.15rem 0;
}
.under-nav-text p {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-dark);
  margin: 0;
  line-height: 1.25;
}
.under-nav-item:hover .under-nav-text p {
  color: var(--color-primary);
}

/* 4. KD-Style Unique Selling Points (USPs) Section */
.usps-section-kd {
  padding: 5rem 0;
  background: #FFFFFF;
}
.usps-grid-kd {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3rem;
}
.usp-card-kd {
  background: #F8FAFC;
  border: 1px solid var(--color-border);
  border-radius: 16px;
  padding: 2rem;
  transition: transform 250ms ease, box-shadow 250ms ease, border-color 250ms ease;
  display: flex;
  flex-direction: column;
}
.usp-card-kd:hover {
  transform: translateY(-5px);
  background: #FFFFFF;
  border-color: var(--color-primary-subtle);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.07);
}
.usp-card-icon {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  background: var(--color-primary-light);
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
}
.usp-card-kd h3 {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--color-dark);
  margin-bottom: 0.75rem;
  line-height: 1.3;
}
.usp-card-kd p {
  font-size: 0.9rem;
  color: var(--color-body);
  line-height: 1.6;
  margin: 0;
}

/* 5. "Why Do You Need Interior Designers in Delhi" Section */
.why-need-section {
  padding: 5rem 0;
  background: #F1F5F9;
}
.why-need-layout {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 3.5rem;
  align-items: center;
}
.why-need-content h2 {
  font-size: 2.3rem;
  font-weight: 800;
  color: var(--color-dark);
  margin-bottom: 1.25rem;
  line-height: 1.2;
}
.why-need-content p {
  font-size: 1rem;
  color: var(--color-body);
  line-height: 1.7;
  margin-bottom: 1.5rem;
}
.why-need-points {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
  margin-top: 1.5rem;
}
.why-point-box {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 1rem 1.25rem;
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}
.why-point-icon {
  color: var(--color-primary);
  font-weight: 800;
  font-size: 1.1rem;
  line-height: 1;
  margin-top: 0.15rem;
}
.why-point-box strong {
  display: block;
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--color-dark);
  margin-bottom: 0.2rem;
}
.why-point-box span {
  display: block;
  font-size: 0.8rem;
  color: var(--color-muted);
  line-height: 1.4;
}

/* 6. Dual Specialization: Residential & Commercial Banner */
.dual-specialty-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-top: 2rem;
}
.specialty-card {
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  min-height: 340px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 2.5rem;
  color: #FFFFFF;
  box-shadow: 0 14px 35px rgba(0, 0, 0, 0.1);
}
.specialty-card img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
  transition: transform 500ms ease;
}
.specialty-card:hover img {
  transform: scale(1.05);
}
.specialty-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, rgba(15, 23, 42, 0.15) 0%, rgba(15, 23, 42, 0.88) 100%);
  z-index: 2;
}
.specialty-content {
  position: relative;
  z-index: 3;
}
.specialty-tag {
  display: inline-block;
  background: var(--color-primary);
  color: #FFFFFF;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.3rem 0.8rem;
  border-radius: var(--radius-pill);
  margin-bottom: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.specialty-content h3 {
  font-size: 1.6rem;
  font-weight: 800;
  color: #FFFFFF;
  margin-bottom: 0.5rem;
}
.specialty-content p {
  font-size: 0.92rem;
  color: #E2E8F0;
  line-height: 1.5;
  margin-bottom: 1.25rem;
}

@media (max-width: 1024px) {
  .under-nav-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  .usps-grid-kd {
    grid-template-columns: repeat(2, 1fr);
  }
  .why-need-layout {
    grid-template-columns: 1fr;
  }
  .dual-specialty-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .top-utility-container {
    flex-direction: column;
    gap: 0.4rem;
    text-align: center;
  }
  .usps-grid-kd {
    grid-template-columns: 1fr;
  }
  .why-need-points {
    grid-template-columns: 1fr;
  }
}
'''

css += '\n' + kd_styles

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('[SUCCESS] assets/css/style.css updated with Home Styling by KD menu bar, top bar, under-nav bar, and content styling.')
