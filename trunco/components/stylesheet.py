from typing import Optional

from trunco.base import Component


class Stylesheet(Component):
    """External CSS stylesheet (``<link rel=\"stylesheet\">``)."""

    def __init__(
        self,
        href: str,
        *,
        media: Optional[str] = None,
        crossorigin: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(tag="link", **kwargs)
        self.add_attribute("rel", "stylesheet")
        self.add_attribute("href", href)
        if media:
            self.add_attribute("media", media)
        if crossorigin:
            self.add_attribute("crossorigin", crossorigin)


class InlineStyle(Component):
    """Embedded CSS in a ``<style>`` element."""

    def __init__(self, css: str, **kwargs):
        super().__init__(tag="style", **kwargs)
        self.add_child(css)
