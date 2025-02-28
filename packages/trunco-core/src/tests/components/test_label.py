import unittest
from trunco.html.enums import Attribute
from trunco import html


class TestLabelComponent(unittest.TestCase):
    def test_label_initialization(self):
        label = html.Label(text="Username", for_input_id="username-input")
        self.assertEqual(label.tag, "label")
        self.assertIn("Username", label.children)
        self.assertEqual(label.attributes.get(Attribute.FOR), "username-input")

    def test_label_render(self):
        label = html.Label(text="Password", for_input_id="password-input")
        expected_html = f'<label id="{label.id}" for="password-input">Password</label>'
        self.assertEqual(str(label), expected_html)

    def test_label_render_without_for(self):
        label = html.Label(text="Email")
        expected_html = f'<label id="{label.id}">Email</label>'
        self.assertEqual(str(label), expected_html)

    def test_label_render_with_context(self):
        label = html.Label(text="{text}")
        context = {"text": "First Name"}
        expected_html = f'<label id="{label.id}">First Name</label>'
        self.assertEqual(label.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
