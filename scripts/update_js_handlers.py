with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Fix FAQ Accordion logic
old_faq = '''  // 7. FAQ Accordion
  function initFaqAccordion() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
      const q = item.querySelector('.faq-question');
      if (!q) return;
      q.addEventListener('click', function () {
        const isOpen = item.classList.contains('open');
        faqItems.forEach(i => i.classList.remove('open'));
        if (!isOpen) item.classList.add('open');
      });
    });
  }'''

new_faq = '''  // 7. FAQ Accordion (Dual active & open class sync for rock-solid interaction)
  function initFaqAccordion() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
      const q = item.querySelector('.faq-question');
      if (!q) return;
      q.addEventListener('click', function () {
        const isOpen = item.classList.contains('active') || item.classList.contains('open');
        faqItems.forEach(i => {
          i.classList.remove('active');
          i.classList.remove('open');
          const btn = i.querySelector('.faq-question');
          if (btn) btn.setAttribute('aria-expanded', 'false');
        });
        if (!isOpen) {
          item.classList.add('active');
          item.classList.add('open');
          q.setAttribute('aria-expanded', 'true');
        }
      });
    });
  }'''

js = js.replace(old_faq, new_faq)

# 2. Fix Room Tabs display restore
old_tabs = '''        roomCards.forEach(card => {
          const cardRoom = card.getAttribute('data-room');
          if (targetRoom === 'all' || cardRoom === targetRoom) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });'''

new_tabs = '''        roomCards.forEach(card => {
          const cardRoom = card.getAttribute('data-room');
          if (targetRoom === 'all' || cardRoom === targetRoom) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });'''

js = js.replace(old_tabs, new_tabs)

# 3. Fix mobile menu link selector
js = js.replace("document.querySelectorAll('.mobile-menu a')", "document.querySelectorAll('#mobile-menu a')")

# 4. Add Brief Tier Links handler to smooth scroll to consultation card
tier_handler = '''  // 13. Brief Tier Request Links
  function initBriefTierLinks() {
    const links = document.querySelectorAll('.brief-tier-link');
    links.forEach(link => {
      link.addEventListener('click', function (e) {
        const card = document.getElementById('consultation-card');
        if (card) {
          e.preventDefault();
          card.scrollIntoView({ behavior: 'smooth', block: 'start' });
          const tierSelect = link.getAttribute('data-tier-select');
          const selectEl = document.getElementById('service-type');
          if (tierSelect && selectEl) {
            for (let i = 0; i < selectEl.options.length; i++) {
              if (selectEl.options[i].value.includes(tierSelect) || selectEl.options[i].text.includes(tierSelect)) {
                selectEl.selectedIndex = i;
                break;
              }
            }
          }
          const nameInput = document.getElementById('client-name');
          if (nameInput) {
            setTimeout(() => nameInput.focus(), 600);
          }
        }
      });
    });
  }
'''

if 'initBriefTierLinks' not in js:
    js = js.replace('  // DOM Ready', tier_handler + '\n  // DOM Ready')
    js = js.replace('initMetricCounters();', 'initMetricCounters();\n    initBriefTierLinks();')

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated assets/js/main.js with rock-solid button handlers and accordion fixes.")
