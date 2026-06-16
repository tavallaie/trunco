from docs.src.components import Callout, CodePanel, DocArticle, NextSteps, Section, paragraph
from trunco.daisy import Badge


def build():
    return DocArticle(
        "Integrations",
        Section(
            "Install",
            paragraph(
                "HTMX and Alpine helpers ship with Trunco — zero runtime "
                "dependencies, only typed helpers and CDN script tags."
            ),
            CodePanel(
                "uv pip install trunco",
                language="bash",
            ),
            anchor="install",
        ),
        Section(
            "HTMX",
            paragraph(
                "HTMX extends HTML with attributes like hx-get and hx-post so "
                "the browser can fetch partial responses from your Python backend "
                "and swap them into the page — no client-side router required."
            ),
            paragraph(
                "Include the script once in your layout, then attach hx-* "
                "attributes to any Trunco component."
            ),
            CodePanel(
                """from trunco.htmx import htmx_script_tag

# In your page template:
print(htmx_script_tag())""",
            ),
            paragraph(
                "Use HxMethod, Swap, and Trigger enums on the Component "
                "constructor, or call add_attribute for any HTMX attribute "
                "(hx-target, hx-push-url, hx-indicator, and so on)."
            ),
            CodePanel(
                """from trunco import Component, HxMethod, Swap, Trigger

loader = Component(
    hx_methods=HxMethod.get("/api/items"),
    trigger=Trigger.CLICK,
    swap=Swap.INNER_HTML,
)
loader.add_child("Load more")

nav_link = Component(tag="a")
nav_link.add_attribute("href", "kits.html")
nav_link.add_attribute("hx-get", "fragments/kits.html")
nav_link.add_attribute("hx-target", "#main-content")
nav_link.add_attribute("hx-swap", "innerHTML show:window:top")
nav_link.add_attribute("hx-push-url", "kits.html")
nav_link.add_child("Kit Reference")""",
            ),
            paragraph(
                "This documentation site uses that pattern for sidebar navigation: "
                "each link fetches a pre-rendered HTML fragment and swaps it into "
                "#main-content while updating the browser URL."
            ),
            CodePanel(
                """from trunco import Component, HxMethod, Swap, Trigger
from trunco.daisy import Button, Page
from trunco.htmx import htmx_script_tag

def items_partial():
    return Button(label="Fresh from the server", color="primary").render()

page = Page(
    Component(
        hx_methods=HxMethod.get("/items"),
        trigger=Trigger.CLICK,
        swap=Swap.INNER_HTML,
        tag="button",
    ),
    theme_name="light",
)
# Flask/FastAPI route returns items_partial() for GET /items""",
            ),
            anchor="htmx",
            badge=Badge("HTMX", color="primary", size="sm"),
        ),
        Section(
            "Alpine.js",
            paragraph(
                "Alpine.js adds lightweight reactivity directly in HTML — toggles, "
                "counters, tabs, and modals without a build step. Trunco maps "
                "Alpine directives through add_directive() and the Directive enum."
            ),
            CodePanel(
                """from trunco.alpine import Directive, alpine_script_tag

print(alpine_script_tag())""",
            ),
            paragraph(
                "Directive covers the common Alpine attributes: X_DATA, X_SHOW, "
                "X_ON_CLICK, X_TEXT, X_IF, X_FOR, and more."
            ),
            CodePanel(
                """from trunco import Component
from trunco.alpine import Directive

panel = Component(tag="div")
panel.add_directive(Directive.X_DATA, "{ open: false }")

toggle = Component(tag="button")
toggle.add_directive(Directive.X_ON_CLICK, "open = !open")
toggle.add_child("Toggle panel")

body = Component(tag="div")
body.add_directive(Directive.X_SHOW, "open")
body.add_child("Panel content")

panel.add_child(toggle)
panel.add_child(body)""",
            ),
            paragraph(
                "When HTMX swaps new HTML into the page, call Alpine.initTree() "
                "on the swapped element so directives inside the fragment activate. "
                "This site does that automatically after each navigation swap."
            ),
            CodePanel(
                """document.body.addEventListener("htmx:afterSwap", (e) => {
  if (e.detail.target.id !== "main-content") return;
  if (window.Alpine) Alpine.initTree(e.detail.target);
});""",
                language="javascript",
            ),
            Callout(
                "Combine both: use HTMX for server-driven updates and Alpine for "
                "instant client-side UI state on the same page."
            ),
            anchor="alpine",
            badge=Badge("Alpine.js", color="ghost", size="sm"),
        ),
        NextSteps(
            [
                ("Explore", "Kit Reference →", "kits.html"),
                ("Learn", "Core Components →", "components.html"),
            ]
        ),
        lead=(
            "Ship hypermedia and client interactivity from Python — HTMX for "
            "server-driven partial updates, Alpine.js for lightweight UI state."
        ),
        breadcrumb=[
            ("Documentation", "index.html"),
            ("Guide", None),
            ("Integrations", None),
        ],
        toc=[("install", "Install"), ("htmx", "HTMX"), ("alpine", "Alpine.js")],
    )
