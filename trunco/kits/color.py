def resolve_color(
    color: str | None = None,
    variant: str | None = None,
    default: str | None = None,
) -> str | None:
    """Resolve unified ``color`` API over kit-specific ``variant``/``style`` names."""
    if color is not None:
        return color
    if variant is not None:
        return variant
    return default
