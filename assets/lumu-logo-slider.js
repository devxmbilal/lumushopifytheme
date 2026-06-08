(function () {
  const INTERVAL_MS = 5000;

  function initLogoSlider(slider) {
    if (!slider || slider.dataset.lumuLogoInit === 'true') return;
    slider.dataset.lumuLogoInit = 'true';

    const images = slider.querySelectorAll('.lumu-logo-slider__img');
    if (images.length < 2) return;

    let activeIndex = 0;

    setInterval(() => {
      images[activeIndex].classList.remove('is-active');
      activeIndex = (activeIndex + 1) % images.length;
      images[activeIndex].classList.add('is-active');
    }, INTERVAL_MS);
  }

  function initAll() {
    document.querySelectorAll('[data-lumu-logo-slider]').forEach(initLogoSlider);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  document.addEventListener('shopify:section:load', (event) => {
    const slider = event.target.querySelector('[data-lumu-logo-slider]');
    if (slider) initLogoSlider(slider);
  });
})();
