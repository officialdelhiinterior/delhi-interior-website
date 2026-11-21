/**
 * DELHI INTERIOR — Lead Capture, Honeypot Anti-Spam & WhatsApp Routing
 */

(function () {
  'use strict';

  function initLeadForm() {
    const form = document.getElementById('quote-form');
    if (!form || form.dataset.quoteBound) return;
    form.dataset.quoteBound = 'true';

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // 1. Honeypot anti-spam verification
      const honeypot = form.querySelector('input[name="honeypot"]');
      if (honeypot && honeypot.value.trim() !== '') {
        console.warn('Bot submission blocked.');
        return;
      }

      // 2. Extract inputs
      const nameInput = form.querySelector('#client-name');
      const phoneInput = form.querySelector('#client-phone');
      const serviceSelect = form.querySelector('#service-type');
      const areaInput = form.querySelector('#client-area');
      const messageInput = form.querySelector('#client-message');
      const submitBtn = form.querySelector('#submit-quote-btn');

      let isValid = true;

      // Validation
      if (!nameInput.value.trim()) {
        nameInput.classList.add('is-invalid');
        isValid = false;
      } else {
        nameInput.classList.remove('is-invalid');
      }

      const phoneVal = phoneInput.value.trim().replace(/\D/g, '');
      if (!phoneVal || phoneVal.length < 10) {
        phoneInput.classList.add('is-invalid');
        isValid = false;
      } else {
        phoneInput.classList.remove('is-invalid');
      }

      if (!isValid) {
        const firstError = form.querySelector('.is-invalid');
        if (firstError) {
          firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
          firstError.focus();
        }
        return;
      }

      // 3. UI Loading State
      const originalBtnText = submitBtn.innerHTML;
      submitBtn.innerHTML = 'Sending...';
      submitBtn.disabled = true;
      submitBtn.style.opacity = '0.5';

      // 4. Construct WhatsApp Pre-filled payload
      const clientName = nameInput.value.trim();
      const clientPhone = phoneInput.value.trim();
      const service = serviceSelect ? serviceSelect.value : 'Interior Design Consultation';
      const area = areaInput && areaInput.value.trim() ? areaInput.value.trim() : 'Delhi NCR';
      const msg = messageInput && messageInput.value.trim() ? messageInput.value.trim() : 'Please share portfolio and estimate.';

      const waText = `Hi Delhi Interior, I'm ${clientName}. Service needed: ${service}. Location: ${area}. Requirements: ${msg}. My number: ${clientPhone}.`;
      const waUrl = `https://wa.me/919643817099?text=${encodeURIComponent(waText)}`;

      // 5. Track GA4 Lead Event
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'generate_lead', {
          event_category: 'form',
          event_label: service,
          value: 1
        });
      }

      // 6. Transition to Success State
      const formFields = form.querySelector('.form-fields-container');
      const successState = form.querySelector('.form-success-state');

      setTimeout(() => {
        if (formFields) formFields.style.display = 'none';
        if (successState) {
          const clientNameSpan = successState.querySelector('.client-name-display');
          if (clientNameSpan) clientNameSpan.textContent = clientName;

          const waLinkBtn = successState.querySelector('.wa-direct-link');
          if (waLinkBtn) waLinkBtn.href = waUrl;

          successState.style.display = 'block';
        }

        // Open WhatsApp in a new tab/window
        window.open(waUrl, '_blank', 'noopener,noreferrer');

        // Redirect to Thank-You conversion page after 1.2s
        setTimeout(() => {
          window.location.href = '/thank-you/';
        }, 1200);
      }, 600);
    });

    // Remove invalid states on typing
    const inputs = form.querySelectorAll('.form-control');
    inputs.forEach(input => {
      input.addEventListener('input', function () {
        if (this.classList.contains('is-invalid') && this.value.trim()) {
          this.classList.remove('is-invalid');
        }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', initLeadForm);
})();
