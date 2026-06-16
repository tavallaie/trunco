from html import escape
from typing import List, Optional, Tuple, Union

from trunco.alpine.enums import Directive
from trunco.base import Component
from trunco.daisy import Badge, Link, Table
from trunco.components.table import TableCellComponent, TableRowComponent

from docs.src.catalog import CATALOG, CatalogEntry
from docs.src.highlight import highlight_code


def paragraph(text: str) -> Component:
    el = Component(tag="p")
    el.add_child(text)
    return el


def _slug(text: str) -> str:
    return text.lower().replace(" ", "-")


def htmx_link(href: str, label: str, *, extra_classes: Optional[List[str]] = None) -> Component:
    link = Component(tag="a")
    link.add_attribute("href", href)
    link.add_child(label)
    link.add_attribute("hx-get", f"fragments/{href}")
    link.add_attribute("hx-target", "#main-content")
    link.add_attribute("hx-swap", "innerHTML show:window:top")
    link.add_attribute("hx-push-url", href)
    link.add_attribute("hx-indicator", "#htmx-progress")
    if extra_classes:
        for cls in extra_classes:
            link.add_class(cls)
    return link


class KitBadge(Component):
    """Consistent DaisyUI / 0build identity badge."""

    def __init__(self, kit: str, label: str, *, size: str = "sm"):
        super().__init__(tag="span")
        self.add_class("badge")
        self.add_class(f"badge-kit-{kit}")
        if size:
            self.add_class(f"badge-{size}" if size != "sm" else "badge-sm")
        self.add_child(label)


class KitButton(Component):
    """Preview button using kit brand colors."""

    def __init__(self, kit: str, label: str, *, size: str = "sm"):
        super().__init__(tag="button")
        self.add_attribute("type", "button")
        self.add_class("btn")
        self.add_class(f"btn-kit-{kit}")
        if size:
            self.add_class(f"btn-{size}")
        self.add_child(label)


class CodePanel(Component):
    """Dark syntax-highlighted code block with copy button (JS in layout)."""

    def __init__(
        self,
        code: str,
        language: str = "python",
        filename: Optional[str] = None,
    ):
        super().__init__(tag="div")
        self.add_class("code-panel")
        label = filename or language

        header = Component(tag="div")
        header.add_class("code-panel-header")
        badge = Component(tag="span")
        badge.add_child(label)
        header.add_child(badge)
        self.add_child(header)

        pre = Component(tag="pre")
        code_el = Component(tag="code")
        code_el.add_child(highlight_code(code, language=language, filename=filename))
        pre.add_child(code_el)
        self.add_child(pre)


class Breadcrumb(Component):
    def __init__(self, crumbs: List[Tuple[str, Optional[str]]]):
        super().__init__(tag="nav")
        self.add_class("doc-breadcrumb")
        self.add_attribute("aria-label", "Breadcrumb")
        sep = (
            '<svg class="doc-breadcrumb-sep" fill="none" viewBox="0 0 24 24" stroke-width="2" '
            'stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" '
            'stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg>'
        )
        for i, (label, href) in enumerate(crumbs):
            if i > 0:
                self.add_child(sep)
            if href:
                self.add_child(htmx_link(href, label))
            elif i == len(crumbs) - 1:
                current = Component(tag="span")
                current.add_class("doc-breadcrumb-current")
                current.add_child(label)
                self.add_child(current)
            else:
                span = Component(tag="span")
                span.add_child(label)
                self.add_child(span)


class Toc(Component):
    def __init__(self, items: List[Tuple[str, str]]):
        super().__init__(tag="aside")
        self.add_class("doc-toc")
        self.add_attribute("aria-label", "Table of contents")
        inner = Component(tag="div")
        inner.add_class("doc-toc-inner")
        title = Component(tag="p")
        title.add_class("doc-toc-title")
        title.add_child("On this page")
        inner.add_child(title)
        ul = Component(tag="ul")
        for anchor, label in items:
            li = Component(tag="li")
            a = Component(tag="a")
            a.add_attribute("href", f"#{anchor}")
            a.add_child(label)
            li.add_child(a)
            ul.add_child(li)
        inner.add_child(ul)
        self.add_child(inner)


