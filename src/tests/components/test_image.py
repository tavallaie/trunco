import unittest
from trunco.components.image import ImageComponent
from trunco.enums import Attribute


class TestImageComponent(unittest.TestCase):
    def test_image_initialization(self):
        image = ImageComponent(src="https://example.com/image.jpg", alt="Example Image")
        self.assertEqual(image.tag, "img")
        self.assertEqual(
            image.attributes.get(Attribute.SRC), "https://example.com/image.jpg"
        )
        self.assertEqual(image.attributes.get(Attribute.ALT), "Example Image")

    def test_image_render(self):
        image = ImageComponent(src="https://example.com/image.jpg", alt="Example Image")
        expected_html = f'<img id="{image.id}" src="https://example.com/image.jpg" alt="Example Image">'
        self.assertEqual(image.render(), expected_html)

    def test_image_render_without_alt(self):
        image = ImageComponent(src="https://example.com/image.jpg")
        expected_html = (
            f'<img id="{image.id}" src="https://example.com/image.jpg" alt="">'
        )
        self.assertEqual(image.render(), expected_html)


if __name__ == "__main__":
    unittest.main()
