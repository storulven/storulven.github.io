MENU_NAME = "ROT13"

import codecs
def process(text):
    return codecs.encode(text, 'rot13')