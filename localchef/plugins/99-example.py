MENU_NAME = "ExamplePlugin"

def ONLOAD():
    """Called when the plugin is loaded."""
    print(f"{MENU_NAME} plugin loaded.")

def process(text):
    """Process the input text and return the result."""
    return text.strip() + " (processed by ExamplePlugin)"
