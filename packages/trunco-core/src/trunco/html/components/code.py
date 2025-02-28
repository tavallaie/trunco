from trunco.html.base import Component


class CodeComponent(Component):
    """
    A basic code component for displaying code snippets.
    """

    def __init__(self, code: str = "{code}", **kwargs):
        super().__init__(tag="code", **kwargs)
        # Use unified add() method for adding the code string as a child.
        self.add(code)
