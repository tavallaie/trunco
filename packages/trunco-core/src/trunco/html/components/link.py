from trunco.html.base import Component, AttributeEntry
from trunco.html.enums import Attribute


class LinkComponent(Component):
    """
    A basic hyperlink component.
    """

    def __init__(
        self, href: str, text: str = "{text}", target: str = "_self", **kwargs
    ):
        super().__init__(tag="a", **kwargs)
        self.add(AttributeEntry(Attribute.HREF, href))
        self.add(AttributeEntry(Attribute.TARGET, target))
        self.add(text)
