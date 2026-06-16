"""Programmatic CSS builder for project ``style.css`` files."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from trunco.components.stylesheet import InlineStyle, Stylesheet

PropertyValue = str | int | float

_UNITLESS_PROPERTIES = frozenset(
    {
        "animation-iteration-count",
        "column-count",
        "fill-opacity",
        "flex-grow",
        "flex-shrink",
        "font-weight",
        "line-height",
        "opacity",
        "order",
        "orphans",
        "stroke-dasharray",
        "stroke-dashoffset",
        "widows",
        "z-index",
        "zoom",
    }
)


def _css_property(name: str) -> str:
    return name.replace("_", "-")


def _css_value(property_name: str, value: PropertyValue) -> str:
    if isinstance(value, (int, float)) and _css_property(property_name) not in _UNITLESS_PROPERTIES:
        return f"{value}px"
    return str(value)


def _format_rule(selector: str, properties: dict[str, PropertyValue]) -> str:
    if not properties:
        return ""
    lines = [f"{selector} {{"]
    for name, value in properties.items():
        lines.append(f"  {_css_property(name)}: {_css_value(name, value)};")
    lines.append("}")
    return "\n".join(lines)


class StyleSheet:
    """Build a project stylesheet in Python and write or embed it as ``style.css``.

    Example::

        sheet = StyleSheet()
        sheet.variables(primary="#3b82f6", body_bg="#ffffff")
        sheet.rule("body", font_family="Inter, sans-serif", margin=0)
        sheet.rule(".card", border_radius=12, padding=16)
        sheet.write("assets/style.css")
        page.add_child(sheet.to_link("assets/style.css"))
    """

    def __init__(self) -> None:
        self._chunks: list[str] = []

    def variables(
        self,
        selector: str = ":root",
        /,
        **properties: PropertyValue,
    ) -> StyleSheet:
        """Declare custom properties on a selector (``:root`` by default)."""
        if properties:
            props = {f"--{_css_property(name)}": value for name, value in properties.items()}
            self._chunks.append(_format_rule(selector, props))
        return self

    def rule(self, selector: str, /, **properties: PropertyValue) -> StyleSheet:
        """Add a CSS rule block."""
        block = _format_rule(selector, properties)
        if block:
            self._chunks.append(block)
        return self

    def raw(self, css: str) -> StyleSheet:
        """Append raw CSS text."""
        text = css.strip()
        if text:
            self._chunks.append(text)
        return self

    @contextmanager
    def media(self, query: str) -> Iterator[StyleSheet]:
        """Nest rules inside a ``@media`` block."""
        inner = StyleSheet()
        yield inner
        body = inner.render()
        if body:
            self._chunks.append(f"@media {query} {{\n{body}\n}}")

    def render(self) -> str:
        """Return the full CSS document."""
        return "\n\n".join(self._chunks)

    def write(self, path: str | Path) -> Path:
        """Write CSS to ``style.css`` (or any path) and return the resolved path."""
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(self.render() + "\n", encoding="utf-8")
        return target.resolve()

    def to_inline(self) -> InlineStyle:
        """Embed this stylesheet in a ``<style>`` tag."""
        return InlineStyle(self.render())

    def to_link(self, href: str) -> Stylesheet:
        """Reference this stylesheet from a ``<link rel=\"stylesheet\">`` tag."""
        return Stylesheet(href)
