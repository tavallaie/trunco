from trunco.components import LinkComponent
from trunco import Component
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
    """
    DaisyUI Dropdown Component.

    This component wraps a dropdown in a <details> tag with a <summary> as the trigger.

    Args:
        summary_text (str): The text inside the summary element (button).
        alignment (DaisyUIDropdownAlignment): Controls the alignment of the dropdown.
        trigger (DaisyUIDropdownTrigger): Controls how the dropdown is triggered (hover, open).
        menu_items (List[LinkComponent or str]): List of menu items to be displayed in the dropdown.
        additional_classes (list): List of additional CSS classes.
    """

    def __init__(
        self,
        summary_text: str,
        alignment: DaisyUIDropdownAlignment = DaisyUIDropdownAlignment.BOTTOM,
        trigger: DaisyUIDropdownTrigger = None,
        menu_items: list = None,
        additional_classes: list = None,
        **kwargs,
    ):
        super().__init__(tag="details", **kwargs)
        self.add_class("dropdown")

        summary_component = Component(tag="summary", css_classes=["btn", "m-1"])
        summary_component.add_child(summary_text)
        self.add_child(summary_component)

        menu_component = Component(
            tag="ul",
            css_classes=[
                "menu",
                "dropdown-content",
                "bg-base-100",
                "rounded-box",
                "z-[1]",
                "w-52",
                "p-2",
                "shadow",
            ],
        )

        if menu_items:
            for item in menu_items:
                menu_item_component = Component(tag="li")
                if isinstance(item, str):
                    link_component = LinkComponent(href="#", text=item)
                    menu_item_component.add_child(link_component)
                elif isinstance(item, LinkComponent):
                    menu_item_component.add_child(item)
                menu_component.add_child(menu_item_component)

        self.add_child(menu_component)

        if trigger:
            self.add_class(trigger.value)

        if alignment:
            self.add_class(alignment.value)

        if additional_classes:
            for class_name in additional_classes:
                self.add_class(class_name)
