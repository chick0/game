from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 2층 원장실 숨겨진 방"
event_id = __name__


def start():
    print_title(title=title)

    for text in [
        "당신은 숨겨진 방에 도착했습니다.",
        "숨겨진 방에는 쇼파 위에서 조용히 자고있는 원장이 있습니다.",
        "당신은 쇼파 옆 탁자에서 조용히 사탕을 챙깁니다.",
    ]:
        print_message(text=text)

    item.get(["사탕"] * random.choice([2, 3, 3, 3, 4]))
    return None
