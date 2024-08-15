from trunco.base import Component
from trunco.enums import Attribute, Directive


class ButtonComponent(Component):
    """
    A basic button component that can be customized with a label and onClick action.
    """

    def __init__(self, label: str = "{label}", on_click: str = None, **kwargs):
        super().__init__(tag="button", **kwargs)
        self.add_attribute(Attribute.TYPE, "button")  # Set the type attribute first
        self.children.append(label)
        if on_click:
            self.add_directive(Directive.X_ON_CLICK, on_click)
