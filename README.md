# Trunco

**Trunco** is a Python framework for building dynamic, reusable HTML components. It integrates with Django, Flask, FastAPI, and other web frameworks, with optional DaisyUI and 0build (formerly Franken UI) kits.

## Features

- **Component-based architecture** — composable Python objects render to HTML
- **Optional integrations** — Alpine.js, HTMX, UIKit via extras
- **UI kits** — `trunco.daisy` and `trunco.zbuild` with unified short imports (`Form`, `Button`, `Alert`, …)
- **Custom themes** — register your own color schemes like DaisyUI/Tailwind
- **Zero runtime dependencies** — core install is dependency-free

## Installation

```bash
uv pip install trunco
uv pip install "trunco[daisy,zbuild,alpine,htmx]"
```

## Quickstart

```python
from trunco.daisy import Form, FormControl, Input, Button, Alert, Page

form = Form(action="/save")
form.add_child(FormControl(label="Email", field=Input(placeholder="you@example.com")))
form.add_child(Button(label="Save", color="primary"))
form.add_child(Alert(message="Ready", color="info"))

print(Page(form, theme_name="light").render())
```

Swap kits by changing one import:

```python
import trunco.daisy as ui   # or: import trunco.zbuild as ui
```

## Documentation

The docs site is **built with Trunco** and deployed to GitHub Pages.

```bash
uv pip install -e ".[daisy]"
uv run python docs/serve.py   # preview at http://127.0.0.1:8000
uv run python docs/build.py   # build only → docs/_site/
```

| Resource | Location |
|----------|----------|
| Live docs | GitHub Pages (after deploy) |
| Site source | [`docs/src/`](docs/src/) |
| Build script | [`docs/build.py`](docs/build.py) |
| Legacy markdown | [`docs/archive/`](docs/archive/) |

## Examples

Runnable examples in [`examples/`](examples/):

```bash
uv run python examples/01_core_basics.py
uv run python examples/04_daisy_kit.py
uv run python examples/07_kit_swap.py
```

## Development

```bash
uv sync
uv pip install -e ".[daisy,zbuild,alpine,htmx]"
uv run pytest
uv run python docs/build.py
```

## License

MIT — see [LICENSE](LICENSE).