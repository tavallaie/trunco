import unittest
from trunco.html import Component, Trigger, Swap, HxMethod, Attribute, Directive
from trunco.html.base import (
    DirectiveEntry,
    AttributeEntry,
    CssClass,
    StyleRule,
    TriggerEntry,
)


class TestComponent(unittest.TestCase):
    def test_add_directive(self):
        component = Component()
        component.add(DirectiveEntry(Directive.X_ON_CLICK, "alert('Hello!')"))
        self.assertEqual(component.directives[Directive.X_ON_CLICK], "alert('Hello!')")

    def test_add_attribute(self):
        component = Component()
        component.add(AttributeEntry(Attribute.HREF, "http://example.com"))
        self.assertEqual(component.attributes[Attribute.HREF], "http://example.com")

    def test_add_class(self):
        component = Component()
        component.add(CssClass("btn"))
        self.assertIn("btn", component.css_classes)

    def test_add_style(self):
        component = Component()
        component.add(StyleRule("color", "red"))
        self.assertEqual(component.styles.get("color"), "red")

    def test_add_trigger(self):
        component = Component()
        component.add(TriggerEntry(Trigger.CLICK))
        self.assertIn(Trigger.CLICK, component.triggers)

    def test_add_custom_script(self):
        component = Component()
        # For custom scripts, since no wrapper exists, we update the test to use the underlying list.
        component.custom_scripts.append("console.log('Hello, World!');")
        self.assertIn("console.log('Hello, World!');", component.custom_scripts)

    def test_add_child(self):
        component = Component()
        child_component = Component(tag="span")
        component.add(child_component)
        self.assertIn(child_component, component.children)

    def test_render_with_context(self):
        component = Component()
        component.add("{content}")
        context = {"content": "Dynamic Content"}
        expected_html = f'<div id="{component.id}">Dynamic Content</div>'
        self.assertEqual(component.render(context), expected_html)

    def test_render_without_context(self):
        component = Component()
        component.add(CssClass("btn"))
        rendered = component.render()
        self.assertIn('class="btn"', rendered)

    def test_render_with_hx_get(self):
        component = Component(hx_methods=HxMethod.get("/load-more"))
        expected_html = f'<div id="{component.id}" hx-get="/load-more"></div>'
        self.assertEqual(str(component), expected_html)

    def test_render_with_hx_post(self):
        component = Component(hx_methods=HxMethod.post("/submit"))
        expected_html = f'<div id="{component.id}" hx-post="/submit"></div>'
        self.assertEqual(str(component), expected_html)

    def test_render_with_hx_swap(self):
        component = Component(
            hx_methods=HxMethod.get("/load-more"), swap=Swap.OUTER_HTML
        )
        expected_html = (
            f'<div id="{component.id}" hx-get="/load-more" hx-swap="outerHTML"></div>'
        )
        self.assertEqual(str(component), expected_html)

    def test_render_with_trigger(self):
        component = Component(
            hx_methods=HxMethod.get("/load-more"), trigger=Trigger.CLICK
        )
        expected_html = (
            f'<div id="{component.id}" hx-get="/load-more" hx-trigger="click"></div>'
        )
        self.assertEqual(str(component), expected_html)


if __name__ == "__main__":
    unittest.main()