class DocArticle(Component):
    """Documentation page with breadcrumb, header, prose, and optional TOC."""

    def __init__(
        self,
        title: str,
        *blocks: Union[Component, str],
        lead: Optional[str] = None,
        breadcrumb: Optional[List[Tuple[str, Optional[str]]]] = None,
        toc: Optional[List[Tuple[str, str]]] = None,
        header_extra: Optional[Component] = None,
    ):
        super().__init__(tag="div")
        self.add_class("doc-page")
        inner = Component(tag="div")
        inner.add_class("doc-page-inner")
        main = Component(tag="div")
        main.add_class("doc-page-main")

        if breadcrumb:
            main.add_child(Breadcrumb(breadcrumb))

        header = Component(tag="header")
        header.add_class("doc-page-header")
        head_inner = Component(tag="div")
        h1 = Component(tag="h1")
        h1.add_child(title)
        head_inner.add_child(h1)
        if lead:
            p = Component(tag="p")
            p.add_class("doc-page-lead")
            p.add_child(lead)
            head_inner.add_child(p)
        if header_extra:
            head_inner.add_child(header_extra)
        header.add_child(head_inner)
        main.add_child(header)

        prose = Component(tag="div")
        prose.add_class("doc-prose")
        prose.add_class("doc-stack")
        for block in blocks:
            prose.add_child(block)
        main.add_child(prose)
        inner.add_child(main)

        if toc:
            inner.add_child(Toc(toc))
        self.add_child(inner)


class DocLanding(Component):
    """Home / landing layout without breadcrumb."""

    def __init__(self, *blocks: Union[Component, str]):
        super().__init__(tag="div")
        self.add_class("doc-landing")
        stack = Component(tag="div")
        stack.add_class("doc-stack")
        for block in blocks:
            stack.add_child(block)
        self.add_child(stack)


class Section(Component):
    def __init__(
        self,
        title: str,
        *blocks: Union[Component, str],
        anchor: Optional[str] = None,
        badge: Optional[Component] = None,
    ):
        super().__init__(tag="section")
        self.add_class("doc-section")
        slug = anchor or _slug(title)
        if badge:
            self.add_child(badge)
        h2 = Component(tag="h2")
        h2.add_attribute("id", slug)
        h2.add_child(title)
        self.add_child(h2)
        for block in blocks:
            self.add_child(block)


class Callout(Component):
    def __init__(self, text: str):
        super().__init__(tag="div")
        self.add_class("doc-callout")
        p = Component(tag="p")
        p.add_child(text)
        self.add_child(p)


class NextSteps(Component):
    def __init__(self, links: List[Tuple[str, str, str]]):
        """links: (direction, title, href)"""
        super().__init__(tag="nav")
        self.add_class("doc-next-steps")
        self.add_attribute("aria-label", "Next steps")
        label = Component(tag="p")
        label.add_class("doc-next-steps-label")
        label.add_child("Next steps")
        self.add_child(label)
        grid = Component(tag="div")
        grid.add_class("doc-next-steps-grid")
        for direction, title, href in links:
            grid.add_child(
                htmx_link(
                    href,
                    f'<span class="doc-next-link-dir">{escape(direction)}</span>'
                    f'<span class="doc-next-link-title">{escape(title)}</span>',
                    extra_classes=["doc-next-link"],
                )
            )
        self.add_child(grid)


class PairGrid(Component):
    """Two-column headers + aligned code row (themes, integrations)."""

    def __init__(
        self,
        left_header: Component,
        right_header: Component,
        left_code: CodePanel,
        right_code: CodePanel,
    ):
        super().__init__(tag="div")
        self.add_class("doc-pair-grid")
        self.add_child(left_header)
        self.add_child(right_header)
        for panel in (left_code, right_code):
            wrap = Component(tag="div")
            wrap.add_class("doc-pair-code")
            wrap.add_child(panel)
            self.add_child(wrap)


