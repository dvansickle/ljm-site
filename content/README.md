# Article catalog

Edit `articles.json` and run `python3 scripts/build.py` from the repository root. Each article has a title, publication, category, short editorial summary, PDF, complete first-page preview, card thumbnail, and PDF size. `source` records the original filename for editorial traceability; it is not a public download path.

Use the three existing category slugs unless also updating `CATEGORIES` in the generator. Add the corresponding PDF and preview assets before rebuilding. Keep private drafts and original photos outside the public repository.
