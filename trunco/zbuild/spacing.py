"""0build-compatible spacing helpers.

The 0build kit uses ``display-flex`` for flexbox (``.flex`` is only flex-grow).
Use ``display-flex`` / ``flex-row`` / ``flex-col`` with inline ``gap`` styles.
"""

from __future__ import annotations

from typing import List, Optional, Union

from trunco.base import Component

GapValue = Union[str, int, None]

_GAP_REM = {
    "none": None,
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "0.75rem",
    "lg": "1rem",
    "xl": "1.5rem",
    "2xl": "2rem",
}


def resolve_gap(gap: GapValue) -> Optional[str]:
    """Resolve a gap token to a CSS length for inline ``gap`` styles."""
    if gap is None:
        return None
    if isinstance(gap, int):
        return f"{gap * 0.25}rem"
    if gap in _GAP_REM:
        return _GAP_REM[gap]
    if gap.startswith("gap-"):
        suffix = gap.split("-", 1)[1]
        try:
            return f"{int(suffix) * 0.25}rem"
        except ValueError:
            return suffix
    return gap


def apply_gap(component: Component, gap: GapValue) -> None:
    """Apply ``gap`` as an inline style on a 0build layout container."""
    value = resolve_gap(gap)
    if value:
        component.add_style("gap", value)


def layout_classes(direction: str) -> List[str]:
    """Return kit flex classes for vertical or horizontal stacks."""
    if direction == "horizontal":
        return ["display-flex", "flex-row", "flex-wrap", "items-center", "justify-center"]
    return ["display-flex", "flex-col"]


def control_wrapper_open(gap: GapValue, *, inline: bool = True) -> str:
    """Opening tag for a labeled control row (radio, checkbox, toggle)."""
    display = "display-inline-flex" if inline else "display-flex"
    value = resolve_gap(gap)
    if value:
        return f'<div class="{display} items-center" style="gap: {value};">'
    return f'<div class="{display} items-center">'


def apply_margin_bottom(component: Component, gap: GapValue) -> None:
    """Apply ``margin-bottom`` for stacked 0build form fields."""
    value = resolve_gap(gap)
    if value:
        component.add_style("margin-bottom", value)