from time import sleep
from hashlib import sha1

from nuclear import VALUE


def print_title(title: str):
    print(f"\n\n\n[ {title} ]")


def print_message(text: str, no_wait: bool = False):
    print("  ", text)

    text_id = sha1(text.encode()).hexdigest()
    if not VALUE['event'].get(text_id, None):
        VALUE['event'][text_id] = len(text)
        if not no_wait:
            sleep(0.65)
