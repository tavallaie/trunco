# File: trunco_franken/components/button.py

from trunco.html.components.button import ButtonComponent
from trunco.html.base import CssClass, AttributeEntry
from trunco.html.enums import Attribute


class FrankenButton(ButtonComponent):
    """
    A button styled according to Franken UI guidelines.

    Usage:
      button = FrankenButton(label="Submit", on_click="alert('Submitted!')",
                               style_modifier="uk-btn-primary", size_modifier="uk-btn-lg")

    By default, the button includes:
      - The base class "uk-btn"
      - A style modifier, defaulting to "uk-btn-default"

    Available style modifiers include:
      - "uk-btn-default" (default)
      - "uk-btn-ghost"
      - "uk-btn-primary"
      - "uk-btn-secondary"
      - "uk-btn-destructive"
      - "uk-btn-text"
      - "uk-btn-link"

    Available size modifiers include:
      - "uk-btn-xs"
      - "uk-btn-sm"
      - "uk-btn-md"
      - "uk-btn-lg"
    """

    def __init__(
        self,
        label: str = "Button",
        on_click: str = None,
        style_modifier: str = "uk-btn-default",
        size_modifier: str = None,
        disabled: bool = False,
        **kwargs,
    ):
        super().__init__(label=label, on_click=on_click, **kwargs)
        # Add the base Franken UI class
        self.add(CssClass("uk-btn"))
        # Add style modifier (if provided)
        if style_modifier:
            self.add(CssClass(style_modifier))
        # Add size modifier if provided
        if size_modifier:
            self.add(CssClass(size_modifier))
        # Mark button as disabled if needed
        if disabled:
            self.add(AttributeEntry(Attribute.DISABLED, "disabled"))
