import unittest

from trunco.enums import Directive, HxMethod, Swap, Trigger


class TestLegacyEnumImports(unittest.TestCase):
    def test_directive_from_enums(self):
        self.assertEqual(Directive.X_ON_CLICK.value, "x-on:click")

    def test_htmx_from_enums(self):
        self.assertEqual(Trigger.CLICK.value, "click")
        self.assertEqual(Swap.INNER_HTML.value, "innerHTML")
        self.assertEqual(HxMethod.get("/api")[0], "hx-get")


if __name__ == "__main__":
    unittest.main()