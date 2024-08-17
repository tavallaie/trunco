import unittest
from trunco.daisy_ui.dropdown import (
    DaisyUIDropdown,
    DaisyUIDropdownAlignment,
    DaisyUIDropdownTrigger,
)
from trunco.components import LinkComponent


class TestDaisyUIDropdown(unittest.TestCase):
    def test_dropdown_default(self):
        dropdown = DaisyUIDropdown(
            summary_text="open or close", menu_items=["Item 1", "Item 2"]
        )
        expected_html = f'<details id="{dropdown.id}" class="dropdown dropdown-bottom"><summary class="btn m-1">open or close</summary><ul class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow"><li><a href="#">Item 1</a></li><li><a href="#">Item 2</a></li></ul></details>'
        self.assertEqual(str(dropdown), expected_html)

    def test_dropdown_with_alignment_and_trigger(self):
        dropdown = DaisyUIDropdown(
            summary_text="open or close",
            alignment=DaisyUIDropdownAlignment.LEFT,
            trigger=DaisyUIDropdownTrigger.HOVER,
            menu_items=["Item 1", "Item 2"],
        )
        expected_html = f'<details id="{dropdown.id}" class="dropdown dropdown-left dropdown-hover"><summary class="btn m-1">open or close</summary><ul class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow"><li><a href="#">Item 1</a></li><li><a href="#">Item 2</a></li></ul></details>'
        self.assertEqual(str(dropdown), expected_html)

    def test_dropdown_with_additional_classes(self):
        dropdown = DaisyUIDropdown(
            summary_text="open or close",
            menu_items=["Item 1", "Item 2"],
            additional_classes=["custom-class"],
        )
        expected_html = f'<details id="{dropdown.id}" class="dropdown dropdown-bottom custom-class"><summary class="btn m-1">open or close</summary><ul class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow"><li><a href="#">Item 1</a></li><li><a href="#">Item 2</a></li></ul></details>'
        self.assertEqual(str(dropdown), expected_html)

    def test_dropdown_with_component_menu_items(self):
        dropdown = DaisyUIDropdown(
            summary_text="open or close",
            menu_items=[
                LinkComponent(href="#", text="Link 1"),
                LinkComponent(href="#", text="Link 2"),
            ],
        )
        expected_html = f'<details id="{dropdown.id}" class="dropdown dropdown-bottom"><summary class="btn m-1">open or close</summary><ul class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow"><li><a href="#">Link 1</a></li><li><a href="#">Link 2</a></li></ul></details>'
        self.assertEqual(str(dropdown), expected_html)


if __name__ == "__main__":
    unittest.main()
