import unittest
from trunco.daisy_ui.dropdown import (
    DaisyUIDropdown,
    DaisyUIDropdownAlignment,
    DaisyUIDropdownTrigger,
)
from trunco.components import LinkComponent, LabelComponent, InputComponent


class TestDaisyUIDropdown(unittest.TestCase):
    def test_dropdown_default(self):
        dropdown = DaisyUIDropdown(
            summary_text="Open or Close",
            menu_items=[
                LinkComponent(href="#", text="Item 1", id="item1-id"),
                LinkComponent(href="#", text="Item 2", id="item2-id"),
            ],
            id="dropdown-id",
        )
        expected_html = (
            '<details id="dropdown-id" class="dropdown dropdown-bottom">'
            '<summary id="dropdown-id-summary" class="btn m-1">Open or Close</summary>'
            '<ul id="dropdown-id-menu" class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow">'
            '<li id="dropdown-id-menu-item-0"><a id="item1-id" href="#">Item 1</a></li>'
            '<li id="dropdown-id-menu-item-1"><a id="item2-id" href="#">Item 2</a></li>'
            "</ul>"
            "</details>"
        )
        self.assertEqual(str(dropdown), expected_html)

    def test_dropdown_with_additional_classes(self):
        dropdown = DaisyUIDropdown(
            summary_text="Open or Close",
            menu_items=[
                LinkComponent(href="#", text="Item 1", id="item1-id"),
                LinkComponent(href="#", text="Item 2", id="item2-id"),
            ],
            id="dropdown-id",
            additional_classes=["custom-class"],
            menu_classes=["custom-menu-class"],
        )
        expected_html = (
            '<details id="dropdown-id" class="dropdown dropdown-bottom custom-class">'
            '<summary id="dropdown-id-summary" class="btn m-1">Open or Close</summary>'
            '<ul id="dropdown-id-menu" class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow custom-menu-class">'
            '<li id="dropdown-id-menu-item-0"><a id="item1-id" href="#">Item 1</a></li>'
            '<li id="dropdown-id-menu-item-1"><a id="item2-id" href="#">Item 2</a></li>'
            "</ul>"
            "</details>"
        )
        self.assertEqual(str(dropdown), expected_html)

    def test_dropdown_with_alignment_and_trigger(self):
        dropdown = DaisyUIDropdown(
            summary_text="Open or Close",
            menu_items=[
                LinkComponent(href="#", text="Item 1", id="item1-id"),
                LinkComponent(href="#", text="Item 2", id="item2-id"),
            ],
            id="dropdown-id",
            alignment=DaisyUIDropdownAlignment.LEFT,
            trigger=DaisyUIDropdownTrigger.HOVER,
        )
        expected_html = (
            '<details id="dropdown-id" class="dropdown dropdown-hover dropdown-left">'
            '<summary id="dropdown-id-summary" class="btn m-1">Open or Close</summary>'
            '<ul id="dropdown-id-menu" class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow">'
            '<li id="dropdown-id-menu-item-0"><a id="item1-id" href="#">Item 1</a></li>'
            '<li id="dropdown-id-menu-item-1"><a id="item2-id" href="#">Item 2</a></li>'
            "</ul>"
            "</details>"
        )
        self.assertEqual(str(dropdown), expected_html)

    def test_dropdown_with_component_menu_items(self):
        dropdown = DaisyUIDropdown(
            summary_text="Open or Close",
            menu_items=[
                LinkComponent(href="#", text="Link 1", id="link1-id"),
                LabelComponent(text="Label", id="label1-id"),
                InputComponent(
                    input_type="text", placeholder="Enter text", id="input1-id"
                ),
            ],
            id="dropdown-id",
        )
        expected_html = (
            '<details id="dropdown-id" class="dropdown dropdown-bottom">'
            '<summary id="dropdown-id-summary" class="btn m-1">Open or Close</summary>'
            '<ul id="dropdown-id-menu" class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow">'
            '<li id="dropdown-id-menu-item-0"><a id="link1-id" href="#">Link 1</a></li>'
            '<li id="dropdown-id-menu-item-1"><label id="label1-id">Label</label></li>'
            '<li id="dropdown-id-menu-item-2"><input id="input1-id" type="text" placeholder="Enter text"></li>'
            "</ul>"
            "</details>"
        )
        self.assertEqual(str(dropdown), expected_html)

    def test_nested_dropdown(self):
        nested_dropdown = DaisyUIDropdown(
            summary_text="Nested",
            menu_items=[
                LinkComponent(href="#", text="Nested Item 1", id="nested-item1-id"),
                "Nested Item 2",
            ],
            id="nested-dropdown-id",
        )
        dropdown = DaisyUIDropdown(
            summary_text="Open or Close",
            menu_items=[nested_dropdown, "Item 3"],
            id="dropdown-id",
        )
        expected_html = (
            '<details id="dropdown-id" class="dropdown dropdown-bottom">'
            '<summary id="dropdown-id-summary" class="btn m-1">Open or Close</summary>'
            '<ul id="dropdown-id-menu" class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow">'
            '<li id="dropdown-id-menu-item-0">'
            '<details id="nested-dropdown-id" class="dropdown dropdown-bottom">'
            '<summary id="nested-dropdown-id-summary" class="btn m-1">Nested</summary>'
            '<ul id="nested-dropdown-id-menu" class="menu dropdown-content bg-base-100 rounded-box z-[1] w-52 p-2 shadow">'
            '<li id="nested-dropdown-id-menu-item-0"><a id="nested-item1-id" href="#">Nested Item 1</a></li>'
            '<li id="nested-dropdown-id-menu-item-1"><a href="#">Nested Item 2</a></li>'
            "</ul>"
            "</details>"
            "</li>"
            '<li id="dropdown-id-menu-item-1"><a href="#">Item 3</a></li>'
            "</ul>"
            "</details>"
        )
        self.assertEqual(str(dropdown), expected_html)


if __name__ == "__main__":
    unittest.main()
