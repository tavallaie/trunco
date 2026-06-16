"""Same component API — swap kits by changing the import."""

import trunco.daisy as ui


def build_signup_form(kit):
    form = kit.Form(action="/signup")
    form.add_child(
        kit.FormControl(
            label="Email",
            field=kit.Input(placeholder="you@example.com"),
        )
    )
    form.add_child(kit.Button(label="Join", color="primary"))
    form.add_child(kit.Alert(message="Welcome!", color="success"))
    return form


def main():
    print("=== DaisyUI ===")
    print(build_signup_form(ui).render())
    print()

    import trunco.zbuild as zbuild

    print("=== 0build ===")
    print(build_signup_form(zbuild).render())


if __name__ == "__main__":
    main()