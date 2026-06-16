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
            "Development",
            CodePanel("uv sync\nuv pip install -e .", language="bash"),
            anchor="development",
        ),
        NextSteps(
            [
                ("Continue", "Quickstart →", "quickstart.html"),
                ("Browse", "Kit Reference →", "kits.html"),
            ]
        ),
        lead="Zero required runtime dependencies. UI kits and integrations ship in the core package.",
        breadcrumb=[
            ("Documentation", "index.html"),
            ("Guide", None),
            ("Installation", None),
        ],
        toc=[("core", "Core"), ("development", "Development")],
    )
