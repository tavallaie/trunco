from typing import Optional, Union

from trunco.base import Component


class ZbuildCard(Component):
    """0build Kit card component using z-* classes."""

    STYLES = (
        "default",
        "primary",
        "secondary",
        "success",
        "warning",
        "info",
        "danger",
    )

    def __init__(
        self,
        title: Optional[str] = None,
        body: Optional[Union[str, Component]] = None,
        badge: Optional[str] = None,
        style: str = "default",
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("z-card")
        if style != "default" and style in self.STYLES:
            self.add_class(f"z-card-{style}")

        body_container = Component(tag="div")
        body_container.add_class("z-card-body")

        if title:
            title_el = Component(tag="h3")
            title_el.add_class("z-card-title")
            title_el.add_child(title)
            body_container.add_child(title_el)

        if badge:
            badge_el = Component(tag="p")
            badge_el.add_class("z-text-meta")
            badge_el.add_child(badge)
            body_container.add_child(badge_el)

        if body is not None:
            if isinstance(body, Component):
                body_container.add_child(body)
            else:
                paragraph = Component(tag="p")
                paragraph.add_child(body)
                body_container.add_child(paragraph)

        self.add_child(body_container)
