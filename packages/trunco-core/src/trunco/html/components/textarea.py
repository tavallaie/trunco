from trunco.html.base import Component


class TextAreaComponent(Component):
    """
    A basic text area component for multi-line text input.
    """

    def __init__(self, rows: int = 4, cols: int = 50, placeholder: str = "", **kwargs):
        super().__init__(tag="textarea", **kwargs)
        self.add_attribute("rows", str(rows))
        self.add_attribute("cols", str(cols))
        if placeholder:
            self.children.append(placeholder)
