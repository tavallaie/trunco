from trunco.base import Component
from trunco.enums import Attribute
from typing import List


class RadioComponent(Component):
    """
    A basic radio button component.
    """

    def __init__(
        self,
        name: str,
        value: str,
        label: str = "{label}",
        checked: bool = False,
        **kwargs,
    ):
        super().__init__(tag="input", **kwargs)
        self.add_attribute(Attribute.TYPE, "radio")
        self.add_attribute(Attribute.NAME, name)
        self.add_attribute(Attribute.VALUE, value)
        if checked:
            self.add_attribute(Attribute.CHECKED, "checked")
        self.label = label

    def render(self, context=None) -> str:
        # Render the input element as a self-closing tag
        input_html = super().render(context).replace(f"</{self.tag}>", "")

        # Substitute label with context if available
        label_html = (
            f"<label>{self.label.format(**context) if context else self.label}</label>"
            if self.label
            else ""
        )

        return f"{input_html}{label_html}"


class RadioGroupComponent(Component):
    """
    A group of radio buttons.
    """

    def __init__(self, name: str, options: List[RadioComponent] = None, **kwargs):
        super().__init__(tag="div", **kwargs)
        if options:
            self.children.extend(options)
        self.name = name
