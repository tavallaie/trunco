from docs.src.components import CodePanel, DocArticle, NextSteps, Section


def build():
    return DocArticle(
        "Installation",
        Section(
            "Core",
            CodePanel("uv pip install trunco", language="bash"),
            anchor="core",
        ),
        Section(
            "With extras",
            CodePanel(
                'uv pip install "trunco[daisy]"\nuv pip install "trunco[zbuild,alpine,htmx]"',
                language="bash",
            ),
            anchor="with-extras",
        ),
        NextSteps(
            [
                ("Continue", "Quickstart →", "quickstart.html"),
                ("Browse", "Kit Reference →", "kits.html"),
            ]
        ),
        lead="Zero required runtime dependencies. Install only the extras you need.",
        breadcrumb=[
            ("Documentation", "index.html"),
            ("Guide", None),
            ("Installation", None),
        ],
        toc=[("core", "Core"), ("with-extras", "With extras")],
    )