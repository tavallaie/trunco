import unittest
from trunco.components.table import (
    TableCellComponent,
    TableRowComponent,
    TableComponent,
)


class TestTableComponents(unittest.TestCase):
    def test_table_cell_initialization(self):
        cell = TableCellComponent(content="Cell Content")
        self.assertEqual(cell.tag, "td")
        self.assertIn("Cell Content", cell.children)

        header_cell = TableCellComponent(content="Header Content", header=True)
        self.assertEqual(header_cell.tag, "th")
        self.assertIn("Header Content", header_cell.children)

    def test_table_row_initialization(self):
        cell1 = TableCellComponent(content="Cell 1")
        cell2 = TableCellComponent(content="Cell 2")
        row = TableRowComponent(cells=[cell1, cell2])
        self.assertEqual(row.tag, "tr")
        self.assertEqual(len(row.children), 2)
        self.assertIsInstance(row.children[0], TableCellComponent)
        self.assertIsInstance(row.children[1], TableCellComponent)

    def test_table_initialization(self):
        cell1 = TableCellComponent(content="Cell 1")
        cell2 = TableCellComponent(content="Cell 2")
        row = TableRowComponent(cells=[cell1, cell2])
        table = TableComponent(headers=["Header 1", "Header 2"], rows=[row])
        self.assertEqual(table.tag, "table")
        self.assertEqual(len(table.children), 2)  # One header row and one data row

    def test_table_render(self):
        cell1 = TableCellComponent(content="John")
        cell2 = TableCellComponent(content="30")
        row = TableRowComponent(cells=[cell1, cell2])
        table = TableComponent(headers=["Name", "Age"], rows=[row])
        expected_html = (
            f'<table id="{table.id}">'
            f'<tr id="{table.children[0].id}"><th id="{table.children[0].children[0].id}">Name</th>'
            f'<th id="{table.children[0].children[1].id}">Age</th></tr>'
            f'<tr id="{table.children[1].id}"><td id="{table.children[1].children[0].id}">John</td>'
            f'<td id="{table.children[1].children[1].id}">30</td></tr>'
            f"</table>"
        )
        self.assertEqual(str(table), expected_html)


if __name__ == "__main__":
    unittest.main()
