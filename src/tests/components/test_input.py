import unittest
from trunco.components.input import InputComponent
from trunco.enums import Attribute


class TestInputComponent(unittest.TestCase):
    def test_input_initialization(self):
        input_component = InputComponent(
            input_type="text", placeholder="Enter text", value="Sample text"
        )
        self.assertEqual(input_component.tag, "input")
        self.assertEqual(input_component.attributes.get(Attribute.TYPE), "text")
        self.assertEqual(
            input_component.attributes.get(Attribute.PLACEHOLDER), "Enter text"
        )
        self.assertEqual(input_component.attributes.get(Attribute.VALUE), "Sample text")

    def test_input_render(self):
        input_component = InputComponent(
            input_type="email", placeholder="Enter email", value="user@example.com"
        )
        expected_html = f'<input id="{input_component.id}" type="email" placeholder="Enter email" value="user@example.com">'
        self.assertEqual(str(input_component), expected_html)

    def test_input_render_without_value(self):
        input_component = InputComponent(placeholder="Enter text")
        expected_html = (
            f'<input id="{input_component.id}" type="text" placeholder="Enter text">'
        )
        self.assertEqual(str(input_component), expected_html)


if __name__ == "__main__":
    unittest.main()
