from trunco.html.base import Component


class DividerComponent(Component):
    """
    A basic horizontal divider component (hr).
    """

    def __init__(self, **kwargs):
        super().__init__(tag="hr", **kwargs)

    def render(self, context=None) -> str:
        return super().render(context).replace(f"</{self.tag}>", "")
