from dataclasses import dataclass, field
from typing import List, Optional, Union, Dict
import uuid
from .enums import Directive, Trigger, Attribute


@dataclass
class Component:
    """
    The base class for all components in the Trunco framework.
    Provides common functionality such as HTML attribute generation,
    context management, script handling, and validation.
    """

    tag: str = "div"
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    css_classes: List[str] = field(default_factory=list)
    styles: Dict[str, str] = field(default_factory=dict)
    children: List[Union["Component", str]] = field(default_factory=list)
    directives: Dict[Directive, str] = field(default_factory=dict)
    attributes: Dict[Attribute, str] = field(default_factory=dict)
    triggers: List[Trigger] = field(default_factory=list)
    custom_scripts: List[str] = field(default_factory=list)

    def add_child(self, child: Union["Component", str]):
        """Adds a child component or string to this component's children list."""
        self.children.append(child)

    def add_class(self, class_name: str):
        """Adds a CSS class to this component."""
        self.css_classes.append(class_name)

    def render(
        self,
        context: Optional[Dict[str, Union[str, int, float, bool, list, dict]]] = None,
    ) -> str:
        """
        Renders the component as an HTML string, substituting context variables.
        """
        # Substitute context variables in children strings
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
        return f"<{self.tag} {attributes}>{children_html}{scripts_html}</{self.tag}>"

    def to_html_attributes(self) -> str:
        """Converts the component's attributes, classes, and directives into a string of HTML attributes."""
        attribute_mapping = {
            "id": self.id,
            "class": " ".join(self.css_classes) if self.css_classes else None,
            "style": "; ".join(f"{k}: {v}" for k, v in self.styles.items()) + ";"
            if self.styles
            else None,
        }

        for directive, expression in self.directives.items():
            attribute_mapping[directive.value] = expression

        for attribute, value in self.attributes.items():
            attribute_mapping[attribute.value] = value

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
