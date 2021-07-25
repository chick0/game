from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 2층 복도"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event.get_event_id("hospital"), True):
        print_message(text="전기가 끊어진 병원은 엘리베이터가 작동하지 않습니다.")
        return
    else:
        print_message(text="잠긴 계단을 피해 당신은 엘리베이터를 이용해 2층으로 올라왔습니다.")

    ev_map = {
        "1층으로 내려가기": event.get("hospital_1f"),
        "2층 원장실": event.get("hospital_2f_doctor"),
        "2층 진료실": event.get("hospital_2f_doctor_office"),
        "2층 입원실 A": event.get("hospital_2f_ward_a"),
        "2층 입원실 B": event.get("hospital_2f_ward_b"),
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()

