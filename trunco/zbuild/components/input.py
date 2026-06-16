from typing import Optional

from trunco.components.input import InputComponent


class ZbuildInput(InputComponent):
    """0build Kit input component using z-* classes."""

    SIZES = ("xsmall", "small", "medium", "large")

    def __init__(
        self,
        input_type: str = "text",
        placeholder: str = "",
        value: str = "",
        size: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            input_type=input_type,
            placeholder=placeholder,
            value=value,
            **kwargs,
        )
        self.add_class("z-input")
        if size in self.SIZES:
            self.add_class(f"z-form-{size}")
