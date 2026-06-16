from trunco.base import Component
from trunco.daisy import Alert, Button

from docs.src.components import (
    CodePanel,
    DocLanding,
    FeatureGrid,
    HeroHome,
    HomeButtonDemo,
    Section,
    StatRow,
    htmx_link,
)


def build():
    actions = Component(tag="div")
    actions.add_class("flex")
    actions.add_class("gap-3")
    actions.add_class("flex-wrap")

    start = Button(label="Get started", color="primary", size="lg")
    start.add_attribute("href", "quickstart.html")
    start.add_attribute("hx-get", "fragments/quickstart.html")
    start.add_attribute("hx-target", "#main-content")
    start.add_attribute("hx-swap", "innerHTML show:window:top")
    start.add_attribute("hx-push-url", "quickstart.html")
    start.add_attribute("hx-indicator", "#htmx-progress")
    actions.add_child(start)

    browse = htmx_link("kits.html", "Browse components", extra_classes=["btn", "btn-outline", "btn-lg"])
    actions.add_child(browse)

    return DocLanding(
        HeroHome(
            'Build the web<br><span class="text-primary">in Python</span>',
            "Trunco is a component framework for Python backends. Swap UI kits with one import — ship HTML from composable objects.",
            "Python · DaisyUI · 0build",
            actions,
        ),
        StatRow(
            [
                ("UI Kits", "2", "DaisyUI + 0build"),
                ("Components", "40+", "Forms & UI"),
                ("Runtime deps", "0", "Core library"),
            ]
        ),
        FeatureGrid(
            [
                ("Kits", "Swap with one import", "Same names — Button, Form, Alert — across DaisyUI and 0build."),
                ("HTMX", "Hypermedia-ready", "First-class hx-* attributes on every component."),
                ("Themes", "Custom palettes", "Register DaisyUI themes or 0build palettes at runtime."),
            ]
        ),
        HomeButtonDemo(),
        Section(
            "Install",
            CodePanel(
                "uv pip install trunco",
                language="bash",
            ),
        ),
        Alert(message="This documentation site is built with Trunco.", color="success"),
    )