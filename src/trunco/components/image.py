from trunco.base import Component
from trunco.enums import Attribute


class ImageComponent(Component):
    """
    A basic image component.
    """

    def __init__(self, src: str, alt: str = "", **kwargs):
        super().__init__(tag="img", **kwargs)
        self.add_attribute(Attribute.SRC, src)
        self.add_attribute(Attribute.ALT, alt)

    def render(self, context=None) -> str:
        # Ensure the img tag is self-closing
        return super().render(context).replace(f"</{self.tag}>", "")
