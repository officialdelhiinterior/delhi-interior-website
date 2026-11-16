with open('scripts/generate_master_style.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update FAQ accordion rules to support both .active and .open, plus .chevron rotation
old_faq_css = '''.faq-item {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: border-color var(--duration-fast) ease, box-shadow var(--duration-fast) ease;
}
.faq-item.active {
  border-color: var(--color-primary);
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
}'''

new_faq_css = '''.faq-item {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: border-color var(--duration-fast) ease, box-shadow var(--duration-fast) ease;
}
.faq-item.active,
.faq-item.open {
  border-color: var(--color-primary);
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
  cursor: pointer;
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
.faq-item.active .faq-icon,
.faq-item.open .faq-icon {
  transform: rotate(45deg);
  background: var(--color-primary);
  color: #FFFFFF;
}

.faq-question .chevron {
  font-size: 0.75rem;
  transition: transform var(--duration-fast) ease;
  color: var(--color-muted);
}
.faq-item.active .chevron,
.faq-item.open .chevron {
  transform: rotate(180deg);
  color: var(--color-primary);
}

.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s var(--ease-out);
}
.faq-item.active .faq-answer,
.faq-item.open .faq-answer {
  max-height: 800px;
}

.faq-answer-inner,
.faq-answer p {
  padding: 0 1.6rem 1.4rem;
  font-size: 0.94rem;
  color: var(--color-body);
  line-height: 1.7;
}
.faq-answer-inner {
  border-top: 1px solid var(--color-border-light);
  padding-top: 1rem;
}'''

code = code.replace(old_faq_css, new_faq_css)

# 2. Add styles for Section 2.5 "Why Choose Us" and Section 6.5 "An interior solution for every brief"
new_sections_css = '''/* --------------------------------------------------------------------------
   12.1 WHY CHOOSE US CARDS (SECTION 2.5)
   -------------------------------------------------------------------------- */
.why-choose-section {
  padding: clamp(3.5rem, 6vw, 5.5rem) 0;
  background-color: var(--color-white);
  border-bottom: 1px solid var(--color-border);
}

.why-choose-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.why-choose-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2.2rem 1.6rem;
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out), border-color 0.25s ease;
}
.why-choose-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
  border-color: var(--color-primary-border);
}

.why-choose-icon {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-md);
  background: var(--color-accent-subtle);
  border: 1px solid var(--color-accent-border);
  color: var(--color-accent);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
}

.why-choose-card h3 {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--color-dark);
  margin-bottom: 0.65rem;
}

.why-choose-card p {
  font-size: 0.9rem;
  color: var(--color-body);
  line-height: 1.65;
  margin-bottom: 1.25rem;
  flex: 1;
}

/* --------------------------------------------------------------------------
   16.1 AN INTERIOR SOLUTION FOR EVERY BRIEF (SECTION 6.5)
   -------------------------------------------------------------------------- */
.brief-solutions-section {
  padding: clamp(4rem, 6vw, 6rem) 0;
  background-color: #FFFFFF;
  border-top: 1px solid var(--color-border);
}

.brief-solutions-header {
  max-width: 820px;
  margin-bottom: 3rem;
}

.brief-main-title {
  font-family: var(--font-display);
  font-size: clamp(2.2rem, 3.8vw, 3rem);
  font-weight: 800;
  color: var(--color-dark);
  letter-spacing: -0.025em;
  margin-bottom: 1rem;
  line-height: 1.15;
}

.brief-sub-title {
  font-size: 1.05rem;
  color: var(--color-body);
  line-height: 1.7;
}

.brief-tiers-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1.25rem;
}

.brief-tier-card {
  background: #F8F6F0;
  border: 1px solid #ECE7DD;
  border-radius: var(--radius-sm);
  padding: 2.2rem 1.6rem 1.8rem;
  display: flex;
  flex-direction: column;
  transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease-out), border-color 0.25s ease;
}
.brief-tier-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
  border-color: var(--color-accent);
}

.brief-tier-num {
  font-family: var(--font-display);
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-accent);
  margin-bottom: 1.75rem;
  letter-spacing: 0.05em;
}

.brief-tier-title {
  font-family: var(--font-display);
  font-size: 1.45rem;
  font-weight: 700;
  color: var(--color-dark);
  margin-bottom: 0.75rem;
  line-height: 1.2;
}

.brief-tier-desc {
  font-size: 0.88rem;
  color: var(--color-body);
  line-height: 1.6;
  margin-bottom: 2rem;
  flex: 1;
}

.brief-tier-link {
  font-family: var(--font-display);
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--color-dark);
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  text-decoration: underline;
  text-underline-offset: 4px;
  transition: color var(--duration-fast) ease;
}
.brief-tier-link:hover {
  color: var(--color-accent);
}
.brief-tier-link .arrow-icon {
  font-size: 1rem;
  line-height: 1;
  transition: transform var(--duration-fast) ease;
}
.brief-tier-link:hover .arrow-icon {
  transform: translate(2px, -2px);
}
'''

# Insert the new CSS sections before Responsive Design
code = code.replace('/* --------------------------------------------------------------------------\n   24. RESPONSIVE DESIGN SYSTEM', new_sections_css + '\n/* --------------------------------------------------------------------------\n   24. RESPONSIVE DESIGN SYSTEM')

# Update responsive rules to include brief-tiers-grid and why-choose-grid
old_resp_1024 = '''  .craftsman-advantage-grid,
  .services-visual-grid,
  .room-cards-grid,'''

new_resp_1024 = '''  .craftsman-advantage-grid,
  .why-choose-grid,
  .brief-tiers-grid,
  .services-visual-grid,
  .room-cards-grid,'''

code = code.replace(old_resp_1024, new_resp_1024)

old_resp_640 = '''  .craftsman-advantage-grid,
  .services-visual-grid,
  .room-cards-grid,'''

new_resp_640 = '''  .craftsman-advantage-grid,
  .why-choose-grid,
  .brief-tiers-grid,
  .services-visual-grid,
  .room-cards-grid,'''

code = code.replace(old_resp_640, new_resp_640)

with open('scripts/generate_master_style.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated scripts/generate_master_style.py successfully.")
