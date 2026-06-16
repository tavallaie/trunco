from trunco.components.input import InputComponent
from trunco.kits.color import resolve_color


class DaisyInput(InputComponent):
    """DaisyUI-styled input component."""

    VARIANTS = ("bordered", "ghost")
    SIZES = ("lg", "md", "sm", "xs")

    def __init__(
        self,
        input_type: str = "text",
        placeholder: str = "",
        value: str = "",
        color: str | None = None,
        variant: str = "bordered",
        size: str | None = None,
        **kwargs,
    ):
        super().__init__(
            input_type=input_type,
            placeholder=placeholder,
            value=value,
            **kwargs,
        )
        tone = resolve_color(color=color, variant=variant, default="bordered")
        self.add_class("input")
        if tone in self.VARIANTS:
            self.add_class(f"input-{tone}")
        if size in self.SIZES:
            self.add_class(f"input-{size}")
