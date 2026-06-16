from docs.src.components import CodePanel, DocArticle, Section, paragraph
from trunco.base import Component
from trunco.components.table import TableCellComponent, TableRowComponent
from trunco.daisy import Table


def build():
    core_rows = [
        TableRowComponent(
            cells=[
                TableCellComponent(content="ButtonComponent"),
                TableCellComponent(content="button"),
                TableCellComponent(content="trunco.components.button"),
            ]
        ),
        TableRowComponent(
            cells=[
                TableCellComponent(content="InputComponent"),
                TableCellComponent(content="input"),
                TableCellComponent(content="trunco.components.input"),
            ]
        ),
        TableRowComponent(
            cells=[
                TableCellComponent(content="FormComponent"),
                TableCellComponent(content="form"),
                TableCellComponent(content="trunco.components.form"),
            ]
        ),
        TableRowComponent(
            cells=[
                TableCellComponent(content="SelectComponent"),
                TableCellComponent(content="select"),
                TableCellComponent(content="trunco.components.select"),
            ]
        ),
    ]
    core_table = Table(headers=["Component", "Tag", "Module"], rows=core_rows, zebra=True)

    table_wrap = Component(tag="div")
    table_wrap.add_class("overflow-x-auto")
    table_wrap.add_class("rounded-lg")
    table_wrap.add_class("border")
    table_wrap.add_class("border-base-300")
    table_wrap.add_child(core_table)

    return DocArticle(
        "Core Components",
        table_wrap,
        Section(
            "Base component",
            CodePanel(
                """from trunco import Component

card = Component(tag="div")
card.add_class("card")
card.add_child("Hello")""",
            ),
            anchor="base-component",
        ),
        Section(
            "StyleSheet",
            paragraph(
                "Build a project style.css in Python with variables, rules, "
                "@media blocks, and helpers to write the file or embed it in a page."
            ),
            CodePanel(
                """from trunco.components import StyleSheet

sheet = StyleSheet()
sheet.variables(primary="#3b82f6", body_bg="#ffffff")
sheet.rule("body", font_family="Inter, sans-serif", margin=0)
sheet.rule(".card", border_radius=12, padding=16)
sheet.write("assets/style.css")

page.add_child(sheet.to_link("assets/style.css"))""",
            ),
            anchor="stylesheet",
        ),
        lead="Framework-agnostic HTML primitives — no UI kit required.",
        breadcrumb=[
            ("Documentation", "index.html"),
            ("Reference", None),
            ("Components", None),
        ],
        toc=[("base-component", "Base component"), ("stylesheet", "StyleSheet")],
    )
