from trunco.base import Component
from trunco.enums import Attribute


class LabelComponent(Component):
    """
    A basic label component for input fields.
    """

    def __init__(self, text: str = "{text}", for_input_id: str = "", **kwargs):
        super().__init__(tag="label", **kwargs)
        self.children.append(text)
        if for_input_id:
            self.add_attribute(Attribute.FOR, for_input_id)
