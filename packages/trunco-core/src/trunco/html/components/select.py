from trunco.html.base import Component, AttributeEntry
from trunco.html.enums import Attribute
from typing import List


class OptionComponent(Component):
    """
    A basic option component for the select dropdown.
    """

    def __init__(
        self, value: str, display_text: str = None, selected: bool = False, **kwargs
    ):
        super().__init__(tag="option", **kwargs)
        self.add(AttributeEntry(Attribute.VALUE, value))
        if selected:
            self.add(AttributeEntry(Attribute.SELECTED, "selected"))
        self.add(display_text or value)


class SelectComponent(Component):
    """
    A basic select component with multiple options.
    """

    def __init__(self, options: List[OptionComponent] = None, **kwargs):
        super().__init__(tag="select", **kwargs)
        if options:
            for option in options:
                self.add(option)
