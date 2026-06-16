"""DaisyUI kit with short import names."""

from trunco.daisy import Alert, Button, Form, FormControl, Input, Page, set_theme


def main():
    set_theme("light")

    form = Form(action="/signup")
    form.add_child(
        FormControl(
            label="Email",
            field=Input(placeholder="you@example.com", color="bordered"),
            help_text="We'll never share your email.",
        )
    )
    form.add_child(Button(label="Sign up", color="primary"))
    form.add_child(Alert(message="All fields are required.", color="info"))

    page = Page(form, theme_name="light")
    print(page.render())


if __name__ == "__main__":
    main()