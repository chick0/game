from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "편의점 우측 진열대"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    from nuclear.items import items
    rand_item = random.choice(list(items.keys()))

    print_message(text=f"진열대에서 '{rand_item}'을(를) 발견했다.")
    item.get([rand_item])

    return None
