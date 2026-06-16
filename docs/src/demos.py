"""Live component demos for documentation pages."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Optional

import trunco.daisy as daisy
import trunco.zbuild as zbuild
from trunco.base import Component
from trunco.components.table import TableCellComponent, TableRowComponent


@dataclass(frozen=True)
class DemoResult:
    """Rendered demo payload for one catalog entry."""

    daisy_code: Optional[str] = None
    daisy_preview: Optional[str] = None
    zbuild_code: Optional[str] = None
    zbuild_preview: Optional[str] = None
    preview_height: int = 120
    preview_overlay: bool = False
    preview_full_width: bool = False
    zbuild_portal: Optional[str] = None


def _row(*cells: str) -> TableRowComponent:
    return TableRowComponent(cells=[TableCellComponent(content=c) for c in cells])


def _inline_row(*blocks) -> str:
    row = Component(tag="div")
    row.add_class("flex")
    row.add_class("items-center")
    row.add_class("justify-center")
    row.add_class("gap-3")
    row.add_class("w-full")
    row.add_class("max-w-sm")
    for block in blocks:
        row.add_child(block)
    return row.render()


def _zbuild_inline_row(*blocks) -> str:
    """Horizontal row using 0build kit flex utilities (no Tailwind gap-*)."""
    row = Component(tag="div")
    row.add_class("display-flex")
    row.add_class("flex-row")
    row.add_class("items-center")
    row.add_class("justify-center")
    row.add_class("w-full")
    row.add_class("max-w-sm")
    row.add_style("gap", "0.75rem")
    for block in blocks:
        row.add_child(block)
    return row.render()


def _daisy_modal_preview(
    *,
    modal_id: str,
    title: str,
    body: str,
    trigger_label: str = "Open modal",
) -> str:
    trigger = daisy.Button(label=trigger_label, color="primary", size="sm")
    trigger.add_attribute("onclick", f"document.getElementById('{modal_id}').showModal()")
    cancel = daisy.Button(label="Cancel", color="ghost", size="sm")
    cancel_form = Component(tag="form")
    cancel_form.add_attribute("method", "dialog")
    cancel_form.add_child(cancel)
    modal = daisy.Modal(
        modal_id=modal_id,
        title=title,
        body=body,
        actions=[
            cancel_form,
            daisy.Button(label="Confirm", color="primary", size="sm"),
        ],
    )
    wrap = Component(tag="div")
    wrap.add_class("flex")
    wrap.add_class("items-center")
    wrap.add_class("justify-center")
    wrap.add_class("w-full")
    wrap.add_child(trigger)
    return wrap.render() + modal.render()


def _zbuild_modal_preview(
    *,
    modal_id: str,
    title: str,
    body: str,
    trigger_label: str = "Open modal",
) -> tuple[str, str]:
    trigger = zbuild.Modal.trigger(modal_id, trigger_label)
    cancel = zbuild.Button(label="Cancel", size="small")
    cancel.add_class("z-modal-close")
    modal = zbuild.Modal(
        modal_id=modal_id,
        title=title,
        body=body,
        footer=[
            cancel,
            zbuild.Button(label="Confirm", color="primary", size="small"),
        ],
    )
    wrap = Component(tag="div")
    wrap.add_class("display-flex")
    wrap.add_class("flex-row")
    wrap.add_class("items-center")
    wrap.add_class("justify-center")
    wrap.add_class("w-full")
    wrap.add_child(trigger)
    return wrap.render(), modal.render()


def _daisy_divider_preview() -> str:
    return _inline_row(
        daisy.Button(label="Sign up", color="primary", size="sm"),
        daisy.Divider(text="OR", horizontal=False),
        daisy.Button(label="Log in", color="ghost", size="sm"),
    )


def _zbuild_divider_preview() -> str:
    return _zbuild_inline_row(
        zbuild.Button(label="Sign up", color="primary", size="small"),
        zbuild.Divider(text="OR", horizontal=False),
        zbuild.Button(label="Log in", color="default", size="small"),
    )


# ── Shared UI ────────────────────────────────────────────────────────────────


def button_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Button\n\nButton(label="Save", color="primary", size="sm")',
        daisy_preview=daisy.Button(label="Save", color="primary", size="sm").render(),
        zbuild_code='from trunco.zbuild import Button\n\nButton(label="Save", color="primary", size="small")',
        zbuild_preview=zbuild.Button(label="Save", color="primary", size="small").render(),
        preview_height=100,
    )


def input_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Input\n\nInput(placeholder="you@example.com", color="bordered")',
        daisy_preview=daisy.Input(placeholder="you@example.com", color="bordered").render(),
        zbuild_code='from trunco.zbuild import Input\n\nInput(placeholder="you@example.com")',
        zbuild_preview=zbuild.Input(placeholder="you@example.com").render(),
        preview_height=100,
    )


def card_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Card\n\nCard(title="Trunco", body="Python components.")',
        daisy_preview=daisy.Card(title="Trunco", body="Python components.").render(),
        zbuild_code='from trunco.zbuild import Card\n\nCard(title="Trunco", body="Python components.")',
        zbuild_preview=zbuild.Card(title="Trunco", body="Python components.").render(),
        preview_height=180,
    )


def badge_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Badge\n\nBadge("New", color="primary")',
        daisy_preview=daisy.Badge("New", color="primary").render(),
        zbuild_code='from trunco.zbuild import Badge\n\nBadge("New", color="info")',
        zbuild_preview=zbuild.Badge("New", color="info").render(),
        preview_height=90,
    )


def alert_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Alert\n\nAlert(message="Saved.", color="success")',
        daisy_preview=daisy.Alert(message="Saved.", color="success").render(),
        zbuild_code='from trunco.zbuild import Alert\n\nAlert(message="Saved.", color="success")',
        zbuild_preview=zbuild.Alert(message="Saved.", color="success").render(),
        preview_height=110,
    )


def link_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Link\n\nLink(href="/docs", text="Read docs", color="primary")',
        daisy_preview=daisy.Link(href="/docs", text="Read docs", color="primary").render(),
        zbuild_code='from trunco.zbuild import Link\n\nLink(href="/docs", text="Read docs")',
        zbuild_preview=zbuild.Link(href="/docs", text="Read docs").render(),
        preview_height=90,
    )


def progress_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Progress\n\nProgress(value=65, color="primary")',
        daisy_preview=daisy.Progress(value=65, color="primary").render(),
        zbuild_code="from trunco.zbuild import Progress\n\nProgress(value=65)",
        zbuild_preview=zbuild.Progress(value=65).render(),
        preview_height=90,
    )


def avatar_demo() -> DemoResult:
    src = "https://img.daisyui.com/images/profile/demo/avatar-1.jpg"
    return DemoResult(
        daisy_code=f'from trunco.daisy import Avatar\n\nAvatar(image_src="{src}")',
        daisy_preview=daisy.Avatar(image_src=src).render(),
        zbuild_code=f'from trunco.zbuild import Avatar\n\nAvatar(image_src="{src}")',
        zbuild_preview=zbuild.Avatar(image_src=src).render(),
        preview_height=110,
    )


def table_demo() -> DemoResult:
    rows = [
        _row("Trunco", "1.0.0", "Active"),
        _row("DaisyUI kit", "—", "Stable"),
        _row("0build kit", "—", "Stable"),
        _row("HTMX helpers", "—", "Optional"),
        _row("Alpine helpers", "—", "Optional"),
    ]
    d_code = """from trunco.daisy import Table
