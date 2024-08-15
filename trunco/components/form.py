from trunco.base import Component
from trunco.enums import Attribute, Method


class FormComponent(Component):
    """
    A basic form component that can contain other input elements and handle submission.
    """

    def __init__(self, action: str = "", method: Method = Method.POST, **kwargs):
        super().__init__(tag="form", **kwargs)
        if action:
            self.add_attribute(Attribute.ACTION, action)
        self.add_attribute(Attribute.METHOD, method.value)
