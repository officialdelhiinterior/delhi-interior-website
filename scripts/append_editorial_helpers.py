import re

def append_editorial_helpers():
    helpers = '''
/* --------------------------------------------------------------------------
   EDITORIAL UTILITY & INTERACTIVE HELPERS (BLU BLOOM REFINEMENTS)
   -------------------------------------------------------------------------- */
.chevron {
  display: inline-block;
  font-size: 0.75rem;
  color: var(--color-accent);
  transition: transform 0.25s ease;
}
.faq-item.active .chevron,
.faq-item.open .chevron {
  transform: rotate(180deg);
}

.portfolio-section {
  padding: 5.5rem 0;
  background-color: var(--color-bg-light);
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

.utility-call {
  color: #E2E8F0;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}
.utility-wa {
  color: #25D366;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.form-fields-container {
  display: block;
}
.form-success-state {
  display: none;
  text-align: center;
  padding: 2.5rem 1.5rem;
}
.form-success-state.active,
.form-success-state.show {
  display: block !important;
}
.client-name-display {
  font-weight: 700;
  color: var(--color-accent);
}
.wa-direct-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background-color: var(--color-whatsapp) !important;
  color: #FFFFFF !important;
  font-weight: 600;
  padding: 0.85rem 1.75rem;
  border-radius: var(--radius-sm);
  text-decoration: none;
  margin-top: 1rem;
}
'''
    with open('assets/css/style.css', 'a', encoding='utf-8') as f:
        f.write('\n' + helpers)

    with open('scripts/generate_master_style.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # insert before the closing triple quotes
    idx = content.rfind('"""')
    if idx != -1:
        new_content = content[:idx] + '\n' + helpers + content[idx:]
        with open('scripts/generate_master_style.py', 'w', encoding='utf-8') as f:
            f.write(new_content)
    print("Editorial helpers appended successfully!")

if __name__ == '__main__':
    append_editorial_helpers()