from trunco.components.table import TableRowComponent, TableCellComponent

rows = [TableRowComponent(cells=[TableCellComponent("Trunco"), ...])]
Table(headers=["Name", "Version", "Status"], rows=rows, zebra=True)"""
    z_code = """from trunco.zbuild import Table
from trunco.components.table import TableRowComponent, TableCellComponent

rows = [TableRowComponent(cells=[TableCellComponent("Trunco"), ...])]
Table(headers=["Name", "Version", "Status"], rows=rows, striped=True)"""
    return DemoResult(
        daisy_code=d_code,
        daisy_preview=daisy.Table(
            headers=["Name", "Version", "Status"], rows=rows, zebra=True
        ).render(),
        zbuild_code=z_code,
        zbuild_preview=zbuild.Table(
            headers=["Name", "Version", "Status"], rows=rows, striped=True
        ).render(),
        preview_height=220,
    )


def tooltip_demo() -> DemoResult:
    d_btn = daisy.Button(label="Hover me", color="primary", size="sm")
    z_btn = zbuild.Button(label="Hover me", color="primary", size="small")
    return DemoResult(
        daisy_code='from trunco.daisy import Tooltip, Button\n\nTooltip(tip="Hello", child=Button(label="Hover me"))',
        daisy_preview=daisy.Tooltip(tip="Hello", child=d_btn).render(),
        zbuild_code='from trunco.zbuild import Tooltip, Button\n\nTooltip(tip="Hello", child=Button(label="Hover me"))',
        zbuild_preview=zbuild.Tooltip(tip="Hello", child=z_btn).render(),
        preview_height=110,
        preview_overlay=True,
    )


def modal_demo() -> DemoResult:
    d_code = """from trunco.daisy import Modal, Button

