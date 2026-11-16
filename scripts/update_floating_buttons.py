import glob
import re

NEW_FLOATING_HTML = '''  <!-- Floating Contact Actions (Call above WhatsApp) -->
  <div class="floating-actions-container" aria-label="Direct studio contacts">
    <!-- Call Button (Above) -->
    <a href="tel:+919643817099" class="call-float" aria-label="Call Delhi Interior 24/7">
      <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">
        <path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
      </svg>
      <span class="call-tooltip">Call +91 96438 17099 (24/7)</span>
    </a>

    <!-- WhatsApp Button (Below Call Button) -->
    <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+consultation." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp 24/7">
      <svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor">
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
      </svg>
      <span class="whatsapp-tooltip">Chat on WhatsApp (24/7)</span>
    </a>
  </div>'''

# CSS definitions to update
CSS_FLOATING_SECTION = '''/* ==========================================================================
   14. FLOATING ACTION BUTTONS (CALL ABOVE WHATSAPP)
   ========================================================================== */
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

/* Standalone fallbacks */
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

def update_html_files():
    # Matches the old call-float and whatsapp-float blocks
    pattern = r'(\s*<!-- Floating Call Button.*?<!-- Mobile Sticky Bottom CTA -->)'
    # Or specifically replace from call-float up to sticky-mobile-cta
    specific_pattern = r'(\s*<!-- Floating Call Button.*?</aside>)'

    for html_file in glob.glob('**/*.html', recursive=True):
        if 'k2_raw' in html_file:
            continue
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find where call-float and whatsapp-float are
        call_idx = content.find('call-float')
        if call_idx != -1:
            # Find the start comment before call-float
            comment_start = content.rfind('<!--', 0, call_idx)
            # Find sticky-mobile-cta
            sticky_idx = content.find('<!-- Mobile Sticky Bottom CTA -->', call_idx)
            if sticky_idx != -1 and comment_start != -1:
                old_block = content[comment_start:sticky_idx]
                new_block = NEW_FLOATING_HTML + '\n\n  '
                content = content[:comment_start] + new_block + content[sticky_idx:]
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated HTML: {html_file}")
            else:
                print(f"Warning: indices not found in {html_file}")

def update_css():
    # Update style.css
    with open('assets/css/style.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # Replace section 14
    sec14_pattern = r'/\* ==========================================================================\s*14\. FLOATING ACTION BUTTONS.*?(?=/\* ==========================================================================|$)'
    if re.search(sec14_pattern, css, flags=re.DOTALL):
        css = re.sub(sec14_pattern, CSS_FLOATING_SECTION + '\n\n', css, flags=re.DOTALL)
        print("Updated Section 14 in style.css")
    else:
        # Append or replace call-float block
        print("Replacing call-float and whatsapp-float directly in style.css")
        css += '\n\n' + CSS_FLOATING_SECTION

    # Also update mobile responsive styles for floating buttons
    mobile_pattern = r'(\.call-float,\s*\.whatsapp-float\s*\{\s*bottom:\s*74px;\s*\})'
    replacement_mobile = '''.floating-actions-container {
    bottom: 74px;
    right: 16px;
    gap: 10px;
  }
  body > a.whatsapp-float:not(.floating-actions-container a) {
    bottom: 74px;
    right: 16px;
  }
  body > a.call-float:not(.floating-actions-container a) {
    bottom: 136px;
    right: 16px;
    left: auto;
  }
  .call-float, .whatsapp-float {
    width: 48px;
    height: 48px;
  }
  .call-float svg {
    width: 20px;
    height: 20px;
  }
  .whatsapp-float svg {
    width: 24px;
    height: 24px;
  }
  .call-tooltip, .whatsapp-tooltip {
    display: none;
  }'''

    if re.search(mobile_pattern, css):
        css = re.sub(mobile_pattern, replacement_mobile, css)
        print("Updated mobile styles in style.css")

    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)

def update_generator_scripts():
    for script_file in [
        'scripts/rebuild_complete_site_v3.py',
        'scripts/build_main_and_utility.py',
        'scripts/generate_master_style.py'
    ]:
        try:
            with open(script_file, 'r', encoding='utf-8') as f:
                c = f.read()
            # In python scripts, update if found
            call_idx = c.find('call-float')
            if call_idx != -1 and '<!-- Floating Call Button' in c:
                comment_start = c.rfind('<!--', 0, call_idx)
                sticky_idx = c.find('<!-- Mobile Sticky Bottom CTA -->', call_idx)
                if sticky_idx != -1 and comment_start != -1:
                    c = c[:comment_start] + NEW_FLOATING_HTML + '\n\n  ' + c[sticky_idx:]
                    with open(script_file, 'w', encoding='utf-8') as f:
                        f.write(c)
                    print(f"Updated generator script: {script_file}")
        except Exception as e:
            print(f"Error updating {script_file}: {e}")

if __name__ == '__main__':
    update_html_files()
    update_css()
    update_generator_scripts()
    print("All floating button updates applied successfully!")
