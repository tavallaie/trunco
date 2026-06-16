from typing import Optional

from trunco.base import Component
from trunco.enums import Attribute
from trunco.kits.color import resolve_color


class ZbuildButton(Component):
    """0build Kit button component using z-* classes."""

    STYLES = (
        "default",
        "ghost",
        "primary",
        "secondary",
        "success",
        "warning",
        "info",
        "danger",
        "text",
    )
    SIZES = ("xsmall", "small", "medium", "large")

    def __init__(
        self,
        label: str = "{label}",
        color: Optional[str] = None,
        style: str = "default",
        size: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(tag="button", **kwargs)
        self.add_attribute(Attribute.TYPE, "button")
        tone = resolve_color(color=color, variant=style, default="default")
        self.add_class("z-button")
        if tone in self.STYLES:
            self.add_class(f"z-button-{tone}")
        if size in self.SIZES:
            self.add_class(f"z-button-{size}")
        self.add_child(label)