# Cancelled Futures

Static website for Cancelled Futures, connecting the music on [Bandcamp](https://cancelledfutures.bandcamp.com/) with Unfold, the generative music app for Mac.

## Pages

- `/`: music and tools homepage
- `/unfold/`: Unfold overview and honest release status
- `404.html`: custom missing-page response

Buildless HTML, CSS, JavaScript, and original SVG artwork. No dependencies, analytics, cookies, accounts, external fonts, or external assets are required to render the site. Bandcamp and GitHub are ordinary outgoing links.

## Local preview

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/. Check both pages at desktop and phone widths. The phrase illustration on the Unfold page is visual only and is clearly labeled; it is not an app screenshot or audio demonstration.

## Hosting

GitHub Pages from the `main` branch, repository root. `.nojekyll` preserves the plain static structure. All internal assets and navigation use relative URLs, so the site also works at a repository project path.

Intended domain: `cancelledfutures.com`. Add its `CNAME` file only after registration and connect the domain in GitHub Pages settings. See GitHub's current custom-domain documentation for DNS values. The existing `roger-link.github.io` repository and rogerlink.com do not need source or settings changes.

## Release updates

Unfold is being prepared for release. The app's development repository is currently [roger-link/phrase-mix](https://github.com/roger-link/phrase-mix). When the renamed Mac build is ready, replace the release section's development link with the verified GitHub Release download. Do not advertise an available download before one exists.
