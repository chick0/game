from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "3번가"
event_id = __name__


def start():
    print_title(title=title)

    for text in [
        "평펌한 거리 3번가가 당신을 환영합니다.",
        ""
    ]:
        print_message(text=text)

    ev_map = {
        "2번가로 이동하기": event.get("street_no2"),
        "숲": event.get("forest"),
        "군부대": event.get("military"),
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
