"""0build Kit CDN asset helpers (formerly Franken UI / Frankenstyle)."""

ZBUILD_VERSION = "0.4.5"
ZBUILD_CDN_BASE = f"https://cdn.jsdelivr.net/gh/0builddotdev/0build@{ZBUILD_VERSION}"

KIT_CSS_URL = f"{ZBUILD_CDN_BASE}/dist/css/kit.min.css"
CHART_CSS_URL = f"{ZBUILD_CDN_BASE}/dist/css/chart.min.css"
CORE_JS_URL = f"{ZBUILD_CDN_BASE}/dist/js/hwc/core.iife.js"
ZUIKIT_JS_URL = f"{ZBUILD_CDN_BASE}/dist/js/uikit.min.js"
RUNTIME_JS_URL = f"{ZBUILD_CDN_BASE}/dist/js/runtime.iife.js"
ICON_JS_URL = f"{ZBUILD_CDN_BASE}/dist/js/hwc/icon.iife.js"
CHART_JS_URL = f"{ZBUILD_CDN_BASE}/dist/js/hwc/chart.iife.js"
COMPONENTS_JS_URL = f"{ZBUILD_CDN_BASE}/dist/js/hwc/components.iife.js"


def kit_css_tag(url: str = KIT_CSS_URL) -> str:
    """Return the 0build Kit stylesheet link tag."""
    return f'<link rel="stylesheet" href="{url}">'


def chart_css_tag(url: str = CHART_CSS_URL) -> str:
    """Return the 0build chart stylesheet link tag."""
    return f'<link rel="stylesheet" href="{url}">'


def core_script_tag(url: str = CORE_JS_URL) -> str:
    """Return the 0build core script tag (load in <head>)."""
    return f'<script src="{url}" type="module"></script>'


def zuikit_script_tag(url: str = ZUIKIT_JS_URL) -> str:
    """Return the zUIkit script tag (separate from core since v0.4.5)."""
    return f'<script src="{url}"></script>'


def runtime_script_tag(url: str = RUNTIME_JS_URL) -> str:
    """Return the 0build runtime script tag."""
    return f'<script src="{url}" type="module"></script>'


def icon_script_tag(url: str = ICON_JS_URL) -> str:
    """Return the 0build icon script tag."""
    return f'<script src="{url}" type="module"></script>'


def chart_script_tag(url: str = CHART_JS_URL) -> str:
    """Return the 0build chart script tag."""
    return f'<script src="{url}" type="module"></script>'


def components_script_tag(url: str = COMPONENTS_JS_URL) -> str:
    """Return the 0build components script tag (load last)."""
    return f'<script src="{url}" type="module"></script>'


def theme_init_script() -> str:
    """Return inline script that applies 0build theme classes to <html>."""
    return """<script>
  const htmlElement = document.documentElement;
  const __Z_THEME__ = JSON.parse(localStorage.getItem("__Z_THEME__") || "{}");
  if (
    __Z_THEME__.mode === "dark" ||
    (!__Z_THEME__.mode && window.matchMedia("(prefers-color-scheme: dark)").matches)
  ) {
    htmlElement.classList.add("dark");
  } else {
    htmlElement.classList.remove("dark");
  }
  htmlElement.classList.add(__Z_THEME__.layout || "z-layout-small");
</script>"""