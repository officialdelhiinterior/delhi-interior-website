/**
 * DELHI INTERIOR — Master Interactive Logic & Motion Architecture
 * Luxury Architectural Standard (K2India & Editorial Physics)
 */

(function () {
  'use strict';

  // 1. Dynamic Copyright Year
  function initCopyright() {
    const yearEl = document.getElementById('year');
    if (yearEl) {
      yearEl.textContent = new Date().getFullYear();
    }
  }

  // 2. Announcement Bar & Nav Offset Sync
  function initAnnouncementBar() {
    const bar = document.getElementById('announcement-bar');
    const header = document.querySelector('.site-header');
    if (!bar || !header) return;

    const isDismissed = sessionStorage.getItem('delhi_interior_announcement_dismissed');

    if (isDismissed === 'true') {
      bar.style.display = 'none';
      header.style.top = '0px';
    } else {
      header.style.top = `${bar.offsetHeight}px`;
    }

    const closeBtn = bar.querySelector('.close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', function () {
        bar.style.transform = 'translateY(-100%)';
        header.style.top = '0px';
        sessionStorage.setItem('delhi_interior_announcement_dismissed', 'true');
        setTimeout(() => {
          bar.style.display = 'none';
        }, 300);
      });
    }
  }

  // 3. Smart Scrolled Navigation Bar (K2 Frosted Compression)
  function initNavScroll() {
    const header = document.querySelector('.site-header');
    if (!header) return;

    let ticking = false;

    function onScroll() {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          if (window.scrollY > 30) {
            header.classList.add('scrolled');
          } else {
            header.classList.remove('scrolled');
          }
          ticking = false;
        });
        ticking = true;
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // 4. Mobile Drawer Navigation
  window.openMobileMenu = function () {
    const menu = document.getElementById('mobile-menu');
    if (menu) {
      menu.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeMobileMenu = function () {
    const menu = document.getElementById('mobile-menu');
    if (menu) {
      menu.classList.remove('open');
      document.body.style.overflow = '';
    }
  };

  function initMobileMenu() {
    const toggles = document.querySelectorAll('.hamburger, .mobile-toggle, [aria-controls="mobile-nav"]');
    const closeBtns = document.querySelectorAll('.mobile-menu-close, .mobile-drawer-close');
    const overlay = document.getElementById('mobile-menu');

    toggles.forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        window.openMobileMenu();
      });
    });

    closeBtns.forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        window.closeMobileMenu();
      });
    });

    if (overlay) {
      overlay.addEventListener('click', function(e) {
        if (e.target === overlay) {
          window.closeMobileMenu();
        }
      });
    }

    const links = document.querySelectorAll('#mobile-menu a');
    links.forEach(l => l.addEventListener('click', window.closeMobileMenu));
  }

  // 5. Room Design Explorer Filter Tabs
  function initRoomTabs() {
    const tabBtns = document.querySelectorAll('.room-tab-btn');
    const roomCards = document.querySelectorAll('.room-card[data-room]');
    if (!tabBtns.length || !roomCards.length) return;

    tabBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        tabBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const targetRoom = btn.getAttribute('data-room-target');

        roomCards.forEach(card => {
          const cardRoom = card.getAttribute('data-room');
          if (targetRoom === 'all' || cardRoom === targetRoom) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // 6. Portfolio Category Filter
  function initPortfolioFilter() {
    const filterBtns = document.querySelectorAll('.portfolio-filter-btn');
    const cards = document.querySelectorAll('.portfolio-card[data-category]');
    if (!filterBtns.length || !cards.length) return;

    filterBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.getAttribute('data-filter');

        cards.forEach(card => {
          const category = card.getAttribute('data-category');
          if (filter === 'all' || category === filter) {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // 7. FAQ Accordion (Dual active & open class sync for rock-solid interaction)
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
  }

  // 8. Services Showcase Accordion
  function initServicesAccordion() {
    const cards = document.querySelectorAll('.service-acc-card');
    cards.forEach(card => {
      const btn = card.querySelector('.service-acc-header');
      if (!btn) return;
      btn.addEventListener('click', function () {
        const isOpen = card.classList.contains('open');
        cards.forEach(c => c.classList.remove('open'));
        if (!isOpen) {
          card.classList.add('open');
        }
      });
    });
  }

  // 9. Interactive Hero Consultation Quote Form
  function initQuoteForm() {
    const form = document.getElementById('quote-form');
    if (!form) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const nameInput = form.querySelector('[name="name"]');
      const phoneInput = form.querySelector('[name="phone"]');
      const serviceInput = form.querySelector('[name="service"]');
      const areaInput = form.querySelector('[name="area"]');
      const honeypot = form.querySelector('[name="honeypot"]');

      // Bot protection
      if (honeypot && honeypot.value) return;

      const name = nameInput ? nameInput.value.trim() : '';
      const phone = phoneInput ? phoneInput.value.trim() : '';
      const service = serviceInput ? serviceInput.value : 'Complete Interior';
      const area = areaInput ? areaInput.value.trim() : 'Delhi NCR';

      if (!name || !phone) {
        alert('Please fill in your Name and Phone Number to book your consultation.');
        return;
      }

      // Check phone pattern
      const cleanPhone = phone.replace(/[^\d+]/g, '');
      if (cleanPhone.length < 10) {
        alert('Please enter a valid 10-digit Indian mobile number.');
        return;
      }

      // Instant UI Success Feedback
      const fieldsContainer = form.querySelector('.form-fields-container');
      const successBox = form.querySelector('.form-success-state');
      const nameDisplay = form.querySelector('.client-name-display');
      const waDirectLink = form.querySelector('.wa-direct-link');

      if (nameDisplay) nameDisplay.textContent = name;

      const waMsg = `Hi Delhi Interior, my name is ${name}. I am looking for ${service} in ${area}. Please connect with me to schedule my free consultation. (Phone: ${phone})`;
      const waUrl = `https://wa.me/919643817099?text=${encodeURIComponent(waMsg)}`;

      if (waDirectLink) {
        waDirectLink.href = waUrl;
      }

      if (fieldsContainer) fieldsContainer.style.display = 'none';
      if (successBox) {
        successBox.style.display = 'block';
      }

      // Store in session
      sessionStorage.setItem('delhi_interior_lead', JSON.stringify({ name, phone, service, area, time: new Date().toISOString() }));
    });
  }

  // 10. Navigation Dropdown
  function initDropdown() {
    const dropdownItem = document.querySelector('.nav-dropdown-item');
    if (!dropdownItem) return;

    const trigger = dropdownItem.querySelector('.nav-dropdown-trigger');
    const menu = dropdownItem.querySelector('.nav-dropdown-menu');
    if (!trigger || !menu) return;

    trigger.addEventListener('click', function (e) {
      if (window.innerWidth <= 1080) {
        e.preventDefault();
        dropdownItem.classList.toggle('active');
      }
    });
  }

  // 11. K2India-Inspired Scroll Reveal Animations
  function initScrollAnimations() {
    // Check reduced motion preference
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      return;
    }

    // Flag body as js-ready so reveal initial states take effect smoothly
    document.documentElement.classList.add('js-ready');

    // Select all architectural content elements that benefit from scroll reveals
    const revealTargets = [
      '.section-header-center',
      '.section-header',
      '.craftsman-advantage-grid > div',
      '.usps-grid-kd > div',
      '.why-need-card',
      '.dual-specialty-grid > div',
      '.room-card',
      '.portfolio-card',
      '.specialty-card',
      '.testimonial-card',
      '.faq-item',
      '.trust-item',
      '.trust-strip-item',
      '.process-step-card',
      '.service-acc-card',
      '.cta-banner'
    ];

    const elements = document.querySelectorAll(revealTargets.join(', '));
    if (!elements.length) return;

    // Apply stagger delays to siblings in grid containers
    const grids = document.querySelectorAll('.craftsman-advantage-grid, .usps-grid-kd, .room-grid, .portfolio-grid, .testimonials-grid, .dual-specialty-grid, .trust-strip-grid');
    grids.forEach(grid => {
      const children = Array.from(grid.children);
      children.forEach((child, idx) => {
        const delayClass = `motion-delay-${(idx % 6) + 1}`;
        child.classList.add(delayClass);
      });
    });

    elements.forEach(el => {
      el.classList.add('motion-reveal');
    });

    if (!('IntersectionObserver' in window)) {
      // Fallback: reveal immediately
      elements.forEach(el => el.classList.add('is-visible'));
      return;
    }

    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -40px 0px',
      threshold: 0.12
    });

    elements.forEach(el => observer.observe(el));
  }

  // 12. Animated Metric Counters (Trust Strip)
  function initMetricCounters() {
    const counterElements = document.querySelectorAll('.metric-counter, .trust-item h4, .trust-strip-item > div:first-child');
    if (!counterElements.length) return;

    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      return;
    }

    // Helper easeOutExpo
    function easeOutExpo(x) {
      return x === 1 ? 1 : 1 - Math.pow(2, -10 * x);
    }

    function animateCounter(el) {
      let target = el.getAttribute('data-target');
      let suffix = el.getAttribute('data-suffix');

      if (!target) {
        // Auto parse digits from existing text
        const text = el.textContent.trim();
        const match = text.match(/^(\d+)(.*)$/);
        if (match) {
          target = parseInt(match[1], 10);
          suffix = match[2];
        } else {
          return;
        }
      } else {
        target = parseInt(target, 10);
        suffix = suffix || '';
      }

      if (isNaN(target)) return;

      const duration = 1600; // ms
      const startTime = performance.now();

      function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = easeOutExpo(progress);
        const currentVal = Math.floor(eased * target);

        el.innerHTML = `${currentVal}<span>${suffix}</span>`;

        if (progress < 1) {
          requestAnimationFrame(update);
        } else {
          el.innerHTML = `${target}<span>${suffix}</span>`;
        }
      }

      requestAnimationFrame(update);
    }

    if (!('IntersectionObserver' in window)) {
      return;
    }

    const counterObserver = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.3
    });

    counterElements.forEach(el => counterObserver.observe(el));
  }

  // 13. Brief Tier Request Links
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

  // DOM Ready
  document.addEventListener('DOMContentLoaded', function () {
    initCopyright();
    initAnnouncementBar();
    initNavScroll();
    initMobileMenu();
    initRoomTabs();
    initPortfolioFilter();
    initServicesAccordion();
    initFaqAccordion();
    initQuoteForm();
    initDropdown();
    initScrollAnimations();
    initMetricCounters();
    initBriefTierLinks();
  });
})();
