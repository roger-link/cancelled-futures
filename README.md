# Cancelled Futures

Website at **https://cancelledfutures.com/**, connecting the music on [Bandcamp](https://cancelledfutures.bandcamp.com/) with Unfold, the generative music app for Mac.

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

Custom domain: `cancelledfutures.com`, recorded in `CNAME` and in this repository's GitHub Pages settings. HTTPS is enforced; GitHub manages certificate renewal. `www.cancelledfutures.com` redirects to the root domain.

Porkbun DNS uses these website records (TTL 600):

| Type | Host | Target |
| --- | --- | --- |
| ALIAS | root / blank | `roger-link.github.io` |
| CNAME | `www` | `roger-link.github.io` |

Mail and other TXT records are independent of the website and remain in place. The existing `roger-link.github.io` repository and rogerlink.com retain their own source and settings. See [GitHub's custom-domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) before changing hosting.

## Release updates

Unfold is being prepared for release. The app's development repository is currently [roger-link/phrase-mix](https://github.com/roger-link/phrase-mix). When the renamed Mac build is ready, replace the release section's development link with the verified GitHub Release download. Do not advertise an available download before one exists.
