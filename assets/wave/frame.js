const notify = (state) => window.parent.postMessage({type: 'cf-wave', state}, window.location.origin);
const variant = new URLSearchParams(window.location.search).get('variant') === 'drift' ? 'drift' : 'warm';
let controls;
try {
  const artwork = await import(variant === 'drift' ? './drift.js' : './warm.js');
  controls = await artwork.mountWave();
  document.querySelector('canvas').setAttribute('aria-label', 'Generative wave sculpture');
  document.querySelector('canvas').addEventListener('webglcontextlost', () => {
    controls.pause();
    notify('error');
  });
  window.addEventListener('message', (event) => {
    if (event.origin !== window.location.origin || event.source !== window.parent || event.data?.type !== 'cf-wave') return;
    if (event.data.action === 'play' && !document.hidden) controls.resume();
    if (event.data.action === 'pause') controls.pause();
  });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) controls.pause();
  });
  notify('ready');
} catch {
  const message = document.createElement('p');
  message.className = 'error';
  message.textContent = 'This browser could not start the WebGL artwork. Return to the artwork page to try again.';
  document.body.append(message);
  notify('error');
}
