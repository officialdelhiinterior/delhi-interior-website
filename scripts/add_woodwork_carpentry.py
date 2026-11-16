import re

print("=== 1. Updating scripts/build_kd_delhi_home.py ===")
with open('scripts/build_kd_delhi_home.py', 'r', encoding='utf-8') as f:
    home_code = f.read()

# 1. Update Services dropdown link in home generator
old_dropdown_furniture = '''              <a href="/bedroom-furniture-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 18v3"/><path d="M20 18v3"/><path d="M19 11v7H5v-7"/><path d="M19 11a3 3 0 0 0-3-3H8a3 3 0 0 0-3 3"/><path d="M3 14h18"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Study Desks &amp; Storage</strong>
                  <span>Workstations &amp; Teak Mandirs</span>
                </div>
              </a>'''

new_dropdown_woodwork = '''              <a href="/bedroom-furniture-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">
                  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                </span>
                <div class="dropdown-text">
                  <strong>Custom Woodwork &amp; Carpentry</strong>
                  <span>Teak Mandirs, Beds, Desks &amp; Millwork</span>
                </div>
              </a>'''

home_code = home_code.replace(old_dropdown_furniture, new_dropdown_woodwork)

# 2. Update Mobile menu in home generator
home_code = home_code.replace(
    '<li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">📚 Custom Furniture &amp; Study</a></li>',
    '<li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">🪵 Custom Woodwork &amp; Carpentry</a></li>'
)

# 3. Update Footer in home generator
home_code = home_code.replace(
    '<li><a href="/bedroom-furniture-delhi/">Study Desks &amp; Beds</a></li>',
    '<li><a href="/bedroom-furniture-delhi/">Woodwork &amp; Carpentry</a></li>'
)

# 4. Update Residential Specialization text
home_code = home_code.replace(
    'modular kitchens, custom sliding wardrobes, fluted wall paneling, false ceilings, and pooja mandirs crafted for urban Delhi living.',
    'modular kitchens, custom sliding wardrobes, bespoke woodwork &amp; precision carpentry, fluted wall paneling, and teakwood pooja mandirs crafted for urban Delhi living.'
)

# 5. Update 3x3 visual grid card 7
old_card_7 = '''          <!-- 7. Bespoke Furniture & Study -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-furniture.webp" type="image/webp">
                <img src="/assets/images/service-furniture.jpg" alt="Bespoke Furniture & Study Desks in Delhi NCR" width="800" height="500" loading="lazy">
              </picture>
            </div>
            <div class="service-visual-body">
              <span class="service-cat-tag">Carpentry &amp; Storage</span>
              <h3>Bespoke Furniture &amp; Study</h3>
              <p>Ergonomic work-from-home desks, hydraulic storage beds, upholstered headboards, and serene teakwood pooja mandirs.</p>
              <div class="service-visual-footer">
                <a href="/bedroom-furniture-delhi/" class="service-visual-link">Explore Designs →</a>
              </div>
            </div>
          </div>'''

new_card_7 = '''          <!-- 7. Custom Woodwork & Precision Carpentry -->
          <div class="service-visual-card">
            <div class="service-visual-img">
              <picture>
                <source srcset="/assets/images/service-furniture.webp" type="image/webp">
                <img src="/assets/images/service-furniture.jpg" alt="Custom Woodwork and Carpentry Services in Delhi NCR" width="800" height="500" loading="lazy">
              </picture>
            </div>
            <div class="service-visual-body">
              <span class="service-cat-tag">Master Carpentry</span>
              <h3>Custom Woodwork &amp; Carpentry</h3>
              <p>Handcrafted solid teakwood pooja mandirs, hydraulic storage beds, ergonomic study desks, crockery consoles, and architectural millwork.</p>
              <div class="service-visual-footer">
                <a href="/bedroom-furniture-delhi/" class="service-visual-link">Explore Woodwork →</a>
              </div>
            </div>
          </div>'''

home_code = home_code.replace(old_card_7, new_card_7)

# 6. Add "Woodwork & Mandirs" filter tab and card to Projects Gallery
old_tabs = '''        <div class="room-tabs-bar" role="tablist">
          <button class="room-tab-btn active" data-room-target="all">All Projects</button>
          <button class="room-tab-btn" data-room-target="kitchen">Modular Kitchens</button>
          <button class="room-tab-btn" data-room-target="bedroom">Master Bedrooms</button>
          <button class="room-tab-btn" data-room-target="living">Living &amp; Dining</button>
          <button class="room-tab-btn" data-room-target="wardrobe">Custom Wardrobes</button>
        </div>'''

