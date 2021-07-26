import random

from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "컨테이너 집 욕실"
event_id = __name__


def type_a():
    print_message(text="당신은 세면대에 걸려있는 수건과 세면대 위에 있는 비누를 챙깁니다.")
    item.get(["수건", "비누"])


def type_b():
    choice = random.choice([1, 1, 1, 2])
    if choice == 1:
        print_message(text="당신은 변기 위에 있는 비상 약을 챙깁니다.")
        item.get(["약"])
    else:
        print_message(text="변기에는 특별한 물건이 없습니다.")


def type_c():
    print_message(text="당신은 욕조에 떠있는 오리 인형과 오리 인형이 물고있는 사탕을 챙깁니다.")
    item.get(["인형", "사탕"])


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        print_message(text="욕실을 더 조사하기에는 시간이 부족합니다.")
        return
    else:
        flag.update(event_id, True)

    for text in [
        "커튼을 열고 간단한 욕실을 조사합니다.",
        "세면대와 변기 그리고 욕조가 있습니다.",
    ]:
        print_message(text=text)

    ev_map = {
        "세면대를 조사한다": type_a,
        "변기를 조사한다": type_b,
        "욕조를 조사한다": type_c,
    }
    ev_map[player.choice(list(ev_map.keys()))]()

    return None
