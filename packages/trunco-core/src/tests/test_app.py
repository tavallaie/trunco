import unittest
from trunco import App
from trunco import Component


# A simple dummy component for testing purposes.
class DummyComponent(Component):
    def __init__(self, text):
        # We'll render this as a simple paragraph.
        super().__init__(tag="p")
        self.text = text

    def render(self, context=None):
        return f"<p>{self.text}</p>"


class TestAppRender(unittest.TestCase):
    def test_render_without_framework(self):
        # Initialize the app without a framework.
        app = App()
        dummy = DummyComponent("Hello")
        app.add_child(dummy)
        output = app.render()
        # Verify the child component renders correctly.
        self.assertIn("<p>Hello</p>", output)
        # Ensure no Franken UI assets are included.
        self.assertNotIn("franken-ui.dev", output)

    def test_render_with_franken_framework(self):
        # Initialize the app with the 'franken' framework flag.
        app = App(framework="franken")
        dummy = DummyComponent("Hello")
        app.add_child(dummy)
        output = app.render()
        # Verify the child component renders correctly.
        self.assertIn("<p>Hello</p>", output)
        # Check that the head section includes the Franken UI asset links.
        self.assertIn("https://franken-ui.dev/assets/franken.css", output)
        self.assertIn("https://franken-ui.dev/assets/franken.js", output)


if __name__ == "__main__":
    unittest.main()
