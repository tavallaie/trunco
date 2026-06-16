from docs.src.components import CodePanel, DocArticle, PairGrid, PairHeader


def build():
    return DocArticle(
        "Custom Themes",
        PairGrid(
            PairHeader(
                "DaisyUI",
                "Register a custom DaisyUI theme with CSS variables.",
                anchor="daisyui",
            ),
            PairHeader(
                "0build",
                "Register a custom 0build color palette at runtime.",
                anchor="zbuild",
            ),
            CodePanel(
                """from trunco.daisy import register_theme

register_theme(name="brand",
    colors={"primary": "#1EA1F1"})""",
            ),
            CodePanel(
                """from trunco.zbuild import register_palette

register_palette(name="brand", ...)""",
            ),
        ),
        lead="Register DaisyUI CSS-variable themes or 0build palettes at runtime.",
        breadcrumb=[
            ("Documentation", "index.html"),
            ("Reference", None),
            ("Themes", None),
        ],
        toc=[("daisyui", "DaisyUI"), ("zbuild", "0build")],
    )
