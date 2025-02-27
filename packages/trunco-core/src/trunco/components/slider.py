from trunco.base import Component
from trunco.enums import Attribute
from trunco.components.label import LabelComponent


class SliderComponent(Component):
    """
    A basic slider component that allows users to select a value from a specified range.
    """

    def __init__(
        self,
        min_value: int = 0,
        max_value: int = 100,
        step: int = 1,
        value: int = None,
        **kwargs,
    ):
        super().__init__(tag="input", **kwargs)
        self.add_attribute(Attribute.TYPE, "range")
        self.add_attribute(Attribute.MIN, str(min_value))
        self.add_attribute(Attribute.MAX, str(max_value))
        self.add_attribute(Attribute.STEP, str(step))
        if value is not None:
            self.add_attribute(Attribute.VALUE, str(value))

    def render(self, context=None) -> str:
        # Render the input element as a self-closing tag
        return super().render(context).replace(f"</{self.tag}>", "")


class SliderWithLabelComponent(Component):
    """
    A composite component that includes a label and a slider.
    """

    def __init__(self, label_text: str = "{label_text}", **slider_kwargs):
        super().__init__(tag="div")
        self.add_child(LabelComponent(text=label_text))
        self.add_child(SliderComponent(**slider_kwargs))
