import unittest
from trunco.components.textarea import TextAreaComponent
from trunco.enums import Attribute


class TestTextAreaComponent(unittest.TestCase):
    def test_textarea_initialization(self):
        textarea = TextAreaComponent(rows=5, cols=40, placeholder="Enter your comments")
        self.assertEqual(textarea.tag, "textarea")
        self.assertEqual(textarea.attributes.get(Attribute.ROWS), "5")
        self.assertEqual(textarea.attributes.get(Attribute.COLS), "40")
        self.assertIn("Enter your comments", textarea.children)

    def test_textarea_render(self):
        textarea = TextAreaComponent(rows=5, cols=40, placeholder="Enter your comments")
        expected_html = (
            f'<textarea id="{textarea.id}" rows="5" cols="40">'
            f"Enter your comments</textarea>"
        )
        self.assertEqual(str(textarea), expected_html)

    def test_textarea_render_without_placeholder(self):
        textarea = TextAreaComponent(rows=3, cols=30)
        expected_html = f'<textarea id="{textarea.id}" rows="3" cols="30"></textarea>'
        self.assertEqual(str(textarea), expected_html)


if __name__ == "__main__":
    unittest.main()
