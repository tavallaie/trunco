"""0build (zbuild) kit — formerly Franken UI."""

from trunco.zbuild import Alert, Button, Form, FormControl, Input, Page, set_theme


def main():
    set_theme(palette="sapphire", layout="z-layout-small", mode="light")

    form = Form(action="/login")
    form.add_child(FormControl(label="Username", field=Input(placeholder="jane")))
    form.add_child(FormControl(label="Password", field=Input(input_type="password")))
    form.add_child(Button(label="Log in", color="primary"))
    form.add_child(Alert(message="Secure login.", color="info"))

    page = Page(form, palette="sapphire")
    print(page.render())


if __name__ == "__main__":
    main()
