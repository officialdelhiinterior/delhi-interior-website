import os
import re

ICON_BLOCK = """  <!-- Favicons & App Icons -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">"""

# Regex to match existing favicon / manifest blocks
OLD_FAVICON_PATTERN = re.compile(
    r'(?:[ \t]*<!--\s*Favicons?\s*(?:& App Icons?)?\s*-->\s*)?'
    r'(?:[ \t]*<link rel="(?:icon|apple-touch-icon|manifest)"[^>]*>\s*)+',
    re.IGNORECASE
)

updated_count = 0

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'scripts' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if OLD_FAVICON_PATTERN.search(content):
                new_content = OLD_FAVICON_PATTERN.sub(ICON_BLOCK + '\n', content, count=1)
            else:
                # Insert before </head>
                new_content = content.replace('</head>', f'{ICON_BLOCK}\n</head>')

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_count += 1
                print(f'Updated: {filepath}')

print(f'Total HTML files updated with official favicon links: {updated_count}')
