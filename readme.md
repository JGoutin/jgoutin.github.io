# JGoutin-dev Website

Zensical (MkDocs-Material fork) bilingual EN/FR vitrine site deployed to GitHub Pages.

## Structure

- `docs/en/` — English content
- `docs/fr/` — French content
- `docs/_root/` — Root files (CNAME, robots.txt, assets)
- `docs_hooks/build.py` — Build orchestration (zensical build, JSON-LD injection, llms.txt, CV PDF rendering)
- `zensical.en.toml` — English site config
- `zensical.fr.toml` — French site config
- `.github/workflows/pages.yml` — GitHub Actions deployment

## Tech stack

- Python project using `uv` (see `pyproject.toml`)
- Zensical (MkDocs-Material fork) for static site generation
- Pandoc + WeasyPrint for CV PDF rendering

## Build locally

```bash
uv sync --group docs
uv run python -m docs_hooks.build
```

## Deploy

Automatic via GitHub Actions on push to main branch (`.github/workflows/pages.yml`).

## License

### All rights reserved Content

All site content (text, photos, CV) is **all rights reserved**.

### CC0 (build/config)

The following are dedicated to the public domain under CC0 1.0:

- Build scripts (`docs_hooks/build.py`)
- Site configuration (`zensical.*.toml`)
- GitHub Actions workflows (`.github/workflows/*`)
- Custom styles (`docs/_root/assets/stylesheets/extra.css`)

### Icons

SVG icons are from Material Icons and FontAwesome via Zensical themes, licensed by their respective authors.