"""zUIkit asset helpers backed by the 0build CDN."""

import warnings

from trunco.zbuild.assets import ZUIKIT_JS_URL, zuikit_script_tag as _zuikit_script_tag

# Legacy npm UIKit 3 URLs (pre-0build migration).
UIKIT_CSS_URL = "https://cdn.jsdelivr.net/npm/uikit@3/dist/css/uikit.min.css"
UIKIT_JS_URL = "https://cdn.jsdelivr.net/npm/uikit@3/dist/js/uikit.min.js"
UIKIT_ICONS_URL = "https://cdn.jsdelivr.net/npm/uikit@3/dist/js/uikit-icons.min.js"


def zuikit_script_tag(url: str = ZUIKIT_JS_URL) -> str:
    """Return the zUIkit script tag from the 0build CDN."""
    return _zuikit_script_tag(url)


def uikit_css_tag(url: str = UIKIT_CSS_URL) -> str:
    """Return a legacy UIkit 3 stylesheet link tag."""
    warnings.warn(
        "uikit_css_tag is deprecated; use trunco.zbuild.kit_css_tag for 0build Kit.",
        DeprecationWarning,
        stacklevel=2,
    )
    return f'<link rel="stylesheet" href="{url}">'


def uikit_js_tag(url: str = UIKIT_JS_URL) -> str:
    """Return a legacy UIkit 3 JavaScript script tag."""
    warnings.warn(
        "uikit_js_tag is deprecated; use trunco.zbuild.zuikit_script_tag for zUIkit.",
        DeprecationWarning,
        stacklevel=2,
    )
    return f'<script src="{url}"></script>'


def uikit_icons_tag(url: str = UIKIT_ICONS_URL) -> str:
    """Return a legacy UIkit Icons JavaScript script tag."""
    warnings.warn(
        "uikit_icons_tag is deprecated; use trunco.zbuild.icon_script_tag for 0build icons.",
        DeprecationWarning,
        stacklevel=2,
    )
    return f'<script src="{url}"></script>'