class PairHeader(Component):
    def __init__(self, title: str, description: str, *, anchor: Optional[str] = None, badge: Optional[Component] = None):
        super().__init__(tag="div")
        self.add_class("doc-pair-header")
        if badge:
            self.add_child(badge)
        h2 = Component(tag="h2")
        if anchor:
            h2.add_attribute("id", anchor)
        h2.add_child(title)
        self.add_child(h2)
        p = Component(tag="p")
        p.add_child(description)
        self.add_child(p)


class HeroHome(Component):
    def __init__(self, title: str, lead: str, badge_text: str, actions: Component):
        super().__init__(tag="header")
        self.add_class("doc-hero")
        self.add_class("text-center")
        badge = Badge(badge_text, color="primary", outline=True)
        badge.add_class("mb-4")
        self.add_child(badge)
        h1 = Component(tag="h1")
        h1.add_child(title)
        self.add_child(h1)
        p = Component(tag="p")
        p.add_class("lead")
        p.add_class("mx-auto")
        p.add_child(lead)
        self.add_child(p)
        actions.add_class("actions")
        actions.add_class("justify-center")
        self.add_child(actions)


def _zbuild_live_preview(
    preview_html: str,
    *,
    portal_html: str = "",
) -> str:
    """Render 0build overlay demos in-page so modals cover the viewport."""
    from trunco.zbuild.assets import core_script_tag, kit_css_tag, zuikit_script_tag

    return (
        f'<div class="zbuild-live-preview z-layout-small bg color">'
        f"{kit_css_tag()}"
        f'<div class="preview-root preview-root--overlay">{preview_html}</div>'
        f"{portal_html}"
        f"{core_script_tag()}"
        f"{zuikit_script_tag()}"
        f"</div>"
    )


def _zbuild_iframe(
    preview_html: str,
    *,
    overlay: bool = False,
    portal_html: str = "",
    stretch: bool = False,
    full_width: bool = False,
) -> str:
    from trunco.zbuild.assets import core_script_tag, kit_css_tag, zuikit_script_tag

    body_style = (
        "margin:0;min-height:100%;padding:1rem;box-sizing:border-box;width:100%;"
        "background:var(--z-bg,#fff);color:var(--z-bg-f,#111);"
        "--bg:var(--z-bg);--color:var(--z-bg-f);"
    )
    if overlay:
        body_style += "overflow:visible;"
    use_stretch = (stretch or full_width) and not overlay
    if overlay:
        root_style = (
            "width:100%;min-height:100%;display:flex;align-items:center;"
            "justify-content:center;box-sizing:border-box;"
        )
        content_style = (
            ".preview-root--overlay > div{width:100%;min-height:100%;"
            "display:flex;align-items:center;justify-content:center;}"
        )
        root_class = "preview-root preview-root--overlay"
    elif use_stretch:
        root_style = (
            "width:100%;min-height:100%;display:flex;flex-direction:column;"
            "align-items:stretch;justify-content:flex-start;box-sizing:border-box;"
        )
        content_style = (
            ".preview-root--stretch > form,"
            ".preview-root--stretch > fieldset,"
            ".preview-root--stretch > ul,"
            ".preview-root--stretch > table,"
            ".preview-root--stretch > div:not(.z-modal){width:100%;max-width:18rem;margin:0 auto;}"
        )
        root_class = "preview-root preview-root--stretch"
    else:
        root_style = (
            "width:100%;min-height:100%;display:flex;align-items:center;"
            "justify-content:center;box-sizing:border-box;"
        )
        content_style = ""
        root_class = "preview-root"

    doc = f"""<!DOCTYPE html>
<html lang="en" class="z-layout-small bg color">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
{kit_css_tag()}
{core_script_tag()}
<style>
html,body{{height:100%;}}
body{{{body_style}}}
.{root_class.split()[0]}{{{root_style}}}
{content_style}
</style>
</head>
<body class="bg color">
<div class="{root_class}">{preview_html}</div>
{portal_html}
{zuikit_script_tag()}
</body>
</html>"""
    return (
        f'<iframe class="demo-iframe" title="0build preview" loading="lazy" '
        f'srcdoc="{escape(doc, quote=True)}"></iframe>'
    )


