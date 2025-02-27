from trunco.base import Component
from typing import List


class TableCellComponent(Component):
    """
    A basic table cell component (can be used for both td and th).
    """

    def __init__(self, content: str = "", header: bool = False, **kwargs):
        tag = "th" if header else "td"
        super().__init__(tag=tag, **kwargs)
        self.children.append(content)


class TableRowComponent(Component):
    """
    A basic table row component.
    """

    def __init__(self, cells: List[TableCellComponent] = None, **kwargs):
        super().__init__(tag="tr", **kwargs)
        if cells:
            self.children.extend(cells)


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
            self.add_child(header_row)
        if rows:
            self.children.extend(rows)
