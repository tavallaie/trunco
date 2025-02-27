import unittest
from trunco.components.radio import RadioComponent, RadioGroupComponent
from trunco.enums import Attribute


class TestRadioComponents(unittest.TestCase):
    def test_radio_initialization(self):
        radio = RadioComponent(name="option", value="1", label="Option 1", checked=True)
        self.assertEqual(radio.tag, "input")
        self.assertEqual(radio.attributes.get(Attribute.TYPE), "radio")
        self.assertEqual(radio.attributes.get(Attribute.NAME), "option")
        self.assertEqual(radio.attributes.get(Attribute.VALUE), "1")
        self.assertEqual(radio.attributes.get(Attribute.CHECKED), "checked")
        self.assertEqual(radio.label, "Option 1")

    def test_radio_render(self):
        radio = RadioComponent(name="option", value="1", label="Option 1", checked=True)
        expected_html = (
            f'<input id="{radio.id}" type="radio" name="option" value="1" checked="checked">'
            f"<label>Option 1</label>"
        )
        self.assertEqual(str(radio), expected_html)

    def test_radio_render_with_context(self):
        radio = RadioComponent(name="option", value="1", label="{label}")
        context = {"label": "Dynamic Option"}
        expected_html = (
            f'<input id="{radio.id}" type="radio" name="option" value="1">'
            f"<label>Dynamic Option</label>"
        )
        self.assertEqual(radio.render(context), expected_html)

    def test_radio_group_initialization(self):
        radio1 = RadioComponent(name="group1", value="1", label="Option 1")
        radio2 = RadioComponent(name="group1", value="2", label="Option 2")
        radio_group = RadioGroupComponent(name="group1", options=[radio1, radio2])
        self.assertEqual(radio_group.tag, "div")
        self.assertEqual(len(radio_group.children), 2)
        self.assertIsInstance(radio_group.children[0], RadioComponent)
        self.assertIsInstance(radio_group.children[1], RadioComponent)

    def test_radio_group_render(self):
        radio1 = RadioComponent(name="group1", value="1", label="Option 1")
        radio2 = RadioComponent(name="group1", value="2", label="Option 2")
        radio_group = RadioGroupComponent(name="group1", options=[radio1, radio2])
        expected_html = (
            f'<div id="{radio_group.id}">'
            f'<input id="{radio1.id}" type="radio" name="group1" value="1"><label>Option 1</label>'
            f'<input id="{radio2.id}" type="radio" name="group1" value="2"><label>Option 2</label>'
            f"</div>"
        )
        self.assertEqual(str(radio_group), expected_html)


if __name__ == "__main__":
    unittest.main()
