import unittest

from trunco.daisy import DaisyButton
from trunco.daisy.ui import (
    DaisyAccordion,
    DaisyAlert,
    DaisyAvatar,
    DaisyBadge,
    DaisyBreadcrumbs,
    DaisyDivider,
    DaisyDropdown,
    DaisyHero,
    DaisyLink,
    DaisyList,
    DaisyLoading,
    DaisyMenu,
    DaisyModal,
    DaisyNavbar,
    DaisyPagination,
    DaisyProgress,
    DaisyStat,
    DaisyTable,
    DaisyTabs,
    DaisyTooltip,
)
from trunco.components.table import TableCellComponent, TableRowComponent


class TestDaisyUI(unittest.TestCase):
    def test_daisy_link(self):
        link = DaisyLink(href="/docs", text="Docs", variant="secondary")
        html = link.render()
        self.assertIn('class="link link-secondary"', html)
        self.assertIn('href="/docs"', html)

    def test_daisy_divider(self):
        divider = DaisyDivider(text="OR")
        html = divider.render()
        self.assertIn("divider", html)
        self.assertIn("OR", html)

    def test_daisy_badge(self):
        badge = DaisyBadge(text="New", variant="error", outline=True, size="sm")
        html = badge.render()
        self.assertIn("badge badge-error badge-outline badge-sm", html)

    def test_daisy_alert(self):
        alert = DaisyAlert(message="Saved", variant="success", title="Done")
        html = alert.render()
        self.assertIn("alert alert-success", html)
        self.assertIn("Done", html)
        self.assertIn("Saved", html)

    def test_daisy_progress(self):
        progress = DaisyProgress(value=40, variant="primary")
        html = progress.render()
        self.assertIn("progress progress-primary", html)
        self.assertIn('value="40"', html)

    def test_daisy_avatar(self):
        avatar = DaisyAvatar(image_src="/img.png", alt="User", online=True)
        html = avatar.render()
        self.assertIn("avatar online", html)
        self.assertIn('src="/img.png"', html)

    def test_daisy_breadcrumbs(self):
        crumbs = DaisyBreadcrumbs(items=[DaisyLink(href="/", text="Home"), "Settings"])
        html = crumbs.render()
        self.assertIn("breadcrumbs", html)
        self.assertIn("Home", html)
        self.assertIn("Settings", html)

    def test_daisy_table(self):
        rows = [
            TableRowComponent(
                cells=[
                    TableCellComponent(content="A"),
                    TableCellComponent(content="B"),
                ]
            )
        ]
        table = DaisyTable(headers=["H1", "H2"], rows=rows, zebra=True, size="sm")
        html = table.render()
        self.assertIn("table table-zebra table-sm", html)
        self.assertIn("<th", html)

    def test_daisy_loading(self):
        loading = DaisyLoading(style="dots", size="lg")
        html = loading.render()
        self.assertIn("loading loading-dots loading-lg", html)

    def test_daisy_tooltip(self):
        child = DaisyButton(label="Hover")
        tooltip = DaisyTooltip(tip="Hello", child=child, position="bottom")
        html = tooltip.render()
        self.assertIn("tooltip tooltip-bottom", html)
        self.assertIn('data-tip="Hello"', html)

    def test_daisy_modal(self):
        modal = DaisyModal(
            modal_id="m1",
            title="Confirm",
            body="Are you sure?",
            actions=[DaisyButton(label="OK")],
        )
        html = modal.render()
        self.assertIn('id="m1"', html)
        self.assertIn("modal-box", html)
        self.assertIn("modal-action", html)

    def test_daisy_navbar(self):
        navbar = DaisyNavbar(start=["Brand"], end=[DaisyButton(label="Login")])
        html = navbar.render()
        self.assertIn("navbar", html)
        self.assertIn("navbar-start", html)
        self.assertIn("navbar-end", html)

    def test_daisy_tabs(self):
        tabs = DaisyTabs(
            tabs=[("Tab 1", "t1", True), ("Tab 2", "t2", False)],
            style="boxed",
        )
        html = tabs.render()
        self.assertIn("tabs tabs-boxed", html)
        self.assertIn("tab-active", html)

    def test_daisy_menu(self):
        menu = DaisyMenu(items=[DaisyLink(href="/", text="Home"), "About"])
        html = menu.render()
        self.assertIn("menu", html)
        self.assertIn("Home", html)

    def test_daisy_list(self):
        list_component = DaisyList(items=["One", "Two"])
        html = list_component.render()
        self.assertIn("list-row", html)
        self.assertIn("One", html)

    def test_daisy_hero(self):
        hero = DaisyHero(
            title="Welcome",
            subtitle="Build faster",
            actions=[DaisyButton(label="Start")],
        )
        html = hero.render()
        self.assertIn("hero", html)
        self.assertIn("Welcome", html)

    def test_daisy_stat(self):
        stat = DaisyStat(title="Downloads", value="31K", description="Jan 1st - Feb 1st")
        html = stat.render()
        self.assertIn("stat-title", html)
        self.assertIn("stat-value", html)
        self.assertIn("31K", html)

    def test_daisy_pagination(self):
        pagination = DaisyPagination(pages=[1, 2, 3], active=2)
        html = pagination.render()
        self.assertIn("join", html)
        self.assertIn("btn-active", html)

    def test_daisy_accordion(self):
        accordion = DaisyAccordion(
            title="Section",
            content="Details",
            open=True,
            radio_name="acc",
        )
        html = accordion.render()
        self.assertIn("collapse", html)
        self.assertIn("collapse-title", html)

    def test_daisy_dropdown(self):
        trigger = DaisyButton(label="Menu")
        dropdown = DaisyDropdown(
            trigger=trigger,
            items=[DaisyLink(href="/a", text="Item A")],
        )
        html = dropdown.render()
        self.assertIn("dropdown", html)
        self.assertIn("dropdown-content", html)


if __name__ == "__main__":
    unittest.main()
