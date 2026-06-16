import unittest

from trunco.daisy.forms import (
    DaisyCheckbox,
    DaisyFieldset,
    DaisyFileInput,
    DaisyForm,
    DaisyFormControl,
    DaisyLabel,
    DaisyOption,
    DaisyRadio,
    DaisyRadioGroup,
    DaisyRange,
    DaisySelect,
    DaisyTextarea,
    DaisyToggle,
)
from trunco.enums import Method


class TestDaisyForms(unittest.TestCase):
    def test_daisy_form(self):
        form = DaisyForm(action="/submit", method=Method.POST)
        html = form.render()
        self.assertIn("<form", html)
        self.assertIn('action="/submit"', html)
        self.assertIn('method="POST"', html)

    def test_daisy_form_control(self):
        from trunco.daisy import DaisyInput

        control = DaisyFormControl(
            label="Email",
            field=DaisyInput(placeholder="you@example.com"),
            help_text="Required",
            required=True,
        )
        html = control.render()
        self.assertIn("form-control", html)
        self.assertIn("label-text", html)
        self.assertIn("label-text-alt", html)
        self.assertIn("input-bordered", html)

    def test_daisy_textarea(self):
        textarea = DaisyTextarea(placeholder="Notes", variant="bordered", size="lg")
        html = textarea.render()
        self.assertIn("textarea textarea-bordered textarea-lg", html)
        self.assertIn("Notes", html)

    def test_daisy_select(self):
        options = [
            DaisyOption(value="a", display_text="Option A"),
            DaisyOption(value="b", display_text="Option B", selected=True),
        ]
        select = DaisySelect(options=options, variant="bordered", size="sm")
        html = select.render()
        self.assertIn("select select-bordered select-sm", html)
        self.assertIn('value="a"', html)
        self.assertIn('selected="selected"', html)

    def test_daisy_checkbox(self):
        checkbox = DaisyCheckbox(label="Accept", checked=True, variant="primary")
        html = checkbox.render()
        self.assertIn("checkbox checkbox-primary", html)
        self.assertIn('checked="checked"', html)
        self.assertIn("label-text", html)
        self.assertIn("Accept", html)

    def test_daisy_radio_and_group(self):
        radio = DaisyRadio(name="plan", value="pro", label="Pro", variant="accent")
        html = radio.render()
        self.assertIn("radio radio-accent", html)
        self.assertIn('name="plan"', html)

        group = DaisyRadioGroup(name="plan", options=[radio])
        group_html = group.render()
        self.assertIn("radio-accent", group_html)

    def test_daisy_label(self):
        label = DaisyLabel(text="Username", for_input_id="username")
        html = label.render()
        self.assertIn('class="label"', html)
        self.assertIn("label-text", html)
        self.assertIn('for="username"', html)

    def test_daisy_range(self):
        slider = DaisyRange(min_value=10, max_value=90, value=50, variant="success")
        html = slider.render()
        self.assertIn("range range-success", html)
        self.assertIn('min="10"', html)
        self.assertIn('value="50"', html)

    def test_daisy_toggle(self):
        toggle = DaisyToggle(checked=True, variant="warning", size="lg")
        html = toggle.render()
        self.assertIn("toggle toggle-warning toggle-lg", html)
        self.assertIn('checked="checked"', html)

    def test_daisy_toggle_with_label(self):
        html = DaisyToggle(label="Notifications", variant="primary").render()
        self.assertIn("label-text", html)
        self.assertIn("Notifications", html)
        self.assertIn("toggle-primary", html)

    def test_daisy_file_input(self):
        file_input = DaisyFileInput(variant="bordered", size="md")
        html = file_input.render()
        self.assertIn("file-input file-input-bordered file-input-md", html)
        self.assertIn('type="file"', html)

    def test_daisy_fieldset(self):
        fieldset = DaisyFieldset(legend="Account", children=["content"])
        html = fieldset.render()
        self.assertIn("fieldset", html)
        self.assertIn("fieldset-legend", html)
        self.assertIn("Account", html)


if __name__ == "__main__":
    unittest.main()
