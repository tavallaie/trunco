#!/usr/bin/env python3
"""Build the Trunco documentation site into docs/_site."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from docs.src.builder import SiteBuilder
from docs.src.pages import PAGES


def main() -> None:
    output = Path(__file__).parent / "_site"
    builder = SiteBuilder(output)
    for slug, title, build_fn in PAGES:
        builder.add_page(slug, title, build_fn)
    builder.build()
    print(f"Built {len(PAGES)} pages → {output}")


if __name__ == "__main__":
    main()