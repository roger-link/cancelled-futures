const player = document.querySelector('[data-wave-player]');
if (player) {
  const stage = player.querySelector('[data-wave-stage]');
  const play = player.querySelector('[data-wave-play]');
  const versions = player.querySelectorAll('[data-wave-variant]');
  const restart = player.querySelector('[data-wave-restart]');
  const fullscreen = player.querySelector('[data-wave-fullscreen]');
  const status = player.querySelector('[data-wave-status]');
  const poster = stage.querySelector('img');
  let frame;
  let ready = false;
  let wantsPlayback = false;
  let visible = true;
  let failed = false;
  let variant = 'warm';

  const updatePlayback = () => {
    if (ready) frame.contentWindow.postMessage({type: 'cf-wave', action: wantsPlayback && visible && !document.hidden ? 'play' : 'pause'}, window.location.origin);
    play.textContent = failed ? 'Try again' : wantsPlayback ? 'Pause' : 'Play moving work';
    play.setAttribute('aria-pressed', String(wantsPlayback));
    if (ready) status.textContent = wantsPlayback ? 'Playing · No audio' : 'Paused · No audio';
  };

  const load = () => {
    if (frame) frame.remove();
    ready = false;
    failed = false;
    stage.classList.remove('has-frame');
    frame = document.createElement('iframe');
    frame.title = `Wave Sculpture — ${variant === 'warm' ? 'warm relief' : 'color drift'} version`;
    frame.src = `${player.dataset.frameUrl}?variant=${variant}`;
    frame.setAttribute('tabindex', '-1');
    stage.append(frame);
    status.textContent = 'Loading the original JavaScript artwork…';
    updatePlayback();
  };

  play.addEventListener('click', () => {
    if (!frame || failed) {
      wantsPlayback = true;
      load();
    } else {
      wantsPlayback = !wantsPlayback;
      updatePlayback();
    }
  });

  versions.forEach((button) => {
    button.addEventListener('click', () => {
      if (variant === button.dataset.waveVariant) return;
      variant = button.dataset.waveVariant;
      poster.removeAttribute('srcset');
      poster.src = `${player.dataset.posterBase}wave-${variant}-960.webp`;
      versions.forEach((version) => version.setAttribute('aria-pressed', String(version === button)));
      if (frame) load();
      else status.textContent = `${variant === 'warm' ? 'Warm relief' : 'Color drift'} selected. Press Play to begin.`;
    });
  });

  restart.addEventListener('click', () => {
    wantsPlayback = true;
    load();
  });

  if (!document.fullscreenEnabled || typeof player.requestFullscreen !== 'function') fullscreen.hidden = true;
  document.addEventListener('fullscreenchange', () => {
    fullscreen.textContent = document.fullscreenElement ? 'Exit fullscreen' : 'Fullscreen';
  });
  fullscreen.addEventListener('click', async () => {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else await player.requestFullscreen();
    } catch {
      status.textContent = 'Fullscreen is unavailable in this browser. Playback is still available here.';
    }
  });

  window.addEventListener('message', (event) => {
    if (!frame || event.source !== frame.contentWindow || event.origin !== window.location.origin || event.data?.type !== 'cf-wave') return;
    if (event.data.state === 'ready') {
      ready = true;
      stage.classList.add('has-frame');
      updatePlayback();
    }
    if (event.data.state === 'error') {
      ready = false;
      failed = true;
      wantsPlayback = false;
      frame.remove();
      stage.classList.remove('has-frame');
      updatePlayback();
      status.textContent = 'The artwork needs WebGL, which could not start here. Try again or use another browser. The still image remains available.';
    }
  });

  document.addEventListener('visibilitychange', updatePlayback);
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      visible = entries[0].isIntersecting;
      updatePlayback();
    });
    observer.observe(stage);
  }
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) status.textContent = 'Reduced motion respected. The image stays still unless you press Play.';
}
