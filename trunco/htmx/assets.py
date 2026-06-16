HTMX_CDN_URL = "https://unpkg.com/htmx.org@2.0.4"


def htmx_script_tag(url: str = HTMX_CDN_URL) -> str:
    """Return an HTMX script tag for inclusion in HTML templates."""
    return f'<script src="{url}"></script>'