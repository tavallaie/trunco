from trunco.html.base import Component, AttributeEntry
from trunco.html.enums import Attribute


class LabelComponent(Component):
    """
    A basic label component for input fields.
    """

    def __init__(self, text: str = "{text}", for_input_id: str = "", **kwargs):
        super().__init__(tag="label", **kwargs)
        self.add(text)
        if for_input_id:
            self.add(AttributeEntry(Attribute.FOR, for_input_id))