new_tabs = '''        <div class="room-tabs-bar" role="tablist">
          <button class="room-tab-btn active" data-room-target="all">All Projects</button>
          <button class="room-tab-btn" data-room-target="kitchen">Modular Kitchens</button>
          <button class="room-tab-btn" data-room-target="bedroom">Master Bedrooms</button>
          <button class="room-tab-btn" data-room-target="living">Living &amp; Dining</button>
          <button class="room-tab-btn" data-room-target="wardrobe">Custom Wardrobes</button>
          <button class="room-tab-btn" data-room-target="woodwork">Woodwork &amp; Mandirs</button>
        </div>'''

home_code = home_code.replace(old_tabs, new_tabs)

# Add a dedicated Woodwork & Mandir project card into the gallery
mandir_card = '''          <div class="room-card" data-room="woodwork">
            <div class="room-card-img">
              <picture>
                <source srcset="/assets/images/portfolio-mandir.webp" type="image/webp">
                <img src="/assets/images/portfolio-mandir.jpg" alt="Sacred Teakwood Mandir & Custom Woodwork in South Extension Delhi" width="800" height="600" loading="lazy">
              </picture>
              <span class="tag">South Extension II</span>
            </div>
            <div class="room-card-body">
              <h3>Bespoke Teakwood Mandir &amp; Jali</h3>
              <p>Solid Burma Teak with intricate backlit CNC jaali, brass temple bells, and concealed samagri storage.</p>
              <div class="room-card-footer">
                <div class="price-chip">Delivered in <strong>21 Days</strong></div>
                <a href="/bedroom-furniture-delhi/" class="btn btn-outline" style="padding: 0.4rem 0.9rem; font-size: 0.8rem;">View Woodwork Details</a>
              </div>
            </div>
          </div>
'''

if 'data-room="woodwork"' not in home_code:
    home_code = home_code.replace(
        '<div class="room-cards-grid">\n',
        '<div class="room-cards-grid">\n' + mandir_card
    )

with open('scripts/build_kd_delhi_home.py', 'w', encoding='utf-8') as f:
    f.write(home_code)
print("Updated scripts/build_kd_delhi_home.py")


print("=== 2. Updating scripts/build_main_and_utility.py ===")
with open('scripts/build_main_and_utility.py', 'r', encoding='utf-8') as f:
    main_code = f.read()

main_code = main_code.replace(old_dropdown_furniture, new_dropdown_woodwork)
main_code = main_code.replace(
    '<li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">📚 Custom Furniture &amp; Study</a></li>',
    '<li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">🪵 Custom Woodwork &amp; Carpentry</a></li>'
)
main_code = main_code.replace(
    '<li><a href="/bedroom-furniture-delhi/">Study Desks &amp; Beds</a></li>',
    '<li><a href="/bedroom-furniture-delhi/">Woodwork &amp; Carpentry</a></li>'
)

with open('scripts/build_main_and_utility.py', 'w', encoding='utf-8') as f:
    f.write(main_code)
print("Updated scripts/build_main_and_utility.py")


print("=== 3. Updating scripts/update_build_services.py ===")
with open('scripts/update_build_services.py', 'r', encoding='utf-8') as f:
    serv_code = f.read()

serv_code = serv_code.replace(old_dropdown_furniture, new_dropdown_woodwork)
serv_code = serv_code.replace(
    '<li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">📚 Custom Furniture &amp; Study</a></li>',
    '<li><a href="/bedroom-furniture-delhi/" onclick="closeMobileMenu()">🪵 Custom Woodwork &amp; Carpentry</a></li>'
)
serv_code = serv_code.replace(
    '<li><a href="/bedroom-furniture-delhi/">Study Desks &amp; Beds</a></li>',
    '<li><a href="/bedroom-furniture-delhi/">Woodwork &amp; Carpentry</a></li>'
)

with open('scripts/update_build_services.py', 'w', encoding='utf-8') as f:
    f.write(serv_code)
print("Updated scripts/update_build_services.py")


print("=== 4. Updating scripts/build_services.py with rich Woodwork & Carpentry data ===")
with open('scripts/build_services.py', 'r', encoding='utf-8') as f:
    bs_code = f.read()

bs_code = bs_code.replace(old_dropdown_furniture, new_dropdown_woodwork)
bs_code = bs_code.replace(
    '<li><a href="/bedroom-furniture-delhi/">Study &amp; Furniture</a></li>',
    '<li><a href="/bedroom-furniture-delhi/">Woodwork &amp; Carpentry</a></li>'
)

