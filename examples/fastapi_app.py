"""FastAPI app serving Trunco components."""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from trunco.zbuild import Alert, Button, Form, FormControl, Input, Page
from trunco.zbuild import core_script_tag, kit_css_tag, zuikit_script_tag

app = FastAPI(title="Trunco + FastAPI")


@app.get("/", response_class=HTMLResponse)
def index():
    form = Form(action="/api/save")
    form.add_child(FormControl(label="Task", field=Input(placeholder="What to do?")))
    form.add_child(Button(label="Add", color="primary"))
    form.add_child(Alert(message="Powered by 0build kit.", color="info"))

    body = Page(form, palette="sapphire").render()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Trunco + FastAPI</title>
  {kit_css_tag()}
  {core_script_tag()}
</head>
<body>
  {body}
  {zuikit_script_tag()}
</body>
</html>"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
