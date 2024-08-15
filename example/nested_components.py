from trunco.components import FormComponent, InputComponent, ButtonComponent

# Create a nested form component with multiple input fields
form = FormComponent(action="/submit", method="post")
form.add_child(InputComponent(input_type="text", placeholder="First Name"))
form.add_child(InputComponent(input_type="email", placeholder="Email Address"))
form.add_child(ButtonComponent(label="Submit"))

# Render the form to HTML
print(form)
