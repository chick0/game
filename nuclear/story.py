
from . import FLAG
from . import VALUE
from .handler import *


def start():
    start_event_id = [
        'little_house'
    ]

    event_id = random.choice(start_event_id)

    event.get(event_id)()
