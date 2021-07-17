from time import sleep
from hashlib import sha1

from nuclear import VALUE


def print_title(title: str):
    print(f"\n\n\n[ {title} ]")


def print_message(text: str):
    print("   ", text)

    text_id = sha1(text.encode()).hexdigest()
    if not VALUE['event'].get(text_id, None):
        VALUE['event'][text_id] = True
        sleep(0.35)
