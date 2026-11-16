import re

print("=== 1. Updating scripts/build_kd_delhi_home.py ===")
with open('scripts/build_kd_delhi_home.py', 'r', encoding='utf-8') as f:
    home_code = f.read()

# Remove navbar link
home_code = home_code.replace('          <li><a href="/#estimator">Cost Calculator</a></li>\n', '')
# Remove mobile menu link
home_code = home_code.replace('        <li><a href="/#estimator" onclick="closeMobileMenu()">📊 Cost Calculator</a></li>\n', '')
# Remove footer link
home_code = home_code.replace('            <li><a href="/#estimator">Cost Calculator</a></li>\n', '')

# Remove Marquee Ticker section
marquee_pattern = r'\s*<!-- 6\. SERVICES SCROLLING MARQUEE TICKER \(Continuous Loop\) -->.*?</div>\s*</div>\s*(?=\s*<!-- 7\.)'
home_code = re.sub(marquee_pattern, '\n\n', home_code, flags=re.DOTALL)

# Remove Interactive Cost Calculator section
calc_pattern = r'\s*<!-- 9\. INTERACTIVE COST CALCULATOR \(LIVSPACE ESTIMATOR WIDGET\) -->.*?</section>\s*(?=\s*<!-- 10\.)'
home_code = re.sub(calc_pattern, '\n\n', home_code, flags=re.DOTALL)

# Remove Comparison Table section
comp_pattern = r'\s*<!-- 11\. WHY DELHI INTERIOR VS LOCAL CONTRACTORS \(COMPARISON TABLE\) -->.*?</section>\s*(?=\s*<!-- 12\.)'
home_code = re.sub(comp_pattern, '\n\n', home_code, flags=re.DOTALL)

# Remove Cookie banner
cookie_pattern = r'\s*<!-- Cookie Banner -->\s*<aside id="cookie-banner".*?</aside>\s*'
home_code = re.sub(cookie_pattern, '\n\n', home_code, flags=re.DOTALL)

with open('scripts/build_kd_delhi_home.py', 'w', encoding='utf-8') as f:
    f.write(home_code)
print("Updated scripts/build_kd_delhi_home.py")


print("=== 2. Updating scripts/build_main_and_utility.py ===")
with open('scripts/build_main_and_utility.py', 'r', encoding='utf-8') as f:
    main_code = f.read()

# Remove navbar link
main_code = main_code.replace('          <li><a href="/#estimator">Cost Calculator</a></li>\n', '')
# Remove mobile menu link
main_code = main_code.replace('        <li><a href="/#estimator" onclick="closeMobileMenu()">📊 Cost Calculator</a></li>\n', '')
# Remove footer link
main_code = main_code.replace('            <li><a href="/#estimator">Cost Calculator</a></li>\n', '')

# Remove Cookie banner
main_code = re.sub(cookie_pattern, '\n\n', main_code, flags=re.DOTALL)

with open('scripts/build_main_and_utility.py', 'w', encoding='utf-8') as f:
    f.write(main_code)
print("Updated scripts/build_main_and_utility.py")


print("=== 3. Updating scripts/update_build_services.py ===")
with open('scripts/update_build_services.py', 'r', encoding='utf-8') as f:
    serv_code = f.read()

serv_code = serv_code.replace('          <li><a href="/#estimator">Cost Calculator</a></li>\n', '')
serv_code = serv_code.replace('        <li><a href="/#estimator" onclick="closeMobileMenu()">📊 Cost Calculator</a></li>\n', '')
serv_code = serv_code.replace('            <li><a href="/#estimator">Cost Calculator</a></li>\n', '')
serv_code = re.sub(cookie_pattern, '\n\n', serv_code, flags=re.DOTALL)

with open('scripts/update_build_services.py', 'w', encoding='utf-8') as f:
    f.write(serv_code)
print("Updated scripts/update_build_services.py")


print("=== 4. Updating assets/js/main.js ===")
with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

# Remove initCostEstimator call in DOMContentLoaded
js_code = js_code.replace('    initCostEstimator();\n', '')
# Remove initCookieConsent call in DOMContentLoaded
js_code = js_code.replace('    initCookieConsent();\n', '')
# Remove initAnnouncementBar call
js_code = js_code.replace('    initAnnouncementBar();\n', '')

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_code)
print("Updated assets/js/main.js")
