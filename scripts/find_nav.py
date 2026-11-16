import re

with open('kd_dump.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find navbar container
nav_idx = html.find('Commercial Interior Designing')
if nav_idx != -1:
    print("=== NAV CONTEXT ===")
    start = max(0, nav_idx - 1500)
    end = min(len(html), nav_idx + 1500)
    print(html[start:end])
else:
    print("Could not find nav context")
