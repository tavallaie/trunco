from trunco import Component
from typing import List, Optional, Union
from enum import Enum


class ModalPosition(Enum):
    TOP = "modal-top"
    BOTTOM = "modal-bottom"
    MIDDLE = "modal-middle"


class Modal(Component):
    """
    DaisyUI Modal Component.

    This component represents a modal dialog that can be displayed on a page.

    Args:
        content (List[Union[Component, str]]): The content to display inside the modal.
        position (ModalPosition, optional): The position of the modal on the screen (top, bottom, middle).
            Defaults to ModalPosition.MIDDLE.
        is_open (bool, optional): Whether the modal is open by default. Defaults to False.
        additional_classes (List[str], optional): Additional CSS classes to apply to the modal. Defaults to None.
        **kwargs: Additional keyword arguments passed to the base Component class.

    Example Usage:
        modal = Modal(
            content=[
                ModalBox(content=["This is the content of the modal"]),
                ModalAction(content=[Button(text="Close")]),
            ],
            position=ModalPosition.MIDDLE,
            is_open=True,
            additional_classes=["custom-modal-class"],
        )
    """

    def __init__(
        self,
        content: List[Union[Component, str]],
        position: ModalPosition = ModalPosition.MIDDLE,
        is_open: bool = False,
        additional_classes: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("modal")
        if position:
            self.add_class(position.value)
        if is_open:
            self.add_class("modal-open")
        if additional_classes:
            for class_name in additional_classes:
                self.add_class(class_name)
        self.children.extend(content)


class ModalBox(Component):
    """
    DaisyUI ModalBox Component.

    This component represents the content box within the modal.

    Args:
        content (List[Union[Component, str]]): The content to display inside the modal box.
        additional_classes (List[str], optional): Additional CSS classes to apply to the modal box. Defaults to None.
        **kwargs: Additional keyword arguments passed to the base Component class.
    """

    def __init__(
        self,
        content: List[Union[Component, str]],
        additional_classes: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("modal-box")
        if additional_classes:
            for class_name in additional_classes:
                self.add_class(class_name)
        self.children.extend(content)


class ModalAction(Component):
    """
    DaisyUI ModalAction Component.

    This component represents the container for modal action buttons.

    Args:
        content (List[Union[Component, str]]): The action buttons to display inside the modal action container.
        additional_classes (List[str], optional): Additional CSS classes to apply to the modal action container. Defaults to None.
        **kwargs: Additional keyword arguments passed to the base Component class.
    """

    def __init__(
        self,
        content: List[Union[Component, str]],
        additional_classes: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("modal-action")
        if additional_classes:
            for class_name in additional_classes:
                self.add_class(class_name)
        self.children.extend(content)


class ModalBackdrop(Component):
    """
    DaisyUI ModalBackdrop Component.

    This component represents the backdrop that covers the back of the modal so it can be closed by clicking outside.

    Args:
        **kwargs: Additional keyword arguments passed to the base Component class.
    """

    def __init__(self, **kwargs):
        super().__init__(tag="label", **kwargs)
        self.add_class("modal-backdrop")


class ModalToggle(Component):
    """
    DaisyUI ModalToggle Component.

    This component represents a hidden checkbox that controls the modal.

    Args:
        target_id (str): The ID of the modal to toggle.
        **kwargs: Additional keyword arguments passed to the base Component class.
    """

    def __init__(self, target_id: str, **kwargs):
        super().__init__(tag="input", **kwargs)
        self.add_class("modal-toggle")
        self.attributes["type"] = "checkbox"
        self.attributes["id"] = target_id
