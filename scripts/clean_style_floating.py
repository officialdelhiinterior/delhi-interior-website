import re

def clean_style_css():
    with open('assets/css/style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the appended block at the bottom if present
    appended_marker = '/* ==========================================================================\n   14. FLOATING ACTION BUTTONS (CALL ABOVE WHATSAPP)'
    if appended_marker in content:
        idx = content.find(appended_marker)
        content = content[:idx].rstrip() + '\n'

    # Now replace Section 23 FLOATING ACTION CONTROLS block
    sec23_target = '''/* --------------------------------------------------------------------------
   23. FLOATING ACTION CONTROLS & MOBILE STICKY BAR
   -------------------------------------------------------------------------- */'''
    
    new_sec23 = '''/* --------------------------------------------------------------------------
   23. FLOATING ACTION CONTROLS (CALL ABOVE WHATSAPP) & MOBILE STICKY BAR
   -------------------------------------------------------------------------- */
.floating-actions-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
  z-index: 995;
}

.call-float,
.whatsapp-float {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  position: relative;
  transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.25s ease, background-color 0.2s ease;
}

/* Call Button (Top / Above WhatsApp) */
.call-float {
  background-color: var(--color-primary);
  color: #FFFFFF;
  border: 1px solid rgba(184, 144, 88, 0.4);
  box-shadow: 0 4px 16px rgba(11, 37, 64, 0.4);
}
.call-float:hover {
  background-color: var(--color-primary-hover);
  transform: translateY(-2px) scale(1.06);
  box-shadow: 0 8px 24px rgba(11, 37, 64, 0.55);
}
.call-float svg {
  width: 22px;
  height: 22px;
  fill: #FFFFFF;
  transition: transform 0.2s ease;
}
.call-float:hover svg {
  transform: rotate(12deg);
}

/* WhatsApp Button (Bottom / Below Call) */
.whatsapp-float {
  background-color: #25D366;
  color: #FFFFFF;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
}
.whatsapp-float:hover {
  background-color: #20BD5A;
  transform: translateY(-2px) scale(1.06);
  box-shadow: 0 8px 24px rgba(37, 211, 102, 0.55);
}
.whatsapp-float svg {
  width: 26px;
  height: 26px;
  fill: #FFFFFF;
}

/* Tooltip Labels */
.call-tooltip,
.whatsapp-tooltip {
  position: absolute;
  right: 64px;
  top: 50%;
  transform: translateY(-50%);
  background-color: #060E18;
  color: #FFFFFF;
  font-size: 0.78rem;
  font-weight: 600;
  white-space: nowrap;
  padding: 6px 12px;
  border-radius: 6px;
  border: 1px solid rgba(184, 144, 88, 0.3);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
  pointer-events: none;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s ease, visibility 0.2s ease, transform 0.2s ease;
}

.call-float:hover .call-tooltip,
.whatsapp-float:hover .whatsapp-tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(-4px);
}

/* Standalone fallbacks (in case not wrapped) */
body > a.whatsapp-float:not(.floating-actions-container a) {
  position: fixed;
  right: 24px;
  bottom: 24px;
  z-index: 995;
}
body > a.call-float:not(.floating-actions-container a) {
  position: fixed;
  right: 24px;
  bottom: 86px;
  left: auto;
  z-index: 995;
}'''

    # Pattern from sec23 start to .sticky-mobile-cta
    pattern = r'/\* --------------------------------------------------------------------------\s*23\. FLOATING ACTION CONTROLS.*?/\* Mobile Sticky Bottom CTA \*/'
    
    replacement = new_sec23 + '\n\n/* Mobile Sticky Bottom CTA */'
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        print("Replaced Section 23 cleanly!")
    else:
        print("Warning: Section 23 pattern not matched")

    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("style.css cleaned and rewritten successfully!")

if __name__ == '__main__':
    clean_style_css()
