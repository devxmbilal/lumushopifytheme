(function () {
  function initProductTabs(root) {
    if (!root || root.dataset.lumuTabsInit === 'true') return;
    root.dataset.lumuTabsInit = 'true';

    const buttons = root.querySelectorAll('[data-lumu-tab]');
    const panels = root.querySelectorAll('[data-lumu-panel]');

    buttons.forEach((button) => {
      button.addEventListener('click', () => {
        const target = button.dataset.lumuTab;

        buttons.forEach((btn) => {
          const isActive = btn.dataset.lumuTab === target;
          btn.classList.toggle('is-active', isActive);
          btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });

        panels.forEach((panel) => {
          const isActive = panel.dataset.lumuPanel === target;
          panel.classList.toggle('is-active', isActive);
          panel.hidden = !isActive;
        });
      });
    });

    const descWrap = root.querySelector('[data-lumu-desc-wrap]');
    const seeMoreBtn = root.querySelector('[data-lumu-see-more]');
    const seeMoreLabel = root.querySelector('[data-lumu-see-more-label]');

    if (descWrap && seeMoreBtn) {
      const desc = root.querySelector('[data-lumu-desc]');
      const collapsedHeight = 280;

      const checkHeight = () => {
        if (!desc) return;
        const needsToggle = desc.scrollHeight > collapsedHeight + 20;
        if (!needsToggle) {
          descWrap.classList.add('is-short');
          seeMoreBtn.setAttribute('hidden', '');
        } else {
          descWrap.classList.remove('is-short');
          seeMoreBtn.removeAttribute('hidden');
        }
      };

      checkHeight();
      window.addEventListener('resize', checkHeight);

      seeMoreBtn.addEventListener('click', () => {
        const expanded = descWrap.classList.toggle('is-expanded');
        seeMoreBtn.classList.toggle('is-expanded', expanded);
        seeMoreBtn.setAttribute('aria-expanded', expanded ? 'true' : 'false');

        if (seeMoreLabel) {
          const isAr = document.documentElement.lang === 'ar';
          seeMoreLabel.textContent = expanded
            ? isAr
              ? 'عرض أقل'
              : 'See Less'
            : isAr
              ? 'عرض المزيد'
              : 'See More';
        }
      });
    }
  }

  function initAll() {
    document.querySelectorAll('[data-lumu-tabs]').forEach(initProductTabs);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  document.addEventListener('shopify:section:load', (event) => {
    const tabs = event.target.querySelector('[data-lumu-tabs]');
    if (tabs) initProductTabs(tabs);
  });
})();
