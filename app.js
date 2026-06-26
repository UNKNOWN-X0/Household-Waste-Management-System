/* ─── app.js ─── */

(function () {
  'use strict';

  // ── Tab navigation ──────────────────────────────────────────
  const navTabs = document.querySelectorAll('.nav-tab');
  const panels  = document.querySelectorAll('.panel');

  function showPanel(id) {
    panels.forEach(p => p.classList.remove('active'));
    navTabs.forEach(t => t.classList.remove('active'));

    const target = document.getElementById('panel-' + id);
    if (target) target.classList.add('active');

    const activeTab = document.querySelector(`.nav-tab[data-panel="${id}"]`);
    if (activeTab) {
      activeTab.classList.add('active');
      activeTab.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Close mobile menu if open
    const navTabsEl = document.getElementById('navTabs');
    navTabsEl.classList.remove('open');
  }

  navTabs.forEach(tab => {
    tab.addEventListener('click', () => showPanel(tab.dataset.panel));
  });

  // ── Mobile burger menu ──────────────────────────────────────
  const burger   = document.getElementById('navBurger');
  const navTabsEl = document.getElementById('navTabs');

  burger.addEventListener('click', (e) => {
    e.stopPropagation();
    navTabsEl.classList.toggle('open');
  });

  document.addEventListener('click', (e) => {
    if (!navTabsEl.contains(e.target) && e.target !== burger) {
      navTabsEl.classList.remove('open');
    }
  });

  // ── Checklist persistence (localStorage) ───────────────────
  const checkboxes = document.querySelectorAll('.check-item input[type="checkbox"]');

  checkboxes.forEach((cb, i) => {
    const key = 'check_' + i;
    // Restore saved state
    if (localStorage.getItem(key) === 'true') cb.checked = true;

    cb.addEventListener('change', () => {
      localStorage.setItem(key, cb.checked);
    });
  });

  // ── Scroll-reveal animation ─────────────────────────────────
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });

  function observeRevealTargets() {
    document.querySelectorAll(
      '.card, .stream-card, .week-card, .maint-card, .reward-card, .app-card, .pen-row, .route-row, .mapping-row, .bstep'
    ).forEach(el => {
      el.classList.add('reveal');
      revealObserver.observe(el);
    });
  }

  observeRevealTargets();

  // Re-observe when panels switch (cards may not exist yet in DOM scan)
  navTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      requestAnimationFrame(() => observeRevealTargets());
    });
  });

  // ── Keyboard navigation ─────────────────────────────────────
  const panelOrder = ['overview', 'streams', 'organic', 'outbound', 'penalty', 'roadmap', 'labels'];

  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT') return;

    const activeTab = document.querySelector('.nav-tab.active');
    if (!activeTab) return;
    const current = panelOrder.indexOf(activeTab.dataset.panel);

    if (e.key === 'ArrowRight' && current < panelOrder.length - 1) {
      showPanel(panelOrder[current + 1]);
    } else if (e.key === 'ArrowLeft' && current > 0) {
      showPanel(panelOrder[current - 1]);
    }
  });

  // ── Stream card expand / collapse on mobile ─────────────────
  const streamCards = document.querySelectorAll('.stream-card');

  streamCards.forEach(card => {
    const yesNo = card.querySelector('.yes-no');
    if (!yesNo) return;

    // On small screens, collapse yes-no by default
    if (window.innerWidth <= 600) {
      yesNo.classList.add('collapsed');
      card.classList.add('expandable');

      card.addEventListener('click', () => {
        yesNo.classList.toggle('collapsed');
        card.classList.toggle('expanded');
      });
    }
  });

  // ── Progress tracker for roadmap checklists ─────────────────
  function updateProgress() {
    const total   = checkboxes.length;
    const checked = Array.from(checkboxes).filter(c => c.checked).length;

    let bar = document.getElementById('progressBar');
    if (!bar && total > 0) {
      bar = document.createElement('div');
      bar.id = 'progressBar';
      bar.className = 'progress-bar-wrap';
      bar.innerHTML = `
        <div class="progress-bar-inner">
          <span class="progress-label" id="progressLabel"></span>
          <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
        </div>
      `;
      const penaltyPanel = document.getElementById('panel-penalty');
      const checklistEl  = penaltyPanel.querySelector('.checklist');
      if (checklistEl) checklistEl.before(bar);
    }

    if (bar) {
      const pct = Math.round((checked / total) * 100);
      const fill  = document.getElementById('progressFill');
      const label = document.getElementById('progressLabel');
      if (fill)  fill.style.width = pct + '%';
      if (label) label.textContent = `Onboarding: ${checked} / ${total} steps done`;
    }
  }

  checkboxes.forEach(cb => cb.addEventListener('change', updateProgress));
  updateProgress();

  // ── Init ────────────────────────────────────────────────────
  showPanel('overview');

})();
