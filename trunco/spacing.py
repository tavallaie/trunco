"""Spacing helpers for Tailwind gap / layout classes on components."""

from __future__ import annotations

from typing import List, Optional, Union

GapValue = Union[str, int, None]

_GAP_ALIASES = {
    "none": None,
    "xs": "gap-1",
    "sm": "gap-2",
    "md": "gap-3",
    "lg": "gap-4",
    "xl": "gap-6",
    "2xl": "gap-8",
}

_STACK_ALIASES = {
    "none": None,
    "xs": "space-y-1",
    "sm": "space-y-2",
    "md": "space-y-3",
    "lg": "space-y-4",
    "xl": "space-y-6",
    "2xl": "space-y-8",
}


def gap_classes(gap: GapValue) -> List[str]:
    """Resolve a gap token to Tailwind ``gap-*`` utility class names."""
    if gap is None:
        return []
    if isinstance(gap, int):
        return [f"gap-{gap}"]
    if gap in _GAP_ALIASES:
        resolved = _GAP_ALIASES[gap]
        return [resolved] if resolved else []
    if gap.startswith("gap-"):
        return [gap]
    return [f"gap-{gap}"]


def stack_classes(gap: GapValue) -> List[str]:
    """Resolve a gap token to Tailwind ``space-y-*`` utility class names."""
    if gap is None:
        return []
    if isinstance(gap, int):
        return [f"space-y-{gap}"]
    if gap in _STACK_ALIASES:
        resolved = _STACK_ALIASES[gap]
        return [resolved] if resolved else []
    if gap.startswith("space-y-"):
        return [gap]
    return [f"space-y-{gap}"]


def join_classes(*parts: Optional[str]) -> str:
    """Join class name fragments, skipping empty values."""
    return " ".join(part for part in parts if part)
