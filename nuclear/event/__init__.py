from time import sleep
from hashlib import sha1

from nuclear import VALUE


def print_title(title: str, no_warp: bool = False):
    if not no_warp:
        print("\n\n")

    print(f"[ {title} ]")


def print_message(text: str, no_wait: bool = False, no_indent: bool = False):
    indent = "   " if no_indent is False else ""
    print(indent, text, sep="")

    if not no_wait:
        text_id = sha1(text.encode()).hexdigest()
        if not VALUE['event'].get(text_id, None):
            VALUE['event'][text_id] = len(text)
            sleep(0.65)
