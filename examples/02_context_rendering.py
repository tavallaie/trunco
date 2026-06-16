"""Render components with dynamic context placeholders."""

from trunco.components.button import ButtonComponent
from trunco.components.paragraph import ParagraphComponent


def main():
    button = ButtonComponent(label="{label}")
    paragraph = ParagraphComponent(text="Hello, {name}!")

    print(button.render({"label": "Dynamic Button"}))
    print(paragraph.render({"name": "Trunco"}))


if __name__ == "__main__":
    main()