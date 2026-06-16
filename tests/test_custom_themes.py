import unittest

import trunco.daisy as daisy
import trunco.zbuild as zbuild
from trunco.daisy.theme import _registry as daisy_registry
from trunco.kits.scheme import ColorScheme, PaletteScheme
from trunco.zbuild.theme import _registry as zbuild_registry


class TestDaisyCustomThemes(unittest.TestCase):
    def setUp(self):
        self._saved = dict(daisy_registry._schemes)
        self._theme_name = daisy.get_theme().name
        daisy_registry._schemes.clear()

    def tearDown(self):
        daisy_registry._schemes.clear()
        daisy_registry._schemes.update(self._saved)
        daisy.set_theme(self._theme_name)

    def test_register_theme_with_dict(self):
        scheme = daisy.register_theme(
            name="brand",
            colors={
                "primary": "#1EA1F1",
                "secondary": "teal",
                "base-100": "oklch(98% 0.02 240)",
            },
            color_scheme="light",
            radius_box="0.5rem",
        )
        self.assertEqual(scheme.name, "brand")
        self.assertTrue(daisy.is_custom_theme("brand"))
        self.assertIn("brand", daisy.custom_theme_names())

    def test_theme_css_output(self):
        daisy.register_theme(
            name="brand",
            colors={"primary": "#1EA1F1", "primary-content": "#ffffff"},
        )
        css = daisy.theme_css()
        self.assertIn('[data-theme="brand"]', css)
        self.assertIn("--color-primary: #1EA1F1;", css)
        self.assertIn("--color-primary-content: #ffffff;", css)
        self.assertIn("color-scheme: light;", css)

    def test_page_includes_custom_styles(self):
        daisy.register_theme(name="brand", colors={"primary": "blue"})
        page = daisy.Page(daisy.Button(label="Go"), theme_name="brand")
        html = page.render()
        self.assertIn("<style>", html)
        self.assertIn('data-theme="brand"', html)
        self.assertIn("--color-primary: blue;", html)

    def test_styles_component(self):
        daisy.register_theme(name="brand", colors={"accent": "purple"})
        self.assertIn("--color-accent: purple;", daisy.Styles().render())

    def test_color_scheme_class(self):
        scheme = ColorScheme(
            name="ocean",
            colors={"primary": "cyan", "base-100": "white"},
            color_scheme="dark",
        )
        daisy.register_theme(scheme)
        self.assertIn("color-scheme: dark;", daisy.theme_css())

    def test_available_themes_merges_builtin_and_custom(self):
        daisy.register_theme(name="brand", colors={"primary": "blue"})
        names = daisy.available_themes()
        self.assertIn("light", names)
        self.assertIn("brand", names)

    def test_set_active_on_register(self):
        daisy.register_theme(
            name="brand",
            colors={"primary": "blue"},
            set_active=True,
        )
        self.assertEqual(daisy.theme.name, "brand")


class TestZbuildCustomPalettes(unittest.TestCase):
    def setUp(self):
        self._saved = dict(zbuild_registry._palettes)
        self._theme = zbuild.get_theme().copy()
        zbuild_registry._palettes.clear()

    def tearDown(self):
        zbuild_registry._palettes.clear()
        zbuild_registry._palettes.update(self._saved)
        zbuild.set_theme(
            palette=self._theme.palette,
            layout=self._theme.layout,
            mode=self._theme.mode,
        )

    def test_register_palette(self):
        palette = zbuild.register_palette(
            name="brand",
            light={"primary": "oklch(55% 0.2 240)", "primary-f": "oklch(98% 0 0)"},
            dark={"primary": "oklch(40% 0.18 240)", "primary-f": "oklch(98% 0 0)"},
        )
        self.assertEqual(palette.name, "brand")
        self.assertTrue(zbuild.is_custom_palette("brand"))

    def test_palette_css_output(self):
        zbuild.register_palette(
            name="brand",
            light={"primary": "oklch(55% 0.2 240)"},
            dark={"primary": "oklch(40% 0.18 240)"},
        )
        css = zbuild.palette_css()
        self.assertIn(".z-theme-brand", css)
        self.assertIn(".dark.z-theme-brand", css)
        self.assertIn("--z-primary: oklch(55% 0.2 240);", css)

    def test_page_applies_custom_palette_class(self):
        zbuild.register_palette(name="brand", light={"primary": "red"})
        page = zbuild.Page(zbuild.Button(label="Go"), palette="brand")
        html = page.render()
        self.assertIn("z-theme-brand", html)
        self.assertIn('data-z-palette="brand"', html)
        self.assertIn("<style>", html)

    def test_palette_scheme_class(self):
        palette = PaletteScheme(
            name="cyan",
            light={"bg": "#fff", "primary": "cyan"},
            dark={"bg": "#111", "primary": "cyan"},
        )
        zbuild.register_palette(palette)
        css = zbuild.palette_css()
        self.assertIn("--z-bg: #fff;", css)
        self.assertIn("--z-bg: #111;", css)

    def test_available_palettes(self):
        zbuild.register_palette(name="brand", light={"primary": "red"})
        names = zbuild.available_palettes()
        self.assertIn("sapphire", names)
        self.assertIn("brand", names)


class TestCrossKitThemeWorkflow(unittest.TestCase):
    def setUp(self):
        self._daisy_saved = dict(daisy_registry._schemes)
        self._zbuild_saved = dict(zbuild_registry._palettes)
        self._daisy_theme = daisy.get_theme().name
        self._zbuild_theme = zbuild.get_theme().copy()
        daisy_registry._schemes.clear()
        zbuild_registry._palettes.clear()

    def tearDown(self):
        daisy_registry._schemes.clear()
        daisy_registry._schemes.update(self._daisy_saved)
        zbuild_registry._palettes.clear()
        zbuild_registry._palettes.update(self._zbuild_saved)
        daisy.set_theme(self._daisy_theme)
        zbuild.set_theme(
            palette=self._zbuild_theme.palette,
            layout=self._zbuild_theme.layout,
            mode=self._zbuild_theme.mode,
        )

    def test_same_component_api_with_custom_schemes(self):
        daisy.register_theme(
            name="brand",
            colors={"primary": "#1EA1F1", "secondary": "#0d9488"},
            set_active=True,
        )
        zbuild.register_palette(
            name="brand",
            light={"primary": "#1EA1F1", "primary-f": "#ffffff"},
            set_active=True,
        )

        daisy_html = daisy.Page(daisy.Button(label="Go", color="primary")).render()
        zbuild_html = zbuild.Page(zbuild.Button(label="Go", color="primary")).render()

        self.assertIn('data-theme="brand"', daisy_html)
        self.assertIn("z-theme-brand", zbuild_html)
        self.assertIn("btn-primary", daisy_html)
        self.assertIn("z-button-primary", zbuild_html)


if __name__ == "__main__":
    unittest.main()