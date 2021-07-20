from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "편의점"
event_id = __name__


def door_shutdown():
    if flag.check(event_id, True):
        return "street_no1"
    else:
        flag.update(event_id, True)
        print_message(text="당신이 편의점에서 나오는 순간 간판이 떨어지며 편의점의 문이 막힙니다.")
        print_message(text="뒷문은 잠겨있어 들어갈 수 없습니다.")


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        print_message(text="편의점 안으로 들어갈 수 있는 문이 없습니다.")
        return

    for text in [
        "다양한 물건을 팔고 있었던 편의점이다.",
        "하지만 지금은 아무도 없는 조용한 편의점이다."
    ]:
        print_message(text=text)

    ev_map = {
        "계산대": event.get("convenience_store_counter"),
        "냉장고": event.get("convenience_store_refrigerator"),
        "좌측 진열대": event.get("convenience_store_left"),
        "우측 진열대": event.get("convenience_store_right"),
        "뒷문": event.get("convenience_store_back_door"),
        "1번가로 돌아가기": door_shutdown,
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
