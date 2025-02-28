import unittest
from trunco import html


class TestTextAreaComponent(unittest.TestCase):
    def test_textarea_initialization(self):
        textarea = html.TextArea(rows=5, cols=40, placeholder="Enter your comments")
        self.assertEqual(textarea.tag, "textarea")
        self.assertEqual(textarea.attributes.get("rows"), "5")
        self.assertEqual(textarea.attributes.get("cols"), "40")
        self.assertIn("Enter your comments", textarea.children)

    def test_textarea_render(self):
        textarea = html.TextArea(rows=5, cols=40, placeholder="Enter your comments")
        expected_html = (
            f'<textarea id="{textarea.id}" rows="5" cols="40">'
            f"Enter your comments</textarea>"
        )
        self.assertEqual(str(textarea), expected_html)

    def test_textarea_render_without_placeholder(self):
        textarea = html.TextArea(rows=3, cols=30)
        expected_html = f'<textarea id="{textarea.id}" rows="3" cols="30"></textarea>'
        self.assertEqual(str(textarea), expected_html)


if __name__ == "__main__":
    unittest.main()
