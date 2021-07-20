from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "식당 계산대"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    print_message(text="돈이 의미가 없음을 알면서도 이미 계산대에 있는 돈을 훔쳐 간 것 같습니다.")
    print_message(text="그래도 구석에 있는 사탕 하나를 발견했습니다.")
    item.get(["사탕"])

    return
