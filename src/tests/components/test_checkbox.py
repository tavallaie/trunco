import unittest
from trunco.components.checkbox import CheckboxComponent
from trunco.enums import Attribute


class TestCheckboxComponent(unittest.TestCase):
    def test_checkbox_initialization(self):
        checkbox = CheckboxComponent(label="Accept Terms", checked=True)
        self.assertEqual(checkbox.tag, "input")
        self.assertEqual(checkbox.attributes.get(Attribute.TYPE), "checkbox")
        self.assertEqual(checkbox.attributes.get(Attribute.CHECKED), "checked")
        self.assertEqual(checkbox.label, "Accept Terms")

    def test_checkbox_render(self):
        checkbox = CheckboxComponent(label="Accept Terms", checked=True)
        expected_html = (
            f'<input id="{checkbox.id}" type="checkbox" checked="checked">'
            f"<label>Accept Terms</label>"
        )
        self.assertEqual(checkbox.render(), expected_html)

    def test_checkbox_render_with_context(self):
        checkbox = CheckboxComponent(label="{label}")
        context = {"label": "Subscribe to newsletter"}
        expected_html = (
            f'<input id="{checkbox.id}" type="checkbox">'
            f"<label>Subscribe to newsletter</label>"
        )
        self.assertEqual(checkbox.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
