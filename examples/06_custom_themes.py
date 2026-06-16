"""Register custom color schemes for DaisyUI and 0build."""

from trunco.daisy import Button, Page, register_theme, theme_style_tag
from trunco.zbuild import palette_style_tag, register_palette


def main():
    register_theme(
        name="brand",
        colors={
            "primary": "#1EA1F1",
            "secondary": "#0d9488",
            "base-100": "#f8fafc",
            "base-content": "#0f172a",
        },
        set_active=True,
    )

    register_palette(
        name="brand",
        light={"primary": "#1EA1F1", "primary-f": "#ffffff"},
        dark={"primary": "#0ea5e9", "primary-f": "#ffffff"},
    )

    print("=== DaisyUI custom theme CSS ===")
    print(theme_style_tag())
    print()
    print("=== 0build custom palette CSS ===")
    print(palette_style_tag())
    print()
    print("=== DaisyUI page ===")
    print(Page(Button(label="Launch", color="primary"), theme_name="brand").render())


if __name__ == "__main__":
    main()
