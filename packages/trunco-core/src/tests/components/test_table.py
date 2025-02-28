import unittest
from trunco import html


class TestTableComponents(unittest.TestCase):
    def test_table_cell_initialization(self):
        cell = html.TableCell(content="Cell Content")
        self.assertEqual(cell.tag, "td")
        self.assertIn("Cell Content", cell.children)

        header_cell = html.TableCell(content="Header Content", header=True)
        self.assertEqual(header_cell.tag, "th")
        self.assertIn("Header Content", header_cell.children)

    def test_table_row_initialization(self):
        cell1 = html.TableCell(content="Cell 1")
        cell2 = html.TableCell(content="Cell 2")
        row = html.TableRow(cells=[cell1, cell2])
        self.assertEqual(row.tag, "tr")
        self.assertEqual(len(row.children), 2)
        self.assertIsInstance(row.children[0], html.TableCell)
        self.assertIsInstance(row.children[1], html.TableCell)

    def test_table_initialization(self):
        cell1 = html.TableCell(content="Cell 1")
        cell2 = html.TableCell(content="Cell 2")
        row = html.TableRow(cells=[cell1, cell2])
        table = html.Table(headers=["Header 1", "Header 2"], rows=[row])
        # Table should have a header row and the data row
        self.assertEqual(table.tag, "table")
        self.assertEqual(len(table.children), 2)

    def test_table_render(self):
        cell1 = html.TableCell(content="John")
        cell2 = html.TableCell(content="30")
        row = html.TableRow(cells=[cell1, cell2])
        table = html.Table(headers=["Name", "Age"], rows=[row])
        expected_html = (
            f'<table id="{table.id}">'
            f'<tr id="{table.children[0].id}">'
            f'<th id="{table.children[0].children[0].id}">Name</th>'
            f'<th id="{table.children[0].children[1].id}">Age</th>'
            f"</tr>"
            f'<tr id="{table.children[1].id}">'
            f'<td id="{table.children[1].children[0].id}">John</td>'
            f'<td id="{table.children[1].children[1].id}">30</td>'
            f"</tr>"
            f"</table>"
        )
        self.assertEqual(str(table), expected_html)


if __name__ == "__main__":
    unittest.main()
