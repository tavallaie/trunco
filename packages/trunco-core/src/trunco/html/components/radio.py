from trunco.html.base import Component, AttributeEntry
from trunco.html.enums import Attribute
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
        self.add(AttributeEntry(Attribute.TYPE, "radio"))
        self.add(AttributeEntry(Attribute.NAME, name))
        self.add(AttributeEntry(Attribute.VALUE, value))
        if checked:
            self.add(AttributeEntry(Attribute.CHECKED, "checked"))
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
            for option in options:
                self.add(option)
        self.name = name
