from trunco.base import Component


class BlockquoteComponent(Component):
    """
    A basic blockquote component.
    """

    def __init__(self, quote: str = "{quote}", **kwargs):
        super().__init__(tag="blockquote", **kwargs)
        self.children.append(quote)
