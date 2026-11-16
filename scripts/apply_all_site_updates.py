"""
Apply all site updates:
1. Update scripts/build_main_and_utility.py:
   - Add floating call button, floating whatsapp, and mobile CTA to get_footer()
   - Add logo to thank_you_html
   - Replace 'South Extension II' with 'Mohammadpur, South Delhi'
2. Update scripts/build_services.py:
   - Replace 'South Extension II' with 'Mohammadpur, South Delhi'
3. Update scripts/update_build_services.py:
   - Add floating call button, floating whatsapp, and mobile CTA before </body>
4. Update scripts/build_blog.py:
   - Replace '9811000000' with '9643817099'
5. Update scripts/update_build_blog.py:
   - Replace '9811000000' with '9643817099'
   - Replace 'Free 3D Consultation' with 'Free Design Consultation'
   - Replace '12+ years' with '10+ years'
"""

FLOATING_BUTTONS_HTML = '''  <!-- Floating Call Button (24/7) -->
  <a href="tel:+919643817099" class="call-float" aria-label="Call Delhi Interior">
    <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    <span class="call-tooltip">Call +91 96438 17099 (24/7)</span>
  </a>

  <!-- Floating WhatsApp (24/7) -->
  <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+book+a+free+interior+consultation." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.43.1-.12.19-.48.61-.59.73-.11.12-.22.14-.41.05-.19-.09-.8-.29-1.53-.94-.57-.51-.95-1.13-1.06-1.32-.11-.19-.01-.3.08-.39.09-.08.19-.22.29-.33.09-.11.12-.19.19-.31.06-.12.03-.24-.01-.33-.05-.09-.43-1.04-.6-1.42-.16-.38-.32-.33-.44-.33h-.37c-.13 0-.34.05-.52.24-.18.19-.69.67-.69 1.64s.71 1.9 1.01 2.3c.3.4 1.92 2.93 4.65 4.11.65.28 1.16.45 1.55.58.65.21 1.25.18 1.72.11.53-.08 1.62-.66 1.85-1.3.23-.64.23-1.19.16-1.3-.06-.11-.23-.18-.42-.27z"/></svg>
    <span class="whatsapp-tooltip">Chat on WhatsApp (24/7)</span>
  </a>

  <!-- Mobile Sticky Bottom CTA -->
  <aside class="sticky-mobile-cta" aria-label="Mobile quick actions">
    <div class="cta-btn-group">
      <a href="tel:+919643817099" class="cta-btn btn-call">Call Designer</a>
      <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+a+quote." class="cta-btn btn-wa" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
  </aside>
'''

# 1. Update scripts/build_main_and_utility.py
print("Updating scripts/build_main_and_utility.py...")
with open('scripts/build_main_and_utility.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Add floating buttons to get_footer if not present
old_footer_tail = '''    </div>
  </footer>

  <script defer src="/assets/js/main.js"></script>'''

new_footer_tail = f'''    </div>
  </footer>

{FLOATING_BUTTONS_HTML}
  <script defer src="/assets/js/main.js"></script>'''

if old_footer_tail in text:
    text = text.replace(old_footer_tail, new_footer_tail)
    print("  Added floating buttons to get_footer()")

# Add logo to thank_you_html
old_thank_you_body = '''<body style="background-color: #FAFAFA; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; align-items: center; text-align: center; padding: 2rem 1rem;">
  
  <div style="max-width: 620px; width: 100%; background: var(--color-white); border-radius: var(--radius-xl); border: 1px solid var(--color-border); padding: 3.5rem 2.5rem; box-shadow: var(--shadow-xl);">'''

new_thank_you_body = '''<body style="background-color: #FAFAFA; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; align-items: center; text-align: center; padding: 2rem 1rem;">
  
  <div style="max-width: 620px; width: 100%; background: var(--color-white); border-radius: var(--radius-xl); border: 1px solid var(--color-border); padding: 3.5rem 2.5rem; box-shadow: var(--shadow-xl);">
    <div style="margin-bottom: 2rem;">
      <a href="/" aria-label="Delhi Interior Home">
        <img src="/assets/images/logo.png" alt="Delhi Interior" width="168" height="52" class="brand-logo-img">
      </a>
    </div>'''

if old_thank_you_body in text:
    text = text.replace(old_thank_you_body, new_thank_you_body)
    print("  Added logo to thank_you_html")

# Replace South Extension II with Mohammadpur, South Delhi
text = text.replace("'South Extension II'", "'Mohammadpur, South Delhi'")

with open('scripts/build_main_and_utility.py', 'w', encoding='utf-8') as f:
    f.write(text)


# 2. Update scripts/build_services.py
print("Updating scripts/build_services.py...")
with open('scripts/build_services.py', 'r', encoding='utf-8') as f:
    serv_code = f.read()

serv_code = serv_code.replace("'South Extension II'", "'Mohammadpur, South Delhi'")
with open('scripts/build_services.py', 'w', encoding='utf-8') as f:
    f.write(serv_code)


# 3. Update scripts/update_build_services.py
print("Updating scripts/update_build_services.py...")
with open('scripts/update_build_services.py', 'r', encoding='utf-8') as f:
    up_serv = f.read()

old_serv_tail = '''  </footer>

<script defer src="/assets/js/main.js"></script>'''

new_serv_tail = f'''  </footer>

{FLOATING_BUTTONS_HTML}
<script defer src="/assets/js/main.js"></script>'''

if old_serv_tail in up_serv:
    up_serv = up_serv.replace(old_serv_tail, new_serv_tail)
    print("  Added floating buttons to update_build_services.py")

with open('scripts/update_build_services.py', 'w', encoding='utf-8') as f:
    f.write(up_serv)


# 4. Update scripts/build_blog.py
print("Updating scripts/build_blog.py...")
with open('scripts/build_blog.py', 'r', encoding='utf-8') as f:
    blog_code = f.read()

blog_code = blog_code.replace('9811000000', '9643817099')
with open('scripts/build_blog.py', 'w', encoding='utf-8') as f:
    f.write(blog_code)


# 5. Update scripts/update_build_blog.py
print("Updating scripts/update_build_blog.py...")
with open('scripts/update_build_blog.py', 'r', encoding='utf-8') as f:
    up_blog = f.read()

up_blog = up_blog.replace('9811000000', '9643817099')
up_blog = up_blog.replace('Free 3D Consultation', 'Free Design Consultation')
up_blog = up_blog.replace('12+ years of residential expertise', '10+ years of residential expertise')
up_blog = up_blog.replace('See your home in 3D before committing.', 'Consult with our senior designers before committing.')

with open('scripts/update_build_blog.py', 'w', encoding='utf-8') as f:
    f.write(up_blog)

print("All generator scripts updated successfully!")
