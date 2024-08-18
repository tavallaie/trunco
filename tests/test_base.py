import unittest
from trunco import Component, Trigger, Swap, HxMethod, Attribute, Directive


class TestComponent(unittest.TestCase):
    def test_add_directive(self):
        component = Component()
        component.add_directive(Directive.X_ON_CLICK, "alert('Hello!')")
        self.assertEqual(component.directives[Directive.X_ON_CLICK], "alert('Hello!')")

    def test_add_attribute(self):
        component = Component()
        component.add_attribute(Attribute.HREF, "http://example.com")
        self.assertEqual(component.attributes[Attribute.HREF], "http://example.com")

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

    def test_render_with_swap(self):
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
