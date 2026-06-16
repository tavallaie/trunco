import unittest
from pathlib import Path

from trunco.components import InlineStyle, StyleSheet, Stylesheet


class TestStyleSheet(unittest.TestCase):
    def test_variables_and_rules(self):
        sheet = StyleSheet()
        sheet.variables(primary="#3b82f6", body_bg="#fff")
        sheet.rule("body", font_family="Inter, sans-serif", margin=0)
        sheet.rule(".card", border_radius=12, padding=16)
        css = sheet.render()
        self.assertIn(":root {", css)
        self.assertIn("--primary: #3b82f6;", css)
        self.assertIn("font-family: Inter, sans-serif;", css)
        self.assertIn("border-radius: 12px;", css)

    def test_media_block(self):
        sheet = StyleSheet()
        sheet.variables(bg="#fff")
        with sheet.media("(prefers-color-scheme: dark)") as dark:
            dark.variables(bg="#111")
            dark.rule("body", color="#eee")
        css = sheet.render()
        self.assertIn("@media (prefers-color-scheme: dark) {", css)
        self.assertIn("--bg: #111;", css)

    def test_write_and_link_helpers(self):
        sheet = StyleSheet().rule("body", margin=0)
        path = Path(self._tmp) / "assets" / "style.css"
        written = sheet.write(path)
        self.assertTrue(written.exists())
        self.assertIn("body {", written.read_text(encoding="utf-8"))
        self.assertIn('href="assets/style.css"', sheet.to_link("assets/style.css").render())
        self.assertIn("<style", sheet.to_inline().render())

    def setUp(self):
        import tempfile

        self._tmp = tempfile.mkdtemp()


if __name__ == "__main__":
    unittest.main()