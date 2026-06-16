import unittest

import trunco.daisy as daisy
import trunco.zbuild as zbuild


class TestShortImports(unittest.TestCase):
    def test_daisy_short_names(self):
        from trunco.daisy import Alert, Form, FormControl, Input

        self.assertIs(daisy.Form, Form)
        self.assertIs(daisy.Input, Input)
        self.assertIs(daisy.Alert, Alert)
        self.assertIs(daisy.FormControl, FormControl)

    def test_zbuild_short_names(self):
        from trunco.zbuild import Alert, Form, FormControl, Input

        self.assertIs(zbuild.Form, Form)
        self.assertIs(zbuild.FormControl, FormControl)

    def test_prefixed_names_remain_available(self):
        from trunco.daisy import DaisyButton, DaisyForm
        from trunco.zbuild import ZbuildButton, ZbuildForm

        self.assertIs(daisy.Button, DaisyButton)
        self.assertIs(daisy.Form, DaisyForm)
        self.assertIs(zbuild.Button, ZbuildButton)
        self.assertIs(zbuild.Form, ZbuildForm)


class TestUnifiedColorAPI(unittest.TestCase):
    def test_daisy_color_overrides_variant(self):
        button = daisy.Button(label="Go", color="secondary", variant="primary")
        html = button.render()
        self.assertIn("btn-secondary", html)
        self.assertNotIn("btn-primary", html)

    def test_daisy_alert_color(self):
        alert = daisy.Alert(message="Done", color="success")
        self.assertIn("alert-success", alert.render())

    def test_zbuild_color_overrides_style(self):
        button = zbuild.Button(label="Go", color="primary", style="default")
        html = button.render()
        self.assertIn("z-button-primary", html)

    def test_zbuild_alert_color(self):
        alert = zbuild.Alert(message="Warn", color="warning")
        self.assertIn("z-alert-warning", alert.render())


class TestDaisyTheme(unittest.TestCase):
    def setUp(self):
        self._original = daisy.get_theme().name

    def tearDown(self):
        daisy.set_theme(self._original)

    def test_set_theme(self):
        daisy.set_theme("cupcake")
        self.assertEqual(daisy.theme.name, "cupcake")

    def test_page_applies_theme(self):
        daisy.set_theme("dark")
        page = daisy.Page(daisy.Button(label="Hi"), theme_name="dracula")
        html = page.render()
        self.assertIn('data-theme="dracula"', html)

    def test_theme_apply_on_component(self):
        wrapper = daisy.Page()
        daisy.Theme(name="forest").apply(wrapper)
        self.assertEqual(wrapper.attributes["data-theme"], "forest")


class TestZbuildTheme(unittest.TestCase):
    def setUp(self):
        self._original = zbuild.get_theme().copy()

    def tearDown(self):
        zbuild.theme.palette = self._original.palette
        zbuild.theme.layout = self._original.layout
        zbuild.theme.mode = self._original.mode

    def test_set_theme(self):
        zbuild.set_theme(palette="ruby", layout="z-layout-large", mode="dark")
        self.assertEqual(zbuild.theme.palette, "ruby")
        self.assertEqual(zbuild.theme.layout, "z-layout-large")
        self.assertEqual(zbuild.theme.mode, "dark")

    def test_page_applies_theme_classes(self):
        page = zbuild.Page(
            zbuild.Button(label="Hi"),
            palette="emerald",
            mode="dark",
            layout="z-layout-medium",
        )
        html = page.render()
        self.assertIn("z-layout-medium", html)
        self.assertIn("dark", html)
        self.assertIn('data-z-palette="emerald"', html)


class TestKitSwapPattern(unittest.TestCase):
    """Same component names, different kits — only import changes."""

    def _build_form(self, kit):
        form = kit.Form(action="/save")
        form.add_child(
            kit.FormControl(
                label="Email",
                field=kit.Input(placeholder="you@example.com"),
            )
        )
        form.add_child(kit.Alert(message="Ready", color="info"))
        return form.render()

    def test_daisy_kit_form(self):
        html = self._build_form(daisy)
        self.assertIn("form-control", html)
        self.assertIn("alert-info", html)

    def test_zbuild_kit_form(self):
        html = self._build_form(zbuild)
        self.assertIn("z-form-label", html)
        self.assertIn("z-alert-info", html)


if __name__ == "__main__":
    unittest.main()