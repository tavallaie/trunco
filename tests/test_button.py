import unittest
from trunco.components.button import ButtonComponent
from trunco.enums import Directive, Attribute


class TestButtonComponent(unittest.TestCase):
    def test_button_initialization(self):
        button = ButtonComponent(label="Click Me", on_click="alert('clicked')")
        self.assertEqual(button.tag, "button")
        self.assertIn("Click Me", button.children)
        self.assertEqual(button.attributes.get(Attribute.TYPE), "button")
        self.assertEqual(
            button.directives.get(Directive.X_ON_CLICK), "alert('clicked')"
        )

    def test_button_render(self):
        button = ButtonComponent(label="Click Me", on_click="alert('clicked')")
        expected_html = f'<button id="{button.id}" type="button" x-on:click="alert(\'clicked\')">Click Me</button>'
        self.assertEqual(button.render(), expected_html)

    def test_button_render_with_context(self):
        button = ButtonComponent(label="{label}")
        context = {"label": "Dynamic Button"}
        expected_html = (
            f'<button id="{button.id}" type="button">Dynamic Button</button>'
        )
        self.assertEqual(button.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
