# Cancelled Futures

Replacement website for **https://cancelledfutures.com/**, implementing the approved editorial archive design: oversized Bricolage Grotesque masthead, Instrument Serif Italic, IBM Plex Mono labels, warm paper, black rules, and restrained rust-orange accents.

This replacement is published through the existing GitHub Pages source branch, `main`. DNS and Bandcamp visibility remain unchanged. Plastic Memory is explicitly forthcoming, with no announced release date or public listening player. Its cover is the exact original retrieved from the existing Bandcamp album, not a generated approximation.

## Pages

- `/`: featured recording, numbered Index, and project statement
- `/recordings/` and `/recordings/plastic-memory/`: forthcoming recording and notes
- `/works/`: filterable visual archive, including category links from the Index
- `/works/bicycle-2007/`: four color-inverted photographs
- `/works/body-exposure/`: four photographs, including the hallway closing frame
- `/works/sixteen/`: eight photographs, ending with a pool seen from a high window
- `/works/flowers-out-of-focus/`: four flower photographs, October 17, 2008
- `/works/everyday/`: Chips, Yellow wall, and Desire Lines / pavement, grouped as three photographs, 2010
- `/works/chips/` and `/works/desire-lines/`: retained links redirecting to Everyday
- `/works/drawn-fields/`: fourteen iPad drawings, 2024
- `/works/processing-studies/`: four still outputs from Processing scripts, also linked from Experiments; year awaits confirmation
- `/works/facades-grids/`: three spatial studies
- `/works/rooms-without-occupants/`: Somewhere Between, four spatial studies; original URL retained
- `/works/works-on-paper/`: five drawings and works on paper; photographed June 3, 2025, confirmed by DateTimeOriginal in all five source photographs, not a confirmed artwork creation date
- `/experiments/` and `/experiments/wave-sculpture/`: playable Wave Sculpture in two original versions
- `/whoop-dee-doo/` and `/whoop-dee-doo/tba/`: collaborative project section and three photographs of the TBA installation in Portland
- `/whoop-dee-doo/baltimore/`: three show photographs; date, venue, role, and photo credits await further details
- `/about/`: personal introduction and an uncropped photograph credited to Jaimie Warren, supplied as rojair.jpg
- `/unfold/`: Unfold overview and honest release status
- `404.html`: custom missing-page response

Photography collection details include capture dates read from the original files: Bicycle, April 23, 2007; Body / Exposure, May 17, 2009; Sixteen, August 30–31, 2008. These preserve camera-recorded dates rather than inferring a timezone. The Bicycle title omits its year; its existing URL is unchanged.

Static HTML, CSS, and JavaScript with local WebP artwork and self-hosted fonts. No analytics, cookies, accounts, or external assets are required at runtime. Wave Sculpture uses a locally vendored Three.js 0.160.0 runtime, loaded only after Play; no package installation or build is needed. Font licenses are included in `assets/fonts/`. WebP renditions omit source EXIF metadata, including camera location. Originals remain outside this checkout and are unchanged.

Wave Sculpture preserves the two shader-based versions from rogerlink.com, presented as Warm relief and Color drift. Visitors can play, pause, restart, switch versions, and use fullscreen where supported. Playback pauses when the work is offscreen or the document is hidden; nothing autoplays, including for reduced-motion users. Still images remain available without JavaScript or WebGL. Source provenance and the noise license are in `assets/wave/`; Three.js and its MIT license are in `assets/vendor/three/`. The original rogerlink.com site is unchanged.

The 53 static archive works build on the initial second-review selection, including the expanded fourteen-drawing iPad collection, four later paper works, four Processing outputs, the expanded eight-photo Sixteen sequence, four flower photographs, three Everyday photographs, and the expanded four-image Somewhere Between collection; they are not the entire eventual archive. Whoop Dee Doo has a separate collaborative project section. Its initial TBA page uses three photographs supplied by Roger, with project details and design credits taken from his earlier TBA portfolio entry. No project year is assigned. The source collection records and shared templates are in `tools/render.py`; run `python3 tools/render.py` after editing copy, sequence, or metadata. The generated HTML files are served directly; no server-side Python is needed. Responsive rendition sizes are recorded in `assets/art/dimensions.json`.

Somewhere Between adds IMG_0399.JPG and the closing IMG_0393.JPG from the exact Google Photos images supplied by Roger. Google Photos records November 10, 2022 for both. Their full 512 × 512 compositions are preserved without color edits or upscaling. The collection was previously titled Rooms Without Occupants; its original URL remains valid.

Everyday groups chips.jpg, dbcoopers_wall.jpg, and desire_lines_1.jpg from Roger's shared archive folder. Desire Lines / grass was removed from the selection at Roger's request; source files remain unchanged. Roger confirmed 2010 for the collection; source files lack DateTimeOriginal, and Drive upload and modification dates are not substituted. The description identifies what the photographs show without assigning authorship of the cardboard intervention. Web copies preserve full composition and color without upscaling. Sixteen remains its original eight-photo selection.

Flowers uses IMG_0439.jpg, IMG_0458.jpg, IMG_0434.jpg, and IMG_0464.jpg in that order. October 17, 2008 comes from DateTimeOriginal in all four source files, not the later modification or Drive upload timestamps. Web copies preserve composition and color without cropping, sharpening, or upscaling. Descriptive captions are working labels.

Processing Studies uses the supplied IMG_0035.jpg, IMG_0036.PNG, IMG_0037.PNG, and collage-0128.png without cropping or color edits. The collection links to https://github.com/roger-link/processing. The repository's collage sketches load source imagery and build layered, randomized fragments; these four supplied images are not attributed to individual sketch folders without confirmation. No scripts from the repository are run or embedded on the website.

The image viewer supports arrow keys, previous/next buttons, Escape, modal focus handling, and return to the opening image. Without JavaScript, image links still open local artwork files and all collections remain visible.

Four additional drawings were initially supplied as IMG_0034.PNG, IMG_0031.jpg, IMG_0026.PNG, and IMG_0029.jpg. The later review of Roger's Daily Drive folder selected Untitled 12, 24, 26, 28, 30, and 34 as six additions. Original exports Untitled 19, 20, 21, and 31 replace the existing Peach field, Electric forms, Blue / pink, and Pale field website copies without cropping or color edits. The remaining teal/violet screenshot retains its previously approved narrow bottom-edge crop to remove the home indicator. Roger confirmed 2024 for the iPad drawing collection; paper drawings remain dated 2025. Source files and Drive organization are unchanged. Drawing captions are descriptive working labels, not confirmed artwork titles.

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
