#!/usr/bin/env python3
"""Preview the pure HTML prototype at http://127.0.0.1:8000"""

from __future__ import annotations

import argparse
import http.server
import socketserver
import webbrowser
from functools import partial
from pathlib import Path

ROOT = Path(__file__).parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve Trunco docs prototype")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--no-open", action="store_true")
    args = parser.parse_args()

    from build import main as build_pages

    build_pages()

    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    url = f"http://127.0.0.1:{args.port}/"
    print(f"\n[prototype] {url}")
    print("[prototype] Pure DaisyUI + HTMX — press Ctrl+C to stop.\n")

    if not args.no_open:
        webbrowser.open(url)

    with socketserver.TCPServer(("127.0.0.1", args.port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[prototype] Stopped.")


if __name__ == "__main__":
    main()
