import unittest
from trunco.components.link import LinkComponent
from trunco.enums import Attribute


class TestLinkComponent(unittest.TestCase):
    def test_link_initialization(self):
        link = LinkComponent(
            href="https://example.com", text="Example", target="_blank"
        )
        self.assertEqual(link.tag, "a")
        self.assertEqual(link.attributes.get(Attribute.HREF), "https://example.com")
        self.assertEqual(link.attributes.get(Attribute.TARGET), "_blank")
        self.assertIn("Example", link.children)

    def test_link_render(self):
        link = LinkComponent(href="https://example.com", text="Example")
        expected_html = f'<a id="{link.id}" href="https://example.com">Example</a>'
        self.assertEqual(str(link), expected_html)

    def test_link_render_with_context(self):
        link = LinkComponent(href="https://example.com", text="{text}")
        context = {"text": "Visit our site"}
        expected_html = (
            f'<a id="{link.id}" href="https://example.com">Visit our site</a>'
        )
        self.assertEqual(link.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
