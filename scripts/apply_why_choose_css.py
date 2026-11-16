import re

new_why_choose_css = """/* --------------------------------------------------------------------------
   16. WHY CHOOSE US (SECTION 2.5 - EXACT IMAGE 1 SPECIFICATION)
   -------------------------------------------------------------------------- */
.why-choose-section {
  position: relative;
  padding: clamp(4.5rem, 7vw, 6.5rem) 0;
  background-image: linear-gradient(rgba(248, 246, 240, 0.88), rgba(248, 246, 240, 0.94)), url('/assets/images/portfolio-bedroom.webp');
  background-position: center 30%;
  background-size: cover;
  background-repeat: no-repeat;
  border-bottom: 1px solid var(--color-border);
}

.why-choose-header-center {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 2.75rem auto;
}

.why-choose-main-title {
  font-family: var(--font-display);
  font-size: clamp(2.2rem, 3.8vw, 2.85rem);
  font-weight: 700;
  color: var(--color-primary);
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.why-choose-main-sub {
  font-family: var(--font-sans);
  font-size: 1.1rem;
  color: #5A6472;
  margin: 0;
  line-height: 1.5;
}

/* Floating White Card Container (Exact Image 1 Layout) */
.why-choose-floating-box {
  background: #FFFFFF;
  border-radius: 6px;
  box-shadow: 0 20px 48px -10px rgba(11, 37, 64, 0.10), 0 4px 16px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(226, 232, 240, 0.9);
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  padding: 3.5rem 1.5rem;
  box-sizing: border-box;
}

.why-choose-col {
  padding: 0.5rem 2rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-right: 1px solid #EEF2F6;
  box-sizing: border-box;
}

.why-choose-col:last-child {
  border-right: none;
}

.why-choose-icon-box {
  width: 64px;
  height: 64px;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-primary);
  transition: transform 0.25s ease;
}

.why-choose-floating-box:hover .why-choose-col:hover .why-choose-icon-box {
  transform: translateY(-3px);
}

.why-choose-col-title {
  font-family: var(--font-sans);
  font-size: 1.18rem;
  font-weight: 700;
  color: var(--color-primary);
  margin-bottom: 0.85rem;
  line-height: 1.35;
}

.why-choose-col-desc {
  font-size: 0.88rem;
  color: #5A6472;
  line-height: 1.65;
  margin: 0;
}

@media (max-width: 1024px) {
  .why-choose-floating-box {
    grid-template-columns: repeat(2, 1fr);
    padding: 2.5rem 1rem;
    gap: 2rem 0;
  }
  .why-choose-col:nth-child(2) {
    border-right: none;
  }
  .why-choose-col:nth-child(1),
  .why-choose-col:nth-child(2) {
    border-bottom: 1px solid #EEF2F6;
    padding-bottom: 2rem;
  }
}

@media (max-width: 640px) {
  .why-choose-floating-box {
    grid-template-columns: 1fr;
    padding: 2rem 1rem;
    gap: 2rem;
  }
  .why-choose-col {
    border-right: none !important;
    border-bottom: 1px solid #EEF2F6;
    padding: 0 1rem 2rem 1rem;
  }
  .why-choose-col:last-child {
    border-bottom: none;
    padding-bottom: 0;
  }
}"""

target_pattern = r'/\* -+ 16\. WHY CHOOSE US[\s\S]*?(?=/\* -+ 16\.1 AN INTERIOR SOLUTION|\Z)'

for fname in ['assets/css/style.css', 'scripts/generate_master_style.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated, count = re.subn(target_pattern, new_why_choose_css + "\n\n", content, count=1)
    if count == 0:
        # Fallback search if header comment differs slightly
        fallback_pattern = r'\.why-choose-section\s*\{[\s\S]*?(?=/\* -+ 16\.1|\Z)'
        updated, count = re.subn(fallback_pattern, new_why_choose_css + "\n\n", content, count=1)
    
    print(f'Updated {fname}: replaced {count} occurrences')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(updated)
