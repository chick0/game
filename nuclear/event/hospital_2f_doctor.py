from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 2층 원장실"
event_id = __name__


def more_check():
    for text in [
        "당신은 호기심을 가지고 원장실을 더 조사하기로 결정합니다.",
        "원장실을 둘러보던중 당신은 벽에 숨어있는 문을 발견합니다.",
        "이 문을 열어볼까 아니면 그냥 나갈까 당신은 고민하기 시작합니다.",
    ]:
        print_message(text=text)

    choice = player.choice(["조사한다", "나간다"])
    if choice == "조사한다":
        event.get("hospital_2f_doctor_hidden")()

    return "hospital_2f"


def back():
    print_message(text="궁금함을 뒤로하고 당신은 원장실에서 나갑니다.")
    return "hospital_2f"


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        print_message(text="원장실을 다시 조사 할 시간이 없습니다.")
        return None
    else:
        flag.update(event_id, True)

    for text in [
        "당신은 원장실에 도착했습니다.",
        "사치스러운 장식물은 없지만 은근히 비싸보이는 물건은 많아 보입니다.",
        "하지만 지금 당신에게 중요한 것은 돈이 아니라는 것을 알고 있습니다.",
        "이 방을 조금만 더 조사하거나 원장실에서 나갈 수 있습니다.",
    ]:
        print_message(text=text)

    ev_map = {
        "조사한다": more_check,
        "나간다": back
    }
    ev_map[player.choice(list(ev_map.keys()))]()

    return None
