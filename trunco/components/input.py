from trunco.base import Component
from trunco.enums import Attribute


class InputComponent(Component):
    """
    A basic input component for capturing user input.
    """

    def __init__(
        self, input_type: str = "text", placeholder: str = "", value: str = "", **kwargs
    ):
        super().__init__(tag="input", **kwargs)
        self.add_attribute(Attribute.TYPE, input_type)
        if placeholder:
            self.add_attribute(Attribute.PLACEHOLDER, placeholder)
        if value:
            self.add_attribute(Attribute.VALUE, value)

    def render(self, context=None) -> str:
        # Ensure the input tag is self-closing
        return super().render(context).replace(f"</{self.tag}>", "")
