// Highlight the active nav item based on current page
(function () {
  const brand = document.querySelector('.nav-brand');
  if (brand && location.pathname !== '/' && !location.pathname.endsWith('index.html')) {
    brand.style.opacity = '0.7';
  }
})();
