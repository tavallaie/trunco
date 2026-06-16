import unittest

from trunco.spacing import gap_classes, stack_classes


class TestSpacing(unittest.TestCase):
    def test_gap_aliases(self):
        self.assertEqual(gap_classes("sm"), ["gap-2"])
        self.assertEqual(gap_classes("lg"), ["gap-4"])
        self.assertEqual(gap_classes("none"), [])

    def test_gap_numeric_and_raw(self):
        self.assertEqual(gap_classes(3), ["gap-3"])
        self.assertEqual(gap_classes("gap-5"), ["gap-5"])

    def test_stack_aliases(self):
        self.assertEqual(stack_classes("md"), ["space-y-3"])
        self.assertEqual(stack_classes("none"), [])


if __name__ == "__main__":
    unittest.main()