def _code_section_min_height(*codes: str) -> str:
    lines = max((code.count("\n") + 1 for code in codes if code), default=3)
    return f"{5.5 + lines * 1.45:.2f}rem"


def _showcase_code(
    code: str,
    filename: str,
    *,
    code_min_height: Optional[str] = None,
) -> Component:
    body = Component(tag="div")
    body.add_class("showcase-code")
    if code_min_height:
        body.add_style("min-height", code_min_height)
    body.add_child(CodePanel(code, filename=filename))
    return body


def _normalize_preview(html: str, kit: str) -> str:
    if kit == "daisy":
        return html.replace("btn-secondary", "btn-kit-daisy").replace("btn-primary", "btn-kit-daisy")
    return html.replace("btn-primary", "btn-kit-zbuild").replace("btn-secondary", "btn-kit-zbuild")


def _preview_box(
    preview_html: str,
    kit: str,
    height: int,
    *,
    stretch: bool = False,
    flush: bool = False,
    overlay: bool = False,
    full_width: bool = False,
    portal_html: str = "",
) -> Component:
    box = Component(tag="div")
    box.add_class("preview-box")
    box.add_class("border-0")
    box.add_style("--preview-h", f"{height}px")
    if stretch:
        box.add_class("preview-box--stretch")
    if flush:
        box.add_class("preview-box--flush")
    if overlay:
        box.add_class("preview-box--overlay")
    if full_width:
        box.add_class("preview-box--full-width")
    preview_html = _normalize_preview(preview_html, kit)
    slot = Component(tag="div")
    slot.add_class("preview-slot")
    if kit == "zbuild":
        if overlay or portal_html:
            slot.add_class("preview-slot--live-zbuild")
            slot.add_child(_zbuild_live_preview(preview_html, portal_html=portal_html))
        else:
            slot.add_child(
                _zbuild_iframe(
                    preview_html,
                    overlay=overlay,
                    portal_html=portal_html,
                    stretch=stretch,
                    full_width=full_width,
                )
            )
    else:
        slot.add_child(preview_html)
    box.add_child(slot)
    return box


def _kit_tab_panel(
    *,
    name: str,
    kit: str,
    label: str,
    preview_html: str,
    code: str,
    filename: str,
    height: int,
    checked: bool = False,
    stretch: bool = False,
    flush: bool = False,
    overlay: bool = False,
    full_width: bool = False,
    portal_html: str = "",
    code_min_height: Optional[str] = None,
) -> Tuple[Component, Component]:
    radio = Component(tag="input")
    radio.add_attribute("type", "radio")
    radio.add_attribute("name", name)
    radio.add_attribute("role", "tab")
    radio.add_class("tab")
    radio.add_attribute("aria-label", label)
    if checked:
        radio.add_attribute("checked", "checked")

    panel = Component(tag="div")
    panel.add_attribute("role", "tabpanel")
    panel.add_class("tab-content")
    panel.add_class("bg-base-100")
    panel.add_class("showcase-panel")
    panel.add_child(
        _preview_box(
            preview_html,
            kit,
            height,
            stretch=stretch,
            flush=flush,
            overlay=overlay,
            full_width=full_width,
            portal_html=portal_html,
        )
    )
    panel.add_child(_showcase_code(code, filename, code_min_height=code_min_height))
    return radio, panel


def _single_kit_panel(
    *,
    kit: str,
    preview_html: str,
    code: str,
    filename: str,
    height: int,
    stretch: bool = False,
    flush: bool = False,
    overlay: bool = False,
    full_width: bool = False,
    portal_html: str = "",
) -> Component:
    panel = Component(tag="div")
    panel.add_class("showcase-panel")
    panel.add_child(
        _preview_box(
            preview_html,
            kit,
            height,
            stretch=stretch,
            flush=flush,
            overlay=overlay,
            full_width=full_width,
            portal_html=portal_html,
        )
    )
    panel.add_child(
        _showcase_code(code, filename, code_min_height=_code_section_min_height(code))
    )
    return panel


