import os, json, urllib.parse
from build_blog import ARTICLES
from build_main_and_utility import get_header, get_footer

os.makedirs('blog', exist_ok=True)

# 1. Generate Individual Blog Posts
for art in ARTICLES:
    art_dir = os.path.join('blog', art['slug'])
    os.makedirs(art_dir, exist_ok=True)
    art_file = os.path.join(art_dir, 'index.html')

    schema = {
        '@context': 'https://schema.org',
        '@type': 'BlogPosting',
        'headline': art['h1'],
        'description': art['desc'],
        'image': f"https://delhiinterior.com{art['img']}",
        'datePublished': '2026-11-10T09:00:00+05:30',
        'dateModified': '2026-11-13T10:00:00+05:30',
        'author': {
            '@type': 'Organization',
            'name': 'Delhi Interior Editorial Team',
            'url': 'https://delhiinterior.com/about/'
        },
        'publisher': {
            '@type': 'Organization',
            'name': 'Delhi Interior',
            'logo': {
                '@type': 'ImageObject',
                'url': 'https://delhiinterior.com/og-image.jpg'
            }
        },
        'mainEntityOfPage': {
            '@type': 'WebPage',
            '@id': f"https://delhiinterior.com/blog/{art['slug']}/"
        }
    }

    related_arts = [a for a in ARTICLES if a['slug'] != art['slug']][:3]
    related_html = '\n'.join([
        f'''<article class="blog-card">
  <div class="blog-card-img">
    <picture>
      <source srcset="{ra['img']}" type="image/webp">
      <img src="{ra['img'].replace('.webp', '.jpg')}" alt="{ra['h1']}" width="800" height="450" loading="lazy">
    </picture>
  </div>
  <div class="blog-card-body">
    <div class="blog-card-meta">
      <span class="cat-badge">{ra['category']}</span>
      <span>{ra['read_time']}</span>
    </div>
    <h3>{ra['h1']}</h3>
    <p>{ra['summary']}</p>
    <a href="/blog/{ra['slug']}/" class="blog-read-link">Read Full Guide →</a>
  </div>
</article>'''
        for ra in related_arts
    ])

    share_url_text = urllib.parse.quote(f"{art['h1']} - https://delhiinterior.com/blog/{art['slug']}/")

    article_page_html = f'''{get_header(active_nav='blog', title=f"{art['title']} | Delhi Interior", desc=art['desc'], canonical=f"https://delhiinterior.com/blog/{art['slug']}/", schema=schema)}
  <main id="main-content">
    <article class="article-container">
      
      <!-- Breadcrumbs -->
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="/">Home</a>
        <span class="separator">/</span>
        <a href="/blog/">Blog</a>
        <span class="separator">/</span>
        <span class="current">{art['category']}</span>
      </nav>

      <!-- Article Header -->
      <header class="article-header">
        <div class="pill-badge" style="display:inline-flex; align-items:center; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.8rem; font-weight:700; margin-bottom:1rem;">
          {art['category']}
        </div>
        <h1>{art['h1']}<span class="logo-dot">.</span></h1>
        
        <div class="article-meta-bar">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <div style="width:36px; height:36px; border-radius:50%; background:var(--color-primary-light); color:var(--color-primary); font-weight:800; display:flex; align-items:center; justify-content:center; font-size:0.9rem;">D</div>
            <span>By <strong>Delhi Interior Editorial Team</strong></span>
          </div>
          <span>·</span>
          <span>📅 {art['date']}</span>
          <span>·</span>
          <span>⏱️ {art['read_time']}</span>
        </div>
      </header>

      <!-- Featured Image -->
      <div class="article-featured-img">
        <picture>
          <source srcset="{art['img']}" type="image/webp">
          <img src="{art['img'].replace('.webp', '.jpg')}" alt="{art['h1']} guide by Delhi Interior" width="1200" height="675" loading="eager">
        </picture>
      </div>

      <!-- Article Content Body -->
      <div class="article-body">
        {art['content']}
      </div>

      <!-- Author Bio Card -->
      <div style="background: #FAFAFA; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 2rem; margin: 4rem 0 2rem; display: flex; gap: 1.5rem; align-items: center;">
        <div style="width: 54px; height: 54px; border-radius: 50%; background: var(--color-primary-light); color: var(--color-primary); font-weight: 800; font-size: 1.5rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">D</div>
        <div>
          <h4 style="font-size: 1.1rem; font-weight: 700; color: var(--color-dark); margin-bottom: 0.3rem;">Delhi Interior Editorial Team</h4>
          <p style="font-size: 0.9rem; color: var(--color-muted); margin: 0; line-height: 1.6;">Written by our principal architects, modular engineers, and turnkey site directors with over 10+ years of residential expertise delivering 500+ homes across Delhi NCR.</p>
        </div>
      </div>

      <!-- WhatsApp Share -->
      <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border); padding: 1.25rem 0; margin-bottom: 4rem;">
        <span style="font-size: 0.9rem; font-weight: 600; color: var(--color-dark);">Found this helpful? Share with friends:</span>
        <a href="https://wa.me/?text={share_url_text}" class="btn btn-outline" style="padding: 0.45rem 1.2rem; font-size: 0.85rem;" target="_blank" rel="noopener noreferrer">
          Share on WhatsApp
        </a>
      </div>

      <!-- Related Guides -->
      <div>
        <h2 style="font-size: 1.8rem; font-weight: 800; margin-bottom: 2rem; color: var(--color-dark);">Related Interior Guides</h2>
        <div class="blog-grid" style="grid-template-columns: repeat(3, 1fr);">
          {related_html}
        </div>
      </div>

    </article>
  </main>
{get_footer()}'''

    with open(art_file, 'w', encoding='utf-8') as f:
        f.write(article_page_html)
    print(f'[SUCCESS] Generated blog post: {art_file}')

