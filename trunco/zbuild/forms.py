from typing import List, Optional, Union

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
from trunco.zbuild.spacing import (
    apply_gap,
    apply_margin_bottom,
    control_wrapper_open,
    layout_classes,
    resolve_gap,
)


class ZbuildForm(FormComponent):
    """0build stacked form container."""

    def __init__(
        self,
        action: str = "",
        method: Method = Method.POST,
        stacked: bool = True,
        gap: Union[str, int] = "md",
        **kwargs,
    ):
        super().__init__(action=action, method=method, **kwargs)
        if stacked:
            self.add_class("z-form-stacked")
        self._field_gap = gap

    def add_child(self, child: Union[Component, str]):
        if isinstance(child, ZbuildFormField):
            child.styles.pop("margin-bottom", None)
            apply_margin_bottom(child, self._field_gap)
        super().add_child(child)


class ZbuildFormField(Component):
    """0build form field with label and controls."""

    def __init__(
        self,
        label: Optional[str] = None,
        field: Optional[Component] = None,
        help_text: Optional[str] = None,
        required: bool = False,
        gap: Union[str, int] = "sm",
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        apply_margin_bottom(self, gap)
        if label:
            label_el = Component(tag="label")
            label_el.add_class("z-form-label")
            if required:
                label_el.add_class("z-form-label-required")
            label_el.add_child(label)
            self.add_child(label_el)
        if field is not None:
            controls = Component(tag="div")
            controls.add_class("z-form-controls")
            controls.add_child(field)
            self.add_child(controls)
        if help_text:
            help_el = Component(tag="p")
            help_el.add_class("z-form-help")
            help_el.add_child(help_text)
            self.add_child(help_el)


class ZbuildTextarea(TextAreaComponent):
    """0build textarea."""

    SIZES = ("xsmall", "small", "medium", "large")

    def __init__(
        self,
        rows: int = 4,
        cols: int = 50,
        placeholder: str = "",
        size: Optional[str] = None,
        danger: bool = False,
        **kwargs,
    ):
        super().__init__(rows=rows, cols=cols, placeholder=placeholder, **kwargs)
        self.add_class("z-textarea")
        if size in self.SIZES:
            self.add_class(f"z-form-{size}")
        if danger:
            self.add_class("z-form-danger")


class ZbuildOption(OptionComponent):
    """0build select option."""


class ZbuildSelect(SelectComponent):
    """0build select dropdown."""

    SIZES = ("xsmall", "small", "medium", "large")

    def __init__(
        self,
        options: Optional[List[ZbuildOption]] = None,
        size: Optional[str] = None,
        danger: bool = False,
        **kwargs,
    ):
        super().__init__(options=options, **kwargs)
        self.add_class("z-select")
        if size in self.SIZES:
            self.add_class(f"z-form-{size}")
        if danger:
            self.add_class("z-form-danger")


class ZbuildCheckbox(CheckboxComponent):
    """0build checkbox."""

    def __init__(
        self,
        label: str = "{label}",
        checked: bool = False,
        gap: Union[str, int] = "sm",
        **kwargs,
    ):
        super().__init__(label=label, checked=checked, gap=gap, **kwargs)
        self.add_class("z-checkbox")

    def render(self, context=None) -> str:
        input_html = super(CheckboxComponent, self).render(context).replace(f"</{self.tag}>", "")
        if not self.label:
            return input_html
        text = self.label.format(**context) if context else self.label
        return f"{control_wrapper_open(self.gap)}{input_html}<label>{text}</label></div>"


class ZbuildRadio(RadioComponent):
    """0build radio button."""

    def __init__(
        self,
        name: str,
        value: str,
        label: str = "{label}",
        checked: bool = False,
        gap: Union[str, int] = "sm",
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
        self.add_class("z-radio")

    def render(self, context=None) -> str:
        input_html = super(RadioComponent, self).render(context).replace(f"</{self.tag}>", "")
        if not self.label:
            return input_html
        text = self.label.format(**context) if context else self.label
        return f"{control_wrapper_open(self.gap)}{input_html}<label>{text}</label></div>"


class ZbuildRadioGroup(RadioGroupComponent):
    """0build radio group."""

    def __init__(
        self,
        name: str,
        options: Optional[List[ZbuildRadio]] = None,
        gap: Union[str, int] = "md",
        direction: str = "vertical",
        **kwargs,
    ):
        Component.__init__(self, tag="div", **kwargs)
        for cls in layout_classes(direction):
            self.add_class(cls)
        apply_gap(self, gap)
        if options:
            self.children.extend(options)
        self.name = name
        self.gap = gap
        self.direction = direction


class ZbuildLabel(LabelComponent):
    """0build form label."""

    def __init__(
        self,
        text: str = "{text}",
        for_input_id: str = "",
        required: bool = False,
        **kwargs,
    ):
        super().__init__(text=text, for_input_id=for_input_id, **kwargs)
        self.add_class("z-form-label")
        if required:
            self.add_class("z-form-label-required")


class ZbuildRange(SliderComponent):
    """0build range input."""

    SIZES = ("xsmall", "small", "medium", "large")

    def __init__(
        self,
        min_value: int = 0,
        max_value: int = 100,
        step: int = 1,
        value: Optional[int] = None,
        size: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            min_value=min_value,
            max_value=max_value,
            step=step,
            value=value,
            **kwargs,
        )
        self.add_class("z-range")
        if size in self.SIZES:
            self.add_class(f"z-form-{size}")


class ZbuildToggleSwitch(InputComponent):
    """0build toggle switch."""

    COLORS = ("primary", "danger")

    def __init__(
        self,
        label: Optional[str] = None,
        checked: bool = False,
        color: str = "primary",
        danger: bool = False,
        gap: Union[str, int] = "sm",
        **kwargs,
    ):
        super().__init__(input_type="checkbox", **kwargs)
        self.add_class("z-toggle-switch")
        tone = "danger" if danger else color
        if tone in self.COLORS:
            self.add_class(f"z-toggle-switch-{tone}")
        if checked:
            self.add_attribute(Attribute.CHECKED, "checked")
        self.label = label
        self.gap = gap

    def render(self, context=None) -> str:
        input_html = super().render(context)
        if not self.label:
            return input_html
        text = self.label.format(**context) if context else self.label
        gap_value = resolve_gap(self.gap)
        if gap_value:
            label_open = (
                f'<label class="display-inline-flex items-center" style="gap: {gap_value};">'
            )
        else:
            label_open = '<label class="display-inline-flex items-center">'
        return f"{label_open}{input_html}<span>{text}</span></label>"


class ZbuildFieldset(Component):
    """0build fieldset with legend."""

    def __init__(
        self,
        legend: Optional[str] = None,
        children: Optional[List[Union[Component, str]]] = None,
        gap: Union[str, int] = "md",
        **kwargs,
    ):
        super().__init__(tag="fieldset", **kwargs)
        self.add_class("z-fieldset")
        if legend:
            legend_el = Component(tag="legend")
            legend_el.add_class("z-legend")
            legend_el.add_child(legend)
            self.add_child(legend_el)
        if children:
            body = Component(tag="div")
            for i, child in enumerate(children):
                if isinstance(child, Component) and i < len(children) - 1:
                    apply_margin_bottom(child, gap)
                body.add_child(child)
            self.add_child(body)
