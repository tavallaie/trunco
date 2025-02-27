from trunco.base import Component
from trunco.enums import Attribute


class LinkComponent(Component):
    """
    A basic hyperlink component.
    """

    def __init__(
        self, href: str, text: str = "{text}", target: str = "_self", **kwargs
    ):
        super().__init__(tag="a", **kwargs)
        self.add_attribute(Attribute.HREF, href)
        self.add_attribute(Attribute.TARGET, target)
        self.children.append(text)
