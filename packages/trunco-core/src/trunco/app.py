from trunco.base import Component


class App(Component):
    def __init__(self, framework=None, **kwargs):
        # Initialize as a container component (using a <div> tag)
        super().__init__(tag="div", **kwargs)
        self.framework = framework
        self.children = []  # list to hold child components

    def add_child(self, child):
        """Adds a child component (or HTML string) to the app."""
        self.children.append(child)

    def render(self, context=None) -> str:
        # Render each child (if it’s a Component, call its render; else, treat as string)
        children_html = "".join(
            child.render(context) if hasattr(child, "render") else str(child)
            for child in self.children
        )
        # If the framework is 'franken', inject the extra head assets.
        head_html = ""
        if self.framework == "franken":
            head_html = (
                '<link rel="stylesheet" href="https://franken-ui.dev/assets/franken.css">'
                '<script src="https://franken-ui.dev/assets/franken.js"></script>'
            )
        # Wrap in basic HTML structure.
        full_html = (
            "<!DOCTYPE html>\n"
            "<html>\n"
            f"<head>{head_html}</head>\n"
            f"<body>{children_html}</body>\n"
            "</html>"
        )
        return full_html
