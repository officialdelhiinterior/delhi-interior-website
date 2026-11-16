import glob, re

for f in glob.glob('**/*.html', recursive=True):
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    buttons = re.findall(r'<(?:button|a)[^>]*class=["\'][^"\']*\bbtn\b[^"\']*["\'][^>]*>(.*?)</(?:button|a)>', html, re.DOTALL)
    for b in buttons:
        clean = re.sub(r'<[^>]+>', '', b).strip()
        if '→' in clean or '->' in clean or '&rarr;' in clean:
            print(f, clean.encode('ascii', 'replace').decode('ascii'))
