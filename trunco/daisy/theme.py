from dataclasses import dataclass
from typing import Dict, List, Optional, Union

from trunco.base import Component
from trunco.kits.scheme import ColorScheme, SchemeRegistry, merge_enabled

THEME_NAMES = (
    "light",
    "dark",
    "cupcake",
    "bumblebee",
    "emerald",
    "corporate",
    "synthwave",
    "retro",
    "cyberpunk",
    "valentine",
    "halloween",
    "garden",
    "forest",
    "aqua",
    "lofi",
    "pastel",
    "fantasy",
    "wireframe",
    "black",
    "luxury",
    "dracula",
    "cmyk",
    "autumn",
    "business",
    "acid",
    "lemonade",
    "night",
    "coffee",
    "winter",
    "dim",
    "nord",
    "sunset",
    "caramellatte",
    "abyss",
    "silk",
)

_registry = SchemeRegistry()


@dataclass
class Theme:
    """DaisyUI color scheme applied via ``data-theme``."""

    name: str = "light"

    def apply(self, component: Component) -> None:
        component.add_attribute("data-theme", self.name)

    def copy(self, name: Optional[str] = None) -> "Theme":
        return Theme(name=name or self.name)

    @property
    def is_custom(self) -> bool:
        return _registry.has(self.name)


theme = Theme()


def register_theme(
    scheme: Optional[ColorScheme] = None,
    name: Optional[str] = None,
    colors: Optional[Dict[str, str]] = None,
    *,
    color_scheme: str = "light",
    extends: Optional[str] = None,
    set_active: bool = False,
    **tokens: str,
) -> ColorScheme:
    """Register a custom daisyUI theme (like ``@plugin \"daisyui/theme\"``).

    Examples::

        register_theme(
            name="brand",
            colors={"primary": "#1EA1F1", "secondary": "teal", "base-100": "#f8fafc"},
            color_scheme="light",
            set_active=True,
        )

        register_theme(ColorScheme(name="brand", colors={...}))
    """
    if scheme is None:
        if name is None:
            raise ValueError("register_theme requires a ColorScheme or a theme name")
        scheme = ColorScheme(
            name=name,
            colors=colors or {},
            color_scheme=color_scheme,
            extends=extends,
            tokens=tokens,
        )
    registered = _registry.register(scheme)
    if set_active:
        set_theme(registered.name)
    return registered


def get_custom_theme(name: str) -> Optional[ColorScheme]:
    return _registry.get(name)


def is_custom_theme(name: str) -> bool:
    return _registry.has(name)


def custom_theme_names() -> List[str]:
    return _registry.names()


def available_themes(*, enabled: Optional[List[str]] = None) -> List[str]:
    return merge_enabled(THEME_NAMES, _registry.names(), enabled=enabled)


def theme_css() -> str:
    """Return CSS for all registered custom daisyUI themes."""
    return _registry.css()


def theme_style_tag() -> str:
    """Return a ``<style>`` tag for all registered custom daisyUI themes."""
    return _registry.style_tag()


def set_theme(name: str) -> Theme:
    """Set the active DaisyUI theme for new ``Page`` wrappers."""
    theme.name = name
    return theme


def get_theme() -> Theme:
    return theme


class Styles(Component):
    """Inject CSS for all registered custom daisyUI themes."""

    def render(self, context=None) -> str:
        return theme_style_tag()


class Page(Component):
    """DaisyUI page wrapper that applies the active color scheme."""

    def __init__(
        self,
        *children: Union[Component, str],
        theme_name: Optional[str] = None,
        extra_classes: Optional[List[str]] = None,
        include_styles: bool = False,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        active = theme_name or theme.name
        self._include_styles = include_styles or _registry.has(active)
        self.add_attribute("data-theme", active)
        if extra_classes:
            for class_name in extra_classes:
                self.add_class(class_name)
        for child in children:
            self.add_child(child)

    def render(self, context=None) -> str:
        html = super().render(context)
        if self._include_styles:
            return theme_style_tag() + html
        return html