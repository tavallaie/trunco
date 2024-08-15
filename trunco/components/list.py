from trunco import Component
from typing import List


class ListItemComponent(Component):
    """
    A basic list item component for unordered or ordered lists.
    """

    def __init__(self, content: str = "{content}", **kwargs):
        super().__init__(tag="li", **kwargs)
        self.children.append(content)


class ListComponent(Component):
    """
    A basic list component, which can be either ordered (ol) or unordered (ul).
    """

    def __init__(
        self, ordered: bool = False, items: List[ListItemComponent] = None, **kwargs
    ):
        tag = "ol" if ordered else "ul"
        super().__init__(tag=tag, **kwargs)
        if items:
            self.children.extend(items)
