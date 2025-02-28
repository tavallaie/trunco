from trunco import franken

button = franken.button(
    label="Submit",
    on_click="alert('Submitted!')",
    style_modifier="uk-btn-primary",
    size_modifier="uk-btn-lg",
)
print(str(button))