# Update the data dictionary for bedroom-furniture-delhi
old_bf_dict = """        'slug': 'bedroom-furniture-delhi',
        'title': 'Bedroom Furniture & Study in Delhi | Custom Desks | Delhi Interior',
        'desc': 'Custom bedroom furniture & study tables in Delhi. Hydraulic storage beds, ergonomic desks, bookshelves, shoe racks. 5-yr warranty. Free site quote.',
        'h1': 'Bedroom Furniture & Custom Study in Delhi',
        'sub': 'Custom hydraulic storage beds, ergonomic work-from-home study desks, pooja mandirs, and bespoke storage built to your exact measurements.',
        'hero_img': '/assets/images/service-furniture.webp',
        'alt': 'Custom bedroom furniture by Delhi Interior in Delhi',
        'overview_h2': 'Ergonomic Craftsmanship. Built for Everyday Comfort.',
        'overview_p1': 'Ready-made furniture rarely fits the awkward alcoves or room proportions of Delhi apartments. Gaps of 4 inches waste precious space while cheap particle board sags under book weights. Delhi Interior creates built-in, bespoke furniture crafted from sturdy HDMR and plywood.',
        'overview_p2': 'Whether you need a heavy-duty hydraulic bed with easy under-mattress storage, an L-shaped study desk with integrated cable raceways, or a serene wooden pooja mandir with CNC lattice screens, we build each piece to last for generations.',
        'checklist': [
            'Hydraulic Lift Storage Beds with German Gas Springs',
            'Drawer Storage Platform Beds with Reinforced Frames',
            'Custom Cushioned & Fluted Headboards in Leatherette/Velvet',
            'L-Shaped & Floating Study Tables with Cable Grommets',
            'Heavy-Duty Bookshelves with Non-Sagging 25mm Shelves',
            'Custom Crockery Units with Toughened Glass Display',
            'Concealed Ventilated Shoe Racks (Holds 40+ Pairs)',
            'Floating Bedside Consoles with Wireless Charger Insets',
            'Custom Teakwood & Corian Pooja Mandirs with CNC Jali',
            'Bar Cabinets with Wine Glass Stemware Racks'
        ],"""

new_bf_dict = """        'slug': 'bedroom-furniture-delhi',
        'title': 'Custom Woodwork & Carpentry in Delhi | Teak Mandirs & Furniture | Delhi Interior',
        'desc': 'Master custom woodwork & precision carpentry in Delhi NCR. Handcrafted teak mandirs, hydraulic storage beds, study desks, architectural millwork. 10-yr warranty.',
        'h1': 'Custom Woodwork & Precision Carpentry in Delhi',
        'sub': 'Handcrafted solid teakwood pooja mandirs, hydraulic storage beds, ergonomic study desks, and bespoke architectural millwork built by in-house master carpenters.',
        'hero_img': '/assets/images/service-furniture.webp',
        'alt': 'Custom woodwork and master carpentry services in Delhi NCR by Delhi Interior',
        'overview_h2': 'Master Carpentry. Millimeter Precision. Built to Outlast Generations.',
        'overview_p1': 'Standard showroom furniture rarely fits the specific alcoves and room dimensions of Delhi homes, leaving awkward dead zones and built with weak particleboard that sags. At Delhi Interior, our 40+ in-house master carpenters (karigars) operate from our dedicated 10,000 sq. ft. precision facility, crafting bespoke woodwork from calibrated Boiling Water Proof (BWP) 710 marine ply, high-density HDMR, and seasoned Burma Teak.',
        'overview_p2': 'From sacred teakwood pooja mandirs with illuminated CNC jali screens to effortless hydraulic platform beds, custom home office workstations, and bespoke dining consoles, every joint and surface is hand-finished with cabinet-maker perfection.',
        'checklist': [
            'Handcrafted Solid Teakwood & Sheesham Temple Mandirs',
            'Hydraulic Gas-Lift Platform Storage Beds with German Struts',
            'Heavy-Duty 25mm Calibrated Marine Ply Bookshelves (Zero Sag)',
            'Ergonomic L-Shaped Study Workstations with Pop-up Power Docks',
            'Custom Dining Credenzas, Bar Cabinets & Fluted Crockery Units',
            'Concealed Louvered Shoe Consoles with Odor Ventilation',
            'Precision CNC Backlit Jali Screens & Brass Inlay Details',
            'German Soft-Close Tandem Hardware (Blum & Hettich)',
            'Hand-Rubbed Natural Teak Grain PU & Italian Acrylic Polish',
            'Dust-Free Factory Sizing & On-Site Alignment by Master Carpenters'
        ],"""

bs_code = bs_code.replace(old_bf_dict, new_bf_dict)

with open('scripts/build_services.py', 'w', encoding='utf-8') as f:
    f.write(bs_code)
print("Updated scripts/build_services.py")
