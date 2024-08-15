import unittest
from trunco.components.slider import SliderComponent, SliderWithLabelComponent
from trunco.enums import Attribute


class TestSliderComponents(unittest.TestCase):
    def test_slider_initialization(self):
        slider = SliderComponent(min_value=0, max_value=100, step=5, value=50)
        self.assertEqual(slider.tag, "input")
        self.assertEqual(slider.attributes.get(Attribute.TYPE), "range")
        self.assertEqual(slider.attributes.get(Attribute.MIN), "0")
        self.assertEqual(slider.attributes.get(Attribute.MAX), "100")
        self.assertEqual(slider.attributes.get(Attribute.STEP), "5")
        self.assertEqual(slider.attributes.get(Attribute.VALUE), "50")

    def test_slider_render(self):
        slider = SliderComponent(min_value=0, max_value=100, step=5, value=50)
        expected_html = f'<input id="{slider.id}" type="range" min="0" max="100" step="5" value="50">'
        self.assertEqual(str(slider), expected_html)

    def test_slider_with_label_initialization(self):
        slider_with_label = SliderWithLabelComponent(
            label_text="Volume", min_value=0, max_value=100, step=5, value=50
        )
        self.assertEqual(slider_with_label.tag, "div")
        self.assertEqual(len(slider_with_label.children), 2)

    def test_slider_with_label_render(self):
        slider_with_label = SliderWithLabelComponent(
            label_text="Volume", min_value=0, max_value=100, step=5, value=50
        )
        expected_html = (
            f'<div id="{slider_with_label.id}">'
            f'<label id="{slider_with_label.children[0].id}">Volume</label>'
            f'<input id="{slider_with_label.children[1].id}" type="range" min="0" max="100" step="5" value="50">'
            f"</div>"
        )
        self.assertEqual(str(slider_with_label), expected_html)

    def test_slider_with_label_render_with_context(self):
        slider_with_label = SliderWithLabelComponent(
            label_text="{label_text}", min_value=0, max_value=100, step=5, value=50
        )
        context = {"label_text": "Adjust Volume"}
        expected_html = (
            f'<div id="{slider_with_label.id}">'
            f'<label id="{slider_with_label.children[0].id}">Adjust Volume</label>'
            f'<input id="{slider_with_label.children[1].id}" type="range" min="0" max="100" step="5" value="50">'
            f"</div>"
        )
        self.assertEqual(slider_with_label.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
