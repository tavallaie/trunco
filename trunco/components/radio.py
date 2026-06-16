from trunco.base import Component
from trunco.enums import Attribute
from trunco.spacing import gap_classes, join_classes


class RadioComponent(Component):
    """
    A basic radio button component.
    """

    def __init__(
        self,
        name: str,
        value: str,
        label: str = "{label}",
        checked: bool = False,
        gap: str | int = "sm",
        **kwargs,
    ):
        super().__init__(tag="input", **kwargs)
        self.add_attribute(Attribute.TYPE, "radio")
        self.add_attribute(Attribute.NAME, name)
        self.add_attribute(Attribute.VALUE, value)
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
        return f'<div class="{wrapper_class}">{input_html}<label>{text}</label></div>'


class RadioGroupComponent(Component):
    """
    A group of radio buttons.
    """

    def __init__(
        self,
        name: str,
        options: list["RadioComponent"] | None = None,
        gap: str | int = "md",
        direction: str = "vertical",
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        if direction == "horizontal":
            self.add_class("flex")
            self.add_class("flex-row")
            self.add_class("flex-wrap")
        else:
            self.add_class("flex")
            self.add_class("flex-col")
        for cls in gap_classes(gap):
            self.add_class(cls)
        if options:
            self.children.extend(options)
        self.name = name
        self.gap = gap
        self.direction = direction
