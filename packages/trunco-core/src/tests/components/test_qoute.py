import unittest
from trunco.components.blockquote import BlockquoteComponent


class TestBlockquoteComponent(unittest.TestCase):
    def test_blockquote_initialization(self):
        blockquote = BlockquoteComponent(quote="This is a blockquote.")
        self.assertEqual(blockquote.tag, "blockquote")
        self.assertIn("This is a blockquote.", blockquote.children)

    def test_blockquote_render(self):
        blockquote = BlockquoteComponent(quote="This is a blockquote.")
        expected_html = (
            f'<blockquote id="{blockquote.id}">This is a blockquote.</blockquote>'
        )
        self.assertEqual(blockquote.render(), expected_html)

    def test_blockquote_render_with_context(self):
        blockquote = BlockquoteComponent(quote="{quote}")
        context = {"quote": "This is a dynamic blockquote."}
        expected_html = f'<blockquote id="{blockquote.id}">This is a dynamic blockquote.</blockquote>'
        self.assertEqual(blockquote.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