# 2. Generate Blog Listing Page (/blog/)
blog_list_schema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': 'https://delhiinterior.com/blog/'}
    ]
}

all_cards_html = '\n'.join([
    f'''<article class="blog-card">
  <div class="blog-card-img">
    <picture>
      <source srcset="{art['img']}" type="image/webp">
      <img src="{art['img'].replace('.webp', '.jpg')}" alt="{art['h1']} guide" width="800" height="450" loading="lazy">
    </picture>
  </div>
  <div class="blog-card-body">
    <div class="blog-card-meta">
      <span class="cat-badge">{art['category']}</span>
      <span>{art['read_time']}</span>
    </div>
    <h3>{art['h1']}</h3>
    <p>{art['summary']}</p>
    <a href="/blog/{art['slug']}/" class="blog-read-link">Read Full Guide →</a>
  </div>
</article>'''
    for art in ARTICLES
])

recent_links_html = '\n'.join([
    f'<li><a href="/blog/{art["slug"]}/" style="font-size: 0.9rem; color: var(--color-dark); font-weight: 600; text-decoration: none;">{art["h1"]}</a></li>'
    for art in ARTICLES
])

blog_index_html = f'''{get_header(active_nav='blog', title='Interior Design Guides & Cost Breakdowns | Delhi Interior Blog', desc='Read in-depth interior design guides, modular kitchen cost breakdowns, material guides, and renovation checklists for Delhi homeowners.', canonical='https://delhiinterior.com/blog/', schema=blog_list_schema)}
  <main id="main-content">
    <section class="inner-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="/">Home</a>
          <span class="separator">/</span>
          <span class="current">Guides &amp; Blog</span>
        </nav>
        <div class="pill-badge" style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.35rem 0.85rem; border-radius:999px; font-size:0.8rem; font-weight:700; margin-bottom:1rem;">
          ✦ Practical Home Design Insights
        </div>
        <h1>Interior Guides &amp; Insights<span class="logo-dot">.</span></h1>
        <p class="hero-subtitle">Unfiltered architectural advice, real material cost breakdowns, and room-by-room planning guides from Delhi NCR's premier design studio.</p>
      </div>
    </section>

    <section class="section-padding bg-light">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr 340px; gap: 3.5rem; align-items: start;">
          
          <!-- Articles Grid Left -->
          <div>
            <div class="blog-grid" style="grid-template-columns: 1fr 1fr;">
              {all_cards_html}
            </div>
          </div>

          <!-- Sticky Sidebar Right -->
          <aside style="position: sticky; top: 6rem; display: flex; flex-direction: column; gap: 2rem;">
            
            <!-- Free Consultation Card -->
            <div style="background: var(--color-white); border: 1.5px solid var(--color-primary-subtle); border-radius: var(--radius-lg); padding: 2.2rem 1.8rem; text-align: center; box-shadow: var(--shadow-md);">
              <div class="pill-badge" style="display:inline-flex; padding:0.3rem 0.8rem; border-radius:999px; font-size:0.75rem; font-weight:700; margin-bottom:1rem;">Complimentary Session</div>
              <h4 style="font-size: 1.25rem; font-weight: 800; color: var(--color-dark); margin-bottom: 0.6rem;">Free Design Consultation</h4>
              <p style="font-size: 0.88rem; color: var(--color-muted); line-height: 1.6; margin-bottom: 1.5rem;">Consult with our senior designers before committing. Our designers visit your site anywhere in Delhi NCR.</p>
              <a href="/contact/" class="btn btn-primary btn-block">Book Free Site Visit</a>
            </div>

            <!-- Categories Card -->
            <div style="background: var(--color-white); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 2rem; box-shadow: var(--shadow-sm);">
              <h4 style="font-size: 1.1rem; font-weight: 700; color: var(--color-dark); margin-bottom: 1.2rem;">Explore Services</h4>
              <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.9rem;">
                <li><a href="/modular-kitchen-delhi/" style="color: #4B5563; text-decoration: none;">→ Modular Kitchen Design</a></li>
                <li><a href="/wardrobe-design-delhi/" style="color: #4B5563; text-decoration: none;">→ Custom Wardrobes &amp; Closets</a></li>
                <li><a href="/wall-paneling-delhi/" style="color: #4B5563; text-decoration: none;">→ Wall Paneling &amp; TV Units</a></li>
                <li><a href="/full-home-interior-delhi/" style="color: #4B5563; text-decoration: none;">→ Turnkey Full Home Interiors</a></li>
                <li><a href="/painting-polishing-delhi/" style="color: #4B5563; text-decoration: none;">→ Paints, PU &amp; Polish Guides</a></li>
              </ul>
            </div>

            <!-- Recent Articles Card -->
            <div style="background: var(--color-white); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 2rem; box-shadow: var(--shadow-sm);">
              <h4 style="font-size: 1.1rem; font-weight: 700; color: var(--color-dark); margin-bottom: 1.2rem;">Recent Guides</h4>
              <ul style="list-style: none; display: flex; flex-direction: column; gap: 1rem;">
                {recent_links_html}
              </ul>
            </div>

            <!-- Quick WhatsApp Button -->
            <a href="https://wa.me/919643817099?text=Hi+Delhi+Interior%2C+I+have+a+question+about+interior+design." class="btn btn-outline" style="width: 100%; border-color: #10B981; color: #10B981;" target="_blank" rel="noopener noreferrer">
              Chat Directly on WhatsApp
            </a>

          </aside>

        </div>
      </div>
    </section>
  </main>
{get_footer()}'''

with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(blog_index_html)
print('[SUCCESS] Generated: blog/index.html')

print('All blog pages regenerated successfully in Livspace aesthetic.')
