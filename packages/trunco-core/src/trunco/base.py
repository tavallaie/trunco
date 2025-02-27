from dataclasses import dataclass, field
from typing import List, Optional, Union, Dict, Tuple
import uuid
from .enums import Directive, Trigger, Attribute, Swap


@dataclass
class Component:
    tag: str = "div"
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    css_classes: List[str] = field(default_factory=list)
    styles: Dict[str, str] = field(default_factory=dict)
    children: List[Union["Component", str]] = field(default_factory=list)
    directives: Dict[Directive, str] = field(default_factory=dict)
    attributes: Dict[Union[Attribute, str], str] = field(default_factory=dict)
    triggers: List[Trigger] = field(default_factory=list)
    custom_scripts: List[str] = field(default_factory=list)
    hx_methods: Optional[Tuple[str, str]] = None  # Tuple for HxMethod handling
    swap: Optional[Swap] = None
    trigger: Optional[Trigger] = None

    def __post_init__(self):
        # Handle HxMethod if provided
        if self.hx_methods:
            method, url = self.hx_methods
            self.add_attribute(method, url)  # Use the method string directly

        # Handle Swap if provided
        if self.swap:
            self.add_attribute("hx-swap", self.swap.value)

        # Handle Trigger if provided
        if self.trigger:
            self.add_attribute("hx-trigger", self.trigger.value)

    def add_child(self, child: Union["Component", str]):
        """Adds a child component or string to this component's children list."""
        self.children.append(child)

    def add_class(self, class_name: str):
        """Adds a CSS class to this component."""
        self.css_classes.append(class_name)

    def add_style(self, property_name: str, value: str):
        """Adds a CSS style to this component."""
        self.styles[property_name] = value

    def add_directive(self, directive: Directive, expression: str):
        """Adds a directive (e.g., Alpine.js) to this component, with validation."""
        if not isinstance(directive, Directive):
            raise ValueError(
                f"Invalid directive: {directive}. Must be a Directive enum."
            )
        self.directives[directive] = expression

    def add_attribute(self, attribute: Union[Attribute, str], value: str):
        """Adds a custom HTML attribute to this component, with validation."""
        if not isinstance(attribute, (Attribute, str)):
            raise ValueError(
                f"Invalid attribute: {attribute}. Must be an Attribute enum or string."
            )
        self.attributes[attribute] = value

    def add_trigger(self, trigger: Trigger):
        """Adds an event trigger (e.g., HTMX) to this component, with validation."""
        if not isinstance(trigger, Trigger):
            raise ValueError(f"Invalid trigger: {trigger}. Must be a Trigger enum.")
        self.triggers.append(trigger)

    def add_custom_script(self, script: str):
        """Adds a custom JavaScript script to be included in the component."""
        self.custom_scripts.append(script)

    def render(
        self,
        context: Optional[Dict[str, Union[str, int, float, bool, list, dict]]] = None,
    ) -> str:
        """Renders the component as an HTML string, substituting context variables."""
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
        """Converts the component's attributes, classes, and directives into a string of HTML attributes."""
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
        """Renders any custom scripts and context data as embedded JavaScript."""
        custom_scripts = "\n".join(
            f"<script>{script}</script>" for script in self.custom_scripts
        )
        return custom_scripts

    def __str__(self) -> str:
        """Allows the component to be directly converted to a string (HTML)."""
        return self.render()
