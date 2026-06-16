import uuid
from dataclasses import dataclass, field
from typing import Union

from .enums import Attribute

VOID_TAGS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }
)


@dataclass
class Component:
    tag: str = "div"
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    css_classes: list[str] = field(default_factory=list)
    styles: dict[str, str] = field(default_factory=dict)
    children: list[Union["Component", str]] = field(default_factory=list)
    directives: dict[str, str] = field(default_factory=dict)
    attributes: dict[Attribute | str, str] = field(default_factory=dict)
    triggers: list[str] = field(default_factory=list)
    custom_scripts: list[str] = field(default_factory=list)
    hx_methods: tuple[str, str] | None = None
    swap: str | None = None
    trigger: str | None = None

    def __post_init__(self):
        if self.hx_methods:
            method, url = self.hx_methods
            self.add_attribute(method, url)

        if self.swap:
            swap_value = self.swap.value if hasattr(self.swap, "value") else self.swap
            self.add_attribute("hx-swap", swap_value)

        if self.trigger:
            trigger_value = self.trigger.value if hasattr(self.trigger, "value") else self.trigger
            self.add_attribute("hx-trigger", trigger_value)

    def add_child(self, child: Union["Component", str]):
        """Adds a child component or string to this component's children list."""
        self.children.append(child)

    def add_class(self, class_name: str):
        """Adds a CSS class to this component."""
        self.css_classes.append(class_name)

    def add_style(self, property_name: str, value: str):
        """Adds a CSS style to this component."""
        self.styles[property_name] = value

    def add_directive(self, directive: str | object, expression: str):
        """Adds a directive attribute (e.g. Alpine.js x-on:click) to this component."""
        key = directive.value if hasattr(directive, "value") else str(directive)
        self.directives[key] = expression

    def add_attribute(self, attribute: Attribute | str, value: str):
        """Adds a custom HTML attribute to this component."""
        if not isinstance(attribute, (Attribute, str)):
            raise ValueError(
                f"Invalid attribute: {attribute}. Must be an Attribute enum or string."
            )
        self.attributes[attribute] = value

    def add_trigger(self, trigger: str | object):
        """Adds an HTMX event trigger to this component."""
        value = trigger.value if hasattr(trigger, "value") else str(trigger)
        self.triggers.append(value)

    def add_custom_script(self, script: str):
        """Adds a custom JavaScript script to be included in the component."""
        self.custom_scripts.append(script)

    def render(
        self,
        context: dict[str, str | int | float | bool | list | dict] | None = None,
    ) -> str:
        """Renders the component as an HTML string, substituting context variables."""
        if context:
            rendered_children = [
                child.format(**context) if isinstance(child, str) else child.render(context)
                for child in self.children
            ]
        else:
            rendered_children = [
                child.render() if isinstance(child, Component) else child for child in self.children
            ]

        attributes = self.to_html_attributes()
        scripts_html = self.render_custom_scripts()
        if self.tag in VOID_TAGS:
            return f"<{self.tag} {attributes}>{scripts_html}"
        children_html = "".join(rendered_children)
        return f"<{self.tag} {attributes}>{children_html}</{self.tag}>{scripts_html}"

    def to_html_attributes(self) -> str:
        """Converts attributes, classes, and directives into an HTML attribute string."""
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
            attribute_mapping[directive] = expression

        if self.triggers:
            attribute_mapping["hx-trigger"] = " ".join(self.triggers)

        attributes = [
            f'{attr}="{value}"' for attr, value in attribute_mapping.items() if value is not None
        ]
        return " ".join(attributes)

    def render_custom_scripts(self) -> str:
        """Renders any custom scripts as embedded JavaScript."""
        return "\n".join(f"<script>{script}</script>" for script in self.custom_scripts)

    def __str__(self) -> str:
        return self.render()
