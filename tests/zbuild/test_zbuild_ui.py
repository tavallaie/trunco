import unittest

from trunco.zbuild import ZbuildButton
from trunco.zbuild.ui import (
    ZbuildAccordion,
    ZbuildAccordionGroup,
    ZbuildAlert,
    ZbuildAvatar,
    ZbuildBadge,
    ZbuildBreadcrumb,
    ZbuildDivider,
    ZbuildLink,
    ZbuildModal,
    ZbuildNav,
    ZbuildProgress,
    ZbuildSpinner,
    ZbuildTab,
    ZbuildTable,
    ZbuildTooltip,
)
from trunco.components.table import TableCellComponent, TableRowComponent


class TestZbuildUI(unittest.TestCase):
    def test_zbuild_link(self):
        link = ZbuildLink(href="/home", text="Home", style="muted")
        html = link.render()
        self.assertIn("z-link z-link-muted", html)

    def test_zbuild_badge(self):
        badge = ZbuildBadge(text="9", style="danger")
        html = badge.render()
        self.assertIn("z-badge z-badge-danger", html)

    def test_zbuild_alert(self):
        alert = ZbuildAlert(message="Error occurred", style="danger", closable=True)
        html = alert.render()
        self.assertIn("z-alert z-alert-danger", html)
        self.assertIn("data-z-alert", html)
        self.assertIn("z-alert-close", html)

    def test_zbuild_progress(self):
        progress = ZbuildProgress(value=75)
        html = progress.render()
        self.assertIn("z-progress", html)
        self.assertIn('value="75"', html)

    def test_zbuild_avatar(self):
        avatar = ZbuildAvatar(image_src="/a.png", alt="Avatar")
        html = avatar.render()
        self.assertIn("z-avatar", html)
        self.assertIn("z-avatar-image", html)

    def test_zbuild_breadcrumb(self):
        crumbs = ZbuildBreadcrumb(items=[ZbuildLink(href="/", text="Home"), "Page"])
        html = crumbs.render()
        self.assertIn("z-breadcrumb", html)
        self.assertIn("Home", html)

    def test_zbuild_table(self):
        rows = [
            TableRowComponent(cells=[TableCellComponent(content="Cell")]),
        ]
        table = ZbuildTable(headers=["Col"], rows=rows, striped=True, hover=True)
        html = table.render()
        self.assertIn("z-table z-table-striped z-table-hover", html)

    def test_zbuild_spinner(self):
        spinner = ZbuildSpinner()
        html = spinner.render()
        self.assertIn("data-z-spinner", html)

    def test_zbuild_tooltip(self):
        child = ZbuildButton(label="Tip")
        tooltip = ZbuildTooltip(tip="Info", child=child, position="right")
        html = tooltip.render()
        self.assertIn('data-z-tooltip="title: Info; pos: right"', html)
        self.assertIn("Tip", html)
        self.assertNotIn("z-tooltip-body", html)

    def test_zbuild_tooltip_default_position_uses_plain_title(self):
        child = ZbuildButton(label="Tip")
        html = ZbuildTooltip(tip="Hello", child=child).render()
        self.assertIn('data-z-tooltip="Hello"', html)

    def test_zbuild_modal(self):
        modal = ZbuildModal(
            modal_id="dlg",
            title="Edit",
            body="Content",
            footer=[ZbuildButton(label="Save", style="primary")],
        )
        html = modal.render()
        self.assertIn('id="dlg"', html)
        self.assertIn("z-modal", html)
        self.assertIn('data-z-modal="container: false"', html)
        self.assertIn("z-modal-footer", html)
        self.assertNotIn("z-modal-content", html)

    def test_zbuild_modal_trigger(self):
        html = ZbuildModal.trigger("dlg", "Open").render()
        self.assertIn('href="#dlg"', html)
        self.assertIn('data-z-toggle=""', html)

    def test_zbuild_nav(self):
        nav = ZbuildNav(items=["Home", ZbuildLink(href="/about", text="About")])
        html = nav.render()
        self.assertIn("z-nav", html)
        self.assertIn("About", html)

    def test_zbuild_tab(self):
        tabs = ZbuildTab(tabs=[("One", "one", True), ("Two", "two", False)])
        html = tabs.render()
        self.assertIn("z-tab", html)
        self.assertIn("z-active", html)

    def test_zbuild_accordion(self):
        accordion = ZbuildAccordion(title="FAQ", content="Answer", open=True)
        html = accordion.render()
        self.assertIn("<li", html)
        self.assertIn("z-open", html)
        self.assertIn("z-accordion-title", html)
        self.assertIn('href=""', html)
        self.assertNotIn("data-z-accordion", html)

    def test_zbuild_accordion_group(self):
        group = ZbuildAccordionGroup(
            ZbuildAccordion(title="One", content="A"),
            ZbuildAccordion(title="Two", content="B"),
        )
        html = group.render()
        self.assertIn("<ul", html)
        self.assertIn("data-z-accordion", html)
        self.assertEqual(html.count("z-accordion-title"), 2)
        self.assertEqual(html.count("<li"), 2)

    def test_zbuild_divider(self):
        divider = ZbuildDivider(text="Section")
        html = divider.render()
        self.assertIn("z-divider-small", html)
        self.assertIn("Section", html)

    def test_zbuild_divider_vertical(self):
        divider = ZbuildDivider(text="OR", horizontal=False)
        html = divider.render()
        self.assertIn("display-inline-flex", html)
        self.assertIn("flex-col", html)
        self.assertIn("z-divider-vertical", html)
        self.assertIn("--z-divider-vertical-height: 0.5rem", html)
        self.assertNotIn("align-self: stretch", html)
        self.assertIn("OR", html)

    def test_zbuild_modal_close_button(self):
        modal = ZbuildModal(modal_id="dlg", title="Edit", body="Content")
        html = modal.render()
        self.assertIn("z-modal-close", html)
        self.assertIn("z-margin-auto-vertical", html)
        self.assertIn("z-flex-top", html)


if __name__ == "__main__":
    unittest.main()
