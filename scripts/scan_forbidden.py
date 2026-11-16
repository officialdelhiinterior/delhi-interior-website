import glob

files = glob.glob('**/*.html', recursive=True)
terms = ['warranty', 'guarantee', '45 day', '45-day', '42 day', '42-day', 'starting from', 'from ₹']

found = {}
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read().lower()
    for t in terms:
        if t in c:
            if f not in found:
                found[f] = []
            found[f].append(t)

for f, matches in found.items():
    print(f'{f}: {matches}')
