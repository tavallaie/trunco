from typing import Optional

from trunco.alpine.enums import Directive
from trunco.components.button import ButtonComponent
from trunco.kits.color import resolve_color


class DaisyButton(ButtonComponent):
    """DaisyUI-styled button component."""

    VARIANTS = (
        "primary",
        "secondary",
        "accent",
        "neutral",
        "info",
        "success",
        "warning",
        "error",
        "ghost",
        "link",
    )
    SIZES = ("lg", "md", "sm", "xs")

    def __init__(
        self,
        label: str = "{label}",
        on_click: Optional[str] = None,
        color: Optional[str] = None,
        variant: str = "primary",
        size: Optional[str] = None,
        outline: bool = False,
        **kwargs,
    ):
        super().__init__(label=label, on_click=on_click, **kwargs)
        tone = resolve_color(color=color, variant=variant, default="primary")
        self.add_class("btn")
        if tone in self.VARIANTS:
            self.add_class(f"btn-{tone}")
        if outline:
            self.add_class("btn-outline")
        if size in self.SIZES:
            self.add_class(f"btn-{size}")

    def add_alpine_directive(self, directive: Directive, expression: str):
        self.add_directive(directive, expression)