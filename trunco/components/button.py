from typing import Optional, Union

from trunco.base import Component
from trunco.enums import Attribute


class ButtonComponent(Component):
    """
    A basic button component that can be customized with a label and onClick action.
    """

    def __init__(
        self,
        label: str = "{label}",
        on_click: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(tag="button", **kwargs)
        self.add_attribute(Attribute.TYPE, "button")
        self.children.append(label)
        if on_click:
            self.add_directive("x-on:click", on_click)

    def add_alpine_directive(self, directive: Union[str, object], expression: str):
        """Add an Alpine.js directive with typed helpers."""
        self.add_directive(directive, expression)
