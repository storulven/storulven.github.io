MENU_NAME = "JWT Decode"
from base64 import b64decode

def process(text):
    if text.count(".") != 2:
        return "Invalid JWT format."
    sp = text.split(".")
    try:
        header = b64decode(sp[0] + "===").decode('utf-8')
        payload = b64decode(sp[1] + "===").decode('utf-8')
    except Exception as e:
        return f"Decoding error: {e}"
    return f"Header:\n{header}\n\nPayload:\n{payload}"