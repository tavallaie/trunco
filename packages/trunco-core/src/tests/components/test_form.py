import unittest
from trunco.components.form import FormComponent
from trunco.enums import Attribute, Method


class TestFormComponent(unittest.TestCase):
    def test_form_initialization(self):
        form = FormComponent(action="/submit", method=Method.POST)
        self.assertEqual(form.tag, "form")
        self.assertEqual(form.attributes[Attribute.ACTION], "/submit")
        self.assertEqual(form.attributes[Attribute.METHOD], "POST")

    def test_form_without_action(self):
        form = FormComponent(method=Method.GET)
        self.assertNotIn(Attribute.ACTION, form.attributes)
        self.assertEqual(form.attributes[Attribute.METHOD], "GET")

    def test_form_render(self):
        form = FormComponent(action="/submit", method=Method.POST)
        expected_html = f'<form id="{form.id}" action="/submit" method="POST"></form>'
        self.assertEqual(form.render(), expected_html)


if __name__ == "__main__":
    unittest.main()
