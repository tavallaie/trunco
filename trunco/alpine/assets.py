ALPINE_CDN_URL = "https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"


def alpine_script_tag(url: str = ALPINE_CDN_URL) -> str:
    """Return an Alpine.js script tag for inclusion in HTML templates."""
    return f'<script src="{url}" defer></script>'