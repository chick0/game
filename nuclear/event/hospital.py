from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 정문"
event_id = __name__


def goto_street():
    for text in [
        "당신이 병원을 나가는 순간 병원에 공급되는 전기가 끊어졌습니다.",
    ]:
        print_message(text=text)

    flag.update(event_id, True)
    return "street_no2"


def start():
    print_title(title=title)

    for text in [
        "낡은건지 최신식인지 알 수 없는 병원에 도착했습니다.",
        "지금 생각해보니 이 병원이 넓은건지 좁은건지 알 수 없습니다."
    ]:
        print_message(text=text)

    ev_map = {
        "복도로 들어가기": event.get("hospital_1f"),
        "2번가로 돌아가기": goto_street,
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
