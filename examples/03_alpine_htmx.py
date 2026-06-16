"""Alpine.js and HTMX integrations."""

from trunco import Component, HxMethod, Swap, Trigger
from trunco.alpine import Directive, alpine_script_tag
from trunco.htmx import htmx_script_tag


def main():
    panel = Component(tag="div")
    panel.add_directive(Directive.X_DATA, "{ count: 0 }")
    panel.add_directive(Directive.X_TEXT, "count")

    loader = Component(
        hx_methods=HxMethod.get("/api/items"),
        trigger=Trigger.CLICK,
        swap=Swap.INNER_HTML,
    )
    loader.add_child("Load more")

    print("<!-- Alpine + HTMX assets -->")
    print(alpine_script_tag())
    print(htmx_script_tag())
    print()
    print(panel.render())
    print(loader.render())


if __name__ == "__main__":
    main()
