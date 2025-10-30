MENU_NAME = "Base64 Decode"

import base64
def process(text):
    """Process the input text and return the result."""
    try: 
        return base64.b64decode(text.strip().encode('utf-8')).decode('utf-8')
    except Exception as e:
        return f"Decoding error: {e}"