class CatalogShowcase(Component):
    """Radio-tabbed kit demo — preview + code switch together."""

    def __init__(self, entry: CatalogEntry, *, tab_name: Optional[str] = None, in_grid: bool = True):
        demo = entry.demo()
        super().__init__(tag="article")
        self.add_class("showcase-card")
        self.add_attribute("id", entry.slug)
        if in_grid:
            self.add_directive(
                Directive.X_SHOW,
                f"(!filter || filter === 'all' || filter === '{entry.availability}') && "
                f"(!query || '{entry.name}'.toLowerCase().includes(query.toLowerCase()))",
            )

        head = Component(tag="div")
        head.add_class("card-head")
        h3 = Component(tag="h3")
        h3.add_class("card-title")
        h3.add_child(entry.name)
        head.add_child(h3)
        desc = Component(tag="p")
        desc.add_class("card-desc")
        desc.add_child(entry.description)
        head.add_child(desc)

        meta = Component(tag="div")
        meta.add_class("flex")
        meta.add_class("gap-2")
        meta.add_class("mt-2")
        if entry.availability == "both":
            meta.add_child(KitBadge("daisy", "DaisyUI"))
            meta.add_child(KitBadge("zbuild", "0build"))
        elif entry.availability == "daisy":
            meta.add_child(KitBadge("daisy", "DaisyUI only"))
        else:
            meta.add_child(KitBadge("zbuild", "0build only"))
        head.add_child(meta)
        self.add_child(head)

        tabs_name = tab_name or f"tabs-{entry.slug}"
        tabs = Component(tag="div")
        tabs.add_attribute("role", "tablist")
        tabs.add_class("tabs")
        tabs.add_class("tabs-lifted")
        tabs.add_class("px-6")
        tabs.add_class("mt-3")

        if entry.availability == "both":
            stretch = (
                demo.preview_full_width
                or demo.preview_height >= 160
                or entry.slug in ("table", "menu", "navbar", "dropdown", "form", "formcontrol", "fieldset")
            )
            flush = entry.slug in ("hero", "navbar")
            overlay = demo.preview_overlay
            full_width = demo.preview_full_width
            portal_html = demo.zbuild_portal or ""
            code_min_height = _code_section_min_height(demo.daisy_code, demo.zbuild_code)
            if demo.daisy_code and demo.daisy_preview:
                r, p = _kit_tab_panel(
                    name=tabs_name,
                    kit="daisy",
                    label="DaisyUI",
                    preview_html=demo.daisy_preview,
                    code=demo.daisy_code,
                    filename="daisy.py",
                    height=demo.preview_height,
                    checked=True,
                    stretch=stretch,
                    flush=flush,
                    overlay=overlay,
                    full_width=full_width,
                    portal_html="",
                    code_min_height=code_min_height,
                )
                tabs.add_child(r)
                tabs.add_child(p)
            if demo.zbuild_code and demo.zbuild_preview:
                r, p = _kit_tab_panel(
                    name=tabs_name,
                    kit="zbuild",
                    label="0build",
                    preview_html=demo.zbuild_preview,
                    code=demo.zbuild_code,
                    filename="zbuild.py",
                    height=demo.preview_height,
                    stretch=stretch,
                    flush=flush,
                    overlay=overlay,
                    full_width=full_width,
                    portal_html=portal_html,
                    code_min_height=code_min_height,
                )
                tabs.add_child(r)
                tabs.add_child(p)
        elif entry.availability == "daisy" and demo.daisy_code:
            stretch = demo.preview_height >= 160 or entry.slug in ("menu", "navbar", "dropdown", "list")
            flush = entry.slug in ("hero", "navbar")
            self.add_child(
                _single_kit_panel(
                    kit="daisy",
                    preview_html=demo.daisy_preview or "",
                    code=demo.daisy_code,
                    filename="daisy.py",
                    height=demo.preview_height,
                    stretch=stretch,
                    flush=flush,
                )
            )
            return
        elif entry.availability == "zbuild" and demo.zbuild_code:
            self.add_child(
                _single_kit_panel(
                    kit="zbuild",
                    preview_html=demo.zbuild_preview or "",
                    code=demo.zbuild_code,
                    filename="zbuild.py",
                    height=demo.preview_height,
                )
            )
            return

        self.add_child(tabs)


