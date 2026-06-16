from trunco.base import Component


class DaisyCard(Component):
    """DaisyUI card component with optional title and body sections."""

    def __init__(
        self,
        title: str | None = None,
        body: str | Component | None = None,
        image_src: str | None = None,
        compact: bool = False,
        **kwargs,
    ):
        super().__init__(tag="div", **kwargs)
        self.add_class("card")
        self.add_class("bg-base-100")
        self.add_class("shadow-md")
        if compact:
            self.add_class("card-compact")

        if image_src:
            figure = Component(tag="figure")
            image = Component(tag="img")
            image.add_attribute("src", image_src)
            image.add_attribute("alt", title or "")
            figure.add_child(image)
            self.add_child(figure)

        card_body = Component(tag="div")
        card_body.add_class("card-body")

        if title:
            title_el = Component(tag="h2")
            title_el.add_class("card-title")
            title_el.add_child(title)
            card_body.add_child(title_el)

        if body is not None:
            if isinstance(body, Component):
                card_body.add_child(body)
            else:
                paragraph = Component(tag="p")
                paragraph.add_child(body)
                card_body.add_child(paragraph)

        self.add_child(card_body)
