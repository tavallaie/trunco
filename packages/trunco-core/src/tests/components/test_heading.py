import unittest
from trunco.components.heading import HeadingComponent


class TestHeadingComponent(unittest.TestCase):
    def test_heading_initialization(self):
        heading = HeadingComponent(tag="h2", text="This is a heading")
        self.assertEqual(heading.tag, "h2")
        self.assertIn("This is a heading", heading.children)

    def test_invalid_heading_tag(self):
        with self.assertRaises(ValueError):
            HeadingComponent(tag="h7", text="Invalid heading")

    def test_heading_render(self):
        heading = HeadingComponent(tag="h3", text="This is a heading")
        expected_html = f'<h3 id="{heading.id}">This is a heading</h3>'
        self.assertEqual(heading.render(), expected_html)

    def test_heading_render_with_context(self):
        heading = HeadingComponent(tag="h1", text="{text}")
        context = {"text": "Dynamic Heading"}
        expected_html = f'<h1 id="{heading.id}">Dynamic Heading</h1>'
        self.assertEqual(heading.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
