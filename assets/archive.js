const filters = document.querySelectorAll('[data-filter]');
const cards = document.querySelectorAll('[data-category]');
const filterStatus = document.querySelector('#filter-status');
filters.forEach((filter) => {
  filter.addEventListener('click', () => {
    filters.forEach((button) => button.setAttribute('aria-pressed', String(button === filter)));
    let visibleCount = 0;
    cards.forEach((card) => {
      card.hidden = filter.dataset.filter !== 'all' && card.dataset.category !== filter.dataset.filter;
      if (!card.hidden) visibleCount += 1;
    });
    if (filterStatus) filterStatus.textContent = `${visibleCount} collections shown`;
  });
});

const requestedCategory = new URLSearchParams(window.location.search).get('category');
if (requestedCategory) {
  const requestedFilter = Array.from(filters).find((filter) => filter.dataset.filter === requestedCategory);
  if (requestedFilter) requestedFilter.click();
}

const viewer = document.querySelector('#viewer');
const imageLinks = Array.from(document.querySelectorAll('[data-view-image]'));
if (viewer && typeof viewer.showModal === 'function') {
  const image = viewer.querySelector('img');
  const caption = viewer.querySelector('[data-view-caption]');
  const position = viewer.querySelector('[data-view-position]');
  const previous = viewer.querySelector('[data-view-previous]');
  const next = viewer.querySelector('[data-view-next]');
  let activeIndex = 0;
  let opener;
  const showImage = (index) => {
    activeIndex = index;
    const source = imageLinks[index];
    image.src = source.href;
    image.alt = source.querySelector('img').alt;
    caption.textContent = source.dataset.caption;
    position.textContent = `${index + 1} / ${imageLinks.length}`;
    previous.disabled = index === 0;
    next.disabled = index === imageLinks.length - 1;
  };
  imageLinks.forEach((link, index) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      opener = link;
      showImage(index);
      viewer.showModal();
      document.body.classList.add('modal-open');
    });
  });
  viewer.querySelector('[data-view-close]').addEventListener('click', () => viewer.close());
  previous.addEventListener('click', () => showImage(Math.max(0, activeIndex - 1)));
  next.addEventListener('click', () => showImage(Math.min(imageLinks.length - 1, activeIndex + 1)));
  viewer.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      showImage(Math.max(0, Math.min(imageLinks.length - 1, activeIndex + (event.key === 'ArrowLeft' ? -1 : 1))));
    }
  });
  viewer.addEventListener('close', () => {
    document.body.classList.remove('modal-open');
    if (opener) opener.focus();
  });
}
