from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "식당 냉동창고"
event_id = __name__


def start():
    print_title(title=title)

    for text in [
        "이 식당은 꽤 오래된 식당이었습니다.",
        "그 사실을 당신은 너무 급한 나머지 까먹고 말았습니다.",
        "거기다가 당신은 정말 어이없을 정도로 큰 실수를 하게 됩니다.",
        "바로 자동으로 닫혀버리는 문을 방치해버린 것 입니다."
    ]:
        print_message(text=text)

    player.dead()
