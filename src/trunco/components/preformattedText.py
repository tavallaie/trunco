from trunco import Component


class PreformattedTextComponent(Component):
    """
    A basic preformatted text component.
    """

    def __init__(self, text: str = "{text}", **kwargs):
        super().__init__(tag="pre", **kwargs)
        self.children.append(text)
