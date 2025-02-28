from trunco.html.base import Component, AttributeEntry
from trunco.html.enums import Attribute


class CheckboxComponent(Component):
    """
    A basic checkbox component.
    """

    def __init__(self, label: str = "{label}", checked: bool = False, **kwargs):
        super().__init__(tag="input", **kwargs)
        # Use unified add() with AttributeEntry wrappers
        self.add(AttributeEntry(Attribute.TYPE, "checkbox"))
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