trigger = Button(label="Open modal", color="primary")
trigger.add_attribute("onclick", 'document.getElementById("confirm").showModal()')

Modal(
    modal_id="confirm",
    title="Delete item?",
    body="This action cannot be undone.",
    actions=[
        Button(label="Cancel", color="ghost"),
        Button(label="Delete", color="primary"),
    ],
)"""
    z_code = """from trunco.zbuild import Modal, Button

trigger = Modal.trigger("confirm", "Open modal")
cancel = Button(label="Cancel", size="small")
cancel.add_class("z-modal-close")

Modal(
    modal_id="confirm",
    title="Delete item?",
    body="This action cannot be undone.",
    footer=[cancel, Button(label="Delete", color="primary", size="small")],
)"""
    z_trigger, z_modal = _zbuild_modal_preview(
        modal_id="demo-z",
        title="Delete item?",
        body="This action cannot be undone.",
    )
    return DemoResult(
        daisy_code=d_code,
        daisy_preview=_daisy_modal_preview(
            modal_id="demo-d",
            title="Delete item?",
            body="This action cannot be undone.",
        ),
        zbuild_code=z_code,
        zbuild_preview=z_trigger,
        zbuild_portal=z_modal,
        preview_height=280,
        preview_overlay=True,
    )


def accordion_demo() -> DemoResult:
    d_code = """from trunco.daisy import Accordion

Accordion(title="Shipping", content="Ships in 2–3 days.", open=True, radio_name="faq")
Accordion(title="Returns", content="30-day return policy.", radio_name="faq")
Accordion(title="Support", content="Email support@example.com", radio_name="faq")"""
    z_code = """from trunco.zbuild import Accordion, AccordionGroup

AccordionGroup(
    Accordion(title="Shipping", content="Ships in 2–3 days.", open=True),
    Accordion(title="Returns", content="30-day return policy."),
    Accordion(title="Support", content="Email support@example.com"),
)"""
    d_preview = (
        daisy.Accordion(
            title="Shipping", content="Ships in 2–3 days.", open=True, radio_name="faq"
        ).render()
        + daisy.Accordion(
            title="Returns", content="30-day return policy.", radio_name="faq"
        ).render()
        + daisy.Accordion(
            title="Support", content="Email support@example.com", radio_name="faq"
        ).render()
    )
    z_preview = zbuild.AccordionGroup(
        zbuild.Accordion(title="Shipping", content="Ships in 2–3 days.", open=True),
        zbuild.Accordion(title="Returns", content="30-day return policy."),
        zbuild.Accordion(title="Support", content="Email support@example.com"),
    ).render()
    return DemoResult(
        daisy_code=d_code,
        daisy_preview=d_preview,
        zbuild_code=z_code,
        zbuild_preview=z_preview,
        preview_height=220,
    )


def divider_demo() -> DemoResult:
    d_code = """from trunco.daisy import Divider, Button

# horizontal=False → vertical rule between items in a flex row
Divider(text="OR", horizontal=False)
Button(label="Sign up", color="primary")"""
    z_code = """from trunco.zbuild import Divider, Button

# horizontal=False → vertical rule between items in a flex row
Divider(text="OR", horizontal=False)
Button(label="Sign up", color="primary")"""
    return DemoResult(
        daisy_code=d_code,
        daisy_preview=_daisy_divider_preview(),
        zbuild_code=z_code,
        zbuild_preview=_zbuild_divider_preview(),
        preview_height=100,
    )


# ── Shared forms ─────────────────────────────────────────────────────────────


def form_demo() -> DemoResult:
    d_code = """from trunco.daisy import Form, FormControl, Input, Button

form = Form(action="/save", gap="md")
form.add_child(FormControl(label="Name", field=Input(placeholder="Jane Doe")))
form.add_child(FormControl(label="Email", field=Input(placeholder="you@example.com")))
form.add_child(Button(label="Subscribe", color="primary"))"""
    z_code = """from trunco.zbuild import Form, FormControl, Input, Button

