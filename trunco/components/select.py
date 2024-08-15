from trunco import Component, Attribute
from typing import List


class OptionComponent(Component):
    """
    A basic option component for the select dropdown.
    """

    def __init__(
        self, value: str, display_text: str = None, selected: bool = False, **kwargs
    ):
        super().__init__(tag="option", **kwargs)
        self.add_attribute(Attribute.VALUE, value)  # Use the enum here
        if selected:
            self.add_attribute(Attribute.SELECTED, "selected")  # Use the enum here
        self.children.append(display_text or value)


class SelectComponent(Component):
    """
    A basic select component with multiple options.
    """

    def __init__(self, options: List[OptionComponent] = None, **kwargs):
        super().__init__(tag="select", **kwargs)
        if options:
            self.children.extend(options)
