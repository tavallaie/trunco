"""Shared color-scheme helpers for kit theme registries."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field


def _slug(name: str) -> str:
    cleaned = name.strip().lower().replace(" ", "-")
    if not cleaned or not cleaned.replace("-", "").isalnum():
        raise ValueError(f"Invalid theme name: {name!r}")
    return cleaned


def _normalize_var_name(key: str, *, prefix: str) -> str:
    normalized = key.strip().replace("_", "-")
    if normalized.startswith("--"):
        return normalized
    if normalized.startswith(f"{prefix}-"):
        return f"--{normalized}"
    return f"--{prefix}-{normalized}"


def _format_declarations(variables: dict[str, str], color_scheme: str | None = None) -> str:
    lines: list[str] = []
    if color_scheme is not None:
        lines.append(f"  color-scheme: {color_scheme};")
    for name in sorted(variables):
        lines.append(f"  {name}: {variables[name]};")
    return "\n".join(lines)


@dataclass
class ColorScheme:
    """User-defined color tokens, similar to daisyUI ``@plugin \"daisyui/theme\"``."""

    name: str
    colors: dict[str, str] = field(default_factory=dict)
    color_scheme: str = "light"
    default: bool = False
    prefers_dark: bool = False
    extends: str | None = None
    tokens: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.name = _slug(self.name)

    def variables(self, *, prefix: str = "color") -> dict[str, str]:
        variables: dict[str, str] = {}
        for key, value in self.colors.items():
            variables[_normalize_var_name(key, prefix=prefix)] = value
        for key, value in self.tokens.items():
            token = key.strip().replace("_", "-")
            if token.startswith("--"):
                variables[token] = value
            else:
                variables[f"--{token}"] = value
        return variables

    def daisy_selector(self) -> str:
        return (
            f':root:has(input.theme-controller[value="{self.name}"]:checked), '
            f'[data-theme="{self.name}"]'
        )

    def to_daisy_css(self) -> str:
        declarations = _format_declarations(
            self.variables(prefix="color"),
            color_scheme=self.color_scheme,
        )
        return f"{self.daisy_selector()} {{\n{declarations}\n}}"

    def to_tailwind_theme_css(self, selector: str = ":root") -> str:
        """Tailwind v4-style ``@theme`` block for custom colors."""
        declarations = _format_declarations(self.variables(prefix="color"))
        return f"@theme {{\n{declarations}\n}}"

    def to_style_tag(self) -> str:
        return f"<style>\n{self.to_daisy_css()}\n</style>"


@dataclass
class PaletteScheme:
    """User-defined 0build palette with optional light/dark token sets."""

    name: str
    light: dict[str, str] = field(default_factory=dict)
    dark: dict[str, str] = field(default_factory=dict)
    layout: str | None = None

    def __post_init__(self) -> None:
        self.name = _slug(self.name)

    def _z_variables(self, mapping: dict[str, str]) -> dict[str, str]:
        variables: dict[str, str] = {}
        for key, value in mapping.items():
            normalized = key.strip().replace("_", "-")
            if normalized.startswith("--"):
                variables[normalized] = value
            elif normalized.startswith("z-"):
                variables[f"--{normalized}"] = value
            else:
                variables[f"--z-{normalized}"] = value
        return variables

    def to_zbuild_css(self) -> str:
        blocks: list[str] = []
        if self.light:
            declarations = _format_declarations(self._z_variables(self.light))
            blocks.append(f".z-theme-{self.name} {{\n{declarations}\n}}")
        if self.dark:
            declarations = _format_declarations(self._z_variables(self.dark))
            blocks.append(f".dark.z-theme-{self.name} {{\n{declarations}\n}}")
        return "\n\n".join(blocks)

    def to_style_tag(self) -> str:
        css = self.to_zbuild_css()
        if not css:
            return ""
        return f"<style>\n{css}\n</style>"


class SchemeRegistry:
    """In-memory registry for custom color schemes."""

    def __init__(self) -> None:
        self._schemes: dict[str, ColorScheme] = {}

    def register(self, scheme: ColorScheme) -> ColorScheme:
        self._schemes[scheme.name] = scheme
        return scheme

    def register_colors(
        self,
        name: str,
        colors: dict[str, str] | None = None,
        *,
        color_scheme: str = "light",
        extends: str | None = None,
        **tokens: str,
    ) -> ColorScheme:
        scheme = ColorScheme(
            name=name,
            colors=colors or {},
            color_scheme=color_scheme,
            extends=extends,
            tokens=tokens,
        )
        return self.register(scheme)

    def get(self, name: str) -> ColorScheme | None:
        return self._schemes.get(_slug(name))

    def has(self, name: str) -> bool:
        return _slug(name) in self._schemes

    def names(self) -> list[str]:
        return sorted(self._schemes)

    def css(self) -> str:
        return "\n\n".join(scheme.to_daisy_css() for scheme in self._schemes.values())

    def style_tag(self) -> str:
        css = self.css()
        if not css:
            return ""
        return f"<style>\n{css}\n</style>"


class PaletteRegistry:
    """In-memory registry for custom 0build palettes."""

    def __init__(self) -> None:
        self._palettes: dict[str, PaletteScheme] = {}

    def register(self, palette: PaletteScheme) -> PaletteScheme:
        self._palettes[palette.name] = palette
        return palette

    def register_palette(
        self,
        name: str,
        *,
        light: dict[str, str] | None = None,
        dark: dict[str, str] | None = None,
        **light_tokens: str,
    ) -> PaletteScheme:
        palette = PaletteScheme(
            name=name,
            light=light or light_tokens,
            dark=dark or {},
        )
        return self.register(palette)

    def get(self, name: str) -> PaletteScheme | None:
        return self._palettes.get(_slug(name))

    def has(self, name: str) -> bool:
        return _slug(name) in self._palettes

    def names(self) -> list[str]:
        return sorted(self._palettes)

    def css(self) -> str:
        return "\n\n".join(
            palette.to_zbuild_css()
            for palette in self._palettes.values()
            if palette.to_zbuild_css()
        )

    def style_tag(self) -> str:
        css = self.css()
        if not css:
            return ""
        return f"<style>\n{css}\n</style>"


def merge_enabled(
    built_in: Iterable[str],
    custom: Iterable[str],
    *,
    enabled: Iterable[str] | None = None,
) -> list[str]:
    """Merge built-in and custom theme names, optionally filtering enabled set."""
    names = list(dict.fromkeys([*built_in, *custom]))
    if enabled is None:
        return names
    allowed = {_slug(name) for name in enabled}
    return [name for name in names if _slug(name) in allowed]
