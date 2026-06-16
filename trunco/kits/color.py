from typing import Optional


def resolve_color(
    color: Optional[str] = None,
    variant: Optional[str] = None,
    default: Optional[str] = None,
) -> Optional[str]:
    """Resolve unified ``color`` API over kit-specific ``variant``/``style`` names."""
    if color is not None:
        return color
    if variant is not None:
        return variant
    return default
