import unittest
import warnings

from trunco.daisy import Button as DaisyBtn, Card, Input
from trunco.zbuild import Button as ZBtn, Card as ZCard, Input as ZInput
from trunco.zbuild import kit_css_tag, zuikit_script_tag


class TestKitBasics(unittest.TestCase):
    def test_daisy_button(self):
        button = DaisyBtn(label="Save", color="primary", size="sm")
        html = button.render()
        self.assertIn('class="btn btn-primary btn-sm"', html)
        self.assertIn("Save", html)

    def test_daisy_input(self):
        input_component = Input(placeholder="Email", color="bordered")
        html = input_component.render()
        self.assertIn('class="input input-bordered"', html)

    def test_daisy_card(self):
        card = Card(title="Hello", body="World")
        html = card.render()
        self.assertIn("card-title", html)
        self.assertIn("Hello", html)

    def test_zbuild_button(self):
        button = ZBtn(label="Submit", color="primary", size="small")
        html = button.render()
        self.assertIn("z-button z-button-primary z-button-small", html)

    def test_zbuild_input(self):
        input_component = ZInput(placeholder="Name", size="large")
        html = input_component.render()
        self.assertIn('class="z-input z-form-large"', html)

    def test_zbuild_card(self):
        card = ZCard(title="Profile", body="Details", badge="Updated")
        html = card.render()
        self.assertIn("z-card-title", html)
        self.assertIn("z-text-meta", html)

    def test_zbuild_assets(self):
        self.assertIn("0build@0.4.5", kit_css_tag())
        self.assertIn("uikit.min.js", zuikit_script_tag())


class TestFrankenDeprecation(unittest.TestCase):
    def test_franken_reexports_zbuild(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            from trunco.franken import Button as FrankenButton

        self.assertTrue(any("deprecated" in str(w.message).lower() for w in caught))
        button = FrankenButton(label="Go", color="primary")
        html = button.render()
        self.assertIn("z-button z-button-primary", html)


if __name__ == "__main__":
    unittest.main()
