from trunco.base import Component
from trunco.components.link import LinkComponent
from trunco.components.table import TableComponent, TableRowComponent
from trunco.enums import Attribute
from trunco.kits.color import resolve_color


class ZbuildLink(LinkComponent):
    """0build link."""

    STYLES = ("muted", "text", "heading", "reset")

    def __init__(
        self,
        href: str,
        text: str = "{text}",
        target: str = "_self",
        color: str | None = None,
        style: str | None = None,
        **kwargs,
    ):
        super().__init__(href=href, text=text, target=target, **kwargs)
        tone = resolve_color(color=color, variant=style)
        self.add_class("z-link")
        if tone in self.STYLES:
            self.add_class(f"z-link-{tone}")


class ZbuildBadge(Component):
    """0build badge."""

    STYLES = ("danger", "warning", "success", "info")

    def __init__(
        self,
        text: str,
        color: str | None = None,
        style: str | None = None,
        **kwargs,
    ):
        super().__init__(tag="span", **kwargs)
        tone = resolve_color(color=color, variant=style)
        self.add_class("z-badge")
        if tone in self.STYLES:
            self.add_class(f"z-badge-{tone}")
        self.add_child(text)


class ZbuildAlert(Component):
    """0build alert."""

    STYLES = ("danger", "warning", "success", "info")

    def __init__(
        self,
        message: str,
        color: str | None = None,
        style: str | None = None,
        closable: bool = False,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        tone = resolve_color(color=color, variant=style)
        self.add_class("z-alert")
        self.add_attribute("data-z-alert", "")
        if tone in self.STYLES:
            self.add_class(f"z-alert-{tone}")
        if closable:
            close_btn = Component(tag="a")
            close_btn.add_class("z-alert-close")
            close_btn.add_attribute(Attribute.HREF, "")
            self.add_child(close_btn)
        self.add_child(message)


class ZbuildProgress(Component):
    """0build progress bar."""

    def __init__(self, value: int = 0, **kwargs):
        super().__init__(tag="progress", **kwargs)
        self.add_class("z-progress")
        self.add_attribute(Attribute.VALUE, str(value))
        self.add_attribute("max", "100")

    def render(self, context=None) -> str:
        return super().render(context).replace(f"</{self.tag}>", "")


class ZbuildAvatar(Component):
    """0build avatar."""

    def __init__(self, image_src: str, alt: str = "", **kwargs):
        super().__init__(tag="div", **kwargs)
        self.add_class("z-avatar")
        image = Component(tag="img")
        image.add_class("z-avatar-image")
        image.add_attribute(Attribute.SRC, image_src)
        if alt:
            image.add_attribute(Attribute.ALT, alt)
        self.add_child(image)


class ZbuildBreadcrumb(Component):
    """0build breadcrumb navigation."""

    def __init__(self, items: list[str | ZbuildLink], **kwargs):
        super().__init__(tag="ul", **kwargs)
        self.add_class("z-breadcrumb")
        for item in items:
            li = Component(tag="li")
            if isinstance(item, ZbuildLink):
                li.add_child(item)
            else:
                li.add_child(item)
            self.add_child(li)


class ZbuildTable(TableComponent):
    """0build table."""

    STYLES = ("divider", "striped", "hover", "small", "justify", "middle")

    def __init__(
        self,
        headers: list[str] | None = None,
        rows: list[TableRowComponent] | None = None,
        striped: bool = False,
        hover: bool = False,
        small: bool = False,
        **kwargs,
    ):
        super().__init__(headers=headers, rows=rows, **kwargs)
        self.add_class("z-table")
        if striped:
            self.add_class("z-table-striped")
        if hover:
            self.add_class("z-table-hover")
        if small:
            self.add_class("z-table-small")


class ZbuildSpinner(Component):
    """0build loading spinner."""

    def __init__(self, **kwargs):
        super().__init__(tag="div", **kwargs)
        self.add_attribute("data-z-spinner", "")


class ZbuildTooltip(Component):
    """0build tooltip — marks the trigger with ``data-z-tooltip`` for zUIkit.

    zUIkit creates the ``.z-tooltip`` popup on hover/focus; it is not part of
    the static HTML like DaisyUI's ``data-tip`` wrapper.
    """

    POSITIONS = ("top", "bottom", "left", "right")

    def __init__(
        self,
        tip: str,
        child: Component,
        position: str = "top",
        delay: int | None = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.tip = tip
        self.child = child
        self.position = position
        self.delay = delay

    def _tooltip_attr(self) -> str:
        if (
            self.position == "top"
            and self.delay is None
            and ":" not in self.tip
            and ";" not in self.tip
        ):
            return self.tip
        parts = [f"title: {self.tip}"]
        if self.position in self.POSITIONS and self.position != "top":
            parts.append(f"pos: {self.position}")
        if self.delay is not None:
            parts.append(f"delay: {self.delay}")
        return "; ".join(parts)

    def render(self, context=None) -> str:
        self.child.add_attribute("data-z-tooltip", self._tooltip_attr())
        return self.child.render(context)


class ZbuildModal(Component):
    """0build modal dialog."""

    def __init__(
        self,
        modal_id: str,
        title: str,
        body: str | Component,
        footer: list[Component] | None = None,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_attribute("id", modal_id.lstrip("#"))
        self.add_class("z-modal")
        self.add_class("z-flex-top")
        self.add_attribute("data-z-modal", "container: false")

        dialog = Component(tag="div")
        dialog.add_class("z-modal-dialog")
        dialog.add_class("z-margin-auto-vertical")

        header = Component(tag="div")
        header.add_class("z-modal-header")
        title_el = Component(tag="h2")
        title_el.add_class("z-modal-title")
        title_el.add_child(title)
        header.add_child(title_el)
        close_btn = Component(tag="button")
        close_btn.add_class("z-modal-close")
        close_btn.add_class("z-close")
        close_btn.add_attribute(Attribute.TYPE, "button")
        close_btn.add_attribute("aria-label", "Close")
        close_btn.add_child("×")
        header.add_child(close_btn)
        dialog.add_child(header)

        body_el = Component(tag="div")
        body_el.add_class("z-modal-body")
        if isinstance(body, Component):
            body_el.add_child(body)
        else:
            body_el.add_child(body)
        dialog.add_child(body_el)

        if footer:
            footer_el = Component(tag="div")
            footer_el.add_class("z-modal-footer")
            footer_el.add_class("z-text-right")
            for item in footer:
                footer_el.add_child(item)
            dialog.add_child(footer_el)

        self.add_child(dialog)

    @staticmethod
    def trigger(
        modal_id: str,
        label: str = "Open modal",
        *,
        color: str = "primary",
        size: str = "small",
    ) -> Component:
        """Return an anchor that toggles a modal by ``href`` + ``data-z-toggle``."""
        link = Component(tag="a")
        link.add_attribute("href", f"#{modal_id.lstrip('#')}")
        link.add_attribute("data-z-toggle", "")
        link.add_class("z-button")
        link.add_class(f"z-button-{color}")
        if size:
            link.add_class(f"z-button-{size}")
        link.add_child(label)
        return link


class ZbuildNav(Component):
    """0build navigation."""

    def __init__(self, items: list[str | ZbuildLink | Component], **kwargs):
        super().__init__(tag="ul", **kwargs)
        self.add_class("z-nav")
        for item in items:
            li = Component(tag="li")
            if isinstance(item, (ZbuildLink, Component)):
                li.add_child(item)
            else:
                link = ZbuildLink(href="#", text=item)
                li.add_child(link)
            self.add_child(li)


class ZbuildTab(Component):
    """0build tab navigation."""

    def __init__(self, tabs: list[tuple], **kwargs):
        super().__init__(tag="ul", **kwargs)
        self.add_class("z-tab")
        for label, target, active in tabs:
            li = Component(tag="li")
            if active:
                li.add_class("z-active")
            link = Component(tag="a")
            link.add_attribute(Attribute.HREF, f"#{target}")
            link.add_child(label)
            li.add_child(link)
            self.add_child(li)


class ZbuildAccordion(Component):
    """Single 0build accordion panel — use inside :class:`ZbuildAccordionGroup`."""

    def __init__(
        self,
        title: str,
        content: str | Component,
        open: bool = False,
        **kwargs,
    ):
        super().__init__(tag="li", **kwargs)
        if open:
            self.add_class("z-open")

        title_el = Component(tag="a")
        title_el.add_class("z-accordion-title")
        title_el.add_attribute(Attribute.HREF, "")
        title_el.add_child(title)
        self.add_child(title_el)

        content_el = Component(tag="div")
        content_el.add_class("z-accordion-content")
        if isinstance(content, Component):
            content_el.add_child(content)
        else:
            content_el.add_child(content)
        self.add_child(content_el)


class ZbuildAccordionGroup(Component):
    """0build accordion container — wraps multiple :class:`ZbuildAccordion` items."""

    def __init__(
        self,
        *items: ZbuildAccordion,
        multiple: bool = False,
        **kwargs,
    ):
        super().__init__(tag="ul", **kwargs)
        self.add_attribute("data-z-accordion", "")
        if multiple:
            self.add_attribute("data-z-accordion", "multiple: true")
        for item in items:
            self.add_child(item)


class ZbuildDivider(Component):
    """0build divider — use ``horizontal=False`` for a vertical rule in flex rows."""

    def __init__(
        self,
        text: str | None = None,
        horizontal: bool = True,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        if not horizontal:
            # z-divider-vertical defaults to 100px tall — override to match button height.
            line_height = "0.5rem"
            if text:
                self.add_class("display-inline-flex")
                self.add_class("flex-col")
                self.add_class("items-center")
                self.add_style("gap", "0.125rem")
                self.add_style("padding", "0 0.5rem")
                self.add_style("align-self", "center")
                for _ in range(2):
                    line = Component(tag="div")
                    line.add_class("z-divider-vertical")
                    line.add_style("--z-divider-vertical-height", line_height)
                    line.add_style("height", line_height)
                    self.add_child(line)
                    if _ == 0 and text:
                        label = Component(tag="span")
                        label.add_style("font-size", "0.75rem")
                        label.add_style("line-height", "1")
                        label.add_child(text)
                        self.add_child(label)
            else:
                self.add_class("z-divider-vertical")
                self.add_style("--z-divider-vertical-height", "1.75rem")
                self.add_style("height", "1.75rem")
                self.add_style("align-self", "center")
        else:
            self.add_class("z-divider-small")
            if text:
                self.add_child(text)
