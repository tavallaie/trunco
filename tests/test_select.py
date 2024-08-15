import unittest
from trunco.components.select import OptionComponent, SelectComponent
from trunco.enums import Attribute


class TestSelectComponents(unittest.TestCase):
    def test_option_initialization(self):
        option = OptionComponent(value="1", display_text="Option 1", selected=True)
        self.assertEqual(
            option.attributes.get(Attribute.VALUE), "1"
        )  # Update this line
        self.assertEqual(option.attributes.get(Attribute.SELECTED), "selected")
        self.assertIn("Option 1", option.children)

    def test_option_render(self):
        option = OptionComponent(value="1", display_text="Option 1", selected=True)
        expected_html = (
            f'<option id="{option.id}" value="1" selected="selected">Option 1</option>'
        )
        self.assertEqual(str(option), expected_html)

    def test_select_initialization(self):
        option1 = OptionComponent(value="1", display_text="Option 1")
        option2 = OptionComponent(value="2", display_text="Option 2", selected=True)
        select = SelectComponent(options=[option1, option2])
        self.assertEqual(select.tag, "select")
        self.assertEqual(len(select.children), 2)
        self.assertIsInstance(select.children[0], OptionComponent)
        self.assertIsInstance(select.children[1], OptionComponent)

    def test_select_render(self):
        option1 = OptionComponent(value="1", display_text="Option 1")
        option2 = OptionComponent(value="2", display_text="Option 2", selected=True)
        select = SelectComponent(options=[option1, option2])
        expected_html = (
            f'<select id="{select.id}">'
            f'<option id="{option1.id}" value="1">Option 1</option>'
            f'<option id="{option2.id}" value="2" selected="selected">Option 2</option>'
            f"</select>"
        )
        self.assertEqual(str(select), expected_html)


if __name__ == "__main__":
    unittest.main()
