from trunco.base import Component


class DividerComponent(Component):
    """
    A basic horizontal divider component (hr).
    """

    def __init__(self, **kwargs):
        super().__init__(tag="hr", **kwargs)

    def render(self, context=None) -> str:
        # Ensure the hr tag is self-closing
        return super().render(context).replace(f"</{self.tag}>", "")
