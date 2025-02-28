from trunco.html import Component
from typing import List


class TableCellComponent(Component):
    """
    A basic table cell component (can be used for both td and th).
    """

    def __init__(self, content: str = "", header: bool = False, **kwargs):
        tag = "th" if header else "td"
        super().__init__(tag=tag, **kwargs)
        self.add(content)


class TableRowComponent(Component):
    """
    A basic table row component.
    """

    def __init__(self, cells: List[TableCellComponent] = None, **kwargs):
        super().__init__(tag="tr", **kwargs)
        if cells:
            for cell in cells:
                self.add(cell)


class TableComponent(Component):
    """
    A basic table component with rows and cells.
    """

    def __init__(
        self, headers: List[str] = None, rows: List[TableRowComponent] = None, **kwargs
    ):
        super().__init__(tag="table", **kwargs)
        if headers:
            header_row = TableRowComponent(
                cells=[
                    TableCellComponent(content=header, header=True)
                    for header in headers
                ]
            )
            self.add(header_row)
        if rows:
            for row in rows:
                self.add(row)
