 # Trunco Components

 This document provides an overview of the built-in components available in **Trunco**. These components can be used to create dynamic, reusable HTML elements in your Python applications.

 ## Table of Contents

 - [ButtonComponent](#buttoncomponent)
 - [FormComponent](#formcomponent)
 - [InputComponent](#inputcomponent)
 - [TextAreaComponent](#textareacomponent)
 - [CheckboxComponent](#checkboxcomponent)
 - [RadioComponent and RadioGroupComponent](#radiocomponent-and-radiogroupcomponent)
 - [SliderComponent](#slidercomponent)
 - [TableComponent](#tablecomponent)
 - [ListComponent and ListItemComponent](#listcomponent-and-listitemcomponent)
 - [LinkComponent](#linkcomponent)
 - [ImageComponent](#imagecomponent)
 - [HeadingComponent](#headingcomponent)
 - [ParagraphComponent](#paragraphcomponent)
 - [CodeComponent](#codecomponent)
 - [DividerComponent](#dividercomponent)
 - [LabelComponent](#labelcomponent)
 - [BlockquoteComponent](#blockquotecomponent)

 ## ButtonComponent

 The `ButtonComponent` is used to create a clickable button element. You can customize the label and the onClick action.

 ```python
 button = ButtonComponent(label="Click Me", on_click="alert('Hello!')")
 ```

 This will render:

 ```html
 <button id="unique-button-id" class="btn" x-on:click="alert('Hello!')">Click Me</button>
 ```

 ## FormComponent

 The `FormComponent` is used to create a form element that can contain other input elements and handle submission.

 ```python
 form = FormComponent(action="/submit", method="post")
 form.add_child(InputComponent(input_type="text", placeholder="Enter your name"))
 form.add_child(ButtonComponent(label="Submit"))
 ```

 This will render:

 ```html
 <form id="unique-form-id" action="/submit" method="post">
     <input id="unique-input-id" type="text" placeholder="Enter your name">
     <button id="unique-button-id" class="btn">Submit</button>
 </form>
 ```

 ## InputComponent

 The `InputComponent` is used to create various types of input fields, such as text, email, and password.

 ```python
 input_field = InputComponent(input_type="email", placeholder="Enter your email")
 ```

 This will render:

 ```html
 <input id="unique-input-id" type="email" placeholder="Enter your email">
 ```

 ## TextAreaComponent

 The `TextAreaComponent` is used to create a multi-line text input field.

 ```python
 textarea = TextAreaComponent(rows=5, cols=40, placeholder="Enter your comments")
 ```

 This will render:

 ```html
 <textarea id="unique-textarea-id" rows="5" cols="40">Enter your comments</textarea>
 ```

 ## CheckboxComponent

 The `CheckboxComponent` is used to create a checkbox input field.

 ```python
 checkbox = CheckboxComponent(label="Accept Terms", checked=True)
 ```

 This will render:

 ```html
 <input id="unique-checkbox-id" type="checkbox" checked="checked"><label>Accept Terms</label>
 ```

 ## RadioComponent and RadioGroupComponent

 The `RadioComponent` is used to create a single radio button. You can group radio buttons together using `RadioGroupComponent`.

 ```python
 radio1 = RadioComponent(name="options", value="1", label="Option 1", checked=True)
 radio2 = RadioComponent(name="options", value="2", label="Option 2")
 radio_group = RadioGroupComponent(name="options", options=[radio1, radio2])
 ```

 This will render:

 ```html
 <div id="unique-group-id">
     <input id="unique-radio1-id" type="radio" name="options" value="1" checked="checked"><label>Option 1</label>
     <input id="unique-radio2-id" type="radio" name="options" value="2"><label>Option 2</label>
 </div>
 ```

 ## SliderComponent

 The `SliderComponent` is used to create a range input (slider).

 ```python
 slider = SliderComponent(min_value=0, max_value=100, step=5, value=50)
 ```

 This will render:

 ```html
 <input id="unique-slider-id" type="range" min="0" max="100" step="5" value="50">
 ```

 ## TableComponent

 The `TableComponent` is used to create tables, along with `TableRowComponent` and `TableCellComponent`.

 ```python
 table = TableComponent(
     headers=["Name", "Age"],
     rows=[
         TableRowComponent(cells=[TableCellComponent(content="John"), TableCellComponent(content="30")]),
         TableRowComponent(cells=[TableCellComponent(content="Jane"), TableCellComponent(content="25")])
     ]
 )
 ```

 This will render:

 ```html
 <table id="unique-table-id">
     <tr id="unique-header-row-id"><th>Name</th><th>Age</th></tr>
     <tr id="unique-row-id"><td>John</td><td>30</td></tr>
     <tr id="unique-row-id"><td>Jane</td><td>25</td></tr>
 </table>
 ```

 ## ListComponent and ListItemComponent

 The `ListComponent` is used to create unordered or ordered lists, along with `ListItemComponent`.

 ```python
 ul = ListComponent(ordered=False, items=[
     ListItemComponent(content="Item 1"),
     ListItemComponent(content="Item 2")
 ])
 ```

 This will render:

 ```html
 <ul id="unique-ul-id">
     <li>Item 1</li>
     <li>Item 2</li>
 </ul>
 ```

 ## LinkComponent

 The `LinkComponent` is used to create hyperlinks.

 ```python
 link = LinkComponent(href="https://example.com", text="Visit Example")
 ```

 This will render:

 ```html
 <a id="unique-link-id" href="https://example.com" target="_self">Visit Example</a>
 ```

 ## ImageComponent

 The `ImageComponent` is used to display images.

 ```python
 image = ImageComponent(src="https://example.com/image.jpg", alt="Example Image")
 ```

 This will render:

 ```html
 <img id="unique-image-id" src="https://example.com/image.jpg" alt="Example Image">
 ```

 ## HeadingComponent

 The `HeadingComponent` is used to create headings (h1, h2, etc.).

 ```python
 heading = HeadingComponent(tag="h1", text="Welcome to Trunco")
 ```

 This will render:

 ```html
 <h1 id="unique-heading-id">Welcome to Trunco</h1>
 ```

 ## ParagraphComponent

 The `ParagraphComponent` is used to create paragraphs.

 ```python
 paragraph = ParagraphComponent(text="This is a paragraph.")
 ```

 This will render:

 ```html
 <p id="unique-paragraph-id">This is a paragraph.</p>
 ```

 ## CodeComponent

 The `CodeComponent` is used to display code snippets.

 ```python
 code = CodeComponent(code="print('Hello, world!')")
 ```

 This will render:

 ```html
 <code id="unique-code-id">print('Hello, world!')</code>
 ```

 ## DividerComponent

 The `DividerComponent` is used to create horizontal dividers.

 ```python
 divider = DividerComponent()
 ```

 This will render:

 ```html
 <hr id="unique-divider-id">
 ```

 ## LabelComponent

 The `LabelComponent` is used to create labels for input elements.

 ```python
 label = LabelComponent(text="Username", for_input_id="username-input")
 ```

 This will render:

 ```html
 <label id="unique-label-id" for="username-input">Username</label>
 ```

 ## BlockquoteComponent

 The `BlockquoteComponent` is used to display block quotes.

 ```python
 blockquote = BlockquoteComponent(quote="This is a blockquote.")
 ```

 This will render:

 ```html
 <blockquote id="unique-blockquote-id">This is a blockquote.</blockquote>
 ```

 ## Creating Custom Components

 In addition to the built-in components, you can create custom components by extending the `Component` class. This allows you to create reusable components that fit your specific needs.

 ```python
 from trunco import Component

 class CustomComponent(Component):
     def __init__(self, content: str, **kwargs):
         super().__init__(tag="div", **kwargs)
         self.children.append(content)
 ```

 This custom component can be used just like any other Trunco component.

 ## Conclusion

 Trunco provides a powerful, flexible way to build dynamic HTML components in Python. Whether you're creating simple buttons or complex forms, Trunco's component-based approach will help you build maintainable and reusable code.
