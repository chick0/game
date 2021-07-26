
from . import AUTHOR
from . import TITLE
from .handler import *


def start():
    print(f"{AUTHOR}'s '{TITLE}'")
    start_event_id = [
        "little_house",
        "container",
    ]

    event_id = random.choice(start_event_id)
    event.get(event_id)()
