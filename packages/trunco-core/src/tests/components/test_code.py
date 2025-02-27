import unittest
from trunco.components.code import CodeComponent


class TestCodeComponent(unittest.TestCase):
    def test_code_initialization(self):
        code_component = CodeComponent(code="print('Hello, world!')")
        self.assertEqual(code_component.tag, "code")
        self.assertIn("print('Hello, world!')", code_component.children)

    def test_code_render(self):
        code_component = CodeComponent(code="print('Hello, world!')")
        expected_html = (
            f"<code id=\"{code_component.id}\">print('Hello, world!')</code>"
        )
        self.assertEqual(code_component.render(), expected_html)

    def test_code_render_with_context(self):
        code_component = CodeComponent(code="{code}")
        context = {"code": "print('Dynamic code')"}
        expected_html = f"<code id=\"{code_component.id}\">print('Dynamic code')</code>"
        self.assertEqual(code_component.render(context), expected_html)


if __name__ == "__main__":
    unittest.main()
