from typing import List, Optional, Union

from trunco.base import Component
from trunco.kits.color import resolve_color
from trunco.components.link import LinkComponent
from trunco.components.table import TableCellComponent, TableComponent, TableRowComponent
from trunco.enums import Attribute


class DaisyLink(LinkComponent):
    """DaisyUI link."""

    VARIANTS = (
        "primary",
        "secondary",
        "accent",
        "neutral",
        "info",
        "success",
        "warning",
        "error",
    )

    def __init__(
        self,
        href: str,
        text: str = "{text}",
        target: str = "_self",
        color: Optional[str] = None,
        variant: str = "primary",
        **kwargs,
    ):
        super().__init__(href=href, text=text, target=target, **kwargs)
        tone = resolve_color(color=color, variant=variant, default="primary")
        self.add_class("link")
        if tone in self.VARIANTS:
            self.add_class(f"link-{tone}")


class DaisyDivider(Component):
    """DaisyUI divider — use ``horizontal=False`` for a vertical rule in flex rows."""

    def __init__(self, text: Optional[str] = None, horizontal: bool = True, **kwargs):
        super().__init__(tag="div", **kwargs)
        self.add_class("divider")
        if not horizontal:
            self.add_class("divider-horizontal")
        if text:
            self.add_child(text)


class DaisyBadge(Component):
    """DaisyUI badge."""

    VARIANTS = (
        "primary",
        "secondary",
        "accent",
        "neutral",
        "info",
        "success",
        "warning",
        "error",
        "ghost",
        "outline",
    )
    SIZES = ("lg", "md", "sm", "xs")

    def __init__(
        self,
        text: str,
        color: Optional[str] = None,
        variant: str = "primary",
        size: Optional[str] = None,
        outline: bool = False,
        **kwargs,
    ):
        super().__init__(tag="span", **kwargs)
        tone = resolve_color(color=color, variant=variant, default="primary")
        self.add_class("badge")
        if tone in self.VARIANTS:
            self.add_class(f"badge-{tone}")
        if outline:
            self.add_class("badge-outline")
        if size in self.SIZES:
            self.add_class(f"badge-{size}")
        self.add_child(text)


