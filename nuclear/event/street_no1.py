from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "1번가"
event_id = __name__


def start():
    timer.check()
    print_title(title=title)

    for text in [
        "평펌한 거리 1번가가 당신을 환영합니다.",
    ]:
        print_message(text=text)

    ev_map = {
        "2번가로 이동하기": event.get("street_no2"),
        "주유소": event.get("gas_station"),
        "식당": event.get("snack_bar"),
        "놀이터": event.get("playground"),
        "편의점": event.get("convenience_store"),
        "철수네 집": event.get("chul_soo_house"),
        "교회": event.get("church"),
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
