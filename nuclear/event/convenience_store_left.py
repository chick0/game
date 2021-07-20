
from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "편의점 좌측 진열대"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    print_message(text="진열대에서 과자를 발견했다.")
    item.get(["과자"] * random.choice([1, 1, 2, 2, 2, 2, 3, 3, 4, 5]))

    return None
