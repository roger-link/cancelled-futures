# Cancelled Futures

Replacement website for **https://cancelledfutures.com/**, implementing the approved editorial archive design: oversized Bricolage Grotesque masthead, Instrument Serif Italic, IBM Plex Mono labels, warm paper, black rules, and restrained rust-orange accents.

This replacement is published through the existing GitHub Pages source branch, `main`. DNS and Bandcamp visibility remain unchanged. Plastic Memory is explicitly forthcoming, with no announced release date or public listening player. Its cover is the exact original retrieved from the existing Bandcamp album, not a generated approximation.

## Pages

- `/`: featured recording, numbered Index, and project statement
- `/recordings/` and `/recordings/plastic-memory/`: forthcoming recording and notes
- `/works/`: filterable visual archive, including category links from the Index
- `/works/bicycle-2007/`: four color-inverted photographs
- `/works/body-exposure/`: four photographs, including the hallway closing frame
- `/works/sixteen/`: two selected interior photographs
- `/works/drawn-fields/`: four drawings
- `/works/facades-grids/`: three spatial studies
- `/works/rooms-without-occupants/`: two spatial studies
- `/works/works-on-paper/`: one layered work on paper
- `/experiments/` and `/experiments/wave-sculpture/`: playable Wave Sculpture in two original versions
- `/about/`: project context
- `/unfold/`: Unfold overview and honest release status
- `404.html`: custom missing-page response

Static HTML, CSS, and JavaScript with local WebP artwork and self-hosted fonts. No analytics, cookies, accounts, or external assets are required at runtime. Wave Sculpture uses a locally vendored Three.js 0.160.0 runtime, loaded only after Play; no package installation or build is needed. Font licenses are included in `assets/fonts/`. WebP renditions omit source EXIF metadata, including camera location. Originals remain outside this checkout and are unchanged.

Wave Sculpture preserves the two shader-based versions from rogerlink.com, presented as Warm relief and Color drift. Visitors can play, pause, restart, switch versions, and use fullscreen where supported. Playback pauses when the work is offscreen or the document is hidden; nothing autoplays, including for reduced-motion users. Still images remain available without JavaScript or WebGL. Source provenance and the noise license are in `assets/wave/`; Three.js and its MIT license are in `assets/vendor/three/`. The original rogerlink.com site is unchanged.

The 20 archive works are an initial implementation of the second review, not the entire eventual archive. Whoop Dee Doo is deliberately deferred. The source collection records and shared templates are in `tools/render.py`; run `python3 tools/render.py` after editing copy, sequence, or metadata. The generated HTML files are served directly; no server-side Python is needed. Responsive rendition sizes are recorded in `assets/art/dimensions.json`.

The image viewer supports arrow keys, previous/next buttons, Escape, modal focus handling, and return to the opening image. Without JavaScript, image links still open local artwork files and all collections remain visible.

## Archive follow-up

- Confirm working collection names, years, authorship, and materials against originals. Spatial works are labeled generally as Digital image studies until their process is confirmed.
- Replace screenshot-derived drawing copies with clean exports where possible; recover higher-resolution early photographs and spatial studies if available.
- Expand or tighten the small selections through final sequencing rather than padding to a quota.
- Add album listening links only when supplied or made public by the owner.
- Review future changes before committing and pushing to the existing GitHub Pages source branch.

## Local preview

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/. Check the homepage, archive filtering, gallery keyboard controls, and interior pages at desktop and phone widths. The phrase illustration on Unfold is visual only and explicitly labeled; it is not an app screenshot or audio demonstration.

## Hosting

GitHub Pages from the `main` branch, repository root. `.nojekyll` preserves the plain static structure. All internal assets and navigation use relative URLs, so the site also works at a repository project path.

Custom domain: `cancelledfutures.com`, recorded in `CNAME` and in this repository's GitHub Pages settings. HTTPS is enforced; GitHub manages certificate renewal. `www.cancelledfutures.com` redirects to the root domain.

Porkbun DNS uses these website records (TTL 600):

| Type | Host | Target |
| --- | --- | --- |
| ALIAS | root / blank | `roger-link.github.io` |
| CNAME | `www` | `roger-link.github.io` |

Mail and other TXT records are independent of the website and remain in place. The existing `roger-link.github.io` repository and rogerlink.com retain their own source and settings. See [GitHub's custom-domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) before changing hosting.

## Release updates

Unfold is being prepared for release. The app's development repository is [roger-link/unfold](https://github.com/roger-link/unfold). When the renamed Mac build is ready, replace the release section's development link with the verified GitHub Release download. Do not advertise an available download before one exists.
