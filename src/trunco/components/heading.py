from trunco.base import Component
from dataclasses import dataclass


@dataclass
class HeadingComponent(Component):
    """
    A basic heading component (h1, h2, h3, etc.).
    """

    def __init__(self, tag: str = "h1", text: str = "{text}", **kwargs):
        if tag not in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            raise ValueError("Invalid tag for heading. Must be one of 'h1' to 'h6'.")
        super().__init__(tag=tag, **kwargs)
        self.children.append(text)
