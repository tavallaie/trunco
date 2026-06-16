from docs.src.components import Callout, CodePanel, DocArticle, Section


def build():
    return DocArticle(
        "Quickstart",
        Section(
            "DaisyUI kit",
            CodePanel(
                """from trunco.daisy import Button, Page

btn = Button(label="Hello", color="primary")
page = Page(btn, theme_name="light")
print(page.render())""",
            ),
            anchor="daisyui-kit",
        ),
        Section(
            "Swap kits",
            Callout("Change trunco.daisy to trunco.zbuild — same component names."),
            anchor="swap-kits",
        ),
        lead="From zero to rendered HTML in under a minute.",
        breadcrumb=[
            ("Documentation", "index.html"),
            ("Guide", None),
            ("Quickstart", None),
        ],
        toc=[("daisyui-kit", "DaisyUI kit"), ("swap-kits", "Swap kits")],
    )