#!/usr/bin/env python3
"""Build and preview the Trunco docs site on your local machine."""

from __future__ import annotations

import argparse
import http.server
import socketserver
import sys
import threading
import time
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from docs.build import main as build_site

SITE_DIR = Path(__file__).parent / "_site"
WATCH_PATHS = (
    Path(__file__).parent / "src",
    Path(__file__).parent / "assets",
    Path(__file__).parent / "build.py",
)


def _snapshot() -> float:
    latest = 0.0
    for base in WATCH_PATHS:
        if not base.exists():
            continue
        paths = [base] if base.is_file() else base.rglob("*")
        for path in paths:
            if path.is_file():
                latest = max(latest, path.stat().st_mtime)
    return latest


def _watch_and_rebuild(interval: float, stop: threading.Event) -> None:
    last = _snapshot()
    while not stop.is_set():
        time.sleep(interval)
        current = _snapshot()
        if current > last:
            last = current
            print("\n[docs] Changes detected — rebuilding…")
            build_site()
            print("[docs] Rebuild complete.\n")


def serve(host: str, port: int) -> None:
    handler = partial_handler(SITE_DIR)
    with socketserver.TCPServer((host, port), handler) as httpd:
        httpd.serve_forever()


def partial_handler(directory: Path):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(directory), **kwargs)

        def log_message(self, format: str, *args) -> None:
            print(f"[docs] {self.address_string()} - {format % args}")

    return Handler


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview Trunco docs locally")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Port (default: 8000)")
    parser.add_argument(
        "--no-build", action="store_true", help="Serve existing _site without rebuilding"
    )
    parser.add_argument("--no-open", action="store_true", help="Do not open a browser tab")
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Rebuild automatically when docs/src or docs/assets change",
    )
    args = parser.parse_args()

    if not args.no_build:
        build_site()
    elif not SITE_DIR.exists():
        print("No docs/_site found. Run without --no-build first.")
        sys.exit(1)

    url = f"http://{args.host}:{args.port}/"
    stop = threading.Event()

    if args.watch:
        watcher = threading.Thread(
            target=_watch_and_rebuild,
            args=(1.0, stop),
            daemon=True,
        )
        watcher.start()

    print(f"\n[docs] Preview at {url}")
    print("[docs] Press Ctrl+C to stop.\n")

    if not args.no_open:
        webbrowser.open(url)

    try:
        serve(args.host, args.port)
    except KeyboardInterrupt:
        print("\n[docs] Stopped.")
    finally:
        stop.set()


if __name__ == "__main__":
    main()