form = Form(action="/save", gap="xl")
form.add_child(FormControl(label="Name", field=Input(placeholder="Jane Doe")))
form.add_child(FormControl(label="Email", field=Input(placeholder="you@example.com")))
form.add_child(Button(label="Subscribe", color="primary"))"""
    d_form = daisy.Form(action="/save", gap="md")
    d_form.add_child(
        daisy.FormControl(
            label="Name",
            field=daisy.Input(placeholder="Jane Doe", color="bordered"),
        )
    )
    d_form.add_child(
        daisy.FormControl(
            label="Email",
            field=daisy.Input(placeholder="you@example.com", color="bordered"),
        )
    )
    d_form.add_child(daisy.Button(label="Subscribe", color="primary"))
    z_form = zbuild.Form(action="/save", gap="xl")
    z_form.add_child(zbuild.FormControl(label="Name", field=zbuild.Input(placeholder="Jane Doe")))
    z_form.add_child(
        zbuild.FormControl(label="Email", field=zbuild.Input(placeholder="you@example.com"))
    )
    z_form.add_child(zbuild.Button(label="Subscribe", color="primary"))
    return DemoResult(
        d_code,
        d_form.render(),
        z_code,
        z_form.render(),
        preview_height=280,
        preview_full_width=True,
    )


def formcontrol_demo() -> DemoResult:
    d_code = """from trunco.daisy import FormControl, Input

FormControl(
    label="Email",
    field=Input(placeholder="you@example.com"),
    help_text="We never share your email.",
    required=True,
)"""
    z_code = """from trunco.zbuild import FormControl, Input

FormControl(
    label="Email",
    field=Input(placeholder="you@example.com"),
    help_text="We never share your email.",
    required=True,
)"""
    d_field = daisy.FormControl(
        label="Email",
        field=daisy.Input(placeholder="you@example.com", color="bordered"),
        help_text="We never share your email.",
        required=True,
    )
    z_field = zbuild.FormControl(
        label="Email",
        field=zbuild.Input(placeholder="you@example.com"),
        help_text="We never share your email.",
        required=True,
    )
    return DemoResult(
        d_code,
        d_field.render(),
        z_code,
        z_field.render(),
        preview_height=160,
        preview_full_width=True,
    )


def textarea_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Textarea\n\nTextarea(placeholder="Message…", variant="bordered")',
        daisy_preview=daisy.Textarea(placeholder="Message…", variant="bordered").render(),
        zbuild_code='from trunco.zbuild import Textarea\n\nTextarea(placeholder="Message…")',
        zbuild_preview=zbuild.Textarea(placeholder="Message…").render(),
        preview_height=140,
    )


def select_demo() -> DemoResult:
    d_opts = [
        daisy.Option(value="a", display_text="Option A"),
        daisy.Option(value="b", display_text="Option B"),
    ]
    z_opts = [
        zbuild.Option(value="a", display_text="Option A"),
        zbuild.Option(value="b", display_text="Option B"),
    ]
    return DemoResult(
        daisy_code="from trunco.daisy import Select, Option\n\nSelect(options=[Option(value='a', display_text='A')])",
        daisy_preview=daisy.Select(options=d_opts, variant="bordered").render(),
        zbuild_code="from trunco.zbuild import Select, Option\n\nSelect(options=[Option(value='a', display_text='A')])",
        zbuild_preview=zbuild.Select(options=z_opts).render(),
        preview_height=100,
    )


def checkbox_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Checkbox\n\nCheckbox(label="Accept terms", checked=True)',
        daisy_preview=daisy.Checkbox(label="Accept terms", checked=True).render(),
        zbuild_code='from trunco.zbuild import Checkbox\n\nCheckbox(label="Accept terms", checked=True)',
        zbuild_preview=zbuild.Checkbox(label="Accept terms", checked=True).render(),
        preview_height=90,
    )


def radio_demo() -> DemoResult:
    d_code = """from trunco.daisy import RadioGroup, Radio

# direction: "vertical" (default) or "horizontal"
RadioGroup(
    name="plan",
    gap="md",
    direction="horizontal",
    options=[
        Radio(name="plan", value="free", label="Free", checked=True, gap="sm"),
        Radio(name="plan", value="pro", label="Pro", gap="sm"),
    ],
)"""
    z_code = """from trunco.zbuild import RadioGroup, Radio

