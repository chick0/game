from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "2번가"
event_id = __name__


def start():
    timer.check()
    print_title(title=title)

    for text in [
        "평펌한 거리 2번가가 당신을 환영합니다.",
    ]:
        print_message(text=text)

    ev_map = {
        "1번가로 이동하기": event.get("street_no1"),
        "3번가로 이동하기": event.get("street_no3"),
        "병원": event.get("hospital"),
        "경찰서": event.get("police"),
        "식당": event.get("snack_bar_no2"),
        "편의점": event.get("convenience_store_no2"),
        "지하철 역": event.get("subway_station_no2"),
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
