import re

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dropdown link fix
    old_comm_dropdown = '''<a href="/commercial-interior-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">🏢</span>
                <div class="dropdown-text">
                  <strong>Commercial Interiors</strong>
                  <span>Offices, Retail &amp; Clinics</span>
                </div>
              </a>
              <a href="/plumbing-electrical-delhi/" class="dropdown-link" role="menuitem" style="grid-column: span 2;">
                <span class="dropdown-icon">🎨</span>
                <div class="dropdown-text">
                  <strong>MEP, Civil &amp; Luxury Finishes</strong>
                  <span>Concealed Plumbing, Electrical, Asian Paints Royale &amp; PU Polish</span>
                </div>
              </a>'''

    new_comm_dropdown = '''<a href="/painting-polishing-delhi/" class="dropdown-link" role="menuitem">
                <span class="dropdown-icon">🎨</span>
                <div class="dropdown-text">
                  <strong>Painting &amp; PU Polish</strong>
                  <span>Asian Paints Royale, PU &amp; Duco</span>
                </div>
              </a>
              <a href="/plumbing-electrical-delhi/" class="dropdown-link" role="menuitem" style="grid-column: span 2;">
                <span class="dropdown-icon">⚡</span>
                <div class="dropdown-text">
                  <strong>Plumbing &amp; Electrical MEP</strong>
                  <span>Concealed Piping, 4mm Fire-Proof Wiring &amp; Sanitaryware</span>
                </div>
              </a>'''

    content = content.replace(old_comm_dropdown, new_comm_dropdown)

    # Mobile menu fix
    old_comm_mobile = '''<li><a href="/commercial-interior-delhi/" onclick="closeMobileMenu()">🏢 Commercial Interiors</a></li>
        <li><a href="/plumbing-electrical-delhi/" onclick="closeMobileMenu()">🎨 MEP, Civil &amp; Paints</a></li>'''

    new_comm_mobile = '''<li><a href="/painting-polishing-delhi/" onclick="closeMobileMenu()">🎨 Painting &amp; PU Polish</a></li>
        <li><a href="/plumbing-electrical-delhi/" onclick="closeMobileMenu()">⚡ Plumbing &amp; Electrical MEP</a></li>'''

    content = content.replace(old_comm_mobile, new_comm_mobile)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'[FIXED] {path}')

for file_path in ['scripts/build_home.py', 'scripts/build_main_and_utility.py', 'scripts/update_build_services.py']:
    fix_file(file_path)
