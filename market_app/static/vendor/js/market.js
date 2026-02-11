document.addEventListener('DOMContentLoaded', () => {
  const slider = document.querySelector('.insta-slider');
  const track = slider ? slider.querySelector('.insta-track') : null;

  if (track && track.dataset.cloned !== 'true') {
    const items = Array.from(track.children);
    if (items.length) {
      items.forEach((item) => {
        const clone = item.cloneNode(true);
        clone.setAttribute('aria-hidden', 'true');
        track.appendChild(clone);
      });

      track.dataset.cloned = 'true';
      track.classList.add('insta-track--animated');
      slider.classList.add('is-animated');
    }
  }

  document.querySelectorAll('.product-gallery').forEach((gallery) => {
    const mainImage = gallery.querySelector('.product-gallery__main img');
    const thumbs = gallery.querySelector('.product-gallery__thumbs');

    if (!mainImage || !thumbs) {
      return;
    }

    thumbs.addEventListener('click', (event) => {
      const button = event.target.closest('.product-thumb');
      if (!button || !thumbs.contains(button)) {
        return;
      }

      const thumbImage = button.querySelector('img');
      if (!thumbImage) {
        return;
      }

      const fullSrc = button.dataset.full || thumbImage.src;
      mainImage.src = fullSrc;
      mainImage.alt = thumbImage.alt || mainImage.alt;

      thumbs.querySelectorAll('.product-thumb.is-active').forEach((item) => {
        item.classList.remove('is-active');
      });
      button.classList.add('is-active');
    });
  });
});
