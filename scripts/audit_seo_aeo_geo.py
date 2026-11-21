import glob, json, re

pages = glob.glob('**/*.html', recursive=True)
pages = [p for p in pages if 'scripts' not in p and 'google' not in p]

summary = []
for p in sorted(pages):
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    title_m = re.search(r'<title>(.*?)</title>', html)
    desc_m = re.search(r'<meta name="description" content="(.*?)">', html)
    og_image_m = re.search(r'<meta property="og:image" content="(.*?)">', html)
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)

    schema_types = []
    has_faq_schema = False
    has_breadcrumb_schema = False
    has_localbiz_schema = False

    for s in schemas:
        try:
            d = json.loads(s.strip())
            t = d.get('@type')
            if not t and '@graph' in d:
                t = f"@graph({len(d['@graph'])})"
                for item in d['@graph']:
                    it = item.get('@type')
                    types = it if isinstance(it, list) else [it]
                    if 'FAQPage' in types: has_faq_schema = True
                    if 'BreadcrumbList' in types: has_breadcrumb_schema = True
                    if any(x in ['HomeAndConstructionBusiness', 'LocalBusiness', 'InteriorDesignStudio'] for x in types):
                        has_localbiz_schema = True
            else:
                types = t if isinstance(t, list) else [t]
                if 'FAQPage' in types: has_faq_schema = True
                if 'BreadcrumbList' in types: has_breadcrumb_schema = True
                if any(x in ['HomeAndConstructionBusiness', 'LocalBusiness', 'InteriorDesignStudio'] for x in types):
                    has_localbiz_schema = True
            schema_types.append(str(t))
        except Exception as e:
            schema_types.append("ERR")

    summary.append({
        'path': p,
        'title': title_m.group(1) if title_m else 'MISSING',
        'desc_len': len(desc_m.group(1)) if desc_m else 0,
        'has_og_image': bool(og_image_m),
        'schemas': schema_types,
        'has_faq_schema': has_faq_schema,
        'has_breadcrumb_schema': has_breadcrumb_schema,
        'has_localbiz_schema': has_localbiz_schema
    })

print(f"{'Page':<40} | {'Schemas':<12} | {'FAQ?':<5} | {'Bread?':<6} | {'Biz?':<5} | {'OG-Img?':<7}")
print("-" * 85)
for s in summary:
    print(f"{s['path']:<40} | {','.join(s['schemas'])[:12]:<12} | {str(s['has_faq_schema']):<5} | {str(s['has_breadcrumb_schema']):<6} | {str(s['has_localbiz_schema']):<5} | {str(s['has_og_image']):<7}")
