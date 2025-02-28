from trunco.html.base import Component, AttributeEntry
from trunco.html.enums import Attribute


class ImageComponent(Component):
    """
    A basic image component.
    """

    def __init__(self, src: str, alt: str = "", **kwargs):
        super().__init__(tag="img", **kwargs)
        self.add(AttributeEntry(Attribute.SRC, src))
        self.add(AttributeEntry(Attribute.ALT, alt))

    def render(self, context=None) -> str:
        return super().render(context).replace(f"</{self.tag}>", "")
