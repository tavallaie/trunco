"""Component catalog — availability and demo wiring for kit documentation."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal

from docs.src.demos import DemoResult

Availability = Literal["both", "daisy", "zbuild"]
Category = Literal["ui", "form", "layout"]


@dataclass(frozen=True)
class CatalogEntry:
    name: str
    description: str
    category: Category
    availability: Availability
    demo: Callable[[], DemoResult]
    anchor: str = ""

    @property
    def slug(self) -> str:
        return self.anchor or self.name.lower().replace(" ", "-")


def _entries() -> list[CatalogEntry]:
    from docs.src import demos as d

    return [
        # Shared UI
        CatalogEntry("Button", "Clickable action control.", "ui", "both", d.button_demo),
        CatalogEntry("Input", "Single-line text field.", "ui", "both", d.input_demo),
        CatalogEntry("Card", "Content container with title and body.", "ui", "both", d.card_demo),
        CatalogEntry("Badge", "Small status or metadata label.", "ui", "both", d.badge_demo),
        CatalogEntry("Alert", "Inline feedback message.", "ui", "both", d.alert_demo),
        CatalogEntry("Link", "Hyperlink styled for the kit.", "ui", "both", d.link_demo),
        CatalogEntry("Progress", "Progress bar indicator.", "ui", "both", d.progress_demo),
        CatalogEntry("Avatar", "User or entity image.", "ui", "both", d.avatar_demo),
        CatalogEntry("Table", "Tabular data display.", "ui", "both", d.table_demo),
        CatalogEntry("Tooltip", "Hover hint on a child element.", "ui", "both", d.tooltip_demo),
        CatalogEntry("Modal", "Dialog overlay with title and actions.", "ui", "both", d.modal_demo),
        CatalogEntry("Accordion", "Expandable content section.", "ui", "both", d.accordion_demo),
        CatalogEntry(
            "Divider", "Visual separator with optional label.", "ui", "both", d.divider_demo
        ),
        # Shared forms
        CatalogEntry("Form", "Form container with action and method.", "form", "both", d.form_demo),
        CatalogEntry(
            "FormControl",
            "One labeled field with optional help text.",
            "form",
            "both",
            d.formcontrol_demo,
            anchor="formcontrol",
        ),
        CatalogEntry("Textarea", "Multi-line text input.", "form", "both", d.textarea_demo),
        CatalogEntry("Select", "Dropdown selection.", "form", "both", d.select_demo),
        CatalogEntry(
            "Option", "Select option element.", "form", "both", d.select_demo, anchor="option"
        ),
        CatalogEntry("Checkbox", "Boolean checkbox input.", "form", "both", d.checkbox_demo),
        CatalogEntry("Radio", "Single radio input.", "form", "both", d.radio_demo, anchor="radio"),
        CatalogEntry("RadioGroup", "Grouped radio inputs.", "form", "both", d.radio_demo),
        CatalogEntry("Range", "Slider / range input.", "form", "both", d.range_demo),
        CatalogEntry("Toggle", "On/off toggle switch.", "form", "both", d.toggle_demo),
        CatalogEntry("Fieldset", "Grouped fields with legend.", "form", "both", d.fieldset_demo),
        CatalogEntry("Label", "Standalone form label.", "form", "both", d.label_demo),
        # DaisyUI only
        CatalogEntry("FileInput", "File upload input.", "form", "daisy", d.file_input_demo),
        CatalogEntry(
            "Breadcrumbs", "Hierarchical navigation trail.", "layout", "daisy", d.breadcrumbs_demo
        ),
        CatalogEntry("Loading", "Animated loading indicator.", "ui", "daisy", d.loading_demo),
        CatalogEntry("Navbar", "Top navigation bar.", "layout", "daisy", d.navbar_demo),
        CatalogEntry("Tabs", "Tab navigation links.", "layout", "daisy", d.tabs_demo),
        CatalogEntry("Menu", "Vertical navigation menu.", "layout", "daisy", d.menu_demo),
        CatalogEntry("List", "Styled list of items.", "ui", "daisy", d.list_demo),
        CatalogEntry("Hero", "Large hero banner section.", "layout", "daisy", d.hero_demo),
        CatalogEntry("Stat", "Statistic highlight block.", "ui", "daisy", d.stat_demo),
        CatalogEntry("Pagination", "Page number controls.", "ui", "daisy", d.pagination_demo),
        CatalogEntry(
            "Dropdown", "Dropdown menu triggered by a button.", "ui", "daisy", d.dropdown_demo
        ),
        # 0build only
        CatalogEntry("Spinner", "Loading spinner.", "ui", "zbuild", d.spinner_demo),
        CatalogEntry("Nav", "Horizontal navigation list.", "layout", "zbuild", d.nav_demo),
        CatalogEntry("Tab", "Tab navigation (0build).", "layout", "zbuild", d.tab_demo),
        CatalogEntry(
            "Breadcrumb", "Breadcrumb trail (singular API).", "layout", "zbuild", d.breadcrumb_demo
        ),
    ]


CATALOG: list[CatalogEntry] = _entries()


def shared_entries() -> list[CatalogEntry]:
    return [e for e in CATALOG if e.availability == "both"]


def daisy_only_entries() -> list[CatalogEntry]:
    return [e for e in CATALOG if e.availability == "daisy"]


def zbuild_only_entries() -> list[CatalogEntry]:
    return [e for e in CATALOG if e.availability == "zbuild"]
