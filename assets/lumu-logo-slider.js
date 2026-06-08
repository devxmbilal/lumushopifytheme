(function () {
  const INTERVAL_MS = 5000;

  function initLogoSlider(slider) {
    if (!slider || slider.dataset.lumuLogoInit === 'true') return;
    slider.dataset.lumuLogoInit = 'true';

    const images = slider.querySelectorAll('.lumu-logo-slider__img');
    if (images.length < 2) return;

    let activeIndex = 0;

    const tick = () => {
      images.forEach((img) => img.classList.remove('is-active'));
      images[activeIndex].classList.add('is-active');
      activeIndex = (activeIndex + 1) % images.length;
    };

    tick();
    window.setInterval(tick, INTERVAL_MS);
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
    event.target.querySelectorAll('[data-lumu-logo-slider]').forEach(initLogoSlider);
  });
})();
