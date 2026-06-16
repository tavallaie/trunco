import unittest

from trunco.components.script_block import ScriptBlock
from trunco.components.stylesheet import InlineStyle, Stylesheet


class TestHtmlAssets(unittest.TestCase):
    def test_stylesheet_void_element(self):
        link = Stylesheet("assets/app.css")
        html = link.render()
        self.assertIn('rel="stylesheet"', html)
        self.assertIn('href="assets/app.css"', html)
        self.assertNotIn("</link>", html)

    def test_inline_style(self):
        style = InlineStyle("body { margin: 0; }")
        html = style.render()
        self.assertIn("<style", html)
        self.assertIn("body { margin: 0; }", html)

    def test_script_block_inline(self):
        script = ScriptBlock(content="console.log('ok')")
        html = script.render()
        self.assertIn("<script", html)
        self.assertIn("console.log('ok')", html)

    def test_script_block_external(self):
        script = ScriptBlock(src="app.js", defer=True)
        html = script.render()
        self.assertIn('src="app.js"', html)
        self.assertIn("defer", html)


if __name__ == "__main__":
    unittest.main()
