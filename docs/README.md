# Trunco Documentation Site

This directory contains the **Trunco-powered** static documentation site.

## Structure

```
docs/
  build.py          # Run to generate HTML
  src/              # Site builder + page definitions (uses Trunco)
  assets/           # CSS and static assets
  _site/            # Generated HTML (deployed to GitHub Pages)
  archive/          # Legacy markdown docs
```

## Preview locally (before pushing)

```bash
uv sync
uv pip install -e .
uv run python docs/serve.py
```

This builds the site, starts a local server at **http://127.0.0.1:8000**, and opens your browser.

Options:

```bash
uv run python docs/serve.py --watch      # auto-rebuild on file changes
uv run python docs/serve.py --port 3000  # custom port
uv run python docs/serve.py --no-open    # don't open browser
```

## Build only (no server)

```bash
uv run python docs/build.py
```

## GitHub Pages

The workflow in `.github/workflows/pages.yml` builds and deploys `docs/_site` on every push to `main`.