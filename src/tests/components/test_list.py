import unittest
from trunco.components.list import ListComponent, ListItemComponent


class TestListComponents(unittest.TestCase):
    def test_list_item_initialization(self):
        list_item = ListItemComponent(content="Item 1")
        self.assertEqual(list_item.tag, "li")
        self.assertIn("Item 1", list_item.children)

    def test_unordered_list_initialization(self):
        ul = ListComponent(
            ordered=False,
            items=[
                ListItemComponent(content="Item 1"),
                ListItemComponent(content="Item 2"),
            ],
        )
        self.assertEqual(ul.tag, "ul")
        self.assertEqual(len(ul.children), 2)
        self.assertIsInstance(ul.children[0], ListItemComponent)

    def test_ordered_list_initialization(self):
        ol = ListComponent(
            ordered=True,
            items=[
                ListItemComponent(content="Item 1"),
                ListItemComponent(content="Item 2"),
            ],
        )
        self.assertEqual(ol.tag, "ol")
        self.assertEqual(len(ol.children), 2)
        self.assertIsInstance(ol.children[0], ListItemComponent)

    def test_list_render(self):
        ul = ListComponent(
            ordered=False,
            items=[
                ListItemComponent(content="Item 1"),
                ListItemComponent(content="Item 2"),
            ],
        )
        rendered_html = str(ul)
        self.assertIn("<ul", rendered_html)
        self.assertIn("<li", rendered_html)
        self.assertIn("Item 1", rendered_html)
        self.assertIn("Item 2", rendered_html)

    def test_list_render_with_context(self):
        ul = ListComponent(ordered=False, items=[ListItemComponent(content="{item}")])
        context = {"item": "Dynamic Item"}
        rendered_html = ul.render(context)
        self.assertIn("<ul", rendered_html)
        self.assertIn("<li", rendered_html)
        self.assertIn("Dynamic Item", rendered_html)


if __name__ == "__main__":
    unittest.main()
