import unittest
from trunco.components.paragraph import ParagraphComponent


class TestParagraphComponent(unittest.TestCase):
    def test_paragraph_initialization(self):
        paragraph = ParagraphComponent(text="This is a paragraph.")
        self.assertEqual(paragraph.tag, "p")
        self.assertIn("This is a paragraph.", paragraph.children)

    def test_paragraph_render(self):
        paragraph = ParagraphComponent(text="This is a paragraph.")
        expected_html = f'<p id="{paragraph.id}">This is a paragraph.</p>'
        self.assertEqual(str(paragraph), expected_html)

    def test_paragraph_render_with_context(self):
        paragraph = ParagraphComponent(text="{text}")
        context = {"text": "Dynamic paragraph content"}
        expected_html = f'<p id="{paragraph.id}">Dynamic paragraph content</p>'
        self.assertEqual(paragraph.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
