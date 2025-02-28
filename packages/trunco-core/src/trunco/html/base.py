from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union, Dict, Tuple
import uuid
from .enums import Directive, Trigger, Attribute, Swap
from functools import singledispatchmethod


# Wrapper classes for different types of additions.
@dataclass
class CssClass:
    value: str


@dataclass
class StyleRule:
    property_name: str
    value: str


@dataclass
class DirectiveEntry:
    directive: "Directive"  # Assumes Directive is imported from your enums.
    expression: str


@dataclass
class AttributeEntry:
    attribute: Union["Attribute", str]
    value: str


@dataclass
class TriggerEntry:
    trigger: "Trigger"  # Assumes Trigger is imported from your enums.


# We'll use a class-level alias to help with forward references.
# Initially set to None; it will be updated after the class definition.
_Component: type = None


@dataclass
class Component:
    tag: str = "div"
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    css_classes: List[str] = field(default_factory=list)
    styles: Dict[str, str] = field(default_factory=dict)
    children: List[Union["Component", str]] = field(default_factory=list)
    directives: Dict["Directive", str] = field(default_factory=dict)
    attributes: Dict[Union["Attribute", str], str] = field(default_factory=dict)
    triggers: List["Trigger"] = field(default_factory=list)
    custom_scripts: List[str] = field(default_factory=list)
    hx_methods: Optional[Tuple[str, str]] = None  # Tuple for HxMethod handling
    swap: Optional["Swap"] = None
    trigger: Optional["Trigger"] = None

    # Create a class-level alias for Component for use in annotations.
    _Component: type = _Component

    def __post_init__(self):
        if self.hx_methods:
            method, url = self.hx_methods
            self.add(AttributeEntry(method, url))
        if self.swap:
            self.add(AttributeEntry("hx-swap", self.swap.value))
        if self.trigger:
            self.add(AttributeEntry("hx-trigger", self.trigger.value))

    @singledispatchmethod
    def add(self, item):
        raise ValueError(f"Unsupported type: {type(item)}")

    @add.register
    def _(self, child: str):
        self.children.append(child)

    @add.register
    def _(self, css: CssClass):
        self.css_classes.append(css.value)

    @add.register
    def _(self, rule: StyleRule):
        self.styles[rule.property_name] = rule.value

    @add.register
    def _(self, directive: DirectiveEntry):
        if not isinstance(directive.directive, Directive):
            raise ValueError(f"Invalid directive: {directive.directive}")
        self.directives[directive.directive] = directive.expression

    @add.register
    def _(self, attr: AttributeEntry):
        if not isinstance(attr.attribute, (Attribute, str)):
            raise ValueError(f"Invalid attribute: {attr.attribute}")
        self.attributes[attr.attribute] = attr.value

    @add.register
    def _(self, trig: TriggerEntry):
        if not isinstance(trig.trigger, Trigger):
            raise ValueError(f"Invalid trigger: {trig.trigger}")
        self.triggers.append(trig.trigger)

    def render(
        self,
        context: Optional[Dict[str, Union[str, int, float, bool, list, dict]]] = None,
    ) -> str:
        if context:
            rendered_children = [
                child.format(**context)
                if isinstance(child, str)
                else child.render(context)
                for child in self.children
            ]
        else:
            rendered_children = [
                child.render() if isinstance(child, Component) else child
                for child in self.children
            ]
        attributes = self.to_html_attributes()
        children_html = "".join(rendered_children)
        scripts_html = self.render_custom_scripts()
        return f"<{self.tag} {attributes}>{children_html}</{self.tag}>{scripts_html}"

    def to_html_attributes(self) -> str:
        attribute_mapping = {
            "id": self.id,
            "class": " ".join(self.css_classes) if self.css_classes else None,
            "style": "; ".join(f"{k}: {v}" for k, v in self.styles.items()) + ";"
            if self.styles
            else None,
        }
        if Attribute.TYPE in self.attributes:
            attribute_mapping["type"] = self.attributes[Attribute.TYPE]
        for attribute, value in self.attributes.items():
            if isinstance(attribute, Attribute) and attribute.value != "type":
                attribute_mapping[attribute.value] = value
            elif isinstance(attribute, str):
                attribute_mapping[attribute] = value
        for directive, expression in self.directives.items():
            attribute_mapping[directive.value] = expression
        if self.triggers:
            attribute_mapping["hx-trigger"] = " ".join(
                trigger.value for trigger in self.triggers
            )
        attributes = [
            f'{attr}="{value}"'
            for attr, value in attribute_mapping.items()
            if value is not None
        ]
        return " ".join(attributes)

    def render_custom_scripts(self) -> str:
        return "\n".join(f"<script>{script}</script>" for script in self.custom_scripts)

    def __str__(self) -> str:
        return self.render()


Component._Component = Component
globals()["Component"] = Component
Component.add.register(Component, lambda self, child: self.children.append(child))
