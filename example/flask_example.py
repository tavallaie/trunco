from flask import Flask, render_template_string
from trunco.components import ButtonComponent

app = Flask(__name__)


@app.route("/")
def index():
    # Create the button component
    button = ButtonComponent(label="Click Me", on_click="alert('Button clicked!')")

    # Define the HTML template including Alpine.js and HTMX
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Trunco Example</title>
        <!-- Include Alpine.js -->
        <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
        <!-- Include HTMX -->
        <script src="https://unpkg.com/htmx.org@1.x.x"></script>
    </head>
    <body>
        {button}
    </body>
    </html>
    """

    # Render the HTML with the button component
    return render_template_string(html_template)


if __name__ == "__main__":
    app.run(debug=True)
