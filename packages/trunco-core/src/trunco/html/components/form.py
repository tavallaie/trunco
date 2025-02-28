from trunco.html.base import Component, AttributeEntry
from trunco.html.enums import Attribute, Method


class FormComponent(Component):
    """
    A basic form component that can contain other input elements and handle submission.
    """

    def __init__(self, action: str = "", method: Method = Method.POST, **kwargs):
        super().__init__(tag="form", **kwargs)
        if action:
            self.add(AttributeEntry(Attribute.ACTION, action))
        self.add(AttributeEntry(Attribute.METHOD, method.value))
