from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 1층 안내데스크"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    for text in [
        "안내데스크에는 다양한 서류들이 보입니다.",
        "그리고 그 옆에는 사탕 바구니가 보입니다.",
        "당신은 알 수 없는 서류 대신 사탕 바구니 안에 있는 사탕을 챙깁니다.",
    ]:
        print_message(text=text)

    item.get(["사탕"] * random.choice([2, 2, 2, 2, 3, 3, 4, 4, 5, 6]))

    return None
