from trunco.base import Component
from trunco.components.checkbox import CheckboxComponent
from trunco.components.form import FormComponent
from trunco.components.input import InputComponent
from trunco.components.label import LabelComponent
from trunco.components.radio import RadioComponent, RadioGroupComponent
from trunco.components.select import OptionComponent, SelectComponent
from trunco.components.slider import SliderComponent
from trunco.components.textarea import TextAreaComponent
from trunco.enums import Attribute, Method
from trunco.spacing import gap_classes, join_classes, stack_classes


class DaisyForm(FormComponent):
    """DaisyUI form container."""

    def __init__(
        self,
        action: str = "",
        method: Method = Method.POST,
        gap: str | int = "md",
        **kwargs,
    ):
        super().__init__(action=action, method=method, **kwargs)
        self.add_class("flex")
        self.add_class("flex-col")
        for cls in stack_classes(gap):
            self.add_class(cls)


class DaisyFormControl(Component):
    """DaisyUI form-control wrapper with optional label and help text."""

    def __init__(
        self,
        label: str | None = None,
        field: Component | None = None,
        help_text: str | None = None,
        required: bool = False,
        gap: str | int = "sm",
        **kwargs,
    ):
        super().__init__(tag="label", **kwargs)
        self.add_class("form-control")
        self.add_class("flex")
        self.add_class("flex-col")
        for cls in gap_classes(gap):
            self.add_class(cls)

        if label:
            label_wrapper = Component(tag="div")
            label_wrapper.add_class("label")
            label_text = Component(tag="span")
            label_text.add_class("label-text")
            if required:
                label_text.add_class("label-text-alt")
            label_text.add_child(label)
            label_wrapper.add_child(label_text)
            self.add_child(label_wrapper)

        if field is not None:
            self.add_child(field)

        if help_text:
            help_wrapper = Component(tag="div")
            help_wrapper.add_class("label")
            help_span = Component(tag="span")
            help_span.add_class("label-text-alt")
            help_span.add_child(help_text)
            help_wrapper.add_child(help_span)
            self.add_child(help_wrapper)


class DaisyTextarea(TextAreaComponent):
    """DaisyUI textarea."""

    VARIANTS = ("bordered", "ghost")
    SIZES = ("lg", "md", "sm", "xs")

    def __init__(
        self,
        rows: int = 4,
        cols: int = 50,
        placeholder: str = "",
        variant: str = "bordered",
        size: str | None = None,
        **kwargs,
    ):
        super().__init__(rows=rows, cols=cols, placeholder=placeholder, **kwargs)
        self.add_class("textarea")
        if variant in self.VARIANTS:
            self.add_class(f"textarea-{variant}")
        if size in self.SIZES:
            self.add_class(f"textarea-{size}")


class DaisyOption(OptionComponent):
    """DaisyUI select option."""


class DaisySelect(SelectComponent):
    """DaisyUI select dropdown."""

    VARIANTS = ("bordered", "ghost")
    SIZES = ("lg", "md", "sm", "xs")

    def __init__(
        self,
        options: list[DaisyOption] | None = None,
        variant: str = "bordered",
        size: str | None = None,
        **kwargs,
    ):
        super().__init__(options=options, **kwargs)
        self.add_class("select")
        if variant in self.VARIANTS:
            self.add_class(f"select-{variant}")
        if size in self.SIZES:
            self.add_class(f"select-{size}")


class DaisyCheckbox(CheckboxComponent):
    """DaisyUI checkbox."""

    VARIANTS = (
        "primary",
        "secondary",
        "accent",
        "neutral",
        "info",
        "success",
        "warning",
        "error",
    )

    def __init__(
        self,
        label: str = "{label}",
        checked: bool = False,
        variant: str = "primary",
        gap: str | int = "sm",
        **kwargs,
    ):
        super().__init__(label=label, checked=checked, gap=gap, **kwargs)
        self.add_class("checkbox")
        if variant in self.VARIANTS:
            self.add_class(f"checkbox-{variant}")

    def render(self, context=None) -> str:
        input_html = super(CheckboxComponent, self).render(context).replace(f"</{self.tag}>", "")
        if not self.label:
            return input_html
        text = self.label.format(**context) if context else self.label
        label_class = join_classes(
            "label",
            "cursor-pointer",
            *gap_classes(self.gap),
        )
        return (
            f'<label class="{label_class}">'
            f"{input_html}"
            f'<span class="label-text">{text}</span>'
            f"</label>"
        )


