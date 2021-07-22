from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 1층"
event_id = __name__


def start():
    print_title(title=title)

    ev_map = {
        "복도로 돌아가기": event.get("hospital"),
        "2층으로 올라가기": event.get("hospital_2f"),
        "1층 안내데스크": event.get("hospital_1f_info"),
        "1층 화장실": event.get("hospital_1f_bathroom"),
        "1층 약국": event.get("hospital_1f_pharmacy"),
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
