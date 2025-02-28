from __future__ import annotations
from trunco.html.base import Component, AttributeEntry


class TextAreaComponent(Component):
    """
    A basic text area component for multi-line text input.
    """

    def __init__(self, rows: int = 4, cols: int = 50, placeholder: str = "", **kwargs):
        super().__init__(tag="textarea", **kwargs)
        self.add(AttributeEntry("rows", str(rows)))
        self.add(AttributeEntry("cols", str(cols)))
        if placeholder:
            self.add(placeholder)
