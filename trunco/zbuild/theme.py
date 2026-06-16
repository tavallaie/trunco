from dataclasses import dataclass

from trunco.base import Component
from trunco.kits.scheme import PaletteRegistry, PaletteScheme, merge_enabled

PALETTES = (
    "zinc",
    "slate",
    "stone",
    "gray",
    "neutral",
    "red",
    "rose",
    "orange",
    "green",
    "blue",
    "yellow",
    "violet",
    "amber",
    "purple",
    "teal",
    "sapphire",
    "ruby",
    "emerald",
    "daylight",
    "midnight",
)

LAYOUTS = ("z-layout-small", "z-layout-medium", "z-layout-large")
MODES = ("light", "dark")

_registry = PaletteRegistry()


@dataclass
class Theme:
    """0build color scheme: palette, layout density, and light/dark mode."""

    palette: str = "sapphire"
    layout: str = "z-layout-small"
    mode: str = "light"

    def classes(self, palette: str | None = None) -> list[str]:
        active_palette = palette or self.palette
        classes = [self.layout]
        if self.mode == "dark":
            classes.append("dark")
        if _registry.has(active_palette):
            classes.append(f"z-theme-{active_palette}")
        return classes

    def style(self) -> str:
        return "--bg: var(--z-bg); --color: var(--z-bg-f)"

    def copy(
        self,
        palette: str | None = None,
        layout: str | None = None,
        mode: str | None = None,
    ) -> "Theme":
        return Theme(
            palette=palette or self.palette,
            layout=layout or self.layout,
            mode=mode or self.mode,
        )

    @property
    def is_custom_palette(self) -> bool:
        return _registry.has(self.palette)


theme = Theme()


def register_palette(
    palette: PaletteScheme | None = None,
    name: str | None = None,
    *,
    light: dict[str, str] | None = None,
    dark: dict[str, str] | None = None,
    set_active: bool = False,
    **light_tokens: str,
) -> PaletteScheme:
    """Register a custom 0build palette (``.z-theme-*`` CSS variables).

    Examples::

        register_palette(
            name="brand",
            light={"primary": "oklch(55% 0.2 240)", "primary-f": "oklch(98% 0 0)"},
            dark={"primary": "oklch(45% 0.18 240)", "primary-f": "oklch(98% 0 0)"},
            set_active=True,
        )
    """
    if palette is None:
        if name is None:
            raise ValueError("register_palette requires a PaletteScheme or palette name")
        palette = PaletteScheme(name=name, light=light or light_tokens, dark=dark or {})
    registered = _registry.register(palette)
    if set_active:
        set_theme(palette=registered.name)
    return registered


def get_custom_palette(name: str) -> PaletteScheme | None:
    return _registry.get(name)


def is_custom_palette(name: str) -> bool:
    return _registry.has(name)


def custom_palette_names() -> list[str]:
    return _registry.names()


def available_palettes(*, enabled: list[str] | None = None) -> list[str]:
    return merge_enabled(PALETTES, _registry.names(), enabled=enabled)


def palette_css() -> str:
    """Return CSS for all registered custom 0build palettes."""
    return _registry.css()


def palette_style_tag() -> str:
    """Return a ``<style>`` tag for all registered custom 0build palettes."""
    return _registry.style_tag()


def set_theme(
    palette: str | None = None,
    layout: str | None = None,
    mode: str | None = None,
) -> Theme:
    """Set the active 0build theme for new ``Page`` wrappers."""
    if palette is not None:
        theme.palette = palette
    if layout is not None:
        theme.layout = layout
    if mode is not None:
        theme.mode = mode
    return theme


def get_theme() -> Theme:
    return theme


class Styles(Component):
    """Inject CSS for all registered custom 0build palettes."""

    def render(self, context=None) -> str:
        return palette_style_tag()


class Page(Component):
    """0build page wrapper that applies palette, layout, and mode classes."""

    def __init__(
        self,
        *children: Component | str,
        palette: str | None = None,
        layout: str | None = None,
        mode: str | None = None,
        extra_classes: list[str] | None = None,
        include_styles: bool = False,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        active = theme.copy(palette=palette, layout=layout, mode=mode)
        self._include_styles = include_styles or _registry.has(active.palette)
        for class_name in active.classes(palette=active.palette):
            self.add_class(class_name)
        if extra_classes:
            for class_name in extra_classes:
                self.add_class(class_name)
        self.add_class("bg")
        self.add_class("color")
        self.add_style("--bg", "var(--z-bg)")
        self.add_style("--color", "var(--z-bg-f)")
        self.add_attribute("data-z-palette", active.palette)
        for child in children:
            self.add_child(child)

    def render(self, context=None) -> str:
        html = super().render(context)
        if self._include_styles:
            return palette_style_tag() + html
        return html
