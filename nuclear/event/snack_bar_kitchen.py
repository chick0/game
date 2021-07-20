from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "식당 주방"
event_id = __name__


def event_a():
    print_message(text="냉장고에서 토마토 수프를 발견했다.")
    item.get(["토마토 수프"] * random.choice([1, 1, 1, 2, 2, 3, 4]))


def event_b():
    print_message(text="버려진 사탕을 발견했다.")
    print_message(text="또 그 사탕의 옆에 한 메모가 있었다.")
    print_message(text='"인터넷에서 사탕을 2Kg 사는 것은 나쁜 생각이다..."')
    item.get(["사탕"] * random.choice([3, 3, 3, 4, 5, 6]))


def event_c():
    print_message(text="수건을 발견했다.")
    item.get(["수건"])


def event_d():
    print_message(text="당신보다 빨리 이 식당에 온 사람이 있었나 봅니다.")
    print_message(text="수납장에는 아무것도 없었다.")


def event_e():
    print_message(text="환풍기는 고장 난 듯 아무런 반응을 하지 않습니다.")


def start():
    print_title(title=title)
    for text in [
        "주방 구석에 조그만한 불씨가 보입니다.",
        "여러 곳을 조사하기에는 시간이 부족해보인다."
    ]:
        print_message(text=text)

    flag.update(event.get_event_id("snack_bar"), "burn")

    ev_map = {
        "냉장고": event_a,
        "휴지통": event_b,
        "도마": event_c,
        "수납장": event_d,
        "환풍기": event_e
    }

    choice = player.choice(list(ev_map.keys()))
    ev_map[choice]()

    print_message(text="그때 커져 버린 불씨가 당신을 위협합니다.")

    return None
