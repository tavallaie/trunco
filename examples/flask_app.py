"""Flask app serving Trunco components."""

from flask import Flask, render_template_string

from trunco.daisy import Button, Form, FormControl, Input, Page, alpine_script_tag
from trunco.htmx import htmx_script_tag

app = Flask(__name__)


@app.route("/")
def index():
    form = Form(action="/submit")
    form.add_child(FormControl(label="Name", field=Input(placeholder="Your name")))
    form.add_child(Button(label="Submit", color="primary", on_click="alert('Submitted!')"))

    page = Page(form, theme_name="light")
    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en" data-theme="light">
        <head>
          <meta charset="utf-8" />
          <title>Trunco + Flask</title>
          <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" />
          <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
        </head>
        <body>
          {{ content | safe }}
          {{ alpine | safe }}
          {{ htmx | safe }}
        </body>
        </html>
        """,
        content=page.render(),
        alpine=alpine_script_tag(),
        htmx=htmx_script_tag(),
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
