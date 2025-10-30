MENU_NAME = "Base64 Encode"

import base64
def process(text):
    """Process the input text and return the result."""
    try: 
        return base64.b64encode(text.strip().encode('utf-8')).decode('utf-8')
    except Exception as e:
        return f"Encoding error: {e}"