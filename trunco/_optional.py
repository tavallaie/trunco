"""Helpers for optional Trunco integration and UI-kit extras."""

from __future__ import annotations

import os
from typing import FrozenSet

_EXTRA_ALIASES = {
    "alpine": "alpine",
    "htmx": "htmx",
    "uikit": "uikit",
    "uikit3": "uikit",
    "daisy": "daisy",
    "zbuild": "zbuild",
    "0build": "zbuild",
    "franken": "franken",
    "all": "all",
}

_KIT_REQUIRES: dict[str, FrozenSet[str]] = {
    "daisy": frozenset({"alpine"}),
    "zbuild": frozenset({"uikit"}),
    "franken": frozenset({"zbuild", "uikit"}),
}


def _normalize_extra(name: str) -> str:
    normalized = _EXTRA_ALIASES.get(name.lower())
    if normalized is None:
        raise ValueError(f"Unknown Trunco extra: {name}")
    return normalized


def _enabled_extras() -> FrozenSet[str]:
    configured = os.environ.get("TRUNCO_EXTRAS", "")
    if not configured:
        return frozenset()
    return frozenset(
        _normalize_extra(item.strip())
        for item in configured.split(",")
        if item.strip()
    )


def require_extra(extra: str) -> None:
    """Raise ImportError when strict extra checking is enabled and an extra is missing."""
    if os.environ.get("TRUNCO_STRICT_EXTRAS") != "1":
        return

    normalized = _normalize_extra(extra)
    enabled = _enabled_extras()
    if not enabled or normalized in enabled or "all" in enabled:
        return

    missing = {normalized, *_KIT_REQUIRES.get(normalized, frozenset())}
    missing -= enabled
    if not missing:
        return

    extras = ", ".join(sorted(missing))
    raise ImportError(
        f"Trunco extra '{normalized}' is required. Install with: pip install trunco[{extras}]"
    )