from typing import Union

from trunco.base import Component
from trunco.enums import Attribute
from trunco.spacing import gap_classes, join_classes


class CheckboxComponent(Component):
    """
    A basic checkbox component.
    """

    def __init__(
        self,
        label: str = "{label}",
        checked: bool = False,
        gap: Union[str, int] = "sm",
        **kwargs,
    ):
        super().__init__(tag="input", **kwargs)
        self.add_attribute(Attribute.TYPE, "checkbox")
        if checked:
            self.add_attribute(Attribute.CHECKED, "checked")
        self.label = label
        self.gap = gap

    def render(self, context=None) -> str:
        input_html = super().render(context).replace(f"</{self.tag}>", "")
        if not self.label:
            return input_html

        text = self.label.format(**context) if context else self.label
        wrapper_class = join_classes(
            "inline-flex",
            "items-center",
            *gap_classes(self.gap),
        )
        return (
            f'<div class="{wrapper_class}">'
            f"{input_html}<label>{text}</label>"
            f"</div>"
        )
