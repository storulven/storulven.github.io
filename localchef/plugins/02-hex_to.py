MENU_NAME = "To hex-string"

from binascii import hexlify
def process(text):
    """Process the input text and return the result."""
    return hexlify(text.strip().encode('utf-8')).decode('utf-8')