import unittest
from pathlib import Path


class TestDocsBuild(unittest.TestCase):
    def test_build_generates_site(self):
        import docs.build as build_module

        build_module.main()
        site = Path(__file__).resolve().parent.parent / "docs" / "_site"
        self.assertTrue((site / "index.html").exists())
        self.assertTrue((site / "installation.html").exists())
        self.assertTrue((site / "kits.html").exists())
        self.assertTrue((site / "fragments" / "kits.html").exists())
        kits = (site / "kits.html").read_text(encoding="utf-8")
        self.assertIn("showcase-card", kits)
        self.assertIn("htmx.org", kits)
        self.assertIn("alpinejs", kits)
        self.assertTrue((site / ".nojekyll").exists())
        index = (site / "index.html").read_text(encoding="utf-8")
        self.assertIn("Trunco", index)
        self.assertIn("daisyui", index)
        self.assertIn("doc-navbar", index)
        self.assertIn("code-panel", index)
        self.assertIn("badge-kit-daisy", index)
        self.assertIn('rel="stylesheet"', index)
        self.assertIn("assets/style.css", index)


if __name__ == "__main__":
    unittest.main()
