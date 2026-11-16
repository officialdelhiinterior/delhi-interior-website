import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_section_6_5_html = """<!-- 6.5 AN INTERIOR SOLUTION FOR EVERY BRIEF (EXACT IMAGE 2 BLU BLOOM SPECIFICATION) -->
    <section class="brief-solutions-section">
      <div class="container">
        <div class="brief-solutions-header">
          <h2 class="brief-main-title">An interior solution for every<br>brief.</h2>
          <p class="brief-sub-title">
            Every property, material palette and scope is different. Choose a starting direction, then let our team prepare a project-specific BOQ and quotation.
          </p>
        </div>

        <div class="brief-tiers-container">
          <!-- 01 Ultra Luxury -->
          <div class="brief-tier-col" data-tier="Ultra Luxury">
            <span class="brief-tier-num">01</span>
            <h3 class="brief-tier-title">Ultra Luxury</h3>
            <p class="brief-tier-desc">Bespoke detailing and an elevated material palette.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 02 Luxury -->
          <div class="brief-tier-col" data-tier="Luxury">
            <span class="brief-tier-num">02</span>
            <h3 class="brief-tier-title">Luxury</h3>
            <p class="brief-tier-desc">Premium finishes with complete design and execution support.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 03 Minimalist -->
          <div class="brief-tier-col" data-tier="Minimalist">
            <span class="brief-tier-num">03</span>
            <h3 class="brief-tier-title">Minimalist</h3>
            <p class="brief-tier-desc">Calm, functional spaces with disciplined material choices.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 04 Essential -->
          <div class="brief-tier-col" data-tier="Essential">
            <span class="brief-tier-num">04</span>
            <h3 class="brief-tier-title">Essential</h3>
            <p class="brief-tier-desc">A focused interior scope built around everyday priorities.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>

          <!-- 05 Basic -->
          <div class="brief-tier-col" data-tier="Basic">
            <span class="brief-tier-num">05</span>
            <h3 class="brief-tier-title">Basic</h3>
            <p class="brief-tier-desc">Practical solutions for a clearly defined project scope.</p>
            <a href="#consultation-card" class="brief-tier-link" data-tier-select="Full Home 2BHK/3BHK/4BHK">
              Request details <span class="arrow-icon">↗</span>
            </a>
          </div>
        </div>
      </div>
    </section>"""

pattern = r'<!-- 6\.5 AN INTERIOR SOLUTION FOR EVERY BRIEF -->[\s\S]*?</section>'
updated, count = re.subn(pattern, new_section_6_5_html, text, count=1)
print('Replaced Section 6.5 count:', count)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated)
