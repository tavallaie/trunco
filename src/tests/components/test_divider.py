import unittest
from trunco.components.divider import DividerComponent


class TestDividerComponent(unittest.TestCase):
    def test_divider_initialization(self):
        divider = DividerComponent()
        self.assertEqual(divider.tag, "hr")

    def test_divider_render(self):
        divider = DividerComponent()
        expected_html = f'<hr id="{divider.id}">'
        self.assertEqual(divider.render(), expected_html)


if __name__ == "__main__":
    unittest.main()
