import unittest
import warnings

from trunco import Component, Directive, HxMethod, Swap, Trigger
from trunco.alpine import alpine_script_tag
from trunco.htmx import htmx_script_tag
from trunco.uikit import zuikit_script_tag


class TestBackwardCompatibleImports(unittest.TestCase):
    def test_directive_import(self):
        component = Component()
        component.add_directive(Directive.X_DATA, "{ open: false }")
        self.assertEqual(component.directives["x-data"], "{ open: false }")

    def test_htmx_import(self):
        component = Component(
            hx_methods=HxMethod.post("/submit"),
            swap=Swap.OUTER_HTML,
            trigger=Trigger.SUBMIT,
        )
        html = component.render()
        self.assertIn('hx-post="/submit"', html)
        self.assertIn('hx-swap="outerHTML"', html)
        self.assertIn('hx-trigger="submit"', html)


class TestOptionalAssets(unittest.TestCase):
    def test_alpine_script_tag(self):
        self.assertIn("alpinejs", alpine_script_tag())

    def test_htmx_script_tag(self):
        self.assertIn("htmx.org", htmx_script_tag())

    def test_zuikit_script_tag(self):
        self.assertIn("0build@0.4.5", zuikit_script_tag())
        self.assertIn("uikit.min.js", zuikit_script_tag())

    def test_legacy_uikit_assets_warn(self):
        from trunco.uikit import uikit_css_tag, uikit_js_tag

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            uikit_css_tag()
            uikit_js_tag()

        self.assertEqual(len(caught), 2)
        self.assertTrue(all(isinstance(w.message, DeprecationWarning) for w in caught))


if __name__ == "__main__":
    unittest.main()