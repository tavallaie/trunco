from trunco.html.base import Component, AttributeEntry
from trunco.html.enums import Attribute


class InputComponent(Component):
    """
    A basic input component for capturing user input.
    """

    def __init__(
        self, input_type: str = "text", placeholder: str = "", value: str = "", **kwargs
    ):
        super().__init__(tag="input", **kwargs)
        self.add(AttributeEntry(Attribute.TYPE, input_type))
        if placeholder:
            self.add(AttributeEntry(Attribute.PLACEHOLDER, placeholder))
        if value:
            self.add(AttributeEntry(Attribute.VALUE, value))

    def render(self, context=None) -> str:
        return super().render(context).replace(f"</{self.tag}>", "")
