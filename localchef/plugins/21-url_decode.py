MENU_NAME = "URL Decode"

from urllib.parse import unquote

def process(text):
    try:
        return unquote(text.strip())
    except Exception as e:
        return f"Decoding error: {e}"
