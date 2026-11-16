import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add Dropdown & Refined Header Styles
dropdown_css = '''
/* Nav Links & Dropdown System */
.nav-links {
  display: flex;
  align-items: center;
  gap: 1.6rem;
  list-style: none;
}
.nav-links a {
  font-size: 0.92rem;
  font-weight: 600;
  color: #374151;
  position: relative;
  padding: 0.5rem 0;
  text-decoration: none;
  transition: color var(--trans-fast);
}
.nav-links a:hover,
.nav-links a.active {
  color: var(--color-primary);
}
.nav-links a.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background-color: var(--color-primary);
  border-radius: var(--radius-pill);
}

/* Services Dropdown in Header */
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
}
.dropdown-chevron {
  font-size: 0.72rem;
  color: #9CA3AF;
  transition: transform var(--trans-fast);
}
.nav-dropdown-item:hover .dropdown-chevron,
.nav-dropdown-item:focus-within .dropdown-chevron {
  transform: rotate(180deg);
  color: var(--color-primary);
}
.nav-dropdown-menu {
  position: absolute;
  top: calc(100% + 0.6rem);
  left: -1.5rem;
  width: 340px;
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: 0 16px 45px rgba(0, 0, 0, 0.12);
  padding: 0.8rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: opacity 220ms ease, transform 220ms ease, visibility 220ms ease;
  z-index: 250;
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
  gap: 0.85rem;
  padding: 0.65rem 0.85rem;
  border-radius: var(--radius-md);
  text-decoration: none;
  transition: background-color var(--trans-fast);
}
.dropdown-link:hover {
  background-color: #F9FAFB;
}
.dropdown-icon {
  font-size: 1.25rem;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-primary-light);
  border-radius: var(--radius-sm);
  flex-shrink: 0;
}
.dropdown-text strong {
  display: block;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-dark);
}
.dropdown-text span {
  display: block;
  font-size: 0.75rem;
  color: var(--color-muted);
  font-weight: 400;
}
.dropdown-link:hover .dropdown-text strong {
  color: var(--color-primary);
}

/* Mobile Menu Enhancements */
.mobile-menu-section-title {
  font-size: 0.75rem;
  font-weight: 800;
  color: var(--color-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 0.75rem;
}
.mobile-nav-services {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  margin-bottom: 1.5rem;
}
.mobile-nav-services a {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--color-dark);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}
.mobile-nav-links a {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--color-dark);
  text-decoration: none;
}
'''

# Replace old nav-links definition
old_nav_links_pattern = r'/\* Nav Links \*/[\s\S]*?\.nav-links a\.active::after\s*\{[^}]*\}'
if re.search(old_nav_links_pattern, css):
    css = re.sub(old_nav_links_pattern, dropdown_css, css)
else:
    css += '\n' + dropdown_css

# 2. Update Media Queries: Move nav hiding from 768px to 1080px
old_mq = '''@media (max-width: 768px) {
  .nav-links, .nav-phone {
    display: none;
  }
  .hamburger {
    display: flex;
  }'''

new_mq = '''@media (max-width: 1080px) {
  .nav-links, .nav-phone {
    display: none;
  }
  .hamburger {
    display: flex;
  }
}

@media (max-width: 768px) {'''

css = css.replace(old_mq, new_mq)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('[SUCCESS] style.css updated with Services Dropdown and 1080px responsive breakpoint.')
