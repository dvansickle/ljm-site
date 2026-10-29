# Lolly Merrell — journalist portfolio

A lightweight static website for **https://lollymerrell.com**, hosted on GitHub Pages. No dependencies, build step, backend, analytics, or external fonts.

## Enable deployment from main

1. Open this repository’s **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select **main** and **/ (root)**, then save.
4. Confirm **Custom domain** is `lollymerrell.com` (also tracked in `CNAME`).
5. Once the DNS check and certificate finish, enable **Enforce HTTPS**.

Every push to `main` then publishes the site. No GitHub Actions workflow is needed for branch publishing. `.nojekyll` tells Pages to serve these files directly.

## DNS at WordPress.com

Keep the existing WordPress.com nameservers. Root (`@`) A records should point to:

- `185.199.108.153`
- `185.199.109.153`
- `185.199.110.153`
- `185.199.111.153`

Set `www` CNAME to `dvansickle.github.io`. Preserve email and verification records. With the apex custom domain selected in Pages, GitHub redirects the configured www variant to the apex.

## Local preview

Run from the repository root:

```sh
python3 -m http.server 8000
```

Visit http://localhost:8000. Check desktop and narrow mobile layouts before pushing.

## Files and future content

- `index.html`: homepage, portfolio, about, and contact sections.
- `assets/styles.css`: shared responsive styles.
- `assets/favicon.svg`: initials favicon.
- `404.html`: custom missing-page response.
- `content/README.md`: content editing guidance.
- `robots.txt` and `sitemap.xml`: basic search discovery.

Inspired by the biography-first and portfolio structure of https://stephanieannpearson.com/. No text, images, or biographical claims from that site are reused. The initial page clearly marks content as forthcoming. Add approved copy, real articles, a portrait, and contact information when available.