def _title(title: str, desc: str) -> Component:
    wrap = Component(tag="div")
    h = Component(tag="h3")
    h.add_class("card-title")
    h.add_child(title)
    wrap.add_child(h)
    p = Component(tag="p")
    p.add_class("card-desc")
    p.add_child(desc)
    wrap.add_child(p)
    badges = Component(tag="div")
    badges.add_class("flex")
    badges.add_class("gap-2")
    badges.add_class("mt-2")
    badges.add_child(KitBadge("daisy", "DaisyUI"))
    badges.add_child(KitBadge("zbuild", "0build"))
    wrap.add_child(badges)
    return wrap


class HomeButtonDemo(Component):
    def __init__(self):
        import trunco.daisy as daisy
        import trunco.zbuild as zbuild

        super().__init__(tag="section")
        self.add_class("showcase-card")
        head = Component(tag="div")
        head.add_class("card-head")
        h3 = Component(tag="h3")
        h3.add_class("card-title")
        h3.add_child("Button")
        head.add_child(h3)
        desc = Component(tag="p")
        desc.add_class("card-desc")
        desc.add_child("Same API — different CSS kits.")
        head.add_child(desc)
        meta = Component(tag="div")
        meta.add_class("flex")
        meta.add_class("gap-2")
        meta.add_class("mt-2")
        meta.add_child(KitBadge("daisy", "DaisyUI"))
        meta.add_child(KitBadge("zbuild", "0build"))
        head.add_child(meta)
        self.add_child(head)

        tabs = Component(tag="div")
        tabs.add_attribute("role", "tablist")
        tabs.add_class("tabs")
        tabs.add_class("tabs-lifted")
        tabs.add_class("px-6")
        tabs.add_class("mt-3")

        daisy_preview = daisy.Button(label="Get started", color="primary", size="sm").render()
        zbuild_preview = zbuild.Button(label="Get started", color="primary", size="small").render()
        daisy_code = 'from trunco.daisy import Button\n\nButton(label="Get started", color="primary")'
        zbuild_code = 'from trunco.zbuild import Button\n\nButton(label="Get started", color="primary")'

        code_min_height = _code_section_min_height(daisy_code, zbuild_code)
        r1, p1 = _kit_tab_panel(
            name="demo-btn",
            kit="daisy",
            label="DaisyUI",
            preview_html=daisy_preview,
            code=daisy_code,
            filename="daisy.py",
            height=100,
            checked=True,
            code_min_height=code_min_height,
        )
        r2, p2 = _kit_tab_panel(
            name="demo-btn",
            kit="zbuild",
            label="0build",
            preview_html=zbuild_preview,
            code=zbuild_code,
            filename="zbuild.py",
            height=100,
            code_min_height=code_min_height,
        )
        tabs.add_child(r1)
        tabs.add_child(p1)
        tabs.add_child(r2)
        tabs.add_child(p2)
        self.add_child(tabs)


class AvailabilityTable(Component):
    def __init__(self, entries: Optional[List[CatalogEntry]] = None):
        super().__init__(tag="div")
        self.add_class("overflow-x-auto")
        self.add_class("rounded-lg")
        self.add_class("border")
        self.add_class("border-base-300")
        items = entries or CATALOG
        rows = []
        for entry in items:
            d = "yes" if entry.availability in ("both", "daisy") else "—"
            z = "yes" if entry.availability in ("both", "zbuild") else "—"
            rows.append(
                TableRowComponent(
                    cells=[
                        TableCellComponent(content=f'<a href="#{entry.slug}" class="link">{entry.name}</a>'),
                        TableCellComponent(content=entry.category),
                        TableCellComponent(content=d),
                        TableCellComponent(content=z),
                    ]
                )
            )
        self.add_child(Table(headers=["Component", "Category", "DaisyUI", "0build"], rows=rows, zebra=True))


