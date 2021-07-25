from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 2층 진료실"
event_id = __name__


def start():
    print_title(title=title)
    print_message(text="특별한 물건이 보이지 않습니다.")
    if flag.check(event_id, None):
        print_message(text="그래도 당신은 구석에 있는 사탕을 발견합니다.")
        item.get(["사탕"] * random.choice([1, 1, 2, 2, 3, 4]))
        flag.update(event_id, True)

    return None