class DaisyAlert(Component):
    """DaisyUI alert."""

    VARIANTS = ("info", "success", "warning", "error")

    def __init__(
        self,
        message: str,
        color: Optional[str] = None,
        variant: str = "info",
        title: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        tone = resolve_color(color=color, variant=variant, default="info")
        self.add_class("alert")
        if tone in self.VARIANTS:
            self.add_class(f"alert-{tone}")
        if title:
            title_el = Component(tag="h3")
            title_el.add_class("font-bold")
            title_el.add_child(title)
            self.add_child(title_el)
        body = Component(tag="span")
        body.add_child(message)
        self.add_child(body)


class DaisyProgress(Component):
    """DaisyUI progress bar."""

    VARIANTS = (
        "primary",
        "secondary",
        "accent",
        "neutral",
        "info",
        "success",
        "warning",
        "error",
    )

    def __init__(
        self,
        value: int = 0,
        max_value: int = 100,
        color: Optional[str] = None,
        variant: str = "primary",
        **kwargs,
    ):
        super().__init__(tag="progress", **kwargs)
        tone = resolve_color(color=color, variant=variant, default="primary")
        self.add_class("progress")
        if tone in self.VARIANTS:
            self.add_class(f"progress-{tone}")
        self.add_attribute(Attribute.VALUE, str(value))
        self.add_attribute("max", str(max_value))

    def render(self, context=None) -> str:
        return super().render(context).replace(f"</{self.tag}>", "")


class DaisyAvatar(Component):
    """DaisyUI avatar."""

    def __init__(
        self,
        image_src: str,
        alt: str = "",
        online: bool = False,
        offline: bool = False,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("avatar")
        if online:
            self.add_class("online")
        if offline:
            self.add_class("offline")
        inner = Component(tag="div")
        inner.add_class("w-12")
        inner.add_class("rounded-full")
        image = Component(tag="img")
        image.add_attribute(Attribute.SRC, image_src)
        if alt:
            image.add_attribute(Attribute.ALT, alt)
        inner.add_child(image)
        self.add_child(inner)


class DaisyBreadcrumbs(Component):
    """DaisyUI breadcrumbs navigation."""

    def __init__(self, items: List[Union[str, DaisyLink]], **kwargs):
        super().__init__(tag="div", **kwargs)
        self.add_class("breadcrumbs")
        list_el = Component(tag="ul")
        for item in items:
            li = Component(tag="li")
            if isinstance(item, DaisyLink):
                li.add_child(item)
            else:
                li.add_child(item)
            list_el.add_child(li)
        self.add_child(list_el)


class DaisyTable(TableComponent):
    """DaisyUI table."""

    STYLES = ("zebra", "pin-rows", "pin-cols", "xs", "sm", "md", "lg")

    def __init__(
        self,
        headers: Optional[List[str]] = None,
        rows: Optional[List[TableRowComponent]] = None,
        zebra: bool = False,
        size: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(headers=headers, rows=rows, **kwargs)
        self.add_class("table")
        if zebra:
            self.add_class("table-zebra")
        if size in ("xs", "sm", "md", "lg"):
            self.add_class(f"table-{size}")


class DaisyLoading(Component):
    """DaisyUI loading spinner."""

    STYLES = ("spinner", "dots", "ring", "ball", "bars", "infinity")
    SIZES = ("xs", "sm", "md", "lg")

    def __init__(
        self,
        style: str = "spinner",
        size: str = "md",
        **kwargs,
    ):
        super().__init__(tag="span", **kwargs)
        self.add_class("loading")
        if style in self.STYLES:
            self.add_class(f"loading-{style}")
        if size in self.SIZES:
            self.add_class(f"loading-{size}")


class DaisyTooltip(Component):
    """DaisyUI tooltip wrapper."""

    POSITIONS = ("top", "bottom", "left", "right")

    def __init__(
        self,
        tip: str,
        child: Component,
        position: str = "top",
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("tooltip")
        if position in self.POSITIONS:
            self.add_class(f"tooltip-{position}")
        self.add_attribute("data-tip", tip)
        self.add_child(child)


class DaisyModal(Component):
    """DaisyUI modal dialog."""

    def __init__(
        self,
        modal_id: str,
        title: str,
        body: Union[str, Component],
        actions: Optional[List[Component]] = None,
        **kwargs,
    ):
        super().__init__(tag="dialog", **kwargs)
        self.add_class("modal")
        self.add_attribute("id", modal_id)

        box = Component(tag="div")
        box.add_class("modal-box")
        title_el = Component(tag="h3")
        title_el.add_class("font-bold")
        title_el.add_class("text-lg")
        title_el.add_child(title)
        box.add_child(title_el)

        if isinstance(body, Component):
            box.add_child(body)
        else:
            paragraph = Component(tag="p")
            paragraph.add_class("py-4")
            paragraph.add_child(body)
            box.add_child(paragraph)

        if actions:
            action_row = Component(tag="div")
            action_row.add_class("modal-action")
            for action in actions:
                action_row.add_child(action)
            box.add_child(action_row)

        self.add_child(box)
        backdrop = Component(tag="form")
        backdrop.add_attribute("method", "dialog")
        backdrop.add_class("modal-backdrop")
        backdrop_btn = Component(tag="button")
        backdrop_btn.add_child("close")
        backdrop.add_child(backdrop_btn)
        self.add_child(backdrop)


class DaisyNavbar(Component):
    """DaisyUI navbar."""

    def __init__(
        self,
        start: Optional[List[Union[Component, str]]] = None,
        center: Optional[List[Union[Component, str]]] = None,
        end: Optional[List[Union[Component, str]]] = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("navbar")
        self.add_class("bg-base-100")

        for section_name, items in (
            ("navbar-start", start),
            ("navbar-center", center),
            ("navbar-end", end),
        ):
            if items:
                section = Component(tag="div")
                section.add_class(section_name)
                for item in items:
                    section.add_child(item)
                self.add_child(section)


class DaisyTabs(Component):
    """DaisyUI tabs."""

    STYLES = ("boxed", "bordered", "lifted")

    def __init__(
        self,
        tabs: List[tuple],
        style: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("tabs")
        if style in self.STYLES:
            self.add_class(f"tabs-{style}")

        for label, content_id, active in tabs:
            tab = Component(tag="a")
            tab.add_class("tab")
            if active:
                tab.add_class("tab-active")
            tab.add_attribute(Attribute.HREF, f"#{content_id}")
            tab.add_child(label)
            self.add_child(tab)


class DaisyMenu(Component):
    """DaisyUI vertical menu."""

    def __init__(self, items: List[Union[str, DaisyLink, Component]], **kwargs):
        super().__init__(tag="ul", **kwargs)
        self.add_class("menu")
        self.add_class("bg-base-200")
        self.add_class("rounded-box")
        self.add_class("w-56")
        for item in items:
            li = Component(tag="li")
            li.add_child(item)
            self.add_child(li)


class DaisyList(Component):
    """DaisyUI list."""

    def __init__(self, items: List[str], **kwargs):
        super().__init__(tag="ul", **kwargs)
        self.add_class("list")
        self.add_class("bg-base-100")
        self.add_class("rounded-box")
        self.add_class("shadow-md")
        for item in items:
            li = Component(tag="li")
            li.add_class("list-row")
            content = Component(tag="div")
            content.add_child(item)
            li.add_child(content)
            self.add_child(li)


class DaisyHero(Component):
    """DaisyUI hero section."""

    def __init__(
        self,
        title: str,
        subtitle: Optional[str] = None,
        actions: Optional[List[Component]] = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("hero")
        self.add_class("bg-base-200")

        content = Component(tag="div")
        content.add_class("hero-content")
        content.add_class("text-center")

        inner = Component(tag="div")
        title_el = Component(tag="h1")
        title_el.add_class("text-5xl")
        title_el.add_class("font-bold")
        title_el.add_child(title)
        inner.add_child(title_el)

        if subtitle:
            subtitle_el = Component(tag="p")
            subtitle_el.add_class("py-6")
            subtitle_el.add_child(subtitle)
            inner.add_child(subtitle_el)

        if actions:
            action_row = Component(tag="div")
            for action in actions:
                action_row.add_child(action)
            inner.add_child(action_row)

        content.add_child(inner)
        self.add_child(content)


class DaisyStat(Component):
    """DaisyUI stat block."""

    def __init__(
        self,
        title: str,
        value: str,
        description: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("stats")
        self.add_class("shadow")

        stat = Component(tag="div")
        stat.add_class("stat")
        title_el = Component(tag="div")
        title_el.add_class("stat-title")
        title_el.add_child(title)
        stat.add_child(title_el)

        value_el = Component(tag="div")
        value_el.add_class("stat-value")
        value_el.add_child(value)
        stat.add_child(value_el)

        if description:
            desc_el = Component(tag="div")
            desc_el.add_class("stat-desc")
            desc_el.add_child(description)
            stat.add_child(desc_el)

        self.add_child(stat)


class DaisyPagination(Component):
    """DaisyUI pagination using join."""

    def __init__(self, pages: List[Union[str, int]], active: Optional[int] = None, **kwargs):
        super().__init__(tag="div", **kwargs)
        self.add_class("join")
        for page in pages:
            btn = Component(tag="button")
            btn.add_class("join-item")
            btn.add_class("btn")
            if active is not None and page == active:
                btn.add_class("btn-active")
            btn.add_child(str(page))
            self.add_child(btn)


class DaisyAccordion(Component):
    """DaisyUI collapse accordion item."""

    def __init__(
        self,
        title: str,
        content: Union[str, Component],
        open: bool = False,
        radio_name: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("collapse")
        self.add_class("bg-base-100")
        self.add_class("border-base-300")
        self.add_class("border")

        if radio_name:
            radio = Component(tag="input")
            radio.add_attribute(Attribute.TYPE, "radio")
            radio.add_attribute(Attribute.NAME, radio_name)
            if open:
                radio.add_attribute(Attribute.CHECKED, "checked")
            self.add_child(radio)

        title_el = Component(tag="div")
        title_el.add_class("collapse-title")
        title_el.add_class("font-semibold")
        title_el.add_child(title)
        self.add_child(title_el)

        content_el = Component(tag="div")
        content_el.add_class("collapse-content")
        if isinstance(content, Component):
            content_el.add_child(content)
        else:
            content_el.add_child(content)
        self.add_child(content_el)


class DaisyDropdown(Component):
    """DaisyUI dropdown menu."""

    def __init__(
        self,
        trigger: Component,
        items: List[Union[str, DaisyLink]],
        align: str = "end",
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("dropdown")
        if align == "end":
            self.add_class("dropdown-end")

        trigger.add_attribute("tabindex", "0")
        trigger.add_attribute(Attribute.ROLE, "button")
        self.add_child(trigger)

        menu = Component(tag="ul")
        menu.add_class("dropdown-content")
        menu.add_class("menu")
        menu.add_class("bg-base-100")
        menu.add_class("rounded-box")
        menu.add_class("z-1")
        menu.add_class("w-52")
        menu.add_class("p-2")
        menu.add_class("shadow-sm")
        menu.add_attribute("tabindex", "0")
        for item in items:
            li = Component(tag="li")
            li.add_child(item)
            menu.add_child(li)
        self.add_child(menu)