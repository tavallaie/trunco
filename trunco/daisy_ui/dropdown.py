from typing import List, Union, Optional
from trunco import Component
from trunco.components import LinkComponent, ListComponent, ListItemComponent
from enum import Enum


class DaisyUIDropdownAlignment(Enum):
    TOP = "dropdown-top"
    BOTTOM = "dropdown-bottom"
    LEFT = "dropdown-left"
    RIGHT = "dropdown-right"
    END = "dropdown-end"


class DaisyUIDropdownTrigger(Enum):
    HOVER = "dropdown-hover"
    OPEN = "dropdown-open"


class DaisyUIDropdown(Component):
    def __init__(
        self,
        summary_text: str,
        menu_items: List[Union[Component, str]] = None,
        alignment: DaisyUIDropdownAlignment = DaisyUIDropdownAlignment.BOTTOM,
        trigger: Optional[DaisyUIDropdownTrigger] = None,
        additional_classes: List[str] = None,
        menu_classes: List[str] = None,
        **kwargs,
    ):
        super().__init__(tag="details", **kwargs)
        self.add_class("dropdown")

        if alignment:
            self.add_class(alignment.value)
        if trigger:
            self.add_class(trigger.value)
        if additional_classes:
            for class_name in additional_classes:
                self.add_class(class_name)

        # Create the summary component
        summary_component = Component(
            tag="summary", css_classes=["btn", "m-1"], id=f"{self.id}-summary"
        )
        summary_component.add_child(summary_text)
        self.add_child(summary_component)

        # Default menu classes
        default_menu_classes = [
            "menu",
            "dropdown-content",
            "bg-base-100",
            "rounded-box",
            "z-[1]",
            "w-52",
            "p-2",
            "shadow",
        ]

        # Combine user-provided and default menu classes
        if menu_classes:
            menu_classes = default_menu_classes + menu_classes
        else:
            menu_classes = default_menu_classes

        # Create the menu component using ListComponent
        menu_component = ListComponent(
            items=[
                ListItemComponent(
                    children=[
                        item
                        if isinstance(item, Component)
                        else LinkComponent(href="#", text=item, target=None)
                    ],
                    id=f"{self.id}-menu-item-{i}",
                )
                for i, item in enumerate(menu_items or [])
            ],
            css_classes=menu_classes,
            id=f"{self.id}-menu",
        )

        self.add_child(menu_component)
