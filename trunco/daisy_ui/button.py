from trunco.components.button import ButtonComponent
from enum import Enum


class DaisyUIButtonVariant(Enum):
    NEUTRAL = "btn-neutral"
    PRIMARY = "btn-primary"
    SECONDARY = "btn-secondary"
    ACCENT = "btn-accent"
    INFO = "btn-info"
    SUCCESS = "btn-success"
    WARNING = "btn-warning"
    ERROR = "btn-error"
    GHOST = "btn-ghost"
    LINK = "btn-link"


class DaisyUIButtonModifier(Enum):
    OUTLINE = "btn-outline"
    ACTIVE = "btn-active"
    DISABLED = "btn-disabled"
    GLASS = "glass"
    NO_ANIMATION = "no-animation"


class DaisyUIButtonSize(Enum):
    LARGE = "btn-lg"
    MEDIUM = "btn-md"
    SMALL = "btn-sm"
    EXTRA_SMALL = "btn-xs"
    WIDE = "btn-wide"
    BLOCK = "btn-block"
    CIRCLE = "btn-circle"
    SQUARE = "btn-square"


class DaisyUIButton(ButtonComponent):
    """
    DaisyUI Button Component that inherits from Trunco's ButtonComponent.

    Allows customization of the button with DaisyUI-specific variants, sizes, and modifiers.

    Args:
        label (str): The text to display on the button.
        variant (DaisyUIButtonVariant): The color variant of the button.
        size (DaisyUIButtonSize): The size of the button.
        modifier (List[DaisyUIButtonModifier]): List of additional button styles/modifiers.
        additional_classes (list): List of additional CSS classes.
    """

    def __init__(
        self,
        label: str,
        variant: DaisyUIButtonVariant = DaisyUIButtonVariant.PRIMARY,
        size: DaisyUIButtonSize = DaisyUIButtonSize.MEDIUM,
        modifiers: list = None,
        additional_classes: list = None,
        **kwargs,
    ):
        super().__init__(label=label, **kwargs)
        self.add_class("btn")
        self.add_class(variant.value)
        self.add_class(size.value)

        if modifiers:
            for modifier in modifiers:
                self.add_class(modifier.value)

        if additional_classes:
            for class_name in additional_classes:
                self.add_class(class_name)
