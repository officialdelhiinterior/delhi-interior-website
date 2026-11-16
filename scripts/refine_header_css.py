import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Refined Dropdown & Hero Enhancements
refined_styles = '''
/* --- REFINED DROPDOWN NAVIGATION --- */
.nav-dropdown-item {
  position: relative;
  display: flex;
  align-items: center;
}
.nav-dropdown-trigger {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  cursor: pointer;
  text-decoration: none;
}
.dropdown-chevron {
  font-size: 0.65rem;
  color: #9CA3AF;
  transition: transform 200ms ease, color 200ms ease;
}
.nav-dropdown-item:hover .dropdown-chevron,
.nav-dropdown-item:focus-within .dropdown-chevron {
  transform: rotate(180deg);
  color: var(--color-primary);
}
.nav-dropdown-menu {
  position: absolute;
  top: calc(100% + 0.6rem);
  left: -2rem;
  width: 520px;
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12), 0 4px 12px rgba(0, 0, 0, 0.05);
  padding: 0.85rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.35rem;
  opacity: 0;
  visibility: hidden;
  transform: translateY(10px);
  transition: opacity 200ms ease, transform 200ms ease, visibility 200ms ease;
  z-index: 500;
}
/* Invisible hover bridge */
.nav-dropdown-menu::before {
  content: '';
  position: absolute;
  top: -16px;
  left: 0;
  right: 0;
  height: 16px;
}
.nav-dropdown-item:hover .nav-dropdown-menu,
.nav-dropdown-item:focus-within .nav-dropdown-menu {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
.dropdown-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.6rem 0.75rem;
  border-radius: var(--radius-md);
  text-decoration: none;
  background: transparent;
  transition: background-color 150ms ease;
}
.dropdown-link:hover {
  background-color: #F8F9FA;
}
.dropdown-icon {
  font-size: 1.25rem;
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-primary-light);
  border-radius: var(--radius-sm);
  flex-shrink: 0;
}
.dropdown-text {
  display: flex;
  flex-direction: column;
}
.dropdown-text strong {
  display: block;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-dark);
  line-height: 1.2;
}
.dropdown-text span {
  display: block;
  font-size: 0.74rem;
  color: var(--color-muted);
  font-weight: 400;
  line-height: 1.3;
}
.dropdown-link:hover .dropdown-text strong {
  color: var(--color-primary);
}

/* --- HERO STATS ROW & BALANCED RIGHT CARD --- */
.hero-stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.2rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--color-border);
}
.hero-stat-box h4 {
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--color-dark);
  margin-bottom: 0.15rem;
  line-height: 1.1;
}
.hero-stat-box h4 span {
  color: var(--color-primary);
}
.hero-stat-box p {
  font-size: 0.78rem;
  color: var(--color-muted);
  font-weight: 500;
  line-height: 1.3;
  margin: 0;
}
.hero-card-trust {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  font-size: 0.76rem;
  color: var(--color-muted);
  margin-top: 0.85rem;
  text-align: center;
}
.hero-recent-preview {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  margin-top: 1.25rem;
  padding: 0.75rem 0.9rem;
  background: #F9FAFB;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
}
.recent-thumb {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-sm);
  object-fit: cover;
  flex-shrink: 0;
}
.recent-info {
  display: flex;
  flex-direction: column;
}
.recent-title {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--color-dark);
}
.recent-desc {
  font-size: 0.74rem;
  color: var(--color-muted);
}
'''

# Replace previous dropdown block if present
dropdown_pattern = r'/\* Nav Links & Dropdown System \*/[\s\S]*?\.dropdown-link:hover \.dropdown-text strong\s*\{[^}]*\}'
if re.search(dropdown_pattern, css):
    css = re.sub(dropdown_pattern, refined_styles, css)
else:
    css += '\n' + refined_styles

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('[SUCCESS] assets/css/style.css refined with wide 2-column dropdown and hero stats.')
