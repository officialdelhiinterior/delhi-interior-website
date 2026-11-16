import os, re

print("=== 1. Updating assets/css/style.css ===")
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add brand logo styling
logo_css = '''/* Brand Logo Image */
.site-logo {
  display: inline-flex;
  align-items: center;
  text-decoration: none;
  flex-shrink: 0;
}
.brand-logo-img {
  height: 48px;
  width: auto;
  max-width: 175px;
  object-fit: contain;
  display: block;
}
'''

if '.brand-logo-img' not in css:
    css = css.replace('.site-logo {', logo_css + '\n.site-logo {', 1)

# Add Floating Call Button CSS
floating_call_css = '''
/* Floating Call Button */
.call-float {
  position: fixed;
  bottom: 24px;
  left: 24px;
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background-color: #2563EB;
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(37, 99, 235, 0.4);
  z-index: 998;
  transition: transform var(--trans-fast), box-shadow var(--trans-fast);
  text-decoration: none;
}
.call-float:hover {
  transform: scale(1.08) translateY(-2px);
  box-shadow: 0 8px 24px rgba(37, 99, 235, 0.55);
}
.call-float svg {
  width: 24px;
  height: 24px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
}
.call-tooltip {
  position: absolute;
  left: calc(100% + 12px);
  background-color: #0F172A;
  color: #FFFFFF;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  font-size: 0.82rem;
  font-weight: 600;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--trans-fast);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
.call-float:hover .call-tooltip {
  opacity: 1;
}

@media (max-width: 768px) {
  .call-float {
    display: none;
  }
}
'''

if '.call-float' not in css:
    css += floating_call_css

# Ensure hero section padding is clean
css = css.replace('padding-top: 2.75rem;', 'padding-top: 2.5rem;')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated assets/css/style.css")


print("=== 2. Updating scripts/audit_site.py ===")
with open('scripts/audit_site.py', 'r', encoding='utf-8') as f:
    audit_code = f.read()

audit_code = audit_code.replace('919811000000', '919643817099')

with open('scripts/audit_site.py', 'w', encoding='utf-8') as f:
    f.write(audit_code)
print("Updated scripts/audit_site.py")
