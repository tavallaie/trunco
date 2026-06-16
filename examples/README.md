# Trunco Examples

Runnable examples demonstrating core components, integrations, UI kits, and framework usage.

## Run

From the repository root:

```bash
uv sync
uv pip install -e .
uv run python examples/01_core_basics.py
```

## Index

| File | Description |
|------|-------------|
| `01_core_basics.py` | Core HTML components without a UI kit |
| `02_context_rendering.py` | Dynamic `{placeholder}` rendering |
| `03_alpine_htmx.py` | Alpine.js and HTMX integrations |
| `04_daisy_kit.py` | DaisyUI kit with short imports |
| `05_zbuild_kit.py` | 0build (zbuild) kit |
| `06_custom_themes.py` | Custom color schemes |
| `07_kit_swap.py` | Same API, different kit import |
| `flask_app.py` | Flask integration |
| `fastapi_app.py` | FastAPI integration |

## Documentation

The full docs site is built with Trunco itself — see `docs/build.py`.