RadioGroup(
    name="plan",
    gap="md",
    direction="horizontal",
    options=[
        Radio(name="plan", value="free", label="Free", checked=True, gap="sm"),
        Radio(name="plan", value="pro", label="Pro", gap="sm"),
    ],
)"""
    d_group = daisy.RadioGroup(
        name="plan",
        gap="md",
        direction="horizontal",
        options=[
            daisy.Radio(name="plan", value="free", label="Free", checked=True, gap="sm"),
            daisy.Radio(name="plan", value="pro", label="Pro", gap="sm"),
        ],
    )
    z_group = zbuild.RadioGroup(
        name="plan",
        gap="md",
        direction="horizontal",
        options=[
            zbuild.Radio(name="plan", value="free", label="Free", checked=True, gap="sm"),
            zbuild.Radio(name="plan", value="pro", label="Pro", gap="sm"),
        ],
    )
    return DemoResult(
        daisy_code=d_code,
        daisy_preview=d_group.render(),
        zbuild_code=z_code,
        zbuild_preview=z_group.render(),
        preview_height=100,
    )


def range_demo() -> DemoResult:
    return DemoResult(
        daisy_code="from trunco.daisy import Range\n\nRange(min_value=0, max_value=100, value=40)",
        daisy_preview=daisy.Range(min_value=0, max_value=100, value=40).render(),
        zbuild_code="from trunco.zbuild import Range\n\nRange(min_value=0, max_value=100, value=40)",
        zbuild_preview=zbuild.Range(min_value=0, max_value=100, value=40).render(),
        preview_height=90,
    )


def toggle_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Toggle\n\nToggle(label="Notifications", checked=False, variant="primary")',
        daisy_preview=daisy.Toggle(
            label="Notifications", checked=False, variant="primary"
        ).render(),
        zbuild_code='from trunco.zbuild import Toggle\n\nToggle(label="Notifications", checked=False, color="primary")',
        zbuild_preview=zbuild.Toggle(
            label="Notifications", checked=False, color="primary"
        ).render(),
        preview_height=90,
    )


def fieldset_demo() -> DemoResult:
    d_code = """from trunco.daisy import Fieldset, FormControl, Input

Fieldset(
    legend="Account",
    children=[
        FormControl(label="Username", field=Input(placeholder="jane")),
        FormControl(label="Email", field=Input(placeholder="you@example.com")),
    ],
)"""
    z_code = """from trunco.zbuild import Fieldset, FormControl, Input

