# Lolly Merrell

A static journalist portfolio at https://lollymerrell.com, hosted on GitHub Pages from `main` and the repository root. No installation or framework is required. Keep `CNAME` and `.nojekyll` in place.

## Edit and rebuild

- The approved biography is in `scripts/build.py` (`BIO`).
- Article titles, publication credits, summaries, and file paths are in `content/articles.json`.
- Article PDFs are in `assets/pdfs/`; optimized previews and the Dolomites photograph are in `assets/images/`.
- Shared styling is in `assets/styles.css`. Typography uses self-hosted Libre Baskerville, including regular, bold, and italic with its OFL license in `assets/fonts/`.
- Contact links open an email to `lollymerrell@yahoo.com`.

Run `python3 scripts/build.py` after changing content. It regenerates the homepage, three category archives, 20 article pages, the 404 page, and the sitemap. Commit the generated pages along with content edits.

For a preview, run `python3 -m http.server 8000 --bind 127.0.0.1` here and open http://127.0.0.1:8000.

## Design reference

The design follows https://stephanieannpearson.com/: pale blue-gray background, navy and blue palette, Libre Baskerville throughout, a biography beside the complete Dolomites photo on desktop, stacked photo and biography on smaller screens, labeled article cards, category pages, and article pages with PDF links and previous/next navigation. Lolly’s name uses bold Libre Baskerville. All biography text and article materials are Lolly’s; no reference-site photographs, logos, or article copy are included.

Raw source materials remain in the parent workspace outside this repository. Public article summaries are short editorial descriptions based on the supplied scans. Publication dates are omitted where not established. `Ski Cities` is credited to Snow Country, as printed in the supplied scan; `Southern Fried Skiing` is credited to Mountain Sports & Living, as printed in its scan. PDFs retain the supplied originals.

Lolly’s feedback: larger name and Featured Work heading; no separate featured-article spotlight; no homepage View All Science button; contact consists of the email button. The source photograph is displayed in full without cropping.
