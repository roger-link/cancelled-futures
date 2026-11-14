(() => {
  const grids = [...document.querySelectorAll('.note-grid')];
  const button = document.getElementById('new-pattern');
  const status = document.getElementById('pattern-status');
  if (!grids.length || !button) return;
  let variation = 0;
  function draw() {
    const motif = Array.from({length: 8}, (_, i) =>
      (Math.round(Math.sin((i + variation * .7) * 1.2) * 2) + 3));
    grids.forEach((grid, row) => {
      grid.replaceChildren();
      for (let step = 0; step < 16; step++) {
        const note = document.createElement('span');
        note.className = 'note';
        const pitch = (motif[(step + row * 2) % 8] + row + (step > 7 ? 1 : 0)) % 7;
        note.style.setProperty('--pitch', `${pitch * 10 + 3}px`);
        note.style.setProperty('--opacity', (step + row + variation) % 5 === 0 ? '.15' : '.95');
        grid.append(note);
      }
    });
  }
  button.addEventListener('click', () => {
    variation++;
    draw();
    status.textContent = `Visual phrase illustration changed. Variation ${variation + 1}. No audio is playing.`;
  });
  draw();
})();
