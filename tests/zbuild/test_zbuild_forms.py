import unittest

from trunco.enums import Method
from trunco.zbuild.forms import (
    ZbuildCheckbox,
    ZbuildFieldset,
    ZbuildForm,
    ZbuildFormField,
    ZbuildLabel,
    ZbuildOption,
    ZbuildRadio,
    ZbuildRadioGroup,
    ZbuildRange,
    ZbuildSelect,
    ZbuildTextarea,
    ZbuildToggleSwitch,
)


class TestZbuildForms(unittest.TestCase):
    def test_zbuild_form(self):
        form = ZbuildForm(action="/api", method=Method.POST)
        html = form.render()
        self.assertIn("z-form-stacked", html)
        self.assertIn('action="/api"', html)

    def test_zbuild_form_field(self):
        from trunco.zbuild import ZbuildInput

        field = ZbuildFormField(
            label="Name",
            field=ZbuildInput(placeholder="Jane"),
            help_text="Your full name",
            required=True,
        )
        html = field.render()
        self.assertIn("z-form-label", html)
        self.assertIn("margin-bottom", html)
        self.assertIn("z-form-label-required", html)
        self.assertIn("z-form-controls", html)
        self.assertIn("z-form-help", html)

    def test_zbuild_textarea(self):
        textarea = ZbuildTextarea(placeholder="Bio", size="large", danger=True)
        html = textarea.render()
        self.assertIn("z-textarea z-form-large z-form-danger", html)

    def test_zbuild_select(self):
        options = [ZbuildOption(value="1", display_text="One")]
        select = ZbuildSelect(options=options, size="small")
        html = select.render()
        self.assertIn("z-select z-form-small", html)
        self.assertIn("One", html)

    def test_zbuild_checkbox(self):
        checkbox = ZbuildCheckbox(label="Agree", checked=True)
        html = checkbox.render()
        self.assertIn("z-checkbox", html)
        self.assertIn("Agree", html)

    def test_zbuild_radio_and_group(self):
        radio = ZbuildRadio(name="size", value="m", label="Medium")
        html = radio.render()
        self.assertIn("z-radio", html)
        self.assertIn("display-inline-flex", html)
        self.assertNotIn("gap-2", html)
        group = ZbuildRadioGroup(name="size", options=[radio])
        self.assertIn("z-radio", group.render())

    def test_zbuild_radio_group_horizontal_uses_kit_flex_and_inline_gap(self):
        radios = [
            ZbuildRadio(name="plan", value="free", label="Free"),
            ZbuildRadio(name="plan", value="pro", label="Pro"),
        ]
        group = ZbuildRadioGroup(
            name="plan",
            options=radios,
            gap="md",
            direction="horizontal",
        )
        html = group.render()
        self.assertIn("display-flex", html)
        self.assertIn("flex-row", html)
        self.assertIn("flex-wrap", html)
        self.assertIn("justify-center", html)
        self.assertIn("gap: 0.75rem", html)
        self.assertIn("display-inline-flex", html)
        self.assertNotIn("gap-3", html)
        self.assertNotIn("flex-col", html)

    def test_zbuild_form_applies_field_margin_not_tailwind_space(self):
        from trunco.zbuild import ZbuildInput

        form = ZbuildForm(action="/api", gap="md")
        form.add_child(ZbuildFormField(label="Name", field=ZbuildInput()))
        html = form.render()
        self.assertIn("margin-bottom: 0.75rem", html)
        self.assertNotIn("space-y-3", html)
        self.assertNotIn("flex-col", html)

    def test_zbuild_label(self):
        label = ZbuildLabel(text="Email", for_input_id="email", required=True)
        html = label.render()
        self.assertIn("z-form-label z-form-label-required", html)
        self.assertIn('for="email"', html)

    def test_zbuild_range(self):
        slider = ZbuildRange(value=25, size="medium")
        html = slider.render()
        self.assertIn("z-range z-form-medium", html)
        self.assertIn('value="25"', html)

    def test_zbuild_toggle_switch(self):
        toggle = ZbuildToggleSwitch(label="Enable", checked=True, danger=True)
        html = toggle.render()
        self.assertIn("z-toggle-switch z-toggle-switch-danger", html)
        self.assertIn("Enable", html)

    def test_zbuild_toggle_switch_primary_default(self):
        html = ZbuildToggleSwitch(label="Alerts").render()
        self.assertIn("z-toggle-switch-primary", html)

    def test_zbuild_fieldset(self):
        fieldset = ZbuildFieldset(legend="Profile", children=["x"])
        html = fieldset.render()
        self.assertIn("z-fieldset", html)
        self.assertIn("z-legend", html)
        self.assertIn("Profile", html)


if __name__ == "__main__":
    unittest.main()
