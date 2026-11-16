import os, json
from build_services import SERVICES_DATA
from build_main_and_utility import get_header, get_footer

for s in SERVICES_DATA:
    page_dir = s['slug']
    os.makedirs(page_dir, exist_ok=True)
    html_file = os.path.join(page_dir, 'index.html')

    schema = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Services', 'item': 'https://delhiinterior.com/modular-kitchen-delhi/'},
            {'@type': 'ListItem', 'position': 3, 'name': s['h1'], 'item': f'https://delhiinterior.com/{s["slug"]}/'}
        ]
    }

    checklist_html = '\n'.join([
        f'<div class="checklist-item"><span class="check">✓</span><span>{item}</span></div>'
        for item in s['checklist']
    ])

    process_html = '\n'.join([
        f'<div class="process-step"><div class="step-circle">{idx+1}</div><h4>{title}</h4><p>{desc}</p></div>'
        for idx, (title, desc) in enumerate(s['process_steps'])
    ])

    gallery_html = '\n'.join([
        f'''<div class="portfolio-card">
  <picture>
    <source srcset="{img}" type="image/webp">
    <img src="{img.replace(".webp", ".jpg")}" alt="{title} by Delhi Interior in Delhi NCR" width="800" height="600" loading="lazy">
  </picture>
  <div class="portfolio-overlay">
    <h3>{title}</h3>
    <p>{loc}</p>
  </div>
</div>'''
        for img, title, loc in s['gallery']
    ])

    pricing_html = '\n'.join([
        f'''<div class="price-tier-card {'featured' if idx == 1 else ''}">
  {f'<div class="price-tier-badge">Most Popular</div>' if idx == 1 else ''}
  <h3>{tier_name}</h3>
  <div class="package-badge" style="display:inline-block; font-size:0.82rem; font-weight:700; color:#B89058; background:#F0FDF4; padding:0.3rem 0.8rem; border-radius:999px; margin:0.5rem 0 1.25rem; border:1px solid #DCFCE7;">✦ Custom Workshop Fabrication</div>
  <ul>
    ''' + '\n    '.join([f'<li>{feat}</li>' for feat in feats]) + f'''
  </ul>
  <a href="/contact/" class="btn {'btn-primary' if idx == 1 else 'btn-outline'} btn-block">Book Site Measurement</a>
</div>'''
        for idx, (tier_name, price, feats) in enumerate(s['pricing'])
    ])

    faq_html = '\n'.join([
        f'''<div class="faq-item">
  <button class="faq-question" aria-expanded="false">
    <span>{q}</span>
    <span class="faq-icon">+</span>
  </button>
  <div class="faq-answer">
    <div class="faq-answer-inner">{a}</div>
  </div>
</div>'''
        for q, a in s['faqs']
    ])

    related_html = '\n'.join([
        f'''<div class="blog-card">
  <div class="blog-card-body">
    <h3>{rtitle}</h3>
    <p>{rdesc}</p>
    <a href="{rlink}" class="blog-read-link">Explore Service →</a>
  </div>
</div>'''
        for rtitle, rlink, rdesc in s['related']
    ])

    page_content = f'''{get_header(
    active_nav='services',
    title=s['title'],
    desc=s['desc'],
    canonical=f"https://delhiinterior.com/{s['slug']}/",
    schema=schema
)}
  <main id="main-content">
    <!-- 1. Hero -->
    <section class="inner-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="/">Home</a>
          <span class="separator">/</span>
          <a href="/modular-kitchen-delhi/">Services</a>
          <span class="separator">/</span>
          <span class="current">{s['h1']}</span>
        </nav>
        <div class="pill-badge" style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.8rem; font-weight:700; margin-bottom:1rem;">
          ✦ {s['h1']} in Delhi NCR
        </div>
        <h1>{s['h1']}<span class="logo-dot">.</span></h1>
        <p class="hero-subtitle">{s['sub']}</p>
        <div class="hero-cta-group" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.5rem;">
          <a href="/contact/" class="btn btn-primary">Book Free Consultation</a>
          <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+consult+for+{s['slug']}." class="btn btn-outline" target="_blank" rel="noopener noreferrer">WhatsApp Specialist</a>
        </div>
      </div>
    </section>

    <!-- 2. Featured Real Photo -->
    <div class="container" style="margin-top: -2.5rem; margin-bottom: 3.5rem;">
      <div class="featured-service-photo" style="border-radius: var(--radius-xl); overflow: hidden; box-shadow: var(--shadow-lg);">
        <picture>
          <source srcset="{s['hero_img']}" type="image/webp">
          <img src="{s['hero_img'].replace('.webp', '.jpg')}" alt="{s['h1']} by Delhi Interior in Delhi NCR" width="1200" height="600" style="width:100%; height:480px; object-fit:cover; display:block;" loading="eager">
        </picture>
      </div>
    </div>

    <!-- 3. Overview Section -->
    <section class="section-padding bg-white">
      <div class="container">
        <div class="section-title-wrap" style="text-align:left; max-width:850px; margin-bottom:2.5rem;">
          <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Engineering Excellence</div>
          <h2>{s['overview_h2']}</h2>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; font-size: 1.02rem; line-height: 1.8; color: #4B5563;">
          <p>{s['overview_p1']}</p>
          <p>{s['overview_p2']}</p>
        </div>
      </div>
    </section>

    <!-- 4. What's Included (Checklist) -->
    <section class="section-padding bg-light">
      <div class="container">
        <div class="section-title-wrap">
          <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Standard Inclusions</div>
          <h2>What's Included in Every Project</h2>
          <p>Every single material specification is committed in writing. Zero hidden costs, zero contractor substitutions.</p>
        </div>
        <div class="checklist-grid">
          {checklist_html}
        </div>
      </div>
    </section>

    <!-- 5. 3-Step Process -->
    <section class="section-padding bg-white">
      <div class="container">
        <div class="section-title-wrap">
          <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Milestone Timeline</div>
          <h2>Our Delivery Process</h2>
          <p>Factory-engineered offsite, assembled on-site with zero dust and laser precision.</p>
        </div>
        <div class="process-grid">
          {process_html}
        </div>
      </div>
    </section>

    <!-- 6. Real Completed Projects -->
    <section class="section-padding bg-light">
      <div class="container">
        <div class="section-title-wrap">
          <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Completed Homes</div>
          <h2>Real Projects in Delhi NCR</h2>
          <p>All photographs represent authentic turnkey projects designed and executed across South Delhi, West Delhi, and Gurugram.</p>
        </div>
        <div class="portfolio-grid">
          {gallery_html}
        </div>
      </div>
    </section>

    <!-- 7. Bespoke Material Packages & Specifications -->
    <section class="section-padding bg-white">
      <div class="container">
        <div class="section-title-wrap">
          <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Material Specifications</div>
          <h2>Bespoke Execution Packages</h2>
          <p>Custom fabricated at our Mohammadpur workshop to your exact architectural specifications. Includes genuine materials, authentic German hardware, and lasting craftsmanship.</p>
        </div>
        <div class="pricing-grid">
          {pricing_html}
        </div>
      </div>
    </section>

    <!-- 8. Frequently Asked Questions -->
    <section class="section-padding bg-light">
      <div class="container" style="max-width: 860px;">
        <div class="section-title-wrap">
          <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Client FAQs</div>
          <h2>Frequently Asked Questions</h2>
          <p>Everything you need to know about materials, timelines, craftsmanship standards, and payment terms.</p>
        </div>
        <div class="faq-accordion">
          {faq_html}
        </div>
      </div>
    </section>

    <!-- 9. Related Services -->
    <section class="section-padding bg-white">
      <div class="container">
        <div class="section-title-wrap">
          <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.78rem; font-weight:700; margin-bottom:0.75rem;">Holistic Living</div>
          <h2>Related Interior Solutions</h2>
          <p>Combine multiple services into a unified turnkey package for seamless finish matching.</p>
        </div>
        <div class="blog-grid" style="grid-template-columns: repeat(3, 1fr);">
          {related_html}
        </div>
      </div>
    </section>

    <!-- 10. Final Call to Action -->
    <section class="final-cta section-padding" style="background: linear-gradient(135deg, #0D47A1 0%, #004D40 100%); color: white; text-align: center;">
      <div class="container" style="max-width: 760px;">
        <h2 style="color: white; font-size: 2.4rem; font-weight: 800; margin-bottom: 1rem;">Ready to Transform Your Home?</h2>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; line-height: 1.7; margin-bottom: 2rem;">Book a free consultation with our senior designers. We visit your site in Delhi NCR with material swatches and design catalogs.</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="/contact/" class="btn btn-secondary" style="background: white; color: #0D47A1; font-weight: 700;">Book Free Consultation</a>
          <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+want+to+book+a+consultation." class="btn btn-outline" style="border-color: white; color: white;" target="_blank" rel="noopener noreferrer">Chat on WhatsApp</a>
        </div>
      </div>
    </section>
  </main>
{get_footer()}'''

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(page_content)
    print(f'[SUCCESS] Generated: {html_file}')

print('All 9 service pages regenerated cleanly in Livspace aesthetic.')
