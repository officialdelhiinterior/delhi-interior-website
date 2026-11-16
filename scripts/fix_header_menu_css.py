import os

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace the entire old Header navigation block with refined Livspace + KD header
old_nav_block = '''/* Modern Header / Navigation */
.site-header {
  position: fixed;
  top: 40px;
  left: 0;
  right: 0;
  height: 72px;
  background-color: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--color-border);
  z-index: 150;
  transition: all var(--trans-smooth);
}
.site-header.scrolled {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
}
.site-header .nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}

/* Livspace-style Brand Logo */
.site-logo {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--color-dark);
  display: inline-flex;
  align-items: center;
  gap: 0.2rem;
  letter-spacing: -0.03em;
}
.site-logo .logo-dot {
  color: var(--color-primary);
}



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
}'''

new_nav_block = '''/* ==========================================================================
   HEADER & NAVIGATION SYSTEM (Livspace Standard)
   ========================================================================== */

/* Main Header Bar */
.site-header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  height: 74px;
  background: #FFFFFF;
  border-bottom: 1px solid var(--color-border);
  z-index: 990;
  transition: all var(--trans-fast);
}

.site-header.scrolled {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.site-header .nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}

/* Brand Logo */
.site-logo {
  font-family: var(--font-display);
  font-size: 1.55rem;
  font-weight: 800;
  color: var(--color-dark);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  letter-spacing: -0.03em;
  flex-shrink: 0;
}

.site-logo .logo-dot {
  color: var(--color-primary);
  margin-left: 1px;
}

/* Main Navigation Menu */
.main-navigation {
  display: flex;
  align-items: center;
  height: 100%;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.85rem;
  list-style: none;
  margin: 0;
  padding: 0;
  height: 100%;
}

.nav-links li {
  display: flex;
  align-items: center;
  height: 100%;
  position: relative;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-links a {
  font-family: var(--font-main);
  font-size: 0.94rem;
  font-weight: 600;
  color: #1F2937;
  text-decoration: none;
  padding: 0.5rem 0.2rem;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  transition: color var(--trans-fast);
  white-space: nowrap;
  position: relative;
}

.nav-links a:hover,
.nav-links a:focus,
.nav-links a.active {
  color: var(--color-primary);
}

.nav-links a.active::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: var(--color-primary);
  border-radius: 99px;
}

/* Services Dropdown Item */
.nav-dropdown-item {
  position: relative;
  height: 100%;
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
  font-size: 0.62rem;
  color: #9CA3AF;
  transition: transform 200ms ease, color 200ms ease;
  display: inline-block;
}

.nav-dropdown-item:hover .dropdown-chevron,
.nav-dropdown-item:focus-within .dropdown-chevron,
.nav-dropdown-item.active .dropdown-chevron {
  transform: rotate(180deg);
  color: var(--color-primary);
}

/* Dropdown Mega Menu */
.nav-dropdown-menu {
  position: absolute;
  top: calc(100% - 2px);
  left: 50%;
  transform: translateX(-50%) translateY(8px);
  width: 560px;
  background: #FFFFFF;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.14), 0 0 1px 1px rgba(0, 0, 0, 0.05);
  padding: 0.85rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.4rem;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 180ms ease, transform 180ms ease, visibility 180ms ease;
  z-index: 1050;
}

/* Hover Bridge so cursor doesn't lose dropdown */
.nav-dropdown-menu::before {
  content: '';
  position: absolute;
  top: -12px;
  left: 0;
  right: 0;
  height: 12px;
}

.nav-dropdown-item:hover .nav-dropdown-menu,
.nav-dropdown-item:focus-within .nav-dropdown-menu,
.nav-dropdown-item.active .nav-dropdown-menu {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: translateX(-50%) translateY(0);
}'''

css = css.replace(old_nav_block, new_nav_block)

# 2. Remove duplicate snippet2 at bottom
duplicate_site_header = '''/* 2. Main Site Header (Sticky Tier) */
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
}'''

css = css.replace(duplicate_site_header, '/* 2. Main Site Header styled above */')

# 3. Fix hero-livspace padding-top
css = css.replace(
    'padding-top: calc(72px + 40px + 2.5rem);',
    'padding-top: 2.75rem;'
)

# 4. Fix mobile-menu-overlay z-index
css = css.replace(
    '.mobile-menu-overlay {\n  position: fixed;\n  inset: 0;\n  background-color: var(--color-white);\n  z-index: 300;',
    '.mobile-menu-overlay {\n  position: fixed;\n  inset: 0;\n  background-color: var(--color-white);\n  z-index: 2000;'
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Successfully updated assets/css/style.css with polished Header Menu styles!')
