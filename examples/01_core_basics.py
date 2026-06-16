"""Core Trunco components — no UI kit required."""

from trunco.components.button import ButtonComponent
from trunco.components.form import FormComponent
from trunco.components.input import InputComponent
from trunco.components.heading import HeadingComponent
from trunco.enums import Method


def main():
    form = FormComponent(action="/contact", method=Method.POST)
    form.add_child(HeadingComponent(tag="h2", text="Contact us"))
    form.add_child(InputComponent(input_type="text", placeholder="Your name"))
    form.add_child(InputComponent(input_type="email", placeholder="Your email"))
    form.add_child(ButtonComponent(label="Send message"))
    print(form.render())


if __name__ == "__main__":
    main()
