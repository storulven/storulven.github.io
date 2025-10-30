MENU_NAME = "From hex-string"

import binascii
def process(text):
    """Process the input text and return the result."""
    try:
        return binascii.unhexlify(text.strip().encode('utf-8')).decode('utf-8')
    except binascii.Error:
        return "Invalid hex string."