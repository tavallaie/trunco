import unittest
from trunco.daisy_ui.button import (
    DaisyUIButton,
    DaisyUIButtonVariant,
    DaisyUIButtonSize,
    DaisyUIButtonModifier,
)


class TestDaisyUIButton(unittest.TestCase):
    def test_button_default(self):
        button = DaisyUIButton(label="Click Me")
        expected_html = f'<button id="{button.id}" class="btn btn-primary btn-md" type="button">Click Me</button>'
        self.assertEqual(str(button), expected_html)

    def test_button_with_variant_and_size(self):
        button = DaisyUIButton(
            label="Click Me",
            variant=DaisyUIButtonVariant.SUCCESS,
            size=DaisyUIButtonSize.LARGE,
        )
        expected_html = f'<button id="{button.id}" class="btn btn-success btn-lg" type="button">Click Me</button>'
        self.assertEqual(str(button), expected_html)

    def test_button_with_modifiers(self):
        button = DaisyUIButton(
            label="Click Me",
            variant=DaisyUIButtonVariant.WARNING,
            size=DaisyUIButtonSize.SMALL,
            modifiers=[DaisyUIButtonModifier.OUTLINE, DaisyUIButtonModifier.GLASS],
        )
        expected_html = f'<button id="{button.id}" class="btn btn-warning btn-sm btn-outline glass" type="button">Click Me</button>'
        self.assertEqual(str(button), expected_html)

    def test_button_with_additional_classes(self):
        button = DaisyUIButton(
            label="Click Me", additional_classes=["custom-class", "another-class"]
        )
        expected_html = f'<button id="{button.id}" class="btn btn-primary btn-md custom-class another-class" type="button">Click Me</button>'
        self.assertEqual(str(button), expected_html)


if __name__ == "__main__":
    unittest.main()
