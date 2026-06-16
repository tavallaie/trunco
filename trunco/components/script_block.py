from typing import Optional

from trunco.base import Component


class ScriptBlock(Component):
    """JavaScript via ``<script>`` — external ``src`` or inline ``content``."""

    def __init__(
        self,
        *,
        src: Optional[str] = None,
        content: Optional[str] = None,
        defer: bool = False,
        module: bool = False,
        **kwargs,
    ):
        super().__init__(tag="script", **kwargs)
        if src:
            self.add_attribute("src", src)
        if defer:
            self.add_attribute("defer", "defer")
        if module:
            self.add_attribute("type", "module")
        if content:
            self.add_child(content)