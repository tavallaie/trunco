import unittest
from trunco.base import Component
from trunco.enums import Directive, Attribute, Trigger


class TestComponent(unittest.TestCase):
    def test_initialization(self):
        component = Component()
        self.assertEqual(component.tag, "div")
        self.assertIsInstance(component.id, str)
        self.assertEqual(component.css_classes, [])
        self.assertEqual(component.styles, {})
        self.assertEqual(component.children, [])
        self.assertEqual(component.directives, {})
        self.assertEqual(component.attributes, {})
        self.assertEqual(component.triggers, [])
        self.assertEqual(component.custom_scripts, [])

    def test_add_class(self):
        component = Component()
        component.add_class("btn")
        self.assertIn("btn", component.css_classes)

    def test_add_style(self):
        component = Component()
        component.add_style("color", "red")
        self.assertEqual(component.styles["color"], "red")

    def test_add_directive(self):
        component = Component()
        component.add_directive(Directive.X_ON_CLICK, "alert('clicked')")
        self.assertEqual(component.directives[Directive.X_ON_CLICK], "alert('clicked')")

    def test_add_attribute(self):
        component = Component()
        component.add_attribute(Attribute.HREF, "http://example.com")
        self.assertEqual(component.attributes[Attribute.HREF], "http://example.com")

    def test_add_trigger(self):
        component = Component()
        component.add_trigger(Trigger.CLICK)
        self.assertIn(Trigger.CLICK, component.triggers)

    def test_add_child(self):
        component = Component()
        child_component = Component(tag="span")
        component.add_child(child_component)
        self.assertIn(child_component, component.children)

    def test_render_without_context(self):
        component = Component()
        component.add_class("btn")
        component.add_child("Click Me")
        expected_html = f'<div id="{component.id}" class="btn">Click Me</div>'
        self.assertEqual(component.render(), expected_html)

    def test_render_with_context(self):
        component = Component()
        component.add_child("{content}")
        context = {"content": "Hello, World!"}
        expected_html = f'<div id="{component.id}">Hello, World!</div>'
        self.assertEqual(component.render(context), expected_html)

    def test_render_custom_scripts(self):
        component = Component()
        component.add_custom_script("console.log('Hello, World!');")
        expected_html = f"<div id=\"{component.id}\"></div><script>console.log('Hello, World!');</script>"
        self.assertEqual(component.render(), expected_html)


if __name__ == "__main__":
    unittest.main()
