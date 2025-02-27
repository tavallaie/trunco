from trunco.components import ParagraphComponent

# Define context with dynamic data
context = {"message": "Hello, Trunco!"}

# Create a paragraph component that uses the context
paragraph = ParagraphComponent(text="{message}")

# Render the paragraph with the context applied
print(paragraph.render(context))
