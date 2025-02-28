from trunco.html.base import Component, AttributeEntry, DirectiveEntry
from trunco.html.enums import Attribute, Directive


class ButtonComponent(Component):
    """
    A basic button component that can be customized with a label and onClick action.
    """

    def __init__(self, label: str = "{label}", on_click: str = None, **kwargs):
        super().__init__(tag="button", **kwargs)
        self.add(AttributeEntry(Attribute.TYPE, "button"))
        self.add(label)
        if on_click:
            self.add(DirectiveEntry(Directive.X_ON_CLICK, on_click))
