from trunco.html import Component


class ParagraphComponent(Component):
    """
    A basic paragraph component.
    """

    def __init__(self, text: str = "", **kwargs):
        super().__init__(tag="p", **kwargs)
        self.add(text)
