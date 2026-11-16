import os
import re

# 1. Update index.html to add Card 10
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

card_10 = """          <!-- 10. Aluminium & Glass Work -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-glass.webp" type="image/webp">
                <img src="/assets/images/service-glass.jpg" alt="Aluminium and Glass Work in Delhi NCR" width="600" height="375" loading="lazy">
              </picture>
              <span class="service-visual-tag">6063-T6 Aluminium &amp; AIS Glass</span>
            </div>
            <div class="service-visual-body">
              <h3>Aluminium &amp; Glass Work</h3>
              <p>Slim profile architectural aluminium partitions, acoustic double-glazed enclosures, frameless shower cubicles, and designer fluted glass systems.</p>
              <div class="service-visual-pills">
                <span class="service-visual-pill">Slim Partitions</span>
                <span class="service-visual-pill">Acoustic Glazing</span>
                <span class="service-visual-pill">Shower Enclosures</span>
              </div>
              <div class="service-visual-footer">
                <span class="service-visual-badge">✦ Toughened Safety Glass</span>
                <a href="/aluminium-glass-work-delhi/" class="service-visual-link">Explore Systems →</a>
              </div>
            </div>
          </div>"""

if '/aluminium-glass-work-delhi/' not in index_html:
    # Target right before line 917: </div>\n        </div>\n      </div>\n    </section>\n\n    <!-- 6.5 AN INTERIOR SOLUTION FOR EVERY BRIEF
    target = '          <!-- 9. Plumbing & Electrical MEP -->'
    idx = index_html.find('<!-- 9. Plumbing & Electrical MEP -->')
    if idx != -1:
        # Find closing </div> of card 9
        closing_card9 = index_html.find('</div>\n          </div>', idx)
        if closing_card9 != -1:
            end_card9 = closing_card9 + len('</div>\n          </div>')
            index_html = index_html[:end_card9] + '\n\n' + card_10 + index_html[end_card9:]
            print("Added Card 10 to index.html services grid")

# 2. Update navigation dropdown and footer across all HTML files
dropdown_snippet = """              <a href="/aluminium-glass-work-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="1"/><line x1="12" y1="3" x2="12" y2="21"/><line x1="3" y1="12" x2="21" y2="12"/><circle cx="7.5" cy="7.5" r="1.5"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Aluminium &amp; Glass Work</strong>
                  <span>Slim Partitions, Railings &amp; Glazing</span>
                </div>
              </a>"""

footer_link = '            <li><a href="/aluminium-glass-work-delhi/">Aluminium &amp; Glass Work</a></li>'

updated_files = 0

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'scripts' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as fp:
                c = fp.read()
            
            orig = c
            
            # Remove span 2 from plumbing-electrical in dropdown so 10 items align in 2 equal columns of 5
            c = c.replace(
                '<a href="/plumbing-electrical-delhi/" class="dropdown-link" role="menuitem" style="grid-column: span 2;">',
                '<a href="/plumbing-electrical-delhi/" class="dropdown-link" role="menuitem">'
            )
            c = c.replace(
                '<a href="/plumbing-electrical-delhi/" class="dropdown-link active" role="menuitem" style="grid-column: span 2;">',
                '<a href="/plumbing-electrical-delhi/" class="dropdown-link active" role="menuitem">'
            )
            
            # Add to dropdown if missing
            if '/aluminium-glass-work-delhi/' not in c:
                # Insert after plumbing-electrical in dropdown
                marker = '/plumbing-electrical-delhi/" class="dropdown-link'
                marker_idx = c.find(marker)
                if marker_idx != -1:
                    # Find closing </a> for plumbing
                    end_a = c.find('</a>', marker_idx)
                    if end_a != -1:
                        end_a += 4
                        c = c[:end_a] + '\n' + dropdown_snippet + c[end_a:]
            
            # Add to footer if missing
            if '/aluminium-glass-work-delhi/' not in c:
                footer_marker = '<li><a href="/doors-partitions-delhi/">Doors &amp; Architectural Partitions</a></li>'
                if footer_marker in c:
                    c = c.replace(footer_marker, footer_marker + '\n' + footer_link)
                else:
                    alt_marker = '<li><a href="/false-ceiling-delhi/">False Ceilings &amp; Lighting</a></li>'
                    if alt_marker in c:
                        c = c.replace(alt_marker, alt_marker + '\n' + footer_link)
            else:
                # If it's already in the dropdown but not in the footer
                if footer_link not in c:
                    footer_marker = '<li><a href="/doors-partitions-delhi/">Doors &amp; Architectural Partitions</a></li>'
                    if footer_marker in c:
                        c = c.replace(footer_marker, footer_marker + '\n' + footer_link)
                    else:
                        alt_marker = '<li><a href="/false-ceiling-delhi/">False Ceilings &amp; Lighting</a></li>'
                        if alt_marker in c:
                            c = c.replace(alt_marker, alt_marker + '\n' + footer_link)

            if c != orig:
                with open(filepath, 'w', encoding='utf-8') as fp:
                    fp.write(c)
                updated_files += 1
                print(f"Updated navigation & footer in: {filepath}")

# 3. Update sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap_xml = f.read()

sitemap_entry = """  <url>
    <loc>https://delhiinterior.com/aluminium-glass-work-delhi/</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>"""

if '/aluminium-glass-work-delhi/' not in sitemap_xml:
    doors_entry = '<loc>https://delhiinterior.com/doors-partitions-delhi/</loc>'
    doors_idx = sitemap_xml.find(doors_entry)
    if doors_idx != -1:
        # Find closing </url>
        end_url = sitemap_xml.find('</url>', doors_idx)
        if end_url != -1:
            end_url += 6
            sitemap_xml = sitemap_xml[:end_url] + '\n' + sitemap_entry + sitemap_xml[end_url:]
            with open('sitemap.xml', 'w', encoding='utf-8') as f:
                f.write(sitemap_xml)
            print("Added aluminium-glass-work-delhi to sitemap.xml")

# 4. Update sitemap/index.html
with open('sitemap/index.html', 'r', encoding='utf-8') as f:
    sitemap_html = f.read()

if '/aluminium-glass-work-delhi/' not in sitemap_html:
    doors_link = '<li><a href="/doors-partitions-delhi/">'
    doors_idx = sitemap_html.find(doors_link)
    if doors_idx != -1:
        end_li = sitemap_html.find('</li>', doors_idx)
        if end_li != -1:
            end_li += 5
            new_item = '\n            <li><a href="/aluminium-glass-work-delhi/">Aluminium &amp; Glass Work</a> — Slim partitions, acoustic glazing &amp; shower cubicles</li>'
            sitemap_html = sitemap_html[:end_li] + new_item + sitemap_html[end_li:]
            with open('sitemap/index.html', 'w', encoding='utf-8') as f:
                f.write(sitemap_html)
            print("Added aluminium-glass-work-delhi to sitemap/index.html")

print(f"Script complete! Total HTML files updated: {updated_files}")