Fieldset(
    legend="Account",
    children=[
        FormControl(label="Username", field=Input(placeholder="jane")),
        FormControl(label="Email", field=Input(placeholder="you@example.com")),
    ],
)"""
    d_children = [
        daisy.FormControl(
            label="Username",
            field=daisy.Input(placeholder="jane", color="bordered"),
        ),
        daisy.FormControl(
            label="Email",
            field=daisy.Input(placeholder="you@example.com", color="bordered"),
        ),
    ]
    z_children = [
        zbuild.FormControl(label="Username", field=zbuild.Input(placeholder="jane")),
        zbuild.FormControl(label="Email", field=zbuild.Input(placeholder="you@example.com")),
    ]
    return DemoResult(
        daisy_code=d_code,
        daisy_preview=daisy.Fieldset(legend="Account", children=d_children).render(),
        zbuild_code=z_code,
        zbuild_preview=zbuild.Fieldset(legend="Account", children=z_children).render(),
        preview_height=200,
        preview_full_width=True,
    )


def label_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Label\n\nLabel(text="Email address")',
        daisy_preview=daisy.Label(text="Email address").render(),
        zbuild_code='from trunco.zbuild import Label\n\nLabel(text="Email address")',
        zbuild_preview=zbuild.Label(text="Email address").render(),
        preview_height=90,
    )


# ── DaisyUI only ─────────────────────────────────────────────────────────────


def file_input_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import FileInput\n\nFileInput(variant="bordered")',
        daisy_preview=daisy.FileInput(variant="bordered").render(),
        preview_height=100,
    )


def breadcrumbs_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Breadcrumbs, Link\n\nBreadcrumbs(items=[Link(href="/", text="Home"), "Settings"])',
        daisy_preview=daisy.Breadcrumbs(
            items=[daisy.Link(href="/", text="Home"), "Settings"]
        ).render(),
        preview_height=90,
    )


def loading_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Loading\n\nLoading(style="spinner", size="md")',
        daisy_preview=daisy.Loading(style="spinner", size="md").render(),
        preview_height=100,
    )


def navbar_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Navbar, Link\n\nNavbar(start=["Trunco"], end=[Link(href="/", text="Home")])',
        daisy_preview=daisy.Navbar(
            start=["Trunco"], end=[daisy.Link(href="/", text="Home")]
        ).render(),
        preview_height=110,
    )


def tabs_demo() -> DemoResult:
    return DemoResult(
        daisy_code="from trunco.daisy import Tabs\n\nTabs(tabs=[('Tab 1', 't1', True), ('Tab 2', 't2', False)])",
        daisy_preview=daisy.Tabs(tabs=[("Tab 1", "t1", True), ("Tab 2", "t2", False)]).render(),
        preview_height=90,
    )


def menu_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Menu, Link\n\nMenu(items=[Link(href="/", text="Home"), "About"])',
        daisy_preview=daisy.Menu(items=[daisy.Link(href="/", text="Home"), "About"]).render(),
        preview_height=160,
    )


def list_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import List\n\nList(items=["Install trunco", "Pick a kit", "Ship it"])',
        daisy_preview=daisy.List(items=["Install trunco", "Pick a kit", "Ship it"]).render(),
        preview_height=180,
    )


def hero_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Hero, Button\n\nHero(title="Hello", subtitle="World", actions=[Button(label="Go")])',
        daisy_preview=daisy.Hero(
            title="Hello",
            subtitle="World",
            actions=[daisy.Button(label="Go", color="primary", size="sm")],
        ).render(),
        preview_height=220,
    )


def stat_demo() -> DemoResult:
    return DemoResult(
        daisy_code='from trunco.daisy import Stat\n\nStat(title="Downloads", value="31K", description="Jan 2026")',
        daisy_preview=daisy.Stat(title="Downloads", value="31K", description="Jan 2026").render(),
        preview_height=130,
    )


def pagination_demo() -> DemoResult:
    return DemoResult(
        daisy_code="from trunco.daisy import Pagination\n\nPagination(pages=[1, 2, 3, '…', 10], active=2)",
        daisy_preview=daisy.Pagination(pages=[1, 2, 3, "…", 10], active=2).render(),
        preview_height=100,
    )


def dropdown_demo() -> DemoResult:
    trigger = daisy.Button(label="Menu", color="primary", size="sm")
    return DemoResult(
        daisy_code="from trunco.daisy import Dropdown, Button, Link\n\nDropdown(trigger=Button(label='Menu'), items=[Link(href='#', text='Item')])",
        daisy_preview=daisy.Dropdown(
            trigger=trigger,
            items=[daisy.Link(href="#", text="Profile"), daisy.Link(href="#", text="Logout")],
        ).render(),
        preview_height=160,
    )


# ── 0build only ──────────────────────────────────────────────────────────────


def spinner_demo() -> DemoResult:
    return DemoResult(
        zbuild_code="from trunco.zbuild import Spinner\n\nSpinner()",
        zbuild_preview=zbuild.Spinner().render(),
        preview_height=100,
    )


def nav_demo() -> DemoResult:
    return DemoResult(
        zbuild_code='from trunco.zbuild import Nav, Link\n\nNav(items=[Link(href="/", text="Home"), "About"])',
        zbuild_preview=zbuild.Nav(items=[zbuild.Link(href="/", text="Home"), "About"]).render(),
        preview_height=110,
    )


def tab_demo() -> DemoResult:
    return DemoResult(
        zbuild_code="from trunco.zbuild import Tab\n\nTab(tabs=[('Tab 1', 't1', True), ('Tab 2', 't2', False)])",
        zbuild_preview=zbuild.Tab(tabs=[("Tab 1", "t1", True), ("Tab 2", "t2", False)]).render(),
        preview_height=90,
    )


def breadcrumb_demo() -> DemoResult:
    return DemoResult(
        zbuild_code='from trunco.zbuild import Breadcrumb, Link\n\nBreadcrumb(items=[Link(href="/", text="Home"), "Settings"])',
        zbuild_preview=zbuild.Breadcrumb(
            items=[zbuild.Link(href="/", text="Home"), "Settings"]
        ).render(),
        preview_height=90,
    )
