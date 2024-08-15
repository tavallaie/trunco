 # Trunco Usage Guide

 This guide provides practical examples and best practices for using **Trunco** to create dynamic, reusable HTML components in your Python applications.

 ## Table of Contents

 - [Basic Usage](#basic-usage)
 - [Including Alpine.js and HTMX](#including-alpinejs-and-htmx)
 - [Working with Context](#working-with-context)
 - [Nested Components](#nested-components)
 - [Handling Events](#handling-events)
 - [Styling Components](#styling-components)
 - [Custom Directives](#custom-directives)
 - [Advanced Usage](#advanced-usage)
 - [Integrating with Web Frameworks](#integrating-with-web-frameworks)

 ## Basic Usage

 Trunco makes it easy to create and render HTML components in Python. Here’s a simple example of creating a button:

 ```python
 from trunco.components import ButtonComponent

 button = ButtonComponent(label="Click Me", on_click="alert('Button clicked!')")
 print(button)
 ```

 This will generate the following HTML:

 ```html
 <button id="unique-button-id" class="btn" x-on:click="alert('Button clicked!')">Click Me</button>
 ```

 ## Including Alpine.js and HTMX

 If you plan to use Trunco components that rely on Alpine.js or HTMX for handling interactivity and events, you'll need to include these libraries in your HTML.

 ### Adding Alpine.js

 Add the following script tag in the `<head>` section of your HTML to include Alpine.js:

 ```html
 <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
 ```

 ### Adding HTMX

 Similarly, include HTMX by adding the following script tag:

 ```html
 <script src="https://unpkg.com/htmx.org@1.x.x"></script>
 ```

 Once these libraries are included, your Trunco components will be able to utilize their functionalities.

 ## Working with Context

 Context in Trunco allows you to pass dynamic data to components, making it easier to create components that adapt to changing data.

 ```python
 from trunco.components import ParagraphComponent

 context = {"message": "Hello, Trunco!"}
 paragraph = ParagraphComponent(text="{message}")

 print(paragraph.render(context))
 ```

 This will output:

 ```html
 <p id="unique-paragraph-id">Hello, Trunco!</p>
 ```

 ## Nested Components

 Trunco supports nesting components within other components. For example, you can nest multiple input fields within a form:

 ```python
 from trunco.components import FormComponent, InputComponent, ButtonComponent

 form = FormComponent(action="/submit", method="post")
 form.add_child(InputComponent(input_type="text", placeholder="Enter your name"))
 form.add_child(InputComponent(input_type="email", placeholder="Enter your email"))
 form.add_child(ButtonComponent(label="Submit"))

 print(form)
 ```

 This will render:

 ```html
 <form id="unique-form-id" action="/submit" method="post">
     <input id="unique-input-id" type="text" placeholder="Enter your name">
     <input id="unique-input-id" type="email" placeholder="Enter your email">
     <button id="unique-button-id" class="btn">Submit</button>
 </form>
 ```

 ## Handling Events

 Trunco integrates seamlessly with Alpine.js and HTMX to handle events like clicks. Here’s how you can handle a button click:

 ```python
 from trunco.components import ButtonComponent

 button = ButtonComponent(label="Click Me", on_click="alert('Button clicked!')")
 print(button)
 ```

 This will generate the following HTML:

 ```html
 <button id="unique-button-id" class="btn" x-on:click="alert('Button clicked!')">Click Me</button>
 ```

 ## Styling Components

 You can add custom styles to components by passing CSS classes or inline styles:

 ```python
 from trunco.components import ParagraphComponent

 paragraph = ParagraphComponent(text="Styled paragraph")
 paragraph.add_class("text-primary")
 paragraph.add_style("font-weight", "bold")

 print(paragraph)
 ```

 This will render:

 ```html
 <p id="unique-paragraph-id" class="text-primary" style="font-weight: bold;">Styled paragraph</p>
 ```

 ## Custom Directives

 Trunco allows you to add custom Alpine.js or HTMX directives to components:

 ```python
 from trunco.components import ButtonComponent

 button = ButtonComponent(label="Click Me")
 button.add_directive("x-data", "{ count: 0 }")
 button.add_directive("x-on:click", "count++")

 print(button)
 ```

 This will render:

 ```html
 <button id="unique-button-id" class="btn" x-data="{ count: 0 }" x-on:click="count++">Click Me</button>
 ```

 ## Advanced Usage

 Trunco also supports more advanced usage scenarios, such as:

 - **Dynamic components**: Create components that render based on dynamic data.
 - **Custom components**: Extend the `Component` class to create your own reusable components.
 - **Complex forms**: Build forms with validation and complex layouts.

 Explore the advanced features in the [Components](components.md) documentation.

  ## Integrating with Web Frameworks

 Trunco can be easily integrated into Django, Flask, FastAPI, and other web frameworks. Here’s a basic example with Flask:

 ```python
 from flask import Flask, render_template_string
 from trunco.components import ButtonComponent

 app = Flask(__name__)

 @app.route('/')
 def index():
     button = ButtonComponent(label="Click Me", on_click="alert('Button clicked!')")
     
     html_template = f'''
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
     '''
     
     return render_template_string(html_template)

 if __name__ == '__main__':
     app.run(debug=True)
 ```

 This creates a simple Flask application that renders a button. Make sure to include Alpine.js and HTMX in your HTML template for full functionality. You can apply similar approaches in Django and FastAPI.