class KitFilterBar(Component):
    def __init__(self):
        super().__init__(tag="div")
        self.add_class("filter-bar")
        search = Component(tag="input")
        search.add_attribute("type", "search")
        search.add_attribute("placeholder", "Search components…")
        search.add_class("input")
        search.add_class("input-bordered")
        search.add_class("w-full")
        search.add_class("max-w-md")
        search.add_directive("x-model", "query")
        self.add_child(search)
        tabs = Component(tag="div")
        tabs.add_class("tabs")
        tabs.add_class("tabs-boxed")
        tabs.add_class("mt-3")
        for key, label in (
            ("all", "All"),
            ("both", "Shared"),
            ("daisy", "DaisyUI only"),
            ("zbuild", "0build only"),
        ):
            tab = Component(tag="button")
            tab.add_class("tab")
            tab.add_attribute("type", "button")
            tab.add_directive(Directive.X_ON_CLICK, f"filter = '{key}'")
            tab.add_directive("x-bind:class", f"{{ 'tab-active': filter === '{key}' }}")
            tab.add_child(label)
            tabs.add_child(tab)
        self.add_child(tabs)


class ShowcaseGrid(Component):
    def __init__(self, *showcases: Component):
        super().__init__(tag="div")
        self.add_class("doc-stack")
        self.add_directive(Directive.X_DATA, "{ filter: 'all', query: '' }")
        self.add_child(KitFilterBar())
        for item in showcases:
            self.add_child(item)


class FeatureGrid(Component):
    def __init__(self, items: List[Tuple[str, str, str]]):
        """(badge_label, title, body)"""
        super().__init__(tag="div")
        self.add_class("feature-grid")
        for badge_label, title, body in items:
            badge = Badge(badge_label, color="ghost", size="sm")
            badge.add_class("mb-2")
            # prepend badge - rebuild as custom card
            c = Component(tag="div")
            c.add_class("card")
            c.add_class("feature-card")
            c.add_class("bg-base-100")
            inner = Component(tag="div")
            inner.add_class("card-body")
            inner.add_child(badge)
            t = Component(tag="h2")
            t.add_class("card-title")
            t.add_class("text-lg")
            t.add_child(title)
            inner.add_child(t)
            p = Component(tag="p")
            p.add_class("text-sm")
            p.add_class("opacity-70")
            p.add_child(body)
            inner.add_child(p)
            c.add_child(inner)
            self.add_child(c)


class StatRow(Component):
    def __init__(self, stats: List[Tuple[str, str, str]]):
        super().__init__(tag="div")
        self.add_class("stats")
        self.add_class("stats-vertical")
        self.add_class("lg:stats-horizontal")
        self.add_class("hero-stats")
        self.add_class("w-full")
        self.add_class("bg-base-100")
        for title, value, desc in stats:
            stat = Component(tag="div")
            stat.add_class("stat")
            st = Component(tag="div")
            st.add_class("stat-title")
            st.add_child(title)
            stat.add_child(st)
            sv = Component(tag="div")
            sv.add_class("stat-value")
            if value == "2":
                sv.add_class("text-primary")
            sv.add_child(value)
            stat.add_child(sv)
            sd = Component(tag="div")
            sd.add_class("stat-desc")
            sd.add_child(desc)
            stat.add_child(sd)
            self.add_child(stat)


class LinkList(Component):
    def __init__(self, items: List[tuple]):
        super().__init__(tag="ul")
        self.add_class("menu")
        self.add_class("bg-base-100")
        self.add_class("rounded-lg")
        self.add_class("border")
        self.add_class("border-base-300")
        for label, href in items:
            li = Component(tag="li")
            if href.startswith("http"):
                li.add_child(Link(href=href, text=label, target="_blank"))
            else:
                li.add_child(htmx_link(href, label))
            self.add_child(li)


# Backward-compatible aliases
CodeBlock = CodePanel
DocPageContent = DocArticle
PageHero = DocArticle
Prose = DocArticle
KitShowcase = CatalogShowcase
SingleKitShowcase = CatalogShowcase
Demo = CatalogShowcase