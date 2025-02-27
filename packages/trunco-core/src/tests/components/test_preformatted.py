import unittest
from trunco.components.preformattedText import PreformattedTextComponent


class TestPreformattedTextComponent(unittest.TestCase):
    def test_preformatted_text_initialization(self):
        preformatted_text = PreformattedTextComponent(text="This is preformatted text.")
        self.assertEqual(preformatted_text.tag, "pre")
        self.assertIn("This is preformatted text.", preformatted_text.children)

    def test_preformatted_text_render(self):
        preformatted_text = PreformattedTextComponent(text="This is preformatted text.")
        expected_html = (
            f'<pre id="{preformatted_text.id}">This is preformatted text.</pre>'
        )
        self.assertEqual(str(preformatted_text), expected_html)

    def test_preformatted_text_render_with_context(self):
        preformatted_text = PreformattedTextComponent(text="{text}")
        context = {"text": "Dynamic preformatted text"}
        expected_html = (
            f'<pre id="{preformatted_text.id}">Dynamic preformatted text</pre>'
        )
        self.assertEqual(preformatted_text.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
