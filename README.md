 # Trunco

 **Trunco** is a modern Python framework for building dynamic, reusable, and modular HTML components. Designed with web developers in mind, Trunco provides a simple and Pythonic API that integrates seamlessly with popular web frameworks like Django, Flask, and FastAPI. Whether you’re building simple pages or complex web applications, Trunco gives you the tools to create clean, maintainable, and reusable components.

 ## Features

 - **Component-Based Architecture**: Trunco encourages the use of components, making your HTML more modular and easier to manage.
 - **Context Support**: Pass dynamic data into your components easily, allowing for flexible and adaptive UI elements.
 - **Alpine.js and HTMX Integration**: Build reactive and interactive components with built-in support for Alpine.js and HTMX directives.
 - **Seamless Integration**: Trunco works out-of-the-box with Django, Flask, FastAPI, and other popular web frameworks.
 - **Extensible**: Easily extend and customize components, or create your own, to fit your specific needs.
 - **Custom Directives and Attributes**: Leverage the power of custom HTML attributes and directives to build rich, interactive UIs.

 ## Installation

 To start using Trunco, you can install it directly from PyPI using pip:

 ```bash
 pip install trunco
 ```

 Trunco requires Python 3.6+.

 ## Basic Usage

 Creating components with Trunco is straightforward. Here’s an example of how to create a basic button component:

 ```python
 from trunco.components import ButtonComponent

 button = ButtonComponent(label="Click Me", on_click="alert('Hello World!')")
 print(button)
 ```

 This will output the following HTML:

 ```html
 <button id="unique-button-id" class="btn" x-on:click="alert('Hello World!')">Click Me</button>
 ```

 ## Advanced Usage

 Trunco is more than just simple components. It allows for complex layouts and interactions. Here’s an example of a form with multiple inputs:

 ```python
 from trunco.components import FormComponent, InputComponent, ButtonComponent

 form = FormComponent(action="/submit", method="post")
 form.add_child(InputComponent(input_type="text", placeholder="Enter your name"))
 form.add_child(InputComponent(input_type="email", placeholder="Enter your email"))
 form.add_child(ButtonComponent(label="Submit", on_click="submitForm()"))

 print(form)
 ```

 This will generate the following HTML:

 ```html
 <form id="unique-form-id" action="/submit" method="post">
     <input id="input1-id" type="text" placeholder="Enter your name">
     <input id="input2-id" type="email" placeholder="Enter your email">
     <button id="button-id" class="btn" x-on:click="submitForm()">Submit</button>
 </form>
 ```

 ## Documentation

 Full documentation is available in the `docs` directory, covering everything from installation to advanced component usage.

 - [Installation Guide](docs/installation.md)
 - [Components](docs/components.md)
 - [Usage Examples](docs/usage.md)

 ## Examples

 Check out the `examples` directory for more code samples demonstrating how to use Trunco in different scenarios:

 - **basic_usage.py**: Simple examples to get you started.
 - **advanced_usage.py**: More complex usage involving forms, tables, and dynamic content.
 - **form_example.py**: Demonstrates how to build and handle forms using Trunco.

 ## Contributing

 We welcome contributions from the community! If you'd like to contribute, please follow these steps:

 1. Fork the repository.
 2. Create a new branch for your feature or bugfix.
 3. Implement your changes.
 4. Write tests to ensure your changes work as expected.
 5. Submit a pull request with a clear description of your changes.

 ## License

 Trunco is open-source software licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

 ## Contact

 If you have any questions, suggestions, or feedback, feel free to reach out. We’re here to help you get the most out of Trunco.
