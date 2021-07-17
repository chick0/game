from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "1번가"
event_id = __name__


def start():
    print_title(title=title)

    for text in [
        "평펌한 거리 1번가가 당신을 환영합니다.",
        ""
    ]:
        print_message(text=text)

    ev_map = {
        "2번가로 이동하기": event.get("street_no1"),
        "편의점": event.get("street_no1"),
        "식당": event.get("street_no1"),
        "철수네 집": event.get("street_no1"),
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