class DaisyRadio(RadioComponent):
    """DaisyUI radio button."""

    VARIANTS = (
        "primary",
        "secondary",
        "accent",
        "neutral",
        "info",
        "success",
        "warning",
        "error",
    )

    def __init__(
        self,
        name: str,
        value: str,
        label: str = "{label}",
        checked: bool = False,
        variant: str = "primary",
        gap: str | int = "sm",
        **kwargs,
    ):
        super().__init__(
            name=name,
            value=value,
            label=label,
            checked=checked,
            gap=gap,
            **kwargs,
        )
        self.add_class("radio")
        if variant in self.VARIANTS:
            self.add_class(f"radio-{variant}")

    def render(self, context=None) -> str:
        input_html = super(RadioComponent, self).render(context).replace(f"</{self.tag}>", "")
        if not self.label:
            return input_html
        text = self.label.format(**context) if context else self.label
        label_class = join_classes(
            "label",
            "cursor-pointer",
            *gap_classes(self.gap),
        )
        return (
            f'<label class="{label_class}">'
            f"{input_html}"
            f'<span class="label-text">{text}</span>'
            f"</label>"
        )


class DaisyRadioGroup(RadioGroupComponent):
    """DaisyUI radio group."""

    def __init__(
        self,
        name: str,
        options: list[DaisyRadio] | None = None,
        gap: str | int = "md",
        direction: str = "vertical",
        **kwargs,
    ):
        super().__init__(name=name, options=options, gap=gap, direction=direction, **kwargs)


class DaisyLabel(LabelComponent):
    """DaisyUI label."""

    def __init__(self, text: str = "{text}", for_input_id: str = "", **kwargs):
        super().__init__(text=text, for_input_id=for_input_id, **kwargs)
        self.add_class("label")
        if self.children:
            wrapped = Component(tag="span")
            wrapped.add_class("label-text")
            wrapped.add_child(self.children[0])
            self.children = [wrapped]


class DaisyRange(SliderComponent):
    """DaisyUI range slider."""

    VARIANTS = (
        "primary",
        "secondary",
        "accent",
        "neutral",
        "info",
        "success",
        "warning",
        "error",
    )

    def __init__(
        self,
        min_value: int = 0,
        max_value: int = 100,
        step: int = 1,
        value: int | None = None,
        variant: str = "primary",
        **kwargs,
    ):
        super().__init__(
            min_value=min_value,
            max_value=max_value,
            step=step,
            value=value,
            **kwargs,
        )
        self.add_class("range")
        if variant in self.VARIANTS:
            self.add_class(f"range-{variant}")


class DaisyToggle(InputComponent):
    """DaisyUI toggle switch."""

    VARIANTS = (
        "primary",
        "secondary",
        "accent",
        "neutral",
        "info",
        "success",
        "warning",
        "error",
    )
    SIZES = ("lg", "md", "sm", "xs")

    def __init__(
        self,
        label: str | None = None,
        checked: bool = False,
        variant: str = "primary",
        size: str | None = None,
        gap: str | int = "sm",
        **kwargs,
    ):
        super().__init__(input_type="checkbox", **kwargs)
        self.add_class("toggle")
        if variant in self.VARIANTS:
            self.add_class(f"toggle-{variant}")
        if size in self.SIZES:
            self.add_class(f"toggle-{size}")
        if checked:
            self.add_attribute(Attribute.CHECKED, "checked")
        self.label = label
        self.gap = gap

    def render(self, context=None) -> str:
        input_html = super().render(context)
        if not self.label:
            return input_html
        text = self.label.format(**context) if context else self.label
        label_class = join_classes(
            "label",
            "cursor-pointer",
            *gap_classes(self.gap),
        )
        return (
            f'<label class="{label_class}">'
            f'<span class="label-text">{text}</span>'
            f"{input_html}"
            f"</label>"
        )


class DaisyFileInput(InputComponent):
    """DaisyUI file input."""

    VARIANTS = ("bordered", "ghost")
    SIZES = ("lg", "md", "sm", "xs")

    def __init__(
        self,
        variant: str = "bordered",
        size: str | None = None,
        **kwargs,
    ):
        super().__init__(input_type="file", **kwargs)
        self.add_class("file-input")
        if variant in self.VARIANTS:
            self.add_class(f"file-input-{variant}")
        if size in self.SIZES:
            self.add_class(f"file-input-{size}")


class DaisyFieldset(Component):
    """DaisyUI fieldset with optional legend."""

    def __init__(
        self,
        legend: str | None = None,
        children: list[Component | str] | None = None,
        **kwargs,
    ):
        super().__init__(tag="fieldset", **kwargs)
        self.add_class("fieldset")
        self.add_class("bg-base-100")
        self.add_class("border")
        self.add_class("border-base-300")
        self.add_class("rounded-box")
        self.add_class("p-4")
        if legend:
            legend_el = Component(tag="legend")
            legend_el.add_class("fieldset-legend")
            legend_el.add_child(legend)
            self.add_child(legend_el)
        if children:
            body = Component(tag="div")
            body.add_class("flex")
            body.add_class("flex-col")
            body.add_class("gap-3")
            for child in children:
                body.add_child(child)
            self.add_child(body)
